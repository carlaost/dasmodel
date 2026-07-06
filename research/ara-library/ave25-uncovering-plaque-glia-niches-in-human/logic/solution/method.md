# Computational Method (Analysis Pipeline)

The paper's core methodological contribution is a computational pipeline linking Visium spatial
transcriptomics to paired adjacent-section IHC. This file lays out the pipeline stage by stage, as
described in Methods; exact software versions/parameters are captured per-parameter in
`src/configs/analysis_parameters.md`.

## Stage 1: ST data generation and QC
1. Space Ranger (10x Genomics) maps barcodes to the human genome (Gencode 27), builds a per-section
   count matrix.
2. Sections merged into one Seurat object (Seurat v4.2.0, R).
3. Per-spot QC: spots with fewer than 500 measured genes removed.
4. `Seurat::SCTransform` normalizes/scales UMI counts (regularized negative binomial regression).

## Stage 2: Integration and spot clustering
1. PCA on top 3,000 variable genes; top 50 PCs retained.
2. Harmony (v0.1.0) integration across donors, correcting for age, RIN, library batch, donor
   (technical/biological covariates) - chosen after benchmarking against scANVI, fastMNN, ComBat,
   Seurat v3 RPCA, scVI, and BBKNN (scib snakemake pipeline, 16 representative sections from 4
   individuals; metrics: PCR batch, graph iLISI, graph connectivity, kBET for batch correction;
   isolated-label F1, isolated-label silhouette, graph cLISI for biological conservation; 40/60
   weighted mean).
3. Top 10 Harmony embeddings used (selected via elbow-plot inspection) for UMAP + Louvain
   clustering (SNN graph, resolution 0.3), giving 11 clusters, manually annotated to cortical
   layers (L1, L2-3, L3-5, L5, L6), white matter, meninges, blood vessel, and interneuron
   populations using canonical markers and spatialLIBD (v7.5); one low-spot-count glial-signature
   cluster excluded from downstream analyses.
4. Integration/clustering outputs (SCT-normalized, Harmony-integrated values) used only for spot
   clustering; all downstream DEG, cell-proportion, and LR analyses use pre-integration count
   data.
5. Validation: repeated pipeline on a 16-section subsample and compared against BayesSpace
   (q=8, chosen via qPlot inspection); 99% concordance on gray-matter spot labels between methods.

## Stage 3: Cell-type deconvolution
1. cell2location estimates abundance of cell types (8 major types, or 44 finer subtypes) per spot,
   using average expression from a published ROSMAP DLPFC snRNA-seq reference.
2. GSEA (100 permutations, BH-FDR) tests enrichment of predicted cell-type abundance within each
   spot cluster.

## Stage 4: Co-expression network quality check
1. Pseudobulk gene expression per donor (summed UMIs); genes filtered to at least 1 CPM in all
   samples; TMM-voom normalized (edgeR v3.36.0).
2. `removeBatchEffect` (limma v3.50.1) adjusts for library batch, RIN, age, PMI.
3. SpeakEasy (SE v1.0) consensus clustering (100 initializations, Spearman correlation) on 14,534
   expressed genes from 21 donors gives 29 modules (23 with at least 30 genes, covering 99.3% of
   assigned genes).
4. Functional enrichment: gprofiler g:GOSt (g:SCS correction) and Fisher's exact test (Bonferroni);
   all 23 modules significantly enriched for at least one function.
5. Module preservation: WGCNA `modulePreservation` against an independent 478-donor bulk RNA-seq
   network (Mostafavi et al. 2018); Zsummary statistic, Kruskal-Wallis test for significance
   (Z<2 not preserved, 2-10 preserved, >10 highly preserved). All ST modules preserved in bulk and
   vice versa.

## Stage 5: IHC image processing and per-spot intensity quantification
1. H&E images (20x, 9x9 tiled, 10% overlap) stitched (Adobe Photoshop); spot coordinates
   confirmed aligned to stitched image.
