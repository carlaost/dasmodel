# Figure 5: Differential effects of glia abundance on the local transcriptome
- **Source**: Figure 5, Page 15 of 23
- **Caption**: "Differential effects of glia abundance on the local transcriptome. A Schematic of
  the three contrasts tested. Aβ and glia graphics created with BioRender.com (B) Volcano plot of
  glia-high vs. glia-low. Genes with FDR-adjusted p < 0.05 in green. C Scatterplot of glia effects
  stratified by low or high Aβ. Genes with FDR-adjusted p < 0.05 in yellow and blue for low and
  high Aβ conditions, respectively. D Venn diagram on the number of DEGs found across glia
  contrasts. E GSEA enrichment of glia contrasts for GO terms and canonical pathways (*p < 5e-4,
  **p < 5e-5, ***p < 5e-6). F GSEA enrichment of glia contrasts for Aβ/glia-relevant genesets
  (*p < 5e-2, **p < 5e-3, ***p < 5e-4). PIG31: plaque-induced genes, OLIG31: oligodendrocyte gene
  module, DAM32: disease-associated microglia, DAA33: disease-associated astrocytes; MG0-12:
  microglia states in human AD brains8. G Boxplot of representative genes found for each glia
  contrast (LMM, FDR-corrected; *p < 0.05, ***p < 5e-4, n.s. not significant). H Images of
  representative high Aβ plaques from FFPE tissue sections stained with DAPI (blue), Aβ (4G8;
  yellow), IBA1 (cyan), GFAP (magenta), and synaptophysin (SYP; green, top-left panel) or NEUN
  (green, bottom-left panel). SYP and NEUN display lower-intensity staining surrounding glia-high
  plaques compared to glia-low plaques (quantification on right). Points represent average values
  from each of 10 AD individuals quantified in the area surrounding plaques (scale bar = 25 µm;
  paired t-test; **p < 0.005, ***p < 1e-10, n.s. not significant)"
- **Screenshot**: figure5.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (panel D Venn counts, panel C correlation R/p are
  printed values; other panels read qualitatively)
- **Reading confidence**: high (panel D, H quantification trend); medium (panels B, C, E, F, G
  individual values)

## Data table (Panel D - Venn diagram of DEG overlap across glia contrasts, quantitative)
| Region | Genes (p<5e-4) |
|---|---|
| "glia-high vs. glia-low (combined)" only | 56 |
| "glia-high vs. glia-low (low Aβ)" only | 77 |
| "glia-high vs. glia-low (high Aβ)" only | 30 |
| combined ∩ low-Aβ only | 141 |
| low-Aβ ∩ high-Aβ only | 23 |
| combined ∩ high-Aβ only | 10 |
| all three (combined ∩ low-Aβ ∩ high-Aβ) | 23 (center circle, distinct from the low-Aβ∩high-Aβ-only=23 region — both regions independently labeled "23" in the source figure) |

Note: the source Venn diagram prints two separate "23" labels (one for the three-way center region
and one for the low-Aβ∩high-Aβ-only two-way region); both are transcribed as printed, without
inferring which is which beyond their diagram position, since the rendered resolution does not
allow disambiguating overlapping label placement with certainty (reading confidence for this
specific pair of values: medium).

## Trend summary (Panel D)
The large combined∩low-Aβ overlap (141 genes) indicates the "combined" glia-high-vs-glia-low
contrast is dominated by the low-Aβ-stratum signal, consistent with the main-text DEG counts
(230/241/63 for combined/low-Aβ/high-Aβ at FDR<0.05) showing low-Aβ yields nearly as many DEGs as
the combined contrast while high-Aβ yields substantially fewer (supports C03).

## Data table (Panel C - glia-effect scatterplot, quantitative_plot)
- **Plot kind**: scatter
- **Axes**: X = t-value, glia-high vs. glia-low (low Aβ), linear (range ≈ -8 to 6); Y = t-value,
  glia-high vs. glia-low (high Aβ), linear (range ≈ -8 to 8)
- **Printed statistic**: r = 0.43, p = 0.00 (exact, printed on panel)

Named genes with large effects (yellow/blue/labeled): RNASE2, SERPINE2, C3AR1, SPARC, SFRP2,
SEMA3C, TRIM22, CD68, C1QB, FGF2 (positive / glia-high-associated); ATP13A2, ALDH1A3, HTR2A,
SLC6A17, NEFL, PVALB, CAST, DLX6 (negative / glia-low-associated).

