# Study Design — GBD 2021 extraction + GAM projection + EAPC/Mann-Whitney/correlation analysis

This paper does not modify GBD's underlying estimation pipeline; it (a) extracts pre-computed GBD
2021 ASRs, (b) applies a Generalized Additive Model (GAM) to forecast those ASRs to 2030, (c)
computes EAPC over both the historical (1990–2021) and projected (2022–2030) windows, and (d) runs
group comparisons (Mann-Whitney U) and correlations (Pearson/linear regression) against SDI. This
file documents the pipeline as the paper describes it (Methods, pp.2–3).

## 1. Scope and framing
- **Design**: Secondary analysis of GBD 2021 estimates (1990–2021) plus the authors' own GAM-based
  forecast (2022–2030); observational, descriptive + predictive epidemiology.
- **Coverage**: GBD 2021 covers 371 diseases/injuries and 87 risk factors across 204
  countries/territories. This study extracts Alzheimer's disease incidence, death, and DALY rates
  globally, and stratified by sex, SDI (5 categories + 2 thresholds), 18 GBD regions (per Table 1),
  and individual country.
- **Time windows**: Historical 1990–2021 (from GBD estimates); projected 2022–2030 (from the GAM
  forecast). EAPC is reported separately for each window.
- **Outputs**: Age-standardized incidence rate (ASIR), age-standardized death rate (ASDR), and
  age-standardized DALY rate, each with 95% CI/UI; EAPC (%) with 95% CI.

## 2. Data source and case definition
- **Source**: Global Health Data Exchange (GHDx) platform's GBD tool (GBD 2021 cycle).
- **AD-specific inputs**: both prevalence and incidence data; incidence data newly added in GBD
  2021 (81 data points, 60 locations), supported by excess-mortality data from cohort studies
  comparing dementia vs. non-dementia death risk. USA claims data were excluded from dementia
  modeling "due to their disproportionate weight on global prevalence and incidence patterns
  relative to other input data." Data were adjusted using matched datasets to adhere to the
  reference case definition.
- **Case definition**: ICD-9 290.0–290.9 (senile dementia 290.0, presenile dementia 290.1,
  unspecified senile dementia 290.9); ICD-10 G30.0–G30.9 (AD early onset G30.0, late onset G30.1,
  other G30.8, unspecified G30.9).
- **Upstream modeling tools**: CODEm (Cause of Death Ensemble model) and DisMod-MR 2.1 (Bayesian
  meta-regression), both run by IHME, not by this paper's authors — used "to address data gaps and
  maintain internal consistency across locations and time periods."
- **Ethics**: publicly available data; no ethical approval required (stated twice, Methods p.2 and
  Ethics statement p.4).

## 3. Age-standardization
- ASR = Σᵢ wᵢrᵢ across age groups i = 1…n, where wᵢ = Pᵢ / Σᵢ Pᵢ (Pᵢ = standard population of age
  group i) and rᵢ is the age-group-specific rate (incidence, death, or DALY).
- Applied across all age groups for incidence, mortality, and DALYs.

## 4. GAM-based projection (2022–2030)
- Model form: y = β₀ + s(x₁) + s(x₂) + … + s(xₙ) + ε, where y is the predicted ASR, s(x) is a
  smooth function of a predictor (calendar year, median age are named), β₀ the intercept, ε the
  residual.
- Purpose: "flexibly model disease trends over time, with smooth functions adjusting to variations
  in predictor variables."
- Applied to the 1990–2021 GBD ASR series to produce 2022–2030 forecasts, separately for each
  stratum (global, sex, SDI category, region, country).

## 5. EAPC computation
- EAPC = 100 × [(ASR_end / ASR_start)^(1/t) − 1], computed for 1990–2021 and, separately, for the
  GAM-projected 2022–2030 window, with a reported 95% CI. A change is significant if the CI
  excludes zero.

## 6. Group comparisons and correlation analysis
- **Mann-Whitney U test**: U = n₁n₂ + n₁(n₁+1)/2 − R₁; used to compare 2030 ASIR/ASDR/DALY ASR
  between SDI groups — at the ≥0.8/<0.8 threshold, the ≥0.7/<0.7 threshold, and across the five
  SDI categories (low, low-middle, middle, high-middle, high).
- **SDI–burden correlation**: "Linear regression and Pearson correlation" of SDI against
  ASIR/ASDR/DALY ASR, computed separately within each of five continents (Africa, America, Asia,
  Europe, Oceania), "while considering potential confounders like gender and regional economic
  status" (no confounder-adjusted numbers are reported in the main text).

## 7. What is original to THIS paper vs. inherited from GBD
- Inherited from IHME/GBD 2021: all base incidence/death/DALY estimation (CODEm, DisMod-MR 2.1,
  case definitions, draw-based UIs).
- Original to this paper: the GAM-based 2022–2030 projection, EAPC computation over both windows
  at every stratification level, the SDI-threshold Mann-Whitney comparisons, and the per-continent
  SDI–burden correlation/regression analysis.
