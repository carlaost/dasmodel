# Experiments (Analysis Plans)

> Abstract-only compile. These are declarative reconstructions of the analyses the abstract states
> were performed. Directional only — NO exact numbers (those live in claims.md/evidence). Because
> the full Methods section is unavailable, procedural detail (exact CDC WONDER query filters,
> standard population, Joinpoint settings) is marked "Not available from provided input (no full
> text)" where not stated in the abstract.

## E01: Temporal trend of EOAD mortality via Joinpoint regression
- **Verifies**: C01
- **Setup**:
  - Data: CDC WONDER US mortality, 2015-2024; EOAD = ICD-10-CM G30.0 as underlying cause of death.
  - Population: US resident population (denominator for AAMR per 1,000,000).
  - Tool: Joinpoint regression (specific software/version not specified in paper).
- **Procedure**:
  1. Extract annual EOAD death counts and AAMRs (per 1,000,000) from CDC WONDER for 2015-2024.
  2. Fit Joinpoint regression to the AAMR time series to estimate annual percent change (APC).
  3. Report endpoint AAMRs (2015, 2024) and the APC.
- **Metrics**: AAMR (deaths per 1,000,000/yr); APC (%/yr).
- **Expected outcome**:
  - EOAD AAMR increases monotonically over the study window.
  - APC is positive and statistically significant (rising trend).
- **Baselines**: The 2015 baseline AAMR is the internal reference; cross-check against C06 (LOAD).
- **Dependencies**: none

## E02: Sex disparity via rate ratio of AAMRs
- **Verifies**: C02
- **Setup**:
  - Data: CDC WONDER G30.0 deaths stratified by sex, 2015-2024.
  - Comparison: female AAMR vs male AAMR.
- **Procedure**:
  1. Extract sex-stratified EOAD death counts and AAMRs.
  2. Compute the female-to-male rate ratio (RR) with a 95% confidence interval.
  3. Report the female share of total EOAD deaths.
- **Metrics**: AAMR by sex; RR (female/male) with 95% CI; female percentage of deaths.
- **Expected outcome**:
  - Female AAMR exceeds male AAMR (RR > 1, CI excluding 1.0).
  - Females constitute the majority of EOAD deaths.
- **Baselines**: Male AAMR as reference group.
- **Dependencies**: none

## E03: Racial/ethnic disparity in EOAD mortality
- **Verifies**: C03
- **Setup**:
  - Data: CDC WONDER G30.0 deaths stratified by race/ethnicity (e.g., Non-Hispanic White, Non-Hispanic Black, Hispanic, others), 2015-2024.
- **Procedure**:
  1. Extract race/ethnicity-stratified EOAD AAMRs.
  2. Rank groups by AAMR; compute rate ratios relative to a reference group (reference not specified in abstract).
- **Metrics**: AAMR by race/ethnicity; rate ratios.
- **Expected outcome**:
  - Non-Hispanic White individuals show the highest AAMR among groups.
- **Baselines**: A designated reference racial/ethnic group (not specified in paper).
- **Dependencies**: none

## E04: Regional disparity in EOAD mortality
- **Verifies**: C04
- **Setup**:
  - Data: CDC WONDER G30.0 deaths stratified by US census region (Northeast, Midwest, South, West), 2015-2024.
- **Procedure**:
  1. Extract region-stratified EOAD AAMRs.
  2. Rank regions by AAMR; compute rate ratios relative to a reference region.
- **Metrics**: AAMR by census region; rate ratios.
- **Expected outcome**:
  - The Midwest shows the highest AAMR among regions.
- **Baselines**: A designated reference region (not specified in paper).
- **Dependencies**: none

## E05: Age-at-death distribution of EOAD decedents
- **Verifies**: C05
- **Setup**:
  - Data: CDC WONDER G30.0 deaths stratified by age band (e.g., <55, 55-64, 65-74, 75+), 2015-2024.
- **Procedure**:
  1. Extract death counts by age band.
  2. Compute the mean age at death and identify the modal age band.
- **Metrics**: Death counts by age band; mean age at death (years); modal band.
- **Expected outcome**:
  - The 65-74 band contains the greatest number of deaths; mean age at death is in the high 60s.
- **Baselines**: none (descriptive).
- **Dependencies**: none

## E06: Sensitivity analysis — EOAD (G30.0) vs late-onset AD (G30.1) trends
- **Verifies**: C06
- **Setup**:
  - Data: CDC WONDER G30.1 (LOAD) deaths/AAMRs, 2015-2024, extracted in parallel to G30.0.
  - Tool: Joinpoint regression on the LOAD series.
- **Procedure**:
  1. Extract LOAD (G30.1) annual AAMRs.
  2. Fit Joinpoint regression to obtain the LOAD APC.
  3. Compare the LOAD increase/APC against the EOAD increase/APC from E01.
- **Metrics**: LOAD AAMR and APC; qualitative comparison of EOAD vs LOAD increase.
- **Expected outcome**:
  - The LOAD increase is smaller than the EOAD increase over the same period.
- **Baselines**: EOAD (G30.0) trend from E01.
- **Dependencies**: E01
