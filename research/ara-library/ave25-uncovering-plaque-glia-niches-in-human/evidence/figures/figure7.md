# Figure 7: Aβ oligomer treatment of co-cultured iMGL partially recapitulates ST glia response to Aβ plaques
- **Source**: Figure 7, Page 18 of 23
- **Caption**: "Aβ oligomer treatment of co-cultured iMGL partially recapitulates ST glia response
  to Aβ plaques. A Schematic of in vitro co-culture experiments. Graphics created with
  BioRender.com (B) Representative immunofluorescence for DCX (neuronal), IBA1 (iMGL) and GFAP
  (astrocyte) proteins in co-culture models, scale bar: 100 µm, inset: 50 µm. C UMAP visualization
  of cells from control and Aβ oligomer-treated cultures, colored by annotated cell type clusters.
  D Dotplot of cluster/cell-type enriched genes. E GSEA enrichment of Aβ-induced genes for ST
  glial response by cell type. Red dotted line corresponds to FDR-threshold. F Boxplots of genes
  differentially expressed in iMGL upon Aβ treatment. G UMAP visualization of Aβ oligomer-treated
  iMGL, colored by subtype cluster. H Heatmap of the top 5 differentially expressed gene markers
  per iMGL subtype cluster. I GSEA enrichment of Aβ-treated iMGL cluster DEGs (Supplementary
  Table 11) for ST glial response. Red dotted line corresponds to FDR-threshold. J GSEA enrichment
  of Aβ-treated iMGL cluster (vs. control) DEGs (Supplementary Table 12) for reported MG state
  genesets in human AD brains[8] (*p < 5e-2, **p < 5e-3, ***p < 5e-4)"
- **Screenshot**: figure7.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (cell counts, panel E/I bar identities and FDR-threshold
  line are legible; panel J individual significance stars legible per cell)
- **Reading confidence**: high

