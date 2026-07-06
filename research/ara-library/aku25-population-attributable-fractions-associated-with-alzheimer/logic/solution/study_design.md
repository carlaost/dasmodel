# Study Design — Observational Cox + PAF-Decomposition Pipeline

> Reconstructed at the level the conference abstract (`paper.pdf`, pp. 743–744) supports. This is an
> **observational, retrospective cohort** analysis of administrative claims — not an interventional
> trial (no NCT/PROSPERO registration; per `sources.yaml`, verified). Procedural detail the abstract
> omits is marked "Not specified in the published abstract"; nothing is invented.

## Design type
- Observational retrospective cohort study on the Medicare 5% sample; survival (time-to-event)
  analysis of clinical AD/ADRD diagnosis, followed by population-attributable-fraction estimation
  and decomposition.

## Pipeline (as described in the abstract)

1. **Cohort & outcome definition** (Medicare 5% sample)
   - Data source: CMS administrative claims/enrollment data, 5% sample.
   - Outcome: clinical diagnosis of AD/ADRD from Medicare records.
   - Exposures: comorbid diseases + low income proxied by dual Medicare eligibility.
   - *Not specified*: N, calendar years, follow-up window, censoring rules, ICD code definitions.

2. **Univariable Cox screening** (→ E01)
   - Fit a univariable Cox proportional-hazards model per candidate disease (and dual eligibility).
   - Purpose: identify the "most powerful predictors" of AD/ADRD risk.

3. **Multivariable model construction & predictor identification** (→ E02)
   - Fit multivariable Cox model(s) jointly adjusting the surviving candidates.
   - Result: a compact **nine-disease** predictor set — heart failure, hypertension, arrhythmia,
     stroke, hypotension, renal disease, depression, traumatic brain injury, diabetes mellitus — as
     the primary determinants of AD/ADRD risk variation.
   - *Not specified*: exact selection criterion/threshold, adjusted hazard ratios, model-fit metrics.

4. **Total-PAF estimation & age stratification** (→ E03)
   - Convert the multivariable risk estimates into a **total PAF** for the general older-adult
     population; examine how the explained fraction of total PAF varies across age.
   - Finding: the explained fraction of total PAF **increases with age**.
   - *Not specified*: PAF estimator/formula, exposure-prevalence source, age-bin definitions.

5. **Disease-specific PAF decomposition, stratified by race and sex** (→ E04)
   - Decompose the total PAF into per-disease shares (% of total PAF), computed within sex and race
     subpopulations, and rank contributors.
   - Findings (see `logic/claims.md` C03–C09 for exact quoted values): hypertension/stroke/depression
     dominate throughout, with the leading contributor shifting by subpopulation; heart failure is a
     consistent fourth; a subpopulation-specific secondary tail (hypotension, diabetes, arrhythmia,
     TBI) follows.
   - *Not specified*: decomposition/allocation method (e.g., sequential vs average attribution),
     subgroup sample sizes.

## Rationale for the design
- A high-power administrative sample makes jointly-adjusted survival modeling and subpopulation PAF
  decomposition feasible where cohort studies are typically under-powered — enabling a ranked,
  demographically resolved map of modifiable attributable AD/ADRD burden.

## What the design does NOT establish (per the source)
- No causal effect estimates beyond the attributable-fraction framing (see `constraints.md` A4/L3).
- No validation of the proportional-hazards assumption, no handling of competing risk of death, and
  no uncertainty quantification are reported in the abstract.
