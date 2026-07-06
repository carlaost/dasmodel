# Study Design

## Type
Retrospective, observational, registry-based cross-sectional incidence study of a single calendar year (2021), with regional (public-health-region) comparison. Explicitly "the first to characterize the incidence of ADRD by PHRs in South Carolina using the SCADR data." Not a clinical trial; no intervention; no individual follow-up beyond registry records.

## Data sources
- **Numerator**: South Carolina Alzheimer's Disease Registry (SCADR), 2021 Registry data — the most recent and complete data available at analysis time. In existence since 1988; described as the oldest and most comprehensive dementia registry in the US. Cases identified/diagnosed by a physician/neurologist following a healthcare visit and coded via ICD-10-CM. Case ascertainment from SC inpatient hospitalizations, emergency departments, vital records, state health plans, and other claims data.
- **Denominator**: Annual County Resident Population Estimates (ACRPE), US Census Bureau (2020 census, Vintage 2020 estimates, 2020 Demographic Analysis estimates).
- **Geography**: US Census TIGER/Line shapefiles for mapping.

## Unit and grouping
- **Independent variable**: Public Health Region (PHR) — Low Country, Midlands, Pee Dee, Upstate (fixed effect).
- **Dependent variable**: new (2021) ADRD case counts by PHR (modeled as rates via a population offset).
- **Geographic resolution**: county-level incidence aggregated to PHR-level.

## Case definition and inclusion
- ADRD cases with year of diagnosis = 2021.
- Registrants aged 50–110 years (age 50 chosen to capture early-onset ADRD; 110 as an upper bound).
- **Exclusions** (Figure 1): year of diagnosis before 2021 (n = 357,895); age <50 or >110 (n = 293, excluded for possible data-entry/measurement error). Registry total 1988–2021 = 377,143 → 19,248 (2021) → **18,955** analytic sample.
- Cases with missing county/zip (n = 3,910) are retained in the overall sample but cannot be assigned a PHR (handled in sensitivity analyses).

## Variable operationalization
- **ADRD subtype**: Alzheimer's disease, Vascular dementia, Mixed dementia, Other medical conditions (combining alcohol/drug-induced dementia, dementia with other conditions, dementia with Lewy bodies, Pick's disease, frontotemporal dementia).
- **Age groups**: <65, 65–74, 75–84, ≥85.
- **Race**: non-Hispanic White; non-Hispanic Black (African American); "Other" (Asian, American Indian, Other listed race, Hispanic, unknown — combined due to small numbers).
- **Sex**: male / female.

## Ethics / governance
- No IRB/consent statement is present in the provided text (registry secondary-data analysis). Funding supported by the South Carolina Alzheimer's Disease Research Center via state resources. Data access is by request under licenses/restrictions (Data availability statement).

## Reporting/context
- Conducted after the COVID-19 lockdown period in South Carolina (authors flag potential effect on ADRD case reporting).
