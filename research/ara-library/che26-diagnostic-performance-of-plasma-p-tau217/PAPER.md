---
title: "Diagnostic performance of plasma p-Tau217, p-Tau181, and p-Tau231 across the Alzheimer's disease continuum: a network meta-analysis"
authors: ["Xiaofeng Chen", "Tingting Huang", "Chao Shi", "Shuizhi Xu", "Shuwei Fan"]
year: 2026
venue: "Frontiers in Aging Neuroscience"
doi: "10.3389/fnagi.2026.1834591"
ara_version: "1.0"
domain: "Alzheimer's disease diagnostics — blood-based biomarkers; Bayesian/frequentist network meta-analysis of diagnostic test accuracy"
keywords: ["Alzheimer's disease continuum", "diagnostic performance", "network meta-analysis", "plasma biomarkers", "plasma phosphorylated tau 181", "plasma phosphorylated tau 217", "plasma phosphorylated tau 231", "mass spectrometry", "automated immunoassay", "p-tau217/Abeta42 ratio"]
claims_summary:
  - "Plasma p-tau217 measured by mass spectrometry (p217_MS) has the highest diagnostic accuracy for amyloid-beta pathology (P-score = 0.859), far outranking standard p-tau181 immunoassay (P-score = 0.117)."
  - "The p-tau217/Abeta42 ratio on automated platforms yields a significant incremental AUC gain of 0.025 (95% CI 0.005-0.045; I2 = 0%) over single-analyte assays."
  - "p217_MS is the top marker for advanced Tau-PET staging (P-score = 0.907) and for predicting MCI-to-AD-dementia conversion (P-score = 0.821)."
  - "p-tau231 achieves the highest rank in the preclinical subgroup for detecting early amyloidosis (P-score = 0.66), supporting a 'relay' hypothesis."
  - "p-tau217 diagnostic performance is consistent across Han Chinese and Western cohorts (P-score = 1.00 across the Asian datasets)."
  - "Mass spectrometry is the gold-standard platform (P-score = 0.953); automated immunoassays (Lumipulse, P-score = 0.706) outperform manual immunoassays (P-score = 0.268); serum is a viable matrix (serum p-tau217 P-score = 0.568)."
  - "Standard p-tau181 immunoassay is effectively obsolete for high-precision AD diagnostics (P-score < 0.20 across all outcomes)."
abstract: "Blood-based biomarkers (BBMs) are transforming the diagnostic workflow for Alzheimer's disease (AD). However, there is no consensus on the optimal phosphorylated tau (p-tau) isoform (217, 181, or 231) or analytical platform [mass spectrometry (MS) vs. immunoassay (IA)] for clinical implementation across different disease stages. Objective: To systematically compare the diagnostic accuracy and prognostic value of plasma p-tau isoforms using different technical platforms for detecting amyloid-beta (Abeta) pathology, tau pathology, and predicting cognitive decline. Study selection: Studies reporting diagnostic accuracy [Area Under the Curve (AUC)] of plasma p-tau against cerebrospinal fluid (CSF) or Positron Emission Tomography (PET) standards were included. To ensure statistical independence, overlapping cohorts (e.g., BioFINDER, ADNI) were rigorously screened, selecting only the most comprehensive dataset per cohort. Results: A total of 18 high-quality studies comprising 24 independent datasets and 4,736 participants were included. For detecting Abeta pathology, p-tau217 measured by MS (p217_MS) demonstrated the highest diagnostic accuracy (P-score = 0.86), followed by p-tau217 ratio (p217_Ratio) (P-score = 0.78) and automated immunoassays (P-score = 0.67-0.69), all of which significantly outperformed standard p-tau181 immunoassays (P-score = 0.12). Notably, the p-tau217/Abeta42 ratio on automated platforms provided a significant incremental AUC gain of 0.025 (95% CI: 0.005 to 0.045; I2 = 0%) compared to single-analyte assays, effectively bridging the performance gap with MS. In disease staging, while p-tau231 showed potential in detecting early amyloidosis, p-tau217_MS was superior for identifying advanced Tau-PET pathology (P-score = 0.91) and predicting MCI-to-dementia conversion (P-score = 0.82). Subgroup analyses confirmed consistent performance of p-tau217 across Han Chinese and Western cohorts, and demonstrated the diagnostic potential of serum-based assays as a viable matrix. Conclusions and relevance: Plasma p-tau217, particularly when measured by mass spectrometry or as a ratio on fully automated platforms, offers the highest accuracy for AD diagnosis and staging. While p-tau231 may serve as an early indicator of amyloidosis, p-tau217 is the most robust marker for tau pathology and disease progression. These findings support the integration of automated p-tau217 assays into routine clinical care to streamline patient stratification for disease-modifying therapies. Systematic review registration: https://www.crd.york.ac.uk/prospero/, identifier (CRD420261327845)."
---

# Diagnostic performance of plasma p-Tau217, p-Tau181, and p-Tau231 across the Alzheimer's disease continuum: a network meta-analysis

## Overview

This is a PRISMA-DTA systematic review and network meta-analysis (NMA) that, for the first time, simultaneously compares plasma phosphorylated-tau isoforms (p-tau217, p-tau181, p-tau231), across analytical platforms (mass spectrometry vs. immunoassays; single-analyte vs. ratio) and sample matrices (plasma vs. serum), for detecting amyloid-beta pathology, Tau-PET pathology, and predicting MCI-to-AD-dementia conversion. It integrates direct and indirect evidence from 18 studies / 24 independent datasets / 4,736 participants, ranking each biomarker-platform node by SUCRA-analogous P-scores across four outcomes. The central finding is a clear hierarchy: p-tau217 (especially by MS or as an automated ratio) is the premier marker for diagnosis and staging, p-tau231 is a specialized early-amyloidosis "smoke detector", and standard p-tau181 immunoassay is effectively obsolete for high-precision diagnostics. The review is prospectively registered on PROSPERO (CRD420261327845). No analysis code or accessioned primary dataset was released; the work reuses extracted summary AUC statistics from established AD cohorts.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (biomarker/platform heterogeneity) → gaps → key insight (simultaneous NMA) |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01-C08) with pooled diagnostic-performance findings |
| [concepts.md](logic/concepts.md) | 13 technical terms (p-tau isoforms, P-score/SUCRA, NMA, AUC, ratio metric, matrices, AT(N)) |
| [experiments.md](logic/experiments.md) | 6 declarative NMA/analysis plans (E01-E06), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's 30 references + PROSPERO registration |
| [solution/study_design.md](logic/solution/study_design.md) | PRISMA-DTA search, inclusion/exclusion, cohort de-overlap, NMA model, ranking |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations, assumptions, boundary conditions |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment: netmeta R package, PROSPERO protocol, cohorts, data access |
| [artifacts.md](src/artifacts.md) | Non-code deliverables: PROSPERO registration, extracted summary-data (no released dataset/code) |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG of the review's decision trajectory |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 2 tables + 3 figures |
| [tables/table1.md](evidence/tables/table1.md) | Characteristics of included studies and cohorts |
| [tables/table2.md](evidence/tables/table2.md) | SUCRA-based P-score rankings across 4 outcomes |
| [figures/figure1.md](evidence/figures/figure1.md) | PRISMA flow diagram of study selection |
| [figures/figure2.md](evidence/figures/figure2.md) | Evidence network plots (Abeta, Tau-PET) |
| [figures/figure3.md](evidence/figures/figure3.md) | Forest plots of AUC mean differences vs. p-tau181 baseline |
