# Related Work — Typed Dependency Graph

> Grounding: abstract-only. The full References list was not accessible (paywalled full text), so
> the paper's complete citation footprint cannot be reproduced. The dependencies below are the ones
> the abstract and verified `sources.yaml` make explicit — primarily the data source and the
> methodological tooling — plus the standard infrastructure the study relies on. Individual prior
> studies cited in the (inaccessible) Introduction/Discussion are: Not available from provided input
> (no full text).

## RW01: CDC WONDER Multiple Cause of Death database
- **DOI**: — (public data system; https://wonder.cdc.gov/)
- **Type**: imports (primary data dependency — a concrete, open data source)
- **Delta**:
  - What changed: The study consumes CDC WONDER mortality records rather than collecting new data.
  - Why: Provides nationwide, standardized, death-certificate-based mortality data for 1999–2020.
- **Claims affected**: C01, C02, C03, C04, C05, C06, C07, C08
- **Adopted elements**: AD-attributed death counts, population denominators, and demographic /
  geographic stratifiers (sex, race/ethnicity, age, urbanization, census region, state).
- **Access**: open / public. Data identifier: none study-specific (query defined by ICD-10 codes
  F01, F03, G30, G31.1; ages 45+; 1999–2020). Verified in `sources.yaml` (data[0], verified: true).

## RW02: ICD-10 (International Classification of Diseases, 10th Revision)
- **DOI**: — (WHO classification standard)
- **Type**: imports (case-definition dependency)
- **Delta**:
  - What changed: AD-related deaths are operationalized via ICD-10 codes F01, F03, G30, G31.1.
  - Why: Standardized cause-of-death coding enables reproducible case identification.
- **Claims affected**: C02 (and, via the case definition, all claims)
- **Adopted elements**: The four-code AD/dementia case definition.

## RW03: Joinpoint regression methodology
- **DOI**: — (method; commonly the NCI Joinpoint Regression Program)
- **Type**: imports (analytical-method dependency)
- **Delta**:
  - What changed: Temporal trends in AAMR are quantified via joinpoint regression and summarized as
    AAPC.
  - Why: Detects changes in trend slope over the 22-year window and yields a single trend summary.
- **Claims affected**: C01
- **Adopted elements**: Segmented log-linear trend fitting; APC/AAPC estimation.

## RW04: Age-standardization / standard population methodology
- **DOI**: — (standard demographic method)
- **Type**: imports (rate-comparison dependency)
- **Delta**:
  - What changed: Crude rates are converted to age-adjusted rates (AAMR) for cross-group comparison.
  - Why: Removes confounding by age structure across sex, race/ethnicity, and geography.
- **Claims affected**: C02, C03, C04, C06, C07, C08
- **Adopted elements**: Direct age standardization to a reference population (specific standard not
  available without full text).

---

## Citation footprint note

The abstract makes no explicit reference to prior AD-mortality studies by name. A full typed
dependency graph of the Introduction/Discussion citations (background prevalence studies, prior
CDC WONDER analyses of other conditions, disparity literature) cannot be constructed:
**Not available from provided input (no full text).**
