# Experiments (Analysis Plans)

> Grounding: abstract-only. These are declarative, directional analysis plans reconstructed from the
> abstract's METHODS. They contain NO exact numbers (those live in [claims.md](claims.md); no
> separate evidence objects were extractable from the paywalled full text). Each plan is what would
> be run against CDC WONDER to verify the corresponding claim(s).

## E01: Temporal trend of AD-related mortality (joinpoint regression)
- **Verifies**: C01
- **Setup**:
  - Data: CDC WONDER Multiple Cause of Death database, 1999–2020
  - Case definition: ICD-10 F01, F03, G30, G31.1; decedents aged 45+
  - Metric: annual age-adjusted mortality rate (AAMR) per 100,000
  - Tool: joinpoint regression software (e.g. NCI Joinpoint) — specific settings not available (no full text)
- **Procedure**:
  1. Query CDC WONDER for annual AD-attributed deaths and population, 1999–2020, ages 45+.
  2. Compute annual AAMR (age-standardized).
  3. Fit joinpoint regression to the annual AAMR series; identify joinpoints.
  4. Derive Annual Percent Change per segment and the overall Average Annual Percent Change (AAPC).
- **Metrics**: AAMR per 100,000 per year; APC and AAPC (%) with significance.
- **Expected outcome**: A statistically significant increasing trend over the period.
- **Baselines**: Comparison is temporal (early vs late years); no external baseline.
- **Dependencies**: none

## E02: Overall AD mortality burden and rate
- **Verifies**: C02
- **Setup**:
  - Data: CDC WONDER, 1999–2020; ICD-10 F01, F03, G30, G31.1; ages 45+
  - Metric: total death count; overall AAMR per 100,000
- **Procedure**:
  1. Query total AD-attributed deaths across 1999–2020.
  2. Compute the pooled age-adjusted mortality rate.
- **Metrics**: aggregate death count; overall AAMR per 100,000.
- **Expected outcome**: A large multi-million death count with a positive overall AAMR.
- **Baselines**: none (descriptive total).
- **Dependencies**: none

## E03: Demographic disparity stratification (sex, race/ethnicity, age)
- **Verifies**: C03, C04, C05
- **Setup**:
  - Data: CDC WONDER, 1999–2020; same case definition
  - Strata: sex (female/male); race/ethnicity (non-Hispanic Black, non-Hispanic White, non-Hispanic
    American Indian, Hispanic, non-Hispanic Asian); age bands (through 85+)
  - Metric: AAMR per stratum (sex, race/ethnicity); CMR per age band
- **Procedure**:
  1. Stratify AD deaths and population by each demographic axis.
  2. Compute AAMR (sex, race/ethnicity) and CMR (age bands).
  3. Rank strata within each axis.
- **Metrics**: AAMR / CMR per 100,000 by stratum.
- **Expected outcome**: Female AAMR > male; non-Hispanic Black highest and non-Hispanic Asian lowest
  by race/ethnicity; oldest age band (85+) highest CMR.
- **Baselines**: within-axis comparison across strata.
- **Dependencies**: none

## E04: Geographic disparity stratification (urbanization, census region, state)
- **Verifies**: C06, C07, C08
- **Setup**:
  - Data: CDC WONDER, 1999–2020; same case definition
  - Strata: urbanization (rural/urban); census region (Northeast, Midwest, South, West); state
  - Metric: AAMR per 100,000 per geographic unit
- **Procedure**:
  1. Stratify AD deaths and population by urbanization, region, and state.
  2. Compute AAMR per unit.
  3. Rank units; identify extremes.
- **Metrics**: AAMR per 100,000 by geographic unit.
- **Expected outcome**: Rural > urban; Midwest highest and Northeast lowest region; wide state
  spread (some Southern states high, some Northeastern/Southeastern states lower).
- **Baselines**: within-axis comparison across geographic units.
- **Dependencies**: none

## E05: Reproduction / robustness of the CDC WONDER query
- **Verifies**: C02 (and underpins C01, C03–C08)
- **Setup**:
  - Data: CDC WONDER, 1999–2020; ICD-10 F01, F03, G30, G31.1; ages 45+
- **Procedure**:
  1. Independently re-run the CDC WONDER query with the exact code set, age filter, and years.
  2. Confirm death counts and rates match reported values within CDC's suppression rules.
  3. Test sensitivity to including/excluding non-G30 dementia codes (F01, F03, G31.1).
- **Metrics**: death count and AAMR under the primary and sensitivity code sets.
- **Expected outcome**: Primary reproduction matches; broader dementia codes inflate counts relative
  to G30-only.
- **Baselines**: G30-only case definition vs the full four-code set.
- **Dependencies**: E02

## E06: Sensitivity of the trend to age-standardization choice
- **Verifies**: C01
- **Setup**:
  - Data: CDC WONDER annual AD AAMR series, 1999–2020
- **Procedure**:
  1. Recompute annual AAMR under an alternative standard population if the primary standard differs.
  2. Re-fit joinpoint regression.
  3. Compare AAPC direction and significance.
- **Metrics**: AAPC (%) under alternative standardization.
- **Expected outcome**: The increasing trend is robust to the standardization choice.
- **Baselines**: primary standard population vs alternative.
- **Dependencies**: E01
