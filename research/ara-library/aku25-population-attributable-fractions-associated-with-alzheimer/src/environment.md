# Environment

> This is a purely analytical epidemiological study. No software repository, code, or computational
> environment was released or referenced (per `sources.yaml`, verified; and no code appears in the
> abstract). The fields below record what the source states and mark the rest as unspecified — no
> tooling is invented.

- **Language/runtime**: Not specified in the published abstract (statistical survival analysis;
  typical tools for Cox modeling on Medicare data are SAS, R, or Stata, but none is named — not
  recorded to avoid fabrication).
- **Framework**: Not specified in the published abstract (Cox proportional-hazards modeling + PAF
  estimation; specific package/procedure not named).
- **Hardware**: n/a — analytical/statistical computation; not specified.
- **Data sources**:
  - **Medicare 5% sample** — a 5% sample of the U.S. Medicare beneficiary population, drawn from CMS
    administrative claims/enrollment data.
    - Provider/repository: CMS via **ResDAC** (Research Data Assistance Center).
    - Access type: **controlled** — obtainable only through standard CMS/ResDAC research data request
      procedures (Data Use Agreement).
    - Identifier/accession: **none public** (no accession ID); no formal Data Availability statement
      in the abstract. (Source: `sources.yaml`, verified; abstract p. 743.)
    - Variables used: AD/ADRD clinical diagnosis (outcome), comorbid-disease diagnoses (9 modeled
      predictors), dual Medicare/Medicaid eligibility (low-income proxy), race, sex, age.
    - See `data/dataset.md` for full provenance.
  - **No clinical-trial data source**: observational study; no NCT or PROSPERO registration exists or
    was found (per `sources.yaml`, verified).
- **Key dependencies**: None released. No code repository, container, or environment file exists
  (`code: []` in `sources.yaml`).
- **Protocols**: No preregistration/protocol referenced. Analysis pipeline (univariable Cox →
  multivariable Cox → total-PAF → disease-specific PAF decomposition by age/race/sex) is described
  qualitatively in the abstract; see `logic/solution/study_design.md`.
- **Random seeds**: n/a / Not specified in the published abstract.
