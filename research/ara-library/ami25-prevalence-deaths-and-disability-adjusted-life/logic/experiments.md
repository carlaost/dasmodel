# Experiments (verification / analysis plans)

This is a secondary descriptive-epidemiology study: its "experiments" are extraction-and-analysis
procedures over GBD 2021 estimates, not primary data collection or interventions. Plans below are
declarative and directional only — all exact numbers live in `evidence/`.

## E01: Regional burden and 1990→2021 trend
- **Verifies**: C01, C02
- **Setup**:
  - Data: GBD 2021 estimates for "Alzheimer's disease and other dementias" (cause), MENA
    ("North Africa and Middle East") region, years 1990 and 2021, both sexes, all ages.
  - System: IHME GHDx GBD Results Tool / GBD Compare; analysis in R (v3.5.2).
  - Measures: prevalence, deaths, DALYs — as counts and age-standardised rates per 100,000.
- **Procedure**:
  1. Extract 2021 counts and ASRs (with 1000-draw 95% UIs) for the regional aggregate.
  2. Extract 1990 ASRs and compute percentage change 1990→2021 for each measure.
  3. Flag a change as significant if its 95% UI excludes zero.
- **Metrics**: ASR per 100,000; percentage change (%); 95% UI bounds.
- **Expected outcome**:
  - Regional prevalence, death, and DALY ASRs all decreased from 1990 to 2021.
  - Each decrease is statistically significant (UI excludes 0).
  - The death-rate decrease is larger than the prevalence decrease.
- **Baselines**: 1990 MENA rates; prior GBD 2019 MENA analysis (ref 6, directional comparison only).
- **Dependencies**: none

## E02: Country-level ranking and per-country trend
- **Verifies**: C03, C04
- **Setup**: Same source; unit = each of the 21 MENA countries; years 1990, 2021; all ages, both sexes.
- **Procedure**:
  1. Extract each country's 2021 prevalence/death/DALY ASR with 95% UI.
  2. Rank countries to identify highest and lowest for each measure.
  3. Compute per-country 1990→2021 percentage change; count countries with a significant decrease.
- **Metrics**: per-country ASR; rank; percentage change with 95% UI; count of significant declines.
- **Expected outcome**:
  - Prevalence highest in Lebanon, lowest in UAE; a modest inter-country spread.
  - A majority (but not all) of countries show a significant prevalence decline; fewer show
    significant death- or DALY-rate declines.
  - Gulf/high-income states show the largest declines.
- **Baselines**: regional aggregate (E01); each country's own 1990 value.
- **Dependencies**: E01

## E03: Sex comparison
- **Verifies**: C05
- **Setup**: Same source; stratify by sex (male, female); MENA aggregate; all ages and by age band; 2021.
- **Procedure**:
  1. Extract male and female counts and ASRs for prevalence, deaths, DALYs.
  2. Compare female vs male point estimates within each age band.
  3. Assess whether the female–male difference is statistically significant (UI overlap).
- **Metrics**: sex-specific counts and ASRs; direction of female–male difference; significance.
- **Expected outcome**:
  - Female estimates exceed male in every measure and age band.
  - The female–male difference is NOT statistically significant (overlapping wide UIs).
- **Baselines**: male stratum as reference.
- **Dependencies**: E01

## E04: Age-pattern analysis
- **Verifies**: C06
- **Setup**: Same source; stratify into five-year age bands (40–44 … 95+); MENA aggregate; both sexes; 2021.
- **Procedure**:
  1. Extract counts and rates per age band for prevalence, deaths, DALYs.
  2. Locate the age band at which counts peak.
  3. Assess whether age-standardised rates rise monotonically with age.
- **Metrics**: per-age-band counts and rates; location of count peak; monotonicity of rate.
- **Expected outcome**:
  - Counts rise to a peak (mid-80s) then decline; rates rise monotonically with age in both sexes.
  - Prevalence and DALY counts peak one band earlier (80–84) than deaths (85–89).
- **Baselines**: youngest modelled band (40–44).
- **Dependencies**: E01

## E05: MENA-vs-global DALY ratio by age and sex, over time
- **Verifies**: C07
- **Setup**: GBD 2021 DALY rates for MENA and for Global, by age band and sex, for 1990 and 2021.
- **Procedure**:
  1. Compute the MENA/Global DALY-rate ratio for each age band and sex, for 1990 and 2021.
  2. Check whether all ratios are ≥1 (MENA ≥ global).
  3. Compare 2021 ratios against 1990 within each stratum to assess the time trend.
- **Metrics**: MENA/Global DALY ratio; per-stratum 1990-vs-2021 difference; location of the maximum ratio.
- **Expected outcome**:
  - Ratio ≥1 across all age/sex strata; maximum ratio in older working-age males.
  - 2021 ratio ≤ 1990 ratio in every stratum (a decreasing, converging trend).
- **Baselines**: global DALY rate (ratio denominator); 1990 ratio.
- **Dependencies**: E01

## E06: SDI relationship (expected vs observed)
- **Verifies**: C08
- **Setup**: Per-country age-standardised DALY rate vs SDI, 2021 (with year-trajectory points);
  smoothing-spline fit of expected rate across all GBD locations.
- **Procedure**:
  1. Plot each country's observed ASR DALY against its SDI.
  2. Fit a smoothing-spline "expected" curve using SDI and disease rates from all locations.
  3. Classify each country as above or below its SDI-expected value.
- **Metrics**: observed ASR DALY; SDI; residual (observed − expected).
- **Expected outcome**:
  - The expected curve is non-monotonic (falls, slight rise, falls) rather than a clean gradient.
  - Some countries lie above the expected line (higher burden than SDI predicts) and some below;
    no clear overall SDI trend.
- **Baselines**: SDI-expected smoothing-spline curve.
- **Dependencies**: E01
