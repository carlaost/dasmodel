# Experiments (Analysis Plans)

> Grounding: abstract-only, directional only. These reconstruct the paper's analytical procedures from the abstract. Exact numerical results are kept in `claims.md`; no exact values are repeated here except source time windows needed to define the setup.

## E01: Descriptive GBD burden trend analysis
- **Verifies**: C01, C02
- **Setup**:
  - Data source: Global Burden of Disease database.
  - Geography: global, regional, and national data.
  - Disease category: Alzheimer's disease and other dementias.
  - Measures: incidence, prevalence, and DALYs.
  - Stratification: age and gender where available from the paper's analysis.
- **Procedure**:
  1. Extract GBD estimates for the disease category across the retrospective period.
  2. Summarize incidence, prevalence, and DALYs globally and by region/nation.
  3. Compare sex- and age-stratified prevalence patterns, especially older female versus male burden.
- **Metrics**: Incidence, prevalence, DALYs, age/sex/geographic strata.
- **Expected outcome**:
  - Global burden increases over time; East Asia is the highest-burden region among regions named in the abstract; older females show a higher prevalence increase than males.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Joinpoint regression trend-change detection
- **Verifies**: C03
- **Setup**:
  - Input series: burden metrics from the GBD data.
  - Model: Joinpoint regression analysis.
  - Metric-specific settings: Not available from provided input.
- **Procedure**:
  1. Fit Joinpoint regression to temporal burden series.
  2. Identify significant change points in the trends.
  3. Characterize whether trend slopes accelerate after detected change points.
- **Metrics**: Detected Joinpoint years, direction of trend changes, trend acceleration.
- **Expected outcome**:
  - Multiple historical change points are identified, with acceleration after later change points.
- **Baselines**: A no-change-point or single-slope time trend; exact comparison not available from provided input.
- **Dependencies**: E01

## E03: Age-period-cohort risk analysis
- **Verifies**: C04
- **Setup**:
  - Factors: age, period, and birth cohort.
  - Outcome: risk of AD and other dementias.
  - Age, period, and cohort binning: Not available from provided input.
- **Procedure**:
  1. Model age, period, and birth-cohort effects on disease risk.
  2. Inspect age-specific risk patterns.
  3. Identify the age range where risk rises sharply.
- **Metrics**: Direction and relative strength of age, period, and cohort effects.
- **Expected outcome**:
  - Age emerges as a significant risk factor and risk rises sharply in older ages.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E04: DALY-driver decomposition across SDI quintiles
- **Verifies**: C01, C05
- **Setup**:
  - Outcome: DALYs.
  - Drivers: aging, population growth, and epidemiological changes.
  - Stratification: Socio-demographic Index quintiles, region, and gender.
- **Procedure**:
  1. Decompose DALY change into aging, population growth, and epidemiological-change components.
  2. Compare driver contributions across SDI quintiles.
  3. Assess whether epidemiological changes are globally minor but heterogeneous by region and gender.
- **Metrics**: Directional contribution of aging, population growth, and epidemiological changes to DALY burden.
- **Expected outcome**:
  - Aging dominates in high-SDI regions; demographic expansion dominates in low-SDI regions; epidemiological changes have globally smaller but heterogeneous effects.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E03

## E05: Bayesian age-period-cohort forecast to 2040
- **Verifies**: C05
- **Setup**:
  - Model: Bayesian age-period-cohort modeling.
  - Forecast horizon: through 2040.
  - Target outcomes: age-standardized incidence and prevalence rates.
  - Prior specification and uncertainty reporting: Not available from provided input.
- **Procedure**:
  1. Fit a Bayesian age-period-cohort model to historical GBD burden series.
  2. Project age-standardized incidence and prevalence rates through the forecast horizon.
  3. Interpret projected growth by SDI-related demographic drivers.
- **Metrics**: Forecasted age-standardized incidence and prevalence rates, growth direction, driver attribution.
- **Expected outcome**:
  - Forecasts indicate sustained growth through 2040, with different dominant demographic drivers by SDI level.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E03, E04
