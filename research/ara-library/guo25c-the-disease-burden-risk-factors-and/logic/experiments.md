# Experiments and Analyses

> Grounding: abstract-only. These are declarative reconstructions of analyses named in the abstract, not runnable scripts. Exact numerical results are intentionally omitted here and kept in claims where directly quoted.

## E01: Quantify 1990-2021 ADOD burden count changes in Asia
- **Verifies**: C01
- **Setup**:
  - Model: Not available from provided input.
  - Hardware: Not available from provided input.
  - Dataset: Global Burden of Disease Study 2021 ADOD estimates for Asia from 1990 to 2021.
  - System: Secondary epidemiological analysis; software not available from provided input.
- **Procedure**:
  1. Extract ADOD deaths, DALYs, incidence, and prevalence counts for Asia across the study period.
  2. Compare endpoint counts across the 1990-2021 period.
  3. Report directional and percentage change by metric.
- **Metrics**: Deaths, DALYs, incidence, and prevalence counts.
- **Expected outcome**:
  - ADOD burden counts increase across all named metrics.
- **Baselines**: 1990 burden counts.
- **Dependencies**: none

## E02: Analyze age-standardized and country-level burden trends
- **Verifies**: C02, C03, C04
- **Setup**:
  - Model: Joinpoint regression for trend assessment; exact settings not available from provided input.
  - Hardware: Not available from provided input.
  - Dataset: GBD 2021 ADOD estimates for Asian countries and sex strata from 1990 to 2021.
  - System: Not available from provided input.
- **Procedure**:
  1. Compute or extract age-standardized rates for incidence, prevalence, death, and DALYs by sex.
  2. Evaluate temporal trends during 1990-2021 with Joinpoint regression and AAPCs.
  3. Rank countries by changes in selected burden counts and by 2021 ASMR.
- **Metrics**: ASRs for incidence, prevalence, death, and DALYs; AAPCs; country-level changes; ASMR.
- **Expected outcome**:
  - Age-standardized rates increase over time and are higher among females.
  - Qatar and the United Arab Emirates appear at the top of selected burden-count change rankings.
  - Afghanistan and China appear at the top of the 2021 ASMR ranking.
- **Baselines**: Earlier years in the 1990-2021 GBD series and other Asian countries in ranking analyses.
- **Dependencies**: E01

## E03: Assess ADOD risk-factor patterns
- **Verifies**: C05
- **Setup**:
  - Model: GBD risk-factor attribution or comparative risk framework; exact method not available from provided input.
  - Hardware: Not available from provided input.
  - Dataset: GBD 2021 ADOD risk-factor estimates for Asia.
  - System: Not available from provided input.
- **Procedure**:
  1. Extract risk-factor contributions for ADOD onset or burden.
  2. Compare the relative importance of high fasting blood glucose, high BMI, and smoking.
  3. Stratify risk-factor patterns by sex where available.
- **Metrics**: Risk-factor ranking and sex-stratified susceptibility or effect patterns.
- **Expected outcome**:
  - High fasting blood glucose ranks as the top risk factor.
  - High BMI is more prominent among females and smoking is more prominent among males.
- **Baselines**: Other available ADOD risk factors in the GBD estimates.
- **Dependencies**: none

## E04: Forecast future ADOD burden in Asia
- **Verifies**: C06
- **Setup**:
  - Model: ARIMA prediction model; order and diagnostics not available from provided input.
  - Hardware: Not available from provided input.
  - Dataset: Historical GBD 2021 ADOD time series for Asia.
  - System: Not available from provided input.
- **Procedure**:
  1. Fit an ARIMA model to historical ADOD burden trends.
  2. Forecast ADOD burden over the next 30 years.
  3. Assess whether the forecast trajectory is upward, flat, or downward.
- **Metrics**: Forecast direction for ADOD disease burden over the future horizon.
- **Expected outcome**:
  - The forecasted ADOD disease burden continues upward.
- **Baselines**: Historical trend extrapolation and the fitted ARIMA baseline.
- **Dependencies**: E01, E02
