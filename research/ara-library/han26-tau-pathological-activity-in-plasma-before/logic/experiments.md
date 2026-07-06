# Experiments

Declarative analysis plans reconstructed from the Methods/Statistical Analysis section (PDF p.15–17). No exact numerical results are given here — exact values are in `evidence/`.

## E01: Concordance of VeraBIND Tau with tau-PET/amyloid status across A/T groups
- **Verifies**: C11, C12
- **Setup**:
  - Cohort: 145 participants (79 CU, 66 CI) with paired VeraBIND Tau, amyloid status (PET or CSF), and [18F]MK6240 tau-PET.
  - Grouping: four A/T groups — A-T-, A+T-, A+T+, A-T+ — cross-tabulated by clinical status (CU/CI).
  - System: VeraBIND Tau dichotomized at test result Score ≥1.0 (positive) vs <1.0 (negative).
- **Procedure**:
  1. Restrict to individuals with concordant PET results (A-T-, A+T+); tabulate VeraBIND Tau positivity rate within each group, overall and separately by clinical status.
  2. Compute overall accuracy of VeraBIND Tau against the concordant-group tau status.
  3. Restrict to individuals with discordant PET results (A+T-, A-T+); tabulate VeraBIND Tau positivity rate in each discordant group.
  4. Compare the two discordant-group positivity rates with a Fisher's Exact test.
  5. Review individual clinical/diagnostic profiles of any unexpected positives/negatives (e.g., non-AD tauopathy phenotypes).
- **Metrics**: % VeraBIND Tau positivity per A/T×clinical-status cell; overall accuracy in concordant groups; Fisher's Exact test p-value comparing discordant groups.
- **Expected outcome**:
  - VeraBIND Tau positivity should track tau-PET status (T+/T-) more closely than amyloid status (A+/A-) in the discordant groups, if the assay is specifically tau-driven rather than amyloid-driven.
  - Concordant-group accuracy should be high and comparable between CU and CI.
- **Baselines**: None (single-assay concordance description); implicitly benchmarked against amyloid status as an alternative explanatory variable.
- **Dependencies**: none

## E02: ROC/AUC comparison of VeraBIND Tau against other plasma biomarkers
- **Verifies**: C01, C02
- **Setup**:
  - Cohort: entire sample (n=145), with per-biomarker missing-data exclusions (pTau181: -3; pTau231: -27; Aβ42/Aβ40: -6).
  - Biomarkers compared: VeraBIND Tau, plasma pTau217, pTau181, pTau231, Aβ42/Aβ40 ratio.
  - Outcomes: (a) tau-PET positivity (Braak-like stage>0), (b) amyloid positivity (Centiloid≥20 or CSF Aβ42≤544 pg/mL).
- **Procedure**:
  1. Compute ROC curves and AUC for each biomarker against each binary outcome.
  2. Pairwise compare AUCs using DeLong tests, anchored on the best performer for each outcome.
  3. Repeat separately for the tau-PET outcome and the amyloid outcome.
- **Metrics**: AUC (with ROC curve); DeLong test z-statistic and p-value for each pairwise comparison.
- **Expected outcome**:
  - VeraBIND Tau is expected to have the largest AUC for tau-PET positivity.
  - Plasma pTau217 is expected to have the largest AUC for amyloid positivity, consistent with prior literature that pTau species better reflect amyloid than tau pathology.
- **Baselines**: Each biomarker serves as the other's baseline; pTau217 is the primary comparator (the best-established single plasma biomarker).
- **Dependencies**: none

## E03: Threshold-stratified diagnostic performance of VeraBIND Tau vs. pTau217
- **Verifies**: C01, C03
- **Setup**:
  - Cohort: entire sample (n=145), and CU (n=79) / CI (n=66) subgroups separately.
  - VeraBIND Tau: single threshold (Score ≥1.0).
  - pTau217: three literature-derived thresholds (0.142, 0.193, 0.256 pg/mL), each previously calibrated in an independent multicentric cohort for 95% sensitivity, balanced sensitivity/specificity, and 95% specificity (respectively) for amyloid-PET status.
  - Population priors for PPV/NPV: 60% tau-PET positivity prevalence in CI, 10% in CU (from an external meta-analysis).
- **Procedure**:
  1. For each of the four test/threshold combinations, cross-tabulate predicted vs. observed tau-PET status.
  2. Compute sensitivity, specificity, overall accuracy, with 95% confidence intervals, for the entire sample and each clinical subgroup.
  3. Compute PPV and NPV per clinical subgroup, substituting the external prevalence priors rather than the observed (enriched) sample prevalence.
- **Metrics**: Sensitivity, specificity, accuracy, PPV, NPV, each with 95% CI.
- **Expected outcome**: VeraBIND Tau is expected to show higher sensitivity, specificity, accuracy, and (especially) PPV than any pTau217 threshold, most notably in the CU subgroup where pTau217's accuracy is known to be weakest.
- **Baselines**: Plasma pTau217 at three clinically-derived thresholds.
- **Dependencies**: E02

## E04: Braak-stage-stratified comparison of biomarker levels and diagnostic performance
- **Verifies**: C04, C05, C06
- **Setup**:
  - Cohort: entire sample, stratified into Braak-like tau-PET stage groups: 0, 1–3 ("low"), 4–6 ("high"), and finer-grained single-stage groups (0, 1–2, 3, 4, 5, 6).
  - Covariates: age, sex, education (regression adjustment); Bonferroni correction for multiple comparisons.
