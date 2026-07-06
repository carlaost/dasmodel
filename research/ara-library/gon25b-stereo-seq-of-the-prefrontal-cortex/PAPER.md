---
title: "Stereo-seq of the prefrontal cortex in aging and Alzheimer's disease"
authors: [Yun Gong, Mohammad Haeri, Xiao Zhang, Yisu Li, A. Liu, Di Wu, Qilei Zhang, S. M. Jazwinski, Xiang Zhou, Xiaoying Wang, Kai Zhang, Lindong Jiang, Yi-Ping Chen, Xiaoxin Yan, R. Swerdlow, Hui Shen, Hong-wen Deng]
year: 2025
venue: "Nature Communications"
doi: "10.1038/s41467-024-54715-y"
ara_version: "1.0"
grounding: abstract-only
domain: "Neurogenomics - spatial transcriptomics of Alzheimer's disease"
keywords: [Alzheimer's disease, aging, prefrontal cortex, Stereo-seq, spatial transcriptomics, laminar structure, cell-cell interactions, amyloid-beta, ZNF460]
claims_summary:
  - "The study presents a subcellular-resolution Stereo-seq spatial transcriptome atlas of human prefrontal cortex from male AD cases and age-matched male controls."
  - "The abstract reports AD-associated transcriptional alterations across PFC layers, disrupted laminar structure, and altered layer-to-layer and cell-cell interactions."
  - "The abstract reports upregulated genes in stressed neurons and nearby glial cells, alongside diminished stress-response interactions that promote amyloid-beta clearance in AD."
  - "The abstract reports three cell-type-specific neuronal co-expression modules linked to neuroprotection, protein dephosphorylation, and amyloid-beta regulation, all downregulated as AD progresses, and identifies ZNF460 as a regulator."
abstract: "Aging increases the risk for Alzheimer’s disease (AD), driving pathological changes like amyloid-β (Aβ) buildup, inflammation, and oxidative stress, especially in the prefrontal cortex (PFC). We present the first subcellular-resolution spatial transcriptome atlas of the human prefrontal cortex (PFC), generated with Stereo-seq from six male AD cases at varying neuropathological stages and six age-matched male controls. Our analyses revealed distinct transcriptional alterations across PFC layers, highlighted disruptions in laminar structure, and exposed AD-related shifts in layer-to-layer and cell-cell interactions. Notably, we identified genes highly upregulated in stressed neurons and nearby glial cells, where AD diminished stress-response interactions that promote Aβ clearance. Further, cell-type-specific co-expression analysis highlighted three neuronal modules linked to neuroprotection, protein dephosphorylation, and Aβ regulation, with all modules downregulated as AD progresses. We identified ZNF460 as a transcription factor regulating these modules, offering a potential therapeutic target. In summary, this spatial transcriptome atlas provides valuable insight into AD’s molecular mechanisms. Aging increases the risk for Alzheimer’s disease (AD). Here, the authors present a spatial transcriptome atlas of the human prefrontal cortex in AD, revealing distinct transcriptional alterations."
---

# Stereo-seq of the prefrontal cortex in aging and Alzheimer's disease

> **Grounding note: abstract-only.** The provided inputs contain metadata and abstract text only. No full-text PDF, figures, tables, methods section, supplement, code, or data files were provided. This ARA is therefore source-bounded to `metadata.json` and `metadata.md`. Required fields unsupported by those inputs are marked "Not available from provided input".

## Overview

This paper reports a Stereo-seq spatial transcriptome atlas of the human prefrontal cortex in aging and Alzheimer's disease. The abstract states that the atlas was generated from six male AD cases at varying neuropathological stages and six age-matched male controls, and that analyses found AD-associated transcriptional, laminar, interaction, stress-response, and neuronal co-expression changes.

The abstract identifies ZNF460 as a transcription factor regulating three downregulated neuronal modules linked to neuroprotection, protein dephosphorylation, and amyloid-beta regulation. Because only abstract and metadata are available, this ARA captures the study's claims and analysis structure without fabricating numerical results, figures, tables, protocols, or software.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions supported by the abstract |
| [claims.md](logic/claims.md) | 4 falsifiable claims (C01-C04) |
| [concepts.md](logic/concepts.md) | 9 abstract-grounded technical concepts |
| [experiments.md](logic/experiments.md) | 4 directional analysis plans reconstructed from the abstract |
| [related_work.md](logic/related_work.md) | Typed dependency graph limited to concepts and prior domains named in the abstract |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and limitations of the abstract-only artifact |
| [solution/study_design.md](logic/solution/study_design.md) | Abstract-grounded study design and analysis components |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Input availability, reproducibility boundaries, and absent artifacts | - |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 6-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence ledger; no numbered figures or tables were available in provided input |
