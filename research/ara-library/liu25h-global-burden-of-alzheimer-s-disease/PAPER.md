---
title: "Global burden of Alzheimer's disease and other dementias in adults aged 65 years and over, and health inequality related to SDI, 1990-2021: analysis of data from GBD 2021"
authors: [Wen Liu, Wei Deng, Xinhao Gong, Jinping Ou, Shuchun Yu, Shoulin Chen]
year: 2025
venue: "BMC Public Health"
doi: "10.1186/s12889-025-22378-z"
ara_version: "1.0"
grounding: abstract-only
domain: "Public health epidemiology — dementia burden and health inequality"
keywords: [Alzheimer's disease, dementia, GBD 2021, DALYs, mortality, SDI, frontier analysis, slope inequality index, concentration index, health inequality]
claims_summary:
  - "Global age-standardized DALYs and mortality rates for adults aged 65 and older with Alzheimer's disease and other dementias declined over 1990-2021."
  - "The dementia disease burden among adults aged 65 and older is significantly associated with SDI."
  - "High-SDI countries have 169% higher baseline dementia burden than low-SDI countries at their current level of social development."
  - "Although DALYs increase with SDI overall, the dementia burden is primarily concentrated in lower-SDI populations because non-developed countries account for most of the population."
  - "Most countries have dementia burden above the minimum burden associated with their SDI, while low- and middle-SDI burden is increasing and gaps across SDI regions are narrowing."
  - "The global population aged 65 and older experiences a significant reduction in healthy life expectancy due to dementia."
abstract: "The disease burden of dementia in the elderly is predicted to rise, and dementia among older adults has become a crucial issue for public health. Quantifying the disease burden of dementia in the elderly can provide relevant areas and countries with scientific data to help them adjust their healthcare strategies. We analyzed the disease burden of Alzheimer's disease and other dementias among individuals aged 65 and older from 1990 to 2021; the relationship between mortality rates and disability-adjusted life years (DALYs) with socio-demographic index (SDI); conducted a frontier analysis of the disease burden across 204 countries; and quantified inequalities in age-standardized DALYs for Alzheimer's disease and other dementias using the slope inequality index and concentration index. Globally, age-standardized DALYs and mortality rates for individuals aged 65 and older have declined over time. We find that the disease burden of dementia is significantly associated with SDI. High SDI countries have 169% higher baseline levels of dementia burden compared to low SDI countries, as estimated based on their current level of social development. Finally, our health inequality analyses reveal that while the overall trend of DALYs for dementia increases with SDI, the burden is primarily concentrated in populations with lower SDI, as non-developed countries account for the majority of the population. The global population aged 65 and older experiences a significant reduction in healthy life expectancy due to dementia. The burden of disease in most countries is higher than the minimum disease burden associated with SDI in those countries. The burden of disease in low and middle SDI countries has been showing an increasing trend. The gap in disease burden among regions with different SDI levels is also continuously narrowing."
---

# Global burden of Alzheimer's disease and other dementias in adults aged 65 years and over, and health inequality related to SDI, 1990-2021

> **Grounding note: abstract-only.** The only provided inputs are `metadata.json` and `metadata.md`. No full-text PDF, tables, figures, appendices, code, or supplementary files were provided. Fields not supported by the provided abstract/metadata are marked "Not available from provided input". No claims, exact estimates, dead ends, or implementation details are added beyond those inputs.

## Overview

This paper analyzes the global disease burden of Alzheimer's disease and other dementias among adults aged 65 years and older using GBD 2021 data over 1990-2021. From the abstract, the study links dementia mortality and DALYs to SDI, conducts frontier analysis across 204 countries, and evaluates inequality in age-standardized DALYs using the slope inequality index and concentration index.

The abstract reports declining global age-standardized DALYs and mortality rates over time, a significant association between dementia burden and SDI, a 169% higher baseline burden in high-SDI versus low-SDI countries, and a distributional pattern in which lower-SDI populations carry much of the burden because non-developed countries account for most of the population. It also reports that most countries exceed the minimum burden associated with their SDI, low- and middle-SDI burden is increasing, and cross-SDI gaps are narrowing.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions from the abstract |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01-C06) |
| [concepts.md](logic/concepts.md) | 8 abstract-grounded technical terms |
| [experiments.md](logic/experiments.md) | 4 directional analysis plans (E01-E04) |
| [related_work.md](logic/related_work.md) | Typed dependency graph from metadata/abstract only |
| [solution/constraints.md](logic/solution/constraints.md) | Boundaries, assumptions, and limitations |
| [solution/study_design.md](logic/solution/study_design.md) | GBD 2021 burden, SDI, frontier, and inequality analysis design |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Reproducibility context and missing implementation artifacts | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 7-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Empty numbered-object ledger; no figures/tables available from inputs |
