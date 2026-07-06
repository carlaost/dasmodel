# Environment

> Grounding: reconstructed from the verified analysis repository (`library(...)` calls in the two R
> scripts) and `sources.yaml`. Exact package versions, R version, OS, and hardware are **Not
> available from provided input (no full text; repo has no lockfile/DESCRIPTION/sessionInfo)**.

- **Language/runtime**: R (version not specified in repo). Analysis/plotting only; wet-lab work
  (slice culture, sequencing) is upstream and not code.
- **Framework**: Bioconductor/CRAN R ecosystem for single-cell and bulk transcriptomics.
- **Hardware**: Not specified in repo (typical: workstation/HPC for snRNA-seq; not stated).
- **Key dependencies** (from `library()` calls; versions not pinned):
  - snRNA-seq (`sNucRNAseq_plots.R`): `Seurat`, `ggplot2`, `dplyr`, `cowplot`, `pheatmap`,
    `ComplexHeatmap`, `gridExtra`, `viridis`, `Nebulosa`
  - bulk (`bulk_treatments_plots.R`): `ComplexHeatmap`, `circlize`, `dplyr`, `readr`, `tidyr`,
    `ggplot2`, `viridis`, `MASS` (LDA)
  - Named in README but not in the two released scripts: WGCNA and MultiNicheNet (their construction
    code is not included in the repo — the released scripts consume precomputed inputs).
- **Data sources**:
  - **Primary (generated in this study)** — adult human organotypic brain slice **bulk RNA-seq** and
    **snRNA-seq**. No public accession located; access: **unknown/likely embargoed** (no
    GEO/SRA/EGA/ArrayExpress id in repo, Europe PMC PPR1228173 `hasData=N`). Recorded as unavailable
    rather than fabricated (`sources.yaml` → `data[0].identifier: null`).
  - **Bundled supplementary data (open, in repo)** — `data/Supplementary Table 1–5.xlsx` (see
    `src/artifacts.md`, `data/dataset.md`).
  - **Precomputed analysis inputs referenced by scripts (not all in repo)** — `LDA_treatments.csv`,
    `WGCNA_program_trait_correlations.csv`, `WGCNA_program_trait_p_values.csv`, per-program pathway
    `*.csv`, `TNF.rds` Seurat object, DE-results folder.
  - **External validation datasets (public, reused; access per original source)** — mouse microglia;
    human iPSC-derived astrocytes; COVID-19 postmortem human brain; large AD snRNA-seq cohorts
    (specific accessions Not available from provided input).
- **Protocols**: Analysis pipeline = LDA + WGCNA (bulk) → cell-type annotation + TNFα-vs-control DE
  (snRNA-seq) → external-dataset validation → MultiNicheNet cell-cell communication. Wet-lab
  protocol (slicing, culture, dosing, timepoints): Not available from provided input.
- **Random seeds**: Not specified in repo.
- **Code location**: `github.com/naomihabiblab/HumanOrganotypicTNF` (verified; corresponding-author
  lab). Captured at commit `89ed326` (2026-02-22). Both scripts transcribed under `src/execution/`.
- **Clinical trials**: None (basic-science / methods paper; no NCT ids — `sources.yaml`
  `clinical_trials: []`).
