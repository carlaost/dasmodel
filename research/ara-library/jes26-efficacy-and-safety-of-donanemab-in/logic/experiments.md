# Experiments (Analysis Plans)

Declarative analysis designs for a post-hoc secondary analysis of TRAILBLAZER-ALZ 2 (NCT04437511).
Directional only — exact numbers live in `evidence/`. "Experiment" here = a pre-specified
statistical analysis of trial data restricted to the EU-eligible subpopulation.

## E01: Clinical-scale efficacy via MMRM with conservative hybrid imputation
- **Verifies**: C01, C02, C04, C10
- **Setup**:
  - Population: EU-eligible subset of randomised TRAILBLAZER-ALZ 2 (APOE ε4 non-carriers/heterozygotes without superficial siderosis, anticoagulant use, or uncontrolled hypertension); placebo vs donanemab.
  - Data: iADRS, CDR-SB (and its six domains), ADAS-Cog13, ADCS-iADL, MMSE over 76 weeks.
  - System: Mixed model for repeated measures (MMRM); SAS 9.4.
- **Procedure**:
  1. Fit MMRM with factors treatment, visit, baseline tau category, pooled investigator, concomitant symptomatic treatment; covariates baseline age and baseline score; treatment-by-visit and baseline-score-by-visit interactions.
  2. Apply the EMA-required hybrid imputation for missing values: jump-to-reference (J2R) for missingness due to serious/severe/symptomatic ARIA or death, copy increment reference (CIR) for all other causes.
  3. Repeat without imputation (original methodology) for comparison.
  4. Compute adjusted mean change-from-baseline differences, 95% CIs (normal approximation), p values, and percent slowing (Delta method).
- **Metrics**: Adjusted mean CFB difference (scale units), 95% CI, p value, percent slowing (%).
- **Expected outcome**: Donanemab significantly slows decline on all five scales; effect is directionally consistent between imputation methods.
- **Baselines**: Internal placebo arm; original (no-imputation) methodology.
- **Dependencies**: none

## E02: Progression-risk analysis via Cox proportional hazards (CDR-G)
- **Verifies**: C03
- **Setup**:
  - Population: EU-eligible subset; placebo vs donanemab.
  - Data: Time to CDR-G progression (any increase at two consecutive visits) and to moderate/severe dementia (CDR-G ≥2 at two consecutive visits, baseline CDR-G ≤1).
  - System: Cox proportional hazards model; SAS 9.4.
- **Procedure**:
  1. Define progression events; count discontinuations due to death and ARIA as events (for the next-stage analysis).
  2. Fit Cox model stratified by pooled investigator and baseline tau level, with covariates age, AChEI/memantine use, and baseline clinical outcome score.
  3. Estimate hazard ratios, 95% CIs, and p values.
- **Metrics**: Hazard ratio, 95% CI, p value, number of events/n.
- **Expected outcome**: Donanemab reduces the hazard of progression to the next stage and to moderate dementia (HR < 1).
- **Baselines**: Internal placebo arm.
- **Dependencies**: none

## E03: Disease-stabilisation (no-progression) analysis via generalized mixed model
- **Verifies**: C05
- **Setup**:
  - Population: EU-eligible subset; placebo vs donanemab.
  - Data: Proportion with no CDR-SB progression (CFB ≤0) at 52 and 76 weeks.
  - System: Generalized mixed model.
- **Procedure**:
  1. Define "no progression" as CDR-SB CFB ≤0.
  2. Fit generalized mixed model with factors treatment, visit, treatment-by-visit interaction and covariates age, tau category, AChEI/memantine use, baseline clinical outcome score, and score-by-visit interaction.
  3. Estimate proportions with no progression, 95% CIs, and p values at 52 and 76 weeks.
- **Metrics**: Estimated percent with no progression (%), 95% CI, p value.
- **Expected outcome**: A greater proportion of donanemab than placebo participants show no progression at both timepoints.
- **Baselines**: Internal placebo arm.
- **Dependencies**: E01

## E04: Time-saved analysis via time-progression model for repeated measures
- **Verifies**: C06
- **Setup**:
  - Population: EU-eligible overall and EU-eligible low-medium tau subpopulations.
  - Data: CDR-SB trajectories over 76 weeks.
  - System: Time-progression model for repeated measures (as in Sims et al. [2]); some time-based analyses in R 4.3.0, with conservative hybrid imputation.
- **Procedure**:
  1. Estimate the difference in time for the placebo arm to reach the same CDR-SB change observed in the donanemab arm at end of the placebo-controlled period.
  2. Repeat for the low-medium tau subpopulation.
