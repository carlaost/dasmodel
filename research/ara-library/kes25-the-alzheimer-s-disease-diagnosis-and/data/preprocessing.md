# Preprocessing & Sample Processing

## Blood sample collection and processing
- **CSF cohort**: 8 mL K2-EDTA tubes; plasma centrifuged 2000 × g, 10 min, room temperature; CSF 1750 × g, 5 min, 4°C. Processed within 2 h. Plasma and CSF aliquoted, stored −80°C. Inclusion: ≥ 1 mL plasma + ≥ 500 µL matched CSF.
- **Amyloid PET cohort**: 4 mL K3-EDTA tubes; centrifuged 2000 × g, 10 min, 4°C; within 2 h; −80°C. Inclusion: ≥ 1 mL plasma.
- **CN-CKD cohort**: K2-EDTA tubes; 1000 × g, 10 min, room temperature; −80°C. Inclusion: aged < 60, CKD G1–G4, ≥ 250 µL plasma.
- **Handling experiments**: 8 mL K2-EDTA; 2000 × g, 10 min, room temperature; −80°C. 40 participants (10 per experiment); 2 excluded for incorrect processing at centrifugation.

## Assay preparation
- **Lumipulse**: thaw at RT, vortex briefly, centrifuge 2000 × g 10 min RT, pipette supernatant into Hitachi analyzer cups; run on Lumipulse G1200. Main cohorts in duplicate; pre-analytic experiments in singlicate. LLOQ 0.03 pg/mL (independently verified; CV < 10%).
- **ALZpath**: thaw at RT, vortex briefly, centrifuge 2000 × g 5 min RT; run on Simoa HD-X. Duplicates (main cohorts) / singlicate (pre-analytic experiments). LLOQ 0.06 pg/mL.

## AD-status derivation (labels)
- **CSF "amyloid only"** (primary): CSF Lumipulse Aβ42/Aβ40 ratio ≤ 0.065 → positive.
- **CSF "amyloid and p-tau"**: Aβ42/Aβ40 ≤ 0.065 AND p-tau181 ≥ 57 pg/mL.
- **Clinical AD status**: most recent clinical diagnosis confirmed via follow-up + CSF results.
- **Malmö**: Lumipulse CSF Aβ42/p-tau181 < 11.94 (Palmqvist et al.).
- **FDA**: Lumipulse CSF Aβ42/Aβ40 < 0.073.
- **Amyloid PET**: visual read positive (¹⁸F-florbetaben), plaque load scored 1/2/3.

## eGFR / CKD staging
- Serum-creatinine-based eGFR via CKD-EPI 2021 equation (race-free). Stages: G1 ≥ 90, G2 60–89, G3a 45–59, G3b 30–44, G4 15–29, G5 < 15 (mL/min/1.73 m²).

## Clinical severity staging
- MMSE cut-offs (NICE): 27–30 MCI, 21–26 mild AD dementia, ≤ 20 moderate/severe. ACE-III (amyloid PET cohort): 76–100 MCI, 59–75 mild, ≤ 58 moderate/severe. Applied within ±6 months (CSF) or ±1 year (PET) of blood sampling.

## Statistical preprocessing
- Continuous variables summarized as mean (SD) or median (IQR) per Shapiro–Wilk normality (data assumed non-normal → non-parametric tests). Pre-analytical p-tau217 expressed as relative % change vs baseline condition; p-tau217 log-transformed for CKD regression models.
