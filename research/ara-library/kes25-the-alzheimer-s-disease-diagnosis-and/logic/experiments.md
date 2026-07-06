# Experiments (Analysis Plans)

Directional plans only — no exact numbers (those live in `evidence/`). "Experiment" here
generalizes to the statistical analyses and study designs that test each diagnostic claim.

## E01: Assay diagnostic accuracy vs CSF reference (ROC)
- **Verifies**: C01, C02
- **Setup**:
  - Cohort: CSF cohort of symptomatic memory-clinic patients (UCL/NHNN), AD status = CSF Aβ42/Aβ40 ratio ≤ 0.065 ("amyloid only")
  - Assays: Lumipulse G1200 (Fujirebio) and ALZpath Simoa HD-X (Quanterix), measured blinded in duplicate
  - Reference: CSF Lumipulse Aβ42/Aβ40 (G1200 immunoassay)
- **Procedure**:
  1. Measure plasma p-tau217 with both assays.
  2. Assess correlation between assays (Spearman rho) and agreement (Passing–Bablok regression, slope/intercept CIs vs identity).
  3. Compute median fold-change AD vs non-AD per assay (Wilcoxon signed-rank).
  4. Fit logistic regression models (p-tau217 alone) and compute ROC AUC with 95% CI per assay.
  5. Compare assay AUCs (DeLong test).
- **Metrics**: Spearman rho; fold-change (unitless ratio); AUC (95% CI); DeLong P.
- **Expected outcome**:
  - Both assays achieve high AUC; assay AUCs not significantly different.
  - Lumipulse shows a larger AD-vs-non-AD fold-change than ALZpath.
- **Baselines**: Age+sex-only logistic model.
- **Dependencies**: none

## E02: Fold-change and accuracy vs amyloid PET reference
- **Verifies**: C02, C04
- **Setup**:
  - Cohort: independent amyloid PET cohort (Imperial), AD status = amyloid PET visual read (¹⁸F-florbetaben, Siemens Biograph 64 PET/CT)
  - Assays: Lumipulse and ALZpath p-tau217
- **Procedure**:
  1. Measure plasma p-tau217 with both assays.
  2. Correlate assays (Spearman rho); compute fold-change AD vs non-AD.
  3. ROC analysis of each assay against PET visual read; compute AUC (95% CI).
- **Metrics**: Spearman rho; fold-change; AUC (95% CI).
- **Expected outcome**: AUCs directionally lower than in the CSF cohort; Lumipulse fold-change again exceeds ALZpath.
- **Baselines**: Age+sex-only model.
- **Dependencies**: E01

## E03: Derivation of dual clinical cut-points in the CSF cohort
- **Verifies**: C03, C10
- **Setup**:
  - Cohort: CSF cohort, "amyloid only" definition
  - Assay: Lumipulse (primary) and ALZpath
- **Procedure**:
  1. From the ROC curve, derive a lower cut-point at 95% sensitivity and an upper cut-point at maximized (and 95%) specificity — the dual cut-point approach.
  2. Compute intermediate-zone proportion, NPV (lower), PPV (upper), and accuracy for definitively classified individuals (95% CI via binomial).
  3. Search for a cut-point pair keeping intermediate proportion < 20% at ≥ 90% sensitivity/specificity.
  4. Repeat metrics under alternative AD definitions (amyloid+p-tau, clinical, Malmö, FDA).
  5. Apply externally derived Malmö cut-points to the cohort and compare sensitivity/NPV/accuracy.
- **Metrics**: cut-point values (pg/mL); sensitivity/specificity (%); intermediate zone (%); NPV, PPV, accuracy (%, 95% CI).
- **Expected outcome**: A dual cut-point pair maintaining high sensitivity/specificity with a modest intermediate zone; within-cohort cut-points outperform external Malmö cut-points on sensitivity/NPV/accuracy.
- **Baselines**: External Malmö cut-points; Figdore cut-points.
- **Dependencies**: E01

## E04: Validation of CSF-derived cut-points in the amyloid PET cohort
- **Verifies**: C04
- **Setup**: Amyloid PET cohort; apply CSF-cohort-derived Lumipulse cut-points and ALZpath cut-points.
- **Procedure**:
  1. Apply CSF-derived cut-points to PET-cohort p-tau217 values.
  2. Compute intermediate-zone proportion, NPV, PPV, accuracy against PET visual read.
  3. Also derive within-PET-cohort cut-points and apply Figdore external cut-points for comparison; build confusion matrices vs PET status.
