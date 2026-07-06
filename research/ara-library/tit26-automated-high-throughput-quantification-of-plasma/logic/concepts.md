# Concepts

## Plasma p-tau217 (phosphorylated tau 217)
- **Notation**: p-tau217
- **Definition**: Tau protein phosphorylated at threonine 217, measured in blood plasma. Among blood-based AD biomarkers it is the most accurate marker of AD pathology, rising with amyloid/tau pathophysiology.
- **Boundary conditions**: Absolute concentrations are assay-specific (Elecsys ECLIA vs Lumipulse CLEIA differ; see Passing–Bablok/Bland–Altman). Interpreted against assay-specific cut-offs.
- **Related concepts**: Plasma p-tau181, Elecsys platform, Lumipulse platform, AUC.

## Plasma p-tau181 (phosphorylated tau 181)
- **Notation**: p-tau181
- **Definition**: Tau phosphorylated at threonine 181, measured in plasma. An earlier-generation AD blood biomarker; FDA-cleared (Elecsys, Oct 2025) as a rule-out test for cognitive decline in primary care.
- **Boundary conditions**: Lower discriminative accuracy than p-tau217 for AD vs non-AD (AUC 0.903 vs 0.939 here).
- **Related concepts**: p-tau217, rule-out test, negative predictive value.

## APOE-ε4 carrier status (plasma proteotyping)
- **Notation**: APOE-ε4
- **Definition**: Presence of at least one apolipoprotein E ε4 allele. Here inferred from blood via the Elecsys APOE-ε4 plasma proteotyping assay, yielding carrier vs non-carrier status (not direct genotyping).
- **Boundary conditions**: Used as a binary covariate in logistic regression; plasma proteotyping shows high agreement with genotyping but genetic-risk disclosure ethics apply.
- **Related concepts**: PPV, NPV, grey zone.

## Aβ42/40 ratio (amyloid-β 42/40)
- **Notation**: Aβ42/Aβ40
- **Definition**: Ratio of amyloid-β 1-42 to amyloid-β 1-40 concentrations; a marker of cerebral amyloidosis. Lower ratios indicate amyloid pathology. Combined with p-tau217 (as p-tau217/Aβ42 or p-tau217/(Aβ42/Aβ40)) to attempt classification improvement.
- **Boundary conditions**: Measured on the Fujirebio Lumipulse platform (subset n = 182); incremental diagnostic value over p-tau217 alone was small in this cohort.
- **Related concepts**: p-tau217, CSF reference standard.

## Area under the ROC curve (AUC)
- **Notation**: AUC
- **Definition**: Area under the receiver operating characteristic curve; probability that a randomly chosen AD case has a higher biomarker value than a randomly chosen non-AD case. 0.5 = chance, 1.0 = perfect discrimination.
- **Boundary conditions**: Reported with 95% CI; compared across assays using the DeLong test.
- **Related concepts**: DeLong test, Youden index, sensitivity, specificity.

## Youden index
- **Notation**: J = sensitivity + specificity − 1
- **Definition**: Criterion for selecting an optimal single diagnostic cut-off — the threshold that maximizes (sensitivity + specificity − 1).
- **Boundary conditions**: Used here to derive the optimal single cut-off for each biomarker and combination.
- **Related concepts**: single cut-off, sensitivity, specificity.

## Two-cut-off strategy / grey (intermediate) zone
- **Notation**: —
- **Definition**: A classification scheme with two thresholds — a lower cut-off at 95% sensitivity and an upper cut-off at 95% specificity — creating an intermediate ("grey") zone of indeterminate results between clearly normal and clearly abnormal.
- **Boundary conditions**: Intermediate proportion is assay-dependent (19.9% Elecsys p-tau217, 11.9% Lumipulse p-tau217, 33.2% Elecsys p-tau181); BBM workgroup recommends 15–20%. Intermediate patients need confirmatory CSF/PET.
- **Related concepts**: Youden index, likelihood ratio, BBM workgroup criteria.

## DeLong test
- **Notation**: —
- **Definition**: Non-parametric statistical test for comparing two (correlated) ROC AUCs from the same samples.
- **Boundary conditions**: Used for pairwise AUC comparisons between assays and between models with/without APOE-ε4 or Aβ42.
- **Related concepts**: AUC, logistic regression.

## Passing–Bablok regression
- **Notation**: —
- **Definition**: A non-parametric regression method for method comparison that estimates a slope and intercept (with CIs) between two measurement methods without assuming a distribution of measurement error.
- **Boundary conditions**: Slope ≠ 1 indicates proportional bias; intercept ≠ 0 indicates systematic bias. Performed in MedCalc.
- **Related concepts**: Bland–Altman analysis, method comparison, harmonization.

## Bland–Altman analysis
- **Notation**: —
- **Definition**: Plot of the difference between two methods against their mean, with mean bias and limits of agreement (mean ± 1.96 SD). Here differences are expressed as relative (%).
- **Boundary conditions**: Wide limits of agreement (−27.2% to 144.6%; up to 59% discrepancy) indicate the assays are not interchangeable in absolute value.
- **Related concepts**: Passing–Bablok regression, method comparison.

## CSF biomarker reference standard / AT(N) framework
- **Notation**: A/T/N
- **Definition**: Classification of AD pathology using cerebrospinal-fluid biomarkers of amyloid (A: Aβ42, Aβ42/40 ratio), tau phosphorylation (T: p-tau181), and neurodegeneration (N: total tau). Used here as the reference standard defining AD vs non-AD.
- **Boundary conditions**: Reference-lab cut-offs: Aβ42/Aβ40 ≤ 0.070, Aβ42 ≤ 722 pg/mL, p-tau181 ≥ 50 pg/mL, total tau ≥ 403 pg/mL. Discordant profiles (e.g. A+T−N−) excluded from primary analysis.
- **Related concepts**: discordant CSF profile, amyloid-PET.

## Lower limit of quantification (LLOQ)
- **Notation**: LLOQ / LoQ
- **Definition**: Lowest analyte concentration measurable with acceptable precision, defined here at a predefined 20% CV specification. Samples below LLOQ are interpreted using the LLOQ value.
- **Boundary conditions**: 0.32 pg/mL (Elecsys p-tau181), 0.10 pg/mL (Elecsys p-tau217); 5/187 samples fell below the p-tau217 LOQ.
- **Related concepts**: precision (CV), linearity, CLSI EP15-A3.

## Montreal Cognitive Assessment (MoCA)
- **Notation**: MoCA
- **Definition**: Brief global cognitive screening test used here as the baseline cognitive measure and the longitudinal cognitive outcome in mixed-effects models.
- **Boundary conditions**: Limited sensitivity to subtle within-subject change; may show floor effects in AD — longitudinal findings are exploratory.
- **Related concepts**: cognitive decline, linear mixed-effects model.
