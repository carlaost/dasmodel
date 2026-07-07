# Figure 2: AD trait association analysis of different cellular subtypes in the TC region

- **Source**: Fig. 2, Gaur et al. (2025), *Nature Communications* 16:10395, doi:10.1038/s41467-025-65350-6, page 5 of 17 (panels rendered on page 4; caption printed on page 5).
- **Caption**: "Fig. 2 | AD trait association analysis of different cellular subtypes in the TC region. a Differential abundance of statistically significant neuronal subpopulations with respect to AD pathology indicated by varying Braak stages in GM and WM obtained using ANCOM-BC, which applies a log-linear regression model to assess proportion differences. Two-sided Z-tests were performed, and p-values were adjusted for multiple comparisons using the Benjamini-Hochberg method. The x-axis represents the estimated log fold-change in the abundance of a subpopulation between different Braak stages, and the y-axis represents subpopulations that were found to be statistically significant after multiple testing corrections. b Box plots of all neuronal subpopulations shown in panel a, representing the distribution of nuclei in each subpopulation with respect to their concerned major cell type (GM and WM samples from n = 36 individuals). c Differential abundance of statistically significant glial subpopulations with respect to AD pathology indicated by varying Braak stages. X and Y axis representations and statistical approach are consistent with panel a. d Box plots of all glial subpopulations shown in panel c, representing the distribution of nuclei in each subpopulation with respect to their concerned major cell type (GM and WM samples from n = 36 individuals). Boxplot: center line = median; box = upper and lower quartiles; whiskers = values within +/- 1.5*IQR (interquartile range); points = outliers beyond whiskers. e Differential abundance of statistically significant subpopulations with respect to sex (male). X and Y axis representations and statistical approach are consistent with panel a. Source data are provided as a Source Data file."
- **Screenshot**: figure2.png (full journal page 4, all 5 panels a-e; caption text is on page 5 and quoted above)
- **Figure type**: quantitative_plot (ANCOM-BC beta-value dot plots in a/c/e; box plots of cell-cluster proportions across Braak-stage tertiles in b/d)
- **Extraction method**: digitized_estimate (panels a, c, e plot per-subcluster beta values as dot/triangle/circle marker positions along a continuous x-axis with no printed numeric labels; positions are read approximately off the axis, marked `≈` below); box-plot y-axis scales in b/d are printed exactly (axis tick labels), but individual quartile/median values are not numerically labeled
- **Reading confidence**: medium (marker shapes/colors and left/right-of-zero direction are unambiguous and match the exact `beta`-sign directionality reported in the Results text and grounded in `logic/claims.md` C01-C03; the exact numeric beta values are not printed on the figure itself)

## Visual description

- **Panel a (Neuronal clusters, dot plot)**: x-axis "beta.values" (range approx. -2 to 2, dashed
  vertical reference line at 0); y-axis lists 13 neuronal subcluster names (top to bottom):
  L5-6_Gluta_THEMIS_POSTN, L5_Gluta_RORB_IL1RAPL2_LINC02196, L5_Gluta_RORB_IL1RAPL2,
  L4-6_Gluta_SPARCL1, L4_Gluta_COL5A2, L3_Gluta_CUX2_GLIS3_COL5A2, L3_Gluta_CUX2_GLIS3,
  L3_Gluta_CUX2_CBLN2_GNAL, L2-4_Gluta_TLL1, Gaba_SST_TRHDE_THSD7B, Gaba_PVALB_TMEM132C,
  Gaba_LAMP5_CHST9, Gaba_PVALB_SPARCL1. Marker legend: color = tissue (teal=GM, orange/yellow=WM);
  shape = Braak-stage contrast (circle = Braak Stage 2-4, triangle = Braak Stage 5-6). Visually:
  L5-6_Gluta_THEMIS_POSTN sits at a positive beta (≈+0.8 to +1, GM triangle) — the only clearly
  positive-beta neuronal row, consistent with its enrichment (C01). All other GM triangles/circles
  sit at negative beta (≈-0.5 to -2), consistent with depletion. The WM circle for
  L5_Gluta_RORB_IL1RAPL2 sits at a positive beta (≈+1, orange), consistent with the opposite-direction
  WM finding in C03 (RORB+/IL1RAPL2+ higher at intermediate Braak stage 2/4 in WM vs. lower in GM at
  late stage).
