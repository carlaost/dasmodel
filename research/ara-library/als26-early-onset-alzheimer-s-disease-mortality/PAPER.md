---
title: "Early-onset Alzheimer's disease mortality in the United States: A population-based study of trends and disparities, 2015-2024."
authors: [A. Alsalahat, A. B. Abdul Jabbar, Keara Kennedy, Andy Song, Maura Hackett, Majd A Abualrob, Himanshu Verma, Jagkirat Singh, E. Bernitsas]
year: 2026
venue: "Journal of Alzheimer's Disease (JAD)"
doi: "10.1177/13872877261453030"
ara_version: "1.0"
grounding: abstract-only
domain: "Epidemiology / population health — dementia mortality surveillance"
keywords: [early-onset Alzheimer's disease, mortality, CDC WONDER, age-adjusted mortality rate, Joinpoint regression, health disparities, ICD-10-CM G30.0, rate ratio, late-onset Alzheimer's disease, United States]
claims_summary:
  - "Reported EOAD mortality (AAMR per 1,000,000) rose from 0.14 (2015) to 2.59 (2024), annual percent change +19.96%."
  - "Females had higher EOAD mortality than males (RR = 1.50, 95% CI 1.40-1.59); 63.7% of the 4890 deaths were female."
  - "Non-Hispanic White individuals exhibited the highest EOAD mortality among racial/ethnic groups."
  - "Residents of the Midwest census region exhibited the highest EOAD mortality among US regions."
  - "Mean age at death was 69.8 years, with the greatest number of deaths in the 65-74 age band."
  - "The increase in late-onset Alzheimer's disease (G30.1) mortality was lower than that of EOAD (G30.0)."
abstract: "Background: Population-level data on trends and disparities in early-onset Alzheimer's disease (EOAD) mortality are limited. Objective: This study aimed to examine demographic disparities and trends in mortality from EOAD in the US from 2015 to 2024. Methods: We analyzed US mortality data from the Centers for Disease Control and Prevention Wide-ranging Online Data for Epidemiologic Research (CDC WONDER), 2015-2024. We examined and identified mortality from EOAD as the underlying cause of death (UCD) using the International Classification of Disease-10-Clinical Modification code, G30.0. Age-adjusted mortality rates (AAMRs) per 1,000,000 population were extracted. Temporal trends were assessed with Joinpoint regression, and demographic disparities were analyzed and compared using rate ratios (RR) of AAMRs. Sensitivity analysis compared EOAD trends with late-onset Alzheimer's disease (G30.1). Results: Among 4890 EOAD-related deaths (63.7% female), mortality increased from 0.14 to 2.59 per 1,000,000 between 2015 and 2024 (annual percent change: +19.96%). Females had higher mortality than males (RR = 1.50, 95% CI: 1.40 to 1.59). Non-Hispanic White individuals and residents of the Midwest exhibited the highest mortality rates. The mean age at death was 69.8 years, with the greatest number of deaths occurring between the ages of 65 and 74 years. In comparison, the increase in late-onset Alzheimer's disease mortality was lower than that of EOAD. Conclusions: Reported EOAD mortality increased markedly in the US, with significant sex, racial, and regional disparities. These findings highlight persistent inequities in EOAD diagnosis and care and underscore the need for improved recognition and equitable access to specialized dementia care."
---

# Early-onset Alzheimer's Disease Mortality in the United States (2015-2024)

## Grounding note

**Full text was unavailable (no licit open-access copy).** Unpaywall reports `oa_status: closed`
(is_oa false); Europe PMC reports `isOpenAccess: N`, `inPMC: N`; the article is subscription-only
via SAGE. This ARA is therefore an **abstract-only compile**: all content is grounded in the
published abstract (`metadata.md` / `metadata.json`) and the verified `sources.yaml`. Where the
abstract does not support a section, the file states "Not available from provided input (no full
text)". No numbers, tables, or figures have been fabricated. The `trace/exploration_tree.yaml`
reconstructs the study's logic with `support_level: inferred` for nodes not directly stated.

## Overview

This is a population-based, retrospective observational study of United States mortality attributed
to early-onset Alzheimer's disease (EOAD). Using de-identified death-certificate data from CDC
WONDER (2015-2024), the authors identified EOAD deaths by ICD-10-CM underlying-cause code **G30.0**,
computed age-adjusted mortality rates (AAMRs) per 1,000,000 population, characterized temporal
trends with Joinpoint regression, and quantified demographic disparities (sex, race/ethnicity,
census region, age) via rate ratios (RR) of AAMRs. A sensitivity analysis contrasted EOAD trends
with late-onset Alzheimer's disease (LOAD, code **G30.1**). The headline finding is a steep reported
rise in EOAD AAMR (0.14 → 2.59 per 1,000,000; annual percent change +19.96%) alongside significant
sex, racial, and regional disparities, framed as reflecting inequities in EOAD recognition and care.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions (abstract-grounded) |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01-C06) with abstract-sourced numbers |
| [concepts.md](logic/concepts.md) | 9 technical terms (EOAD, LOAD, AAMR, APC, Joinpoint, RR, UCD, ICD-10-CM coding, CDC WONDER) |
| [experiments.md](logic/experiments.md) | 6 declarative analysis plans (E01-E06), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph; CDC WONDER data source as first-class dependency |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Study design and analytic method (as far as abstract supports) |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Analytical environment; CDC WONDER data source, ICD codes, access | all |
| [../data/dataset.md](data/dataset.md) | CDC WONDER mortality dataset provenance and variables | all |

No code was released and no code/pseudocode appears in the abstract, so `src/execution/` is
intentionally absent (Rule 14).

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node reconstructed research DAG (mostly `inferred`) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index; no full text ⇒ no source tables/figures extractable (completeness N/A) |
