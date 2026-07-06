---
title: "Vision and convolutional transformers for Alzheimer's disease diagnosis: a systematic review of architectures, multimodal fusion and critical gaps"
authors: ["Ibrahem Afifi", "Mostafa Elgendy", "Mohamed Abdelfatah", "Shaker El-Sappagh"]
year: 2026
venue: "Brain Informatics (SpringerOpen) 13:1"
doi: "10.1186/s40708-025-00286-7"
ara_version: "1.0"
domain: "Medical AI / neuroimaging — systematic review of Vision Transformers and Convolutional Vision Transformers for Alzheimer's disease diagnosis"
grounding: full-text
keywords: ["Alzheimer's disease", "Vision Transformer (ViT)", "Convolutional Vision Transformer (CViT)", "systematic review", "PRISMA", "multimodal fusion", "MCI-to-AD progression", "reproducibility", "Explainable AI", "Large Vision Models"]
claims_summary:
  - "Hybrid CViT architectures (46/68 studies) have overtaken pure ViTs (22/68) as the dominant transformer paradigm for AD diagnosis."
  - "sMRI is the predominant input modality across the reviewed literature (single-modality: sMRI 31, fMRI 7, PET 3)."
  - "The field is over-reliant on ADNI (~72–73% of studies), raising dataset-bias and generalizability concerns."
  - "MCI-to-AD progression prediction is markedly underexplored relative to AD-stage classification."
  - "A reproducibility crisis exists: only 10 of 68 studies (~15%) share publicly accessible code."
  - "PyTorch is the most-used framework (35 studies) vs TensorFlow (13)."
  - "Multimodal fusion is far more common in CViT (26/46, ~57%) than ViT (2/22, ~9%) studies."
  - "Reported near-perfect accuracies (>99%) largely reflect methodological bias risk and the 'accuracy paradox', not clinical readiness."
abstract: "Alzheimer's disease (AD), a significant public health challenge, requires accurate early diagnosis to improve patient outcomes. Vision Transformers (ViTs) and Convolutional Vision Transformers (CViTs) have emerged as powerful Deep Learning architectures for this task. Following PRISMA guidelines, this systematic review analyzes 68 studies selected from 564 publications (2021–2025) across five major databases: Scopus, Web of Science, ScienceDirect, IEEE Xplore, and PubMed. We introduce novel taxonomies to systematically categorize these works by model architecture, data modality, fusion strategy, and diagnostic objective. Our analysis reveals key trends, such as the rise of hybrid CViT frameworks, and critical gaps, including a limited focus on Mild Cognitive Impairment-to-AD progression. Critically, we also assess practical implementation details, revealing widespread challenges in algorithmic reproducibility. The discussion culminates in a forward-looking analysis of Large Vision Models and proposes future directions emphasizing the need for robust multimodal integration, lightweight transformer designs, and Explainable AI to advance AD research and bridge the critical gap between high-performance modeling and clinical applicability."
---

# Vision and Convolutional Transformers for Alzheimer's Disease Diagnosis: A Systematic Review

## Overview

This is a PRISMA-2020 systematic review (not a primary empirical study) synthesizing 68 peer-reviewed
journal studies (2021–2025) that apply Vision Transformers (ViTs) and hybrid Convolutional Vision
Transformers (CViTs) to Alzheimer's disease (AD) classification and MCI-to-AD conversion prediction.
The review's contributions are conceptual: four novel taxonomies (model architecture, data modality,
fusion strategy, diagnostic objective), a critical synthesis of trends and gaps (rise of CViTs,
under-exploration of prognosis, over-reliance on ADNI, a pervasive reproducibility gap, and an
"accuracy paradox" of inflated benchmark metrics), a dataset-bias analysis, an assessment of how
Large-Vision-Model (LVM) principles are used, a proposed conceptual LVM architecture for future AD
research, and a limitations→future-directions roadmap.

The review team **released no code and no dataset** ("No datasets were generated or analysed during
the current study"); the tables and figures below are the review's own synthesized evidence over the
68 reviewed works. This ARA therefore has a rich cognitive/evidence layer and a minimal `src/`
(analytical work, no runnable artifact).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (epidemiology, prior-review gaps) → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 11 falsifiable claims (C01–C11) with grounded number sources |
| [concepts.md](logic/concepts.md) | 14 technical concepts (ViT, CViT, fusion levels, integration patterns, PRISMA, accuracy paradox, …) |
| [experiments.md](logic/experiments.md) | 9 analysis/verification plans (E01–E09), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph: 8 prior reviews + foundational method citations |
| [solution/constraints.md](logic/solution/constraints.md) | Review scope, assumptions, and stated limitations |
| [solution/study_design.md](logic/solution/study_design.md) | PRISMA search strategy, eligibility, data extraction |
| [solution/taxonomies.md](logic/solution/taxonomies.md) | The four novel taxonomies (architecture / fusion / modality / objective) |
| [solution/proposed_lvm.md](logic/solution/proposed_lvm.md) | Conceptual future LVM architecture (Fig. 43) |
| [solution/future_directions.md](logic/solution/future_directions.md) | Limitations → four future-research pathways (Fig. 44) |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Analytical review; no code/data released; data sources used by reviewed works (ADNI, OASIS, AIBL, …) | C03 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 20-node research DAG reconstructing the review's logic |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 8 tables + 44 figures (each with .md + .png) |
