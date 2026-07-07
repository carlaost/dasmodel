# Experiments (Analysis Plans)

Declarative analysis designs for the 78-week long-term extension (LTE) of TRAILBLAZER-ALZ 2
(NCT04437511), bringing total observation to 154 weeks (~3 years). Directional only — exact
numbers live in `evidence/`. "Experiment" here = a pre-specified statistical analysis of trial
data plus an external comparator cohort (ADNI). All analyses are exploratory and not controlled
for multiplicity (§2.5).

## E01: Early-start CDR-SB efficacy vs weighted ADNI external control via MMRM
- **Verifies**: C01
- **Setup**:
  - Population: Early-start group (randomized to donanemab in the placebo-controlled period) who received ≥1 LTE infusion, vs a propensity-score-weighted ADNI external control cohort.
  - Data: CDR-SB change from baseline at months 0, 6, 12, 18, 24, 30, 36 (weeks aligned to LTE visit schedule).
  - System: Mixed model for repeated measures (MMRM), using ADNI propensity weights.
- **Procedure**:
  1. Estimate propensity score weights for the ADNI cohort (ATT estimand, inverse probability weighting, generalized linear model) using the early-start reference population.
  2. Check covariate balance (standardized mean difference <0.10) and trim extreme weights at the 95th percentile.
  3. Fit MMRM with treatment, age, APOE ε4 status, baseline CDR-SB, baseline ADAS-Cog13, screening MMSE, visit, and visit-by-treatment / visit-by-baseline-CDR-SB interactions.
  4. Compute LS mean treatment differences (early-start vs weighted ADNI) and 95% CIs at each visit through 36 months.
- **Metrics**: Adjusted mean (LS mean) CDR-SB change-from-baseline difference, 95% CI, sample sizes / effective sample size (ESS) at each timepoint.
- **Expected outcome**: The early-start vs ADNI CDR-SB difference is negative (donanemab arm progresses less) and its magnitude increases over the 36-month follow-up.
- **Baselines**: Weighted external ADNI cohort; (validation step) TRAILBLAZER-ALZ 2 internal placebo arm vs weighted ADNI cohort through 76 weeks.
- **Dependencies**: none

## E02: Delayed-start CDR-SB efficacy vs weighted ADNI external control via MMRM
- **Verifies**: C02
- **Setup**:
  - Population: Delayed-start group (randomized to placebo, started donanemab at LTE entry) who received ≥1 LTE infusion, vs a propensity-score-weighted ADNI external control cohort (separately weighted using the placebo-arm subset that entered the LTE as the reference population).
  - Data: CDR-SB change from baseline, aligned to the delayed-start group's donanemab-exposure timeline.
  - System: MMRM, same covariate specification as E01, using delayed-start-specific ADNI weights.
- **Procedure**:
  1. Re-estimate propensity weights for the ADNI cohort using the placebo-arm-entering-LTE reference population.
  2. Fit MMRM for CDR-SB change from baseline through 76 weeks after donanemab initiation (month 36 on the overall trial timeline).
  3. Compute LS mean treatment differences and 95% CIs at each visit.
- **Metrics**: Adjusted mean CDR-SB change-from-baseline difference, 95% CI, N / ESS at each timepoint.
- **Expected outcome**: The delayed-start vs ADNI CDR-SB difference is negative and increases in magnitude as donanemab exposure accumulates, though the total exposure/observation window is shorter than for early-start.
- **Baselines**: Weighted external ADNI cohort.
- **Dependencies**: none

## E03: CDR-SB efficacy in the subset of early-start participants who met treatment course completion criteria by 52 weeks
- **Verifies**: C03
- **Setup**:
  - Population: Early-start participants who met amyloid-based treatment course completion criteria by week 52 of the placebo-controlled period, vs the same weighted ADNI external control used in E01.
  - Data: CDR-SB change from baseline through 36 months.
  - System: Same MMRM specification as E01, restricted to this subgroup.
- **Procedure**:
  1. Identify the subset of the early-start group meeting completion criteria by 52 weeks.
  2. Repeat the E01 MMRM analysis on this subgroup vs the weighted ADNI cohort.
- **Metrics**: Adjusted mean CDR-SB change-from-baseline difference, 95% CI, N / ESS.
- **Expected outcome**: The subgroup's treatment effect is directionally consistent with, and of similar magnitude to, the overall early-start effect (E01), supporting durability of benefit after early treatment completion.
- **Baselines**: Weighted external ADNI cohort; overall early-start result (E01).
- **Dependencies**: E01

## E04: Early- vs delayed-start progression-risk analysis via Cox proportional hazards (CDR-G)
- **Verifies**: C04
- **Setup**:
  - Population: Early-start vs delayed-start groups (as defined for the LTE), all participants with CDR-G assessments.
  - Data: Time to CDR-G progression (increase in CDR-G score at two consecutive visits, assessed every 3 months) over the 154-week combined placebo-controlled + LTE period.
  - System: Cox proportional hazards model, stratified by pooled investigator and baseline tau level.
