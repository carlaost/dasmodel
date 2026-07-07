# Figure 5: Gene expression in tissue niches of plaques and tangles

- **Source**: Fig. 5, Gaur et al. (2025), *Nature Communications* 16:10395, doi:10.1038/s41467-025-65350-6, page 10 of 17.
- **Caption**: "Fig. 5 | Gene expression in tissue niches of plaques and tangles. a A cartoon representing the distance for a cell to get assigned as close, intermediate, or far from plaque/tangle depositions. (Partly created in BioRender. Gaur, P. (2025)). b Heatmap displaying the Delta (change in log-transformed expression) estimated by a linear mixed model (LMM) comparing gene expression across varying distances relative to the close-proximity from plaques in GM of TC on tissue. Each row represents a gene, grouped by cell type, while the color gradient reflects the magnitude and direction of the effect- positive values indicate enriched expression, and negative values indicate depleted expression with distance. Bold values (Delta) annotated with '**' denote statistically significant differences (p-value <=0.01). c Same as b, for tangles. Source data are provided as a Source Data file."
- **Screenshot**: figure5.png (full journal page 10, all 3 panels a-c, plus caption)
- **Figure type**: mixed (panel a = diagram; panels b, c = quantitative heatmaps with exact printed Delta values and significance markers)
- **Extraction method**: exact_from_labels (all Delta values and significance stars in panels b/c are printed directly in each heatmap cell)
- **Reading confidence**: high

## Visual description

- **Panel a (diagram)**: A schematic showing a tissue section with navy-blue squares ("Plaque
  coordinates") and magenta squares ("Tangle coordinates") scattered on a pale background, with a
  zoomed inset showing individual cells (colored dots/squares) around a highlighted region. To the
  right, three concentric-ring cartoons labeled "Close," "Intermediate," and "Far," each showing a
  yellow center dot with plaque/tangle-coordinate squares and colored cell dots at varying radii,
  illustrating the three-tier proximity-binning scheme. Distance cutoffs are given below the panel:
  plaques Close <70 µm / Intermediate 70-154 µm / Far >154 µm; tangles Close <98 µm /
  Intermediate 98-262 µm / Far >262 µm.
- **Panel b (heatmap, Distance from plaques, exact_from_labels)**: 7 gene rows (GFAP, ID3, RELN,
  ALDH5A1, NEFL, NEFM, CD68), each tagged with a colored major-cell-type bar (Astro=yellow,
  Endo_Peri=salmon, GABA=dark red, Glut=light blue, Micro=green), x 2 columns ("Intermediate vs.
  close," "Far vs. close"); color scale "Delta log transformed expression" from -0.05 (blue) to
  +0.05 (red); "**" marks p<0.01. Printed values: GFAP 0.001 / 0.061**; ID3 0.035 / 0.050**; RELN
  0.051** / 0.095**; ALDH5A1 0.006** / 0.006**; NEFL -0.007 / -0.015**; NEFM -0.025** / -0.084**;
  CD68 0.010** / 0.006.
- **Panel c (heatmap, Distance from tangles, exact_from_labels)**: 3 gene rows (GFAP, THEMIS, PLP1),
  tagged Astro=yellow, Glut=light blue, Oligo=purple, x 2 columns ("Intermediate vs. close," "Far
  vs. close"); color scale 0.02-0.06 (all positive/red, no blue). Printed values: GFAP 0.037** /
  0.067**; THEMIS 0.019** / 0.051**; PLP1 0.029** / 0.042**.

## Data table (panel b — Distance from plaques, GM, exact printed Delta log-expression values)

| Gene | Major cell type | Intermediate vs. close | Far vs. close |
|---|---|---|---|
| GFAP | Astrocytes | 0.001 | 0.061** |
| ID3 | Endothelial/Pericytes | 0.035 | 0.050** |
| RELN | GABAergic | 0.051** | 0.095** |
| ALDH5A1 | Glutamatergic | 0.006** | 0.006** |
| NEFL | Glutamatergic | -0.007 | -0.015** |
| NEFM | Glutamatergic | -0.025** | -0.084** |
| CD68 | Microglia | 0.010** | 0.006 |

## Data table (panel c — Distance from tangles, GM, exact printed Delta log-expression values)

| Gene | Major cell type | Intermediate vs. close | Far vs. close |
|---|---|---|---|
| GFAP | Astrocytes | 0.037** | 0.067** |
| THEMIS | Glutamatergic | 0.019** | 0.051** |
| PLP1 | Oligodendrocytes | 0.029** | 0.042** |

## Trend summary
All 7 plaque-distance genes and all 3 tangle-distance genes show larger absolute Delta at "Far vs.
close" than "Intermediate vs. close" (a monotonic distance-dependent gradient), except CD68 (plaques)
which is largest at intermediate distance. NEFL/NEFM are the only genes with a negative Delta
(lower expression farther from plaques, i.e. higher expression proximal to plaques) — directly
grounding `logic/claims.md` C12's "elevated neurofilament expression near plaques" statement. GFAP's
plaque-distance Delta (0.001 intermediate, 0.061 far — both non-negative, i.e. higher expression
*farther* from plaques) is the counter-intuitive finding that motivates the bimodality analysis in
C13. All tangle-distance genes (GFAP, THEMIS, PLP1) are positive at both distances (higher expression
farther from tangles), matching C12's tangle-distance statement.
