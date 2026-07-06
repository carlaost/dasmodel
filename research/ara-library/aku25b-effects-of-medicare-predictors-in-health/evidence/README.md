# Evidence Index

Full-text compile from `paper.pdf` (11 pages, Europe PMC PMC11982180 / PMID 40225237, open access
CC BY-NC). Every numbered table and figure in the source is filed below with a markdown
transcription and a rendered screenshot (`.png`). The paper contains **4 tables (Table 1–4) and 1
figure (Figure 1)** in the main text. Table 4 spans two pages (continuation on p. 8); a second
screenshot `table4_continued.png` preserves the continued rows.

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1.md](tables/table1.md) | Table 1, §3 (p. 4) | C05 | Study sample: individuals at baseline and AD cases over 5-year follow-up, by age cohort and subpopulation. |
| [tables/table2.md](tables/table2.md) | Table 2, §3 (p. 5) | C02, C03 | Subpopulation-specific baseline prevalence (%) of the 7 predictors. |
| [tables/table3.md](tables/table3.md) | Table 3, §3 (p. 6) | C03, C04 | AD hazard ratios (paired) per predictor and disparity, multivariable Cox model. |
| [tables/table4.md](tables/table4.md) | Table 4, §3 (pp. 7-8) | C01, C02, C03, C05, C06 | Total = exposure x vulnerability effects per predictor, plus observed and unexplained disparity, for all six disparities. |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1.md](figures/figure1.md) | Figure 1, §3 (p. 8) | C02, C05, C06 | Observed disparity (solid), unexplained part (open dots), and low-income-adjusted curve (dashed) across baseline age, for six panels (BW, WN, HW, WA, FM, SB). |

## Notes on completeness
- **No proofs directory**: the decomposition is an algebraic derivation captured in
  `logic/solution/method.md` (Eqs. 1–6), not a formal theorem; no separate proof object is filed.
- **Supporting-information objects not filed**: the paper references supplementary Table S1 (full
  10-disease candidate list), Table S2 (top-40 highest effects), and Table S3 (sensitivity-analysis
  estimates). These are **not present in the provided main-text PDF** and were not extractable; they
  are noted where relevant (concepts, study_design, claims C07/C08) but not filed as evidence.
- **Screenshots**: `table4.png` shows the p. 7 block; `table4_continued.png` shows the p. 8
  continuation (female–male renal/heart-failure/depression rows + full stroke-belt block).
- **Evidence-completeness**: all 4 numbered tables and the 1 numbered figure of the main text are
  filed with both markdown and PNG. No numbered object was omitted.
- **Extraction fidelity**: table cell values transcribed verbatim (exact, unrounded) from
  high-resolution page renders (verified visually). Figure 1 point series equal the exact Observed/
  Unexplained values in Table 4; the dashed low-income series is an ARA-computed product marked `≈`.
