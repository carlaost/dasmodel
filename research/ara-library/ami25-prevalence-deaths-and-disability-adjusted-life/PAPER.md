---
title: "Prevalence, deaths and disability-adjusted life years due to Alzheimer's disease and other dementias in Middle East and North Africa, 1990–2021"
authors: [Fatemeh Amiri, Saeid Safiri, Ali Shamekh, Ali Ebrahimi, Mark J. M. Sullman, Ali-Asghar Kolahi]
year: 2025
venue: "Scientific Reports 15:7058"
doi: "10.1038/s41598-025-89899-w"
ara_version: "1.0"
domain: "Epidemiology / Global burden of disease — Alzheimer's disease and other dementias (neuroepidemiology)"
keywords: [Alzheimer's disease, dementia, Middle East and North Africa, burden of disease, prevalence, DALYs, mortality, Global Burden of Disease 2021, age-standardised rate, socio-demographic index]
grounding: full-text
claims_summary:
  - "In 2021 the MENA age-standardised prevalence of AD and other dementias was 772.7 per 100,000, a statistically significant 4.9% decrease vs 1990."
  - "Age-standardised death and DALY rates in MENA also decreased significantly (8.6% and 7.7% respectively) from 1990 to 2021."
  - "Country-level 2021 age-standardised prevalence ranged from 652.43 (UAE, lowest) to 828.25 (Lebanon, highest) per 100,000."
  - "Age-standardised point prevalence decreased significantly in 13 of 21 MENA countries; no significant change in the remaining 8."
  - "Females carried higher prevalence, death and DALY burden than males across all age groups, though the sex difference was not statistically significant."
  - "Burden rose with age, peaking at 80–84 (prevalence and DALYs) or 85–89 (deaths) before declining."
  - "The MENA burden remained higher than or equal to global rates across ages and sexes, but the MENA/Global DALY ratio was lower or equal in 2021 vs 1990 (decreasing trend)."
  - "Age-standardised DALY rate generally decreased with increasing SDI, with several countries deviating from SDI-expected values."
abstract: "Alzheimer's disease (AD) ranks among the leading causes of morbidity and mortality worldwide. The objective was to evaluate the burden of AD and other dementias among the countries of the Middle East and North Africa (MENA) region by age and sex from 1990 to 2021. The data were sourced from the Global Burden of Disease (GBD) study 2021. The estimates are presented as counts and age-standardised rates per 100,000 accompanied by 95% uncertainty intervals (UIs). In 2021, AD and other dementias recorded an age-standardised prevalence of 772.7 per 100,000 in the MENA region (95% UI 671.2–877.6 per 100,000). This rate decreased by 4.9% in comparison to 1990, marking a statistically significant change. AD and other dementias also accounted for approximately 73.79 thousand deaths in the region in 2021, with the age-standardised rate decreasing by 8.6% compared to 1990. Moreover, the disability-adjusted life years (DALY) rate was 476.3 per 100,000 population (95% UI 225.6–1004.2), representing a 7.7% decrease from 1990 to 2021. Lebanon registered the highest point prevalence per 100,000 at 828.25, while the United Arab Emirates recorded the lowest at 652.43. The age-standardised point prevalence decreased from 1990 to 2021 in 13 of the MENA countries, while no significant changes were observed in eight of countries. Additionally, in 2021, women experienced higher prevalence rates, DALYs, compared to men. In the MENA region, age-standardised dementia prevalence rose with age in both sexes. The burden of dementia in MENA has decreased from 1990 to 2021, but it remains higher than global estimates. Furthermore, the findings indicate that dementia imposes a greater burden on the female population compared to males. To achieve a more accurate estimation of the burden of Alzheimer's disease and other dementias, more systematic studies in low- to middle-income countries within the MENA region are required."
---

# Prevalence, deaths and DALYs due to Alzheimer's disease and other dementias in MENA, 1990–2021

## Overview

This is a **secondary descriptive-epidemiology study** that repackages Global Burden of Disease
(GBD) Study 2021 estimates to characterise the burden of Alzheimer's disease (AD) and other
dementias across the 21 countries of the Middle East and North Africa (MENA) region from 1990 to
2021. It reports prevalence, deaths, and disability-adjusted life years (DALYs) as counts and
age-standardised rates (ASRs) per 100,000 with 95% uncertainty intervals (UIs), stratified by
country, age, sex, and Socio-demographic Index (SDI). The paper performs no primary data
collection and no new statistical modelling of its own beyond descriptive plotting and
smoothing-spline visualisation; the underlying estimates are produced by IHME's GBD 2021 pipeline
(DisMod-MR 2.1, MR-BRT). The headline finding is that the MENA dementia burden declined slightly
and significantly (prevalence −4.9%, deaths −8.6%, DALYs −7.7% in ASR terms) between 1990 and 2021,
yet remained higher than global rates and disproportionately affected women.

This ARA was compiled from the full open-access text (CC BY-NC-ND) plus the verified `sources.yaml`.
The paper's main quantitative content is one main table (Table 1, all 21 countries + regional
aggregate) and four figures; supplementary Tables S1–S3 and Figures S1–S3 are referenced in the
text but live in the online supplement and were not part of the provided input (see
`evidence/README.md`).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) |
| [concepts.md](logic/concepts.md) | 10 technical terms (DALY, ASR, UI, DisMod-MR 2.1, SDI, MR-BRT, PAF, cognitive reserve, GBD, severity split) |
| [experiments.md](logic/experiments.md) | 6 verification/analysis plans (E01–E06) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's citation footprint |
| [solution/study_design.md](logic/solution/study_design.md) | GBD 2021 pipeline as used: case definition, modelling, compilation |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions and limitations |

### Physical/Artifact Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment; GBD 2021 / GHDx data source, R 3.5.2 |
| [data/dataset.md](data/dataset.md) | GBD 2021 provenance, access, variables |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG (inferred + explicit nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 1 table + 4 figures (+ S-material accounting) |
| [tables/table1.md](evidence/tables/table1.md) | Table 1 — full 21-country + regional counts, ASRs, % change |
| [figures/figure1.md](evidence/figures/figure1.md) | Fig 1 — ASR prevalence/deaths/DALYs by country & sex, 2021 |
| [figures/figure2.md](evidence/figures/figure2.md) | Fig 2 — counts & rates by age & sex, 2021 |
| [figures/figure3.md](evidence/figures/figure3.md) | Fig 3 — MENA/Global DALY ratio by age & sex, 1990 & 2021 |
| [figures/figure4.md](evidence/figures/figure4.md) | Fig 4 — ASR DALY vs SDI by country, 2021 |
