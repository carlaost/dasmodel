# Method: Analysis Pipeline

The paper's computational analysis proceeds through the following ordered stages, spanning
dissociated-nuclei profiling, cross-cohort integration, differential expression, and spatial
(CARTANA) validation/discovery.

## Stage 1 — Nuclei isolation, library preparation, and sequencing
- Cryosection (10 µm) each donor's mid-temporal-gyrus block; separate GM from subcortical WM with a
  razor blade.
- Isolate nuclei (Nuclei PURE Prep kit, Sigma-Aldrich; 0.1% Triton X, 1 mM DTT, 0.4 U/µl
  SUPERase-In lysis buffer); sucrose-cushion centrifugation (1.8 M, 45 min, 16,000 x g, 4°C).
- Load ~12,000 nuclei/sample onto the 10x Single Cell Next GEM G Chip; prepare cDNA libraries
  (Chromium Single Cell 3' Library and Gel Bead v3 kit); sequence on Illumina NovaSeq 6000 (S2 kit
  v1.5, 100 cycles), targeting 30,000 reads/nucleus.

## Stage 2 — Data processing and quality control
- Process all samples (own TC data + public datasets) uniformly with Cell Ranger v3.1.0 (GRCh38,
  Ensembl GRCh38.91 annotation modified to include intronic reads).
- Retain nuclei with >=500 UMIs (excluding mitochondrial RNA) and <5% mitochondrial RNA; cap at the
  top 10,000 nuclei (by UMI count) for samples exceeding 10,000 nuclei.
- Flag (but do not exclude, absent cluster-level doublet enrichment) potential doublets via
  scDblFinder v1.4.0; remove nuclei flagged as doublets from downstream trait-association analysis.
- Exclude 2 samples (1 individual) for low quality (few cells, low UMI/gene counts, high
  mitochondrial fraction).

## Stage 3 — Clustering and subcluster annotation
- Merge the 80 TC samples (Seurat workflow, no batch correction), then integrate with 6 external
  multi-region studies via Harmony (v0.1.0; 30 PCs, resolution 0.8, `study` as the integration
  variable), using Harmony-corrected embeddings for all downstream clustering.
- Cluster with Seurat `FindClusters` (SNN graph + Louvain, resolution 0.8); annotate into 8 broad
  cell types via canonical markers.
- Subcluster each broad cell type independently (same Harmony-integration workflow, applied within
  the cell-type subset).
- Refine subclusters with a Random Forest classifier (subclusters with >=50 cells; 75/25 train/test
  split; scran `modelGeneVar`-derived top-variable genes as features); merge subcluster pairs with
  >=~10% mutual confusion (from the post-hoc confusion matrix) that are also UMAP-adjacent.
- Cross-compare TC-only clustering against the integrated-dataset clustering; merge additional
  integrated clusters based on ~10% similarity and UMAP adjacency; annotate final subclusters via
  top marker genes (Seurat `FindAllMarkers`, >=25% detection, >=0.25 log-fold-change threshold), with
  glutamatergic subclusters additionally cross-referenced against the Allen Brain Atlas
  Transcriptomics Explorer for cortical-layer assignment.

## Stage 4 — AD trait association (cluster proportion) analysis
- Implement ANCOM-BC (v1.0.5) per broad cell type, separately in GM and WM, with Braak stage
  (categorized 0-1/2-4/5-6) as the covariate of interest and sex/age-of-death/PMI (scaled by 2×SD)
  regressed out.
- Repeat the same framework with sex (male) as the covariate of interest for the sex-association
  analysis.
- Repeat on the Harmony-integrated multi-region dataset (adding a brain-region covariate), and on
  the SEA-AD MTG and ROSMAP PFC datasets after Cell Type Mapper label transfer (ANCOM-BC2, v2.0.2).

## Stage 5 — Pseudobulk differential expression
- Sum UMI counts per gene per sample per cell type to build pseudobulk pseudo-replicates.
- Retain samples with >=10 nuclei of the target cell type, and subpopulations detected in >=20
  samples with median CPM>=1; apply edgeR `filterByExpr` for further low-count gene filtering.
