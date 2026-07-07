---
title: "Assessing and projecting the global impacts of Alzheimer's disease"
authors: [Nanlong Zhang, Shuren Chai, Jixing Wang]
year: 2025
venue: "Frontiers in Public Health 12:1453489"
doi: "10.3389/fpubh.2024.1453489"
ara_version: "1.0"
domain: "Epidemiology / Global burden of disease — Alzheimer's disease (neuroepidemiology, disease forecasting)"
keywords: [Alzheimer's disease, incidence, mortality, disability-adjusted life years, projection, Global Burden of Disease 2021, Estimated Annual Percentage Change, Generalized Additive Model, Socio-Demographic Index, age-standardized rate]
grounding: full-text
claims_summary:
  - "Global age-standardized DALY, death, and incidence EAPCs are projected to remain negative (declining) from 2022 to 2030: −1.4375 (DALYs), −1.7982 (deaths), −1.2718 (incidence)."
  - "Global male and female projected EAPCs both decline 2022–2030; the paper reports male death-rate EAPC −2.28 vs female −1.03, and — printed identically to the female death figure — female incidence EAPC −1.03 (male incidence −1.73)."
  - "Andean Latin America, Southern Latin America, and the Caribbean have the highest (most positive / rising) projected DALY EAPCs (0.94, 0.77, 0.59); Eastern Europe, Central Europe, and East Asia have the lowest (most negative) (−16.31, −12.03, −2.77)."
  - "Central Sub-Saharan Africa is projected to have the highest 2030 DALY ASR (22,703.53); Eastern Europe the lowest (1,404.84)."
  - "Cyprus, Serbia, and Montenegro have the highest positive country-level DALY EAPCs (12.55, 9.64, 5.16); Bahrain, Armenia, and Qatar the lowest (−87.28, −85.40, −85.39)."
  - "Cyprus and North Macedonia are projected to have the highest 2030 country DALY ASRs (296,472.95; 260,543.83); Armenia, Bulgaria, and Romania the lowest (all printed as 0.05)."
  - "Countries with SDI ≥0.8 (and, separately, ≥0.7) show significantly higher 2030 ASIR, ASDR, and DALY ASR than countries below the threshold; across the five SDI categories, high-SDI regions have the highest values and low-SDI the lowest, all comparisons highly significant."
  - "Across five continents, SDI–burden correlations are weak-to-moderate and mostly non-significant; Oceania has the strongest (ASIR R²=0.203, p=0.0463; DALY R²=0.204, p=0.0459), Africa the weakest (ASIR R²=0.008, p=0.0699)."
abstract: "Background: This study aims to assess the global burden of Alzheimer's disease (AD) from 1990 to 2030, with a focus on incidence, mortality, and disability-adjusted life years (DALY). Methods: Data on the incidence rates, DALY rates, and death rates of AD across various geographic populations from 1990 to 2021 were obtained from the Global Burden of Disease (GBD) 2021 study. Generalized Additive Models (GAMs) were employed to forecast the disease burden from 2022 to 2030. Results: The projected global burden of Alzheimer's disease from 2022 to 2030 indicates a decrease in DALYs, with an Estimated Annual Percentage Change (EAPC) of −1.44 (95% CI: −1.45, −1.42). Similarly, death rates and incidence rates also show a decline, with EAPCs of −1.80 (95% CI: −1.83, −1.77) and −1.27 (95% CI: −1.29, −1.26) respectively. Gender-specific analysis reveals that the projected global incidence EAPC from 2022 to 2030 is estimated at −1.73 (95% CI: −1.75, −1.70) for males and −1.03 (95% CI: −1.04, −1.02) for females. Regionally, Andean Latin America and the Caribbean exhibit the highest positive EAPCs for DALYs at 0.94 (95% CI: 0.93, 0.94) and 0.59 (95% CI: 0.59, 0.60) respectively, while Eastern Europe shows the lowest EAPC at −16.31 (95% CI: −18.60, −13.95). Country-specific projections highlight Cyprus and Serbia with the highest positive EAPCs for DALYs at 12.55 (95% CI: 11.21, 13.91) and 9.6416 (95% CI: 8.86, 10.4333) respectively. On the other hand, Bahrain and Armenia exhibit significant negative EAPCs at −87.28 (95% CI: −94.66, −69.70) and −85.41 (95% CI: −92.80, −70.41). An analysis based on the Socio-Demographic Index (SDI) reveals that regions with higher SDI values have greater burdens of AD, with countries having SDI ≥ 0.8 showing significantly higher age-standardized Incidence Rates (ASIR), age-standardized Death Rates (ASDR), and age-standardized DALY rates compared to those with SDI < 0.8. Conclusion: From 1990 to 2030, global burden of AD is projected to decrease, with significant gender and regional disparities. Regions with higher SDI show higher disease burdens, underscoring the necessity for targeted interventions and customized public health strategies to effectively address AD in varied socio-economic settings."
---

# Assessing and projecting the global impacts of Alzheimer's disease

## Overview

This is a **secondary descriptive-and-forecasting epidemiology study**. It re-expresses Global
Burden of Disease (GBD) 2021 estimates of Alzheimer's disease (AD) incidence, death, and DALY
rates for 1990–2021, and then uses **Generalized Additive Models (GAMs)** to forecast
age-standardized rates (ASRs) and **Estimated Annual Percentage Change (EAPC)** from 2022 to
2030 — globally, by sex, by five SDI (Socio-demographic Index) tiers, by 18 GBD regions, and by
individual country. It performs no primary data collection; all base estimates come from the
GHDx GBD 2021 tool. The paper's own analytical contribution is the GAM-based projection, the EAPC
calculation over both the historical (1990–2021) and projected (2022–2030) windows, Mann-Whitney U
comparisons across SDI thresholds, and Pearson/linear-regression correlation between SDI and
burden by continent.

The headline finding is a projected **global decline** in AD burden 2022–2030 (DALYs EAPC
−1.4375, deaths −1.7982, incidence −1.2718), consistent across sexes, but with sharp regional and
country-level divergence — some regions/countries (Andean Latin America, Cyprus, Serbia) show
rising projected burden while others (Eastern Europe, Bahrain, Armenia) show very large declines
— and a persistent finding that higher-SDI countries carry a higher absolute AD burden.

This ARA was compiled from the full open-access text (CC BY) of the 11-page PDF; no code
repository, supplementary tables, or supplementary figures were provided as input (see
`evidence/README.md` for what the paper cites but the ARA could not verify). The paper's own
numbers contain several internal inconsistencies (duplicate EAPC values for female incidence vs.
female deaths; abstract-vs-body-text rounding mismatches; ASR magnitudes that are difficult to
reconcile against a 100,000-population age-standardized-rate convention) which are preserved
verbatim per Rule 10 and flagged in `logic/solution/constraints.md`.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) |
| [concepts.md](logic/concepts.md) | 11 technical terms (ASR, EAPC, GAM, SDI, Mann-Whitney U, DALY, ASIR, ASDR, DisMod-MR 2.1, CODEm, ICD codes) |
| [experiments.md](logic/experiments.md) | 6 verification/analysis plans (E01–E06) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's 43-reference citation footprint |
| [solution/study_design.md](logic/solution/study_design.md) | GBD 2021 pipeline + GAM/EAPC/Mann-Whitney/correlation analysis as used |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, limitations, and internal-consistency caveats |

### Physical/Artifact Layer (`/src`, `/data`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment; GBD 2021/GHDx data source (no released code) |
| [data/dataset.md](data/dataset.md) | GBD 2021 provenance, access, variables used |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG (explicit + inferred nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 1 table + 4 figures (+ supplementary-material accounting) |
| [tables/table1.md](tables/table1.md) | Table 1 — EAPC of DALYs/deaths/incidence, 1990–2021 and 2022–2030, 24 locations |
| [figures/figure1.md](figures/figure1.md) | Fig 1 — projected 2022–2030 EAPC by region, ASIR/ASDR/DALY (sorted bar) |
| [figures/figure2.md](figures/figure2.md) | Fig 2 — projected 2030 ASR by region, ASIR/ASDR/DALY (bar + 95% UI) |
| [figures/figure3.md](figures/figure3.md) | Fig 3 — 1990–2030 ASR trend by SDI tier, ASIR/ASDR/DALY (line + band) |
| [figures/figure4.md](figures/figure4.md) | Fig 4 — 2030 sex-percentage split by region, ASIR/ASDR/DALY (stacked bar) |
