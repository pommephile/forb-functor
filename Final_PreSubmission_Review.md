# 投稿前最終チェックレポート — Forb シリーズ（7本）

**査読者:** Claude  
**査読日:** 2026-06-25  
**対象ファイル（7本）:**
1. `Forbidden_Pattern_Functor.html` — メイン（2845行）
2. `Forb_Functor_Tower.html` — 物理スケール（347行）
3. `Forb_PA_Godel.html` — PA/Gödel（316行）
4. `Forb_LLM_Constrained_Decoding.html` — LLM（517行）
5. `Forb_Survey.html` — サーベイ（373行）
6. `Forb_Topological_Grammar.html` — 位相的特徴（432行）
7. `OP11_Categorical_Unification.html` — 圏論的統合（731行）

*除外: `Forb_Spectrum_Classification.html`（インダス文字論文）*

---

## ✅ 前回指摘の最終確認

| 問題 | 状態 |
|---|---|
| R-1: Tower §12.2「monotonic increase」 | ✅ 修正済 |
| C-7: Main paper Finding 1-12 未番号 | ✅ **完全修正済** — FINDING 1-16 すべて明示番号付き（line 2040 注記：「All 16 Findings are now sequentially numbered」）|
| N-1: Survey vs OP11 の OP3 不整合 | ✅ 修正済 |
| N-5: Theorem 1 DEDUCTIVE タグ | ✅ 修正済（STRUCTURAL + 複合注記）|
| N-6: Topological Grammar ナビリンク | ✅ 修正済（OP11 リンク追加）|
| V-1: §2.2 forbidden bigrams/Dowker の概念混在 | ⚠️ 部分修正（Definition 1b 参照明示、但し後述）|
| N-3: β₁/\|V\| per-vertex 表現 | ⚠️ 部分修正 |

---

## 新規指摘

### FIN-1. OP2 クロスペーパー不整合 [HIGH] ★ 再発パターン

**場所:**

| ファイル | OP2 の記述 |
|---|---|
| `Forb_Survey.html` §6 + 現状表 | **✓ Resolved (§6)** — Theorem 4 (Feature Dimension Bound) を提示 |
| `Forb_Survey.html` フッター | **OP2, OP3, OP4 (Locality horizon), OP10, OP11: Resolved.** |
| `OP11_Categorical_Unification.html` OP table | **Open** |
| `Forbidden_Pattern_Functor.html` OP2 セクション | **Open 問題のまま** — `[RESOLVED]` マークなし |

これは N-1（OP3）と完全に同型の再発（3回目）。Survey を更新した際に OP11 および Main paper に連携しなかった。

**修正:**
1. `OP11_Categorical_Unification.html` OP table: `Open` → `✓ Resolved (Survey §6, Theorem 4)`
2. `Forbidden_Pattern_Functor.html` line 2424: `<div class="num">OP2 — ...` を `<div class="num">OP2 — ... <strong>[RESOLVED — see Survey §6, Theorem 4 (Feature Dimension Bound)]</strong>` に更新

---

### FIN-2. Main paper の Resolved OP に [RESOLVED] マークがない [HIGH]

**場所:** `Forbidden_Pattern_Functor.html` OP セクション（§7）

OP1 のみ `[RESOLVED for i.i.d. sampling — Theorem 3.3]` と明示されているが、他の解決済み OP にはマークがない：

| OP | Main paper の状態 | 実際の解決状況 |
|---|---|---|
| OP1 | ✅ `[RESOLVED...]` あり | 解決済 |
| OP2 | ❌ Open 議論のまま | Survey §6 で解決 |
| OP3 | ❌ Open 議論のまま | Forb_Topological_Grammar で解決 |
| OP5 | ❌ Open 議論のまま | Trigram verified（Survey 表では Resolved）|
| OP10 | ❌ Open 議論のまま（サブ問 (a)–(e) は引き続き Open と明記） | コア結果は §6.8.1 で解決 |

読者が Main paper の OP セクション（§7）だけを読むと、OP2/OP3/OP5/OP10 がすべて Open に見える。

**修正:** OP1 に倣い、各 OP のヘッダーに `[RESOLVED — see ...]` を追加：
- OP2: `[RESOLVED — see Survey §6, Theorem 4]`
- OP3: `[RESOLVED — see Forb_Topological_Grammar.html]`
- OP5: `[RESOLVED — trigram extension verified]`
- OP10: `[RESOLVED (core result) — see §6.8.1, Theorem 6.2; sub-questions (a)–(e) remain]`

