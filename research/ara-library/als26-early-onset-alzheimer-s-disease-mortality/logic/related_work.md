# Related Work & Typed Dependencies

> Abstract-only compile. The abstract names no specific prior publications, so no bibliographic
> predecessor works can be cited (that citation footprint is "Not available from provided input (no
> full text)"). What the abstract and the verified `sources.yaml` DO establish are the study's
> concrete **methodological and data dependencies**, captured below as typed dependency blocks. These
> are the artifacts the study imports and builds on.

## RW01: CDC WONDER — Multiple Cause of Death mortality database
- **DOI**: — (data resource; https://wonder.cdc.gov)
- **Type**: imports (data source — first-class dependency)
- **Delta**:
  - What changed: This study queries the existing CDC WONDER national death-certificate database rather than collecting new data; the contribution is the EOAD-specific extraction, age-adjustment, trend, and disparity analysis layered on top.
  - Why: CDC WONDER provides publicly available, de-identified US mortality data with the demographic/geographic/temporal granularity needed to compute AAMRs and rate ratios.
- **Claims affected**: C01, C02, C03, C04, C05, C06
- **Adopted elements**: Underlying-cause-of-death records 2015-2024; age-adjusted mortality rate computation; demographic/regional stratification. Access: open/public. Identifier: ICD-10-CM G30.0 (EOAD), G30.1 (LOAD sensitivity).

## RW02: ICD-10-CM classification (WHO/CDC clinical modification)
- **DOI**: — (classification standard)
- **Type**: imports (case-definition standard)
- **Delta**:
  - What changed: The study operationalizes "EOAD death" as ICD-10-CM code **G30.0** ("Alzheimer's disease with early onset") recorded as underlying cause of death, and "LOAD death" as **G30.1**.
  - Why: A standardized code is required to identify cases consistently across the national dataset and over time.
- **Claims affected**: C01, C05, C06 (case definition), and by extension all claims
- **Adopted elements**: G30.0 and G30.1 code definitions.

## RW03: Joinpoint regression methodology (segmented log-linear trend analysis)
- **DOI**: — (statistical method; commonly the NCI Joinpoint Regression Program, Kim et al. 2000, Stat Med)
- **Type**: imports (analytic method)
- **Delta**:
  - What changed: Applies Joinpoint regression to the EOAD (and LOAD) AAMR time series to estimate the annual percent change and detect trend change points.
  - Why: Joinpoint is the standard tool in mortality/cancer surveillance for characterizing whether and where a rate trend changes slope.
- **Claims affected**: C01, C06
- **Adopted elements**: APC estimation via segmented log-linear fitting. Specific software/version/settings: Not available from provided input (no full text).

## RW04: Rate-ratio disparity analysis
- **DOI**: — (standard epidemiologic method)
- **Type**: imports (analytic method)
- **Delta**:
  - What changed: Uses rate ratios (RR) of AAMRs with 95% confidence intervals to quantify demographic disparities (sex reported as RR = 1.50, 95% CI 1.40-1.59).
  - Why: RR is a standard, interpretable measure for comparing group mortality after age adjustment.
- **Claims affected**: C02, C03, C04
- **Adopted elements**: RR computation and CI-based inference.

## Predecessor literature (bibliographic)
- Not available from provided input (no full text). The abstract states only that "population-level
  data on trends and disparities in EOAD mortality are limited," implying a gap relative to the
  broader (late-onset-dominated) AD-mortality literature, but names no specific prior series.