- Fit glmmTMB (family=nbinom2) negative-binomial mixed models per cell type:
  `counts ~ Braak_stage (or diagnosis) * tissue + age + sex + pmi + (1|individual)`, offset by
  log(TMM-normalized library size) minus log(1e6); categorize Braak_stage/age/pmi prior to fitting
  for convergence.
- Apply two-sided Wald tests; Benjamini-Hochberg-adjust p-values; declare significance at FDR<0.05.

## Stage 6 — Gene-constraint and pathway-enrichment analysis of DEGs
- Compare LOEUF scores (Karczewski et al. 2020) between Up/Down DEG sets and FDR>=5% (non-DE) genes
  via two-sided Wilcoxon rank-sum tests (uncorrected), within glutamatergic neurons.
- Run MAGMA on AD GWAS summary statistics (Wightman et al. 2021) to identify AD-genetically-
  associated pathways (GO_BP/CC/MF, Hallmark, KEGG, REACTOME; Benjamini-Hochberg-corrected); test
  cell-type-specific DEGs for enrichment within these pathways via fgsea.

## Stage 7 — CARTANA in-situ sequencing (spatial) data generation
- Select 155 genes (based on snRNA-seq results and prior literature) to represent all 8 major cell
  classes plus subcluster-discriminating combinations.
- Perform CARTANA in-situ sequencing (probe ligation, rolling-circle amplification, 7 sequential
  fluorescence-labeling/imaging cycles, 20x magnification, Nikon ECLIPSE Ti2) on 13 tissue sections.
- After ISS-probe removal (formamide washes), immunostain the same sections for phospho-tau
  (Ser202/Thr205) and β-amyloid (MOAB-2), plus DAPI nuclear counterstain.
- Align/combine the reference DAPI image with 6 sequencing-cycle images per sample (ISSanalysis
  software) to generate per-cell and per-target-RNA spatial coordinates.
- Build a Halo v3.1 classifier to automatically detect β-amyloid plaques from the immunostaining
  images; export plaque coordinates.

## Stage 8 — CARTANA cell-type classification and per-cell-class Braak-stage validation
- Aggregate pseudobulk snRNA-seq counts per broad cell type; compute a CP10k specificity metric per
  gene per cell type; define broad-cell-type marker genes as CP10k>=0.01 and specificity>0.5,
  restricted to genes also present in the 155-gene CARTANA panel.
- For each CARTANA cell, sum counts across all markers per candidate cell type, z-score, convert to
  a one-sided p-value (via `pnorm`), and assign the cell type label if p<0.05.
- Fit lmerTest linear mixed-effects models (gene expression ~ Braak-stage category + (1|individual))
  per broad cell type, separately for GM and WM, to validate the snRNA-seq-derived proportion/
  expression associations in intact tissue (Fig. 4c).

## Stage 9 — Global and tile-based (plaque-density) CARTANA differential expression
- Sum and normalize (to 6000 counts/section, near the 5649 median) all-cell-class gene counts per
  section; log-transform; test across Braak-stage categories and, separately, low-vs-high pathology
  groups via Wilcoxon rank-sum tests (Benjamini-Hochberg-adjusted).
- Divide tissue into 100x100-pixel (1056 µm²) tiles; classify each as plaque-containing or
  plaque-free; sum/normalize (to 20,000 counts/sample/category) and log(+1)-transform gene counts;
  test via paired Wilcoxon rank-sum tests (Benjamini-Hochberg-adjusted), restricted to amyloid-beta
  plaques (tangle tile-analysis was infeasible due to insufficient tangle-free tiles).

## Stage 10 — Distance-based (proximity) spatial expression modeling
- Compute each cell's Euclidean distance (pixel-area-scaled, 0.1056 µm²/pixel) to the nearest
  plaque and, separately, nearest tangle; empirically bin into close/intermediate/far categories
  (plaques: <70/70-154/>154 µm; tangles: <98/98-262/>262 µm) via the `ntile` function.
- Fit lmerTest linear mixed-effects models (gene expression ~ distance bin + (1|individual)) per
  major cell type, for plaques and tangles separately, and a further model including a
  plaque-distance x tangle-distance interaction term.
- For GFAP specifically, apply kernel density estimation to identify local minima and define
  density-based expression-group thresholds; compute Hartigan's dip statistic per distance bin to
  test distributional unimodality.
