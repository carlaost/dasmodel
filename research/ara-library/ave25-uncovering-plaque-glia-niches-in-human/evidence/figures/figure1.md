# Figure 1: Spatial Transcriptomics Profiles of Postmortem DLPFC from 21 individuals
- **Source**: Figure 1, Page 5 of 23
- **Caption**: "Spatial Transcriptomics Profiles of Postmortem DLPFC from 21 individuals. A
  Diagrammatic summary of experimental workflow. Per individual, up to four 10-μm frozen sections
  of DLPFC were subjected to spatial transcriptomic sequencing using Visium. For each ST section,
  two adjacent sections were stained for DAPI, Aβ, GFAP, and IBA1 and imaged by fluorescence
  microscopy. IHC images were then aligned to the middle ST section, enabling spot-level
  quantification of IHC intensity for each stain and subsequent identification of genes associated
  with amyloid plaques and/or glial reactivity. Cartoon graphics created with BioRender.com (B)
  UMAP visualization of all ST spots from all individuals. Clusters were annotated manually based
  on the enriched expression of known layer- and/or cell-type-specific genes. C Spot clusters
  overlaid on a representative section (Sect. 8_C). D The expression level of SNAP25
  (pan-neuronal), MBP (oligodendrocytes; white matter), and PCP4 (Cortical layer 5) overlaid on a
  representative tissue section (Sect. 8_C). E Heatmap showing z-score of average expression of a
  subset of cluster-enriched genes. F Heatmap of GSEA normalized enrichment score (NES) for
  cell2location predicted neural sub-cell-types abundance across all spots comprising each spot
  cluster (BH-FDR: *p < 0.01, **p < 0.001, ***p < 1e-4)"
- **Screenshot**: figure1.png
- **Figure type**: mixed
- **Extraction method**: visual_description
- **Reading confidence**: medium (panels A-E clearly legible; panel F heatmap cell values are not
  individually legible at rendered resolution — see note in that panel's description)

## Visual description (Panel A - diagram)
- **Components**: Five numbered workflow stages laid out left to right/top to bottom: (1) Sample
  preparation — brain diagram, 21 ROSMAP participants, 6mm x 6mm frozen DLPFC block, cryosection,
  Visium slide with "up to 4 Visium sections per individual (78 total sections)"; (2) Sequencing
  Data Analysis — spatial gene expression matrix -> normalization -> PCA & UMAP -> clustering ->
  visualize genes of interest; (3) Immunostaining Analysis — adjacent top/bottom IHC sections and
  center H&E/Visium section aligned, per-spot quantification of Aβ/GFAP/IBA1; (4) Spot
  stratification by intensity — violin plots of Aβ intensity split into no/low/high groups; (5)
  Integrative analysis — differential genes/pathways (volcano plot), GSEA terms heatmap, cell type
  abundance (cell2location), intercellular communication (cell-cell interaction diagram).
- **Connections**: Sequential workflow arrows: sample prep -> library prep & sequencing -> (in
  parallel) immunostaining analysis -> align to Visium section -> spot stratification by
  intensity -> integrative analysis (differential genes, cell type abundance, intercellular
  communication), which in turn feeds back into differential genes/pathways box.
- **Annotations**: Color-coded background panels (green = sample prep/sequencing, gray/tan =
  immunostaining, pink = integrative analysis, lavender = spot stratification).
- **What it conveys**: The overall paired ST + adjacent-section-IHC experimental and computational
  workflow that underlies every downstream analysis in the paper (this is the pipeline documented
  in `logic/solution/method.md`).

## Data table (Panel F - quantitative heatmap, digitized/qualitative reading only)
Panel F shows a GSEA normalized-enrichment-score heatmap (cell2location-predicted cell-type
abundance enrichment per spot cluster); exact NES values are not printed as data labels and are not
individually legible at rendered resolution, so no per-cell numeric table is transcribed here
(risk of misreading a color-coded heatmap without an accompanying scale bar reference at this
resolution). Qualitatively: white-matter (WM) spots are strongly enriched for oligodendrocyte
subtypes (Oli0-5); meninges/blood-vessel spots are enriched for endothelial cells (End1/2) and
pericytes (Per); cortical-layer clusters (L1-L6) are enriched for layer-appropriate excitatory
neuron subtypes (Ex1-Ex14) and interneuron subtypes (In1-In11); astrocyte subtypes (Ast0-3) and
microglia/oligodendrocyte-lineage subtypes (Mic0-3, Opc0-2) show more diffuse enrichment across
gray-matter clusters. Significance stars (*p<0.01, **p<0.001, ***p<1e-4, BH-FDR) are shown per cell
but not individually transcribed.

## Data table (Panel B/C - spot cluster identities, qualitative/categorical)

| Cluster label | Anatomical/cell-type annotation |
|---|---|
| L1 | Cortical layer 1 |
| L2-3 | Cortical layer 2-3 |
| L3-5 | Cortical layer 3-5 (transitional) |
| L5 | Cortical layer 5 |
| L6 | Cortical layer 6 |
| L1-5 Low UMI | Low-UMI spots spanning layers 1-5 |
| WM | White matter |
| Meninges | Meningeal tissue |
| Blood Vessel | Vasculature |
| Interneuron | Interneuron-enriched spots |
| (excluded) | One additional low-spot-count glial-signature cluster, excluded from downstream analyses |

## Trend summary
Panels B-C establish 11 manually annotated spot clusters (L1, L2-3, L3-5, L5, L6, L1-5 Low UMI, WM,
Meninges, Blood Vessel, Interneuron, plus one excluded low-count glial cluster) that map onto
expected cortical anatomy. Panel D confirms expected marker gene spatial expression (SNAP25
pan-neuronal/gray-matter broad; MBP restricted to white matter; PCP4 restricted to a
layer-5-like band). Panel E shows a cluster x gene z-score heatmap in which each cluster has a
visually distinct block of high-expression marker genes (e.g., GFAP/CLU/RELN for Meninges; MBP/
OLIG1/CNP for WM; HBB/HBA1/HBA2 for Blood Vessel), confirming clean, non-overlapping cluster
identity. This figure is foundational context (tissue architecture / cell-type deconvolution
validation) for all downstream plaque-glia niche analyses; it does not itself carry a claim ID but
underlies the cell2location deconvolution referenced in `logic/concepts.md`.
