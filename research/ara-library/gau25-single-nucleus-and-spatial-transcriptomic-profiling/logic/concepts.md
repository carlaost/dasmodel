# Concepts

## Braak staging as an AD-progression proxy variable
- **Notation**: Braak stage 1-6, binned as 0-1 / 2-4 / 5-6
- **Definition**: A neuropathological staging system assigning a stage (1-6) based on the spatial spread of neurofibrillary tangle (tau) pathology through the brain, with early stages (1/2) confined to entorhinal cortex/hippocampus and later stages (3-6) extending tau pathology to cortical regions including the temporal cortex; used throughout this paper as the primary continuous-to-categorical AD-pathology-progression variable, chosen over amyloid-beta pathology because tangle spread is more stereotyped and post-mortem tau correlates more strongly with cognitive impairment.
- **Boundary conditions**: Collapsed into three discrete bins (0-1, 2-4, 5-6) for all statistical models in this paper (ANCOM-BC trait association, glmmTMB differential expression, lmerTest spatial validation); finer Braak-stage resolution is not modeled.
- **Related concepts**: ANCOM-BC trait association, Pseudobulk differential expression.

## Paired gray matter (GM) / white matter (WM) sampling design
- **Notation**: —
- **Definition**: Each of 40 donors contributed two temporal-cortex samples — gray matter and its associated (subcortical) white matter, both from the middle third of the mid-temporal gyrus — enabling within-donor GM-vs-WM comparison and explicit Braak-stage x tissue interaction-term modeling rather than pooled or GM-only analysis.
- **Boundary conditions**: WM samples are neuron-sparse (dominated by oligodendrocytes), limiting statistical power for WM-specific neuronal-subcluster findings relative to GM.
- **Related concepts**: Braak staging, Pseudobulk differential expression.

## Harmony/Louvain subclustering with Random Forest-based refinement
- **Notation**: Resolution = 0.8 (both broad-cell-type and subcluster-level clustering)
- **Definition**: Batch integration (Harmony, 30 principal components) followed by shared-nearest-neighbor-graph Louvain community detection (Seurat FindClusters, resolution 0.8) to define 8 broad cell types and, per broad cell type, finer subclusters; a post-hoc Random Forest classifier (trained on subclusters with >=50 cells, 75/25 train/test split, using scran-derived highly-variable genes) is used to identify and merge subclusters exhibiting >=10% mutual confusion and UMAP spatial adjacency, refining the final subcluster set.
- **Boundary conditions**: Refinement merges only spatially-adjacent, high-confusion cluster pairs; training is performed prior to final identity-label assignment, so labels are applied after refinement is complete.
- **Related concepts**: Cell Type Mapper label transfer.

## ANCOM-BC trait association (compositional differential abundance)
- **Notation**: beta value (log fold-change in compositional abundance)
- **Definition**: A log-linear regression model (Analysis of Compositions of Microbiomes with Bias Correction, Lin & Peddada 2020) applied to subcluster proportions (per broad cell type) as a function of Braak-stage category, with age, sex, and postmortem interval regressed out; two-sided Z-tests with Benjamini-Hochberg correction identify subclusters whose proportional abundance differs significantly with pathology stage.
- **Boundary conditions**: Detects proportional (relative) shifts among subclusters within a broad cell type, not absolute cell-count changes; cannot by itself distinguish a true compositional shift from differential dissociation susceptibility (motivating the CARTANA spatial validation).
- **Related concepts**: Braak staging, Cell Type Mapper label transfer, CARTANA in-situ sequencing.

## Pseudobulk differential expression with Braak-stage x tissue interaction (glmmTMB)
- **Notation**: counts ~ Braak_stage * tissue + age + sex + pmi + (1|individual); family = nbinom2
- **Definition**: A negative-binomial mixed model (glmmTMB) fit per broad cell type on pseudobulk (summed-UMI) gene counts, offset by log-TMM-normalized library size, including an explicit Braak-stage x GM/WM-tissue interaction term to isolate genes whose AD-pathology response differs by tissue compartment, in addition to the main Braak-stage effect.
- **Boundary conditions**: Requires >=10 nuclei of the target cell type per sample and detection in >=20 samples; the interaction term specifically tests differential response between GM and WM, not a WM-only or GM-only effect in isolation.
- **Related concepts**: Paired GM/WM sampling design, LOEUF gene constraint, MAGMA/fgsea pathway enrichment.

## LOEUF gene constraint score
- **Notation**: LOEUF (loss-of-function observed/expected upper bound fraction)
- **Definition**: A per-gene metric (Karczewski et al. 2020, gnomAD) quantifying the degree to which a gene tolerates loss-of-function variation in the human population; lower LOEUF indicates a more evolutionarily constrained (less variation-tolerant, typically more functionally essential) gene; used here to test whether late-Braak-stage DEGs are more constrained than non-DE genes.
- **Boundary conditions**: A population-genetics-derived constraint metric, not a direct measure of a gene's functional importance in AD or in the brain specifically; comparisons in this paper used two-sided Wilcoxon rank-sum tests without multiple-testing correction.
- **Related concepts**: Pseudobulk differential expression.

## MAGMA / fgsea AD-genetic-risk pathway enrichment
- **Notation**: NES (normalized enrichment score)
- **Definition**: MAGMA (de Leeuw et al. 2015) computes gene-level genetic-association statistics from AD GWAS summary statistics (Wightman et al. 2021, 1,126,563 individuals), which are then used to identify AD-genetically-associated pathways (GO_BP/CC/MF, Hallmark, KEGG, REACTOME); fgsea (Korotkevich et al.) subsequently tests whether cell-type-specific DEGs (from the pseudobulk analysis) are enriched within those AD-genetically-associated pathways.
- **Boundary conditions**: Tests enrichment of transcriptomic DEGs within *genetically* (GWAS-)associated pathways, not direct GWAS-DEG gene overlap; enrichment reflects concordance between a cell type's transcriptional response and independently-derived AD genetic risk architecture.
- **Related concepts**: Pseudobulk differential expression.

