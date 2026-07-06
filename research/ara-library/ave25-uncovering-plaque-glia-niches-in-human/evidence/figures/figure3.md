# Figure 3: Differential effects of low vs. high Aβ on the local transcriptome
- **Source**: Figure 3, Page 12 of 23
- **Caption**: "Differential effects of low vs. high Aβ on the local transcriptome. A Schematic of
  the three contrasts tested. Aβ and glia graphics created with BioRender.com (B) Volcano plot of
  low vs. high Aβ. Genes with FDR-adjusted p < 0.05 in purple. C Scatterplot of Aβ effects
  stratified by glia-low or glia-high. Genes with FDR-adjusted p < 0.05 in red and blue for
  glia-low and glia-high conditions, respectively. D Venn diagram showing the number of DEGs found
  across Aβ contrasts. E GSEA enrichment of Aβ contrasts showing GO terms and canonical pathways
  (*p < 5e-4, **p < 5e-5, ***p < 5e-6) (F) GSEA enrichment of Aβ contrasts for relevant genesets
  (*p < 5e-2, **p < 5e-3, ***p < 5e-4). PIG31: plaque-induced genes, OLIG31: oligodendrocyte gene
  module, DAM32: disease-associated microglia, DAA33: disease-associated astrocytes; MG0-12:
  microglia states in human AD brains8. G Boxplots of representative genes for each Aβ contrast
  (LMM, FDR-corrected; *p < 0.05, ***p < 5e-4). H Images of representative plaques from FFPE tissue
  sections stained with DAPI (blue), Aβ (4G8; yellow), NEUN (cyan), and cleaved Caspase 3 (magenta)
  (scale bar = 25 um). I Average number of Caspase 3 puncta within NEUN + nuclei (left) or total
  nuclei (right) in the area within and surrounding plaques. Points represent average values from >
  100 ROIs for each of 10 AD individuals (paired t-test; *p = 0.041, **p = 2.61e-4)"
- **Screenshot**: figure3.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (panel D Venn counts, panel I p-values are printed data
  labels; panels B/C/E/F/G are quantitative plots without fully legible individual data labels at
  this resolution, so read qualitatively/by rank; panel A/H are diagrams/qualitative images)
- **Reading confidence**: high (panels A, D, H, I); medium (panels B, C, E, F, G — gene/pathway
  identities and significance tiers are legible; exact numeric coordinates/NES values are not)

## Visual description (Panel A - diagram)
- **Components**: Three schematic contrast boxes: "combined" (low Aβ plaque vs. high Aβ plaque,
  no glia distinction), "glia-low" (low- vs. high-Aβ plaques both with minimal surrounding glia),
  "glia-high" (low- vs. high-Aβ plaques both with abundant surrounding glia).
- **Connections**: Each box shows a "vs." comparison arrow between a smaller/diffuse Aβ deposit
  (low Aβ) and a larger/dense Aβ deposit (high Aβ), with glia cartoon icons present/absent per row.
- **What it conveys**: Defines the three DEG contrasts analyzed in panels B-G (combined, glia-low,
  glia-high), each testing low-Aβ vs. high-Aβ spots.

## Data table (Panel D - Venn diagram of DEG overlap, quantitative)
| Region | Genes (p<5e-4) |
|---|---|
| "low vs. high Aβ (combined)" only | 37 |
| "low vs. high Aβ (glia-low)" only | 106 |
| "low vs. high Aβ (glia-high)" only | 87 |
| combined ∩ glia-high only | 38 |
| glia-low ∩ glia-high only | 16 |
| combined ∩ glia-low only | 0 |
| all three (combined ∩ glia-low ∩ glia-high) | 18 |

## Trend summary (Panel D)
Total unique genes across the three low-vs-high-Aβ contrasts (at p<5e-4, a looser threshold than
the FDR<0.05 used for the headline 93/140/159 DEG counts in the main text) = 37+106+87+38+16+0+18 =
302. Only 18 genes (6% of the union) are shared across all three contrasts, confirming that glial
context substantially reshapes which genes respond to Aβ load (supports C01).

