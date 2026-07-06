---
title: "Trend analysis and future predictions of global burden of alzheimer's disease and other dementias: a study based on the global burden of disease database from 1990 to 2021"
authors: [Miao Hao, Jiajun Chen]
year: 2025
venue: "BMC Medicine"
doi: "10.1186/s12916-025-04169-w"
ara_version: "1.0"
grounding: abstract-only
domain: "Epidemiology — global burden of disease forecasting for Alzheimer's disease and other dementias"
keywords: [Alzheimer's disease, dementia, Global Burden of Disease, incidence, prevalence, DALYs, Joinpoint regression, age-period-cohort model, Socio-demographic Index, forecasting]
claims_summary:
  - "The global burden of Alzheimer's disease and other dementias increased from 1990 to 2021, with East Asia reporting the highest incidence, prevalence, and DALYs."
  - "Prevalence increased notably among females older than 65 years compared with males."
  - "Joinpoint analysis identified trend changes in 1995, 2005, 2011, and 2019, with acceleration after 2011 and especially after 2019."
  - "Age is a significant risk factor, with risk increasing sharply after age 60."
  - "Bayesian age-period-cohort modeling projects continued growth through 2040, with age-standardized incidence and prevalence reaching 144.85 and 821.80 per 100,000."
abstract: "As the global aging issue grows, dementia, particularly Alzheimer's disease (AD), has become a major public health challenge for everyone. This study utilizes the Global Burden of Disease (GBD) database to analyze trends in the epidemiology of AD and other dementias from 1990 to 2021 and to predict future burdens to 2040. We examined global, regional, and national data on AD and other dementias, focusing on incidence, prevalence, and Disability-Adjusted Life Years (DALYs). Joinpoint regression analysis was employed to identify significant changes in trends over time. The effects of age, period, and birth cohort on the risk of AD and other dementias were analyzed. Additionally, the impact of aging, population growth, and epidemiological changes on DALYs was assessed across different Socio-demographic Index (SDI) quintiles. The global burden of AD and other dementias has significantly increased, with the highest incidence, prevalence, and DALYs observed in East Asia. A notable increase in prevalence was observed in females over 65 years compared to males. Joinpoint regression analysis revealed substantial changes in trends in 1995, 2005, 2011, and 2019, with a noticeable acceleration post-2011, especially after 2019. Age was a significant risk factor, with a sharp increase in risk after 60 years of age. Epidemiological changes had a minor impact globally but varied by region and gender. Bayesian age-period-cohort modeling predicts sustained growth through 2040, with age-standardized incidence and prevalence rates projected to reach 144.85 and 821.80 per 100,000 respectively, driven predominantly by aging populations in high SDI regions and demographic expansion in low SDI regions. The global burden of AD and other dementias is escalating, with a pronounced increase expected by 2040. This study highlights the need for targeted interventions, particularly in regions with higher burdens and among older populations. The findings underscore the importance of considering SDI, age, and gender when planning public health strategies to address the growing challenge of AD and other dementias."
---

# Trend analysis and future predictions of global burden of alzheimer's disease and other dementias

> **Grounding note: abstract-only.** The provided input consists only of `metadata.json` and `metadata.md`; no full-text PDF, tables, figures, appendices, code, or complete reference list was provided. This ARA is therefore reconstructed strictly from the abstract and metadata. Fields not derivable from the provided input are marked "Not available from provided input." No evidence table or figure files are generated because no numbered source objects are available to enumerate or screenshot.

## Overview

Hao and Chen analyze Global Burden of Disease (GBD) data for Alzheimer's disease and other dementias from 1990 to 2021 and forecast future burden through 2040. The abstract describes global, regional, and national analyses of incidence, prevalence, and disability-adjusted life years (DALYs), using Joinpoint regression, age-period-cohort analysis, decomposition of DALY drivers across SDI quintiles, and Bayesian age-period-cohort forecasting.

The abstract reports increasing global burden, highest burden in East Asia, higher prevalence growth among females over 65 than males, trend changes in 1995, 2005, 2011, and 2019, sharply rising age-related risk after 60, and projected 2040 age-standardized incidence and prevalence rates of 144.85 and 821.80 per 100,000. Exact data tables, model specifications, uncertainty intervals, and software details are not available from provided input.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations -> gaps -> key insight (abstract-grounded) |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01-C05) |
| [concepts.md](logic/concepts.md) | 8 key technical terms |
| [experiments.md](logic/experiments.md) | 5 directional analysis plans (E01-E05) |
| [related_work.md](logic/related_work.md) | Typed dependency graph from abstract-visible dependencies |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations, assumptions, and unavailable implementation details |
| [solution/study_design.md](logic/solution/study_design.md) | Abstract-grounded study design and analysis workflow |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Data source, analytical environment, and unavailable reproducibility fields | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 8-node research DAG reconstructed from abstract/metadata |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Empty ledger — no full text, tables, or figures provided |