## Trend summary (Panel C)
Moderate positive correlation (r=0.43) between the low-Aβ and high-Aβ glia-contrast t-statistics,
indicating a partially shared but not identical glia-high transcriptional signature depending on
Aβ context (supports C03's Aβ-context-dependent DEG counts).

## Visual description (Panels E, F - GSEA heatmaps, quantitative but not individually legible)
- **Panel E** rows: synapse, exocytic vesicle, macroautophagy, intermediate-filament-bundle
  assembly, voltage-gated channel activity, apoptotic process, translation, response to lipid,
  regulation of cell-cell adhesion, collagen-containing ECM, inflammatory response, leukocyte
  mediated immunity, antigen processing/presentation of peptide antigen, response to cytokine,
  cytokine production, response to transforming growth factor beta, interleukin-6 production,
  interferon-gamma signaling, complement and coagulation cascades; columns = combined/low-Aβ/
  high-Aβ glia contrasts. Qualitative pattern: synapse/exocytic-vesicle/voltage-channel terms
  strongly negative (blue) across all three columns; apoptotic-process through
  complement-and-coagulation-cascades terms strongly positive (red/orange), generally strongest in
  magnitude for the combined and low-Aβ columns.
- **Panel F**: Same PIG/OLIG/DAM/DAA and MG0-MG12 geneset columns as Fig. 3F, rows = combined/
  low-Aβ/high-Aβ glia contrasts. MG3 column again shows the visually brightest (yellow, highest)
  enrichment across all three rows; MG0/MG1 show minimal enrichment.

## Trend summary (Panels E, F)
Glia-high spots show coordinated downregulation of synaptic/vesicle/channel pathways and
upregulation of a broad immune/inflammatory/complement program, with the MG3 (DAM-like) state
again the most consistently enriched microglial state — supporting C03 and C04.

## Visual description / partial data (Panel G - gene-level boxplots, 9 genes x 3 contrasts)
Glia markers SPARC, CD44, HLA-DRA (left column) show higher normalized expression in "glia-high"
than "glia-low" bars across combined/low-Aβ/high-Aβ (up to ***). Neuronal markers SYT2, RORB,
PVALB (middle column) and synaptic markers SLC6A17, GRM7, GABBR2 (right column) show lower
normalized expression in "glia-high" than "glia-low" bars (GRM7 not significant in the "low Aβ"
comparison, "n.s."). Exact expression values not transcribed (no printed data labels); direction
and significance tier read directly.

## Data table (Panel H - SYP/NEUN/CD68 IHC quantification, quantitative_plot)
- **Plot kind**: box plot (3 sub-panels: SYP intensity, NEUN+ proportion, NEUN+ count)
- **Axes**: X = glia stratum x Aβ stratum (6 groups: glia-high/glia-low crossed with
  combined/low-Aβ/high-Aβ), Y = respective intensity/proportion/count metric, linear scale

| Metric | Pattern (glia-high vs. glia-low, qualitative) | Significance |
|---|---|---|
| SYP average intensity | Lower in glia-high across all 3 Aβ groupings | *** (combined, low Aβ); *** (high Aβ, per figure) |
| NeuN+ nuclei proportion | Lower in glia-high across all 3 Aβ groupings | ** to *** |
| NeuN+ count per plaque area | Lower in glia-high for combined/low-Aβ; n.s. for high-Aβ | ** (combined); n.s. (high Aβ) |

Exact box-plot median/quartile values are not transcribed (no printed data labels at this
resolution); only direction and significance tier are read, consistent with the figure caption's
own summary statistics (paired t-test, **p<0.005, ***p<1e-10, n.s. not significant).

## Trend summary (Panel H)
Synaptic (SYP) and neuronal (NEuN) markers are reduced surrounding glia-high plaques relative to
glia-low plaques across n=10 AD individuals, directly supporting C03 and corroborating the ST-level
finding (Panel G) of reduced neuronal/synaptic gene expression in glia-high spots.

## Visual description (Panel H images - qualitative_sample)
- **Shows**: Representative FFPE plaque images (4G8-Aβ/IBA1/GFAP merge, plus SYP or NeuN channel)
  for glia-high vs. glia-low plaques.
- **Demonstrates**: Visually reduced SYP/NeuN signal intensity surrounding glia-high plaques.
- **Supports**: C03.
