---
title: "Trends and Disparities in Alzheimer Disease-Related Mortality in the United States From 1999 to 2020: A CDC WONDER Analysis"
authors: ["Sophia Ahmed", "M. Shoaib", "H. Farooqi", "M. Nadir", "M. M. Sajid", "H. W. Saeed", "Mahrukh Iqbal", "M. Sohaib", "V. Barun", "Sheetal Goyal"]
year: 2026
venue: "Alzheimer Disease and Associated Disorders"
doi: "10.1097/WAD.0000000000000712"
ara_version: "1.0"
domain: "Epidemiology — population-level mortality surveillance (Alzheimer disease)"
keywords: ["Alzheimer disease", "mortality", "CDC WONDER", "age-adjusted mortality rate", "joinpoint regression", "health disparities", "ICD-10", "United States", "race/ethnicity", "geographic disparities"]
grounding: abstract-only
claims_summary:
  - "AD-related mortality in the US rose significantly from 1999 to 2020 (AAPC 3.18)"
  - "6,697,209 AD-attributed deaths occurred over the period (overall AAMR 90.727 per 100,000)"
  - "Females had higher AD AAMR (94.31) than males (83.23)"
  - "Non-Hispanic Black individuals had the highest AAMR by race/ethnicity (94.53); non-Hispanic Asian the lowest (46.16)"
  - "Rural areas had higher AAMR (95.080) than urban areas (89.772)"
  - "The Midwest had the highest regional AAMR (96.131); the Northeast the lowest (78.564)"
  - "Substantial state-level variation (e.g. South Carolina 119.789 vs New York 64.16)"
  - "Adults aged 85+ had the highest crude mortality rate (3574.928)"
abstract: "BACKGROUND: Alzheimer disease (AD) is a leading cause of mortality in the United States; yet, population-level mortality trends and disparities remain underexplored. OBJECTIVE: This study aimed to evaluate AD-related mortality trends from 1999 to 2020 and assess disparities by demographic and geographic factors. METHODS: Data were obtained from the CDC WONDER database. Deaths were identified using ICD-10 codes for AD (F01, F03, G30, G31.1) among individuals aged 45 years and older. Crude mortality rates (CMRs) and age-adjusted mortality rates (AAMRs) per 100,000 population were calculated. Joinpoint regression analysis was used to assess trends, and disparities were analyzed by sex, race/ethnicity, age, urbanization, census region, and state. RESULTS: From 1999 to 2020, 6,697,209 deaths were attributed to AD (AAMR: 90.727). Mortality rates increased significantly (AAPC: 3.18). Females had higher AAMRs (94.31) than males (83.23). Non-Hispanic Black individuals had the highest AAMR (94.53), followed by non-Hispanic White (93.73), non-Hispanic American Indian (66.80), Hispanic (66.33), and non-Hispanic Asian individuals (46.16). Individuals aged 85 years and older had the highest CMR (3574.928). Rural areas had higher AAMRs (95.080) than urban areas (89.772). The Midwest had the highest AAMR (96.131), whereas the Northeast had the lowest (78.564). States such as South Carolina (119.789) and Tennessee (113.624) had higher AAMRs compared with New York (64.16) and Florida (68.677). CONCLUSIONS: Significant disparities exist in AD-related mortality across demographic and geographic groups. These findings highlight the need for targeted public health interventions, improved health care access, and early diagnostic efforts."
---

# Trends and Disparities in Alzheimer Disease-Related Mortality in the United States From 1999 to 2020: A CDC WONDER Analysis

## Overview

This is a retrospective, population-level epidemiological study of Alzheimer disease (AD)-related
mortality in the United States over 1999–2020, using the CDC WONDER Multiple Cause of Death
database. Deaths were identified by ICD-10 codes (F01, F03, G30, G31.1) among adults aged 45 and
older. The authors computed crude mortality rates (CMRs) and age-adjusted mortality rates (AAMRs)
per 100,000 population and applied joinpoint regression to characterize temporal trends. They
report a significant increase in AD-related mortality (Average Annual Percent Change, AAPC 3.18)
and substantial disparities across sex, race/ethnicity, age, urbanization, census region, and
state. The stated implication is a need for targeted public health interventions, improved health
care access, and earlier diagnosis.

> **Grounding: abstract-only.** No licit open-access full text was available (article paywalled
> via Ovid / Wolters Kluwer; Unpaywall `oa_status: closed`; no PMC/Europe PMC copy; PMID
> 41773884). This ARA is compiled from the structured abstract and verified `sources.yaml` only.
> All numbers reproduced here are quoted from the abstract; the paper's numbered tables and figures
> could not be accessed, so no table/figure evidence objects were extracted (see
> [evidence/README.md](evidence/README.md)). Fields that require full text are marked
> "Not available from provided input (no full text)."

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) grounded in the abstract |
| [concepts.md](logic/concepts.md) | 8 technical terms (CMR, AAMR, AAPC, joinpoint regression, ICD-10 AD coding, urbanization classification, census region, CDC WONDER) |
| [experiments.md](logic/experiments.md) | 6 declarative analysis plans (E01–E06), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph — data source + methodological/background references (abstract-limited) |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, boundary conditions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Descriptive-epidemiology study design and analysis pipeline |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Analytical environment, data source (CDC WONDER), tools | all |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node reconstructed research DAG (all `inferred` — no session record) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index — explains why no tables/figures were extracted (no full text) |
