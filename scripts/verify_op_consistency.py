#!/usr/bin/env python3
"""Forb series: verify all OP tables are consistent across papers.
Exits 0 if consistent, 1 if mismatch found.
Run before every commit. Hook install: scripts/install_hooks.sh
"""
import os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAPERS = {
    'Survey':    os.path.join(BASE, 'Forb_Survey.html'),
    'Main':      os.path.join(BASE, 'Forbidden_Pattern_Functor.html'),
    'OP11':      os.path.join(BASE, 'OP11_Categorical_Unification.html'),
}

# Expected OP resolution status (source of truth: Survey footer)
# Format: OP number -> expected status
EXPECTED = {
    'OP1':  'Resolved',
    'OP2':  'Resolved',
    'OP3':  'Resolved',
    'OP4':  'Open',
    'OP5':  'Resolved',
    'OP6':  'Implemented',
    'OP7':  'Partial',
    'OP8':  'Implemented',
    'OP9':  'Open',
    'OP10': 'Resolved',
    'OP11': 'Resolved',
}

def check_file(name, path):
    """Check a single file's OP status against expected."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    
    # Check every OP in cross-reference tables and OP headers
    for op_num, expected in EXPECTED.items():
        # Find OP status mentions
        patterns = [
            re.compile(rf'{op_num}\s*\((\w+)\)', re.IGNORECASE),  # "OP2 (Open)"
            re.compile(rf'{op_num}[^<]*\[RESOLVED', re.IGNORECASE),  # "[RESOLVED"
        ]
        
        found_statuses = set()
        for pat in patterns:
            for m in pat.finditer(content):
                if 'RESOLVED' in m.group(0).upper():
                    found_statuses.add('Resolved')
                else:
                    found_statuses.add(m.group(1) if m.lastindex else m.group(0))
        
        # Check: if status is expected to be Resolved, no "Open" should appear
        if expected == 'Resolved':
            if 'Open' in found_statuses:
                errors.append(f"  {op_num}: expected Resolved, found Open in {name}")
    
    return errors

def main():
    all_errors = []
    for name, path in PAPERS.items():
        if os.path.exists(path):
            errs = check_file(name, path)
            all_errors.extend(errs)
    
    if all_errors:
        print("❌ OP TABLE INCONSISTENCY DETECTED:")
        for e in all_errors:
            print(e)
        print("\nFix: update OP tables in ALL files before committing.")
        print("See: skill forb-op-table-sync")
        sys.exit(1)
    else:
        print("✅ All OP tables consistent across Survey / Main / OP11")
        sys.exit(0)

if __name__ == '__main__':
    main()
