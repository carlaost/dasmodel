# Constraints, Assumptions, and Limitations

> Grounding: abstract-only. The abstract does not include a Limitations section; the items below are
> the boundary conditions inherent to the stated design (CDC WONDER death-certificate analysis with
> the given case definition) plus assumptions the method requires. Author-stated limitations from
> the Discussion are: Not available from provided input (no full text).

## Boundary conditions
- **Time window**: 1999–2020 only. Pre-1999 (ICD-9 era) and post-2020 data are out of scope.
- **Population**: Decedents aged 45 years and older only.
- **Geography**: United States (national), with strata by urbanization, census region, and state.
- **Case definition**: AD-related deaths captured by ICD-10 codes F01, F03, G30, G31.1 — a
  dementia-inclusive definition, broader than Alzheimer disease (G30) alone.
- **Data granularity**: Subject to CDC WONDER's small-cell suppression (rates/counts below CDC
  thresholds are not released), which can limit fine strata (e.g. small states, rare race/ethnicity
  cells).

## Assumptions
- A1: Death-certificate cause-of-death coding reliably identifies AD-related deaths across the study
  period. (Known concern: AD is under-reported and variably coded on death certificates.)
- A2: The four-code ICD-10 set is an appropriate operational definition of "AD-related" mortality.
- A3: Age standardization renders AAMRs comparable across demographic and geographic groups.
- A4: CDC WONDER population denominators are accurate for rate computation.
- A5: Joinpoint log-linear segmentation is an appropriate model for the AAMR time series.

## Known limitations (inherent to design; author-stated limitations unavailable)
- **Ecological / descriptive**: The study reports associations and disparities, not causes; no
  individual-level risk factors, adjustment for socioeconomic status, comorbidity, or access.
- **Cause-of-death misclassification**: AD deaths are known to be under- and mis-attributed on death
  certificates; changes in coding practice or awareness over 1999–2020 can inflate apparent trends
  (the AAPC of 3.18 may partly reflect improved diagnosis/reporting rather than true incidence).
- **Dementia-inclusive codes**: Including F01/F03/G31.1 mixes non-Alzheimer dementias into
  "AD-related" mortality; a G30-only definition would yield lower counts.
- **Definition of urbanization**: The specific rural/urban classification scheme is not stated in
  the abstract (not available without full text).
- **Standard population**: The reference standard population used for age adjustment is not stated in
  the abstract (not available without full text).
- **No joinpoint detail**: Segment breakpoints and per-segment APCs are not in the abstract; only the
  overall AAPC (3.18) is reported.
- **Suppressed / partial reporting**: The abstract reports only extreme regions (Midwest, Northeast)
  and four illustrative states; the full stratum tables are not accessible.
