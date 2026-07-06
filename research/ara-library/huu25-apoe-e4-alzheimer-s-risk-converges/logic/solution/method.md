# Methods (detailed, grounded to §Materials and Methods)

All exact QC/count values below are transcribed from the paper's Methods section. This file records
method structure and parameters; result-derived numbers are additionally captured in `claims.md`
and `evidence/`.

## Visium raw processing & QC
- Slide images split into capture areas with `VistoSeg::splitSlide()`; capture areas aligned in Loupe Browser v7.0.1.
- SpaceRanger v2.1.0, GRCh38 + 2020-A annotation. Of 154,752 total spots, 122,742 were in-tissue (median 3,989/sample, min 2,396, max 4,880); counts for 32,006 genes; in-tissue median 3,327 UMIs and 1,573 detected genes.
- QC: spatialLIBD v1.17.0 `add_qc_metrics()`; 143 off-tissue spots removed by manual annotation; SpotSweeper v0.99.5 `localOutliers()` flagged 403 spots (0.3%) as local outliers on low library size / low genes / high mito. Total 544 spots dropped → **122,202 in-tissue spots** (median 3,964/sample, min 2,367, max 4,869).

## Visium clustering
- nnSVG v1.8.0 SVGs: 1,454 genes passed `filter_genes()` in ≥5 samples with average rank <1,500.
- DLPFC layer markers: top 100 enrichment genes per spatialDLPFC domain; 441 already SVGs. Union = **1,765 genes** used for dimensionality reduction.
- PCA (scater v1.30.1); harmony v1.2.0 batch correction `RunHarmony(group.by.vars=sample_id)`.
- BayesSpace v1.11.0 `spatialCluster(nrep=20000)` over k=2..28; optimal **k=9** by `qTune()` negative log-likelihood.
- Annotation: MeanRatio markers (DeconvoBuddies v0.99.10), `registration_wrapper()` (spatialLIBD v1.21.3) pseudobulk + anova/pairwise/enrichment modeling; spatial registration to DLPFC (k=9) and Franjic et al. ERC subset.
- Nuclei/spot: `spaceranger segment` (SpaceRanger v4.0.1) → GeoPandas v1.0.1 spatial join to count nuclei per spot.

## snRNA-seq processing & QC
- CellRanger v7.2.0, GRCh38 + 2020-A. Median depth 525,073,680 reads; median 5,369 UMIs/nucleus; median 2,452 genes/nucleus; 38,480,710 droplets (min 581,462, max 1,732,806).
- emptyDrops (DropletUtils v1.22.0, niters=30000): knee+100 threshold 206–984 UMI; manual knee 200 for 6 samples → **160,743 non-empty droplets** (median 5,222/sample, min 2,169, max 7,847).
- scDblFinder v1.16.0: **10,820 doublets (6.7%)** removed → 149,923 single-nuclei droplets.
- Adaptive 3-MAD QC (scuttle `isOutlier`) on mito%, sum UMI, detected genes → **140,119 nuclei (93.4%)** (median 4,589/donor, min 1,811, max 6,946).

## snRNA-seq clustering
- GLM-PCA: scry v1.14.0 top 2,000 deviant genes → `nullResiduals` → scater `runPCA(ncomponents=100)`; harmony v1.2.1 batch correction.
- Preliminary: scran `buildSNNGraph(k=10)` + igraph `clusterwalktrap()` → 44 clusters; ScType annotation. Quality cutoffs (median + 3·MAD; scDblFinder.score > 0.5): sum UMI non-neuron >1,340.94 / neuron >5,592.43; detected genes non-neuron >1,217.95 / neuron >4,174.27; mito non-neuron <0.4 / neuron <0.53. 29/44 clusters passed → 125,771 nuclei.
- Secondary optimal: k tested 10–30; **k=13** chosen (max mean silhouette 0.049, bluster) → 23 clusters; dropped 1 Oligo cluster → 125,683 nuclei.
- Non-neuronal subclustering: 98,669 non-neuronal nuclei subclustered → 94,990 retained; **total 122,004 nuclei**, 38 fine subclusters across 8 broad cell types (median 3,949/sample, min 1,517, max 6,288).

## Differential expression
- Pseudobulk with spatialLIBD v1.21.5 `registration_pseudobulk(filter_expr=FALSE)` (min_ncells=10); clusters with <2 pseudobulk samples per carrier group excluded.
- Normalization/filtering: edgeR v4.6.2 `calcNormFactors()` + `filterByExpr.DGEList()`.
- Model fit: `voomLmFit(block, adaptive.span=TRUE, sample.weights=TRUE)`; contrasts via limma v3.64.1 `makeContrast`/`eBayes`/`topTable`. Carrier, ancestry-combined, sex-combined models as in study_design.md.

## Composition, functional, trajectory
- Differential proportion: crumblr v1.0.0 (CLR) + variancePartition v1.38.1 `dream`; covariate removal via jaffelab v0.99.34 `cleaningY`.
- GO overrepresentation: clusterProfiler v4.16.0 `compareCluster`; parent terms via rrvgo v1.20.0.
- Trajectory: TSCAN v1.46.0 MST + pseudotime on OPC+Oligo PCs (scuttle `aggregateAcrossCells`).

## Integration
- Spot deconvolution: RCTD (spacexr v1.0.0) `createRctd(UMI_min=2)`, `runRctd(rctd_mode="multi", max_multi_types=5)`.
- Cross-dataset enrichment: `fisher.test(alt="greater")` on 2×2 DEG-overlap tables vs Grubman et al. and Blanchard et al.
- CCC: LIANA+ v1.5.1 `rank_aggregate.by_sample` (use_raw=True); LR pairs kept if magnitude_rank<0.05 in ≥20/30 samples; spatial validation via `bivariate(global_name='morans', n_perms=1000)`.
- MOFA: MOFAcellulaR v0.0.0.9 `create_init_exp`/`prepare_mofa`/`run_mofa` (spikeslab_weights=FALSE, num_factors=7); `get_associations` (linear model for continuous, ANOVA for categorical; BH-corrected).

## Data QC correction (donor drop)
- After clustering, donor "Br1289" showed female sex-specific gene expression despite being recorded male; traced to a case-table typo — actually Br1285, a 17-year-old (outside the study age range) E3/E4 AA female. Dropped from downstream APOE analyses → final n=30. Br1285's data (labeled Br1289) remains valid for atlas/clustering purposes.
