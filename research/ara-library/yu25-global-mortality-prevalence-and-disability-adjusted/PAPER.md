---
title: "Global mortality, prevalence and disability-adjusted life years of Alzheimer's disease and other dementias in adults aged 60 years or older, and the impact of the COVID-19 pandemic: a comprehensive analysis for the global burden of disease 2021"
authors: ["Dongting Yu", "Rui-xuan Li", "Jing Sun", "Xuewen Rong", "Xu-Guang Guo", "Guo-Dong Zhu"]
year: 2025
venue: "BMC Psychiatry"
doi: "10.1186/s12888-025-06661-2"
ara_version: "1.0"
grounding: abstract-only
domain: "Alzheimer's disease epidemiology / global burden of disease / public health"
keywords: ["Alzheimer's disease", "other dementias", "GBD 2021", "mortality", "prevalence", "DALYs", "COVID-19", "EAPC", "BAPC", "health inequality"]
claims_summary:
  - "In 2021, global mortality from Alzheimer's disease and other dementias among adults aged 60 years or older reached approximately 1,922,970.75 cases, and prevalence reached 52,560,253.51 cases."
  - "High Body Mass Index and High Fasting Plasma Glucose were prominent risk factors."
  - "Projections suggest a near fourfold increase in AD cases by 2050, driven by population growth and aging, with females disproportionately affected."
  - "Health inequalities persist, with higher disease burdens in high-SDI regions."
  - "The COVID-19 pandemic impacted mortality unevenly, highlighting regional disparities."
  - "Although incidence rates declined from 1990 to 2021, the overall burden remains substantial and is expected to rise significantly by 2050."
abstract: "Alzheimer's disease (AD) and other dementias are major public health concerns with an increasing global impact. The burden of these conditions varies by region, age, and gender, and the COVID-19 pandemic has further exacerbated these disparities, potentially influencing disease prevalence, mortality, and disability burden. This study aimed to assess the global and regional burden and trends of Alzheimer's disease and other dementias in adults aged 60 years or older from 1990 to 2021, with a particular focus on the impact of the COVID-19 pandemic on mortality, prevalence, and disability-adjusted life years. Using Global Burden of Disease (GBD 2021) data, we analyzed age-standardized death rates (ASDR), incidence rates (ASIR), prevalence rates (ASPR), and disability-adjusted life years (DALYs) from 1990 to 2021. Temporal trends were assessed using the Estimated Annual Percentage Change (EAPC). Projections were modeled using Bayesian Age-Period-Cohort (BAPC) techniques. We evaluated excess mortality by comparing actual versus expected deaths during the pandemic. Decomposition analysis examined the contributions of population growth, aging, and epidemiological shifts. We analyzed health inequality to highlight and address disparities in health status and resource access across regions. All plots and tables were created using Joinpoint Regression model (Version 4.8.0.1), StataMP 18, and R statistical packages (Version 4.4.1). In 2021, global mortality from AD and other dementias among individuals aged 60 and older reached approximately 1,922,970.75 cases (95% CI: 480,348.08 to 5,104,315.95), and the prevalence was 52,560,253.51 cases (95% CI: 41,399,948.84 to 65,633,448.71). High Body Mass Index (BMI) and High Fasting Plasma Glucose (FPG) were prominent risk factors. Projections suggest a near fourfold increase in AD cases by 2050, driven by population growth and aging, with females disproportionately affected. Health inequalities persist, with higher disease burdens in high-SDI regions. The pandemic impacted mortality unevenly, highlighting regional disparities. Although incidence rates declined from 1990 to 2021, the overall burden of AD and dementias remains substantial and is expected to rise significantly by 2050. The findings underscore the need for targeted interventions addressing risk factors like High FPG, gender disparities, and the socioeconomic effects of COVID-19, particularly in high-SDI countries."
---

# Global mortality, prevalence and disability-adjusted life years of Alzheimer's disease and other dementias in adults aged 60 years or older

> **Grounding: abstract-only.** No full-text PDF, figures, tables, appendices, or source code were provided. This ARA is compiled only from `metadata.json` and `metadata.md`. Every unsupported field says "Not available from provided input"; no claims, numbers, experiments, dead ends, or evidence objects are invented.

## Overview

Yu et al. analyze the global and regional burden of Alzheimer's disease and other dementias among adults aged 60 years or older using GBD 2021 data from 1990 to 2021. The abstract reports trend analysis with EAPC, projections with BAPC, pandemic excess-mortality comparisons, decomposition analysis, and health-inequality analysis.

The abstract reports 2021 global mortality and prevalence case counts with confidence intervals, identifies High BMI and High FPG as prominent risk factors, and states that projected AD cases may rise nearly fourfold by 2050. Methodological details, full tables, regional estimates, model specifications, and all plotted outputs are not available from the provided input.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions from abstract/metadata |
| [claims.md](logic/claims.md) | 6 abstract-grounded claims (C01-C06) |
| [concepts.md](logic/concepts.md) | 12 paper-specific epidemiological and modeling concepts |
| [experiments.md](logic/experiments.md) | 6 directional analysis plans (E01-E06) |
| [related_work.md](logic/related_work.md) | Typed dependency graph from sources named in the abstract |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Study design reconstructable from the abstract |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Data/software environment reported in the abstract; no code provided | C01-C06 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 8-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index; no numbered tables or figures available from provided input |