- **Metrics**: Time saved (months), 95% CI.
- **Expected outcome**: Donanemab delays CDR-SB progression by a positive number of months; delay is larger in the low-medium tau subpopulation.
- **Baselines**: Internal placebo arm.
- **Dependencies**: E01

## E05: Biomarker analysis (amyloid PET, amyloid clearance, plasma P-tau217) via MMRM
- **Verifies**: C07
- **Setup**:
  - Population: EU-eligible subset; placebo vs donanemab.
  - Data: Amyloid PET (Centiloids), amyloid clearance status (<24.1 CL) at weeks 24/52/76, plasma P-tau217 (log10).
  - System: MMRM; amyloid clearance percentages with Wilson score CIs and one-sample frequency test; SAS 9.4.
- **Procedure**:
  1. Fit MMRM for Centiloid CFB with treatment, visit, treatment-by-visit interaction, and covariates score, score-by-visit, age, tau category (hybrid imputation for amyloid CFB per Table 3 footnote).
  2. Compute proportion achieving amyloid clearance (<24.1 CL) at each timepoint with Wilson CIs.
  3. Analyse plasma P-tau217 CFB at each timepoint.
- **Metrics**: Adjusted mean CFB difference (CL), 95% CI, p value; % achieving clearance, 95% CI; P-tau217 log10 CFB difference, 95% CI.
- **Expected outcome**: Donanemab reduces amyloid plaque more than placebo; clearance rates rise across weeks 24→52→76; P-tau217 falls at all timepoints.
- **Baselines**: Internal placebo arm.
- **Dependencies**: none

## E06: Descriptive safety analysis
- **Verifies**: C08
- **Setup**:
  - Population: All EU-eligible participants exposed to study drug; placebo vs donanemab.
  - Data: TEAEs (MedDRA v25.1), deaths, SAEs, discontinuations, ARIA-E/ARIA-H (MRI or TEAE cluster), infusion-related reactions, radiographic severity, symptomatic status.
  - System: Descriptive summaries only (no inferential model).
- **Procedure**:
  1. Tabulate incidence (n, %) of each safety category by arm.
  2. Characterise ARIA-E/ARIA-H by seriousness, symptomatic status, and maximum radiographic severity.
  3. Compare EU-eligible any-ARIA incidence to the overall TRAILBLAZER-ALZ 2 population.
- **Metrics**: Incidence n (%) per category; comparison of any-ARIA rates.
- **Expected outcome**: ARIA burden is lower in the EU-eligible than the overall population; no ARIA-related deaths; most ARIA-E asymptomatic and mild-to-moderate.
- **Baselines**: Internal placebo arm; published overall-population rates [2].
- **Dependencies**: none

## E07: Long-term extension efficacy vs propensity-weighted external control
- **Verifies**: C09
- **Setup**:
  - Population: LTE non-carriers/heterozygotes, early-start (randomised donanemab) and delayed-start (randomised placebo, donanemab initiated in LTE) groups.
  - Data: CDR-G progression and amyloid over 154 weeks; untreated comparator drawn from ADNI.
  - System: Propensity-score weighting to balance baseline disease characteristics vs the ADNI external control (per Zimmer et al. [7]); Cox model for progression. Hybrid J2R/CIR imputation is NOT applied (not methodologically compatible with propensity reweighting).
- **Procedure**:
  1. Construct propensity-weighted ADNI external control (EU-eligible weighting not feasible — siderosis, anticoagulant use, BP not in ADNI).
  2. Compare treatment effect trajectory over 154 weeks vs external control.
  3. Compare early-start vs delayed-start progression risk (CDR-G) at 154 weeks.
- **Metrics**: Treatment-effect trajectory; relative risk of progression (%); amyloid clearance maintenance.
- **Expected outcome**: Increasing treatment effect over 154 weeks; early-start has lower progression risk than delayed-start; amyloid clearance maintained after treatment completion.
- **Baselines**: Propensity-weighted ADNI external control; delayed-start group.
- **Dependencies**: none

## E08: Robustness / consistency comparison across estimands and populations
- **Verifies**: C10
- **Setup**:
  - Population: EU-eligible (with and without hybrid imputation) and overall TRAILBLAZER-ALZ 2 population.
  - Data: CDR-SB and other clinical scales at week 76.
  - System: Reuse E01 outputs (both estimands) and published overall-population results [2].
- **Procedure**:
  1. Compare adjusted mean differences, p values, and percent slowing between conservative and original methodologies (Table 2).
  2. Compare EU-eligible CDR-SB slowing to the overall population estimate.
- **Metrics**: Percent slowing (%), direction, significance across methods and populations.
- **Expected outcome**: Estimates agree in direction and significance across imputation methods and are consistent with the overall population.
- **Baselines**: Original methodology; overall-population results.
- **Dependencies**: E01
