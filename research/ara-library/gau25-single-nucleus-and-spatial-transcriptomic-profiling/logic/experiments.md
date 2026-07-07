# Experiments

Declarative verification/analysis plans reconstructed from the paper's Methods and Results.
Directional only — no exact numerical results (those live in `evidence/`).

## E01: ANCOM-BC trait-association (subpopulation proportion) analysis in GM and WM of the temporal cortex
- **Verifies**: C01, C02, C03
- **Setup**:
  - Model/analysis: ANCOM-BC (Analysis of Compositions of Microbiomes with Bias Correction, version 1.0.5), a log-linear regression model for compositional differential abundance
  - Hardware: Not specified in paper
  - Dataset: 430,271 nuclei retained after QC from 80 samples (40 individuals x GM+WM) of the temporal cortex; AD001 and AD002 excluded for not meeting QC criteria; all non-AD dementia samples removed for this analysis
  - System: Subclusters treated as "taxa"; Braak stage (categorized 0-1 / 2-4 / 5-6) as the covariate of interest; sex, age of death, and postmortem interval (PMI) regressed out (numeric covariates scaled by 2x their standard deviation); analysis run separately per broad cell type and separately for GM and WM
- **Procedure**:
  1. Assign each nucleus to one of 8 broad cell types and one of the corresponding subclusters (via Harmony-integrated Louvain clustering, resolution 0.8, with Random-Forest-based cluster refinement)
  2. Fit a log-linear ANCOM-BC model of subcluster compositional abundance against Braak-stage category, per broad cell type, separately in GM and WM
  3. Perform two-sided Z-tests per subcluster; adjust p-values for multiple comparisons via Benjamini-Hochberg
  4. Repeat with sex (male) as the covariate of interest for a parallel sex-association analysis
- **Metrics**: Estimated log fold-change (beta value) in subcluster abundance between Braak-stage groups; BH-adjusted p-value per subcluster
- **Expected outcome**: Distinct, and in some cases tissue-compartment-specific (including reversed-direction), sets of neuronal and glial subclusters show significant proportional depletion or enrichment with Braak stage in GM vs. WM
- **Baselines**: Braak stage 0-1 group as the reference level for both GM and WM contrasts
- **Dependencies**: none

## E02: Cross-region and cross-cohort replication of subcluster-Braak-stage trait associations
- **Verifies**: C04
- **Setup**:
  - Model/analysis: Harmony (version 0.1.0) integration (30 PCs, resolution 0.8) of the TC dataset with 6 external studies covering entorhinal cortex, prefrontal cortex, superior frontal gyrus, and PFC white matter; Cell Type Mapper algorithm for subcluster label transfer onto two additional external cohorts (SEA-AD MTG, ROSMAP PFC); ANCOM-BC (version 2.0.2) for trait association in the transferred-label datasets
  - Dataset: 959,237 nuclei from TC + 6 external studies pre-QC; 888,784 nuclei retained after doublet removal; 835,413 nuclei (216 samples) after additional metadata-completeness filtering (excluding the Grubman et al. study) used for the multi-region trait-association analysis; SEA-AD MTG cohort (84 individuals); ROSMAP PFC cohort (424 individuals)
  - System: Same ANCOM-BC log-linear model as E01, with an added brain-region covariate for the multi-study integration
- **Procedure**:
  1. Merge TC data with external-study count matrices (via SingleCellExperiment/Seurat object conversion), normalize/scale/PCA (30 PCs), integrate with Harmony (resolution 0.8)
  2. Cluster integrated data (Seurat FindClusters, Louvain, resolution 0.8); annotate broad cell types and (for TC-only) subclusters
  3. Run ANCOM-BC trait association (Braak stage, +brain-region covariate) across the integrated multi-region dataset
  4. Separately, transfer TC subcluster labels onto SEA-AD MTG (84 individuals) and ROSMAP PFC (424 individuals) datasets via Cell Type Mapper (precompute_stats_scrattch + map_to_on_the_fly_markers), then run ANCOM-BC trait association within each transferred-label cohort
