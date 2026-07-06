# Concepts

## Plasma phospho-tau217 (p-tau217)
- **Notation**: p-tau217
- **Definition**: Tau protein phosphorylated at threonine residue 217, measured in blood plasma. A specific, high-performing blood-based biomarker for Alzheimer's disease neuropathology; concentrations reported in pg/mL.
- **Boundary conditions**: Diagnostic utility requires appropriate high pre-test probabilities (specialist memory-service populations here). Concentrations can be elevated by reduced renal function (≤ CKD-3a).
- **Related concepts**: Lumipulse assay, ALZpath assay, dual cut-point, AD biomarker status

## Dual cut-point approach
- **Notation**: (lower cut-point, upper cut-point) — e.g., (0.153, 0.422) pg/mL
- **Definition**: A two-threshold scheme in which a lower cut-point is set for high sensitivity (e.g., 95%) and an upper cut-point for high specificity (e.g., 95% or maximized); results below the lower cut-point are "low" (non-AD), above the upper cut-point are "high" (AD), and between the two are "intermediate/indeterminate."
- **Boundary conditions**: Trade-off is quantified by the proportion of individuals in the intermediate zone; the study also sought cut-point combinations keeping the intermediate proportion < 20% while maintaining ≥ 90% sensitivity/specificity.
- **Related concepts**: intermediate (indeterminate) zone, sensitivity, specificity, NPV, PPV

## Intermediate (indeterminate) zone
- **Notation**: —
- **Definition**: The range of plasma p-tau217 values lying between the lower and upper cut-points, for which the assay does not return a definitive AD/non-AD classification. Reported as a percentage of the cohort.
- **Boundary conditions**: CSF-defined = 19.4% (Lumipulse); PET-defined = 34.2%. NPV/PPV/accuracy metrics are computed on those receiving a definitive classification (excluding the intermediate zone).
- **Related concepts**: dual cut-point, negative/positive predictive value

## AD biomarker status (reference standards)
- **Notation**: —
- **Definition**: Ground-truth AD classification used to derive/validate cut-points. Primary definition = CSF "amyloid only": Lumipulse CSF Aβ42/Aβ40 ratio ≤ 0.065 (positive). Independent validation definition = amyloid PET visual read. Sensitivity analyses used additional definitions: "amyloid and p-tau" (Aβ42/Aβ40 ≤ 0.065 AND p-tau181 ≥ 57 pg/mL), "clinical AD status," "Malmö" (Aβ42/p-tau181 < 11.94), and "FDA" (Aβ42/Aβ40 < 0.073).
- **Boundary conditions**: Definitions yield different AD-positive counts (e.g., CSF cohort: 159 amyloid-only vs 170 FDA); cut-point performance varies by definition.
- **Related concepts**: p-tau217, amyloid PET, CSF Aβ42/Aβ40 ratio

## Lumipulse G p-tau217 assay
- **Notation**: —
- **Definition**: Fully automated chemiluminescent enzyme immunoassay for plasma p-tau217 on the Lumipulse G1200 platform (Fujirebio); capture antibody RD85 mAb, detector binds mid-region tau. Lower limit of quantification (LLOQ) 0.03 pg/mL (independently verified by the laboratory, CV < 10%).
- **Boundary conditions**: Run in singlicate (pre-analytic experiments) or duplicate (main cohorts); samples quantifiable above LLOQ.
- **Related concepts**: ALZpath assay, p-tau217, lot-to-lot variability

## ALZpath p-tau217 assay
- **Notation**: —
- **Definition**: Single-molecule array (Simoa) immunoassay for plasma p-tau217 on the Quanterix HD-X platform (ALZpath v2 kit); proprietary capture mAb, detector binds N-terminal tau. LLOQ 0.06 pg/mL.
- **Boundary conditions**: Comparator assay; not selected as the clinical assay owing to smaller fold-change and larger intermediate proportion.
- **Related concepts**: Lumipulse assay, p-tau217, Simoa HD-X

## Pre-analytical handling factors
- **Notation**: —
- **Definition**: Sample-processing variables tested for their effect on measured p-tau217: pre-centrifugation delay (room temperature; 2–8°C), post-centrifugation delay/storage temperature and duration, freeze–thaw cycles, and transport temperature. Effects expressed as percentage relative change from a baseline condition.
- **Boundary conditions**: A ±10% relative change is treated as the clinically significant threshold; four experiments with n = 10 each.
- **Related concepts**: p-tau217, robustness, lot-to-lot variability

## CKD stage / eGFR (CKD-EPI 2021)
- **Notation**: eGFR (mL/min/1.73 m²)
- **Definition**: Chronic kidney disease staging based on estimated glomerular filtration rate computed with the race-free CKD-EPI 2021 creatinine equation: G1 ≥ 90, G2 60–89, G3a 45–59, G3b 30–44, G4 15–29, G5 < 15.
- **Boundary conditions**: CN-CKD cohort spanned stages G1–G4, aged < 60; ≤ CKD-3a (eGFR < 60) associated with p-tau217 elevation into the intermediate zone.
- **Related concepts**: p-tau217, confounders, serum creatinine

## Fold-change (AD vs non-AD)
- **Notation**: —
- **Definition**: Ratio of the median plasma p-tau217 concentration in AD participants to that in non-AD participants within a cohort; a measure of an assay's dynamic separation between groups.
- **Boundary conditions**: Tested for group difference with a Wilcoxon signed-rank test; larger fold-change (Lumipulse) implies clearer separation.
- **Related concepts**: Lumipulse assay, ALZpath assay, diagnostic accuracy
