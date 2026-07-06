# Figure 6: Plaque-surrounding reactive glia modifies intercellular communication
- **Source**: Figure 6, Page 17 of 23
- **Caption**: "Plaque-surrounding reactive glia modifies intercellular communication. A
  Differential ligand-receptor (LR) genes between glia-high vs. glia-low under High Aꞵ spots
  (y-axis) and glia-high vs. glia-low under low Aꞵ spots (x-axis). Each dot corresponds to an LR
  pair tested; the axis represents the t-statistics from linear model tests accounting for
  repeated donors. Significant LR pairs (FDR < 0.05) are highlighted in blue (glia-high vs.
  glia-low under low Aꞵ only), yellow (glia-high vs. glia-low under high Aꞵ only), or green
  (significant in both comparisons). B Example Sect. (15_D) colored by normalized expression of
  selected differentially expressed LR gene pairs. All the statistical analyses were performed on
  gray matter spots only. C Normalized expression levels by stratified spot groups for selected
  differentially expressed LR pairs. (*p ≤ 0.05, **p ≤ 0.01, ***p ≤ 0.001). D Selected Gene
  Ontology terms enrichment from LR differentially expressed between glia-high vs. glia-low under
  low Aꞵ, high Aꞵ, and combined were considered for the enrichment of both ligand and receptor
  genes. P-values were adjusted using the g:SCS method from gprofiler. Colors in the heatmap
  represent the signed -log10(adj. P) (*p ≤ 0.05, **p ≤ 0.01, ***p ≤ 0.001)"
- **Screenshot**: figure6.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (panel A correlation R/p printed; panel C significance
  stars printed; panel D heatmap read qualitatively)
- **Reading confidence**: high (panel A correlation, named genes, panel C significance);
  medium (panel D individual cell values)

## Data table (Panel A - LR differential expression scatterplot, quantitative_plot)
- **Plot kind**: scatter
- **Axes**: X = t-statistic, glia-high vs. glia-low (low Aβ), linear (range ≈ -5 to 3); Y =
  t-statistic, glia-high vs. glia-low (high Aβ), linear (range ≈ -6 to 6)
- **Printed statistic**: R = 0.41, p < 2.2e-16 (exact, printed on panel)

Named LR pairs positive on both axes ("Both Signif" analog / high-Aβ-specific, blue-labeled):
SPARC-ENG, APOE-LDLR, APP-TSPAN15, GFAP-APLNR, KCNAB1-ENG, CALM3-GRM7, RTN4-RTN4R,
PLXNA1-TREM2, GSTO1-RYR1, DBP-ACKR1, CLU-TREM2. Named LR pairs specific to low-Aβ (yellow):
SEMA6D-PLXNC1, SPARC-FGFR1, PTPRD-SLITRK4, ECM1-CACHD1, MET-SEMA4D. Named LR pairs negative on
both axes (green, "significant in both"): SEMA6D-PLXNA1, CD47-SCN1B, GNB3-GABBR2,
TNFRSF14-LRFN5, RPH3A-NRXN1, SLIT2-PLXNA1, DSCAM-DCC. Named LR pairs high-Aβ-specific,
bottom-right region (blue): ADAM15-ITGAV, APLN-GRM7, CORT-GRM7, TGFB1-ITGAV, CXCL16-GRM7,
NRG1-EGFR, CFC1-ACVR1B, RIMS1-SLC17A7.

## Trend summary (Panel A)
Moderate positive correlation (R=0.41) between the low-Aβ and high-Aβ glia-contrast LR
t-statistics, directly matching claim C07's "positive correlation (R=0.41)" statement. Named LR
pairs recur for synaptic signaling (RPH3A-NRXN1, RIMS1-SLC17A7, GNB3-GABBR2, DSCAM-DCC — all
negative, i.e., downregulated in glia-high) and for immune/TREM2 signaling (CLU-TREM2,
PLXNA1-TREM2) and ECM (SPARC-ENG) specifically in the high-Aβ-positive region, matching claim C07.

