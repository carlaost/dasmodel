# Evidence Index

This paper contains 3 numbered tables and 5 numbered figures (main text; no appendix/supplementary tables or figures were included in the supplied PDF beyond a textual reference to a "Supplemental Material" section for the APOE genotyping method and "Supplementary Methods" for equipment/supplies — neither of which contains its own numbered table/figure objects in the 48-page PDF provided). All 8 numbered objects are filed below — a complete, in-order sweep.

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1.md](tables/table1.md) | Table 1, PDF p.40 | C01 (context) | Participants' demographic, cognitive, and biomarker characteristics, all (N=145) vs. CU (n=79) vs. CI (n=66) |
| [tables/table2.md](tables/table2.md) | Table 2, PDF p.41 | C11, C12 | VeraBIND Tau result and % positivity, cross-tabulated by clinical status (CU/CI) and A/T group (A-T-, A+T-, A+T+, A-T+) |
| [tables/table3.md](tables/table3.md) | Table 3, PDF p.42 | C01, C03 | Sensitivity/specificity/accuracy/PPV/NPV of VeraBIND Tau vs. plasma pTau217 (3 thresholds), entire sample and CU/CI subgroups |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1.md](figures/figure1.md) | Figure 1, PDF p.43 | (mechanism, all claims) | Diagram of the VeraBIND Tau assay's 9-step reaction pipeline and molecular binding schematic |
| [figures/figure2.md](figures/figure2.md) | Figure 2, PDF p.44 | C01, C02 | ROC curves (5 biomarkers) predicting tau-PET status (panel A) and amyloid status (panel B), with printed AUCs |
| [figures/figure3.md](figures/figure3.md) | Figure 3, PDF p.45–46 | C04, C05, C06 | VeraBIND Tau score and pTau217 concentration by Braak-like tau-PET stage group (coarse and fine-grained), with printed % positivity tables |
| [figures/figure4.md](figures/figure4.md) | Figure 4, PDF p.47–48 | C08 | Six scatter panels correlating VeraBIND Tau score with MMSE, episodic memory, tau-PET SUVr (×2 regions), pTau217, pTau181 |
| [figures/figure5.md](figures/figure5.md) | Figure 5, PDF p.48 | C10 | Individual longitudinal VeraBIND Tau score trajectories by Braak-like stage group, with converters highlighted |

## Notes on Completeness
- No numbered table/figure was omitted. All 3 tables and 5 figures present in the source are filed above.
- No derived/subset evidence files were created; all filed objects faithfully reproduce their full original source table/figure (no rows or panels were dropped).
- Two transcription anomalies are flagged rather than silently corrected (both are internal inconsistencies present in the source PDF itself, not introduced by this compile):
  1. In Table 3, the CU-subgroup NPV cell at the 0.256 pg/mL pTau217 threshold prints as "91.5%" with an adjacent CI of "92.2 – 97.4" — the CI's lower bound exceeds the point estimate. See the footnote in `tables/table3.md`.
  2. In the Results text (PDF p.20), the pTau217 sensitivity figure for the 0.193 pg/mL threshold in the Braak-like 1-3 group (n=17) is reported as "41.2% (n=7/11)" — 7/17=41.2% is arithmetically correct for this group, while 7/11=63.6% is not. See the flagged note in `logic/claims.md` Claim C04.
