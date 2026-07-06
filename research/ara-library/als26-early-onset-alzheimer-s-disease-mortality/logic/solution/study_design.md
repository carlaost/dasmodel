# Study Design & Analytic Method

> Abstract-only compile. The design below is reconstructed from the abstract's Methods and Results
> sentences. Steps stated in the abstract are grounded; procedural detail absent from the abstract is
> marked "Not available from provided input (no full text)."

## Design type
Population-based, retrospective, observational cross-temporal study of national death-certificate
mortality (a descriptive/analytic epidemiological trends-and-disparities study). Not interventional;
no clinical trial, no PROSPERO registration (per `sources.yaml`).

## Data source & study window
- **Source**: CDC WONDER (Wide-ranging Online Data for Epidemiologic Research), US mortality data.
- **Window**: 2015-2024.
- **Case definition (EOAD)**: ICD-10-CM code **G30.0** recorded as the underlying cause of death (UCD).
- **Comparator (LOAD)**: ICD-10-CM code **G30.1**, used only in the sensitivity analysis.

## Outcome measure
- **Age-adjusted mortality rate (AAMR)** per 1,000,000 population, extracted from CDC WONDER.
- Standard population used for age adjustment: Not available from provided input (no full text)
  (CDC WONDER conventionally uses the US 2000 standard population).

## Analytic pipeline
1. **Extraction**: Query CDC WONDER for G30.0 UCD deaths, 2015-2024, with counts and AAMRs, stratified
   by calendar year, sex, race/ethnicity, US census region, and age band.
2. **Temporal trend**: Fit **Joinpoint regression** to the annual EOAD AAMR series to estimate the
   **annual percent change (APC)** and detect any change points. → C01.
3. **Disparity analysis**: Compute **rate ratios (RR)** of AAMRs between demographic groups with 95%
   confidence intervals; rank groups by AAMR.
   - Sex: female vs male RR → C02.
   - Race/ethnicity: highest-AAMR group → C03.
   - US census region: highest-AAMR region → C04.
4. **Age-at-death description**: Summarize deaths by age band; compute mean age at death and modal
   band. → C05.
5. **Sensitivity analysis**: Repeat the extraction and Joinpoint trend for **G30.1 (LOAD)** and
   compare its increase against EOAD's. → C06.

## Reported top-line outputs (exact values in claims.md / evidence)
- EOAD AAMR rose from 0.14 to 2.59 per 1,000,000 (2015→2024), APC +19.96% (C01).
- 4890 EOAD deaths, 63.7% female; female-vs-male RR = 1.50 (95% CI 1.40-1.59) (C02).
- Non-Hispanic White (C03) and Midwest (C04) highest AAMRs.
- Mean age at death 69.8 y; modal band 65-74 (C05).
- LOAD increase lower than EOAD (C06).

## Reference groups & software
- RR reference groups (e.g., which sex/race/region is the denominator): Not available from provided
  input (no full text) — only the female-vs-male RR direction is given.
- Joinpoint software/version and settings: Not available from provided input (no full text).
