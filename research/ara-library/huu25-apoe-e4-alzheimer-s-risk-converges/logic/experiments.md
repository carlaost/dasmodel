# Experiments (Analysis Plans)

Declarative, directional only. Exact numbers live in `evidence/` and `logic/claims.md`.

## E01: Build the ERC snRNA-seq cell-type atlas (fine subclusters)
- **Verifies**: C01, C04
- **Setup**:
  - Assay: 10x Chromium 3' v3.1 snRNA-seq, 1 PI+ sample per donor, n=31 donors
  - Sequencing: Illumina NovaSeq 6000, min 50,000 reads/nucleus
  - Reference/alignment: CellRanger, human GRCh38 2020-A
  - System: R/Bioconductor pipeline (DropletUtils, scDblFinder, scran, scater, harmony, ScType, DeconvoBuddies)
- **Procedure**:
  1. Align reads; call empty droplets; remove doublets; apply adaptive-MAD QC.
  2. GLM-PCA dimensionality reduction; harmony batch correction; graph-based clustering + iterative subclustering.
  3. Annotate broad cell types and fine subclusters using marker genes and spatial registration to external ERC/DLPFC datasets.
- **Metrics**: number of high-quality nuclei; number of broad cell types and fine subclusters; per-subcluster marker genes.
- **Expected outcome**: A stable set of fine subclusters spanning glia, neurons, and vascular cells, including multiple oligodendrocyte subclusters.
- **Baselines**: Franjic et al. ERC/hippocampus taxonomy; PsychENCODE DLPFC cell types.
- **Dependencies**: none

## E02: Build the ERC Visium spatial-domain atlas
- **Verifies**: C03
- **Setup**:
  - Assay: 10x Visium spatial gene expression, one section per donor, 31 samples
  - Sequencing: NovaSeq 6000, min 60,000 reads/spot
  - Pipeline: VistoSeg → SpaceRanger (GRCh38, 2020-A) → spatialLIBD QC → SpotSweeper → nnSVG → harmony → BayesSpace
- **Procedure**:
  1. Segment slides, align capture areas, run SpaceRanger; QC spots (manual + SpotSweeper).
  2. Select spatially variable genes + layer markers; PCA; harmony batch correction.
  3. BayesSpace spatially-aware clustering over a range of k; choose optimal k; annotate SpDs via registration to DLPFC and ERC references.
- **Metrics**: number of in-tissue spots; optimal k / number of SpDs; SpD annotations.
- **Expected outcome**: A small number of transcriptionally distinct SpDs including gray-matter layers, two white-matter domains, and a vascular domain.
- **Baselines**: DLPFC spatial atlas (Huuki-Myers et al. 2024; Maynard et al. 2021).
- **Dependencies**: none

## E03: APOE carrier DGE in spatial domains (+ ancestry- and sex-specific)
- **Verifies**: C03, C05, C06
- **Setup**: Visium pseudobulk per SpD (registration_pseudobulk, min_ncells=10); edgeR filtering; voomLmFit + limma.
- **Procedure**:
  1. Fit carrier model `~0 + APOE_syn + Sex + Age + Anc_Afr + pseudo_expr_chrM_ratio`, block on Visium slide; contrast E4+ vs E2+.
  2. Repeat with ancestry-combined covariate (carrier_Anc) and sex-combined covariate (carrier_Sex, excluding X/Y genes).
  3. GO overrepresentation on DEG sets (clusterProfiler).
- **Metrics**: per-SpD DEG counts (up/down, FDR<0.05); enriched GO terms; ancestry/sex-specific DEG counts.
- **Expected outcome**: DEGs concentrate in white-matter and vascular SpDs; ancestry-specific sets differ; male-dominated sex-specific sets.
- **Baselines**: within-study comparison across SpDs.
- **Dependencies**: E02

