# Experiments — TRAILBLAZER-ALZ 4

Directional verification plans reflecting the trial's prespecified analyses. NO exact numerical results here (those live in `evidence/`). "Experiment" = a prespecified statistical test of a trial endpoint. All analyses ran in SAS v9.4 (two-sided α = 0.05); primary and key secondary endpoints were adjusted for multiplicity via a gated hierarchy.

## E01: Co-primary — proportion reaching AP clearance at 6 months (logistic regression)
- **Verifies**: C01, C02
- **Setup**:
  - Design: 76-week, randomized, open-label, parallel-group, active-comparator phase 3 trial; 31 US sites; NCT05108922.
  - Arms: donanemab (700 mg IV Q4W ×3 doses, then 1400 mg Q4W) vs aducanumab per US ADUHELM label; randomized 1:1, stratified by amyloid level and APOE ε4 status.
  - Population: early symptomatic AD (MCI or mild dementia), age 50–85, MMSE 20–30, CDR-GS 0.5/1.0, amyloid-positive by florbetapir PET. Analysis sets: overall population and low–medium tau subpopulation.
  - Endpoint: proportion reaching AP clearance (< 24.1 CL, florbetapir PET) at 6 months.
- **Procedure**:
  1. Fit logistic regression with treatment, APOE ε4 carrier status, baseline amyloid level, baseline age as fixed effects.
  2. Summarize treatment effects as estimated probabilities per arm plus odds ratios and 100·(1−α)% CIs.
  3. Test in the overall population and, separately, the low–medium tau subpopulation.
- **Metrics**: Proportion (%) reaching clearance per arm; P value for superiority.
- **Expected outcome**: Higher clearance proportion with donanemab than aducanumab in both analysis sets (superiority).
- **Baselines**: Aducanumab arm (active comparator).
- **Dependencies**: none

## E02: Secondary — AP clearance at 12 and 18 months (longitudinal logistic regression)
- **Verifies**: C03
- **Setup**: Same populations/arms as E01; endpoint = proportion reaching AP clearance (< 24.1 CL) at 12 and 18 months, overall and low–medium tau.
- **Procedure**:
  1. Estimate clearance proportions from a longitudinal logistic regression model.
  2. Compare donanemab vs aducanumab at each timepoint.
- **Metrics**: Proportion (%) cleared per arm/timepoint; P value.
- **Expected outcome**: Donanemab clearance proportion exceeds aducanumab at 12 and 18 months in the overall population and low–medium tau subpopulation.
- **Baselines**: Aducanumab arm.
- **Dependencies**: E01

## E03: Key secondary — time to AP clearance (Kaplan–Meier, log-rank)
- **Verifies**: C04
- **Setup**: Time-to-event = interval from first dose to the PET scan showing AP clearance; participants not clearing censored at final PET.
- **Procedure**:
  1. Estimate cumulative clearance with Kaplan–Meier.
  2. Compare arms with a 2-sided unstratified log-rank test.
  3. Report median time to clearance with CI per arm.
- **Metrics**: Median time-to-clearance (days) per arm; number of clearance events; log-rank P value.
- **Expected outcome**: Shorter median time to clearance with donanemab than aducanumab.
- **Baselines**: Aducanumab arm.
- **Dependencies**: E01

## E04: Key secondary — mean absolute/percent change in amyloid PET (ANCOVA / MMRM)
- **Verifies**: C05
- **Setup**: Change from baseline in florbetapir PET CL and percent change, at 6/12/18 months, overall and low–medium tau.
- **Procedure**:
  1. 6-month analysis: ANCOVA with treatment as fixed effect; covariates APOE ε4 carrier status, baseline amyloid level, baseline age (single postbaseline PET within 6 months).
  2. 12- and 18-month analyses: MMRM with treatment, time, treatment-by-time interaction as fixed effects; same covariates.
  3. Apply identical models to the percent-change endpoint.
- **Metrics**: LS mean absolute change (CL) and percent change from baseline per arm/timepoint; P value.
- **Expected outcome**: Greater reduction (more negative change) with donanemab than aducanumab at every timepoint.
- **Baselines**: Aducanumab arm.
- **Dependencies**: E01

## E05: Exploratory — plasma biomarker trajectories (MMRM)
- **Verifies**: C06
- **Setup**: Plasma p-tau217, p-tau181, GFAP, NfL (log-transformed) at scheduled visits (weeks 24/52/76), overall population and low–medium tau.
- **Procedure**:
  1. Fit MMRM with treatment, visit, treatment-by-visit interaction as fixed categorical effects; baseline biomarker level and baseline age as continuous covariates.
  2. Estimate adjusted mean change differences vs aducanumab per timepoint.
- **Metrics**: LSM change from baseline per arm/visit; adjusted mean difference vs aducanumab with 95% CI; P value.
- **Expected outcome**: Larger early reductions with donanemab for p-tau217/p-tau181/GFAP (significant early, attenuating by 18 months); no significant treatment effect on NfL.
- **Baselines**: Aducanumab arm.
- **Dependencies**: E04

## E06: Safety — adverse events, ARIA incidence, and time-to-ARIA-E
- **Verifies**: C07, C08
- **Setup**: Safety analysis set (all participants exposed to treatment). AEs of special interest: ARIA-E, ARIA-H, infusion-related reactions (class effects). ARIA identified via TEAE cluster + centrally read MRI.
- **Procedure**:
  1. Tabulate SAEs, TEAEs, treatment/study discontinuations, and AEs of special interest by arm and frequency.
  2. Characterize ARIA-E radiographic severity and symptomatic status.
  3. Estimate time to first ARIA-E with Kaplan–Meier; compare arms with 2-sided log-rank test.
- **Metrics**: AE incidence n (%) per arm; ARIA-E/H incidence; time-to-first-ARIA-E KM and P value.
- **Expected outcome**: Comparable overall tolerability; ARIA incidence not higher with the faster/deeper-clearing agent (donanemab); no significant arm difference in time-to-ARIA-E.
- **Baselines**: Aducanumab arm.
- **Dependencies**: none
