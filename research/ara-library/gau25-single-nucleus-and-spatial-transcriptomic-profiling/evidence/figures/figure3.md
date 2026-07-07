# Figure 3: Differential expression analysis at cell type level

- **Source**: Fig. 3, Gaur et al. (2025), *Nature Communications* 16:10395, doi:10.1038/s41467-025-65350-6, page 7 of 17 (panels rendered on page 6; caption printed on page 7).
- **Caption**: "Fig. 3 | Differential expression analysis at cell type level. a Number of differentially expressed genes per cell type when compared across Braak stages using a false discovery rate (FDR) of 5%. b Differentially expressed genes with the largest log fold change for each cell type at late Braak stage (5-6) vs early Braak stage (0-1). '*' indicates statistical significance at a false discovery rate (FDR) of < 5%, based on a two-sided Wald test. c Pathway enrichment of differentially expressed genes, examining pathways specifically associated with AD genes. The color of the dot reflects NES, which refers to the Normalized Enrichment Score (NES) for Gene set enrichment analysis, whereas the size refers to the absolute value of NES. d LOEUF score (a measure of gene constraint) for differentially expressed genes in glutamatergic neurons (GM and WM samples from n = 39 individuals). p-values are derived from two-sided Wilcoxon rank-sum tests. No multiple testing correction was applied. e Pathway enrichment (10% FDR) of differentially expressed genes in pathways specifically associated with AD genes (20% FDR). The color and size of the dots are the same as in c. f Expression of NPTX2 in Glutamatergic neurons at different Braak stages. g Expression of FCER1G in Microglia at different Braak stages and in GM vs WM. h Expression of APOE in endothelial cells at different Braak stages and in GM vs WM. For (f-h), Boxplot: center line = median; box = upper and lower quartiles; whiskers = values within +/- 1.5*IQR; points = individual data with outliers beyond whiskers. GM and WM samples from n = 39 individuals with varying Braak stages. Differential expression was assessed using a negative binomial mixed model (glmmTMB) fitted separately for each cell type. Two-sided Wald tests were performed, and p-values were adjusted for multiple comparisons using the Benjamini-Hochberg method. i Differentially expressed genes affected in a different manner between GM and WM that belong to pathways associated with AD genes (5% FDR, denoted by '*'). Source data are provided as a Source Data file."
- **Screenshot**: figure3.png (full journal page 6, all 9 panels a-i; caption on page 7 quoted above)
- **Figure type**: mixed (panel a = bar chart with exact printed gene counts; panel b = heatmap, diagram-like; panels c/e/i = pathway-enrichment dot/heatmap plots; panel d = violin/dot plot with exact printed p-values; panels f-h = box plots with exact printed adjusted p-values)
- **Extraction method**: exact_from_labels (panels a, d, g, h have numeric values printed directly on the image); digitized_estimate (panel b heatmap color intensities and panels c/e/i pathway dot sizes/colors are read qualitatively, not digitized to exact NES values)
- **Reading confidence**: high (panels a, d, g, h — all values printed and directly legible); medium (panels b, c, e, i — color-coded, non-numeric)

## Visual description

