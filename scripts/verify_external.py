#!/usr/bin/env python3
"""External verification: Send OP tables to Qwen-Max for independent consistency check.
Usage: python3 scripts/verify_external.py
Returns 0 if PASS, 1 if FAIL.
Requires: DASHSCOPE_API_KEY env var
"""
import os, re, json, urllib.request, sys

API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")
if not API_KEY:
    print("❌ DASHSCOPE_API_KEY not set")
    sys.exit(1)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def extract_ops(fname):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    ops = []
    for m in re.finditer(r'(OP\d+[^<]*(?:<(?:td|span|div)[^>]*>)*[^<]*(?:Open|Resolved|Partial|Implemented|RESOLVED)[^<]*)', content):
        clean = re.sub(r'<[^>]+>', ' ', m.group(0))
        clean = re.sub(r'\s+', ' ', clean).strip()
        if len(clean) > 5 and clean not in ops:
            ops.append(clean)
    return ops[:25]

# Build prompt
papers_data = {}
for name, fname in [('Survey', 'Forb_Survey.html'), ('Main', 'Forbidden_Pattern_Functor.html'), ('OP11', 'OP11_Categorical_Unification.html')]:
    fpath = os.path.join(BASE, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        footer = re.findall(r'<div class="footer">(.*?)</div>', content, re.DOTALL)
        papers_data[name] = {
            'ops': extract_ops(fname),
            'footer': re.sub(r'<[^>]+>', ' ', footer[0] if footer else '').strip()[:300]
        }

prompt = """External audit: verify OP (Open Problem) status consistency across 3 Forb series papers.

Known: Survey OP4 (Locality horizon) ≠ Main/OP11 OP4 (Chomsky hierarchy) — these are different OPs with the same number. Do NOT flag this as inconsistency.

Flag ONLY genuine mismatches where the SAME OP has different status in different papers.

Reply in EXACTLY this format:
PASS: <reason>  OR  FAIL: <list each mismatch with file names and statuses>

Papers:
"""
for name, data in papers_data.items():
    prompt += f"\n=== {name} ===\nFooter: {data['footer']}\n"
    for op in data['ops']:
        prompt += f"  {op}\n"

# Call Qwen-Max
req_data = json.dumps({
    "model": "qwen-max",
    "messages": [{"role": "system", "content": "You are an automated OP table verifier. Reply concisely in the exact format specified. No explanations unless you find a FAIL."}, {"role": "user", "content": prompt}],
    "temperature": 0,
    "max_tokens": 500
}).encode()

try:
    req = urllib.request.Request(
        "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions",
        data=req_data,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read())
    verdict = result['choices'][0]['message']['content']
    print(verdict)
    
    if verdict.strip().startswith('PASS'):
        sys.exit(0)
    else:
        sys.exit(1)
except Exception as e:
    print(f"❌ API error: {e}")
    sys.exit(2)
