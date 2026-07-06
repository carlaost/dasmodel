---
title: "Global incidence trends and projections of Alzheimer disease and other dementias: an age-period-cohort analysis 2021"
authors: [Libo Xu, Zhenhao Wang, Mao Li, Qingsong Li]
year: 2025
venue: "Journal of Global Health"
doi: "10.7189/jogh.15.04156"
ara_version: "1.0"
grounding: abstract-only
domain: "Global health epidemiology — Alzheimer disease and other dementias incidence forecasting"
keywords: [Alzheimer disease, dementia, incidence, GBD 2021, age-period-cohort, Bayesian APC, ASIR, sociodemographic index, global health]
claims_summary:
  - "Global Alzheimer disease and other dementia cases rose from 4.078 million to 9.837 million during 1992-2021 while global ASIR changed only slightly from 117.7 to 119.8 per 100,000."
  - "ASIR increased significantly in high-middle and middle-SDI regions but declined in low-SDI regions."
  - "Women had consistently higher incidence rates than men across all regions."
  - "The BAPC projection reports 2036 global cases of 19.117 million and ASIR of 418.92 per 100,000."
  - "The authors interpret rising case counts amid stable ASIR as driven by population ageing, with prevention and health-care equity implications."
abstract: "Background Alzheimer disease (AD) is a growing global health issue, with incidence varying by gender, age, and region. Understanding these trends is essential for developing effective prevention strategies as the population ages. Unlike previous Global Burden of Disease (GBD) studies that primarily focussed on prevalence and mortality, we offer a novel perspective by examining historical incidence trends and projecting future patterns of AD and other dementias using advanced analytical approaches. Methods We used data from 204 countries and 21 global regions from the GBD 2021 database. We applied the age-period-cohort (APC) model to analyse historical incidence trends, and the Bayesian APC (BAPC) model to forecast future incidence from 2022-36. These models help reveal changes related to age, period, and birth cohort and enable forecasting of future trends - analytical perspectives not provided in the original GBD data sets or their supplementary documents. Results Between 1992-2021, global AD cases increased from 4.078 million to 9.837 million, while the global age-standardised incidence rate (ASIR) remained relatively stable, rising slightly from 117.7 to 119.8 per 100 000. ASIR increased significantly in high-middle and middle-sociodemographic index regions, but declined in the low-sociodemographic index regions. Women consistently exhibited higher incidence rates than men across all regions. Projections indicate that 2036 global AD cases will reach 19.117 million, with an ASIR of 418.92 per 100 000. Conclusions While global ASIR has remained stable, the number of AD cases continues to rise due to population ageing, particularly in middle- and high-income regions. Low-income regions face additional challenges due to limited health care resources. Gender disparities and unequal access to health care contribute to the variations in disease burden. These findings emphasise the need to prioritise early diagnosis and implement targeted interventions to reduce future disease burdens and address global health care inequalities."
---

# Global incidence trends and projections of Alzheimer disease and other dementias: an age-period-cohort analysis 2021

> **Grounding note: abstract-only.** The full-text PDF, tables, figures, appendices, analysis code, and detailed methods were not provided. This ARA is compiled only from `metadata.json` and `metadata.md`. Fields not derivable from those inputs are marked "Not available from provided input." No numbered tables or figures exist in the provided source material, so the evidence layer is intentionally empty.

## Overview

This paper uses GBD 2021 data from 204 countries and 21 global regions to analyze historical incidence trends for Alzheimer disease and other dementias with an age-period-cohort model, and to forecast future incidence from 2022-36 with a Bayesian age-period-cohort model. The abstract frames the contribution as incidence-focused, in contrast to prior GBD work that primarily emphasized prevalence and mortality.

The abstract reports that global cases increased substantially from 1992 to 2021 while global ASIR changed only slightly, with region- and sex-stratified differences. It also reports a 2036 projection for global cases and ASIR. Detailed model specification, uncertainty intervals, tables, figures, and supplementary analyses are not available from the provided input.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions from the abstract |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01-C05) |
| [concepts.md](logic/concepts.md) | 8 abstract-supported technical terms |
| [experiments.md](logic/experiments.md) | 3 directional analysis plans (E01-E03) |
| [related_work.md](logic/related_work.md) | Typed dependencies supported by the abstract |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations, assumptions, and boundary conditions |
| [solution/study_design.md](logic/solution/study_design.md) | Abstract-level study design and analytical workflow |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Data source and reproducibility environment status | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 6-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Empty evidence-object ledger; no numbered tables or figures in provided abstract/metadata |
