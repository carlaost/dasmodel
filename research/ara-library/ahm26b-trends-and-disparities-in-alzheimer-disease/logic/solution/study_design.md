# Study Design

> Grounding: abstract-only. This reflects the design as stated in the abstract METHODS. Steps not
> explicitly described (software versions, standard population, joinpoint settings, exact
> classification schemes) are marked "Not available from provided input (no full text)."

## Design type
Retrospective, population-level, cross-sectional-and-trend **descriptive epidemiological study** of
mortality using a public death registry. No intervention, no comparison cohort — the comparisons are
between demographic and geographic strata and across calendar years.

## Data source
CDC WONDER Multiple Cause of Death database (public/open; https://wonder.cdc.gov/). See
[src/environment.md](../../src/environment.md) and [related_work.md](../related_work.md#rw01-cdc-wonder-multiple-cause-of-death-database).

## Population and case definition
- **Population**: US decedents aged 45 years and older, 1999–2020.
- **Case definition (AD-related death)**: ICD-10 codes F01, F03, G30, G31.1.
  - F01 — vascular dementia
  - F03 — unspecified dementia
  - G30 — Alzheimer disease
  - G31.1 — senile degeneration of brain, not elsewhere classified
- **Underlying vs multiple cause**: Not available from provided input (no full text). (Data source
  is the *Multiple Cause of Death* file per `sources.yaml`.)

## Analysis pipeline
1. **Extraction** — Query CDC WONDER for AD-attributed deaths and matching population denominators,
   1999–2020, ages 45+, stratified by sex, race/ethnicity, age, urbanization, census region, state.
2. **Rate computation** —
   - Crude Mortality Rate (CMR) per 100,000 (used for age-band comparison, e.g. 85+).
   - Age-Adjusted Mortality Rate (AAMR) per 100,000 (primary cross-group metric; standard population
     not specified in abstract).
3. **Trend analysis** — Joinpoint regression on the annual AAMR series to identify trend segments;
   compute segment APCs and the overall Average Annual Percent Change (AAPC). See
   [E01](../experiments.md#e01-temporal-trend-of-ad-related-mortality-joinpoint-regression).
4. **Disparity analysis** — Compute and rank AAMR (and CMR for age) across each demographic and
   geographic axis; identify highest/lowest strata. See
   [E03](../experiments.md#e03-demographic-disparity-stratification-sex-raceethnicity-age),
   [E04](../experiments.md#e04-geographic-disparity-stratification-urbanization-census-region-state).

## Stratification axes
| Axis | Categories reported in abstract |
|------|--------------------------------|
| Sex | Female, Male |
| Race/ethnicity | Non-Hispanic Black, Non-Hispanic White, Non-Hispanic American Indian, Hispanic, Non-Hispanic Asian |
| Age | Bands through 85+ (only 85+ CMR reported in abstract) |
| Urbanization | Rural, Urban |
| Census region | Northeast, Midwest, South, West (only Midwest and Northeast values reported) |
| State | 50 states (only SC, TN, NY, FL cited as examples) |

## Outputs (as reported)
- Overall: death count and AAMR; trend AAPC.
- Per-stratum AAMR (and 85+ CMR).
Exact per-stratum values are in [claims.md](../claims.md); the paper's full numbered tables/figures
are not accessible (no full text).
