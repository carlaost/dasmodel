# Related Work (Typed Dependency Graph)

## RW01: Blanchard et al., 2022 — APOE4 impairs myelination via cholesterol dysregulation in oligodendrocytes
- **DOI**: 10.1038/s41586-022-05439-w (Nature 611, 769–779) — ref 17
- **Type**: baseline / bounds
- **Delta**:
  - What changed: This study compares its neurotypical ERC Oligo.3 E4+ DEGs against Blanchard's PFC AD Oligo DEGs (E3/E4 & E4/E4 vs E3/E3; 20 AD + 12 control) and iPSC-derived Oligos.
  - Why: To test whether risk-stage changes prefigure disease-stage oligodendrocyte changes.
- **Claims affected**: C02, C08
- **Adopted elements**: Concept that APOE4 disrupts oligodendrocyte myelination; used as external enrichment reference. Note: this study did NOT replicate Blanchard's cholesterol-gene upregulation but did replicate myelination-gene downregulation.

## RW02: Grubman et al., 2019 — single-cell atlas of entorhinal cortex in AD
- **DOI**: 10.1038/s41593-019-0539-4 (Nat. Neurosci. 22, 2087–2097) — ref 19
- **Type**: baseline / bounds
- **Delta**:
  - What changed: Used as the primary ERC AD reference (6 AD + 6 controls); Oligo.3 correlated most with Grubman's Oligo "o4" subcluster; enrichment of downregulated Oligo genes.
  - Why: Regional (ERC) comparison of risk vs disease oligodendrocyte signatures.
- **Claims affected**: C08
- **Adopted elements**: Cross-dataset gene-set comparison; subcluster correlation.

## RW03: Kedia & Simons, 2025 — Oligodendrocytes in AD pathophysiology
- **DOI**: 10.1038/s41593-025-01873-x (Nat. Neurosci. 28, 446–456) — ref 20
- **Type**: extends
- **Delta**:
  - What changed: Provides the "vulnerable pre-myelinating oligodendrocyte" hypothesis the paper's Oligo.3 findings support and extend to neurotypical risk.
  - Why: Interpretive frame for maturation-stalled Oligo.3.
- **Claims affected**: C04
- **Adopted elements**: Disease-associated oligodendrocyte state concept; perivascular oligodendrocyte annotation.

## RW04: Huuki-Myers et al., 2024 — data-driven single-cell & spatial map of human PFC
- **DOI**: 10.1126/science.adh1938 (Science 384, eadh1938) — ref 28
- **Type**: imports / baseline
- **Delta**:
  - What changed: The DLPFC spatial reference used for spatial registration of ERC SpDs and for layer-marker gene sets.
  - Why: Annotate ERC domains and contrast ERC's reduced lamination.
- **Claims affected**: C03 (SpD annotation)
- **Adopted elements**: DLPFC BayesSpace k=9 domains; spatialDLPFC modeling results (top-100 enrichment genes).

## RW05: Franjic et al., 2022 — transcriptomic taxonomy of human/macaque/pig hippocampal & entorhinal cells
- **DOI**: 10.1016/j.neuron.2021.10.036 (Neuron 110, 452–469) — ref 29
- **Type**: baseline
- **Delta**:
  - What changed: ERC snRNA-seq reference used for cell-type registration (layer neurons, vascular, inhibitory).
  - Why: Support ERC cell-type and SpD annotations.
- **Claims affected**: C01
- **Adopted elements**: ERC-subset cell-type reference for spatial/single-cell registration.

## RW06: Ramirez Flores et al. — MOFAcellulaR (multicellular factor analysis)
- **DOI**: MOFAcellulaR / eLife (ref 65; builds on Argelaguet et al. MOFA ref 63 and MOFA+ ref 64)
- **Type**: imports (method)
- **Delta**:
  - What changed: Applied MOFAcellulaR to integrate Visium SpD and snRNA-seq subcluster pseudobulk views (7 factors).
  - Why: To find coordinated multicellular signatures across modalities.
- **Claims affected**: C07
- **Adopted elements**: create_init_exp / prepare_mofa / run_mofa; get_associations.

## RW07: Cable et al., 2022 — RCTD robust spot deconvolution
- **DOI**: 10.1038/s41587-021-00830-w (Nat. Biotechnol. 40, 517–526) — ref 41
- **Type**: imports (method)
- **Delta**: Used (spacexr) to deconvolve Visium spots with snRNA-seq references; broad-resolution results confirmed registration; fine-resolution unreliable.
- **Claims affected**: C03 (integration support)
- **Adopted elements**: createRctd / runRctd multi-mode.

## RW08: Dimitrov et al., 2024 — LIANA+ cell-cell communication framework
- **DOI**: 10.1038/s41556-024-01469-w (Nat. Cell Biol. 26, 1613–1622) — ref 59
- **Type**: imports (method)
- **Delta**: Inferred recurrent ligand-receptor pairs; Oligo.3 as frequent source/target; spatial bivariate validation in Visium.
- **Claims affected**: C01 (CCC context)
- **Adopted elements**: rank_aggregate.by_sample; bivariate Moran's scoring.

## RW09: Hoffman & Roussos — crumblr differential proportion analysis
- **DOI**: ref 37 (with variancePartition/dream, ref 121/122)
- **Type**: imports (method)
- **Delta**: CLR-based differential proportion testing of SpDs and subclusters over APOE/sex/age.
- **Claims affected**: C01 (proportion changes: Oligo.1/Oligo.2 decrease in E4+)
- **Adopted elements**: crumblr + dream modeling.

