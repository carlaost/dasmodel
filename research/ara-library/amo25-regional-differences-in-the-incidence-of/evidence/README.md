# Evidence Index

Grounding: **full-text** compile from `paper.pdf` (open-access CC-BY, Frontiers in Neurology, 12 pages). Every numbered Table (1–3) and Figure (1–7) in the source is filed below with BOTH a markdown transcription and a `.png` screenshot of the rendered region. No numbered object was omitted.

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1.md](tables/table1.md) | Table 1, §Results (Sociodemographics), p.4 | C04 | Sociodemographic characteristics (N and %) overall and by PHR: ADRD subtype, age group, sex, race |
| [tables/table2.md](tables/table2.md) | Table 2, §Results (ADRD-specific incidence), p.8 | C01, C02, C03 | Pairwise IRRs (Poisson) with p-values/95% CIs comparing crude and type-specific incidence across PHRs |
| [tables/table3.md](tables/table3.md) | Table 3, §Results (Age-specific incidence), p.9 | C05 | Type-specific incidence per 100,000 by PHR × age group, with population at risk |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1.md](figures/figure1.md) | Figure 1, §Methods, p.3 | C04 | Participant-flow diagram: 377,143 registry records → N = 18,955 analytic sample; regional partition |
| [figures/figure2.md](figures/figure2.md) | Figure 2, §Results, p.5 | C01 | Choropleth: crude ADRD incidence by county (class breaks 386–1148/100k) |
| [figures/figure3.md](figures/figure3.md) | Figure 3, §Results, p.5 | C01 | Choropleth: crude ADRD incidence by PHR (Midlands 684, Low Country 764, Upstate 840, Pee Dee 896) |
| [figures/figure4.md](figures/figure4.md) | Figure 4, §Results, p.6 | C02 | Choropleth: AD incidence by PHR (Midlands 555, Low Country 620, Upstate 655, Pee Dee 727) |
| [figures/figure5.md](figures/figure5.md) | Figure 5, §Results, p.6 | C03 | Choropleth: VaD incidence by PHR (Midlands 38, Low Country 41, Pee Dee 50, Upstate 59) |
| [figures/figure6.md](figures/figure6.md) | Figure 6, §Results, p.7 | C03 | Choropleth: Mixed dementia incidence by PHR (Midlands 11, Pee Dee 16, Low Country 18, Upstate 24) |
| [figures/figure7.md](figures/figure7.md) | Figure 7, §Results, p.7 | C03 | Choropleth: Other dementia-type incidence by PHR (Midlands 80, Low Country 84, Pee Dee 102, Upstate 102) |

## Evidence completeness
All 3 tables and 7 figures in the main text are filed (10/10). No numbered object skipped or duplicated.

## Referenced-but-not-in-input supplementary material
The article cites **Supplementary Table 1** (missing-data associations: Cramér's V for age-group and ADRD-specific diagnosis) and **Supplementary Figure 1** (extreme-case sensitivity analysis) in the Sensitivity-analyses section. These live in the online supplement (https://www.frontiersin.org/articles/10.3389/fneur.2025.1584127/full#supplementary-material) and are **not part of the provided PDF input**, so no evidence file was extracted for them. The in-text values they report (Cramér's V = 0.15 and 0.12; sex V = 0.018; ~20.6% underestimation) are captured in claims.md C06 with their in-text source, not from the supplement itself.

## Notes on source discrepancies (reproduced verbatim, not corrected)
- Table 2: VaD "Low Country vs. Upstate" CI printed as "(0.94–0.850)" (lower > upper) — likely typo; AD "Pee Dee vs. Upstate" p printed "<0.0002".
- Figure 1: the five terminal region/disposition boxes sum to 18,755, not 18,955 (200 short).
- Table 3 vs prose: 75–84 "Midlands lowest across all types" is not exact for AD and Other (Low Country lower); Discussion's <65 "Pee Dee highest for AD/VaD/Mixed" contradicts Table 3 (Upstate highest for AD and Mixed). See table3.md and claims.md C05.
