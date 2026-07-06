# Study Design (ADAPT stage 1)

ADAPT (Alzheimer's Disease Diagnosis and Plasma phospho-Tau217) is a UK multi-center study in
three stages. **Stage 1** (this paper) selects a plasma p-tau217 assay and derives clinical
cut-points; **Stage 2** will examine cut-point stability over time; **Stage 3** will be a
randomized controlled trial of disclosing plasma p-tau217 results to patients and clinicians in
community memory clinics (primary outcome: proportion of AD diagnoses) — a separate future study.

## Design type
Observational biomarker-validation study. Not itself a registered trial; no NCT/ISRCTN number is
stated. Reference-standard-defined cohorts are used to derive and externally validate diagnostic
cut-points for two commercial plasma p-tau217 assays.

## Cohorts

### 1. CSF cohort (derivation) — n = 257
- **Source**: symptomatic patients attending the cognitive clinic at UCL Hospitals NHS FT, National Hospital for Neurology and Neurosurgery (London), Aug 2017–Sep 2024, referred for lumbar puncture.
- **Ethics/consent**: Wolfson CSF study 12/0344 (NRES London Queen Square, Aug 2013, PI Schott).
- **Reference standard**: AD biomarker status positive if CSF Lumipulse Aβ42/Aβ40 ratio ≤ 0.065 ("amyloid only"). Sensitivity analyses used four further definitions (amyloid+p-tau; clinical AD status; Malmö Aβ42/p-tau181 < 11.94; FDA Aβ42/Aβ40 < 0.073).
- **Inclusion**: ≥ 1 mL stored EDTA plasma and ≥ 500 µL matched CSF.
- **Processing**: 8 mL K2-EDTA tubes; plasma centrifuged 2000 × g, 10 min, room temperature; CSF 1750 × g, 5 min, 4°C; processed within 2 h; stored −80°C.

### 2. Amyloid PET cohort (validation) — n = 76
- **Source**: patients attending the cognitive clinic at Imperial College Healthcare NHS Trust, Charing Cross Hospital (London), Aug 2020–Nov 2024, referred for amyloid PET.
- **Ethics/consent**: Imperial Amyloid PET Cohort Study 20/LO/0442 (NRES London Camden and Kings Cross, June 2020, PI Malhotra).
- **Reference standard**: amyloid PET visual read (¹⁸F-florbetaben; Siemens Biograph 64 PET/CT); amyloid load scored 1 = none, 2 = mild, 3 = significant, by two nuclear-medicine experts.
- **Inclusion**: ≥ 1 mL stored EDTA plasma.
- **Processing**: 4 mL K3-EDTA tubes; 2000 × g, 10 min, 4°C; within 2 h; −80°C. A subset (Apr–Jul 2025) contributed to the transport-temperature comparison.

### 3. CN-CKD cohort (renal-function analysis) — n = 58
- **Source**: cognitively normal patients with autosomal dominant polycystic kidney disease (ADPKD) at Royal Free London NHS FT, plasma sampled 2012–2018.
- **Ethics/consent**: Polycystic Kidney Disease (PKD) Biobank, sponsored by PKD Charity at Royal Free (05/Q0508/6).
- **Inclusion**: aged < 60 (expected < 20% background amyloid prevalence), CKD stages G1–G4, ≥ 250 µL stored EDTA plasma.
- **Processing**: K2-EDTA tubes; 1000 × g, 10 min, room temperature; −80°C.

### 4. Pre-analytical handling experiments — n = 40 (10 per experiment; 2 excluded)
- **Source**: cognitive neurology clinic, NHNN (London).
- **Ethics/consent**: Wolfson CSF study 12/0344 and Biomarkers and Genetics in Dementia study 03/N049 (NRES London, Apr 2003, PI Fox).
- **Processing**: 8 mL K2-EDTA; 2000 × g, 10 min, room temperature; −80°C. Four experiments varied pre-/post-centrifugation delays, storage temperatures, and freeze–thaw cycles (see experiments.md E06). Transport comparison used 10 amyloid-PET-cohort samples (E08).

## Assays
- **Lumipulse** G plasma p-tau217 immunoreaction cartridge kits on the Lumipulse G1200 automated platform (Fujirebio Europe); thaw, vortex, centrifuge 2000 × g 10 min RT; LLOQ 0.03 pg/mL (CV < 10%). Main cohorts in duplicate; pre-analytic experiments in singlicate. Selected as the clinical assay.
- **ALZpath** p-tau217 v2 kit on the Simoa HD-X platform (Quanterix); thaw, vortex, centrifuge 2000 × g 5 min RT; LLOQ 0.06 pg/mL. Main cohorts in duplicate; pre-analytic experiments in singlicate.

## Analysis workflow
1. Correlate/agree the two assays (Spearman rho; Passing–Bablok).
2. Fold-change AD vs non-AD (Wilcoxon signed-rank).
3. ROC/AUC per assay (95% CI); compare via DeLong; covariate models compared via AIC.
4. Derive dual cut-points (95% sensitivity lower; maximized/95% specificity upper) from the CSF cohort; quantify intermediate zone, NPV, PPV, accuracy.
5. Validate cut-points in the amyloid PET cohort; compare with external (Malmö, Figdore) cut-points.
6. Test pre-analytical stability (Friedman + Nemenyi), lot-to-lot (Spearman/Passing–Bablok), transport (Spearman), and CKD/BMI effects (Wilcoxon; multiple linear regression).

## Outputs / deployment
Lumipulse dual cut-points 0.153/0.422 pg/mL adopted in the UKAS-accredited Neuroimmunology and CSF
Laboratory (NHS), to be used in the ADAPT stage-3 RCT. A recommended sample-handling protocol was
derived for trial sites.
