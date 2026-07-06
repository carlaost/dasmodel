# Environment and Reproducibility

> Grounding: abstract-only. No code, dataset, data dictionary, container, software versions, or
> analysis scripts were provided.

## Data Source

- Study: Atherosclerosis Risk in Communities (ARIC).
- Field centers: Jackson, Mississippi; Forsyth County, North Carolina; Minneapolis suburbs, Minnesota; Washington County, Maryland.
- Follow-up: 1987-2020.
- Analysis dates: August 2023 to December 2024.

## Cohort Inputs

- Black and White participants with complete exposure and covariate data.
- Baseline defined by age at risk factor measurement: 45-54 years, 55-64 years, and 65-74 years.
- Analytic sample counts and dementia case counts are recorded in `logic/claims.md` C02.

## Exposure Inputs

- Hypertension: systolic BP >=130 mm Hg, diastolic BP >=80 mm Hg, or BP medication use.
- Diabetes: fasting glucose >=126 mg/dL, nonfasting glucose >=200 mg/dL, self-reported physician diagnosis, or diabetes medication use.
- Current smoking: self-reported.
- Aggregate exposure: at least one vascular risk factor.

## Outcome Inputs

- Incident dementia by age 80 years.
- Incident dementia after age 80 years.
- Ascertainment details: Not available from provided input.

## Computational Environment

- Software: Not available from provided input.
- Hardware: Not available from provided input.
- Random seeds: Not available from provided input.
- Statistical packages: Not available from provided input.
- Reproducible code location: Not available from provided input.

## Artifact Capture Decision

No `src/execution/` files were created because the provided source contains no code, pseudocode,
named implementation interface, scripts, or configuration files. Re-encoding the abstract's prose as
code would fabricate implementation details.
