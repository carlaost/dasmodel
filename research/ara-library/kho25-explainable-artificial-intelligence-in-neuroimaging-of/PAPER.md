---
title: "Explainable Artificial Intelligence in Neuroimaging of Alzheimer's Disease"
authors: [Mahdieh Taiyeb Khosroshahi, Soroush Morsali, Sohrab Gharakhanlou, Alireza Motamedi, Saeid Hassanbaghlou, Hadi Vahedi, Siamak Pedrammehr, H. M. D. Kabir, Ali Jafarizadeh]
year: 2025
venue: "Diagnostics"
doi: "10.3390/diagnostics15050612"
ara_version: "1.0"
grounding: abstract-only
domain: "Medical AI — explainable artificial intelligence for Alzheimer's disease neuroimaging"
keywords: [Alzheimer's disease, explainable AI, neuroimaging, MRI, PET, SHAP, LIME, Grad-CAM, Layer-wise Relevance Propagation, clinical interpretability]
claims_summary:
  - "XAI addresses the interpretability barrier limiting clinical applicability of complex AI models in AD neuroimaging diagnosis."
  - "The review covers SHAP, LIME, Grad-CAM, and Layer-wise Relevance Propagation as key XAI techniques for AD neuroimaging."
  - "XAI applications in AD neuroimaging include biomarker identification, disease-progression tracking, and AD-stage distinction across MRI and PET."
  - "Dataset limitations, regulatory concerns, and standardization issues remain current challenges for clinical integration."
  - "XAI has the potential to refine AD diagnostics, personalize treatment strategies, and advance neuroimaging-based research."
abstract: "Alzheimer's disease (AD) remains a significant global health challenge, affecting millions worldwide and imposing substantial burdens on healthcare systems. Advances in artificial intelligence (AI), particularly in deep learning and machine learning, have revolutionized neuroimaging-based AD diagnosis. However, the complexity and lack of interpretability of these models limit their clinical applicability. Explainable Artificial Intelligence (XAI) addresses this challenge by providing insights into model decision-making, enhancing transparency, and fostering trust in AI-driven diagnostics. This review explores the role of XAI in AD neuroimaging, highlighting key techniques such as SHAP, LIME, Grad-CAM, and Layer-wise Relevance Propagation (LRP). We examine their applications in identifying critical biomarkers, tracking disease progression, and distinguishing AD stages using various imaging modalities, including MRI and PET. Additionally, we discuss current challenges, including dataset limitations, regulatory concerns, and standardization issues, and propose future research directions to improve XAI's integration into clinical practice. By bridging the gap between AI and clinical interpretability, XAI holds the potential to refine AD diagnostics, personalize treatment strategies, and advance neuroimaging-based research."
---

# Explainable Artificial Intelligence in Neuroimaging of Alzheimer's Disease

> **Grounding note: abstract-only.** The full-text PDF, figures, tables, reference list, and article sections were not available in the provided input. This ARA is reconstructed only from `metadata.json` and `metadata.md`. Fields not supported by those files are marked "Not available from provided input". No numbered tables or figures were available to extract, so the evidence layer contains only an empty ledger.

## Overview

This Diagnostics review addresses the role of explainable artificial intelligence in Alzheimer's disease neuroimaging. The abstract frames complex machine-learning and deep-learning models as promising for neuroimaging-based AD diagnosis but limited in clinical applicability by poor interpretability. It positions XAI as a way to expose model decision-making, increase transparency, and support trust in AI-assisted diagnostics.

The abstract names SHAP, LIME, Grad-CAM, and Layer-wise Relevance Propagation as key techniques, and states that the review examines their use for biomarker identification, disease-progression tracking, and distinguishing AD stages across MRI and PET. It also identifies dataset limitations, regulatory concerns, and standardization issues as current barriers, with future directions aimed at clinical integration. No empirical result values, study-counts, figures, tables, or detailed protocol are available from the supplied input.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions from the abstract |
| [claims.md](logic/claims.md) | 5 abstract-grounded falsifiable claims (C01-C05) |
| [concepts.md](logic/concepts.md) | 10 key technical terms named or directly implied by the abstract |
| [experiments.md](logic/experiments.md) | 3 declarative review/assessment plans reconstructed from the abstract |
| [related_work.md](logic/related_work.md) | Typed dependency graph limited to named technique families and domains |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and limitations |
| [solution/review_scope.md](logic/solution/review_scope.md) | Review scope and mapped application areas |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Source availability and reproducibility notes; no runnable artifact supplied | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 5-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Empty ledger: no numbered tables or figures in provided input |
