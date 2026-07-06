# Experiments / Analyses

> Grounding: abstract-only. These are declarative analysis blocks corresponding to analyses reported in the abstract. Exact numerical results are intentionally omitted here and captured in `logic/claims.md`.

## E01: Estimate prevalence trend from GBD 2021
- **Verifies**: C01
- **Setup**:
  - Data source: GBD 2021 disease-burden data for AD and other dementias during 1990-2021.
  - Outcome: Age-standardized prevalence per population.
  - System: Not available from provided input.
- **Procedure**:
  1. Extract prevalence data for AD and other dementias from GBD 2021.
  2. Age-standardize prevalence estimates.
  3. Estimate the average annual percentage change over the study window.
- **Metrics**: Age-standardized prevalence and AAPC.
- **Expected outcome**:
  - Global age-standardized prevalence increases over the study window.
- **Baselines**: 1990 prevalence compared with 2021 prevalence.
- **Dependencies**: none

## E02: Estimate mortality trend from GBD 2021
- **Verifies**: C02
- **Setup**:
  - Data source: GBD 2021 disease-burden data for AD and other dementias during 1990-2021.
  - Outcome: Age-standardized mortality.
  - System: Not available from provided input.
- **Procedure**:
  1. Extract mortality data for AD and other dementias from GBD 2021.
  2. Age-standardize mortality estimates.
  3. Estimate the average annual percentage change over the study window.
- **Metrics**: Age-standardized mortality and AAPC.
- **Expected outcome**:
  - Age-standardized mortality is stable over the study window.
- **Baselines**: Mortality trend over 1990-2021.
- **Dependencies**: none

## E03: Estimate DALY trend and risk-factor ranking
- **Verifies**: C03, C05
- **Setup**:
  - Data source: GBD 2021 disease-burden and risk-factor data for AD and other dementias during 1990-2021.
  - Outcomes: Age-standardized DALYs; DALY risk-factor ranking.
  - System: Not available from provided input.
- **Procedure**:
  1. Extract DALY estimates for AD and other dementias from GBD 2021.
  2. Age-standardize DALY estimates and estimate the average annual percentage change.
  3. Rank risk factors contributing to DALYs over the study period.
- **Metrics**: Age-standardized DALYs, AAPC, and ranked DALY risk factors.
- **Expected outcome**:
  - Age-standardized DALYs increase slightly.
  - High fasting plasma glucose ranks highest among DALY risk factors.
- **Baselines**: 1990 DALYs compared with 2021 DALYs; risk-factor ranking within the GBD attribution framework.
- **Dependencies**: none

## E04: Stratify burden by age, SDI, and geography
- **Verifies**: C04
- **Setup**:
  - Data source: GBD 2021 disease-burden data for AD and other dementias.
  - Stratifiers: Age group, SDI grouping, region/country.
  - System: Not available from provided input.
- **Procedure**:
  1. Stratify prevalence, mortality, and DALYs by age group.
  2. Compare burden patterns across SDI groupings and regional/country examples.
  3. Identify the strata with the highest reported burden for each outcome.
- **Metrics**: Stratified prevalence, mortality, and DALY burden patterns.
- **Expected outcome**:
  - Highest prevalence and highest mortality/DALY patterns concentrate in the age group and SDI/geographic strata named in the abstract.
- **Baselines**: Comparisons across age groups, SDI groupings, and regional/country examples.
- **Dependencies**: E01, E02, E03
