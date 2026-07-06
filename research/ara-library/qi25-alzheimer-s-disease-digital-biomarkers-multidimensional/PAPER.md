---
title: "Alzheimer's disease digital biomarkers multidimensional landscape and AI model scoping review"
authors: ["Wenhao Qi", "Xiaohong Zhu", "Bin Wang", "Yankai Shi", "Chaoqun Dong", "Shiying Shen", "Jiaqi Li", "Kun Zhang", "Yunfan He", "Mengjiao Zhao", "Shiyan Yao", "Yongze Dong", "Huajuan Shen", "Junling Kang", "Xiaodong Lu", "Guowei Jiang", "Lizzy M M Boots", "Heming Fu", "Lilin Pan", "Hongkai Chen", "Zhenyu Yan", "Guoliang Xing", "Shihua Cao"]
year: 2025
venue: "NPJ Digital Medicine"
doi: "10.1038/s41746-025-01640-z"
ara_version: "1.0"
grounding: abstract-only
domain: "Alzheimer's disease digital biomarkers / AI model scoping review / bibliometrics"
keywords: ["Alzheimer's disease", "digital biomarkers", "artificial intelligence", "scoping review", "bibliometric analysis", "machine learning", "external validation", "model calibration"]
claims_summary:
  - "The review maps 431 digital-biomarker studies from five online databases and scopes 86 AI models."
  - "The field spans 224 grants, 54 disciplines, 1403 institutions, 44 countries, and 2571 researchers."
  - "Motor activity, neurocognitive tests, eye tracking, and speech analysis are reported as key focus areas."
  - "Classical machine learning dominates AI work, but many models lack performance reporting."
  - "Reported average AUC is 0.887 for 21 AD-focused models and 0.821 for 45 MCI models, while external validation and calibration are rare."
abstract: "As digital biomarkers gain traction in Alzheimer's disease (AD) diagnosis, understanding recent advancements is crucial. This review conducts a bibliometric analysis of 431 studies from five online databases: Web of Science, PubMed, Embase, IEEE Xplore, and CINAHL, and provides a scoping review of 86 artificial intelligence (AI) models. Research in this field is supported by 224 grants across 54 disciplines and 1403 institutions in 44 countries, with 2571 contributing researchers. Key focuses include motor activity, neurocognitive tests, eye tracking, and speech analysis. Classical machine learning models dominate AI research, though many lack performance reporting. Of 21 AD-focused models, the average AUC is 0.887, while 45 models for mild cognitive impairment show an average AUC of 0.821. Notably, only 2 studies incorporated external validation, and 3 studies performed model calibration. This review highlights the progress and challenges of integrating digital biomarkers into clinical practice."
---

# Alzheimer's disease digital biomarkers multidimensional landscape and AI model scoping review

> **Grounding: abstract-only.** The provided input consists only of `metadata.json` and `metadata.md`; no full-text PDF, tables, figures, appendices, reference list, methods details, or supplementary files were provided. This ARA captures only what the abstract and metadata genuinely support. Missing details are marked "Not available from provided input."

## Overview

Qi et al. (2025) review the Alzheimer's disease digital-biomarker landscape through a bibliometric analysis of studies from five databases and a scoping review of AI models. The abstract reports field-scale metadata, dominant sensing/task areas, the prevalence of classical machine learning, average AUCs for AD-focused and mild-cognitive-impairment models, and sparse use of external validation and model calibration.

Because no full text is available, this artifact does not enumerate source tables, figures, included-study lists, model taxonomies, search strings, eligibility criteria, or reference-level related work. It preserves the abstract-supported claims and explicitly records those gaps.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations -> gaps -> key insight from abstract-only input |
| [claims.md](logic/claims.md) | 5 claims (C01-C05) with abstract-grounded source quotes |
| [concepts.md](logic/concepts.md) | 8 key technical terms |
| [experiments.md](logic/experiments.md) | 5 directional review/analysis plans (E01-E05) |
| [related_work.md](logic/related_work.md) | Database/source footprint and missing citation-list note |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Review design reconstructable from the abstract |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Source availability and reproducibility environment; no code/configs provided | C01-C05 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 7-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index; no tables or figures extractable from provided input |
