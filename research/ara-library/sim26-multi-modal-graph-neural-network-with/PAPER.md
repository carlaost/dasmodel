---
title: "Multi-Modal Graph Neural Network with Transformer-Guided Adaptive Diffusion for Preclinical Alzheimer Classification"
authors: ["Jaeyoon Sim", "Minjae Lee", "Guorong Wu", "Won Hwa Kim"]
year: 2026
venue: "Not specified in paper"
doi: "10.1007/978-3-031-72086-4_48"
ara_version: "1.0"
grounding: full-text
domain: "Medical imaging / graph neural networks for Alzheimer's disease classification"
keywords: ["graph neural network", "Alzheimer's disease", "adaptive diffusion", "transformer", "multi-modal", "brain connectome", "heat kernel", "self-attention", "interpretability", "ADNI"]
claims_summary:
  - "GTAD achieves the highest accuracy of all 10 compared methods (9 baselines + GTAD) across all four modality combinations for 3-way (CN/SMC/EMCI) preclinical AD classification on ADNI: 0.945±0.02 (Cortical Thickness & β-Amyloid), 0.963±0.01 (Cortical Thickness & FDG), 0.962±0.01 (β-Amyloid & FDG), 0.963±0.01 (All Imaging Features)."
  - "Ablation shows the Adaptive Convolution Layer + multi-modal (MM) attention combination is best (0.963±0.01 accuracy), versus 0.945±0.03 with adaptive convolution alone (no MM attention), 0.947±0.02 for MLP+MM attention, and 0.900±0.01 for non-adaptive Graph Convolution+MM attention."
  - "Multi-modal (per-modality-head) attention improves the adaptive convolution block by +1.8 accuracy points (94.5%→96.3%), a much larger gain than the +0.8pt (93.9%→94.7%) seen with an MLP block or the +0.1pt (89.9%→90.0%) seen with a non-adaptive Graph Convolution block."
  - "Trained node-wise diffusion scales differ by modality even at the same ROI, and the paper interprets small-scale ROIs as needing only local neighborhood information while large-scale ROIs need distant information; the 8 smallest-scale ROIs per modality span subcortical (thalamus, putamen, globus pallidus), temporal and frontal regions."
  - "Lingual gyrus (G.oc.temp.med.Lingual) has the highest attention-based Importance Rate (IR) across all three modalities in common: 23.13% (Cortical Thickness), 28.75% (β-Amyloid), 30.00% (FDG); hippocampus shows a high IR in FDG (6.25%) and putamen shows high IR in Cortical Thickness (15.63%) and β-Amyloid (14.38%)."
abstract: "The graphical representation of the brain offers critical insights into diagnosing and prognosing neurodegenerative disease via relationships between regions of interest (ROIs). Despite recent emergence of various Graph Neural Networks (GNNs) to effectively capture the relational information, there remain inherent limitations in interpreting the brain networks. Specifically, convolutional approaches ineffectively aggregate information from distant neighborhoods, while attention-based methods exhibit deficiencies in capturing node-centric information, particularly in retaining critical characteristics from pivotal nodes. These shortcomings reveal challenges for identifying disease-specific variation from diverse features from different modalities. In this regard, we propose an integrated framework guiding diffusion process at each node by a downstream transformer where both short- and long-range properties of graphs are aggregated via diffusion-kernel and multi-head attention respectively. We demonstrate the superiority of our model by improving performance of pre-clinical Alzheimer's disease (AD) classification with various modalities. Also, our model adeptly identifies key ROIs that are closely associated with the preclinical stages of AD, marking a significant potential for early diagnosis and prevision of the disease."
---

# Multi-Modal Graph Neural Network with Transformer-Guided Adaptive Diffusion for Preclinical Alzheimer Classification

## Overview

This paper proposes **GTAD** (GNN with Transformer-guided Adaptive Diffusion), an end-to-end
graph neural network for 3-way preclinical Alzheimer's disease (AD) classification
(Control/CN, Significant Memory Concern/SMC, Early Mild Cognitive Impairment/EMCI) from
multi-modal brain-network data. GTAD combines two blocks trained jointly: (1) a **modality-wise
adaptive convolution block** that applies a heat-kernel graph diffusion with a *per-node,
per-modality trainable scale* `s^m` to capture short-range (local) structure, and (2) a
**modality-wise self-attention block** (a transformer where each attention head is assigned to
one imaging modality) that captures long-range (global) structure across ROIs. The scales are
updated end-to-end by backpropagating the classification cross-entropy loss (with an ℓ1
positivity-regularization term) through the whole pipeline, so the local receptive field per ROI
per modality is learned rather than fixed.

The method is evaluated on N=919 subjects from the Alzheimer's Disease Neuroimaging Initiative
(ADNI), using a 160-ROI (148 cortical + 12 sub-cortical) Destrieux-atlas parcellation, DTI-derived
structural brain networks as the graph, and three regional imaging features as modalities
(cortical thickness from MRI, FDG-PET SUVR, and β-Amyloid PET). Under 5-fold cross-validation and
four modality combinations, GTAD is compared against nine baselines spanning three families
(convolution-based GCN/GAT, diffusion-based GraphHeat/GDC/ADC/LSAP, and graph-transformer
NodeFormer/DIFFormer/SGFormer) and reports the best accuracy, precision and recall in every
combination. An ablation isolates the contribution of the adaptive convolution block and the
multi-modal attention block, and the trained scales/attention weights are used post hoc to
identify AD-associated ROIs (e.g., lingual gyrus, hippocampus, putamen). No code repository,
released weights, or hyperparameter appendix accompanies the 10-page paper; the text repeatedly
refers to "more details … in the supplementary," which was not provided with this input.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) with proof pointers |
| [concepts.md](logic/concepts.md) | 12 technical concepts (heat kernel, adaptive scale, modality-wise attention, etc.) |
| [experiments.md](logic/experiments.md) | 3 declarative verification/analysis plans (E01–E03) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's 27-item citation footprint |
| [solution/architecture.md](logic/solution/architecture.md) | GTAD block diagram, tensor shapes, data flow (Fig. 1) |
| [solution/algorithm.md](logic/solution/algorithm.md) | Formal derivation: heat kernel → adaptive convolution → attention → loss (Eq. 1–7) |
| [solution/heuristics.md](logic/solution/heuristics.md) | Stated implementation tricks (ℓ1 scale-positivity term, per-modality attention heads, scale interpretation rule) |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, limitations, and unreported details |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Dataset, atlas, modalities, evaluation protocol, software/hardware (unspecified) | C01–C05 |
| [data/dataset.md](data/dataset.md) | ADNI cohort: 919 subjects, 3 diagnostic groups, 160-ROI parcellation, 3 modalities | C01–C05 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 15-node research DAG (root questions, design decisions, ablation dead ends, experiments) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 2 tables + 3 figures, all filed |
| [tables/table1.md](evidence/tables/table1.md) + `.png` | Main classification results, 9 baselines vs. GTAD × 4 modality combos |
| [tables/table2.md](evidence/tables/table2.md) + `.png` | Ablation: convolution-block type × multi-modal attention on/off |
| [figures/figure1.md](evidence/figures/figure1.md) + `.png` | GTAD architecture diagram |
| [figures/figure2.md](evidence/figures/figure2.md) + `.png` | Learned per-modality node scales (brain maps) + 8 smallest-scale ROIs per modality |
| [figures/figure3.md](evidence/figures/figure3.md) + `.png` | Attention-score distributions per ROI + top-5 importance-rate ROIs per modality |