- **Metrics**: intermediate zone (%); NPV, PPV, accuracy (%, 95% CI).
- **Expected outcome**: Intermediate proportion exceeds 20% (higher than CSF-defined); accuracy remains high for definitively classified individuals.
- **Dependencies**: E03

## E05: Covariate contribution to diagnostic models
- **Verifies**: C05
- **Setup**: Both cohorts; logistic regression models adding age, sex, serum creatinine, and BMI to the p-tau217 model.
- **Procedure**:
  1. Fit base model (age+sex) and p-tau217 models with/without covariates.
  2. Compare AUCs (DeLong test) and model fit (AIC; reduction ≥ 20 deemed significant).
- **Metrics**: AUC (95% CI); DeLong P; ΔAIC.
- **Expected outcome**: Adding covariates does not significantly improve AUC over p-tau217 alone.
- **Dependencies**: E01

## E06: Pre-analytical sample handling stability
- **Verifies**: C06
- **Setup**:
  - Participants: recruited under Wolfson CSF (12/0344) and Biomarkers & Genetics in Dementia (03/N049) studies; n = 40 (10 per experiment; 2 excluded for incorrect processing).
  - Assays: Lumipulse and ALZpath (singlicate).
- **Procedure**: Four experiments — (1) pre-centrifugation delay at room temperature (30 min baseline vs 1 h vs 3 h); (2) pre-centrifugation delay at 2–8°C (30 min vs 3 h vs 24 h); (3) post-centrifugation delay/storage across temperatures and durations (no delay to 2 weeks at RT/2–8°C/−20°C); (4) freeze–thaw cycles (1 baseline vs 2, 3, 4). Express p-tau217 as relative % change vs baseline; Friedman test with Nemenyi post hoc.
- **Metrics**: median relative change (%) vs baseline; Friedman P; per-subject CV.
- **Expected outcome**: Median relative change stays within ±10% across all conditions on both assays (some statistically significant but clinically small differences may occur).
- **Dependencies**: none

## E07: Lumipulse kit lot-to-lot variability
- **Verifies**: C07
- **Setup**: Subset of n = 30 CSF-cohort samples tested across four Lumipulse kit lots (v1: 4128, 5066; v2: 5084, 5086).
- **Procedure**: Correlate p-tau217 across lots (Spearman rho, pairwise); Passing–Bablok regression vs identity; count classification discordances relative to dual cut-points.
- **Metrics**: Spearman rho; regression slope/intercept CIs; number of discordant classifications.
- **Expected outcome**: Strong cross-lot correlation; few discordances, not attributable to within-lot variation.
- **Dependencies**: E03

## E08: Transport temperature comparison
- **Verifies**: C08
- **Setup**: 10 samples from the amyloid PET cohort; post-centrifugation intermediate storage at −20°C (Bio-Freeze transport, −20 to 0°C) vs −80°C (dry-ice transport).
- **Procedure**: Correlate Lumipulse p-tau217 between transport conditions (Spearman rho, Passing–Bablok) and test for systematic bias.
- **Metrics**: Spearman rho; regression bias.
- **Expected outcome**: Excellent correlation, no systematic bias — sub-zero transport comparable to −80°C.
- **Dependencies**: none

## E09: Effect of renal function impairment (CN-CKD)
- **Verifies**: C09
- **Setup**: Cohort of 58 cognitively normal ADPKD/CKD (stage 1–4) individuals aged < 60 (PKD Biobank, 05/Q0508/6); Lumipulse p-tau217.
- **Procedure**:
  1. Plot p-tau217 by CKD stage vs CSF-cohort AD and non-AD groups (linear and log10).
  2. Apply CSF-derived cut-points; count proportions in low/intermediate/high zones.
  3. Test difference between AD/non-AD and each CKD group (Wilcoxon signed-rank).
  4. Multiple linear regression of log-transformed p-tau217 on serum creatinine / CKD stage / BMI, adjusted for age, sex, cohort.
- **Metrics**: median (IQR) p-tau217 by group (pg/mL); proportion in each zone (%); regression association / P.
- **Expected outcome**: p-tau217 rises with CKD stage into the intermediate zone but rarely to AD-positive levels; no significant independent CKD association after adjustment.
- **Dependencies**: E03
