# Experiments / Analyses

Declarative verification plans (directional only; exact numbers live in `evidence/`). In this
retrospective diagnostic-accuracy study, "experiments" are the statistical analyses applied to the
187-patient CCUG cohort with a CSF-biomarker reference standard.

## E01: Single-cut-off ROC diagnostic accuracy of the three p-tau assays
- **Verifies**: C01, C02, C03
- **Setup**:
  - Cohort: 187 CCUG memory-clinic patients (AD n = 103, non-AD n = 84); reference standard = CSF biomarkers (n = 180) or amyloid-PET (n = 7)
  - Analytes/platforms: Elecsys p-tau217, Elecsys p-tau181, APOE-ε4 on Roche cobas pro e801; Lumipulse p-tau217, Aβ42, Aβ40 on Fujirebio LUMIPULSE G1200
  - Software: SPSS 29.0
- **Procedure**:
  1. Compute ROC AUC (with 95% CI) for each biomarker vs AD status.
  2. Derive optimal single cut-off by maximizing the Youden index; report sensitivity, specificity, accuracy, PPV, NPV, TP/TN.
  3. Compare AUCs pairwise with the DeLong test.
- **Metrics**: AUC (unitless), sensitivity/specificity/PPV/NPV (%), cut-off (pg/mL), DeLong p-value.
- **Expected outcome**:
  - Elecsys p-tau217 achieves high AUC (> 0.90).
  - Elecsys p-tau217 ≈ Lumipulse p-tau217 (non-significant DeLong).
  - Elecsys p-tau217 > Elecsys p-tau181 (significant DeLong).
- **Baselines**: Elecsys p-tau181; Lumipulse p-tau217; Lumipulse p-tau217/Aβ42 and /(Aβ42/Aβ40).
- **Dependencies**: none

## E02: Two-cut-off (grey-zone) classification
- **Verifies**: C06
- **Setup**: Same cohort/analytes as E01; thresholds set at 95% sensitivity (lower) and 95% specificity (upper).
- **Procedure**:
  1. For each biomarker, define lower/upper cut-offs at 95% sensitivity / 95% specificity.
  2. Classify patients below lower as negative, above upper as positive, in-between as intermediate.
  3. Report % intermediates, accuracy, PPV, NPV, TP/TN, and AD/non-AD composition of the grey zone.
- **Metrics**: % intermediate, accuracy/PPV/NPV (%), likelihood ratios.
- **Expected outcome**: Intermediate proportion differs by assay; Lumipulse p-tau217 gives the smallest grey zone among single biomarkers, Elecsys p-tau181 the largest.
- **Baselines**: comparison across the three biomarkers and ratio combinations.
- **Dependencies**: E01

## E03: Added value of APOE-ε4 (logistic regression)
- **Verifies**: C04
- **Setup**: Same cohort; APOE-ε4 carrier status (plasma proteotyping) as binary covariate.
- **Procedure**:
  1. Fit logistic regression predicting AD status with each plasma biomarker ± APOE-ε4.
  2. Compare AUCs with and without APOE-ε4 (DeLong).
  3. Recompute the two-cut-off intermediate proportion for the combined models; stratify PPV/NPV by carrier status.
- **Metrics**: AUC change, DeLong p-value, % intermediate change, PPV/NPV by carrier status.
- **Expected outcome**: Adding APOE-ε4 raises AUC (largest and significant for Elecsys p-tau217, modest for Lumipulse) and reduces the grey zone; carriers gain PPV, non-carriers gain NPV.
- **Baselines**: biomarker-only models.
- **Dependencies**: E01, E02

## E04: Aβ42 / Aβ42-40 adjustment on the Fujirebio platform
- **Verifies**: C05
- **Setup**: Fujirebio subset with Aβ42 and Aβ40 available (n = 182); Lumipulse p-tau217, p-tau217/Aβ42, p-tau217/(Aβ42/Aβ40).
- **Procedure**:
  1. Compare AUC of Lumipulse p-tau217 vs p-tau217/Aβ42 and p-tau217/(Aβ42/Aβ40) (DeLong).
  2. Recompute two-cut-off intermediate proportions, PPV, NPV, accuracy.
- **Metrics**: AUC change, DeLong p-value, % intermediate change.
- **Expected outcome**: No significant AUC gain from Aβ42/Aβ42-40 adjustment; modest reduction in intermediate proportion.
- **Baselines**: Lumipulse p-tau217 alone; Elecsys p-tau217.
- **Dependencies**: E01, E02

