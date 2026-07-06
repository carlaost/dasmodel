# Environment

> Grounding: abstract-only. This is a purely analytical, secondary-data study. No code repository,
> released dataset, or clinical trial is associated with it (verified in `sources.yaml`: `code: []`,
> `clinical_trials: []`). Software versions and analysis scripts are not available (no full text).

- **Language/runtime**: analytical — not specified in abstract. No code repository found or
  referenced (`sources.yaml` code: []).
- **Framework**: Not specified in abstract. Trend analysis used joinpoint regression (tool likely
  the NCI Joinpoint Regression Program, but the specific software/version is not available without
  full text).
- **Hardware**: n/a (secondary analysis of aggregate registry data).
- **Data sources**:
  - **CDC WONDER Multiple Cause of Death database** — public/open, https://wonder.cdc.gov/
    - Access type: open (public web query interface; no registration required for aggregate data).
    - Identifier: none study-specific (no accession). Query is defined by: ICD-10 codes
      **F01, F03, G30, G31.1**; decedents aged **45+**; years **1999–2020**; stratifiers sex,
      race/ethnicity, age, urbanization, census region, state.
    - Verified: yes (`sources.yaml` data[0], verified: true).
    - Note: CDC WONDER applies small-cell suppression to protect confidentiality.
- **Key dependencies**: CDC WONDER (data); ICD-10 (case coding); joinpoint regression method;
  age-standardization method. See [logic/related_work.md](../logic/related_work.md).
- **Protocols**: No preregistration (e.g. PROSPERO) identifier found or referenced. Analysis
  protocol beyond the abstract METHODS is Not available from provided input (no full text).
- **Random seeds**: n/a (deterministic descriptive statistics; no stochastic modeling reported).

## Clinical trials
None. This is a registry/database analysis, not an interventional study; no NCT identifiers
(`sources.yaml` clinical_trials: []).

## Reproduction pointer
The headline results are, in principle, reproducible by re-issuing the CDC WONDER query with the
exact case definition above — see [logic/experiments.md](../logic/experiments.md) E05.