## Visual description (Panel A - diagram)
- **Components**: Two starting culture wells ("iPSC-derived iMGL"; "iPSC-derived
  neurons+astrocytes") merging into a "coculture" well; timeline arrows "72 hours" then "24 hours
  +/- abeta"; output box "dissociation + single cell sequencing" leading to "DEG, GSEA".
- **Connections**: Sequential in vitro workflow: separate differentiation -> co-culture (72h) ->
  Aβ oligomer or vehicle treatment (24h) -> dissociation -> scRNA-seq -> DEG/GSEA analysis.
- **What it conveys**: The in vitro experimental design used to generate the cross-validation
  dataset analyzed in panels C-J (see `logic/solution/method.md` Stage 10).

## Data table (Panel C - UMAP cell counts, quantitative)
| Cluster | Approx. label |
|---|---|
| iMGL | largest cluster, left side of UMAP |
| cycling iMGL | small side cluster adjacent to iMGL |
| astrocytes | distinct cluster, upper right |
| neurons | distinct cluster, lower right |
| cycling ast/neu | small intermediate cluster |
| other/progenitor | distinct cluster, top |

Total cells: 13,740 (printed on panel, matches main text).

## Visual description (Panel D - dotplot, quantitative but not individually legible)
Marker genes shown per cluster: AIF1, C3, MKI67, PCNA, GFAP, SLC1A3, SNAP25, DCX. iMGL clusters
show high expression/percent-expressing for AIF1/C3; astrocyte cluster for GFAP/SLC1A3; neuron
cluster for SNAP25/DCX; cycling clusters for MKI67/PCNA. Dot size = percent expressing (legend:
0.25/0.5/0.75/1), color = expression z-score (-2 to 2).

## Data table (Panel E - GSEA enrichment of ST glial response by cell type, quantitative_plot)
- **Plot kind**: horizontal bar
- **Axes**: X = signed -log10(p) (linear, range -15 to 20), Y = cell type (neuron, iMGL,
  astrocyte), 3 bars each (glia-high vs. glia-low: combined/low Aβ/high Aβ)

| Cell type | Aβ-response enrichment for ST glial signature | Crosses FDR-threshold (red dotted line)? |
|---|---|---|
| neuron | ≈0 to slightly positive, small magnitude | No |
| iMGL | ≈15-20 (combined), ≈10 (low Aβ), ≈10 (high Aβ) | Yes, all three |
| astrocyte | ≈0 to slightly negative/positive, small magnitude | No |

Bar heights are digitized estimates (≈); the qualitative conclusion (iMGL bars cross the
FDR-threshold line, neuron/astrocyte bars do not) is read at high confidence and matches the
main-text statement "positive enrichment of the ST glial response in iMGLs. However, no enrichment
was observed in astrocytes and neurons."

## Trend summary (Panel E)
Directly supports claim C08: only iMGL Aβ-response genes are enriched for the in vivo ST
glia-high-vs-glia-low signature.

## Visual description (Panel F - gene-level boxplots, 6 genes, quantitative but not fully legible)
HLA-DRA, CD68, C4ORF48, CXCL16, ITGAX, C1QB each shown as ctrl vs. Aβ boxplots in iMGL; all six
show visually higher expression in the Aβ-treated condition than control, consistent with the
main-text list of iMGL DEGs "including many immune, complement cascade, and phagocytosis genes."

## Data table (Panel G - iMGL subcluster UMAP, quantitative)
Four subclusters shown: iMGL1 (largest, left/center), iMGL2 (upper, green), iMGL3 (lower right,
purple), iMGL4 (small, top right, distinct/separated cluster).

## Visual description (Panel H - subcluster marker heatmap, quantitative but not individually legible)
Top 5 marker genes per subcluster shown as a z-score heatmap: iMGL1 markers include IFITM3,
CX3CR1, MNDA, ADGRG3, SMIM25, CMTM4; iMGL2 markers include CTSL, CCL3, MRC1, CTSB; iMGL3 markers
include HLA-DPB1, HLA-DRB1, HLA-DRA, CD74, HLA-DPA1, FZD2; iMGL4 markers include MKI67, FAM111B,
TYMS, MYBL2, ASPM (proliferation markers, consistent with a cycling-cell subcluster).

## Data table (Panel I - GSEA enrichment of iMGL subcluster DEGs for ST glial response, quantitative_plot)
- **Plot kind**: horizontal bar
- **Axes**: X = signed -log10(p) (linear, range 0-20), Y = subcluster (iMGL1-4), 3 bars each
  (glia-high vs. glia-low: combined/low Aβ/high Aβ)

| Subcluster | Crosses FDR-threshold? | Pattern |
|---|---|---|
| iMGL1 | Yes, all 3 bars | Enriched under both Aβ-low and Aβ-high conditions (bars ≈10-17) |
| iMGL2 | Yes, primarily 1-2 bars | Enrichment primarily in Aβ-low condition |
| iMGL3 | Yes, 1-2 bars | Enrichment primarily in Aβ-low condition |
| iMGL4 | No | Bars near/below threshold |

## Trend summary (Panels I)
Directly supports claim C09: iMGL1 shows the broadest/strongest enrichment for the in vivo ST
glial-response signature across both Aβ conditions, while iMGL2/iMGL3 are more condition-specific
(low-Aβ) and iMGL4 (a proliferation/cycling-associated subcluster) shows minimal enrichment.

## Data table (Panel J - GSEA enrichment of iMGL subcluster DEGs for MG0-MG12 states, quantitative_plot)
- **Plot kind**: heatmap
- **Axes**: rows = MG0-MG12 (12 human microglial states), columns = iMGL1-4

Qualitative pattern (signed enrichment, yellow=high/positive): iMGL1 shows a bright cell at MG3
(strongest in that row) plus weaker positive signal elsewhere; iMGL2 shows bright cells at MG4,
MG5, MG7, MG10; iMGL3 shows a bright cell at MG12; iMGL4 shows scattered weaker signal across
several states. Significance stars (*p<5e-2, **p<5e-3, ***p<5e-4) are visible per cell but not all
individually transcribed here.

## Trend summary (Panel J)
Directly supports claim C09's specific correspondences: iMGL1↔MG3 (DAM/ribosome-biogenesis, the
state most enriched in the in vivo ST glial response per Fig. 3F/5F) and iMGL2↔MG4/MG5/MG7/MG10
(lipid-processing/phagocytic/glycolytic/inflammatory-III states).
