---
title: "Contribution of Modifiable Midlife and Late-Life Vascular Risk Factors to Incident Dementia."
authors: ["Jason R Smith", "James R. Pike", "R. Gottesman", "D. Knopman", "P. Lutsey", "P. Palta", "B. Windham", "Elizabeth Selvin", "M. Szklo", "Karen Bandeen-Roche", "J. Coresh", "A. Sharrett", "Alden L. Gross", "Jennifer A. Deal"]
year: 2025
venue: "JAMA Neurology"
doi: "10.1001/jamaneurol.2025.1495"
ara_version: "1.0"
grounding: abstract-only
domain: "dementia epidemiology / vascular risk factors / population attributable fraction"
keywords: ["dementia", "ARIC", "vascular risk factors", "hypertension", "diabetes", "smoking", "population attributable fraction", "midlife", "late life", "APOE e4"]
claims_summary:
  - "In ARIC, 21.8%, 26.4%, and 44.0% of dementia cases by age 80 were attributed to at least one vascular risk factor measured at ages 45-54, 55-64, and 65-74 years, respectively."
  - "Attributable fractions were higher in APOE e4 noncarriers at age 55 years and older, Black individuals at age 45 years and older, and female individuals at age 55 years and older."
  - "Only 2% to 8% of dementia cases after age 80 were attributable to the studied vascular risk factors."
  - "The authors interpret optimal vascular health across the life course as potentially mitigating a sizeable proportion of dementia risk by age 80, assuming causal relationships."
abstract: "Importance\nMidlife vascular risk factors are associated with an elevated risk of dementia. However, the total contribution of vascular risk factors in midlife and late life with incident dementia is uncertain.\n\nObjective\nTo quantify the proportion of incident dementia attributable to modifiable vascular risk factors measured in midlife and late life and to examine differences by apolipoprotein e4 genotype, self-reported race, and sex.\n\nDesign, Setting, and Participants\nThis was a prospective cohort analysis of the Atherosclerosis Risk in Communities (ARIC) study using 33 years of follow-up (1987-2020). The setting included ARIC field centers (Jackson, Mississippi; Forsyth County, North Carolina; Minneapolis suburbs, Minnesota; Washington County, Maryland). Study baseline in Black and White participants with complete exposure and covariate data was set by age at risk factor measurement (45-54 years, 55-64 years, and 65-74 years). Data were analyzed from August 2023 to December 2024.\n\nExposures\nHypertension (systolic blood pressure [BP] >=130 mm Hg, diastolic BP >=80 mm Hg, or use of medication for BP), diabetes (fasting glucose >=126 mg/dL, nonfasting glucose >=200 mg/dL, self-reported physician's diagnosis, or use of any diabetes medication), and current smoking (self-reported).\n\nMain Outcomes and Measures\nIncident dementia. Population attributable fractions were estimated by age 80 years, and separately after 80 years, from having at least 1 vascular risk factor by age at risk factor measurement.\n\nResults\nA total of 7731 participants were included in analysis of risk factors measured at age 45 to years (4494 female [58%]; 2207 Black [29%]; 5524 White [71%]), 12 274 contributed to analysis of risk factors measured at age 55 to 64 years (6698 female [55%]; 2886 Black [24%]; 9388 White [76%]), and 6787 contributed to analysis of risk factors measured at age 65 to 74 years (3764 female [56%], 1375 Black [20%]; 5412 White [80%]). There were 801, 995, and 422 dementia cases by 80 years, respectively. The fraction of dementia by 80 years attributable to at least 1 vascular factor at age 45 to 54 years was 21.8% (95% CI, 14.3%-29.3%), at 55 to 64 years was 26.4% (95% CI, 19.1%-33.6%), and at 65 to 74 years was 44.0% (95% CI, 30.9%-57.2%). Attributable fractions for these factors were higher in apolipoprotein e4 noncarriers at age 55 years and older (range, 33.3%-61.4%), Black individuals at age 45 years and older (range, 25.5%-52.9%), and female individuals at age 55 years and older (range, 29.2%-51.3%). Only 2% to 8% of dementia cases after 80 years were attributable to these factors.\n\nConclusions and Relevance\nResults of this cohort study suggest that between 22% and 44% of incident dementia cases by 80 years in the ARIC study were attributed to midlife and late-life vascular risk factors. Assuming causal relationships, maintaining optimal vascular health across the life course could mitigate a sizeable proportion of dementia risk by 80 years."
---

# Contribution of Modifiable Midlife and Late-Life Vascular Risk Factors to Incident Dementia.

> **Grounding: abstract-only.** This ARA was compiled only from `metadata.json` and `metadata.md`.
> No full-text PDF, tables, figures, appendix, statistical model details, or code were provided.
> Unsupported details are explicitly marked "Not available from provided input."

## Overview

This prospective cohort analysis of the Atherosclerosis Risk in Communities (ARIC) study quantifies
the proportion of incident dementia attributable to modifiable vascular risk factors measured at
different midlife and late-life age windows. The abstract reports analyses for ages 45-54, 55-64,
and 65-74 years, using incident dementia by age 80 and after age 80 as outcomes.

The reported abstract-level result is that dementia by age 80 had substantial population
attributable fractions for having at least one vascular risk factor, while dementia after age 80 had
much smaller attributable fractions. The abstract also reports subgroup differences by APOE e4
carrier status, self-reported race, and sex. The detailed estimands, models, covariates, diagnostic
ascertainment procedures, and tables/figures are not available from provided input.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions grounded in the abstract |
| [claims.md](logic/claims.md) | 4 falsifiable claims (C01-C04) with source-bound numbers |
| [concepts.md](logic/concepts.md) | 8 technical concepts defined from the abstract |
| [experiments.md](logic/experiments.md) | 4 directional analysis plans (E01-E04) |
| [related_work.md](logic/related_work.md) | Source-bounded dependency graph |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and unavailable details |
| [solution/study_design.md](logic/solution/study_design.md) | Study design reconstructable from the abstract |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Data, cohort, exposure, outcome, and reproducibility notes; no runnable artifacts supplied | C01-C04 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 6-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index; no numbered tables or figures available from provided input |
