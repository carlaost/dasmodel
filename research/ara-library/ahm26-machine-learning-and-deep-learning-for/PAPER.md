---
title: "Machine Learning and Deep Learning for Alzheimer's Disease Diagnosis: A Survey of MRI, PET, Multimodal Fusion, Transformers, Graph Neural Networks, and Explainable AI"
authors: [Imran Ahmad, Tasfia Tarannum, Mohammed Majbah Uddin]
year: 2026
venue: "American Journal of Advanced Technology and Engineering Solutions (AJATES), Vol. 6, Issue 1, pp. 622-649"
doi: "10.63125/vf6dkg22"
ara_version: "1.0"
grounding: full-text
domain: "Medical AI / neuroimaging — narrative survey of machine learning and deep learning for Alzheimer's disease diagnosis"
keywords: [Alzheimer's disease, machine learning, deep learning, MRI, PET, multimodal fusion, transformers, graph neural networks, explainable AI, neuroimaging]
claims_summary:
  - "Multimodal systems (esp. MRI + PET) often outperform single-modality systems because they integrate complementary structural and metabolic information."
  - "The field has transitioned from handcrafted-feature machine-learning pipelines to end-to-end deep representation learning."
  - "Transformers and graph neural networks are promising but not yet consistently superior to strong multimodal CNN baselines."
  - "Reported accuracy alone is not a reliable indicator of clinical value or cross-study comparability due to task/dataset heterogeneity."
  - "Explainability is widely claimed but methodologically underdeveloped — rarely validated for stability, plausibility, or reproducibility."
  - "Benchmark dependence (especially ADNI) and limited external validation leave a gap between computational performance and clinical deployment."
  - "This narrative survey synthesizes 8 representative primary studies (2018-2024) organized into five methodological groups."
abstract: "Alzheimer's disease is the leading cause of dementia and remains a major challenge in neurological diagnosis because early symptoms often overlap with normal aging and other neurodegenerative disorders. In recent years, machine learning and deep learning methods have been widely applied to neuroimaging and multimodal clinical data to improve automated diagnosis, risk prediction, and disease-stage classification. This survey reviews representative studies on Alzheimer's disease diagnosis using traditional machine learning, convolutional neural networks, multimodal fusion methods, transformer-based architectures, graph neural networks, and explainable artificial intelligence. The literature shows a clear transition from handcrafted-feature pipelines to end-to-end deep models trained on magnetic resonance imaging, positron emission tomography, and multimodal data. It also suggests that multimodal systems often outperform single-modality systems because they integrate complementary structural and metabolic information, while graph and transformer methods aim to capture more global and relational disease patterns. At the same time, the field still faces major challenges, including dataset dependence, limited external validation, inconsistent evaluation settings, class imbalance, insufficient interpretability assessment, and weak evidence for clinical deployment. This survey organizes the literature by modeling paradigm and data modality, compares representative methods, and outlines future directions for robust, explainable, and clinically useful Alzheimer's disease diagnosis systems."
---

# Machine Learning and Deep Learning for Alzheimer's Disease Diagnosis: A Survey

## Overview

This is a **narrative literature survey** (explicitly *not* a formal systematic review; no PROSPERO
registration) of machine-learning and deep-learning methods for Alzheimer's disease (AD) diagnosis,
with emphasis on neuroimaging (structural MRI, PET) and multimodal data. It organizes the literature
into five methodological groups — traditional machine learning, convolutional deep learning,
multimodal fusion, transformer/hybrid-attention models, and graph neural networks with explainability
components — and synthesizes eight representative primary studies (2018-2024) plus supporting review
literature. Its contributions are conceptual and organizational: a taxonomy of methods, a comparative
framework of model families, and a critical discussion of why multimodal learning matters, why
accuracy alone is insufficient, and why reproducibility, generalizability, and rigorous explainability
remain the field's central unresolved challenges. The paper releases **no new code, data, or model**;
the datasets it discusses (ADNI, OASIS/OASIS-3, AIBL) are public cohorts belonging to the surveyed
literature, not artifacts of this paper.

**Grounding note:** Compiled from the full-text open-access PDF (28 pages, AJATES pp. 622-649). All
figures were read visually and cropped to PNG. Because this is a qualitative survey, it reports
essentially **no numerical results of its own** (Table 1 and all figures are qualitative/schematic);
the only load-bearing numbers are the survey's own scope figures (≈10-15 studies considered, 8 named,
five method groups). No performance metrics are reproduced because the paper deliberately avoids
leaderboard-style numerical comparison.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight for computational AD diagnosis |
| [claims.md](logic/claims.md) | 7 falsifiable synthesis claims (C01–C07) |
| [concepts.md](logic/concepts.md) | 9 genuine technical concepts |
| [experiments.md](logic/experiments.md) | 5 synthesis/analysis plans (E01–E05) — directional, no numbers |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the 8 surveyed studies + supporting citations |
| [solution/constraints.md](logic/solution/constraints.md) | Survey scope, assumptions, limitations |
| [solution/taxonomy.md](logic/solution/taxonomy.md) | Taxonomy of six method families + comparative framework |
| [solution/survey_methodology.md](logic/solution/survey_methodology.md) | Narrative-survey design, scope, study selection |
| [solution/challenges_and_directions.md](logic/solution/challenges_and_directions.md) | Open challenges and future directions |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Analytical/narrative survey — no code/data released; benchmark cohorts (ADNI, OASIS-3, AIBL) as discussed data sources | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 13-node research DAG reconstructing the survey's organizing logic |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 1 table + 10 figures (8 numbered + 2 unnumbered illustrative) |