- **Metrics**: Estimated log fold-change (beta value) per subcluster per brain region/cohort; BH-adjusted p-value
- **Expected outcome**: THEMIS+/POSTN+ glutamatergic enrichment and PVALB+/TMEM132C+ GABAergic depletion at late Braak stage replicate across brain regions and in both larger external cohorts (SEA-AD MTG, ROSMAP PFC)
- **Baselines**: Cross-region/cross-cohort replication (rather than an external control dataset) is itself the validation baseline
- **Dependencies**: E01

## E03: Pseudobulk negative-binomial mixed-model differential expression analysis across Braak stages, with a Braak-stage x tissue interaction term
- **Verifies**: C05, C06
- **Setup**:
  - Model/analysis: glmmTMB (family = nbinom2) negative binomial mixed model, per cell type: `counts (raw) ~ Braak_stage (or diagnosis) * tissue (gray/white) + age + sex + pmi + (1|individual)`
  - Dataset: Pseudobulk (summed UMI) expression per sample per cell type; samples retained only if they had >=10 nuclei of the given cell type; subpopulations/genes retained if detected in >=20 samples with median CPM>=1; further low-count filtering via edgeR's `filterByExpr`
  - System: log(TMM-normalized library size) minus log(1e6) used as model offset; Braak stage (0-1/2-4/5-6), age (<60/60-80/>80), and PMI (<6/6-8/>8) categorized prior to fitting for convergence
- **Procedure**:
  1. Construct per-sample, per-cell-type pseudobulk count matrices (summed UMIs)
  2. Filter genes/samples per the retention criteria above; TMM-normalize library sizes (edgeR)
  3. Fit glmmTMB negative-binomial mixed model per cell type for two contrasts: Braak 2-4 vs. 0-1, and Braak 5-6 vs. 0-1, each including a Braak-stage x tissue interaction term
  4. Apply two-sided Wald tests per gene; BH-adjust p-values; declare significance at FDR<0.05
- **Metrics**: Number of FDR-significant DEGs per cell type per Braak contrast; number of FDR-significant Braak-stage x tissue interaction DEGs per cell type
- **Expected outcome**: Few DEGs at early Braak stage, restricted to a small number of cell types; substantially more DEGs at late Braak stage, overwhelmingly cell-type-specific; a distinct subset of genes (including FCER1G, APOE, ABCA7) differentially affected by late-stage pathology between GM and WM
- **Baselines**: Braak 0-1 as the reference group for both early- and late-stage contrasts
- **Dependencies**: none

## E04: LOEUF gene-constraint comparison of differentially expressed vs. non-differentially-expressed genes
- **Verifies**: C07
- **Setup**:
  - Model/analysis: Two-sided Wilcoxon rank-sum test (no multiple-testing correction), comparing LOEUF scores (Karczewski et al. 2020) between DEG groups and non-DE (FDR>=5%) genes
  - Dataset: Glutamatergic-neuron DEGs from E03 (Braak 5-6 vs. 0-1, and Braak5-6 x Temporal-Cortex interaction), split into "Up" and "Down" direction groups, each compared against the FDR>=5% (non-significant) gene set
- **Procedure**:
  1. Retrieve LOEUF scores for all tested genes
  2. Partition glutamatergic-neuron genes into Up-DE, Down-DE, and FDR>=5% (non-DE) sets for each of the two contrasts (Braak 5-6; Braak5-6 x Temporal Cortex)
  3. Run pairwise two-sided Wilcoxon rank-sum tests (Up vs. FDR>=5%; Down vs. FDR>=5%) within each contrast
- **Metrics**: Wilcoxon rank-sum p-value per Up/Down-vs-non-DE comparison
- **Expected outcome**: Up-regulated late-Braak-stage and tissue-interaction glutamatergic-neuron genes show significantly lower LOEUF (greater constraint) than non-DE genes
- **Baselines**: FDR>=5% (non-differentially-expressed) glutamatergic-neuron genes as the reference/null comparison group
- **Dependencies**: E03

## E05: MAGMA/fgsea pathway enrichment of differentially expressed genes against AD genetic-risk pathways
- **Verifies**: C08
- **Setup**:
  - Model/analysis: MAGMA (de Leeuw et al. 2015) gene-level genetic association testing on AD GWAS summary statistics (Wightman et al. 2021, 1,126,563 individuals; window 35 kb upstream to 10 kb downstream of each gene), followed by fgsea (Korotkevich et al.) gene set enrichment testing of DEGs against pathways
  - Dataset: GO_BP, GO_CC, GO_MF, Hallmark, KEGG, and REACTOME pathway databases; DEGs from E03 (per cell type, per Braak contrast, per GM/WM-interaction contrast)
