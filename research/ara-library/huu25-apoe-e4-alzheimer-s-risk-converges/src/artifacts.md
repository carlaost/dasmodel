# Artifacts (released deliverables)

The concrete implementation of this work is the `LFF_spatial_ERC` analysis repository plus derived
processed data and interactive apps. Per the compilation instructions the repo (~15 GB, mostly
committed HTML reports) was **not cloned**; it is described here and grounded in the GitHub repo
listing (default branch `devel`) and the raw README. Top-level layout and the `code/` subdirectory
list below were verified via the GitHub contents API on 2025-07-05; processed-data file paths are
transcribed from the README.

## LFF_spatial_ERC analysis pipeline (R + Shell + Python)
- **File(s) in repo**: GitHub `LieberInstitute/LFF_spatial_ERC` (default branch `devel`). Verified top-level entries: `code/`, `processed-data/`, `raw-data/`, `external-data/`, `plots/`, `img/`, `_jhpce_org/`, `utils/` (under code), `LFF_spatial_ERC.Rproj`, `README.md`, `LICENSE`, `header.html`, `.gitignore`.
- **Nature**: Full end-to-end analysis pipeline (specialized to this project's data, not a general-purpose tool).
- **What it does / contains** — `code/` numbered stages (verified via API):
  - `00_project_prep`, `01_spaceranger`, `02_build_spe`, `02.1_spe_compare_trim` — Visium alignment & SpatialExperiment build.
  - `03_cellranger`, `04_snRNA-seq` — snRNA-seq alignment, QC, clustering, subcluster annotation.
  - `05_spe_correct_cluster` — Visium batch correction + BayesSpace clustering + SpD modeling.
  - `06_iSEE_app`, `07_spatialLIBD_app`, `23_spatialLIBD_app_Xenium` — interactive app builders.
  - `08_pseudoBulkDGE_sn`, `09_pseudoBulkDGE_Visium`, `12_voomLmFit`, `13_compile_DGE` — pseudobulk differential expression.
  - `10_dreamlet_sn`, `11_dreamlet_Visium` — dreamlet DE (alternative modeling).
  - `14_MOFA` — multicellular factor analysis (Figure 6).
  - `15_spot_deconvolution` — RCTD.
  - `16_nuclear_counts` — Python nuclei-per-spot workflow.
  - `17_cell_cell_comm`, `24_xenium_liana` — LIANA+ CCC.
  - `18_LDSC` — stratified LD-score regression.
  - `19_other_Oligo`, `20_NMF`, `22_Mediation`, `23_hdWGCNA`, `25_Seurat` — additional oligodendrocyte / factorization / mediation / network analyses.
  - `21_Xenium` — Xenium in situ analysis.
  - `VistoSeg`, `utils` — image processing helpers and shared utilities.
- **How to use / run**: `git clone` (README notes this may take up to an hour due to size); open `LFF_spatial_ERC.Rproj`; run stage scripts on an HPC/JHPCE-like environment. Per-stage software versions are in committed log files. Note: "this code is specialized for this project's data, and will need to be adapted to run on other datasets."
- **Claims supported**: all (C01–C08).

## Released processed data objects
- **File(s) in repo / release**:
  - SRT: `processed-data/spe_objects/spe_ERC_annotated` (SpatialExperiment, dim 30494 × 122202); pre-QC `spe_raw.rds` (~4 GB, not on GitHub).
  - snRNA-seq: `processed-data/sce_objects/sce_ERC_subcluster` (SingleCellExperiment, dim 38606 × 122004; ~36 GB, not on GitHub).
  - Pseudobulk + modeling: `processed-data/04_snRNA-seq/29_sn_subcluster_model_pseudobulk/*.rds` (cell-type / subcluster pseudobulk + modeling); `processed-data/05_spe_correct_cluster/20_model_pseudobulk_anno/spe_pseudobulk-SpD.rds` + `modeling_results-SpD.rds`.
  - Sample tables: `processed-data/04_snRNA-seq/erc_sn_sample_info.csv`, `processed-data/02_build_spe/sample_info.csv`.
- **Nature**: Bioconductor R data objects (HDF5-backed) + CSV metadata.
- **What it does / contains**: annotated spatial + single-nucleus objects and pseudobulk modeling results used to generate all figures.
- **How to use / run**: `HDF5Array::loadHDF5SummarizedExperiment(...)`; or `spatialLIBD::fetch_data(type="LFF_spatial_ERC_SRT" | "LFF_spatial_ERC_snRNAseq")` (spatialLIBD ≥ v1.23.1); logcounts-only versions via LIBD Globus `jhpce#LFF_ERC`.
- **Claims supported**: all.

## Interactive web applications
- **File(s) in repo**: `code/06_iSEE_app`, `code/07_spatialLIBD_app` (builders).
- **Nature**: Shiny apps (spatialLIBD + iSEE) hosted on LIBD Posit Connect.
- **What it does / contains**:
  - `LFF_ERC_Visium` (spatialLIBD): 31 post-QC Visium samples with clustering + modeling — interactive.libd.org/LFF_ERC_spatialLIBD-app/
  - `LFF_ERC_Visium_QC`: pre-QC Visium — libd.shinyapps.io/LFF_ERC_Visium_QC/
  - `iSEE`: snRNA-seq for 31 samples — interactive.libd.org/LFF_ERC_iSEE-app/
- **How to use / run**: open the hosted URLs (from research.libd.org/LFF_spatial_ERC/#interactive-websites).
- **Claims supported**: C01, C03, C04 (exploration/verification of subcluster and SpD expression).

## Zenodo archive
- **File(s) in repo**: snapshot of the GitHub repo.
- **Nature**: Permanent archive (MIT license).
- **What it does / contains**: `preprint-v1.0.0` release of the pipeline + logs.
- **How to use / run**: download from Zenodo. Concept DOI 10.5281/zenodo.17108407 (README badge, ref 96); version/record DOI 10.5281/zenodo.17108408 (Zenodo record page and compilation brief). Both refer to the same project archive (Zenodo concept vs version DOI); recorded here rather than silently choosing one.
- **Claims supported**: all.
