# Experiments (Analysis Plans)

For this population-based cohort study, an "experiment" is the statistical analysis procedure used to estimate and support a claim. These are declarative and directional only; exact numbers live in `evidence/` and `claims.md`.

## E01: Cohort assembly and baseline descriptive characterization
- **Verifies**: C01
- **Setup**:
  - Population: SNAC-K, 3363 randomly selected Kungsholmen residents aged 60+ at baseline (2001-2004).
  - Inclusion: dementia-free at baseline (n=3123) with available blood biomarker data (excludes n=833 missing biomarkers) → baseline n=2290; excludes 142 (6.2%) who dropped out after baseline with no follow-up → analytic n=2148.
  - System: descriptive (medians/IQR for continuous variables, n/% for categorical).
- **Procedure**:
  1. Apply inclusion/exclusion criteria to the SNAC-K baseline sample.
  2. Compare included vs. excluded/dropout participants on demographic and clinical characteristics.
  3. Tabulate baseline demographics, chronic disease burden, and biomarker levels, overall and by age group (<78 vs ≥78).
  4. Tabulate incident MCI, all-cause dementia, AD dementia, and mortality over follow-up.
- **Metrics**: sample sizes at each exclusion step; medians (Q1-Q3) and counts (%) for baseline variables; incidence counts and percentages.
- **Expected outcome**: A large, long-followed community cohort with sufficient baseline MCI cases and incident transitions to power multistate transition modeling; participants with missing biomarker data or attrition differ systematically (older, more comorbid) from the analytic sample.
- **Baselines**: none (descriptive).
- **Dependencies**: none

## E02: Continuous-biomarker multistate Markov spline modeling
- **Verifies**: C02, C05
- **Setup**:
  - Data: baseline z-scored biomarker levels (6 biomarkers) for the analytic cohort (n=2148).
  - Model: four-state parametric multistate Markov model (NC, MCI, dementia, death-absorbing), Gompertz baseline hazard, age as time scale, adjusted for sex and education.
  - Functional form: restricted cubic splines (3 knots at 25th/50th/75th percentiles) per biomarker, median as reference.
- **Procedure**:
  1. Fit the multistate model with each biomarker's spline term, separately per biomarker.
  2. Extract HR curves (with 95% CI bands) for each of the three transitions (NC→MCI, MCI→NC, MCI→all-cause dementia) as a function of biomarker z-score.
  3. Repeat for AD-specific dementia transition (Supplementary Fig. S1, not in provided input).
- **Metrics**: HR curve shape (linear vs. non-linear) and magnitude across the biomarker z-score range, per transition.
- **Expected outcome**: Non-linear, rising HR curves for MCI→dementia transitions for five of six biomarkers (all but Aβ42/40); flat curves (HR≈1) for NC→MCI across all biomarkers.
- **Baselines**: null (HR=1, dashed reference line) at each panel.
- **Dependencies**: E01

## E03: Dichotomized cut-off multistate Markov modeling (basic + fully adjusted)
- **Verifies**: C03, C04, C05, C06
- **Setup**:
  - Data: each biomarker dichotomized into high/low using predefined cut-offs (from a prior bootstrap/Youden-index procedure, ref. 9).
  - Model: same four-state multistate Markov model as E02, fit twice per biomarker — "basic" (adjusted for sex, education) and "fully adjusted" (further adjusted for chronic kidney disease, heart disease, cerebrovascular disease, anemia, obesity).
- **Procedure**:
  1. Classify each participant high/low per biomarker using the fixed cut-offs.
  2. Fit the multistate model per biomarker under each adjustment tier.
  3. Extract HR (95% CI) and transition/participant counts for each of the three transitions, per biomarker, per adjustment tier.
- **Metrics**: HR (95% CI) high vs. low, by transition and adjustment tier; number of observed transitions and participants per group.
- **Expected outcome**: Concordant direction/magnitude with the continuous-spline analysis (E02); attenuation of some associations (notably p-tau181-reversion) after full adjustment; no biomarker associated with NC→MCI under either adjustment tier.
- **Baselines**: "low" biomarker group as reference within each biomarker.
- **Dependencies**: E01, E02

## E04: Biomarker-combination count analysis (p-tau217, NfL, GFAP)
- **Verifies**: C07
- **Setup**:
  - Data: count (0, 1, 2, or 3) of elevated biomarkers among the three strongest univariate markers (p-tau217, NfL, GFAP), using the same dichotomization cut-offs as E03.
  - Model: multistate Markov model, fully adjusted (sex, education, chronic kidney disease, heart disease, cerebrovascular disease, anemia, obesity).
- **Procedure**:
  1. Classify each participant by the number of the three markers elevated at baseline.
  2. Fit the multistate model with this count (reference: none elevated) for each of the three transitions.
  3. Extract HR (95% CI) per count level, per transition, plus AD-dementia-specific HR for the three-vs-none contrast.
- **Metrics**: HR (95% CI) per elevated-biomarker count (one/two/three vs. none), by transition; transition/participant counts per group.
- **Expected outcome**: Monotonic or near-monotonic increase in MCI→dementia hazard, and decrease in MCI→NC (reversion) hazard, with increasing number of elevated biomarkers; no association with NC→MCI.
- **Baselines**: "none elevated" group as reference.
- **Dependencies**: E03

