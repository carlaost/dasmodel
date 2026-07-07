# Evidence Index

Source: Xu et al. (2025), "Epidemiological and sociodemographic transitions in the global burden and risk factors for Alzheimer's disease and other dementias: a secondary analysis of GBD 2021." *International Journal for Equity in Health* 24:149, doi:10.1186/s12939-025-02530-2. Grounding: full-text (Open Access, CC-BY 4.0), 15-page PDF main text.

## Tables (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Table 1 | [tables/table1.md](tables/table1.md) | Incidence cases and ASIR of ADOD in 1990/2010/2021 and 1990-2021 ETPC, by sex, SDI region, super region, and GBD region | C01, C02, C03, C11, C13 | `tables/table1.png` |
| Table 2 | [tables/table2.md](tables/table2.md) | Joinpoint analysis (EAPC per segment, AAPC overall) for ASIR, ASDR, ASR-DALYs, by SDI region, 1990-2021 | C02, C06, C07, C08 | `tables/table2.png` |

## Figures (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Figure 1 | [figures/figure1.md](figures/figure1.md) | Joinpoint-segmented ASIR trend lines by sex and SDI region, 1989-2022, with printed per-segment APC legends | C02, C03 | `figures/figure1.png` |
| Figure 2 | [figures/figure2.md](figures/figure2.md) | Country-level (204 countries, 2021) scatter of SDI vs. ASIR/ASDR/ASR-DALYs by sex, with mean-trend and quantile-regression fits | C04, C05 | `figures/figure2.png` |
| Figure 3 | [figures/figure3.md](figures/figure3.md) | Sex-specific ASDR attributable to smoking/high BMI/high FPG, globally and by SDI region, 1990-2021 line trends | C09, C10 | `figures/figure3.png` |
| Figure 4 | [figures/figure4.md](figures/figure4.md) | Full exact-value heatmap: sex-specific ASDR attributable to smoking/high BMI/high FPG, by global/5 SDI quintiles/21 regions, 1990 and 2021 | C09, C10 | `figures/figure4.png` |

## Accounted-for omissions

- The paper's main text (this 15-page PDF) references a separate **Supplementary Material** file (per §Supplementary Information: "The online version contains supplementary material available at https://doi.org/10.1186/s12939-025-02530-2. Supplementary Material 1.") containing **Table S1, Table S2 (implied), Table S3, and Figure S1 through Figure S7**, none of which were provided as input to this ARA compilation. These supplementary objects are referenced in the main text for: female-specific ASIR by SDI region (Fig. S1); ASIR rank-by-SDI-region over time (Fig. S2); death-case/ASDR breakdown by sex (Table S1, Fig. S3); DALY breakdown by sex (Table S3, Fig. S4); the 21-region RCS-spline SDI association (Fig. S5); risk-factor-attributable DALY trend lines (Fig. S6); and risk-factor-attributable DALY heatmap (Fig. S7, the DALY analogue of main-text Fig. 4). Numbers from these objects that are also stated directly in the main-text prose are captured in `logic/claims.md` (grounded in the main-text sentence, not independently re-verified against the missing table/figure); this is noted explicitly in each affected claim (C01, C05, C08, C12, C13) rather than silently treated as fully verified.
- No other numbered table or figure appears in the main text beyond Table 1, Table 2, Figure 1, Figure 2, Figure 3, and Figure 4 — this is a complete, ordered sweep of the main-text PDF's numbered evidence objects.

## Screenshot rendering notes

- Figures 1-3 and Tables 1-2 screenshots were rendered from `paper.pdf` using PyMuPDF (`fitz`) by a prior compilation pass (kept as-is; verified complete and accurate against the source PDF during this compilation).
- Figure 4's screenshot (`figures/figure4.png`) was likewise already rendered from page 11 of `paper.pdf`; this compilation pass added the full data transcription (`figures/figure4.md`), which was not yet written. All 486 cells (18 rows x 27 columns) of the heatmap carry printed numeric labels and were transcribed at `exact_from_labels` confidence, cross-validated against two in-text values (High-income North America 2021 High-FPG: 5.92 female / 5.34 male, matching the heatmap's rounded 5.9/5.3 at the same row/column position).

## Note on unverifiable / flagged figures

- **C13 (Central Sub-Saharan Africa mortality ETPC)**: The Discussion states a 1990-2021 mortality ETPC of 14.82% for Central Sub-Saharan Africa. This number cannot be checked against a main-text table (it depends on the unprovided Table S1) and numerically coincides with an unrelated value elsewhere in the paper: Table 1 shows −14.82(−19.55,−10.2) as *Australasia's* 1990-2021 *incidence* ASIR ETPC, while Central Sub-Saharan Africa's own Table 1 incidence ETPC is −0.59(−3.02,1.79). Reported as an observed coincidence in `logic/claims.md` C13 and `trace/exploration_tree.yaml` N14, not asserted as a confirmed source error.
