# Environment

This is a computational genomics / spatial-transcriptomics analysis. The concrete artifact is a
runnable R (+ Shell + Python) pipeline released as the `LFF_spatial_ERC` repository (see
`artifacts.md`). The repository (~15 GB, largely committed HTML reports) was **not cloned** here;
the stack below is captured from the paper's §Software and Methods and the repo README (fetched raw
from the `devel` branch). Exact per-analysis versions live in the repo's log files (`sessioninfo::session_info()`).

- **Language/runtime**: R versions 4.3 to 4.5 (Bioconductor 3.18 to 3.21); Python (nuclei-count workflow, LIANA+); Shell (SpaceRanger/CellRanger, cluster job scripts). Repo languages reported by GitHub: R + Shell + Python (dominant listed language: HTML, from committed reports).
- **Framework**: Bioconductor single-cell / spatial ecosystem.
- **Hardware**: Joint High Performance Computing Exchange (JHPCE) cluster, Johns Hopkins Bloomberg School of Public Health. Interactive apps hosted on LIBD's Posit Connect. Internal JHPCE path: `/dcs05/lieber/marmaypag/LFF_spatialERC_LIBD4140/LFF_spatial_ERC/`.
- **Data sources**:
  - GEO GSE307990 — Visium SRT raw data (open metadata/processed; raw reads dbGaP-controlled).
  - GEO GSE308007 — snRNA-seq raw data (open metadata/processed; raw reads dbGaP-controlled).
  - Processed R objects (logcounts) via LIBD Globus endpoint `jhpce#LFF_ERC`.
  - Full processed objects (counts + logcounts) via `spatialLIBD::fetch_data(type="LFF_spatial_ERC_SRT" | "LFF_spatial_ERC_snRNAseq")`, spatialLIBD ≥ v1.23.1.
  - See `data/dataset.md`.
- **Key dependencies (versions as stated in the paper)**:
  - Alignment: SpaceRanger v2.1.0 (+ v4.0.1 `segment`), CellRanger v7.2.0; reference GRCh38, 2020-A.
  - QC / preprocessing: spatialLIBD v1.17.0–v1.21.5, SpotSweeper v0.99.5, nnSVG v1.8.0, DropletUtils v1.22.0, scDblFinder v1.16.0, scuttle v1.12.0/v1.18.0/v1.34.0, scran v1.30.2/v1.34.0, scry v1.14.0, scater v1.30.1, bluster v1.16.0.
  - Integration/batch: harmony v1.2.0/v1.2.1, BayesSpace v1.11.0, RCTD/spacexr v1.0.0.
  - Modeling: edgeR v4.6.2, limma v3.64.1, variancePartition v1.38.1, crumblr v1.0.0, jaffelab v0.99.34, DeconvoBuddies v0.99.10.
  - Trajectory / CCC / integration: TSCAN v1.46.0, LIANA+ v1.5.1, MOFAcellulaR v0.0.0.9.
  - Functional: clusterProfiler v4.16.0, rrvgo v1.20.0.
  - Genetics: Plink v1.9, TOPMed imputation (GRCh38), FLARE, Beagle; 1000 Genomes YRI/CHB/CEU refs.
  - Viz / apps: ComplexHeatmap v2.22.0–2.24.1, ggplot2 v3.5.1/v3.5.2, scDotPlot, iSEE v2.20.0, spatialLIBD v1.21.5 (apps); imaging via ScType brain marker DB, GeoPandas v1.0.1.
- **Protocols**: 10x Visium (User Guide CG000239 Rev D; H&E CG000160 Rev C), 10x Chromium 3' v3.1 (CG000315 Rev E), RNAScope Fluorescent Multiplex v2. Project organization follows the LIBD `template_project`.
- **Random seeds**: Not specified in paper (BayesSpace `nrep=20000`; LIANA+ `n_perms=1000` are stated; explicit RNG seeds are in repo log files, not the manuscript).
- **License**: MIT (source code). Archived on Zenodo (concept DOI 10.5281/zenodo.17108407; version DOI 10.5281/zenodo.17108408).
