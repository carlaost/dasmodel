# Constraints, Assumptions & Limitations

> Abstract-only compile. Limitations the authors themselves state would live in the full-text
> Discussion, which is unavailable; those are marked accordingly. The items below are the boundary
> conditions inherent to the design as described in the abstract, plus the compilation's own caveats.

## Boundary conditions (design as described in the abstract)
- **Case ascertainment is code-dependent.** EOAD deaths are defined solely by ICD-10-CM **G30.0** as
  the *underlying* cause of death in CDC WONDER. Deaths where EOAD is a contributing (not underlying)
  cause, or where AD is coded as unspecified (G30.9) or as "dementia" codes, are excluded — this
  yields a conservative and coding-sensitive count.
- **"Reported" mortality, not incidence.** All rates reflect death-certificate reporting. A rise in
  reported EOAD mortality can reflect improved recognition/coding rather than (or in addition to) a
  true change in disease occurrence. The abstract's own wording ("reported EOAD mortality") signals
  this.
- **Ecological / administrative data.** CDC WONDER provides population-level counts and rates, not
  individual clinical records; no biomarker or autopsy confirmation of AD diagnosis is available.
- **Small-cell suppression.** CDC WONDER suppresses or flags small death counts for confidentiality,
  which can limit the reliability of finely stratified subgroup AAMRs (e.g., rarer race/ethnicity ×
  region × age cells).
- **Age-at-death vs age-at-onset.** G30.0 encodes *early onset* (before age 65); the reported mean
  age at death (69.8 y) and modal band (65-74) describe when EOAD-coded decedents died, not disease
  onset. This is internally consistent but must not be read as "deaths before 65."

## Assumptions
- **A1**: ICD-10-CM G30.0 underlying-cause coding validly and consistently identifies EOAD deaths
  across the 2015-2024 window.
- **A2**: Age-adjusted mortality rates use a consistent standard population across all years and
  subgroups, making cross-group and cross-year comparisons valid. (The specific standard population
  is not stated in the abstract; CDC WONDER conventionally uses the US 2000 standard.)
- **A3**: Joinpoint regression's log-linear-segment assumption adequately describes the EOAD and LOAD
  AAMR trends.
- **A4**: G30.1 (LOAD) is a valid internal comparator for isolating EOAD-specific trend signal from
  generic AD-coding drift.

## Known limitations
- Author-stated limitations: **Not available from provided input (no full text).**
- Compilation limitations: This ARA is grounded only in the published abstract and verified
  `sources.yaml`. Per-year rate series, subgroup denominators and CIs (beyond the sex RR), the
  number of Joinpoint segments, the reference groups used for RRs, the exact CDC WONDER query
  specification, and the standard population are all unavailable and marked as such throughout.