---

### FIN-3. ナビゲーションリンクが Topological Grammar 以外に存在しない [HIGH]

**場所:** 全7論文のフッター

| ファイル | フッターのナビリンク |
|---|---|
| `Forb_Topological_Grammar.html` | ✅ 4本リンクあり |
| `Forb_Survey.html` | ❌ リンクなし |
| `Forbidden_Pattern_Functor.html` | ❌ リンクなし |
| `Forb_Functor_Tower.html` | ❌ リンクなし |
| `Forb_PA_Godel.html` | ❌ リンクなし |
| `Forb_LLM_Constrained_Decoding.html` | ❌ リンクなし |
| `OP11_Categorical_Unification.html` | ❌ リンクなし |

7本シリーズとして提出するならば、各論文から Survey と Parent paper へのナビゲーションリンクは最低限必要。Topological Grammar が手本となっている。

**最小修正案:** 全論文のフッターに以下を追加：
```html
<a href="Forb_Survey.html">Survey</a> ·
<a href="Forbidden_Pattern_Functor.html">Parent paper</a>
```
（各論文固有の関連論文リンクは任意）

---

### FIN-4. Survey の全 Theorem が epistemic status タグを持たない [MEDIUM]

**場所:** `Forb_Survey.html` Theorem 1–4

Survey の Theorem ボックスは `<span class="tag">THEOREM</span>` のみを使用しており、他の論文で用いる `.status-DEDUCTIVE` / `.status-STRUCTURAL` / `.status-EMPIRICAL` タグが付いていない。特に Theorem 3（Bifunctor B）は OP11 Limitation 4 で「pipeline isomorphism は fully constructive ではない」と認められており、THEOREM ラベルが過大に見える。

**修正:** Theorem 1–2 には `DEDUCTIVE`、Theorem 3 には `STRUCTURAL`、Theorem 4 には `DEDUCTIVE` の status タグを追加すること。

---

### FIN-5. V-1 残存：§2.2「forbidden bigrams correspond to absent 1-simplices」[MEDIUM]

（v4 レポートより持ち越し）

`Forb_Topological_Grammar.html` §2.2 line 191:
> "forbidden bigrams correspond to absent 1-simplices"

Dowker complex K_D（Definition 1b）の absent 1-simplex は「同一語内に一切共起しない phoneme ペア」であり、forbidden bigrams（隣接ペアとして出現しない）とは異なる条件。前者は後者より strictly stronger。

**修正:** 「absent 1-simplices in K_D correspond to phoneme pairs that never co-occur within any word — a stronger condition than forbidden adjacency」のような表現に置き換えること。

---

## 軽微な残存指摘（LOW）

| ID | 場所 | 内容 |
|---|---|---|
| E-2 | `Forb_Functor_Tower.html` Axiom A | `.theorem` CSS クラス（赤枠）のままだが EMPIRICAL タグは付いている。CSS クラスを `.finding` か `.empirical` に変更推奨 |
| N-3 | `Forb_Topological_Grammar.html` §2.1 | 「many independent 1-dimensional homology classes **per vertex**」に per-vertex 表現が残存 |
| STAT-1 | `Forb_Functor_Tower.html` | フッターに entity カウント統計なし |
| STAT-2 | `Forb_PA_Godel.html` | フッターに entity カウント統計なし |

---

## 総評

### 優先度マトリクス

```
投稿前に必須修正（ブロッカー）:
  FIN-1  OP2 クロスペーパー不整合（OP11 table + Main paper OP section）
  FIN-2  Main paper OP2/OP3/OP5/OP10 の [RESOLVED] マーク欠落
  FIN-3  全論文へのナビゲーションリンク追加

投稿前に推奨修正:
  FIN-4  Survey Theorem epistemic status タグ
  FIN-5  §2.2 forbidden bigrams / Dowker の記述精度

軽微（投稿後修正可）:
  E-2, N-3, STAT-1, STAT-2
```

### シリーズ全体の数学的健全性

過去4ラウンドの査読を通じて、致命的な数値誤り・論理的矛盾・データで否定された主張はすべて修正されました。Finding 1–16 の番号付けも完了しています。残存問題はすべて **記述・ナビゲーション・OP同期** の問題であり、数学的な主張の正確性には影響しません。

FIN-1〜FIN-3 の3点を修正すれば **投稿可能** と判断します。

---

**最終査読終了**