2. IHC images (20x, 10x10 tiled, 16-bit) background/shading-corrected (ImageJ BaSiC plugin),
   stitched (1% overlap), then aligned to the middle/ST H&E section via 7-12 manually placed
   landmark correspondences (ImageJ "Landmark Correspondences" plugin).
3. Additional artifact correction: grayscale opening/closing (structural element sized above
   plaque/glia scale) to extract and regress out large bright artifacts and local background
   inhomogeneity.
4. Per-spot average pixel intensity computed for each channel (Aβ, GFAP, IBA1) within each ST
   spot's 55-um-diameter area; border spots overlapping bright artifacts excluded.

## Stage 6: Plaque-glia niche stratification
See `logic/solution/study_design.md` and `logic/concepts.md` for the Aβ (no/low/high) and glia
(high/low) intensity thresholds and their calibration against manually annotated plaque sets.

## Stage 7: Differential expression (pseudobulk LMM)
1. Per-section, per-niche-type pseudobulk: sum UMI counts across gray-matter spots of that
   niche/section; retain genes with CPM>1 in at least 80% of sections; TMM-normalize (edgeR) plus
   voom transform (limma).
2. Linear mixed model per gene: niche type (binary) as fixed effect of interest; age, RIN, batch,
   AD status as fixed-effect covariates; donor as random effect (within-subject correlation across
   up to 4 sections). BH-FDR correction across all genes and contrasts (alpha=0.05); niche types
   with fewer than 50 spots in a section excluded from that section's pseudobulk for that
   contrast.

## Stage 8: GSEA interpretation
Per-gene LMM t-values ranked and tested via GSEA (Subramanian et al. 2005) against: (a) GO
terms/canonical pathways (gprofiler g:GOSt, g:SCS correction); (b) mouse PIG/OLIG/DAM/DAA gene
modules; (c) 12 human AD microglial states (MG0-MG12); (d) in-house iMGL/astrocyte/neuron
Aβ-response marker genesets generated from the co-culture scRNA-seq (Stage 10).

## Stage 9: Ligand-receptor (NICHES) intercellular communication inference
NICHES v1.0.0, Omnipath v3.2.8 LR reference; default imputation, k=4 nearest-neighbor niche-matrix
construction (summing signaling input from Euclidean neighbors) per section; spot-level LR
matrices averaged by section/stratification group (gray-matter spots, sections with at least 50
spots per group only); quantile-voom normalization (limma); mixed linear model with
`duplicateCorrelation` for repeated donors; BH-FDR correction.

## Stage 10: iPSC co-culture scRNA-seq and cross-validation
1. iMGL differentiation (iHPC intermediate, about 38 days) from iPSC line AICS-0090-391;
   astrocyte/neuron differentiation (via NPC intermediate) from iPSC line BR28.
2. Co-culture (iMGL + astrocyte/neuron, 1:4 ratio) 72 h, then 50 ug/mL oligomeric Aβ1-42 (or
   vehicle) 24 h.
3. scRNA-seq: 10x Genomics 3' v3 chemistry, NovaSeq 6000, about 50k reads/cell; CellRanger v6.0.1;
   CellBender v0.3.0 ambient-RNA correction; Seurat v4.2.0 QC (cells with <2000 or >9000 genes
   and/or >7.5% mitochondrial reads removed), scaling/log-normalization, PCA (top 2000 variable
   genes), UMAP (top 15 PCs), Louvain clustering (neighbors=20, resolution=0.3); doublets manually
   removed, leaving 13,740 cells.
4. Marker/DEG identification: Wilcoxon rank-sum test with Bonferroni correction
   (`Seurat::FindMarkers`), both for cluster-defining markers and for Aβ-treated-vs-control DEGs
   within each annotated cell type.
5. Aβ-treated iMGLs (3,875 cells) re-clustered (same procedure) into iMGL1-4 subclusters; marker
   genes identified per subcluster and used as GSEA genesets against the ST glial-response
   signature and the 12 human MG-state genesets.
