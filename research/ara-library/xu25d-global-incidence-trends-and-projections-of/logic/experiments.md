# Experiments (Analysis Plans)

> Grounding: abstract-only. These are declarative reconstructions of the analyses named in the abstract. Exact numerical results are kept in `claims.md`; unavailable procedural detail is marked explicitly.

## E01: Historical incidence trend analysis with APC
- **Verifies**: C01, C05
- **Setup**:
  - Data source: GBD 2021 database.
  - Scope: 204 countries and 21 global regions.
  - Outcome: Alzheimer disease and other dementia incidence cases and ASIR.
  - Model: age-period-cohort model.
  - Time span: historical incidence trend period named in the abstract.
- **Procedure**:
  1. Extract incidence case counts and ASIR for Alzheimer disease and other dementias from GBD 2021.
  2. Apply an APC model to estimate historical incidence trends.
  3. Compare global case counts and ASIR over time.
- **Metrics**: Case counts and ASIR per 100,000.
- **Expected outcome**:
  - Absolute global cases rise while global ASIR changes only slightly.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Stratified incidence analysis by SDI region and sex
- **Verifies**: C02, C03, C05
- **Setup**:
  - Data source: GBD 2021 database.
  - Stratification: SDI region and gender/sex categories as reported in the abstract.
  - Model: APC model for historical incidence trends.
- **Procedure**:
  1. Stratify incidence estimates by SDI region.
  2. Stratify incidence estimates by gender/sex across regions.
  3. Compare trend direction and relative incidence rates across strata.
- **Metrics**: Direction of ASIR change by SDI region; relative incidence rates by sex.
- **Expected outcome**:
  - ASIR trend direction differs across SDI regions, and women show higher incidence rates than men across regions.
- **Baselines**: Cross-region and cross-sex comparisons.
- **Dependencies**: E01

## E03: Future incidence forecasting with BAPC
- **Verifies**: C04, C05
- **Setup**:
  - Data source: GBD 2021 database.
  - Model: Bayesian age-period-cohort model.
  - Forecast horizon: future incidence period named in the abstract.
  - Outcome: projected global cases and ASIR.
- **Procedure**:
  1. Fit or parameterize the BAPC model using available historical incidence trends.
  2. Forecast future Alzheimer disease and other dementia incidence.
  3. Report projected global cases and ASIR for the target forecast year.
- **Metrics**: Projected case counts and ASIR per 100,000.
- **Expected outcome**:
  - The forecast indicates continued growth in global case burden and reports a future ASIR.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01
