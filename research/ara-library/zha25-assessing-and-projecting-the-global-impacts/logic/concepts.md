# Concepts

Genuine technical terms used by the paper, defined as the source uses them.

## Age-Standardized Rate (ASR)
- **Notation**: ASR; specifically ASIR (incidence), ASDR (death), and age-standardized DALY rate
- **Definition**: A weighted average of age-group-specific rates, using the standard population as
  the weighting factor: ASR = Σᵢ wᵢrᵢ (i = 1…n age groups), where wᵢ is the standard-population
  weight for age group i and rᵢ is that group's rate (incidence, death, or DALY). The weight wᵢ
  itself is Pᵢ / Σᵢ Pᵢ, where Pᵢ is the population of age group i in the standard population.
- **Boundary conditions**: Computed across all age groups for incidence, mortality, and DALYs;
  removes confounding by differing age structures across locations/time.
- **Related concepts**: DALY, EAPC, standard population

## Disability-Adjusted Life Year (DALY)
- **Notation**: DALY
- **Definition**: A summary disease-burden measure; the paper "combined incidence data with
  disability weights to calculate DALYs, providing a comprehensive measure of the disease burden."
- **Boundary conditions**: Reported as age-standardized rates (not counts) throughout this paper's
  main results; sourced pre-computed from GBD 2021, not independently calculated by the authors.
- **Related concepts**: ASR, EAPC, GBD

## Estimated Annual Percentage Change (EAPC)
- **Notation**: EAPC
- **Definition**: A summary trend statistic computed over a period from a start ASR to an end ASR:
  EAPC = 100 × [(ASR_end / ASR_start)^(1/t) − 1], where t is the number of years in the period.
  Positive values signify an increase; negative values indicate a decrease.
- **Boundary conditions**: Computed separately for 1990–2021 (historical, from observed GBD
  estimates) and 2022–2030 (projected, from GAM-forecast ASRs). Significance is assessed via
  whether the reported 95% CI excludes zero.
- **Related concepts**: ASR, GAM, statistical significance

## Generalized Additive Model (GAM)
- **Notation**: GAM
- **Definition**: The forecasting model used to project 2022–2030 ASRs from the 1990–2021 GBD
  series. Represented as y = β₀ + s(x₁) + s(x₂) + … + s(xₙ) + ε, where y is the predicted ASR, β₀
  is the intercept, s(x) is a smooth function capturing non-linear relationships with predictor
  variables (e.g., calendar year, median age), and ε is the residual/unexplained-variation term.
- **Boundary conditions**: Used to flexibly model non-linear time trends; applied to pre-computed
  GBD ASRs, not to raw case data.
- **Related concepts**: EAPC, ASR, smooth function

## Socio-Demographic Index (SDI)
- **Notation**: SDI (0–1 scale)
- **Definition**: A composite GBD indicator combining per-capita income, education level, and
  fertility rate; higher scores indicate higher income, more education, and lower fertility.
  Countries are classified into five development-level groups by SDI: high (≥0.80),
  upper-middle/high-middle (0.70–0.79), middle (0.60–0.69), lower-middle/low-middle (0.50–0.59),
  and low (<0.50).
- **Boundary conditions**: Used both as a five-category grouping variable and as a continuous
  predictor (linear regression/Pearson correlation) against ASIR/ASDR/DALY ASR, per continent, in
  §3.5.
- **Related concepts**: Mann-Whitney U test, Pearson correlation, linear regression

## Mann-Whitney U test
- **Notation**: U
- **Definition**: A non-parametric test for comparing two independent samples, used here for
  intergroup comparisons of AD burden across the five continents. Formula given as
  U = n₁n₂ + n₁(n₁+1)/2 − R₁, where n₁, n₂ are the two groups' sample sizes and R₁ is the sum of
  ranks for the first group.
- **Boundary conditions**: Used for the SDI-threshold group comparisons (≥0.8 vs <0.8; ≥0.7 vs
  <0.7; five-category breakdown) in §3.5; exact U statistics and p-values for these comparisons
  are deferred to Supplementary Figures 2–4 (not part of the provided input).
- **Related concepts**: SDI, statistical significance

## DisMod-MR 2.1
- **Notation**: DisMod-MR 2.1
- **Definition**: A Bayesian meta-regression tool used within the GBD pipeline (alongside CODEm)
  "to address data gaps and maintain internal consistency across locations and time periods,"
  using covariate data and geographical patterns to produce mortality/burden estimates even where
  direct data are limited.
- **Boundary conditions**: Upstream IHME methodology; not run or modified by this paper's authors.
- **Related concepts**: CODEm, GBD

## Cause of Death Ensemble model (CODEm)
- **Notation**: CODEm
- **Definition**: The GBD ensemble-modeling tool for cause-of-death estimation, used alongside
  DisMod-MR 2.1 to produce internally consistent mortality estimates across locations/time.
- **Boundary conditions**: Upstream IHME methodology.
- **Related concepts**: DisMod-MR 2.1, GBD

## Age-standardized Incidence Rate (ASIR) / Age-standardized Death Rate (ASDR)
- **Notation**: ASIR, ASDR
- **Definition**: The incidence- and death-specific instances of ASR (see above), used throughout
  as the paper's shorthand for the two non-DALY burden measures alongside "age-standardized DALY
  rate."
- **Boundary conditions**: Defined identically to ASR §; distinguished only by which underlying
  measure (incidence vs. death) is standardized.
- **Related concepts**: ASR, DALY

## ICD case-definition codes for Alzheimer's disease
- **Notation**: ICD-9 290.0–290.9; ICD-10 G30.0–G30.9
- **Definition**: The diagnostic coding ranges used to identify AD cases in GBD input data.
  ICD-9: senile dementia (290.0), presenile dementia (290.1), unspecified senile dementia (290.9).
  ICD-10: AD with early onset (G30.0), AD with late onset (G30.1), other AD (G30.8), AD unspecified
  (G30.9).
- **Boundary conditions**: Applied "across all age groups" as the reference case definition
  underlying GBD's AD estimates; the paper notes diagnostic-criteria/healthcare-access variation
  across countries can bias case ascertainment (Discussion, p.9, limitation).
- **Related concepts**: GBD case definition, DisMod-MR 2.1

## Global Burden of Disease (GBD) study
- **Notation**: GBD 2021 (via the GHDx platform)
- **Definition**: IHME's standardized program estimating incidence, prevalence, mortality, and
  DALYs for 371 diseases/injuries and 87 risk factors across 204 countries/territories. GBD 2021
  newly incorporated AD incidence data (81 data points, 60 locations) and excluded USA claims data
  from dementia modeling to avoid disproportionate weighting.
- **Boundary conditions**: Sole data source for this paper; publicly available, so the study states
  no ethical approval was required.
- **Related concepts**: DisMod-MR 2.1, CODEm, SDI, ASR