- **Procedure**:
  1. Fit a regression model of VeraBIND Tau score (and, separately, pTau217 concentration) on Braak-stage group, adjusted for age/sex/education.
  2. Perform pairwise (Bonferroni-corrected) contrasts between Braak-stage groups (0 vs. 1–3, 0 vs. 4–6, 1–3 vs. 4–6).
  3. Within the low-Braak (1–3) subgroup, compute VeraBIND Tau and pTau217 (at each threshold) sensitivity and compare using McNemar's test; compute AUC for Braak 1–3 vs. 0 and compare using a DeLong test.
  4. Repeat the AUC/sensitivity comparison for the high-Braak (4–6) vs. 0 contrast.
- **Metrics**: Regression coefficients (b/β) with 95% CI and corrected p-values; sensitivity/positivity rate per stage group; AUC per stage contrast; McNemar χ² and DeLong z statistics.
- **Expected outcome**: VeraBIND Tau is expected to show a large, early step-up in score/positivity between Braak 0 and Braak 1–3 that does not further increase at Braak 4–6 (an early "on/off" signal), while pTau217 concentration is expected to increase mainly at Braak 4–6, remaining largely unchanged between Braak 0 and 1–3 (a later, dose-graded signal).
- **Baselines**: Plasma pTau217 at three thresholds.
- **Dependencies**: E02, E03

## E05: Regression of continuous entorhinal tau-PET signal on VeraBIND Tau and pTau217 in early-stage individuals
- **Verifies**: C07
- **Setup**:
  - Cohort: subset restricted to Braak-like tau-PET stage 0–3 (n=93).
  - Covariates: age, sex, education.
- **Procedure**:
  1. Fit a linear regression of entorhinal tau-PET SUVr on VeraBIND Tau score, adjusted for age/sex/education.
  2. Fit the analogous regression using plasma pTau217 concentration in place of VeraBIND Tau score.
  3. Compare the significance and effect size (β, 95% CI) of the two predictors.
- **Metrics**: Standardized/unstandardized regression coefficient (β) with 95% CI and p-value, per biomarker.
- **Expected outcome**: VeraBIND Tau is expected to significantly predict continuous entorhinal tau-PET signal restricted to this early-stage subset, while pTau217 is expected to show a weaker, non-significant association.
- **Baselines**: Plasma pTau217 concentration.
- **Dependencies**: E04

## E06: Cross-sectional correlation of VeraBIND Tau with cognition, tau-PET burden, and other plasma biomarkers
- **Verifies**: C08
- **Setup**:
  - Cohort: entire sample (n=145); repeated in the CU-only subsample (n=79).
  - Comparators: MMSE, episodic memory z-score, entorhinal and inferior-temporal tau-PET SUVr, plasma pTau217, pTau181, pTau231.
- **Procedure**:
  1. Compute age-adjusted Spearman's rank correlation coefficients between VeraBIND Tau score and each comparator, across the entire sample.
  2. Repeat the same set of correlations restricted to CU participants only.
  3. Note comparators with reduced sample size due to missing data (e.g., pTau231) and report the available n.
- **Metrics**: Age-adjusted Spearman's rho and p-value per comparator, per subgroup.
- **Expected outcome**: VeraBIND Tau score is expected to correlate significantly with cognitive performance and tau-PET burden in the entire sample; correlations with tau-PET/plasma markers (but not necessarily MMSE, given ceiling effects) are expected to remain significant when restricted to CU participants alone.
- **Baselines**: None (descriptive correlational analysis); implicitly benchmarks whether the CU-only association survives restriction of clinical range.
- **Dependencies**: none

## E07: Longitudinal correlation of annual VeraBIND Tau rate of change with disease-severity proxies
- **Verifies**: C09
- **Setup**:
  - Cohort: longitudinal subsample of 88 participants (58 CU, 30 CI) with 2–5 repeated VeraBIND Tau measurements (total 207 samples across the cohort), mean follow-up 1.72±0.94 years.
  - Comparators: cross-sectional entorhinal and inferior-temporal tau-PET SUVr, Braak-like tau-PET stage, episodic memory z-score, MMSE, plasma pTau217, pTau181, pTau231.
- **Procedure**:
  1. For each participant, fit a linear regression of VeraBIND Tau score on time to estimate an individual annual rate of change.
  2. Compute Spearman's rank correlations (age-adjusted) between each participant's annual rate of change and each cross-sectional comparator.
  3. Report available-n per comparator where missing data reduce the analytic sample (e.g., pTau231).
- **Metrics**: Age-adjusted Spearman's rho and p-value per comparator.
- **Expected outcome**: A steeper annual increase in VeraBIND Tau score is expected to associate with greater tau-PET burden, more advanced Braak-like stage, and worse cognitive scores, supporting the score's rate of change as a disease-progression-sensitive measure.
- **Baselines**: None (descriptive longitudinal correlational analysis).
- **Dependencies**: E06

## E08: Longitudinal test-retest / conversion analysis of VeraBIND Tau positivity status
- **Verifies**: C10
- **Setup**:
  - Cohort: same 88-participant longitudinal subsample as E07.
  - Definition: "conversion" = participant classified negative (Score<1.0) at an earlier timepoint and positive (Score≥1.0) at a later timepoint (including the timepoint closest to baseline tau-PET).
- **Procedure**:
  1. For each participant, classify each available VeraBIND Tau timepoint as positive/negative.
  2. Identify participants whose classification changed from negative to positive over follow-up ("converters").
  3. Tabulate the proportion of converters vs. participants who remained stably positive or stably negative throughout follow-up.
  4. Characterize the biological/clinical profile (A/T status, clinical group, Braak-like stage) of each converter.
- **Metrics**: Proportion of converters; proportion stably positive; proportion stably negative.
- **Expected outcome**: A minority of participants are expected to convert (consistent with genuine early biological change rather than assay noise), while the large majority are expected to remain stable across repeated measurements, supporting test-retest reproducibility.
- **Baselines**: None (descriptive stability analysis).
- **Dependencies**: E07
