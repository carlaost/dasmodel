# Environment

This is a **wet-lab + computational empirical study** (single-nucleus RNA-seq and CARTANA in-situ
sequencing of human post-mortem brain tissue), not a training-run or software-release paper. Per
`sources.yaml` for this ARA (`code: []`, `data: []`, `clinical_trials: []`), **no code repository or
dataset was provided as input** to this compilation — the sections below transcribe the paper's own
stated environment, data-availability, and code-availability information, verified against the PDF
text (Methods, p.12-13; Data/Code availability, p.15), not against an inspected repository. Because no
repository was provided as input, there is **no `src/execution/` code stub** — the paper's ~10-stage
analysis pipeline is prose/procedural and lives in `logic/solution/method.md`; manufacturing a code
stub from that prose would only duplicate it (per Rule 14).

## Wet-lab platform

- **Tissue source**: Netherlands Brain Bank (NBB, Amsterdam); ethics approval VUmc registration
  2009.148.
- **Nuclei isolation**: Nuclei PURE Prep Nuclei Isolation Kit (Sigma-Aldrich), with 0.1% Triton X,
  1 mM DTT, 0.4 U/µl SUPERase-In RNase Inhibitor (Thermo Fisher Scientific) lysis buffer; sucrose
  cushion (1.8 M) centrifugation, 45 min at 16,000 x g, 4°C.
- **Library preparation / sequencing**: ~12,000 nuclei/sample loaded onto the 10x Single Cell Next
  GEM G Chip; Chromium Single Cell 3' Library and Gel Bead v3 kit; Illumina NovaSeq 6000 (NovaSeq
  6000 S2 Reagent Kit v1.5, 100 cycles), targeting a minimum of 30,000 reads/nucleus.
- **CARTANA in-situ sequencing**: Probe-based multiplexed in-situ sequencing (155-gene panel), 7
  sequential fluorescence-labeling/imaging cycles, 20x magnification, Nikon ECLIPSE Ti2 microscope;
  post-ISS immunostaining for β-amyloid (MOAB-2) and phospho-tau (Ser202/Thr205), plus DAPI.
  Source: "Application Note: Mapping brain cell types with CARTANA in situ sequencing on the Nikon
  Ti2-E microscope," Nature (2019), https://www.nature.com/articles/d42473-019-00264-8 [ref 15].

## Computational environment

- **Reference genome/annotation**: GRCh38 (Cell Ranger v3.1.0); Ensembl Homo_sapiens GRCh38.91
  reference annotation, modified to include intronic reads
  (http://ftp.ensembl.org/pub/release-91/gtf/homo_sapiens/).
- **Language/runtime**: R (version 4.0.1 stated for the SingleCellExperiment conversion step).
- **Named software packages/versions** (as stated in Methods):
  - Cell Ranger v3.1.0
  - scDblFinder v1.4.0 (doublet detection)
  - SingleCellExperiment (Bioconductor)
  - Seurat v3.2.0 (`CreateSeuratObject`, `merge`, `FindClusters`, `FindAllMarkers`, `RunHarmony`)
  - Harmony v0.1.0 (batch integration; 30 PCs, resolution 0.8)
  - scran v1.18.7 (`modelGeneVar`, for Random-Forest feature selection)
  - UMAP (McInnes et al. 2018) for 2-D projection (`DimPlot`)
  - dittoSeq (`dittoBarPlot`)
  - ANCOM-BC v1.0.5 (TC-region trait association); ANCOM-BC2 v2.0.2 (cross-region/cross-cohort
    trait association)
  - glmmTMB (Brooks et al. 2017; family=nbinom2, pseudobulk differential expression)
  - edgeR (`filterByExpr`, TMM normalization)
  - MAGMA (de Leeuw et al. 2015; AD-GWAS gene-level association)
  - fgsea (Korotkevich et al.; pathway enrichment)
  - lmerTest (Kuznetsova et al. 2017; linear mixed-effects models for CARTANA validation and
    distance-based spatial models)
  - dplyr (`ntile` function, for empirical distance-bin categorization)
  - Cell Type Mapper (AllenInstitute; `cell_type_mapper.cli.precompute_stats_scrattch`,
    `cell_type_mapper.cli.map_to_on_the_fly_markers`) — label transfer to SEA-AD MTG/ROSMAP PFC
  - Halo v3.1 (image-analysis classifier for automated β-amyloid plaque detection)
  - ISSanalysis software (CARTANA image alignment/combination across sequencing cycles)
- **Hardware**: Not specified in paper (no GPU/CPU/cluster specification given for any
  computational stage).
- **Random seeds**: Not specified in paper.

## Data sources

- **Primary snRNA-seq dataset**: 430,271 nuclei (post-QC) from 80 samples (40 individuals x GM+WM),
  temporal cortex, Netherlands Brain Bank. **Deposited**: European Genome-phenome Archive (EGA,
  hosted by EBI/CRG), accession **EGAD00001009166** (per paper's Data availability statement, p.15
  of 17 — "Single-nuclei RNA-seq data for the Temporal cortex datasets have been deposited at the
  European Genome-phenome Archive... under accession ID- EGAD00001009166").
- **External multi-region integration datasets** (6 studies, 959,237 nuclei pre-QC / 888,784 nuclei
  post-doublet-removal): entorhinal cortex (Leng et al. 2021 [ref 10]; Grubman et al. 2019 [ref 11]),
  prefrontal cortex (Mathys et al. 2019 [ref 5]; Cain et al. 2020 [ref 12]; Zhou et al. 2020
  [ref 13]), superior frontal gyrus (Leng et al. 2021 [ref 10]), deep PFC white matter (Bryois et al.
  2022 [ref 14]).
- **SEA-AD MTG replication cohort**: 84 individuals (Gabitto et al. 2024 [ref 28]).
- **ROSMAP PFC replication cohort**: 424 individuals (Green et al. 2024 [ref 30]).
- **CARTANA spatial cohort**: 13 tissue sections from the study's own NBB donors, 155-gene panel.
- **Source Data file**: The paper states "Source data are provided as a Source Data file" for
  Figs. 1, 2, 3, and 5 captions — this Source Data file is a Nature Communications supplementary
  deliverable, not included in the `paper.pdf` provided as input to this ARA compilation.

## Code availability

- Per the paper's own Code availability statement (p.15 of 17): "The code used to perform the
  analysis described in this study is available at https://github.com/Gaur-et-al."
- **Not verified against an actual repository in this compilation** — no code repository was
  provided as input (`sources.yaml`: `code: []`). Per Rule 16, this URL is transcribed as a stated
  fact from the paper, not confirmed by inspecting the repository's contents; if a discrepancy with
  the paper's methods description were later found upon inspection, it should be flagged rather than
  silently resolved.

## Clinical trials

- None. This is an observational post-mortem tissue study, not a registered clinical trial (per
  `sources.yaml`: `clinical_trials: []`; no NCT identifier appears anywhere in the paper's full text).

## Funding

- NIH grants R01AG066831 (V.M.) and U19AG074862 (V.M.).

## Competing interests

- D.M. was a full-time employee of F. Hoffmann-La Roche Ltd when this study was conducted; D.M. is
  now an employee of Biogen. Remaining authors declare no competing interests.