## E05: Method comparison of the two p-tau217 assays
- **Verifies**: C07
- **Setup**: Paired Elecsys vs Lumipulse p-tau217 measurements (n = 181 for regression; 5/187 below LOQ); MedCalc 15.6.1.
- **Procedure**:
  1. Passing–Bablok regression (slope, intercept, 95% CI) and Pearson correlation.
  2. Bland–Altman analysis of relative differences (mean, ±1.96 SD limits of agreement).
- **Metrics**: slope, intercept, correlation coefficient, mean relative difference (%), limits of agreement (%).
- **Expected outcome**: Strong correlation but proportional (slope > 1) and systematic (intercept > 0) bias; wide Bland–Altman limits — assays not interchangeable in absolute value.
- **Baselines**: line of identity (slope 1, intercept 0).
- **Dependencies**: none

## E06: Analytical validation (precision, linearity, LLOQ)
- **Verifies**: C10
- **Setup**: Commercial QC solutions (PreciControl pT181p and Phospho-Tau 217P PreciControl, Roche RUO); CLSI EP15-A3 protocol; dilution series in triplicate.
- **Procedure**:
  1. Estimate imprecision (CV) at multiple concentrations, 5 measurements/day over 5 non-consecutive days.
  2. Assess linearity by diluting a high-concentration sample (triplicate; mean = correct result).
  3. Determine LLOQ at a predefined 20% CV specification.
- **Metrics**: CV (%), linearity range (pg/mL), LLOQ (pg/mL).
- **Expected outcome**: Low imprecision (single-digit % CV), linearity to sub-0.3 pg/mL, low LLOQ — analytically fit for purpose.
- **Baselines**: comparison to published precision for SIMOA/MSD/CLEIA.
- **Dependencies**: none

## E07: Clinical cofactor influence on Elecsys p-tau217 (linear regression)
- **Verifies**: C09, C08
- **Setup**: Cohort with covariates age, sex, eGFR, Fazekas grade, lobar microbleeds/CAA, diagnostic group, baseline MoCA; Spearman correlation and multivariable linear regression.
- **Procedure**:
  1. Regress baseline Elecsys p-tau217 on each clinical cofactor.
  2. Report standardized β and p-value per cofactor; compare p-tau217 across eGFR categories.
  3. Perform MoCA-adjusted logistic regression for each biomarker vs AD status.
- **Metrics**: β coefficients, p-values, odds ratios (95% CI).
- **Expected outcome**: Significant association with diagnostic group and MoCA; no significant association with age, sex, renal function, Fazekas, or CAA; biomarkers remain associated with AD after MoCA adjustment.
- **Baselines**: unadjusted associations.
- **Dependencies**: E01

## E08: Longitudinal association of baseline p-tau217 with cognitive decline
- **Verifies**: C08
- **Setup**: AD subset with longitudinal MoCA follow-up (n = 69, median 2.1 years); linear mixed-effects models with random intercepts and slopes.
- **Procedure**:
  1. Model MoCA over time with baseline p-tau217 × time interaction.
  2. Adjust for age, sex, and baseline MoCA.
- **Metrics**: interaction coefficient and p-value; baseline association.
- **Expected outcome**: Higher baseline p-tau217 associated with lower baseline MoCA and a (non-significant) trend toward faster decline.
- **Baselines**: none (single-group longitudinal model).
- **Dependencies**: E07

## E09: Discordant-CSF subgroup and sensitivity analysis
- **Verifies**: C11
- **Setup**: 16 excluded discordant-CSF cases (15 A+T−N−, 1 other); comparison to AD and non-AD groups.
- **Procedure**:
  1. Compare plasma p-tau measures of discordant cases vs AD and vs non-AD groups.
  2. Apply the primary Elecsys p-tau217 single cut-off to classify discordant cases.
  3. Sensitivity analysis: reclassify discordant cases as AD and recompute AUC, sensitivity, specificity, optimal cut-offs.
- **Metrics**: group-difference p-values, % above/below cut-off, changes in AUC/sensitivity/specificity/cut-off.
- **Expected outcome**: Discordant cases resemble non-AD on average but are heterogeneous (subset above threshold); reclassifying as AD changes performance only modestly, supporting robustness of main cut-offs.
- **Baselines**: primary AD vs non-AD analysis.
- **Dependencies**: E01