- **Procedure**:
  1. Define the progression event as a CDR-G increase confirmed at two consecutive visits; use the date of the first such visit as the event time.
  2. Fit the Cox model with covariates age, CDR-G score, and acetylcholinesterase inhibitor/memantine use, and group (early- vs delayed-start) as a fixed factor.
  3. Estimate the hazard ratio, 95% CI, and p value.
- **Metrics**: Hazard ratio, 95% CI, p value; cumulative percentage progressing over time.
- **Expected outcome**: Early-start participants show a lower hazard of CDR-G progression than delayed-start participants (HR < 1).
- **Baselines**: Delayed-start group as the comparator.
- **Dependencies**: none

## E05: Cumulative (AUC) CDR-SB benefit analysis, early-start vs weighted ADNI cohort
- **Verifies**: C05
- **Setup**:
  - Population: Early-start group vs the weighted ADNI cohort (as in E01).
  - Data: CDR-SB change-from-baseline trajectories across the 78-week LTE period.
  - System: Area-under-the-curve (AUC) computation using trapezoidal-rule weights.
- **Procedure**:
  1. Compute the AUC of CDR-SB change from baseline for the early-start group and for the weighted ADNI cohort over the LTE period.
  2. Estimate the LS mean difference between the two AUCs and derive an average treatment difference per unit time.
  3. Test for statistical significance.
- **Metrics**: AUC difference (LS mean), average treatment difference (points), p value.
- **Expected outcome**: The early-start AUC shows a superior (larger) cumulative benefit than the ADNI cohort's AUC.
- **Baselines**: Weighted external ADNI cohort.
- **Dependencies**: E01

## E06: Time-saved analysis (back-calculation method), early- and delayed-start vs ADNI
- **Verifies**: C06
- **Setup**:
  - Population: Early-start group (at 3 years) and delayed-start group (at end of LTE, 1.5 years after starting donanemab), each vs its respective weighted ADNI cohort.
  - Data: CDR-SB trajectories between 24 and 36 months.
  - System: Time-progression back-calculation from the MMRM-fitted trajectories (E01, E02).
- **Procedure**:
  1. Fit the ADNI cohort and treated-group CDR-SB trajectories between 24 and 36 months.
  2. Back-calculate the ADNI timepoint at which the ADNI cohort's mean CDR-SB change matches the mean 36-month (or end-of-LTE) treated-group value.
  3. Express the difference between that back-calculated ADNI timepoint and the treated group's actual timepoint as "months saved."
- **Metrics**: Time saved (months).
- **Expected outcome**: Both early- and delayed-start treatment show a positive number of months saved versus the ADNI trajectory, with early-start saving more time than delayed-start.
- **Baselines**: Weighted external ADNI cohort.
- **Dependencies**: E01, E02

## E07: Amyloid PET reduction and clearance analysis via MMRM, early- vs delayed-start
- **Verifies**: C07, C08
- **Setup**:
  - Population: Early-start and delayed-start groups (separately), all participants with amyloid PET assessments during the LTE.
  - Data: Amyloid PET Centiloid (CL) change from baseline; clearance status (<24.1 CL) at weeks 24/52/76 post-donanemab-initiation.
  - System: MMRM with treatment, visit, treatment-by-visit interaction as fixed factors; score, score-by-visit interaction, age, and tau category as covariates.
- **Procedure**:
  1. Fit MMRM for CL change from baseline, separately timed for early-start (through week 76) and delayed-start (through week 154, i.e., 76 weeks post-initiation).
  2. Compute LS mean (SE) CL reduction at the matched 76-week-post-initiation timepoint for each group.
  3. Compute the percentage of participants achieving amyloid clearance (<24.1 CL) at weeks 24/52/76 post-initiation for each group.
- **Metrics**: LS mean (SE) CL reduction; % achieving clearance (with n/N) at each timepoint.
- **Expected outcome**: Amyloid reduction and clearance trajectories are closely similar between early- and delayed-start groups when aligned to donanemab-exposure time, regardless of when treatment started.
- **Baselines**: Cross-group comparison (early- vs delayed-start); no external/placebo comparator needed since decline is compared to each group's own baseline.
- **Dependencies**: none

## E08: Amyloid reaccumulation-rate estimation via cross-study exposure-response model
- **Verifies**: C10
- **Setup**:
  - Population: Early-start participants who met treatment course completion criteria by 52 weeks (amyloid trajectory followed through 154 weeks); combined with data from three earlier donanemab studies.
  - Data: Mean amyloid CL trajectory from week 0 through 154 weeks for the 52-week-completer subset; historical exposure-response data from a phase 1b study (NCT02624778), TRAILBLAZER-ALZ (phase 2; NCT03367403), and TRAILBLAZER-EXT (phase 2 LTE parts B/C; NCT04640077).
  - System: Existing donanemab exposure-response model (previously reported methods [11],[12]), updated with this LTE's data.
- **Procedure**:
  1. Plot mean CL values over time for the 52-week-completer subset (0 to 154 weeks).
  2. Incorporate LTE reaccumulation data into the pre-existing cross-study exposure-response model.
  3. Estimate a pooled amyloid reaccumulation rate (CL/year).
