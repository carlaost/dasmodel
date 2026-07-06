---
title: "Trends in Alzheimer's disease mortality with metabolic syndrome-related conditions among older adults in the United States, 1999-2020."
authors: [Taha Alam, Dhvanit Rajdeep, Sohaima Kamal, Iman Osman Abufatima, Mominah Majid, S. Siddiqui, Syed Ali Waheed, Areesha Nawaz, M. Faheem, Waqas Burney, Aneezeh Khatri, N. Usman, N. Aqeel]
year: 2026
venue: "Journal of Alzheimer's Disease (JAD)"
doi: "10.1177/13872877261445035"
ara_version: "1.0"
domain: "Epidemiology — mortality-trend analysis (Alzheimer's disease + metabolic syndrome)"
grounding: abstract-only
keywords: [Alzheimer's disease, metabolic syndrome, mortality, age-adjusted mortality rate, CDC WONDER, Joinpoint regression, health disparities, older adults, death certificates, United States]
claims_summary:
  - "444,488 of 2,355,233 AD-underlying-cause deaths in adults ≥75 (1999–2020) were related to metabolic syndrome conditions."
  - "AAMR for AD-with-metabolic-syndrome rose from 36.48 (1999) to 157.93 (2020) per 100,000."
  - "Women had consistently higher AAMRs than men (females 107.79 vs males 79.02)."
  - "Non-Hispanic African Americans had the highest AAMR among racial groups (121.65)."
  - "Marked geographic disparity: Mississippi in the top 90th percentile, Massachusetts in the lower 10th percentile."
abstract: "Background: Alzheimer's disease (AD) among patients with metabolic syndrome-related conditions is a global threat, contributing significantly to escalating mortality and economic burden. They demonstrate analogous pathophysiologies and risk determinants, highlighting the necessity for addressing this critical issue. Objective: This study analyzed demographic trends and disparities of AD with metabolic syndrome-related conditions among patients aged 75 and above from 1999 to 2020. Methods: This study examined the death certificates sourced from the CDC-WONDER database from 1999 to 2020, to analyze age-adjusted mortality rates (AAMRs) per 100,000 population. The Joinpoint regression model was used to assess trends in overall demographics, geographic, and place-of-death variables. Results: There were 2,355,233 deaths documented with AD listed as the underlying cause of death among older adults (aged ≥75), out of which 444,488 deaths were related to metabolic syndrome-related conditions from 1999 to 2020. The AAMR rose substantially from 36.48 in 1999 to 157.93 in 2020. Women consistently had higher AAMRs than males (females: 107.79, males: 79.02). Non-Hispanic African Americans (121.65) showed the highest mortality rates among all racial groups. However, from 1999 to the early to mid-2000s, all races highlighted a sharp peak in mortality rates. Striking geographical disparities were noted, with Mississippi in the top 90th percentile and Massachusetts in the lower 10th percentile. Conclusions: This study reveals the demographic and geographic variations in mortality rates, highlighting the modalities of interventions and the need for equitable healthcare access."
---

# Trends in Alzheimer's Disease Mortality with Metabolic Syndrome-Related Conditions Among Older Adults in the United States, 1999–2020

## Overview

This is a retrospective, population-level epidemiological study of mortality trends in the United States. Using US death-certificate data from the CDC WONDER Multiple Cause of Death database (1999–2020), the authors quantify age-adjusted mortality rates (AAMRs, per 100,000) for deaths where Alzheimer's disease (AD) is the underlying cause and a metabolic syndrome-related condition is also present, restricted to older adults aged ≥75. Trends over time and across demographic (sex, race/ethnicity), geographic (state, region), and place-of-death strata are characterized with Joinpoint regression. The central empirical finding is a large increase in AAMR over the two-decade window (36.48 → 157.93) alongside persistent sex, racial, and geographic disparities.

> **Grounding note (abstract-only):** No licit open-access full text was available for this article (Unpaywall: `is_oa:false`, no OA locations, no repository copy; Europe PMC: `isOpenAccess:N`, `inPMC:N`). This ARA is compiled from the bibliographic metadata and abstract only. Numerical values reproduced below are exactly those stated in the abstract; all method detail, tables, and figures beyond the abstract are marked "Not available from provided input (no full text)." No tables or figures were extracted (see `evidence/README.md`).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight for AD+metabolic-syndrome mortality trends |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06), grounded in abstract-reported figures |
| [concepts.md](logic/concepts.md) | 8 technical terms (AAMR, Joinpoint regression, underlying cause of death, etc.) |
| [experiments.md](logic/experiments.md) | 5 declarative analysis plans (E01–E05), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph (data source, methods, background) |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, boundary conditions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Study design and analysis strategy (abstract-supported) |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment; CDC WONDER data source; Joinpoint tooling |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 11-node research DAG (mostly `inferred` — abstract-only reconstruction) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index — no tables/figures extracted (no full text); completeness N/A |