- **Procedure**:
  1. Compute gene-level AD-GWAS genetic association scores via MAGMA
  2. Test which pathways (from the six named databases) are enriched for AD genetic risk (BH-corrected)
  3. Test whether cell-type-specific DEGs (from E03) are enriched in the AD-genetically-associated pathways via fgsea, per cell type and per contrast
- **Metrics**: Normalized enrichment score (NES); BH-adjusted enrichment p-value, reported at 10-20% FDR thresholds depending on panel
- **Expected outcome**: Distinct, largely non-overlapping AD-relevant pathway enrichments per cell type (e.g., amyloid-fibril-formation regulation in neurons, lipid/lipoprotein response in microglia/OPCs, vesicle-transport/endocytosis in glutamatergic neurons/astrocytes, tissue-specific amyloid-beta-formation regulation in WM oligodendrocytes)
- **Baselines**: Genome-wide/all-tested-gene background as the enrichment null; cross-cell-type comparison as the specificity check
- **Dependencies**: E03

## E06: CARTANA in-situ sequencing validation of snRNA-seq-derived cell-type-marker-gene Braak-stage associations
- **Verifies**: C09
- **Setup**:
  - Model/analysis: Linear mixed-effects model (lmerTest R package), gene expression ~ Braak-stage category + (1|individual), fit separately per broad cell type in GM and WM
  - Dataset: CARTANA in-situ sequencing (155-gene probe panel) on 13 tissue samples from study donors, spanning controls through Braak stage 6; GM/WM samples from n=11 individuals for this specific validation analysis
  - System: Cells assigned "major class" labels via a marker-gene z-score/p-value approach (cell types 10k-read-normalized pseudobulk specificity metric >0.5, CP10k>=0.01) using the subset of markers also present in the 155-gene CARTANA panel; alternative (non-optimal) marker genes substituted for several subclusters due to probe-design constraints
- **Procedure**:
  1. Perform CARTANA in-situ sequencing (7 sequencing cycles, 20x magnification) and align reference/sequencing images (ISSanalysis software) to obtain per-cell spatial coordinates and gene counts
  2. Immunostain the same sections for amyloid-beta (MOAB-2) and phospho-tau (Ser202/Thr205) after ISS-probe removal
  3. Assign cells to major classes using the marker-based z-score approach
  4. Fit the lmerTest linear mixed-effects model for each of the 155 genes within each major cell class, separately for GM and WM tissue, across Braak-stage categories
  5. Two-sided tests, no multiple-testing correction applied at the per-gene, per-cell-type level
- **Metrics**: Model-derived p-value per gene per cell type per tissue compartment
- **Expected outcome**: Directionally concordant, statistically significant (uncorrected p<0.05) associations between marker-gene expression and Braak stage for the snRNA-seq-derived subclusters/markers found in E01, in both GM and WM
- **Baselines**: Braak stage 0-1 as reference; snRNA-seq-derived direction of effect (E01) as the concordance benchmark
- **Dependencies**: E01, E03

## E07: Global (all-cell-class) CARTANA differential expression across Braak stage and binarized pathology
- **Verifies**: C10, C11
- **Setup**:
  - Model/analysis: Wilcoxon rank-sum test (BH-adjusted), applied to section-level summed and normalized (to 6000 counts/section) log-transformed gene counts, aggregated across all cell classes
  - Dataset: Same 13-individual CARTANA dataset as E06, not stratified by cell type
- **Procedure**:
  1. Sum CARTANA counts per gene per section; normalize to 6000 counts/section (near the median of 5649); log-transform
  2. Test for differences across Braak-stage categories (0-1/2-4/5-6) via Wilcoxon rank-sum test, BH-adjusted
  3. Separately, binarize donors into low- vs. high-pathology groups and repeat the Wilcoxon comparison
  4. Compare the number of nominally significant (uncorrected p<0.05) genes against the null expectation (155 genes x 0.05 per test)
