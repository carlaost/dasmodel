---
title: "Epidemiological and sociodemographic transitions in the global burden and risk factors for Alzheimer's disease and other dementias: a secondary analysis of GBD 2021"
authors: [Changqing Xu, Chuanping Jiang, Xiaoxue Liu, Wenqi Shi, Jianjun Bai, Sumaira Mubarik, Fang Wang]
year: 2025
venue: "International Journal for Equity in Health"
doi: "10.1186/s12939-025-02530-2"
ara_version: "1.0"
domain: "GBD secondary analysis — global epidemiology of Alzheimer's disease and other dementias (ADOD), socio-demographic index (SDI) association, joinpoint/quantile-regression/restricted-cubic-spline trend analysis, and risk-factor attribution"
keywords: [Global burden of disease, Alzheimer's disease and other dementias, Socio-demographic index, Risk factors, Trends, joinpoint regression, quantile regression, restricted cubic spline]
claims_summary:
  - "Globally in 2021, ADOD caused 9.84 million incident cases, 1.95 million deaths, and 36.33 million DALYs; all three burden measures rose from 1990 to 2021 (global ASIR AAPC +0.06[0.05,0.07])."
  - "Only the high-middle SDI (AAPC +0.32) and middle SDI (AAPC +0.26) regions show rising ASIR 1990-2021; every other SDI region declined; East Asia's ASIR rank rose from 7th (1990) to 1st (2021) while high-income North America fell from 1st to 3rd."
  - "Among 204 countries, China/USA/India have the highest 2021 incident-case counts; 152/204 countries have ASIR>100 per 100,000, 85.5% of them with SDI>0.5."
  - "The SDI-ASIR association is non-linear and sex-differentiated: female ASIR accelerates above a threshold SDI, while male ASIR plateaus/declines above SDI~0.6."
  - "Low-middle SDI has the fastest-rising death rate (ASDR AAPC 0.41[0.31,0.52]) of any quintile; high SDI is the only region with a declining ASDR in its most recent (2016-2021) segment (EAPC -0.24[-0.32,-0.16])."
  - "High fasting plasma glucose (FPG) is the leading 2021 risk factor for ADOD deaths/DALYs (ASDR 3.73[0.15,11.84], DALYs 66.42[3.83,178.85] per 100,000), updating prior GBD-2016/2019 findings that ranked smoking/high-BMI as predominant; high-BMI and high-FPG burden rose 1990-2021 while smoking's fell."
  - "Risk-factor attribution is sharply sex-differentiated: smoking-ASDR is higher in males, FPG/BMI-ASDR much higher in females; High-income North America has the highest FPG-attributable burden (5.92 female / 5.34 male per 100,000)."
abstract: "The study aimed to analyze the long-term trends in the global burden of Alzheimer's disease and other dementias(ADOD) in different regions, and assess the association between socio-demographic index(SDI) and disease burden. We extracted data on the incidence, mortality, disability-adjusted life-years(DALYs), and age-standardized rates related to ADOD, as disease burden measures from 1990 to 2021. The joinpoint regression, quantile regression and restricted cubic splines were adopted to estimate the temporal trends and relationships with SDI. Risk factors for deaths and DALYs were also analyzed. Globally, 9.84 million cases of ADOD occurred in 2021, with 1.95 million ADOD-related deaths, causing 36.33 million DALYs. ADOD incidence, mortality and DALYs all increased from 1990 to 2021. Regional and sex variations persisted, with the fastest increase in age-standardized death rate in low-middle SDI quintiles, experienced the highest estimated annual percentage changes (0.41[0.31,0.52]). The incidence of ADOD increased more rapidly as SDI increased in areas that have historically shown lower incidence compared to other areas. In regions with higher mortality or DALYs burden, these indicators decreased relatively faster as SDI increased. High fasting plasma glucose was the main risk factor, particularly in high SDI region, with an increasing trend in attributable burden. The burden attributable to high BMI was increasing, whereas the burden associated with smoking steadily decreased. ADOD poses a significant and escalating challenge to healthcare sustainability, with persistent regional and gender disparities. By learning from successful ADOD management in certain nations, we can proactively reduce health burdens and bridge disparities between countries at various developmental levels."
---

# Epidemiological and Sociodemographic Transitions in the Global Burden and Risk Factors for Alzheimer's Disease and Other Dementias: A Secondary Analysis of GBD 2021

## Overview

This is a **GBD 2021 secondary statistical analysis** (not an interventional, experimental, or software study) of the global burden of Alzheimer's disease and other dementias (ADOD). It extracts GBD 2021 estimates of incidence, mortality, and disability-adjusted life-years (DALYs) — and their age-standardized rates (ASIR, ASDR, ASR-DALYs) — for 1990-2021, stratified by sex (both/male/female), the socio-demographic index (SDI, 5 quintiles), and 21 GBD regions (204 countries/territories). It applies three complementary statistical lenses: **joinpoint regression** (segmented log-linear trend estimation, yielding APC/EAPC/AAPC), **restricted cubic splines** (non-linear SDI-burden association across the 21-region, 1990-2021 panel), and **quantile regression** (SDI-burden association across the 204-country, 2021 cross-section, at the 5th/25th/50th/75th/95th percentiles). It separately decomposes ADOD deaths and DALYs attributable to three risk factors — smoking, high fasting plasma glucose (FPG), and high body mass index (BMI) — via the GBD comparative-risk-assessment (population attributable fraction) methodology. It has no released code, dataset, or registered clinical trial (per `sources.yaml`: `code: []`, `data: []`, `clinical_trials: []`; "No datasets were generated or analysed during the current study"). The paper's main text references a separate Supplementary Material file (Table S1-S3, Figure S1-S7) that was **not** provided as input to this ARA compilation; claims relying on those objects are explicitly flagged in `logic/claims.md` and `evidence/README.md`.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (global ADOD burden, economic cost, sex disparity) → gaps → key insight (nonlinear, direction-divergent SDI-burden association) → assumptions |
| [claims.md](logic/claims.md) | 13 falsifiable claims (C01-C13) with grounded number sources, including two flagged supplementary-material dependencies and one flagged unverifiable/possibly-inconsistent figure |
| [concepts.md](logic/concepts.md) | 10 technical terms/methods (GBD, ADOD, SDI, ASR, DALYs, joinpoint regression/APC/EAPC/AAPC, restricted cubic spline, quantile regression, PAF, the three risk factors) |
| [experiments.md](logic/experiments.md) | 5 declarative verification/analysis plans (E01-E05) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's 51-reference footprint (full RW blocks for the GBD data/methodology sources and the two prior-GBD-vintage dementia analyses this paper explicitly updates) |
| [solution/constraints.md](logic/solution/constraints.md) | Scope boundaries, assumptions, and the paper's self-reported limitations (plus one ARA-compilation-observed possible inconsistency) |
| [solution/statistical_methods.md](logic/solution/statistical_methods.md) | Full statistical methodology: GBD data source, age-standardization formula, joinpoint regression, restricted cubic splines, quantile regression, and PAF risk-factor decomposition formulas |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment: R 3.6.0, GBD 2021/GHDx data source; no code/dataset/trial released, no code stub (prose-only statistical methodology) |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: 1 root question, methodology decisions and experiments (E01-E05), and 3 dead ends (14 nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 2 numbered tables + 4 numbered figures (all filed, in order), plus accounted-for supplementary-material omissions |
| [tables/table1.md](tables/table1.md) | Incidence cases and ASIR, 1990/2010/2021, by sex/SDI region/super region/GBD region, with 1990-2021 ETPC |
| [tables/table2.md](tables/table2.md) | Joinpoint analysis (EAPC/AAPC) for ASIR, ASDR, ASR-DALYs, by SDI region, 1990-2021 |
| [figures/figure1.md](figures/figure1.md) | Joinpoint-segmented ASIR trend lines by sex and SDI region, 1989-2022, with printed per-segment APC legends |
| [figures/figure2.md](figures/figure2.md) | 204-country scatter of SDI vs. ASIR/ASDR/ASR-DALYs by sex, with quantile-regression fits |
| [figures/figure3.md](figures/figure3.md) | Sex-specific ASDR attributable to smoking/high BMI/high FPG, by SDI region, 1990-2021 line trends |
| [figures/figure4.md](figures/figure4.md) | Full exact-value heatmap: sex-specific ASDR attributable to smoking/high BMI/high FPG, by global/5 SDI quintiles/21 regions, 1990 and 2021 |
