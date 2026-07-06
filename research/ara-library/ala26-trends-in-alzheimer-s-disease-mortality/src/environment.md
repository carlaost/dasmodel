# Environment

> Grounding: abstract-only. This is a purely analytical epidemiological study with no released code
> repository (`sources.yaml` `code: []`). No software versions, seeds, or hardware are reported in
> the abstract. The one concrete, verified artifact is the public data source (CDC WONDER).

- **Language/runtime**: analytical — no programming runtime reported. Death-certificate data queried via the CDC WONDER web interface.
- **Framework**: Joinpoint Regression Program (segmented log-linear trend analysis) — the standard tool for AAMR joinpoint analysis. Specific version: Not specified in paper.
- **Hardware**: n/a (web-query + desktop statistical analysis).
- **Data sources**:
  - **CDC WONDER Multiple Cause of Death database** — US death certificates, 1999–2020. Repository: CDC WONDER (https://wonder.cdc.gov/). Access: **open** (publicly queryable; no login). Identifier/accession: none reported by the authors (no data-availability statement). Verified in `sources.yaml` (`data[0]`, `verified: true`). Query scope used: underlying cause of death = Alzheimer's disease; ages ≥75; metabolic syndrome-related conditions subset via multiple-cause fields. Exact ICD-10 code sets: Not available from provided input (no full text).
- **Clinical trials**: none (`sources.yaml` `clinical_trials: []`) — this is a retrospective mortality-trends study, not a trial or systematic review; no NCT/PROSPERO registration applies.
- **Code**: none located or expected (`sources.yaml` `code: []`). No analysis scripts released; therefore no `src/execution/` files are captured (a prose/tool-based method, not code — capturing a stub would fabricate content that does not exist).
- **Key dependencies**: CDC WONDER data system; Joinpoint Regression Program (version not specified).
- **Protocols**: No preregistration/PROSPERO record reported. Analysis protocol described only at abstract level (age-adjusted rates + Joinpoint regression across demographic, geographic, and place-of-death strata).
- **Random seeds**: n/a (deterministic rate computation and regression).
