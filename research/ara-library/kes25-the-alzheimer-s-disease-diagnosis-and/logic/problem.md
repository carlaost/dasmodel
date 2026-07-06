# Problem Specification

## Observations

### O1: An accurate blood test would reduce reliance on invasive/expensive AD diagnostics
- **Statement**: AD diagnosis is typically formulated using clinical assessment plus molecular tools (CSF Aβ/p-tau or amyloid PET). A blood test would reduce the need for invasive CSF sampling and/or expensive amyloid PET and improve accessibility of early, accurate diagnosis.
- **Evidence**: §1 Background; refs 1,2.
- **Implication**: Motivates translation of plasma p-tau217 into clinical pathways.

### O2: Plasma p-tau217 is a specific, high-performing AD biomarker
- **Statement**: Plasma tau phosphorylated at threonine-217 (p-tau217) discriminates AD neuropathology from other neurological diseases with higher diagnostic accuracy than other plasma biomarkers and comparable performance to CSF/PET standards.
- **Evidence**: §1 Background; refs 3–10; systematic review (Research in Context, ref 4).
- **Implication**: p-tau217 is the leading blood biomarker candidate for AD diagnosis.

### O3: Multiple commercial p-tau217 assays exist but need clinical cut-points
- **Statement**: The Lumipulse automated platform (Fujirebio) and the ALZpath assay on the Simoa HD-X platform (Quanterix) both show high performance for differentiating AD from non-AD, but clinical cut-points must be established and evaluated to integrate them into diagnostic pathways and minimize misclassification.
- **Evidence**: §1 Background; refs 5,6,16–19.
- **Implication**: Cut-point derivation/validation is the concrete gap this study addresses.

### O4: Pre-analytical factors and comorbidities may confound plasma p-tau217
- **Statement**: Sample handling (delays, storage temperatures, freeze–thaw cycles, transport), assay kit lot variability, and comorbidities such as chronic kidney disease (CKD) and body mass index (BMI) could affect measured plasma p-tau217 concentrations.
- **Evidence**: §1, §2.1.1, §2.4; refs 21,22,33–35,44–48.
- **Implication**: These influences must be characterized before clinical deployment.

## Gaps

### G1: No validated clinical cut-points for UK NHS deployment of plasma p-tau217
- **Statement**: Clinically applicable cut-points for the Lumipulse and ALZpath p-tau217 assays, validated against both CSF and amyloid PET reference standards, were not established for a UK memory-service population.
- **Caused by**: O1, O2, O3
- **Existing attempts**: Externally derived cut-points (Palmqvist/Malmö ref 25; Figdore ref 16; Arranz ref 5) from other cohorts/definitions.
- **Why they fail**: External cut-points may not transfer across cohorts defined by different reference amyloid biomarkers; performance (sensitivity, NPV, accuracy) degrades when applied outside the derivation cohort.

### G2: Uncharacterized influence of pre-analytical handling, lot variability, and comorbidities
- **Statement**: The stability of plasma p-tau217 to pre-analytical handling/transport and kit lot, and the impact of CKD and BMI, were not established for the specific assays and protocol to be used in the planned ADAPT stage-3 trial.
- **Caused by**: O4
- **Existing attempts**: Prior stability studies (refs 33–35,42,43) on differing assays/panels.
- **Why they fail**: Assay- and protocol-specific confirmation was needed to define a sample-handling protocol for trial sites and to interpret results in renally impaired patients.

## Key Insight
- **Insight**: A **dual cut-point** approach (a lower cut-point tuned to 95% sensitivity and an upper cut-point tuned to maximized/95% specificity, with an intermediate "indeterminate" zone between) can translate a plasma p-tau217 assay across cohorts defined by different reference amyloid biomarkers while preserving accuracy, NPV, and PPV.
- **Derived from**: O2, O3, G1
- **Enables**: Deriving cut-points in a CSF-defined cohort and validating them in an independent amyloid-PET-defined cohort, quantifying the trade-off as the proportion of indeterminate results.

## Assumptions
- A1: CSF Aβ42/Aβ40 ratio ≤ 0.065 (Lumipulse, "amyloid only" definition) is a valid reference standard for AD biomarker status for cut-point derivation.
- A2: Amyloid PET visual read is a valid independent reference standard for validation.
- A3: The symptomatic memory-clinic populations sampled are representative enough for cut-points to be applied clinically in specialist memory services (explicitly flagged as a limitation for other settings/populations).
- A4: A ±10% relative change from baseline is the threshold for a clinically significant pre-analytical effect (chosen following prior publications, refs 33–35).
- A5: eGFR is computed with the race-free CKD-EPI 2021 creatinine equation (ref 27); CKD staged G1–G5.
