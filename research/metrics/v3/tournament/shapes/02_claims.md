# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 2. `logic/claims.md` (falsifiable claims)

### Artifact + path
`logic/claims.md`, e.g. `research/ara-library/huu25-apoe-e4-alzheimer-s-risk-converges/logic/claims.md`.

### Purpose
The paper's testable, falsifiable assertions — the "what the paper actually claims to have shown,"
stripped of narrative hedging, each traceable to a specific experiment and a specific number's exact
source location. This is the highest-value file for downstream agents deciding whether to trust or
build on the paper's findings.

### Structure
One `## C{NN}: {Short title}` block per claim (`C01`, `C02`, ... zero-padded two digits, more digits
if >99). Every block has ALL of these fields (Seal Level 1 fails a block missing any):

| Field | Type | Real example |
|---|---|---|
| `**Statement**` | markdown-prose, precise & falsifiable, numbers copied exactly (never rounded) | `"For detecting amyloid-beta (Abeta) positivity, mass-spectrometry-derived p-tau217 (p217_MS) achieved the highest rank (P-score = 0.859), followed by ..."` |
| `**Status**` | enum{`hypothesis`, `supported`, `refuted`} (can carry a parenthetical qualifier) | `supported` — or `supported (interpretation-limited by female sample size)` |
| `**Falsification criteria**` | markdown-prose: what observation would disprove this | `"Refuted if, under the same NMA on independent cohorts, p181_IA or another isoform outranked p217_MS for Abeta detection, or if p217_MS's AUC advantage over p181_IA were non-significant (95% CI crossing 0)."` |
| `**Proof**` | list[ref-id] — experiment IDs only (`E01`, `E02`, ...), never file paths | `[E01]` |
| `**Evidence basis**` | markdown-prose: exactly what the cited evidence directly shows | `"Table 2 Outcome 1 P-scores (p217_MS 0.859 > p217_Ratio 0.783 > ...); Figure 3A forest plot MDs vs. p181_IA."` |
| `**Interpretation**` | markdown-prose, optional broader synthesis kept separate from `Evidence basis` | `"All p-tau217 variants and the ratio significantly outperform the older p-tau181 immunoassay standard, which the authors argue is effectively obsolete..."` |
| `**Dependencies**` | list[ref-id] of other claim IDs, or `none` | `[C01]` or `none` |
| `**Sources**` | list of grounding entries (see below) | see below |
| `**Tags**` | comma-separated string list | `p-tau217, mass spectrometry, amyloid-beta, AUC, P-score, ranking` |

**`Sources` entry format** (one per load-bearing number in `Statement`), a hard requirement (Rule 16 /
the "Grounding discipline"):
```
`<value>` ← <file-or-section-ref> (<locator>) «<verbatim matched line>» [input|result]
```
- `<value>` — the exact number/string as it appears in the Statement, in backticks.
- `<file-or-section-ref>` — either a repo-relative evidence path (`evidence/tables/table2.md`) or a
  paper section (`§3.6`, `§4.2`).
- `«...»` — a **verbatim quote** copied from the cited location; a bare path with no quote is invalid
  and must fail validation.
- `[input]` — tags a value that was *set* (e.g. a config/recipe value); `[result]` tags a value a
  run/analysis *produced* (the overwhelmingly common tag in claims).
- `[pending: ...]` is allowed in place of a verified quote only when the source genuinely could not be
  opened this turn — it is honesty, not a shortcut, and is flagged for follow-up.

### A full realistic example

```markdown
## C01: p-tau217 by mass spectrometry has the highest diagnostic accuracy for amyloid-beta pathology
- **Statement**: For detecting amyloid-beta (Abeta) positivity, mass-spectrometry-derived p-tau217
  (p217_MS) achieved the highest rank (P-score = 0.859), followed by the p-tau217 ratio (p217_Ratio,
  P-score = 0.783) and ALZpath-based p-tau217 immunoassay (p217_ALZpath, P-score = 0.686); standard
  p-tau181 immunoassay (p181_IA) ranked last (P-score = 0.117). In the forest plot vs. the p181_IA
  baseline, p217_MS had a mean AUC difference of MD = 0.10 (95% CI 0.04-0.16).
- **Status**: supported
- **Falsification criteria**: Refuted if, under the same NMA on independent cohorts, p181_IA or
  another isoform outranked p217_MS for Abeta detection, or if p217_MS's AUC advantage over p181_IA
  were non-significant (95% CI crossing 0).
- **Proof**: [E01]
- **Evidence basis**: Table 2 Outcome 1 P-scores (p217_MS 0.859 > p217_Ratio 0.783 > p217_ALZpath
  0.686 > p217_Lumi 0.667 > p217_IA 0.412 > p217_Lilly 0.331 > p231_UGOT 0.145 > p181_IA 0.117);
  Figure 3A forest plot MDs vs. p181_IA.
- **Interpretation**: All p-tau217 variants and the ratio significantly outperform the older
  p-tau181 immunoassay standard, which the authors argue is effectively obsolete for high-precision
  diagnostics.
- **Dependencies**: none
- **Sources**:
  - `0.859` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 1) «p217_MS (0.859)» [result]
  - `0.783` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 2) «p217_Ratio (0.783)» [result]
  - `0.686` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 3) «p217_ALZpath (0.686)» [result]
  - `0.117` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 8) «p181_IA (0.117)» [result]
  - `0.10 (95% CI 0.04-0.16)` ← evidence/figures/figure3.md (Figure 3A) «p217_MS ... 0.10 [ 0.04; 0.16]» [result]
- **Tags**: p-tau217, mass spectrometry, amyloid-beta, AUC, P-score, ranking
```

### Cardinality / variability
Typically 5–8 claims per ARA (Seal Level 1 requires ≥1; the compiler's own convention aims higher but
never pads). `Dependencies` chains commonly reference an earlier "anchor" claim (e.g. C01) from
several later claims. RCT/clinical-trial ARAs tend to have claims phrased around primary/secondary
endpoints and hazard ratios; meta-analyses phrase claims around pooled P-scores/rankings; lab/omics
papers phrase claims around DEG counts and pathway enrichment (see huu25's C01: `"679 upregulated and
343 downregulated genes at FDR<0.05"`). `Status` skews heavily to `supported` in practice because
compilers extract what the paper reports as its findings; `hypothesis`/`refuted` appear for stated
ablations or explicitly disconfirmed prior expectations.

### Availability notes
`claims.md` is mandatory core — it is never entirely absent. What varies, and what a penalizing
metric should watch for:
- **Missing `Sources` entries or bare paths with no «quote»** — an automatic Seal Level 1 failure;
  in a "thin" or rushed compilation this is the single most common defect.
- **`Interpretation` collapsing into `Evidence basis`** (no separation of raw support from broader
  reading) — a quality defect the validation checklist explicitly watches for via
  "Evidence-limited wording" (Rule 10).
- **Reviews/meta-analyses**: claims often carry an extra editorializing clause (e.g. "effectively
  obsolete") that is the *authors'* interpretive gloss rather than a directly measured quantity — a
  well-compiled ARA still grounds the ranking fact but should not smuggle the value-judgment in as if
  it were equally grounded (see che26 C08, flagged in its own `grounding_findings.yaml` review with
  `context_match: false` for exactly this reason).
- **Abstract-only / paywalled sources**: claims degrade to only what the abstract states — few claims,
  each with weak "Evidence basis" (often just `§Abstract`) since section-level detail can't be
  grounded; this must read as materially thinner than a full-text compilation, not silently equal.

---

