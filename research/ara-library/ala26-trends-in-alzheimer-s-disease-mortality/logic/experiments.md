# Experiments (Analysis Plans)

> Grounding: abstract-only. These are declarative reconstructions of the analyses the abstract
> implies (CDC WONDER query + AAMR computation + Joinpoint trend detection, stratified). They are
> directional only — no exact numbers (those live in `logic/claims.md` and would live in `evidence/`
> if full text were available). Procedural detail beyond the abstract is reconstructed from standard
> CDC WONDER / Joinpoint practice and marked as such.

## E01: Case ascertainment and counting from CDC WONDER
- **Verifies**: C01
- **Setup**:
  - Data source: CDC WONDER Multiple Cause of Death database (US death certificates), 1999–2020
  - Population: US resident deaths, age ≥75
  - Selection: underlying cause of death = Alzheimer's disease; comorbidity subset = deaths also involving metabolic syndrome-related conditions (multiple-cause fields)
  - System: analytical — public web query (exact ICD-10 code sets Not available from provided input; no full text)
- **Procedure**:
  1. Query CDC WONDER for deaths with AD as underlying cause, ages ≥75, years 1999–2020.
  2. Within that set, identify deaths also coded with metabolic syndrome-related conditions.
  3. Tabulate total and comorbidity-subset death counts over the full window.
- **Metrics**: Death counts (integer) for total AD-underlying-cause deaths and the metabolic-syndrome-related subset.
- **Expected outcome**:
  - The comorbidity subset is a minority (roughly one-fifth) of total AD-underlying-cause deaths in the age group.
- **Baselines**: none (descriptive counting)
- **Dependencies**: none

## E02: Overall temporal AAMR trend via Joinpoint regression
- **Verifies**: C02, C05
- **Setup**:
  - Data source: as E01
  - Rates: age-adjusted mortality rate per 100,000, computed per calendar year 1999–2020
  - System: Joinpoint Regression Program (segmented log-linear model); standard population Not available from provided input
- **Procedure**:
  1. Compute annual AAMR (per 100,000) for the AD+metabolic-syndrome cohort.
  2. Fit Joinpoint regression to the annual AAMR series to detect trend segments and inflection points.
  3. Characterize the overall direction and any early-period peak.
- **Metrics**: Annual AAMR (per 100,000); APC/AAPC per segment; joinpoint year(s).
- **Expected outcome**:
  - AAMR increases substantially from the 1999 endpoint to the 2020 endpoint.
  - A sharp peak/inflection appears in the early-to-mid 2000s.
- **Baselines**: comparison of endpoint years (1999 vs 2020)
- **Dependencies**: E01

## E03: Demographic stratification (sex and race/ethnicity)
- **Verifies**: C03, C04, C05
- **Setup**:
  - Data source: as E01, stratified by sex and by race/ethnicity
  - Rates: AAMR per 100,000 within each stratum
  - System: CDC WONDER stratified query + Joinpoint per stratum
- **Procedure**:
  1. Compute AAMR by sex and by race/ethnicity group.
  2. Compare sex-specific AAMRs; rank racial/ethnic groups by AAMR.
  3. Run Joinpoint per group to assess whether the early-period peak is shared.
- **Metrics**: Stratum-specific AAMR (per 100,000); relative ordering across strata.
- **Expected outcome**:
  - Female AAMR exceeds male AAMR consistently.
  - Non-Hispanic African Americans have the highest AAMR among racial groups.
  - The early-to-mid-2000s peak is present across all racial groups.
- **Baselines**: cross-group comparison (male vs female; each racial group vs the others)
- **Dependencies**: E01, E02

## E04: Geographic stratification (state-level)
- **Verifies**: C06
- **Setup**:
  - Data source: as E01, stratified by state (and region)
  - Rates: state-level AAMR per 100,000
  - System: CDC WONDER state-level query; percentile ranking of states
- **Procedure**:
  1. Compute AAMR for each US state.
  2. Rank states and identify high- and low-percentile extremes.
- **Metrics**: State-level AAMR (per 100,000); percentile rank.
- **Expected outcome**:
  - Wide between-state dispersion in AAMR; a high-rate state (e.g., Mississippi) sits near the top decile and a low-rate state (e.g., Massachusetts) near the bottom decile.
- **Baselines**: inter-state comparison against the national distribution
- **Dependencies**: E01

## E05: Place-of-death stratification
- **Verifies**: C02 (as a supporting stratum of the overall trend)
- **Setup**:
  - Data source: as E01, stratified by place of death (medical facility, nursing home/long-term care, hospice, home, etc.)
  - Rates: AAMR / distribution across place-of-death categories over time
  - System: CDC WONDER place-of-death query + Joinpoint
- **Procedure**:
  1. Compute AAMR or death distribution by place-of-death category per year.
  2. Assess trends across categories with Joinpoint regression.
- **Metrics**: Category-specific AAMR / proportion; temporal trend per category.
- **Expected outcome**:
  - Place-of-death composition and/or category-specific rates shift over the study window. (Direction Not available from provided input — no full text; abstract lists place-of-death only as an analyzed variable.)
- **Baselines**: cross-category comparison over time
- **Dependencies**: E01, E02