## E05: Pairwise biomarker combination analysis (p-tau217 × NfL)
- **Verifies**: C08
- **Setup**:
  - Data: 2×2 cross-classification of high/low p-tau217 and high/low NfL.
  - Model: multistate Markov model (adjustment tier as reported in text; underlying Supplementary Tables S12-S13 not in provided input).
- **Procedure**:
  1. Cross-classify participants into low/low (reference), high-NfL-only, high-p-tau217-only, and both-high groups.
  2. Fit the multistate model and extract HR (95% CI) for progression to all-cause dementia and to AD dementia, per group, relative to low/low.
- **Metrics**: HR (95% CI) per pairwise group, by dementia outcome type (all-cause vs. AD).
- **Expected outcome**: Highest hazard in the both-elevated group for both all-cause and AD dementia outcomes, exceeding either single-marker-elevated group.
- **Baselines**: low/low (both markers below cut-off) as reference.
- **Dependencies**: E04

## E06: Age-stratified subgroup analysis
- **Verifies**: C09
- **Setup**:
  - Strata: age <78 years (n=1283) vs. age ≥78 years (n=865), the same age break used to report Table 1.
  - Model: multistate Markov model with age-dependent (stratum-specific) biomarker HRs (Supplementary Tables S2-S3, not in provided input).
- **Procedure**:
  1. Fit biomarker-transition models allowing HRs to differ by age stratum.
  2. Compare MCI→dementia and MCI→NC HR magnitudes across strata.
- **Metrics**: stratum-specific HR (95% CI) per biomarker, per transition (not available from provided input — directional comparison only).
- **Expected outcome**: Slightly stronger MCI→dementia associations in the younger (<78) stratum; mixed pattern for MCI reversion across strata.
- **Baselines**: cross-stratum comparison (no external baseline).
- **Dependencies**: E03

## E07: Sex-stratified subgroup analysis
- **Verifies**: C10
- **Setup**:
  - Strata: male vs. female.
  - Model: multistate Markov model with sex-specific biomarker HRs (Supplementary Tables S4-S5, not in provided input).
- **Procedure**:
  1. Fit biomarker-transition models separately (or with sex-interaction terms) by sex.
  2. Compare MCI→all-cause-dementia HR magnitude and CI overlap between sexes.
- **Metrics**: sex-specific HR (95% CI) per biomarker (not available from provided input — directional comparison only).
- **Expected outcome**: Numerically stronger MCI→all-cause-dementia associations in women, but with confidence intervals overlapping those in men (precluding a definitive sex-difference conclusion).
- **Baselines**: cross-sex comparison (no external baseline).
- **Dependencies**: E03

## E08: Sensitivity — exclude participants with baseline MCI
- **Verifies**: C11
- **Setup**:
  - Sample: analytic cohort minus the 381 participants with MCI at baseline.
  - Model: same multistate Markov model as E03, re-fit on the restricted sample (Supplementary Tables S6-S7, not in provided input).
- **Procedure**:
  1. Remove baseline-MCI participants (whose MCI duration prior to baseline was unknown).
  2. Re-fit the dichotomized-biomarker multistate model.
  3. Compare resulting HRs to the main-sample results (E03) for consistency.
- **Metrics**: re-fit HR (95% CI) per biomarker, per transition, vs. main-sample HR (not available from provided input — directional comparison only).
- **Expected outcome**: Most associations replicate; p-tau181 (MCI→dementia) and NfL/GFAP (MCI reversion) associations attenuate to non-significance while point estimates stay similar.
- **Baselines**: main-sample E03 results.
- **Dependencies**: E03

## E09: Sensitivity — inverse probability weighting for attrition
- **Verifies**: C12
- **Setup**:
  - Weights: derived from a logistic regression of sample retention on age, sex, education, number of chronic diseases, and biomarker levels.
  - Model: same multistate Markov model as E03, re-fit with IPW weights (Supplementary Tables S8-S9, not in provided input).
- **Procedure**:
  1. Estimate retention-probability weights via logistic regression.
  2. Re-fit the dichotomized-biomarker multistate model with IPW weighting.
  3. Compare weighted HRs to the main (unweighted) results.
- **Metrics**: IPW-weighted HR (95% CI) per biomarker, per transition, vs. main-sample HR (not available from provided input — directional comparison only).
- **Expected outcome**: Estimates consistent with the main (unweighted) results, indicating attrition bias does not materially distort the main findings.
- **Baselines**: main-sample E03 results.
- **Dependencies**: E03

## E10: Sensitivity — CIND operationalization instead of MCI
- **Verifies**: C13
- **Setup**:
  - Alternative case definition: cognitive impairment, no dementia (CIND) — same cognitive-domain z-score threshold as MCI but without the functional-independence requirement.
  - Model: same multistate Markov model as E03, re-fit using CIND in place of MCI as the intermediate state (underlying data stated as available upon request, not in provided input).
- **Procedure**:
  1. Reclassify the intermediate cognitive state using the CIND definition.
  2. Re-fit the four-state multistate model.
  3. Compare CIND-based HRs to the main MCI-based results.
- **Metrics**: CIND-based HR (95% CI) per biomarker, per transition, vs. MCI-based HR (not available from provided input — directional comparison only).
- **Expected outcome**: Results comparable to the main MCI-based analysis.
- **Baselines**: main MCI-based E03 results.
- **Dependencies**: E03
