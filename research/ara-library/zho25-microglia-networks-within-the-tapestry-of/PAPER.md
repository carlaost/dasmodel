---
title: "Microglia networks within the tapestry of alzheimer's disease through spatial transcriptomics"
authors: [Yi Zhou, Christopher K. Glass]
year: 2025
venue: "Molecular Neurodegeneration"
doi: "10.1186/s13024-025-00897-y"
ara_version: "1.0"
grounding: full-text
domain: "Neuroscience — Alzheimer's disease, spatial transcriptomics, microglia biology (narrative review)"
keywords: [spatial transcriptomics, Alzheimer's disease, aging, microglia, amyloid plaque niche, MERFISH, Visium, Stereo-seq, disease-associated microglia, interferon signaling]
claims_summary:
  - "img-ST and seq-ST platforms trade off resolution, throughput, and gene-panel flexibility (Visium ~50 μm to Stereo-seq ~220 nm)."
  - "Microglia constitute ~4-10% of CNS cells with a brain-wide regional density gradient."
  - "DAM, ARM, and MGnD are convergent, overlapping microglial activation states discovered independently across neurodegeneration models."
  - "Plaque-induced genes (57 PIGs) define a multicellular co-expression network around amyloid plaques, primarily microglia-driven."
  - "Microglia are the most plaque-proximal cell type (10-20 μm), with astrocytes/oligodendrocytes/OPCs enriched at greater distances (10-40 μm)."
  - "Disease-associated astrocytes (~14% of the astrocyte population) peak at an intermediate 10-40 μm distance from plaques."
  - "Microglia-astrocyte receptor-ligand crosstalk (130 candidate pairs, 11 overlapping with PIGs) strengthens with proximity to plaques."
  - "Type I interferon signaling is a bidirectional, cell-type-specific node linking microglia and neurons in synaptic loss and plaque accumulation."
  - "p-tau-proximal neuronal identity shifts from cortical to hippocampal excitatory neurons between 8 and 13 months in the TauPS2APP model."
  - "A curated MERFISH gene panel-derived 'activation score' links microglial/astrocytic aging to adjacent oligodendrocyte inflammation."
  - "A 300-gene 'Spatial Ageing Clock' shows microglia accelerate neighbor aging while neural stem cells exert a rejuvenating proximity effect."
  - "Foamy microglia in demyelination lesions co-express DAM and lipid-metabolism genes, localizing near interferon-responsive microglia."
  - "Spatial proteomics (30-60 protein targets) corroborates ST-derived microglial subsets, but microglial mRNA and protein levels can dissociate."
abstract: "Understanding Alzheimer's disease (AD) at the cellular level requires insights into how diverse cell types respond to hallmark pathologies, including amyloid plaques and tau aggregates. Although single-cell transcriptomic approaches have illuminated the trajectories of AD progression in both animal models and human brains, they often lack the spatial context necessary to fully comprehend cell–cell interactions and microenvironmental influences. In this review, we discuss recent advances in spatial transcriptomics—integrating both imaging- and sequencing-based methods—that map gene expression within intact brain tissues. We highlight how these technologies have revealed regional heterogeneity and functional diversity among microglia, and their dynamic interactions with astrocytes, neurons, and oligodendrocytes in both aging and AD. Emphasis is placed on the interactions of microglia within the amyloid plaque niche, their contribution to synaptic degeneration, and how aging accelerates microglial and glial activation. By synthesizing findings from AD mouse models and physiologically characterized human tissues, we provide a comprehensive view of the cellular interplay driving AD pathogenesis and offer insights into potential therapeutic avenues."
---

# Microglia networks within the tapestry of Alzheimer's disease through spatial transcriptomics

## Overview

This is a 14-page narrative review (Zhou & Glass, *Molecular Neurodegeneration*, 2025, 20:102)
synthesizing recent advances in spatial transcriptomics (ST) applied to microglia biology in
Alzheimer's disease (AD) and brain aging. The review is organized around a central unresolved
question — how microglia and their spatial neighborhood interact with AD pathological hallmarks —
and answers it by synthesizing findings from mouse-model and human-tissue ST studies across four
themes: (1) ST platform technology (imaging-based vs. sequencing-based, with their resolution/
coverage trade-offs); (2) baseline microglial regional and functional heterogeneity; (3) the
amyloid plaque niche as a spatially graded, multicellular signaling network (plaque-induced genes,
distance-binned cell-type enrichment, microglia-astrocyte receptor-ligand crosstalk, interferon
signaling, and tau-proximal neuronal vulnerability); and (4) microglia and their neighbors in the
aging (non-AD) brain (activation scores, spatial aging clocks, foamy microglia in demyelination).
It closes with a shorter section on human-sample AD findings and a discussion of complementary
future modalities (spatial proteomics, spatial epigenomics, 3D imaging) needed to address current
ST limitations — including an explicit caveat about microglial mRNA-protein dissociation. The
authors report no new primary data ("No datasets were generated or analysed during the current
study"); this ARA captures the review's synthesized, source-grounded findings rather than original
experiments by Zhou & Glass.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions grounding the review's central spatial-microglia question |
| [claims.md](logic/claims.md) | 14 falsifiable, fully-grounded claims (C01-C14) synthesizing the review's key findings |
| [concepts.md](logic/concepts.md) | 24 technical concepts (ST platforms, microglial states, aging/proximity concepts) formally defined |
| [experiments.md](logic/experiments.md) | 12 directional analysis-approach plans (E01-E12) reconstructed from the primary literature the review synthesizes |
| [related_work.md](logic/related_work.md) | Typed dependency graph: 14 full RW blocks for load-bearing sources plus grouped summary tables for the review's ~162-reference footprint |
| [solution/constraints.md](logic/solution/constraints.md) | Technological, scope, and cross-study comparability limitations stated in the review |
| [solution/study_design.md](logic/solution/study_design.md) | The review's narrative structure, section-by-section, with a figure-to-section map |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Data/code availability (none — review with no new datasets), reproducibility notes, funding/competing-interests disclosures | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 19-node source-bounded research DAG covering all four review themes plus the human-samples and future-directions questions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence ledger: 3 figures filed, 0 tables in source (verified by full-text sweep) |
| [figures/figure1.md](evidence/figures/figure1.md) / [.png](evidence/figures/figure1.png) | Fig. 1 — MERFISH/seqFISH/padlock-ISS encoding-decoding schematic (diagram) |
| [figures/figure2.md](evidence/figures/figure2.md) / [.png](evidence/figures/figure2.png) | Fig. 2 — img-ST/seq-ST platform resolution comparison on shared human AD tissue (mixed: qualitative sample + diagram) |
| [figures/figure3.md](evidence/figures/figure3.md) / [.png](evidence/figures/figure3.png) | Fig. 3 — integrated cell-cell communication schematic for the AD plaque niche (A) and the aging myelin niche (B) (diagram) |