- **Panel a (DEG counts, exact_from_labels)**: Two side-by-side sub-panels ("Braak stage effect" and
  "Tissue specific Braak stage effect"), each split into a top ("Braak 2-4" / "Braak 2-4 * Temporal
  Cortex") and bottom ("Braak 5-6" / "Braak 5-6 * Temporal Cortex") row, with horizontal stacked bars
  per cell type, red = up, blue = down, x-axis "Number of genes (5% FDR)". Printed values:
  - **Braak 2-4 (early, main effect)**: GABAergic 8 (down) / 5 (up); OPCs 1 (down) / 2 (up);
    Oligodendrocytes 1 (down only, no up bar shown).
  - **Braak 2-4 x Temporal Cortex (early, tissue-interaction)**: Astrocytes 5 (down) / 3 (up);
    Pericytes 1 (down only); Glutamatergic 1 (down only).
  - **Braak 5-6 (late, main effect)**: Glutamatergic 260 (down) / 297 (up); Oligodendrocytes 102
    (down) / 351 (up); GABAergic 88 (down) / 44 (up); Astrocytes 35 (down) / 39 (up); Endothelial 3
    (down) / 3 (up); Pericytes 2 (down) / 3 (up); Microglia 2 (one bar only, direction not
    distinguishable from the printed label alone); OPCs bar present but too small for a printed
    number.
  - **Braak 5-6 x Temporal Cortex (late, tissue-interaction)**: Glutamatergic 141 (down) / 165 (up);
    Oligodendrocytes 98 (down) / 82 (up); Microglia 31 (down) / 30 (up); Endothelial 26 (down) / 22
    (up); OPCs 16 (down) / 9 (up); Astrocytes 4 (down) / 7 (up); GABAergic 4 (down) / 6 (up);
    Pericytes 2 (one bar only, small).
- **Panel b (heatmap, diagram-like)**: "Braak 5-6" heatmap, genes (rows, ~40 genes grouped in blocks
  e.g. ARMC3/C6orf118/DRC1/FOXJ1/LINC02251; ARNTL2/DIO2/FAM117B/PREX1/SNAPC3; CARTPT/NPTX2/SCGN/
  SV2C/VGF; FANK1/NEDD4; AP001025.3/FAP/OR2M4/RELN/RGPD2; AC012409.2/ASAP2/GLRX3/SEC63/TRIB2; etc.)
  x cell types (Astrocytes, Endothelial, GABAergic, Glutamatergic, Microglia, Oligodendrocytes, OPCs,
  Pericytes), color = log2FC (red=up to +3, blue=down to -3), asterisk = FDR<5% significance in that
  cell type. FOXJ1 shows a strong red (upregulated) cell in Astrocytes column; PVALB and RELN rows
  visible with strong color in their respective columns (matching text: PVALB down in GABAergic,
  RELN up in Oligodendrocytes).
- **Panel c (pathway enrichment dot plot, Braak 5-6, all cell types)**: y-axis pathway names
  (Clathrin coat assembly; Negative regulation of amyloid fibril formation; Clathrin binding;
  Phospholipid binding; Positive regulation of catalytic activity; Negative regulation of signaling;
  Low density lipoprotein particle binding; Cellular response to lipid; Signaling receptor binding);
  x-axis cell types; dot color = NES (red=positive/up, blue=negative/down), dot size =|NES|, filled
  circle border = significant at 10% FDR. "Negative regulation of amyloid fibril formation" shows a
  large blue (negative NES) significant dot in GABAergic; "Phospholipid binding" a red dot in
  Microglia; "Cellular response to lipid" a red dot in OPCs — matching the text (C08).
- **Panel d (LOEUF violin/dot plot, exact_from_labels)**: Two grouped panels ("Braak 5-6" and
  "Braak 5-6 * Temporal Cortex"), each with 3 columns (Up / Down / FDR>=5%) of jittered dot+violin
  distributions of LOEUF score (y-axis 0-2.5+); bracket p-values printed exactly: Braak 5-6 Up-vs-
  FDR>=5% = **3.5e-09**; Braak 5-6 Down-vs-FDR>=5% = **0.95**; Braak5-6*Temporal Cortex Up-vs-FDR>=5%
  = **1.8e-05**; Braak5-6*Temporal Cortex Down-vs-FDR>=5% = **0.0083**.
- **Panel e (pathway enrichment dot plot, Braak5-6*Temporal Cortex, 10% FDR)**: Same format as c but
  for the tissue-interaction contrast; y-axis pathways include "Negative regulation of amyloid
  fibril formation," "Leukocyte transendothelial migration," "Endocytosis," "Regulation of vesicle
  mediated transport," "Kinase binding," "Clathrin coat assembly," "Cellular response to lipoprotein
  particle stimulus," "Apolipoprotein a i binding," "Apolipoprotein binding," "Regulation of amyloid
  fibril formation." Astrocytes column shows multiple large red (positive NES, significant) dots
  ("Endocytosis," "Kinase binding," "Regulation of vesicle mediated transport" — matching C08's GM
  astrocyte endocytosis/kinase-binding enrichment); Microglia/Oligodendrocytes columns show blue
  (negative NES) dots for "Clathrin coat assembly" and lipoprotein-related terms.
- **Panels f, g, h (gene-level box plots, exact_from_labels for p-values)**:
  - f: NPTX2 in Glutamatergic neurons, y-axis "Log2(CPM+1)" (0-10), x-axis Braak stage (0-1/2-4/5-6);
    bracketed comparison p-values printed: 0.4 (0-1 vs 2-4) and **0.00089** (0-1 vs 5-6); visibly
    decreasing median across the three stages.
  - g: FCER1G in Microglia, y-axis "Log2(CPM+1)" (0-8), x-axis Braak stage x tissue (WM=solid,
    GM=dashed outline per legend); printed **"adjusted P-value = 4.5e-07"**; GM boxes visibly lower
    than WM boxes at Braak 5-6 (concordant with text: FCER1G lower in GM, higher in WM at late stage).
  - h: APOE in Endothelial cells, y-axis "Log2(CPM+1)" (6-10), x-axis Braak stage x tissue; printed
    **"adjusted P-value = 0.04"**; both GM and WM boxes decrease from Braak 0-1 to 5-6, with a visibly
    larger drop in GM (dashed) than WM (solid).
- **Panel i (tissue-interaction pathway/gene heatmap, Braak5-6*Temporal Cortex, 5% FDR)**: Genes
  (rows, each annotated with its GO/pathway term in parentheses, e.g. "APOE (Regulation of amyloid
  fibril formation, Negative regulation of amyloid precursor protein catabolic process)", "FCER1G
  (Fc epsilon receptor signaling pathway, Receptor internalization)", "ABCA7 (Negative regulation of
  amyloid precursor protein catabolic process, Amyloid precursor protein metabolic process)",
  "THEMIS (Antigen receptor mediated signaling pathway, Activation of immune response)") x cell
  types, color = log2FC, asterisk = FDR<5% significant in that cell type/gene combination. APOE row
  shows an asterisked cell in Endothelial column; FCER1G row shows an asterisked cell in Microglia
  column — both directly corroborating the C06 statements.