- **Metrics**: Number of genes reaching nominal (uncorrected) significance; number of genes surviving BH correction; fold-enrichment relative to the null expectation
- **Expected outcome**: No genes survive multiple-testing correction at the global (non-cell-type-resolved) level, but a 2-4-fold nominal enrichment above the null is detected for both the Braak-stage and low/high-pathology comparisons, including a directionally unexpected (upregulated) TMEM119 signal discordant with the co-measured homeostatic marker P2RY12
- **Baselines**: Expected number of nominally significant genes under the null (155 tests x 0.05 ≈ 8 genes)
- **Dependencies**: E06

## E08: Distance-based spatial mixed-effects model of gene expression relative to plaque/tangle proximity
- **Verifies**: C12, C13
- **Setup**:
  - Model/analysis: Linear mixed-effects model (lmerTest), gene expression ~ distance-bin (close/intermediate/far) + (1|individual), fit per major cell type; a separate model with a plaque-distance x tangle-distance interaction term; kernel density estimation and Hartigan's dip statistic for testing GFAP expression-distribution modality
  - Dataset: CARTANA 155-gene panel with paired amyloid-beta/tau pathology coordinates; every cell's Euclidean distance to the nearest plaque and nearest tangle computed and categorized into close/intermediate/far bins via empirically-derived cutoffs (plaques: <70 µm / 70-154 µm / >154 µm; tangles: <98 µm / 98-262 µm / >262 µm)
- **Procedure**:
  1. Compute per-cell minimum Euclidean distance to the nearest plaque (and, separately, nearest tangle) using pixel-area-scaled coordinates (0.1056 µm²/pixel)
  2. Categorize each cell into close/intermediate/far distance bins for plaques and, separately, for tangles
  3. Fit the LMM per gene per major cell type, with distance bin as the fixed effect and individual as a random effect, for plaques and tangles separately
  4. Fit an additional LMM including a plaque-distance x tangle-distance interaction term
  5. For GFAP specifically, apply kernel density estimation to identify local minima/expression-group thresholds, then compute Hartigan's dip statistic per distance bin to test unimodality
- **Metrics**: Δ (change in log-transformed expression) per distance-bin contrast (intermediate-vs-close, far-vs-close), per gene per cell type; model-derived p-value; Hartigan's dip statistic per distance bin
- **Expected outcome**: Distinct, cell-type-specific gene sets show proximity-dependent expression gradients for plaques vs. tangles; GFAP shows a significantly higher dip statistic (greater deviation from unimodality) in the plaque-proximal bin than in intermediate/far bins
- **Baselines**: The "close" distance bin serves as the reference level for both intermediate-vs-close and far-vs-close contrasts
- **Dependencies**: E06

## E09: Tile-based (plaque-density) paired differential expression analysis
- **Verifies**: C14
- **Setup**:
  - Model/analysis: Paired Wilcoxon rank-sum test (BH-adjusted), on tile-level pseudobulked, normalized (to 20,000 counts/sample/plaque-category), log(+1)-transformed gene counts
  - Dataset: Tissue divided into 100x100-pixel (1056 µm²) tiles, classified as plaque-containing or plaque-free; analysis restricted to amyloid-beta plaques only (tangle-based tile analysis was not feasible due to insufficient tangle-free tiles in individuals with cortical tangle pathology)
- **Procedure**:
  1. Classify each tile as plaque-containing or plaque-free based on quantitative plaque density
  2. Sum gene counts within each sample x plaque-category group; normalize to 20,000 counts; log(+1)-transform
  3. Test plaque-containing vs. plaque-free tiles via paired Wilcoxon rank-sum test (per gene), BH-adjusted for multiple comparisons
- **Metrics**: Number of genes reaching nominal (uncorrected) significance (p<0.05); number surviving BH correction; fold-enrichment relative to the null expectation
- **Expected outcome**: No genes survive correction, but a nominal (2-fold) enrichment is detected, including microenvironment-level (plaque-density-based, not just nearest-plaque-distance-based) signals such as elevated microglial BIN1 and low-pathology-specific reduced SERPINE1 in plaque-containing tiles
- **Baselines**: Plaque-free tiles from the same samples as the paired reference
- **Dependencies**: E08
