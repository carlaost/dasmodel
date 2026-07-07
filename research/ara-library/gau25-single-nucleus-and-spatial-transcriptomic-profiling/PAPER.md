---
title: "Single-nucleus and spatial transcriptomic profiling of human temporal cortex and white matter reveals key associations with AD pathology"
authors: [Pallavi Gaur, Julien Bryois, Daniela Calini, Lynette C. Foo, Jeroen J. M. Hoozemans, Archana Yadav, Dheeraj Malhotra, Vilas Menon]
year: 2025
venue: "Nature Communications"
doi: "10.1038/s41467-025-65350-6"
ara_version: "1.0"
domain: "Single-nucleus and spatial transcriptomics — Alzheimer's disease neuropathology in human temporal cortex gray and white matter (snRNA-seq + CARTANA in-situ sequencing)"
keywords: [Alzheimer's disease, single-nucleus RNA-seq, spatial transcriptomics, CARTANA, white matter, gray matter, Braak stage, temporal cortex, cell-type heterogeneity, amyloid plaques, neurofibrillary tangles]
claims_summary:
  - "Multiple neuronal (RORB+/IL1RAPL2+, SPARCL1+, COL5A2+, GLIS3+, GNAL+, TLL1+ glutamatergic; PVALB+, SPARCL1+ GABAergic) and glial (RPL19+ microglia) subpopulations are depleted, while THEMIS+/POSTN+ deep-layer glutamatergic neurons, a SST+/THSD7B+/TRHDE+ GABAergic subpopulation, HSPA1A+ OPCs, MGP+ pericytes, and TNC+ astrocytes are enriched, at late Braak stage in gray matter (n=36 individuals, ANCOM-BC)."
  - "White matter shows distinct, and for RORB+/IL1RAPL2+ neurons opposite-direction, Braak-stage associations compared to gray matter."
  - "THEMIS+/POSTN+ enrichment and PVALB+/TMEM132C+ depletion replicate across independent brain regions and in two much larger external cohorts (SEA-AD MTG n=84; ROSMAP PFC n=424) after Cell Type Mapper label transfer."
  - "Pseudobulk differential expression yields only 17 FDR-significant DEGs at early Braak stage (2-4 vs 0-1) versus 1230 at late Braak stage (5-6 vs 0-1), ~90% (1102/1230) of which are cell-type-specific; 644 genes are additionally affected differently by late-stage pathology between GM and WM (n=39 individuals, glmmTMB)."
  - "Late-Braak-upregulated glutamatergic-neuron genes are significantly more evolutionarily constrained (lower LOEUF) than non-DE genes (p=3.5e-09)."
  - "CARTANA in-situ sequencing (155-gene panel, 13 individuals, n=11 for validation) confirms directionally concordant, statistically significant marker-gene-Braak-stage associations in intact tissue for genes including ACTG1, CC2D1B, PPP1R1A, CD74, P2RY12, GFAP."
  - "Distance-based and tile-based spatial models identify cell-type-specific gene-expression gradients with proximity to amyloid plaques and tau tangles (e.g. NEFL/NEFM near plaques, THEMIS/GFAP/PLP1 far from tangles), including a counter-intuitive GFAP finding reconciled via a bimodal expression-distribution analysis (Hartigan's dip statistic)."
abstract: "Alzheimer's disease, the leading cause of dementia in the elderly, is a neurodegenerative disorder that has been studied to uncover therapeutic pathways through its molecular and cellular hallmarks. Here, we present a comprehensive investigation of cellular heterogeneity from the temporal cortex region of 40 individuals, comprising healthy donors and individuals with differing AD pathology. Using single-nucleus transcriptomic analysis of 430,271 nuclei from both gray and white matter of these individuals, we identified cell type-specific subclusters in both neuronal and glial cell types with varying degrees of association with AD pathology. We extended this analysis by performing multiplexed in situ hybridization using the CARTANA platform, capturing 155 genes in 13 individuals with differing tau pathology. We not only replicated snRNA data key findings from our spatial data analysis but also identified a set of cell type-specific genes that show selective enrichment or depletion near pathological inclusions. While the pathogenesis of Alzheimer's disease (AD) has been extensively studied, the predominant focus has traditionally been on gray matter alterations. Here, authors use single-nucleus and spatial transcriptomic profiling of the human brain's temporal cortex and white matter to uncover cell type specific changes and their associations with Alzheimer's pathology."
---

# Single-Nucleus and Spatial Transcriptomic Profiling of Human Temporal Cortex and White Matter Reveals Key Associations with AD Pathology

## Overview

This is an **empirical/observational biology paper** (not a training-run or software paper): single-nucleus
RNA-seq (snRNA-seq) plus targeted in-situ sequencing (CARTANA) profiling of human post-mortem brain
tissue. The study profiles paired gray matter (GM) and white matter (WM) samples from the mid-temporal
cortex of **40 individuals** (80 samples total: controls and individuals across Braak stages 1-6),
retaining **430,271 nuclei** after QC, segregated into 8 broad cell types and further subclustered
(20/22/7/5/4/3/3/6 subpopulations for glutamatergic neurons/GABAergic neurons/microglia/astrocytes/
oligodendrocytes/OPCs/endothelial cells/pericytes respectively). Cluster-proportion (ANCOM-BC) and
pseudobulk differential-expression (glmmTMB, with an explicit Braak-stage x tissue interaction term)
analyses identify cell-type- and tissue-compartment-specific AD-pathology associations, which are then
(a) replicated across 6 external multi-region studies plus two much larger external cohorts (SEA-AD
MTG n=84; ROSMAP PFC n=424) via Harmony integration and Cell Type Mapper label transfer, and (b)
validated in intact tissue via a 155-gene CARTANA in-situ sequencing platform applied to 13 of the
study's own donors, co-registered with amyloid-beta and phospho-tau immunostaining on the same
sections. The CARTANA data additionally supports two spatial-discovery analyses (distance-based and
tile/plaque-density-based) identifying cell-type-specific gene-expression gradients near pathological
inclusions — a class of finding invisible to dissociated-nuclei approaches. Code is stated as available
at `https://github.com/Gaur-et-al` and snRNA-seq data at EGA accession `EGAD00001009166` (per the
paper's own Data/Code availability statements); per this ARA's `sources.yaml`, no code repository or
dataset was provided as input to this compilation (`code: []`, `data: []`).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | 12 observations (O1-O12) → 4 gaps (G1-G4) → key insight → 6 assumptions (A1-A6) |
| [claims.md](logic/claims.md) | 14 falsifiable claims (C01-C14) with grounded number sources, page-pinned to the PDF |
| [concepts.md](logic/concepts.md) | 13 technical terms (Braak staging, ANCOM-BC, glmmTMB, LOEUF, CARTANA, Cell Type Mapper, distance/tile-based spatial models, GFAP bimodality, THEMIS+/POSTN+ resilience signature, etc.) |
| [experiments.md](logic/experiments.md) | 9 declarative verification/analysis plans (E01-E09), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph: 20 full RW blocks + a grouped list of remaining background citations, covering the paper's full reference footprint |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and the paper's own stated limitations |
| [solution/method.md](logic/solution/method.md) | The 10-stage computational analysis pipeline (nuclei isolation → clustering → trait association → DE → CARTANA generation/validation/discovery) |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, tissue-sampling, cross-cohort integration, and statistical-framework design |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Wet-lab and computational environment: sequencing platform, software versions, data/code availability statements, funding |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: 1 root question, decisions/experiments/dead-ends spanning cohort design, trait association, DE, cross-cohort replication, and CARTANA validation/discovery (20 nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 5 numbered figures (all filed, in order); paper contains no numbered tables |
| [figures/figure1.md](evidence/figures/figure1.md) | Experimental scheme and molecular map of the human TC in 40 individuals (UMAP, marker dot plots) |
| [figures/figure2.md](evidence/figures/figure2.md) | AD trait association analysis of cellular subtypes (ANCOM-BC beta values, box plots, sex association) |
| [figures/figure3.md](evidence/figures/figure3.md) | Differential expression analysis at cell-type level (DEG counts, LOEUF, pathway enrichment, gene-level box plots) |
| [figures/figure4.md](evidence/figures/figure4.md) | Plaque/tangle tissue characterization and CARTANA validation of snRNA-seq associations |
| [figures/figure5.md](evidence/figures/figure5.md) | Gene expression in tissue niches of plaques and tangles (distance-based heatmaps) |