## Data table (Panel C - normalized expression by stratified group, quantitative_plot, 12 LR pairs)
- **Plot kind**: box plot (12 sub-panels, one per LR pair)
- **Axes**: X = stratified spot group (combined/low Aβ/high Aβ, each split glia-high vs.
  glia-low — 6 bars per panel), Y = normalized expression, linear scale (range varies per gene,
  approx. 9-13)

| LR pair | Pattern (glia-high vs. glia-low) | Significance (combined / low Aβ / high Aβ) |
|---|---|---|
| GFAP-APLNR | Higher in glia-high for combined/low-Aβ; markedly higher in high-Aβ glia-high | *** across |
| SPARC-ENG | Higher in glia-high, most pronounced in high-Aβ | ** / * / *** |
| CLU-TREM2 | Higher in glia-high specifically for high-Aβ | * (high Aβ only, others n.s.-like) |
| RPH3A-NRXN1 | Higher in glia-high across all three (downregulation direction differs from panel-A sign convention) | ** / * / *** |
| APP-TSPAN15 | Slightly higher in glia-high for high-Aβ | ** (high Aβ) |
| PLXNA1-TREM2 | Higher in glia-high for high-Aβ | * / *** |
| DSCAM-DCC | Higher in glia-high across all three | *** / * / *** |
| TGFB1-ITGAV | Higher in glia-high for high-Aβ | *** (high Aβ) |
| APOE-LDLR | Higher in glia-high for high-Aβ | *** (high Aβ) |
| GNB3-GABBR2 | Higher in glia-high across all three | * / ** / — |
| RIMS1-SLC17A7 | Higher in glia-high across all three | * / — / *** |
| CXCL16-GRM7 | Higher in glia-high across all three | * / — / ** |

Exact expression values are not transcribed (no printed numeric data labels); direction and
significance tier are read directly from the figure at medium-high confidence.

## Visual description (Panel B - qualitative_sample / spatial expression images)
- **Shows**: Representative tissue section (15_D) colored by normalized expression, with two
  paired maps: GFAP(L)/APLNR(R) and SPARC(L)/ENG(R), each with its own 0-max intensity legend
  (max 52 and 5 respectively for the first pair's L/R panels; max 5 and 2 for the second pair);
  plus RPH3A(L)/NRXN1(R) and APP(L)/TSPAN15(R) maps (max 5/5 and 12/2 respectively).
- **Demonstrates**: Spatial co-localization of selected differentially expressed LR pairs
  implicated in the glia-abundance contrasts.
- **Supports**: C07.

## Visual description (Panel D - GO enrichment heatmap, quantitative but not individually legible)
- Rows: axonogenesis, neuron differentiation, neurogenesis, synapse, cell adhesion, extracellular
  matrix organization, synapse organization, integrin cell surface interactions, ECM proteoglycans,
  semaphorin-plexin signaling pathway, cell migration, vesicle, ion binding, epithelial cell
  proliferation, neuron cell-cell adhesion, extracellular vesicle, autophagy, blood vessel
  development, vasculature development, signaling by NOTCH, downregulation of TGF-beta receptor
  signaling, clathrin-mediated endocytosis, myelination; columns = glia-high vs. glia-low (low Aβ /
  high Aβ / combined). Qualitative pattern: axonogenesis/neuron-differentiation/neurogenesis/
  synapse/cell-adhesion terms strongly negative (blue, roughly -20 to -40) across all three
  columns; ECM-organization/integrin/proteoglycan/vesicle/autophagy/vasculature/NOTCH/TGF-beta-
  downregulation terms positive (orange/red), concentrated in the "combined" column; myelination
  slightly negative (light blue) in the low-Aβ column only.

## Trend summary (Panel D)
Glia-high spots show coordinated downregulation of neurodevelopmental/synaptic GO terms among
differentially expressed LR genes (paralleling Fig. 4B's Aβ-contrast pattern), plus a distinct
ECM-reorganization/vesicle-trafficking signature most prominent in the combined contrast,
supporting C07 and the main-text statement of "more substantial LR differences in the high Aβ
condition."