## Data table (panel a — exact printed DEG counts per cell type per Braak contrast)

| Cell type | Braak 2-4 down/up | Braak 5-6 down/up | Braak2-4*TC down/up | Braak5-6*TC down/up |
|---|---|---|---|---|
| Glutamatergic | — | 260 / 297 | 1 / — | 141 / 165 |
| Oligodendrocytes | 1 / — | 102 / 351 | — | 98 / 82 |
| GABAergic | 8 / 5 | 88 / 44 | — | 4 / 6 |
| Astrocytes | — | 35 / 39 | 5 / 3 | 4 / 7 |
| Endothelial | — | 3 / 3 | — | 26 / 22 |
| Pericytes | — | 2 / 3 | 1 / — | 2 / (unlabeled) |
| Microglia | — | 2 (unresolved direction) | — | 31 / 30 |
| OPCs | 1 / 2 | (bar present, no printed value) | — | 16 / 9 |

## Trend summary
Panel a's printed per-cell-type counts sum to **1229** for the Braak 5-6 main-effect contrast
(260+297+102+351+88+44+35+39+3+3+2+3+2 = 1229) and **643** for the Braak5-6*Temporal-Cortex
interaction contrast (141+165+98+82+31+30+26+22+16+9+4+7+4+6+2 = 643) — both within 1 gene of the
paper's own stated totals of **1230** and **644** DEGs respectively (`logic/claims.md` C05, C06), a
self-consistency check whose 1-gene shortfall is attributable to the unlabeled small OPCs bar (main
effect) / Pericytes bar (interaction effect) too small to print a numeric value on the figure. Panel
d's exact p-values (3.5e-09, 0.95, 1.8e-05, 0.0083) directly ground C07; panels g/h's exact adjusted
p-values (4.5e-07, 0.04) directly ground C06's FCER1G/APOE statements.
