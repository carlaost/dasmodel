# Breakthrough metric — final 3-signal composite (blind validation)

Two graph signals (uptake, disruption) from `breakthrough_v1_results.json` joined with the new
SIGNIFICANCE signal computed from the GRO L8 sidecars (`compute_significance.py`), combined by
`compute_composite.py`. Everything below is what the code actually printed.

## Labelled set
- **POSITIVES (5)**: lecanemab, donanemab, ptau217, dam_microglia, nia_aa_framework — all carry a
  full GRO L8 shape on disk. All 5 also have graph signals in `breakthrough_v1_results.json`.
- **NEGATIVES (10)**: guo25c, hao25, yu25, ami25, zhu25b, wan25c (GBD burden papers) + raz25, kho25,
  ali26, aks25 (deep-learning / XAI detection papers). All 10 have GRO L8 shapes.

Graph signals for the negatives were recomputed locally with the *identical* v1 CD-index/uptake
logic over the same corpus graph (`refs_raw.json`/`works.json`); this reproduces v1 exactly on the
two overlapping papers (ami25 uptake=3 cd=-0.333; hao25 uptake=6 cd=-0.333).

## Means: POSITIVE vs NEGATIVE

| signal | POSITIVE | NEGATIVE | discriminates? |
|---|---|---|---|
| uptake_per_year | 10.35 | 3.70 | means differ, but **not cleanly** (see below) |
| cd_index (disruption) | -0.446 | -0.470 | **no** (down-weighted, as in v1) |
| **significance (L8)** | **0.731** | **0.223** | **yes, cleanly** |
| composite_z | 0.961 | -0.481 | **yes, cleanly** |
| composite (significance only) | 1.337 | -0.668 | **yes, cleanly** |

## Per-paper (sorted by composite)

| label | name | yr | up/yr | cd | SIG | composite | sig-only | flag |
|---|---|---|---|---|---|---|---|---|
| POS | lecanemab | 2022 | 18.00 | 0.06 | 0.806 | 1.849 | 1.633 | established_downstream |
| POS | donanemab | 2023 | 20.33 | -0.84 | 0.814 | 1.797 | 1.663 | established_downstream |
| POS | nia_aa_framework | 2018 | 5.75 | -0.39 | 0.756 | 0.653 | 1.436 | established_downstream |
| POS | ptau217 | 2020 | 4.00 | -0.67 | 0.753 | 0.429 | 1.422 | established_downstream |
| POS | dam_microglia | 2017 | 3.67 | -0.39 | 0.527 | 0.077 | 0.529 | established_downstream |
| NEG | yu25 | 2025 | 5.00 | -0.20 | 0.278 | -0.202 | -0.451 | not_yet_determined |
| NEG | hao25 | 2025 | 6.00 | -0.33 | 0.251 | -0.209 | -0.560 | not_yet_determined |
| NEG | wan25c | 2025 | 3.00 | -0.33 | 0.336 | -0.297 | -0.223 | not_yet_determined |
| NEG | ami25 | 2025 | 3.00 | -0.33 | 0.326 | -0.315 | -0.263 | not_yet_determined |
| NEG | kho25 | 2025 | 8.00 | -1.00 | 0.160 | -0.399 | -0.920 | not_yet_determined |
| NEG | zhu25b | 2025 | 4.00 | -0.50 | 0.223 | -0.466 | -0.671 | not_yet_determined |
| NEG | guo25c | 2025 | 6.00 | -1.00 | 0.189 | -0.507 | -0.803 | not_yet_determined |
| NEG | aks25 | 2025 | 0.00 | 0.00 | 0.158 | -0.759 | -0.925 | not_yet_determined |
| NEG | ali26 | 2026 | 0.00 | 0.00 | 0.128 | -0.812 | -1.043 | not_yet_determined |
| NEG | raz25 | 2025 | 2.00 | -1.00 | 0.184 | -0.837 | -0.825 | not_yet_determined |

Separation (printed by the code):
- **composite**: min(POS)=0.077 > max(NEG)=-0.202 → **clean**.
- **significance**: min(POS)=0.527 > max(NEG)=0.336 → **clean**.

## Does significance close the v1 "facts-and-figures" Goodhart hole? — Yes.

The v1 hole was that raw citation quantity is gameable by recent, derivative, number-dense papers.
This shows up directly in the table:

- **kho25** (a 2025 XAI review) posts **8.0 citations/yr — higher than three of the five real
  landmarks** (nia_aa 5.75, ptau217 4.00, dam 3.67). On uptake alone it *outranks* p-tau217.
- **aks25** shouts "**99.18% accuracy**" — a Goodhart-perfect number-dense paper — yet every one of
  its deltas is `qualitative_only`/`claimed_unresolved` against **no** source-verified baseline, and
  its contributions are `incremental_improvement`/`synthesis`.

Significance is blind to how many impressive numbers a paper prints; it rewards *verified novelty*.
Both of those papers are floored: **kho25 = 0.160, aks25 = 0.158**, versus a positive floor of
**0.527 (dam_microglia)**. The mechanism: negatives score low on all three L8 sub-signals —
contribution type (synthesis/incremental/low-confidence new_finding, not high-confidence
new_finding/method/paradigm), delta ledger (no `quantified` + `source_verified` deltas; the GBD
papers' quantified deltas are `self_reported` within-paper temporal changes, not comparisons to a
verified prior baseline), and sota anchor (empty or `compiler_estimated`, penalized). So the
composite no longer credits number density — the hole is closed for this labelled set.

## Does the composite separate positives from negatives? — Yes, but read the caveat.

The composite gives clean separation (min POS 0.077 > max NEG -0.202). **However, essentially all of
the separating power comes from significance, not uptake.** The `composite (significance only)`
column — which drops the uptake term entirely — separates *just as cleanly and more widely*
(POS 1.337 vs NEG -0.668). Meanwhile the individual signals show:

- **cd_index does not discriminate** (POS -0.446 vs NEG -0.470; lecanemab is the only positive with
  positive disruption). This confirms the v1 finding; it is kept at 10% weight only for reporting.
- **uptake_per_year discriminates on the mean but not cleanly** — kho25 (8.0) and hao25 (6.0),
  both negatives, beat three positives — so on its own it would mis-rank.

## Recency confound (stated honestly, not hidden)

Every positive is 2017–2023 and flagged `established_downstream`; **every negative is 2025–2026 and
flagged `not_yet_determined`.** No negative is old enough to have `failed_to_become` — none has aged
past the young-window, so their empty/thin downstream is *undetermined*, not *failed*. Consequently
the uptake term of the composite is age-confounded: positives simply had years to accumulate
citations that the negatives have not. The honest conclusion is that **significance — computed
entirely from the age-independent L8 shape — is the real discriminator here, and the composite is
trustworthy on this labelled set primarily because of it.** A fair future test needs age-matched
negatives (2017–2023 papers that were derivative) before the uptake/disruption half of the
composite can be credited with separating breakthroughs from non-breakthroughs.
