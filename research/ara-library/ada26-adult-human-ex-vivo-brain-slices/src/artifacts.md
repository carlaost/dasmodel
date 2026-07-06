# Artifacts

> Grounding: verified repository `github.com/naomihabiblab/HumanOrganotypicTNF` @ `89ed326`. The two
> runnable R source files are captured in native form under `src/execution/` (not pointed at). This
> file additionally documents the **non-code deliverables** bundled in the repo — the five
> Supplementary Table `.xlsx` workbooks — whose full numeric contents were not transcribed into
> `evidence/` (large gene/pathway matrices; abstract-only compile, no full text to cross-check).

## Captured source code (see `src/execution/`)
- `src/execution/bulk_treatments_plots.R` — bulk RNA-seq figure code: LDA of treatments,
  WGCNA program–trait correlation heatmap, per-program pathway dotplot. (`# Grounding: transcribed`)
- `src/execution/sNucRNAseq_plots.R` — snRNA-seq figure code: cell-type UMAP/marker dotplot/
  proportions, TNFα-vs-control UMAP + NFKB1 density + shared-gene heatmap, per-glial-type volcano
  and pathway barplots, `main_snuc_pipeline()`. (`# Grounding: transcribed`)

## Supplementary Table 1 — Samples included in the study
- **File(s) in repo**: `data/Supplementary Table 1.xlsx`
- **Nature**: dataset / cohort metadata (1 sheet, 9 data rows × 6 columns)
- **What it does / contains**: Per-donor Age, Sex, Area, Type of tumor, and which assay(s) used
  (Bulk RNA-seq / snuc-RNA-seq). Fully transcribed at `evidence/tables/supp_table1_samples.md`.
- **How to use / run**: reference table (no execution).
- **Claims supported**: C01 (platform/cohort)

## Supplementary Table 2 — WGCNA outputs
- **File(s) in repo**: `data/Supplementary Table 2.xlsx`
- **Nature**: analysis-result matrices (4 sheets)
- **What it does / contains**: sheets — "WGCNA- Program-trait correlations", "WGCNA- Program-trait
  p-values", "Gene-Module membership" (genes with significant module membership), "Programs pathway
  enrichment" (over-representation analysis per program). Feeds `bulk_treatments_plots.R`.
- **How to use / run**: inputs to the bulk WGCNA heatmap/dotplot.
- **Claims supported**: C02, C05

## Supplementary Table 3 — Bulk TNFα transcriptomic response
- **File(s) in repo**: `data/Supplementary Table 3.xlsx`
- **Nature**: DE + pathway matrices (2 sheets)
- **What it does / contains**: "bulk transcriptomic response to TNF" (list of differentially
  expressed genes) and "TNF pathway enrichment" (over-representation analysis).
- **How to use / run**: reference tables for the bulk TNFα response.
- **Claims supported**: C02, C05

## Supplementary Table 4 — Cell-type-specific TNFα response (snRNA-seq)
- **File(s) in repo**: `data/Supplementary Table 4.xlsx`
- **Nature**: per-cell-type DE + pathway matrices (6 sheets)
- **What it does / contains**: DE genes and pathway enrichment for Microglia, Astrocytes, and OPCs
  TNFα responses (two sheets each: genes + pathways).
- **How to use / run**: reference tables for the snRNA-seq glial DE (Figure 2).
- **Claims supported**: C03

## Supplementary Table 5 — MultiNicheNet TNFα signaling
- **File(s) in repo**: `data/Supplementary Table 5.xlsx`
- **Nature**: cell-cell communication result matrix (1 sheet, "TNF signaling analysis")
- **What it does / contains**: MultiNicheNet signaling network with prioritization of top
  ligand–receptor interactions between TNFα-treated and control slices.
- **How to use / run**: reference table for the crosstalk/loop interpretation.
- **Claims supported**: C06, C03
