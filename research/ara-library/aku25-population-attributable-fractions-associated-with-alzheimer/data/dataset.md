# Dataset — Medicare 5% Sample

> Grounded in the abstract (`paper.pdf`, p. 743) and `sources.yaml` (verified discovered source).
> Fields the abstract does not state are marked "Not specified in the published abstract".

## Provenance
- **Name**: Medicare 5% sample (CMS administrative claims / enrollment data).
- **Provider**: U.S. Centers for Medicare & Medicaid Services (CMS).
- **Access channel**: **ResDAC** (Research Data Assistance Center) — the CMS-designated channel for
  research data requests.
- **Access type**: **Controlled**. Requires a CMS research data request and Data Use Agreement; not
  publicly downloadable.
- **Identifier / accession**: None public. No accession ID; no formal Data Availability statement in
  the abstract. (Per `sources.yaml`, verified.)

## Description
- A 5% random sample of the U.S. Medicare beneficiary population, characterized in the abstract as
  "high-power" — large enough to support jointly-adjusted survival modeling and PAF decomposition
  within race- and sex-specific subpopulations.

## Size & coverage
- **N (beneficiaries)**: Not specified in the published abstract.
- **Calendar years / follow-up window**: Not specified in the published abstract.
- **Geography**: United States (national Medicare program).

## Variables used (as inferable from the abstract)
| Variable | Role | Notes |
|----------|------|-------|
| Clinical AD/ADRD diagnosis | Outcome (event) | From claims; not biomarker/autopsy confirmed |
| Heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, traumatic brain injury, diabetes mellitus | Predictors (9 modeled diseases) | ICD code definitions not specified |
| Dual Medicare/Medicaid eligibility | Low-income proxy | Whether retained in final model not specified |
| Race | Stratification | Categories reported: Black, Asian, Hispanic, White, Native American |
| Sex | Stratification | Male, female |
| Age | Stratification | Age-bin definitions not specified |

## Licensing / ethics
- **Licensing**: Controlled CMS data under a Data Use Agreement (terms not restated in the abstract).
- **Consent / IRB / ethics**: Not specified in the published abstract (secondary use of
  de-identified/limited administrative data is typical for such studies, but not stated here).

## Clinical trials
- None. This is an observational study; no NCT or PROSPERO registration exists or was found (per
  `sources.yaml`, verified).
