---
title: "Alzheimer's Association Clinical Practice Guideline on the use of blood-based biomarkers in the diagnostic workup of suspected Alzheimer's disease within specialized care settings"
authors: [Sebastian Palmqvist, Heather E. Whitson, Laura A. Allen, Marc Suarez-Calvet, Douglas Galasko, Thomas K. Karikari, Hamid R. Okrahvi, Madeline Paczynski, Suzanne E. Schindler, Charlotte E. Teunissen, Henrik Zetterberg, Maria C. Carrillo, Rebecca M. Edelmayer, Simin Mahinrad, Mary Beth McAteer, Lara A. Kahale, Sarah Pahlke, Malavika P. Tampi]
year: 2025
venue: "Alzheimer's & Dementia (Journal of the Alzheimer's Association)"
doi: "10.1002/alz.70535"
ara_version: "1.0"
domain: "Clinical practice guideline — diagnostic test accuracy of blood-based biomarkers for Alzheimer's disease (GRADE methodology)"
keywords: [Alzheimer's disease, blood-based biomarkers, clinical practice guideline, diagnostic test accuracy, GRADE, p-tau217, amyloid, sensitivity, specificity, evidence-to-decision]
claims_summary:
  - "A BBM test with >=90% sensitivity and >=75% specificity can be used as a triaging test in specialized memory care (conditional recommendation, low certainty)."
  - "A BBM test with >=90% sensitivity and >=90% specificity can substitute for amyloid PET or CSF as a confirmatory test (conditional recommendation, low certainty)."
  - "Diagnostic test accuracy across the 31 evaluated tests is highly variable; many commercial tests do not meet the thresholds with a single cutoff."
  - "Some tests meet or exceed the panel's thresholds at a single cut-point."
  - "Certainty of evidence for tests meeting thresholds is low to very low, mostly rated down for risk of bias."
  - "Predictive values of a threshold-meeting test depend strongly on pretest probability of AD pathology."
  - "A BBM test should not be obtained before a comprehensive clinical evaluation (good practice statement)."
abstract: "A panel of clinicians, subject-matter experts, and guideline methodologists convened by the Alzheimer's Association conducted a systematic review and formulated evidence-based recommendations for using blood-based biomarkers (BBMs) in the diagnostic workup of suspected Alzheimer's disease (AD) within specialized care settings. The scope focuses on individuals with objective cognitive impairment, including those with mild cognitive impairment (MCI) or dementia, who are undergoing evaluation by providers trained and experienced in memory disorders, where AD is the suspected underlying etiology."
---

# Alzheimer's Association Clinical Practice Guideline: Blood-Based Biomarkers for Suspected Alzheimer's Disease in Specialized Care

## Overview

This Clinical Practice Guideline (CPG), developed with the GRADE approach and its Evidence-to-Decision (EtD) framework, gives performance-based, **brand-agnostic** recommendations for using plasma blood-based biomarkers (BBMs) — p-tau217, %p-tau217, p-tau181, p-tau231, and Aβ42/40 — in the diagnostic workup of adults with objective cognitive impairment (MCI or dementia) presenting to specialized memory-care settings, where AD is the suspected etiology. It answers two clinical questions (triaging test; confirmatory substitute for CSF/amyloid PET) with two conditional recommendations plus one good practice statement, defining minimum acceptable diagnostic test accuracy thresholds (triaging: ≥90% sensitivity, ≥75% specificity; confirmatory: ≥90% sensitivity and specificity). The evidence base is a companion systematic review of 49 observational diagnostic-test-accuracy studies covering 31 assay/analyte combinations; certainty is low to very low. It is a guideline document, not a primary empirical study: it has no released code, dataset, or registered clinical trial (per sources.yaml).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (diagnostic gaps, BBM emergence) → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) with grounded number sources |
| [concepts.md](logic/concepts.md) | 10 technical terms (BBM test, triaging/confirmatory test, Youden index, GRADE, EtD, certainty, Sn/Sp, PPV/NPV, pretest probability, two-cutoff) |
| [experiments.md](logic/experiments.md) | 6 declarative verification plans (E01–E06) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's citation footprint (RW blocks + brief entries) |
| [solution/constraints.md](logic/solution/constraints.md) | Scope boundaries, assumptions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Guideline development methodology: GRADE, systematic review, EtD process |
| [solution/recommendations.md](logic/solution/recommendations.md) | The two recommendations, thresholds, good practice statement, EtD judgments |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical/methodological environment; data sources (49 studies, databases, MAGICapp, companion review, WebPlotDigitizer); no code/dataset/trial released |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: 2 clinical questions, design decisions, and dead ends (16 nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 3 numbered tables (0 numbered figures); notes on supplementary tables S1–S3 |
| [tables/table1.md](evidence/tables/table1.md) | Definitions: certainty of evidence + strong vs conditional recommendations |
| [tables/table2.md](evidence/tables/table2.md) | The recommendations, remarks, and good practice statement |
| [tables/table3.md](evidence/tables/table3.md) | 31 assay/analyte/brand combinations studied |
