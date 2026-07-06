---
title: "APOE E4 Alzheimer's Risk Converges on an Oligodendrocyte Subtype in the Human Entorhinal Cortex"
authors: [Louise A. Huuki-Myers, Heena R. Divecha, Svitlana V. Bach, Madeline R. Valentine, Nicholas J. Eagles, Bernard Mulvey, Rahul A. Bharadwaj, Ruth Zhang, James R. Evans, Melissa Grant-Peters, Ryan A. Miller, Joel E. Kleinman, Shizhong Han, Thomas M. Hyde, Stephanie C. Page, Daniel R. Weinberger, Keri Martinowich, Mina Ryten, Kristen R. Maynard, Leonardo Collado-Torres]
year: 2025
venue: "bioRxiv (preprint, not peer reviewed)"
doi: "10.1101/2025.11.20.689483"
ara_version: "1.0"
domain: "Neuroscience / spatial transcriptomics & single-nucleus RNA-seq (Alzheimer's disease genetic risk)"
keywords: [Alzheimer's disease, spatially-resolved transcriptomics, APOE, postmortem human brain, single-nucleus RNA-sequencing, entorhinal cortex, oligodendrocyte, myelination, ancestry, MOFA]
claims_summary:
  - "APOE E4+ (vs E2+) differential expression in the ERC concentrates in a single non-myelinating oligodendrocyte subcluster, Oligo.3 (679 up / 343 down DEGs, FDR<0.05)."
  - "In spatial (Visium) data, APOE-dependent DEGs are highest in the vascular domain Vasc~Sp9D8 (22 up / 8 down) and the U-fiber white matter domain WM.uf~Sp9D7, enriched for myelination GO terms."
  - "Oligo.3 is transcriptionally the most OPC-proximal oligodendrocyte subcluster (trajectory analysis), supporting a non-myelinating / pre-myelinating identity whose maturation appears stalled in E4+ carriers."
  - "APOE-associated DEGs are strongly modified by ancestry (largely non-overlapping AA vs EA sets) and by sex (male-dominated), across both spatial domains and cell types."
  - "A MOFA multicellular factor (factor 3) spanning non-myelinating oligodendrocytes (Oligo.3-5) and white matter domain WM~Sp9D6 associates with APOE carrier status (p=0.014) and pTau pathology (FDR<0.05)."
  - "Oligo.3 E4+ DEGs replicate downregulation of myelination genes (PLP1, OPALIN) seen in two published AD snRNA-seq datasets (Grubman et al.; Blanchard et al.)."
abstract: "The entorhinal cortex (ERC) is implicated in early progression of Alzheimer's disease (AD). Here we investigated the impact of established biological risk factors for AD, including APOE genotype (E2 versus E4 alleles), sex, and ancestry, on gene expression in the human ERC. We generated paired spatially-resolved transcriptomics (SRT) and single-nucleus RNA sequencing data (snRNA-seq) in postmortem human ERC tissue from middle aged brain donors with no history of AD. APOE-dependent changes in gene expression predominantly mapped to a transcriptionally-defined oligodendrocyte subtype, which varied substantially with ancestry, and suggested differences in oligodendrocyte differentiation and myelination. Integration of SRT and snRNA-seq data identified a common gene expression signature associated with APOE genotype, which we localized to the same oligodendrocyte subtype and a white matter spatial domain. This suggests that AD risk in ERC may be associated with disrupted oligodendrocyte function, potentially contributing to future neurodegeneration."
---

# APOE E4 Alzheimer's Risk Converges on an Oligodendrocyte Subtype in the Human Entorhinal Cortex

## Overview

This preprint builds the first paired spatial transcriptomics (10x Visium) + single-nucleus
RNA-seq (10x Chromium) molecular atlas of the human entorhinal cortex (ERC) from 30 neurotypical
postmortem donors stratified by AD genetic risk: APOE carrier status (E2+ n=14 vs E4+ n=16),
ancestry (African n=14, European n=16), and sex (21 male, 9 female). It maps 9 spatial domains
(SpDs) and 38 fine cell-type subclusters, then runs pseudobulk differential expression between
APOE carrier groups. The central finding is that APOE E4+ associated transcriptional changes
converge on a single non-myelinating oligodendrocyte subcluster (Oligo.3) and on white
matter / vascular spatial domains, are enriched for myelination and oligodendrocyte-differentiation
GO terms, are strongly modified by ancestry and sex, and are recovered independently by a MOFA
multicellular factor that also tracks pTau pathology. The work is a data-science / genomics
artifact: a runnable R (+ Shell + Python) analysis pipeline (GitHub / Zenodo) and open processed
data (two GEO series + interactive apps).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) with grounded numeric sources |
| [concepts.md](logic/concepts.md) | 10 genuine technical terms defined |
| [experiments.md](logic/experiments.md) | 8 declarative analysis plans (E01–E08) |
| [related_work.md](logic/related_work.md) | Typed dependency graph (RW01–RW18) |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, assay, and analysis-pipeline design |
| [solution/method.md](logic/solution/method.md) | The clustering / DGE / integration methods in detail |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, boundary conditions, limitations |

### Implementation Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | R/Bioconductor + Python/Shell stack, tool versions, data sources | all |
| [artifacts.md](src/artifacts.md) | The `LFF_spatial_ERC` analysis repo (GitHub + Zenodo) + interactive apps | all |

### Data Layer (`/data`)
| File | Description |
|------|-------------|
| [dataset.md](data/dataset.md) | GSE307990 (Visium SRT) + GSE308007 (snRNA-seq); processed R objects; access levels |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG (17 nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of the 6 main-text figures + supplementary-object accounting |
| figures/figure1.md … figure6.md | Main-text Figures 1–6 (markdown + `.png`) |
