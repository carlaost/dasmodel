# Dataset — CDC WONDER US Mortality (2015-2024)

> Abstract-only compile. Provenance and variables below are grounded in the abstract and verified
> `sources.yaml`. Exact extracted counts/rates by stratum are "Not available from provided input (no
> full text)"; top-line values appear in `logic/claims.md` and are attributed to the abstract.

## Provenance
- **Name**: CDC WONDER — Wide-ranging Online Data for Epidemiologic Research (Multiple Cause of Death
  / underlying-cause mortality files).
- **Custodian**: US Centers for Disease Control and Prevention (CDC), National Center for Health
  Statistics.
- **Source records**: US death certificates.
- **Coverage**: United States, 2015-2024.
- **Access**: Open / public (https://wonder.cdc.gov). De-identified. `verified: true` in
  `sources.yaml`. Extracted/analyzed subset also available from the corresponding author on
  reasonable request (per SAGE Data Availability statement).
- **Licensing/consent/IRB**: De-identified public vital-statistics data; typically exempt from IRB
  (not explicitly stated in the abstract).

## Case definition
- **EOAD**: ICD-10-CM **G30.0** ("Alzheimer's disease with early onset") recorded as the
  **underlying cause of death (UCD)**.
- **LOAD (comparator, sensitivity analysis)**: ICD-10-CM **G30.1** ("Alzheimer's disease with late
  onset").

## Cohort size (as reported)
- **4890** EOAD-related deaths over 2015-2024; **63.7%** female. (See C02; exact per-stratum counts
  not available from the abstract.)

## Variables used
| Variable | Role | Notes |
|----------|------|-------|
| Calendar year (2015-2024) | trend axis | Annual AAMR series for Joinpoint regression |
| Underlying cause of death (ICD-10-CM) | case definition | G30.0 (EOAD); G30.1 (LOAD) |
| Age-adjusted mortality rate (per 1,000,000) | outcome | Standard population not stated in abstract |
| Sex | stratifier | Female vs male rate ratio |
| Race/ethnicity | stratifier | Non-Hispanic White highest reported |
| US census region | stratifier | Northeast / Midwest / South / West; Midwest highest reported |
| Age at death (bands) | stratifier | Mean 69.8 y; modal band 65-74 |

## Known data caveats
- Small-cell suppression in CDC WONDER may render finely stratified subgroup rates unreliable or
  unreported.
- Ascertainment depends on death-certificate coding practices; possible misclassification among
  G30.0 / G30.1 / G30.9 (unspecified).
- Rates are "reported" mortality (recognition/coding sensitive), not confirmed incidence.
