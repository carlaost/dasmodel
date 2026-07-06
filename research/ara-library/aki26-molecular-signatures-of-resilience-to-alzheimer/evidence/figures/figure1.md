# Figure 1: Neuronal cell composition across neocortical regions and AD pathology stages
- **Source**: Figure 1, §"Neuronal cell type composition during the spatiotemporal progression of AD"
- **Caption**: "a Experimental design to study AD progression across neocortical regions and disease stages using snRNA-seq. b Neuronal enrichment by FANS, snRNA-seq, and dataset integration yielded 424,528 nuclei (362,224 neurons, after QC). c UMAP and bar plots representing the relative abundance of major cell types. d UMAP plots splitting the datasets by region and disease stage group. e Fraction of nuclei from each major cell type by region (top) and disease stage group (bottom). f, g UMAP plots of the annotated excitatory and inhibitory clusters and heatmaps showing the normalized expression of selected subtype and cluster-specific marker genes. h, i UMAP plots and gene expression heatmaps for each brain region… j Cosine distance matrix comparing the proximity in gene expression between the excitatory and inhibitory clusters from the SEA-AD DLPFC reference dataset (x-axis) and our BA9 dataset (y-axis)… k UMAP and dot plots showing the annotated glial subtypes and states."
- **Screenshot**: figure1.png
- **Figure type**: mixed (diagram + qualitative UMAP + quantitative bar/heatmap/matrix)
- **Extraction method**: exact_from_labels (text-stated counts) + visual_description
- **Reading confidence**: high (for text-stated counts); medium (heatmap/UMAP density)

## Visual description
- **Panel a (diagram)**: three brains (BA9/BA7/BA17) along an "AD Progression" axis (low → intermediate → high pathology); annotation "46 donors, Braak 0–VI, 3 regions, 243 samples".
- **Panel b (diagram)**: workflow — nucleus isolation & NeuN/DAPI staining → FANS (NeuN− / NeuN+) → droplet snRNA-seq (Drop-seq / 10x) → QC & integration → 655,407 nuclei → 424,528 (362,224 neuronal).
- **Panel c (UMAP + bar)**: major cell types (Excitatory, Inhibitory, Oligodendrocyte, OPC, Astrocyte, Microglia, Vascular); relative-fraction bars by region.
- **Panel d (UMAP)**: split by region (BA9 288,030; BA7 72,088; BA17 64,410 nuclei) and disease group (Low 136,344; Int 125,814; High 162,370 nuclei).
- **Panel e (bar)**: fraction of nuclei per major type by region (top) and disease group (bottom); excitatory dominant.
- **Panels f,g (UMAP + heatmap)**: 18 excitatory (Ex1–Ex18) and 19 inhibitory (In1–In19) clusters with cluster-specific marker heatmaps (diagonal specificity). Full labels e.g. Ex5:RORB-CUX2-EYA4-LAMA3; Ex6:RORB-MME; Ex7:RORB-GABRG1; In labels LHX6-/ADARB2- families.
- **Panels h,i (UMAP + heatmap)**: per-region (BA9/BA7/BA17) preservation of marker expression; Ex5 overrepresented in BA17.
- **Panel j (cosine-distance matrix)**: this study's clusters (y) vs SEA-AD DLPFC (x); low distance = high similarity; top-3 closest clusters shown; annotations closely match reference.
- **Panel k (UMAP + dot plot)**: glial states — 4 astrocyte (SLC1A2-WIF1, SLC1A2-SMTN, GFAP-OSMR/CHI3L1, GFAP-AQP1/VCAN), 4 microglia (CX3CR1, AIF1, CACNA1B, CD163), 2 oligodendrocyte (OPALIN, COL18A1).

## Key text-stated quantities
| Quantity | Value |
|----------|-------|
| Nuclei profiled | 655,407 |
| Nuclei after QC | 424,528 |
| Neuronal (Ex / In) | 362,224 (282,930 / 79,294) |
| Astrocytes / Microglia / OPC / Oligo / Vascular | 14,691 / 5,071 / 5,770 / 36,589 / 183 |
| Clusters | 18 Ex + 19 In |

## Trend / structural summary
Establishes the cohort, QC yield, and a cross-dataset-validated neuronal taxonomy; the excitatory
cluster Ex5 (RORB/CUX2/EYA4) is already flagged as overrepresented in BA17. Supports C02, C10.
