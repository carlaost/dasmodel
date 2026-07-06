# Environment

> Abstract-only compile. This is a **secondary-data, analytical** study — there is no released code
> and no computational environment described in the abstract. Fields below are populated from the
> abstract and verified `sources.yaml`; unstated details are marked "Not available from provided
> input (no full text)."

- **Language/runtime**: Analytical — none released. No code/software availability statement; no
  GitHub/GitLab/Zenodo/OSF repository was found (`sources.yaml: code: []`).
- **Framework**: Not applicable / not specified. Trend analysis performed with **Joinpoint
  regression** (software and version not stated in the abstract; commonly the NCI Joinpoint
  Regression Program). Rate extraction performed via the CDC WONDER web query interface.
- **Hardware**: n/a (web-based data query + standard statistical software).
- **Data sources**:
  - **CDC WONDER** — Wide-ranging Online Data for Epidemiologic Research. US Multiple Cause of Death
    mortality data, 2015-2024. Publicly available, de-identified death-certificate data.
    - **Identifiers**: ICD-10-CM **G30.0** = EOAD (underlying cause of death); **G30.1** = late-onset
      AD (used in sensitivity analysis).
    - **Metric extracted**: age-adjusted mortality rate (AAMR) per 1,000,000 population.
    - **Access**: open / public (https://wonder.cdc.gov). `verified: true` in `sources.yaml`.
    - **Availability statement**: Publisher (SAGE) Data Availability note — data are publicly
      available from CDC WONDER; extracted/analyzed data also available from the corresponding
      author on reasonable request.
- **Key dependencies**: CDC WONDER query interface; Joinpoint regression program (version not
  specified); standard rate-ratio / confidence-interval computation.
- **Protocols**: No preregistration / PROSPERO registration (this is not a systematic review; it is a
  registry-data analysis). Analysis protocol beyond the abstract: Not available from provided input
  (no full text).
- **Random seeds**: n/a (deterministic secondary-data analysis).
- **Clinical trials**: None. Population-based epidemiological study; no NCT identifiers
  (`sources.yaml: clinical_trials: []`).
- **Code artifact note**: No concrete code or printed pseudocode exists in the input, so
  `src/execution/` is intentionally absent (Compiler Rule 14 — do not fabricate a stub from a
  prose/abstract-only method).
