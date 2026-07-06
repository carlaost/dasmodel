# Figure 4: Aβ plaques influence intercellular communication
- **Source**: Figure 4, Page 14 of 23
- **Caption**: "Aβ plaques influence intercellular communication. A Differential ligand-receptor
  (LR) interaction genes between low Aꞵ vs. high Aꞵ (y-axis) and low Aꞵ vs. no Aꞵ spots (x-axis).
  Each dot corresponds to an LR pair tested; the axis represents the t-statistics from linear
  mixed model tests accounting for repeated donors. Significant LR pairs (FDR < 0.05) are
  highlighted in red (low Aꞵ vs. high Aꞵ only), blue (low Aꞵ vs. no Aꞵ only), or purple
  (significant in both comparisons). B Selected Gene Ontology terms enrichment from LR
  differentially expressed in low Aꞵ vs. no Aꞵ and low Aꞵ vs. high Aꞵ. Both ligand and receptor
  genes were considered for the enrichment analysis. P-values were adjusted using the g:SCS method
  from gprofiler. Colors in the heatmap represent the signed -log10(adj. P). *p ≤ 0.05, **p ≤ 0.01,
  ***p ≤ 0.001. C Representative Sect. (17_D) image colored by normalized expression of selected
  differentially expressed LR gene pairs. All the statistical analyses were performed on gray
  matter spots only"
- **Screenshot**: figure4.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (panel A correlation R/p is a printed value; gene/LR
  pair identities and significance tiers in panels A/B are legible; panel C is a qualitative
  spatial image)
- **Reading confidence**: high (panel A correlation, named genes); medium (panel B individual
  heatmap cell values)

## Data table (Panel A - LR differential expression scatterplot, quantitative_plot)
- **Plot kind**: scatter
- **Axes**: X = t-statistic, low Aβ vs. no Aβ (linear, range ≈ -10 to 8), Y = t-statistic, low Aβ
  vs. high Aβ (linear, range ≈ -6 to 8)

| Statistic | Value |
|---|---|
| Pearson R (low-vs-no-Aβ t-stat vs. low-vs-high-Aβ t-stat) | 0.85 |
| p-value | < 2.2e-16 |

Both values are printed directly on the panel (exact_from_labels).

Named LR pairs with large effects in both contrasts (purple, "Both Signif"): ITGA7-CD151,
VWF-SIRPA, RIMS1-SLC17A7, HLA-A-APLP2, HLA-C-CD81, HLA-DRA-CD63, TGFA-ADAM17, ITGA3-CD63
(all negative on both axes) and SLITRK1-TNFRSF11B, LRRC4B-PTPRS, SLC7A5-THBS1, CD99-PILRA,
APP-TSPAN12, GAD1-GRM4, ADAM10-IL6R, APP-SLC45A3 (positive on both axes).
Named LR pairs specific to low-vs-high-Aβ only (red): LRPAP1-LSR, C1QA-CD93, L1CAM-ERBB2,
AGT-LRP2, C1QA-CSPG4, LPL-GPIHBP1, APOE-LRP5, GNAI2-S1PR3, LRPAP1-LRP2, SPP1-ITGA9, QDPR-DYSF.
Named LR pairs specific to low-vs-no-Aβ only (blue): APOE-SORL1, LRPAP1-SORL1, APP-DCC, APP-VLDLR,
SPP1-ITGAV-ITGB5, APOE-LDLR, APOE-VLDLR, ATP1A3-AGRN, APP-GRM7.
Named LR pairs negative on both axes ("Both Signif", further down): GRM5-EFNB2, LRRC4B-PTPRF,
GRM1-EFNB2, SLC6A8-LIFR, JAG2-NOTCH2, IL34-PTPRZ1, FGF2-FGFR3, LAMB3-DAG1, CD99-CD99L2, SLIT3-ROBO2.

## Trend summary (Panel A)
Strong positive correlation (R=0.85) between the low-vs-no-Aβ and low-vs-high-Aβ LR contrasts,
directly supporting claim C06's statement of a "positive association" between these two contrasts.
Named LR pairs recur across categories related to synapses (RIMS1-SLC17A7), vesicle/lipoprotein
transport (APOE-SORL1/LDLR/VLDLR, LRPAP1-SORL1/LRP2, APP-DCC/VLDLR), and immune/complement
(C1QA-CD93/CSPG4, HLA-DRA-CD63), consistent with claim C06's description of synapse/neuron/ECM and
vesicle-transport/immune LR involvement.

## Visual description (Panel B - GO enrichment heatmap, quantitative but not individually legible)
- Rows: neurogenesis, neuron differentiation, axonogenesis, axon guidance, cell adhesion, synapse
  organization, regulation of cell migration, cell motility, positive regulation of cell migration,
  semaphorin-plexin signaling pathway, vasculature development, focal adhesion, collagen-containing
  extracellular matrix, apoptotic process, extracellular matrix, wound healing, vesicle-mediated
  transport, regulation of MAPK cascade.
- Columns: low Aβ vs. no Aβ; low Aβ vs. high Aβ.
- Qualitative pattern: Neurogenesis/neuron-differentiation/axonogenesis/axon-guidance/cell-adhesion/
  synapse-organization/cell-migration/focal-adhesion/ECM terms are all strongly negatively enriched
  (blue, roughly -20 to -40 signed -log10(p)) in both columns (almost all marked ***). Apoptotic
  process, extracellular matrix, and wound healing are positively enriched (light red/orange, small
  magnitude, * to **) in one or both columns. Vesicle-mediated transport and regulation of MAPK
  cascade are positively enriched (light red, *) specifically in the low-vs-high-Aβ column.
  Individual numeric -log10(p) values are not legible at render resolution; only sign/significance
  tier and relative magnitude are read.

## Trend summary (Panel B)
The dominant signal is strong negative enrichment (downregulation) of neurodevelopmental/synaptic/
adhesion GO terms among differentially expressed LR genes in low-Aβ spots relative to both no-Aβ
and high-Aβ spots, consistent with a synaptic/neuronal-degeneration interpretation (supports C06).

## Visual description (Panel C - qualitative_sample / spatial expression images)
- **Shows**: A representative tissue section (17_D) with six small paired spatial expression maps,
  each showing one ligand (L) and its paired receptor (R) gene's normalized expression across the
  section: APP(L)/DCC(R), LRPAP1(L)/SORL1(R), APOE(L)/SORL1(R), CD99(L)/CD99L2(R), C1QA(L)/CSPG4(R),
  LRRC4B(L)/PTPRF(R), each with its own 0-max color-scale legend (max values range from 2 to 17
  depending on gene).
- **Demonstrates**: Spatial co-localization patterns of specific ligand-receptor pairs implicated
  in the Aβ-load LR contrasts (e.g., APP/DCC showing complementary/overlapping spatial expression
  patterns across gray/white matter boundaries).
- **Supports**: C06.
