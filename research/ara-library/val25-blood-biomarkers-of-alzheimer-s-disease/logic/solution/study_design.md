# Study Design

## Cohort and sampling
- **Source**: Swedish National study on Aging and Care in Kungsholmen (SNAC-K), an ongoing population-based longitudinal study (ref. 47).
- **Baseline enrollment**: 3363 randomly selected individuals aged 60+ from the Kungsholmen district of Stockholm (2001-2004), 73% participation rate.
- **Follow-up schedule**: every six years for participants <78 years old at baseline; every three years for participants ≥78 (p.6, Methods).
- **Analytic sample derivation**:
  1. Dementia-free at baseline: n=3123.
  2. Exclude missing baseline blood biomarker data: n=833 excluded → n=2290.
  3. Exclude dropouts with no follow-up assessment (142, 6.2%): → analytic n=2148 (Supplementary Fig. S2, not in provided input).
- **Ethics**: written informed consent (or proxy consent for cognitively impaired individuals); approved by the Regional Ethical Review Board in Stockholm across multiple protocol amendments (Dnrs listed p.6); Declaration of Helsinki followed; reported per STROBE guidelines (ref. 48).

## Exposure measurement: blood biomarkers
- Peripheral venous blood collected at baseline (fasting not compulsory); serum aliquots stored at −80°C at the Karolinska Institutet Bio Bank.
- Measured at the Affinity Proteomics Stockholm Unit (SciLifeLab) via Simoa (Quanterix) assays: Neuro 3-plex A Kit (Aβ40, Aβ42, t-tau), pTau-181 Advantage V2 Kit (p-tau181), ALZpath p-Tau-217 Advantage PLUS Kit (p-tau217), Neuro 2-plex B Kit (NfL, GFAP). 25 µL sample, 1:4 dilution, manufacturer protocol; concentrations derived via 4-parameter logistic curve fit (Quanterix SR-X software).
- Precision: within-run coefficient of variation (CV) computed on a triplicate SNAC-K serum pool plus two kit controls per plate; average CVs reported in Supplementary Table S14 (not in provided input).
- Below-detection-limit values imputed with single-value 0 (not-missing-at-random strategy): n=6 (Aβ42), 15 (p-tau181), 5 (p-tau217), 15 (t-tau).
- Analytic representations: (a) continuous z-scores modeled via restricted cubic splines (3 knots at 25th/50th/75th percentiles, median as reference); (b) high/low dichotomization using cut-offs imported from a prior bootstrapped Youden's-index procedure (ref. 9): 0.057 (Aβ42/40), 1.512 pg/mL (p-tau181), 0.134 pg/mL (p-tau217), 0.832 pg/mL (t-tau), 20.171 pg/mL (NfL), 142.515 pg/mL (GFAP).

## Outcome measurement: cognitive stages
- **MCI**: neuropsychological battery across 5 domains (executive function, episodic memory, visuospatial ability, language, perceptual speed); age-specific z-scored domain averages; MCI = ≤1.5 SD below age-specific mean in ≥1 domain + preserved function (≤1 impaired IADL, preserved basic ADLs) + no dementia diagnosis. Same procedure applied at follow-up visits using baseline cut-offs.
- **CIND** (alternative, sensitivity only): same cognitive threshold, without the functional-independence requirement.
- **All-cause / AD dementia**: DSM-IV (all-cause) and NINCDS-ADRDA (AD) criteria; three-step diagnostic adjudication (examining physician → blinded second physician → senior neurologist on disagreement); clinical-chart/death-register review for deceased participants without a diagnosis.
- **Vital status**: Swedish Cause of Death Register.

## Covariates
- Education: elementary / high school / university-or-higher.
- Global cognition: Mini-Mental State Examination (MMSE), descriptive only.
- Chronic diseases: physician-ascertained via clinical evaluation, records, self-report, labs, medication use; coded per ICD-10 (ref. 53). Specific comorbidities used in the "fully adjusted" model: chronic kidney disease, heart disease, cerebrovascular disease, anemia, obesity (chosen because a companion study, ref. 42, found these associated with AD blood biomarker levels).

## Statistical model
- **Structure**: four-state parametric multistate Markov model — NC, MCI, dementia, death (absorbing) — fit with the R `msm` package (ref. 56), accounting for interval censoring.
- **Time scale**: age (not calendar/study time).
- **Baseline hazard**: Gompertz distribution (ref. 55).
- **Transition constraints**: direct NC→dementia disallowed (assumed to pass through unobserved MCI); MCI↔NC is the only reversible transition pair; unknown-MCI-status-but-alive-and-dementia-free participants are modeled as uncertain between {NC, MCI}; dementia diagnosed at death is assumed to have onset between last assessment and death.
- **Adjustment tiers**: "basic" (sex, education) and "fully adjusted" (basic + chronic kidney disease, heart disease, cerebrovascular disease, anemia, obesity).
- **Exposure specifications fit**: (1) single continuous biomarker (spline) per model; (2) single dichotomized biomarker per model; (3) count of elevated biomarkers among {p-tau217, NfL, GFAP} (0-3) per model; (4) pairwise cross-classification of p-tau217 × NfL.
- **Subgroup/sensitivity variants**: age-stratified (<78 vs. ≥78) models; sex-stratified models; baseline-MCI-excluded re-fit; IPW-weighted re-fit (weights from logistic regression on age, sex, education, chronic-disease count, biomarker levels); CIND-substituted re-fit.
- **Software**: R version 4.3.1 (R Foundation for Statistical Computing); `msm` package for multistate model fitting.

## Reporting
- Results reported per the STROBE statement for observational studies (ref. 48).