## CARTANA in-situ sequencing (ISS) platform
- **Notation**: 155-gene probe panel
- **Definition**: A probe-based, multiplexed in-situ RNA sequencing platform (barcoded gene-specific probe ligation, rolling-circle amplification, 7 sequential fluorescence-labeling/imaging cycles at 20x magnification) applied to 13 tissue samples spanning control through Braak stage 6, on the same sections subsequently immunostained for amyloid-beta (MOAB-2) and phospho-tau (Ser202/Thr205), enabling joint spatial localization of gene expression and pathology within the same tissue section.
- **Boundary conditions**: Probe-design constraints required substituting alternative (non-optimal) marker genes for several snRNA-seq-derived subclusters; sparse per-cell gene detection precluded definitive assignment of every cell to an snRNA-seq-derived subcluster (only to broad "major class" labels), and the platform is limited to 2-D tissue sections (no 3-D pathology context).
- **Related concepts**: ANCOM-BC trait association, Distance-based spatial model, Tile-based spatial model.

## Cell Type Mapper label transfer
- **Notation**: —
- **Definition**: An Allen Institute algorithm (precompute_stats_scrattch + map_to_on_the_fly_markers commands) used to transfer this study's TC-derived subcluster taxonomy onto external single-nucleus datasets (SEA-AD middle temporal gyrus, ROSMAP prefrontal cortex) as a reference-to-query mapping, enabling replication of trait-association findings in independently collected, differently-sized cohorts without re-deriving a subcluster taxonomy from scratch in each dataset.
- **Boundary conditions**: Mapping quality depends on transcriptomic similarity between the reference (TC) and query (MTG/PFC) datasets/regions; assessed here via visual/quantitative concordance (Supplementary Fig. 3a-b, not included in the provided PDF) prior to running trait association on the transferred labels.
- **Related concepts**: Harmony/Louvain subclustering, ANCOM-BC trait association.

## Distance-based spatial model (plaque/tangle proximity)
- **Notation**: Close / Intermediate / Far distance bins (plaques: <70 µm / 70-154 µm / >154 µm; tangles: <98 µm / 98-262 µm / >262 µm)
- **Definition**: A linear mixed-effects model (lmerTest) testing cell type-specific gene expression as a function of each cell's empirically-binned Euclidean distance to the nearest amyloid-beta plaque (or, separately, nearest tau tangle), including a plaque-distance x tangle-distance interaction-term variant, to identify genes whose expression varies specifically with physical proximity to a pathological inclusion.
- **Boundary conditions**: Distance cutoffs are empirically derived from the overall distance distribution (not a pre-registered biological threshold); computed per-cell using a fixed area-per-pixel scaling (0.1056 µm²/pixel); analysis performed in GM only.
- **Related concepts**: CARTANA in-situ sequencing, Tile-based spatial model, GFAP expression bimodality.

## Tile-based (plaque-density) spatial model
- **Notation**: 100x100 pixel tiles (1056 µm² each)
- **Definition**: An alternative (to per-cell distance) spatial analysis dividing tissue into fixed-size tiles and classifying each as plaque-containing or plaque-free, then testing paired plaque-vs-no-plaque tile-level pseudobulked gene expression, capturing local plaque *density* effects (not just distance to the single nearest plaque).
- **Boundary conditions**: Applied only to amyloid-beta plaques, not tangles, because individuals with cortical tangle pathology lacked sufficient tangle-free tiles for a paired comparison.
- **Related concepts**: Distance-based spatial model, CARTANA in-situ sequencing.

## GFAP expression bimodality (Hartigan's dip statistic)
- **Notation**: Dip statistic (Hartigan's dip test)
- **Definition**: A nonparametric test for departure from unimodality in a distribution; applied here to the plaque-distance-binned GFAP expression distribution to test whether the counterintuitive average finding (higher bulk GFAP transcript farther from plaques) reflects a genuinely bimodal (GFAP-high and GFAP-low astrocyte subpopulations both elevated) rather than unimodal-but-shifted distribution specifically near plaques.
- **Boundary conditions**: A distributional-shape diagnostic, not itself a differential-expression test; used qualitatively (comparing median dip values across three distance bins) rather than with a formal significance threshold in this paper.
- **Related concepts**: Distance-based spatial model.

## THEMIS+/POSTN+ deep-layer glutamatergic resilience signature
- **Notation**: —
- **Definition**: A deep-cortical-layer (L5-6) glutamatergic neuronal subcluster, marked by co-expression of THEMIS and POSTN (and co-expressing NR4A2/NTNG2), that is overrepresented (rather than depleted) at late Braak stages in GM in the TC cohort, and which replicates as an enriched (not depleted) population across multiple independent brain regions and in two much larger external cohorts (SEA-AD MTG n=84; ROSMAP PFC n=424) — proposed as a candidate AD-resistant excitatory neuronal subtype.
- **Boundary conditions**: Defined and validated at the level of relative proportional enrichment with Braak stage, not by a direct causal or mechanistic resilience assay; cross-validated in the CARTANA spatial data via an alternative marker combination (PPP1R1A + CC2D1B) necessitated by probe-design constraints on the original snRNA-seq markers.
- **Related concepts**: ANCOM-BC trait association, Cell Type Mapper label transfer, CARTANA in-situ sequencing.