## E04: APOE carrier DGE in cell types — broad and fine subcluster
- **Verifies**: C01, C02, C05, C06
- **Setup**: snRNA-seq pseudobulk per broad cell type and per fine subcluster; same voomLmFit/limma model, block on experimental round.
- **Procedure**:
  1. Broad-resolution carrier contrast; fine-subcluster carrier contrast.
  2. Ancestry-specific and sex-specific contrasts.
  3. GO overrepresentation on DEG sets.
- **Metrics**: per-cell-type / per-subcluster DEG counts and directions; GO terms.
- **Expected outcome**: Broad Oligo has the most DEGs; at fine resolution DEGs concentrate in one Oligo subcluster with myelination/differentiation genes down and immune/calcium genes up.
- **Baselines**: SRT DGE (E03) for cross-modality consistency.
- **Dependencies**: E01

## E05: GO / functional interpretation of Oligo.3 and related subcluster DEGs
- **Verifies**: C02
- **Setup**: clusterProfiler compareCluster + rrvgo parent-term reduction on DEG sets (Oligo.3, Astro.3, Micro.4, SpDs).
- **Procedure**: run overrepresentation analysis on up/down DEG sets; summarize dominant biological-process terms; compare shared terms across subclusters.
- **Metrics**: enriched BP GO terms, gene ratios, adjusted p-values.
- **Expected outcome**: Downregulated Oligo.3/Astro.3 terms enriched for myelination and oligodendrocyte differentiation; upregulated terms for calcium-ion transport / synaptic signaling.
- **Baselines**: none.
- **Dependencies**: E04

## E06: Oligodendrocyte maturation trajectory
- **Verifies**: C04
- **Setup**: OPC + Oligo nuclei subset; PCs; TSCAN MST + pseudotime; MeanRatio marker gene dot plots.
- **Procedure**: compute cluster centroids, minimum spanning tree, pseudotime; order Oligo subclusters relative to OPCs; inspect maturation markers.
- **Metrics**: trajectory ordering; marker-gene expression patterns.
- **Expected outcome**: Oligo.3 sits nearest OPCs; Oligo.1/Oligo.2 are the mature/myelinating endpoints.
- **Baselines**: none.
- **Dependencies**: E01

## E07: Cross-dataset enrichment against published AD snRNA-seq
- **Verifies**: C05, C08
- **Setup**: Fisher exact tests (alt="greater") on 2×2 tables comparing this study's subcluster DEGs against cell-type DEGs from Grubman et al. (ERC AD) and Blanchard et al. (PFC AD/iPSC).
- **Procedure**: build reference/target DEG sets; test overlap significance for up/down directions and ancestry-specific sets; correlate Oligo.3 with published Oligo subclusters.
- **Metrics**: enrichment significance (FDR), shared genes, subcluster correlation.
- **Expected outcome**: Significant overlap of downregulated myelination genes (PLP1, OPALIN) with AD-downregulated Oligo sets; opposite-direction enrichment for some upregulated sets.
- **Baselines**: Grubman et al. 2019; Blanchard et al. 2022.
- **Dependencies**: E04

## E08: Integrative multicellular factor analysis (MOFA) and pathology association
- **Verifies**: C07
- **Setup**: MOFAcellulaR on combined Visium + snRNA-seq pseudobulk views; 7 factors; associate donor factor scores with covariates (APOE carrier, ancestry, age, sex, pTau, Braak, CERAD).
- **Procedure**: fit MOFA model; compute variance explained per view; test factor–covariate associations (linear model / ANOVA, BH-corrected); interpret top signature genes.
- **Metrics**: variance explained per view; factor–covariate p/FDR; signature genes and their DEG overlap.
- **Expected outcome**: A factor spanning non-myelinating Oligos and a WM SpD associates with APOE carrier status and pTau, and its signature genes overlap Oligo.3 E4+ DEGs plus additional WM genes.
- **Baselines**: independent DGE results (E03, E04) as corroboration.
- **Dependencies**: E03, E04