- **Metrics**: Mean (SD) amyloid CL at 154 weeks; reaccumulation rate (CL/year).
- **Expected outcome**: The 52-week-completer subset's mean amyloid level remains below the 24.1 CL amyloid-negativity cutoff at 154 weeks, and the estimated reaccumulation rate is comparable to independently reported natural (untreated) amyloid accumulation rates.
- **Baselines**: Independently published natural amyloid accumulation rate estimates ([14],[15]).
- **Dependencies**: E07

## E09: Descriptive tracking of treatment-course-completion timing across the placebo-controlled period and LTE
- **Verifies**: C09
- **Setup**:
  - Population: Early-start participants continuing donanemab in the LTE; delayed-start participants receiving donanemab in the LTE; compared descriptively to placebo-controlled-period donanemab-treated participants.
  - Data: Proportion meeting amyloid-based treatment course completion criteria at each assessment point (24/52/76 weeks in the placebo-controlled period; 102/130/154 weeks, i.e., 24/52/76 weeks post-donanemab-initiation, in the LTE).
  - System: Descriptive tabulation (no inferential model).
- **Procedure**:
  1. Tabulate n/N and % meeting completion criteria at each LTE assessment point for early-start continuers and for delayed-start LTE-donanemab recipients.
  2. Compare these proportions, aligned by donanemab-exposure duration, to the published placebo-controlled-period completion rates.
- **Metrics**: % meeting completion criteria (n/N) at each aligned exposure-duration timepoint.
- **Expected outcome**: Completion-criteria rates at a given donanemab-exposure duration are similar whether that exposure occurred during the placebo-controlled period or the LTE.
- **Baselines**: Placebo-controlled-period completion rates (17.1%/46.6%/69.2% at 24/52/76 weeks).
- **Dependencies**: E07

## E10: Descriptive safety analysis by treatment-sequence group during the LTE
- **Verifies**: C11
- **Setup**:
  - Population: All participants receiving ≥1 infusion during the LTE, stratified into three treatment-sequence groups: donanemab→placebo (early-start switchers, N=393), donanemab→donanemab (early-start continuers, N=157), placebo→donanemab (delayed-start, N=657).
  - Data: Deaths, SAEs, TEAEs, study/treatment discontinuations due to AE, and AEs of special interest (ARIA-E, ARIA-H, headache, infusion-related reaction, superficial siderosis, cerebral microhemorrhage, vomiting, nausea, macrohemorrhage), plus an ARIA-overview breakdown (any ARIA, any SAE of ARIA, symptomatic ARIA-E/H, SAE of ARIA-E/H).
  - System: Descriptive summaries only (no inferential model); AEs based on MRI or TEAE-cluster reporting where noted.
- **Procedure**:
  1. Tabulate n (%) for each AE category by treatment-sequence group (Table 1).
  2. Compare event frequencies within the LTE to previously reported placebo-controlled-period donanemab safety data [2].
- **Metrics**: Incidence n (%) per category per group.
- **Expected outcome**: No new categories of AE emerge; event frequencies are broadly consistent with (often lower than) the placebo-controlled-period donanemab safety profile, particularly for participants who have discontinued to placebo or continued at longer cumulative exposure.
- **Baselines**: Previously reported placebo-controlled-period donanemab-treated safety profile [2].
- **Dependencies**: none

## E11: ARIA time-course and post-discontinuation risk analysis
- **Verifies**: C12
- **Setup**:
  - Population: All participants exposed to donanemab (any point in the trial); subgroup of early-start participants who met treatment course completion criteria by 52 weeks, followed after switching to placebo.
  - Data: Time to first ARIA-E event (treatment period + 57 days); new ARIA events (MRI or new/worsening AE) in 6-month intervals starting 58 days after the last donanemab dose; participant-years at risk for OAIR calculation.
  - System: Descriptive time-to-event and interval-incidence analysis; OAIR = (participants with ≥1 AE of a category × 100) ÷ participant-years at risk.
- **Procedure**:
  1. Plot cumulative incidence of first ARIA-E event across weeks of donanemab exposure for all exposed participants.
  2. Tabulate ARIA-E and ARIA-H incidence within sequential 6-month intervals after each participant's last donanemab dose.
  3. For the 52-week-completer subgroup, tabulate any-ARIA/ARIA-E/ARIA-H incidence after switching to placebo and compute OAIRs.
  4. Compare these OAIRs to the OAIRs for participants who received placebo throughout the placebo-controlled period.
- **Metrics**: Cumulative incidence of first ARIA-E event (by week); ARIA-E/ARIA-H incidence per 6-month post-discontinuation interval; OAIR (per 100 participant-years).
- **Expected outcome**: ARIA-E incidence is front-loaded (concentrated in the first 24 weeks of exposure) and declines toward low, stable rates after treatment discontinuation, converging toward placebo-period OAIRs.
- **Baselines**: Placebo-controlled-period placebo-arm OAIRs.
- **Dependencies**: E10
