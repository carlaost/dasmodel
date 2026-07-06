---
title: "Multimodal Self-Supervised Learning for Early Alzheimer's: Cross-Modal MRI–PET, Longitudinal Signals, and Site Invariance"
authors: ["Soumaya Belhaj Ali", "Naglaa E. Ghannam", "H. Mancy", "Basma Gh. Elkilany"]
year: 2025
venue: "Diagnostics (MDPI), 15(24), 3135"
doi: "10.3390/diagnostics15243135"
ara_version: "1.0"
grounding: full-text
domain: "Medical imaging / self-supervised deep learning for Alzheimer's disease diagnosis and prognosis"
keywords: ["Alzheimer's disease", "self-supervised learning", "contrastive learning", "MRI", "PET", "longitudinal modeling", "domain adaptation", "site invariance", "prognosis", "survival analysis"]
claims_summary:
  - "On ADNI AD-vs-CN diagnosis the framework reaches 93.0% balanced accuracy and 0.96 AUC, the best among five baselines."
  - "The site-invariant model transfers across cohorts: 78.0% BACC (AUC 0.87) on OASIS-3 and 77.5% BACC (AUC 0.85) on AIBL under ADNI→X transfer."
  - "On the TADPOLE MCI→AD prognosis benchmark it reaches AUC 0.85, C-index 0.82, tdAUC@36m 0.82, and IBS 0.16."
  - "On MIRIAD it attains test–retest ICC 0.91 and atrophy sensitivity 76.5%, the highest reliability among compared methods."
  - "On BioFINDER it predicts ATN biomarker status from MRI: amyloid 83% vs 79% and tau 75% vs 73% BACC over Radiology'23, with comparable neurodegeneration (0.86 AUC)."
  - "The framework reports the lowest expected calibration error among baselines on the tabulated cohorts (e.g. 5.9% on BioFINDER AD-vs-CN)."
  - "It is presented as the first framework to unify cross-modal MRI–PET learning, longitudinal consistency, and explicit site/domain-invariance in one SSL pipeline."
abstract: "Background: The early and accurate identification of Alzheimer's disease (AD) is complicated by a number of factors, such as the diversity of imaging modalities, variability in scanners across multiple sites, and the long-term progression of neurodegeneration. Such modest gains and the range of diagnostic scenarios suggest that robust multimodal applications, which incorporate both structural, molecular, and longitudinal measurements, are required if realistic benefits are to be seen in actual clinical settings. Methods: We introduce a multimodal self-supervised learning (SSL) approach, which learns feature representations of MRI and PET jointly using the cross-modal alignment, longitudinal temporal consistency, and domain-invariant embedding optimization. The approach integrates contrastive learning, scanner harmonization strategies, and missing modality-aware fusion for handling real-world cohort diversity. Six widely used datasets were evaluated, which are made publicly available: ADNI, OASIS-3, AIBL, BioFINDER, TADPOLE, and MIRIAD. Results: The model performed in a state-of-the-art way on all benchmark tasks. On ADNI, it obtained a BACC of 93.0% and an AUC of 0.96 for the binary classification task (AD vs. CN), surpassing recent baselines such as DiaMond'25, SMoCo, and AnatCL with statistically significant performance gain. Strong cross-cohort generalizability was reported (78.0% BACC on OASIS-3 and 77.5% BACC on AIBL). For TADPOLE, for longitudinal prognosis (i.e., MCI → AD conversion), the model yielded an AUC of 0.85 and a C-index of 0.82, which shows better ascendency over previous SSL-based methods. High test–retest consistency was observed on MIRIAD (ICC = 0.91), indicating that instability in volume measurement due to atrophy progression was minimal. Conclusions: The proposed multimodal SSL framework offers effective transferable and domain-robust biomarkers for the early diagnosis of AD and prediction of MCI-to-AD progression. It has strong cross-dataset generalization."
---

# Multimodal Self-Supervised Learning for Early Alzheimer's: Cross-Modal MRI–PET, Longitudinal Signals, and Site Invariance

## Overview

This paper proposes a two-stage multimodal self-supervised learning (SSL) framework for early
Alzheimer's disease (AD) diagnosis, MCI→AD prognosis, and ATN biomarker estimation from
structural MRI and PET. **Stage 1** pretrains two modality-specific 3D encoders (3D ResNet-50 or
3D Swin Transformer) with five families of self-supervised objectives — intra-modal InfoNCE,
cross-modal MRI↔PET InfoNCE, longitudinal consistency (with optional cross-time coupling),
BYOL-style regression, and domain-adversarial site invariance via a gradient-reversal layer —
combined with offline scanner harmonization (histogram matching + ComBat) and in-network
GroupNorm/DSBN. **Stage 2** fine-tunes the encoders under a multi-task objective with a
missing-modality-aware gating late-fusion, a class-weighted cross-entropy diagnosis head, a Cox
survival head, a training-only PET→MRI distillation loss, and post-hoc temperature-scaling
calibration.

The framework is evaluated on six public AD cohorts (ADNI, OASIS-3, AIBL, BioFINDER, TADPOLE,
MIRIAD) with site-stratified 5-fold CV for in-distribution tests and ADNI↔OASIS-3 (plus AIBL /
BioFINDER external) for out-of-distribution transfer; MIRIAD is held out for test–retest
reliability. The paper reports state-of-the-art point-estimate metrics against five recent
baselines (ISBI'23, AnatCL, DiaMond'25, SMoCo, Radiology'23). No code repository or trained
weights were released despite a stated intent to release CV splits, seeds, and preprocessing
versions; ablation and sensitivity analyses are *described* (§3.8) but their numerical results are
**not reported** in the paper. Several internal numerical inconsistencies between the results
tables, the prose, and the calibration figure are documented in the evidence layer.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 7 falsifiable claims (C01–C07) with proof pointers |
| [concepts.md](logic/concepts.md) | 13 technical concepts (SSL objectives, fusion, metrics) |
| [experiments.md](logic/experiments.md) | 7 declarative verification plans (E01–E07) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's citation footprint |
| [solution/method.md](logic/solution/method.md) | Two-stage SSL + multi-task fine-tuning pipeline |
| [solution/algorithm.md](logic/solution/algorithm.md) | Loss formulations (Eq. 1–17) with LaTeX |
| [solution/architecture.md](logic/solution/architecture.md) | Encoders, gating fusion, heads, harmonization |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, limitations, reported inconsistencies |
| [solution/heuristics.md](logic/solution/heuristics.md) | Stated implementation tricks (subject-level splits, gating, distillation) |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Data sources, software/hardware, protocols, seeds | — |
| [configs/pretraining.md](src/configs/pretraining.md) | Stage-1 SSL hyperparameters | C01–C06 |
| [configs/finetuning.md](src/configs/finetuning.md) | Stage-2 fine-tuning + calibration config | C01–C06 |
| [execution/ssl_losses.py](src/execution/ssl_losses.py) | Reconstructed loss stubs from Eq. 1–13 | C01, C05 |
| [data/dataset.md](data/dataset.md) | Six cohorts: size, groups, modalities, access | C01–C06 |
| [data/preprocessing.md](data/preprocessing.md) | MRI/PET preprocessing + harmonization pipeline | C02, C06 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 17-node research DAG (questions, decisions, experiments, dead ends) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 8 tables + 11 figures |