## RW10: Zhao et al., 2021 — BayesSpace spatial clustering
- **DOI**: 10.1038/s41587-021-00935-2 (Nat. Biotechnol. 39, 1375–1384) — ref 25
- **Type**: imports (method)
- **Delta**: Spatially-aware clustering to define the 9 SpDs (k=9 optimal).
- **Claims affected**: C03
- **Adopted elements**: spatialCluster(nrep=20000), qTune.

## RW11: Korsunsky et al., 2019 — Harmony batch integration
- **DOI**: 10.1038/s41592-019-0619-0 (Nat. Methods 16, 1289–1296) — ref 24
- **Type**: imports (method)
- **Delta**: Batch correction of PCs (Visium and snRNA-seq).
- **Claims affected**: C01, C03
- **Adopted elements**: RunHarmony(group.by.vars=sample_id).

## RW12: Pardo et al., 2022 — spatialLIBD
- **DOI**: 10.1186/s12864-022-08601-w (BMC Genomics 23, 434) — ref 26
- **Type**: imports (method/tool)
- **Delta**: Core QC, spatial registration, pseudobulk modeling, gene-set enrichment, and the interactive app.
- **Claims affected**: C03, C08
- **Adopted elements**: add_qc_metrics, registration_wrapper, registration_pseudobulk, gene_set_enrichment.

## RW13: Maynard et al., 2021 — DLPFC spatial transcriptomics
- **DOI**: 10.1038/s41593-020-00787-0 (Nat. Neurosci. 24, 425–436) — ref 27
- **Type**: baseline
- **Delta**: Earlier DLPFC spatial atlas and layer markers used in registration.
- **Claims affected**: C03
- **Adopted elements**: layer marker gene framework.

## RW14: Mathys et al., 2019 — single-cell transcriptomics of AD
- **DOI**: 10.1038/s41586-019-1195-2 (Nature 570, 332–337) — ref 18
- **Type**: baseline
- **Delta**: Prior AD snRNA-seq showing cell-type-specific changes and male-specific Oligo changes; contextual comparison, not directly enriched here.
- **Claims affected**: C06
- **Adopted elements**: Cell-type-specific AD DEG concept.

## RW15: Huuki-Myers et al., 2025 — DeconvoBuddies / deconvolution benchmark
- **DOI**: 10.1186/s13059-025-... (Genome Biol. 26, 88) — ref 40
- **Type**: imports (method)
- **Delta**: MeanRatio marker gene selection for SpDs and subclusters.
- **Claims affected**: C04
- **Adopted elements**: get_mean_ratio().

## RW16: Montagne et al., 2020 — APOE4 blood-brain-barrier dysfunction
- **DOI**: 10.1038/s41586-020-2247-3 (Nature 581, 71–76) — ref 72
- **Type**: extends
- **Delta**: Frame for interpreting vascular-domain and EA-specific extracellular-matrix DEGs.
- **Claims affected**: C03, C05
- **Adopted elements**: APOE4-BBB link.

## RW17: Crowell et al., 2020 — muscat (pseudobulk power)
- **DOI**: 10.1038/s41467-020-19894-4 (Nat. Commun. 11, 6077) — ref 74
- **Type**: bounds
- **Delta**: Basis for attributing low DEG counts in rare subclusters (e.g. vascular, neurons) to insufficient cells per donor.
- **Claims affected**: C06
- **Adopted elements**: pseudobulk power considerations.

## RW18: Huuki-Myers, Eagles, Divecha, Miller & Collado-Torres — LFF_spatial_ERC code/data (this project's own release)
- **DOI**: 10.5281/zenodo.17108407 (concept) / 10.5281/zenodo.17108408 (version) — ref 96
- **Type**: imports (self / artifact)
- **Delta**: The archived analysis code, log files, and processed-data release underpinning every result.
- **Claims affected**: all
- **Adopted elements**: full R/Shell/Python pipeline (see src/artifacts.md).

## Additional citation footprint (briefer)
- refs 1–3: AD epidemiology and disease-modifying therapy (background).
- refs 4–6: ancestry & sex risk modifiers (motivation for stratified cohort).
- refs 7, 22, 23, 34: APOE biology and E2/E4 risk (framing; ref 34 = cell-type-specific APOE4 roles).
- refs 9–15: ERC anatomy and early AD pathology / white-matter myelin changes.
- refs 30–33: cortical/ERC layer marker gene sets (human and rodent).
- refs 43–48, 52, 55, 60, 61, 66–71, 73, 75–80, 85–93: gene-/pathway-specific AD, PD, myelination, caveolae, peroxisome, LRRK2 interpretation references.
- refs 97–136: methods/tooling — Plink (99), TOPMed (100), FLARE (101), Beagle (103), 1000 Genomes (104), VistoSeg (105), SpaceRanger/CellRanger (106,112), SpotSweeper (107), nnSVG (108), scater/scuttle (109), ClinVar/OpenTargets (110), GeoPandas (111), DropletUtils (113), scDblFinder (114), GLM-PCA/scry (115,116), scran/igraph (117,118), ScType (119), bluster (120), variancePartition (121), dream (122), jaffelab/cleanY (123), edgeR (124,125), limma (126), clusterProfiler (127), rrvgo (128), TSCAN (129), deconvolution benchmarks (130,131), R/Bioconductor (132,133), ComplexHeatmap (134), ggplot2 (135), scDotPlot (136).
