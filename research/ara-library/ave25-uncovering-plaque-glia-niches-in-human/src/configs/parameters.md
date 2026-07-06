# Analysis Parameters

Per-parameter record of the quantitative configuration values the paper explicitly states for its
computational pipeline. Format follows the ARA config schema (Value / Rationale / Search range /
Sensitivity / Source).

## Spot QC minimum gene count
- **Value**: 500 genes/spot (spots below this threshold removed)
- **Rationale**: Not specified in paper (standard low-quality-spot QC)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, spatial transcriptomics sequencing data processing subsection, Page 4-5 of 23

## Principal components for clustering
- **Value**: Top 3,000 variable genes for PCA; top 50 PCs computed; top 10 Harmony embeddings used for downstream UMAP/clustering
- **Rationale**: Top 10 Harmony embeddings chosen by visual inspection of an elbow plot of standard deviation attributed to each embedding (Supplementary Fig. 1E)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, spatial transcriptomics sequencing data processing subsection, Page 4-6 of 23

## Louvain clustering resolution for ST spots
- **Value**: 0.3 (all other parameters default)
- **Rationale**: Not specified in paper
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, spatial transcriptomics sequencing data processing subsection, Page 5 of 23

## BayesSpace cluster count, benchmarking comparator
- **Value**: q = 8
- **Rationale**: Deemed optimal upon inspection of the qPlot (Supplementary Fig. 3C)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, ST analysis pipeline benchmarking subsection, Page 5-6 of 23

## Co-expression network gene filtering
- **Value**: Genes retained at 1 CPM or more in all samples; 14,534 expressed genes from 21 donors used as SpeakEasy input; 100 initializations, Spearman correlation
- **Rationale**: Not specified in paper (standard low-expression filtering)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, co-expression network analysis in spatial transcriptomics subsection, Page 6 of 23

## Module preservation thresholds, WGCNA Zsummary
- **Value**: Z below 2 = not preserved; Z between 2 and 10 = preserved; Z above 10 = highly preserved
- **Rationale**: Standard WGCNA modulePreservation interpretation thresholds (Langfelder and Horvath)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, co-expression network analysis in spatial transcriptomics subsection, Page 6 of 23

## Amyloid-beta intensity stratification thresholds
- **Value**: log2(avg amyloid-beta intensity + 1): no amyloid-beta group is 2.5 to 4; low group is 4 to 6.5; high group is above 6.5
- **Rationale**: Selected via manual scoring of 781 plaques; the 6.5 cutoff (between low and high) maximized the distinction between diffuse and compact/dense-core plaque types
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, spot stratifications subsection, Page 6-7 of 23

## Glia intensity stratification thresholds
- **Value**: Glia-high group defined by log2(avg intensity+1) IBA1 above 6.8 and/or GFAP above 7.2. Glia-low group defined by IBA1 below 6.2 and GFAP below 6.5
- **Rationale**: Manual assessment indicated glia-high spots typically contain more than 4 glial cells while glia-low spots contain approximately 0 to 4 (Supplementary Fig. 7)
- **Search range**: Stricter thresholds and single-positive-only stratification (for example GFAP-positive/IBA1-negative only) were tested
- **Sensitivity**: High - increasing threshold stringency or requiring single-positivity reduced the number of sections with adequate spot counts for pseudobulk analysis, reducing statistical power for DEG detection; the reported thresholds were retained as the power-preserving choice
- **Source**: Methods, spot stratifications subsection, Page 7 of 23

## Pseudobulk gene-expression filtering for niche contrasts
- **Value**: Genes with CPM greater than 1 in at least 80 percent of brain sections retained; brain sections with fewer than 50 spots for a given niche type excluded from that contrast
- **Rationale**: Not specified in paper (standard low-expression / low-power filtering)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, statistical analysis to identify amyloid-beta and glia differential genes subsection, Page 7 of 23

## Differential expression significance threshold
- **Value**: FDR-adjusted p less than 0.05 (Benjamini-Hochberg across all genes and all amyloid-beta/glia contrasts)
- **Rationale**: Standard multiple-testing correction for genome-wide contrasts
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, statistical analysis to identify amyloid-beta and glia differential genes subsection, Page 7 of 23

## NICHES ligand-receptor construction parameters
- **Value**: k equals 4 nearest-neighbor graph for imputation and niche matrix construction; Omnipath v3.2.8 LR reference; default NICHES v1.0.0 parameters otherwise
- **Rationale**: Not specified in paper (tool defaults used)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, ligand-receptor analysis subsection, Page 7 of 23

## NICHES analysis inclusion criteria
- **Value**: Gray-matter spots only; sections/strata with 50 or more spots per group only; LR genes with CPM of 1 or less in fewer than 50 percent of sections removed
- **Rationale**: Not specified in paper (standard power/coverage filtering)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, ligand-receptor analysis subsection, Page 7 of 23

## scRNA-seq (iPSC co-culture) QC thresholds
- **Value**: Cells with fewer than 2,000 or more than 9,000 genes and/or more than 7.5 percent mitochondrial reads removed; final retained set equals 13,740 cells (whole co-culture) and 3,875 cells (amyloid-beta-treated iMGL subset)
- **Rationale**: Not specified in paper (standard scRNA-seq QC to exclude low-quality/doublet-like cells)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, single-cell RNA sequencing and data processing subsection, Page 8 of 23

## scRNA-seq clustering parameters
- **Value**: PCA on top 2,000 variable genes; UMAP/clustering on top 15 PCs; SNN neighbors equals 20; Louvain resolution equals 0.3 (both for whole co-culture and for amyloid-beta-treated-iMGL-only subclustering)
- **Rationale**: Not specified in paper
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, single-cell RNA sequencing and data processing subsection, Page 8 of 23

## FFPE plaque classification thresholds
- **Value**: Average 4G8 intensity filter greater than 2000 (post-scaling/centering per case); high amyloid-beta equals top 25 percent of scaled 4G8-intensity objects; low amyloid-beta equals bottom 75 percent; glia-high equals top 25 percent scaled GFAP or IBA1 intensity; glia-low equals remainder
- **Rationale**: Consistent with the ST IHC stratification criteria, adapted for the higher-resolution FFPE imaging modality
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, immunostaining quantification for FFPE tissue sections subsection, Page 4 of 23

## Sequencing depth targets
- **Value**: ST minimum 50,000 raw reads per spot (NovaSeq, 3 batches); scRNA-seq target of 50,000 reads per cell (NovaSeq 6000)
- **Rationale**: Not specified in paper (standard depth targets for respective assays)
- **Search range**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods, spatial transcriptomics subsection (Page 3 of 23) and single-cell RNA sequencing and data processing subsection (Page 8 of 23)