## Data table (Panel I - caspase-3 quantification, quantitative_plot)
- **Plot kind**: box plot (two panels: "CASP3+/NEUN+ nuclei within plaque ROI" and "CASP3+/all
  nuclei within plaque ROI")
- **Axes**: X = Aβ stratum (low Aβ, high Aβ), Y = average CASPASE3+ count (proportion), linear scale

| Metric | low Aβ (≈median) | high Aβ (≈median) | Significance |
|---|---|---|---|
| CASP3+/NEUN+ nuclei proportion | ≈0.60-0.65 | ≈0.45-0.50 | *p = 0.041 |
| CASP3+/all nuclei proportion | ≈0.50 | ≈0.45 | **p = 2.61e-4 |

Median values are digitized estimates (≈) read off the box-plot midlines; the p-values themselves
are exact, printed data labels (also confirmed in main text, Page 13 of 23).

## Trend summary (Panel I)
Both apoptosis metrics are higher near low-Aβ plaques than high-Aβ plaques across n=10 AD
individuals (paired design, >100 ROIs per individual), directly supporting claim C02.

## Visual description (Panel H - qualitative_sample)
- **Shows**: Representative FFPE plaque images (DAPI/4G8-Aβ/NeuN/cleaved-Caspase-3 merge and
  individual channels) for a low-Aβ vs. a high-Aβ plaque.
- **Demonstrates**: Visually more numerous caspase-3+ puncta co-localizing with NeuN+ nuclei
  surrounding the low-Aβ plaque than the high-Aβ plaque.
- **Supports**: C02.

## Visual description / partial data (Panels B, C, E, F, G - volcano/scatter/GSEA heatmaps/boxplots)
- **Panel B (volcano, low vs. high Aβ combined)**: Named significant genes (FDR<0.05, purple)
  include THEMIS, SEMA3E, NR4A2, OPRK1 (upregulated toward "low" per the effect-size axis
  direction) and COL5A2, CDH8, SLC30A3, NEFH, GABRD, NEFM, LY6H, SYT13 (upregulated toward "high").
  Axis: X = effect size (low <-> high, linear, range ≈ -0.6 to 0.6), Y = -log10(p) (linear, range
  0-9).
- **Panel C (scatter, glia-low vs. glia-high stratified Aβ effects, r=0.34, p=0.00)**: X = t-value
  low-vs-high Aβ (glia-low), Y = t-value low-vs-high Aβ (glia-high); named genes with the largest
  effects in one or both strata include SEMA3E, PEG10, KCNIP2, ADAM10, SFRP2, C3AR1, DAB1, ICAM1,
  C1QB, SERPINE2 (glia-high-associated) and POU3F1, CDH8, MEF2C, GABRD, SYT13, HAPLN4, COL5A2
  (glia-low-associated). The printed correlation r=0.34 (p=0.00, i.e., p<computational precision)
  is an exact reported value.
- **Panel E (GSEA of GO terms/pathways, heatmap, signed -log10(p) scale -6 to 6)**: Rows =
  synapse, synaptic signaling, voltage-gated channel activity, ion transport, neurofibrillary
  tangle, intermediate filament bundle assembly, collagen-containing ECM, cell adhesion,
  gliogenesis, apoptotic process, immune system development; columns = combined/glia-low/glia-high
  Aβ contrasts. Qualitative pattern: synapse/ion-transport terms are negatively enriched (blue)
  especially under glia-high; ECM/cell-adhesion/apoptosis/immune terms are positively enriched
  (red/orange) especially under glia-high and glia-low respectively (ECM stronger in glia-low,
  apoptosis/immune stronger in glia-high) — individual cell -log10(p) values are not legible at
  render resolution.
- **Panel F (GSEA of curated gene modules, heatmap, signed -log10(p) scale 0-25+)**: Columns = PIG,
  OLIG, DAM, DAA (left block) and MG0-MG12 human microglia states (right block); rows =
  combined/glia-low/glia-high Aβ contrasts. Qualitative pattern: PIG/OLIG/DAM/DAA all positively
  enriched (blue-green, low-to-moderate -log10(p)) across all three row-contrasts; MG3 column shows
  the visually brightest (highest, yellow) enrichment across all three rows, consistent with the
  main-text statement that MG3 is the strongest-enriched state; MG0/MG1 show minimal/no enrichment
  (dark blue).
- **Panel G (gene-level boxplots, 9 genes x 3 contrasts)**: Neuronal/synaptic genes NEFH, NEFM,
  SYT13 (top row) and SYNGR1, SLC17A6, GABRD (middle row) show lower normalized expression in
  "low Aβ" than "high Aβ" bars across combined/glia-low/glia-high (significance stars up to
  ***p<5e-4); apoptosis gene CIDEA and immune/apoptosis genes SFRP2, SEMA3E (right column) show
  higher normalized expression in "low Aβ" than "high Aβ" bars, most pronounced under glia-high.
  Exact expression values are not transcribed (arbitrary normalized-expression y-axis units without
  printed data labels); qualitative direction and significance tier are read directly from the
  figure.

## Trend summary (Panels B, C, E, F, G combined)
Collectively these panels support C01 (distinct, largely non-overlapping low-vs-high-Aβ DEG sets
depending on glia context), C02 (lower neuronal/synaptic, higher apoptosis-gene expression in
low-Aβ spots), and C04 (convergent enrichment of PIG/OLIG/DAM/DAA modules and human MG states, MG3
strongest, across all three Aβ contrasts).
