---
title: "Adult human ex vivo brain slices for dissecting glial biology and multicellular communication"
authors: [Miriam Adam, Inbar Shapira, Hanan Schoffman, Gavin Piester, Zhaorong Li, Francisco J. Quintana, Iddo Paldor, Tal Shahar, Naomi Habib]
year: 2026
venue: "bioRxiv (preprint, v1, not peer reviewed)"
doi: "10.64898/2026.01.12.698855"
ara_version: "1.0"
grounding: abstract-only
domain: "Neuroscience / glial biology — adult human organotypic brain slice culture; bulk & single-nucleus RNA-seq; cell-cell communication"
keywords: [organotypic brain slice, glia, microglia, astrocytes, OPCs, TNFα, neuroinflammation, snRNA-seq, WGCNA, MultiNicheNet, ex vivo, neurosurgical resection]
claims_summary:
  - "Adult human organotypic brain slice cultures from neurosurgical resections preserve tissue architecture and mature cell identities over weeks."
  - "Cultures elicit stimulus-specific transcriptional programs in response to diverse stressors (TNFα, LPS, H₂O₂, BLM)."
  - "TNFα drives coordinated glial responses among microglia, astrocytes, and OPCs, including pro-/anti-inflammatory loops."
  - "The slice-derived coordinated glial TNFα response is validated in postmortem human brains."
  - "WGCNA of bulk RNA-seq defines shared and stimulus-specific gene programs across treatments."
  - "MultiNicheNet prioritizes ligand-receptor interactions that differ between TNFα-treated and control slices."
abstract: "Glial cells are critical modulators of brain function in health, aging, and disease. This study establishes a robust ex vivo platform for cell-type-specific interrogation of glial responses and multicellular crosstalk, based on adult human organotypic brain slice cultures from neurosurgical resections. Cultures preserve tissue architecture and mature cell identities over weeks, elicit stimulus-specific transcriptional programs to diverse stressors, and resolve coordinated glial responses to TNFα (validated in postmortem human brains), including pro-/anti-inflammatory loops among microglia, astrocytes, and OPCs."
---

# Adult human ex vivo brain slices for dissecting glial biology and multicellular communication

## Grounding note

**This is an abstract-only compile.** No licit open-access copy of the full text could be
retrieved: the bioRxiv PDF and JATS full text sit behind a Cloudflare challenge (403) and Unpaywall
does not index the `10.64898` DOI prefix, so `paper.pdf` was unavailable to the compiler
(`pdf.downloaded: false` in `sources.yaml`). The cognitive layer is therefore populated to the
level the **abstract** supports, augmented by the authors' **verified analysis code repository**
(`github.com/naomihabiblab/HumanOrganotypicTNF`, corresponding author N. Habib) and the
**Supplementary Tables 1–5** bundled in that repo — both first-class grounded inputs. Where a fact
would require the paper's running text, this ARA writes "Not available from provided input (no full
text)" rather than guessing. The paper's numbered main-text Tables/Figures could **not** be
extracted (no full text); see `evidence/README.md`.

## Overview

The paper establishes an **adult human organotypic brain slice culture** platform derived from
living neurosurgical resection tissue, intended as an ex vivo system for cell-type-specific study of
glial biology and multicellular crosstalk. Per the abstract, the cultures preserve tissue
architecture and mature cell identities over weeks, mount stimulus-specific transcriptional programs
to diverse stressors, and resolve a coordinated glial response to TNFα — spanning pro-/anti-
inflammatory loops among microglia, astrocytes, and OPCs — that the authors validate in postmortem
human brains. The verified code repository shows the analytical backbone: WGCNA of bulk RNA-seq
across five treatment conditions (Control, BLM, H₂O₂, LPS, TNFα) defining gene programs, cell-type-
specific TNFα differential-expression from snRNA-seq, validation against external datasets, and
MultiNicheNet cell-cell communication analysis.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 8 key technical concepts |
| [experiments.md](logic/experiments.md) | 6 declarative verification plans (E01–E06) |
| [related_work.md](logic/related_work.md) | Typed dependency graph + external validation datasets |
| [solution/study_design.md](logic/solution/study_design.md) | Platform + analysis design (reconstructed from repo) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | R analysis stack, data sources, protocols | — |
| [execution/bulk_treatments_plots.R](src/execution/bulk_treatments_plots.R) | Bulk RNA-seq: LDA, WGCNA program-trait heatmap, pathway dotplot | C02, C05 |
| [execution/sNucRNAseq_plots.R](src/execution/sNucRNAseq_plots.R) | snRNA-seq: cell-type UMAP/markers, TNF-vs-control DE, volcano, pathways | C01, C03 |
| [artifacts.md](src/artifacts.md) | Repo scripts + Supplementary Tables 1–5 (.xlsx) | C01–C06 |

### Data Layer (`/data`)
| File | Description |
|------|-------------|
| [dataset.md](data/dataset.md) | Sample cohort (neurosurgical resections), sequencing data, external datasets |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 11-node research DAG (mostly inferred; repo-grounded where explicit) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index + abstract-only completeness note |
| [tables/supp_table1_samples.md](evidence/tables/supp_table1_samples.md) | Supplementary Table 1 — sample cohort (from repo) |