- **Panel b (Neuronal box plots, GM/WM x Braak-stage tertile)**: A grid of 13 GM box-plot panels (3x
  per row: "% of cells" y-axis, three Braak-stage-tertile boxes colored pale-yellow=0-1,
  teal=2-4, blue=5-6) plus 4 WM box-plot panels (L5_Gluta_RORB_IL1RAPL2, Gaba_PVALB_TMEM132C,
  Gaba_LAMP5_CHST9, Gaba_PVALB_SPARCL1), matching the panel-a subclusters. Visually, most GM panels
  show a monotonic decrease in median % of cells from the 0-1 (pale yellow) to 5-6 (blue) box, except
  L5-6_Gluta_THEMIS_POSTN which shows a monotonic *increase*.
- **Panel c (Glial clusters, dot plot)**: Same axis format as panel a; y-axis lists 6 glial
  subclusters: Peri_TAGLN, Peri_MGP, OPCs_HSPA1A, Micro_AIF1_RPL19, Endo_TSHZ2, Astro_TNC.
  OPCs_HSPA1A shows two positive-beta markers (GM triangle ≈+1.5, WM triangle ≈+1.7); Micro_AIF1_RPL19
  shows two negative-beta markers (GM circle and WM circle both ≈-1.5, clustered together);
  Peri_TAGLN (WM triangle, ≈-0.7), Peri_MGP (GM triangle, ≈+0.5), Endo_TSHZ2 (WM triangle, ≈+0.6),
  and Astro_TNC (GM triangle, ≈+1.3) each show one marker.
- **Panel d (Glial box plots)**: Grid of 4 GM panels (Peri_MGP, OPCs_HSPA1A, Micro_AIF1_RPL19,
  Astro_TNC) and 4 WM panels (Peri_TAGLN, OPCs_HSPA1A, Micro_AIF1_RPL19, Endo_TSHZ2), same
  Braak-stage-tertile coloring as panel b. OPCs_HSPA1A panels (both GM and WM) show a visible
  increase in the upper quartile/outliers at Braak 5-6 from a near-zero baseline (consistent with a
  rare, late-stage-emergent population).
- **Panel e (Sex association, dot plot)**: Title "Sex (Male) association in TC region"; x-axis
  "beta.values" (range approx. -5 to 5); y-axis lists 8 subclusters (Gaba_PVALB_TRPM3,
  Gaba_LAMP5_CHST9, Gaba_SST_TRHDE_THSD7B, L5_Gluta_RORB_TSHZ2, L5_Gluta_RORB_IL1RAPL2,
  L3_Gluta_CUX2_GLIS3_COL5A2, L3_Gluta_CUX2_GLIS3, Oligo_HSPA1A, Endo_EMP1), each with a GM (teal)
  and/or WM (orange) circle marker. This panel is a distinct (sex-covariate, not Braak-stage) analysis
  not directly tied to the paper's AD-pathology claims C01-C14, included in the figure for
  completeness of the ANCOM-BC framework demonstration.

## Data table (qualitative direction read from panel a/c marker positions; exact beta values not printed on figure — see `logic/claims.md` C01-C03 for the paper's own textual statements of direction)

| Subcluster | Tissue | Braak contrast | Beta direction (≈ position) |
|---|---|---|---|
| L5-6_Gluta_THEMIS_POSTN | GM | 5-6 | positive (≈+0.8 to +1) |
| L5_Gluta_RORB_IL1RAPL2_LINC02196 | GM | 5-6 | negative (≈-1) |
| L5_Gluta_RORB_IL1RAPL2 | GM | 5-6 | negative (≈-1.5) |
| L5_Gluta_RORB_IL1RAPL2 | WM | 2-4 | positive (≈+1) |
| L4-6_Gluta_SPARCL1 | GM | 5-6 | negative (≈-1.7) |
| Gaba_PVALB_TMEM132C | GM | 5-6 | negative (≈-0.5) |
| Gaba_PVALB_TMEM132C | WM | 5-6 | negative (≈-0.7) |
| OPCs_HSPA1A | GM | 5-6 | positive (≈+1.5) |
| OPCs_HSPA1A | WM | 5-6 | positive (≈+1.7) |
| Micro_AIF1_RPL19 | GM | 5-6 | negative (≈-1.5) |
| Micro_AIF1_RPL19 | WM | 2-4 | negative (≈-1.5) |
| Astro_TNC | GM | 5-6 | positive (≈+1.3) |

## Trend summary
Panel a/c confirm the direction (sign of beta) of every GM subcluster-Braak association reported
textually in `logic/claims.md` C01/C02: THEMIS+/POSTN+ neurons and OPCs_HSPA1A/Astro_TNC show
positive beta (enrichment) while the remaining neuronal subclusters and Micro_AIF1_RPL19 show
negative beta (depletion). Panel a's WM marker for RORB+/IL1RAPL2+ visually confirms the
opposite-direction (positive-beta, Braak 2-4) WM finding central to claim C03. Panel e is a separate
sex-association analysis, not used to ground any Braak-stage claim in this ARA.
