# Study Design

> Grounding: abstract-only. This file reflects the design as stated in the abstract Methods/Results.
> Parameters not stated in the abstract are marked "Not available from provided input (no full text)".

## Design type
Retrospective, population-level ecological trend study of US mortality using death-certificate data.
No intervention, no individual follow-up. Descriptive epidemiology plus segmented trend analysis.

## Data source and cohort definition
- **Source**: CDC WONDER Multiple Cause of Death database (US death certificates), 1999–2020. (Verified data source; open access — `sources.yaml`.)
- **Underlying-cause selector**: Alzheimer's disease.
- **Comorbidity subset**: Deaths also involving metabolic syndrome-related conditions (via multiple-cause fields).
- **Age restriction**: ≥75 years.
- **Exact ICD-10 code sets for AD and metabolic-syndrome conditions**: Not available from provided input (no full text).

## Outcome measure
Age-adjusted mortality rate (AAMR) per 100,000 population, computed overall and within strata.
Standard population used for adjustment: Not available from provided input (no full text).

## Stratification axes (analyzed variables)
1. **Temporal**: calendar year 1999–2020 (primary trend axis).
2. **Sex**: female vs male.
3. **Race/ethnicity**: including Non-Hispanic African American (highest AAMR) and other groups.
4. **Geographic**: state (percentile ranking) and region.
5. **Place of death**: death-certificate place-of-death categories.

## Trend-analysis method
Joinpoint regression (segmented log-linear model) applied to the annual AAMR series overall and per
stratum, to identify significant trend segments, inflection points (joinpoints), and the reported
early-to-mid-2000s peak. Number of joinpoints, APC/AAPC values, and significance thresholds: Not
available from provided input (no full text).

## Analysis flow (reconstructed)
1. Query CDC WONDER → obtain death counts and populations by stratum-year (E01).
2. Compute annual and stratum-specific AAMRs (per 100,000) (E02–E05).
3. Fit Joinpoint regression to detect trends and inflections (E02, E03, E05).
4. Rank states by AAMR percentile for geographic disparity (E04).
5. Summarize disparities across sex, race/ethnicity, and geography for the conclusions.

## Ethics
Uses de-identified, publicly available aggregate mortality data; typically exempt from IRB review.
Explicit ethics statement: Not available from provided input (no full text).
