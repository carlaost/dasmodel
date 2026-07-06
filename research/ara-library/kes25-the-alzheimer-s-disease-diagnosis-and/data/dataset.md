# Datasets (Cohorts)

All data are UK clinical cohorts with **controlled / on-request access** (verified, sources.yaml).
No open accessions (GEO/SRA/EGA/Dryad/figshare) exist. Requests: qualified academic investigators,
proposal approval + signed data access agreement, to a.keshavan@ucl.ac.uk.

## 1. CSF cohort (derivation)
- **Provenance**: UCLH NHS FT, National Hospital for Neurology and Neurosurgery cognitive clinic, London; sampled Aug 2017–Sep 2024.
- **Ethics/consent**: Wolfson CSF study 12/0344 (NRES London Queen Square, Aug 2013, PI Schott). Written informed consent/assent.
- **Size**: n = 257 (153 male, 59.5%; mean age 63.3, SD 7.3). AD-positive (CSF Aβ42/Aβ40 ≤ 0.065): 159 (61.9%).
- **Variables**: plasma p-tau217 (Lumipulse, ALZpath); CSF Aβ42/Aβ40, p-tau181; clinical diagnosis; MMSE; serum creatinine/eGFR/CKD stage (n = 62, 24.1%); BMI (n = 151, 58.8%); age, sex, ethnicity.
- **Reference standard**: CSF Lumipulse Aβ42/Aβ40 ratio ≤ 0.065 ("amyloid only"); alt definitions: amyloid+p-tau, clinical, Malmö, FDA.
- **Access**: request.

## 2. Amyloid PET cohort (validation)
- **Provenance**: Imperial College Healthcare NHS Trust, Charing Cross Hospital cognitive clinic, London; Aug 2020–Nov 2024 (subset Apr–Jul 2025 for transport study).
- **Ethics/consent**: Imperial Amyloid PET Cohort Study 20/LO/0442 (NRES London Camden and Kings Cross, June 2020, PI Malhotra).
- **Size**: n = 76 (34 male, 44.7%; mean age 68.3, SD 8.6). Amyloid PET visual-read positive: 48 (63.2%).
- **Variables**: plasma p-tau217 (Lumipulse, ALZpath); amyloid PET visual read + plaque load score (none/mild/significant); clinical diagnosis; MMSE/ACE-III; serum creatinine/eGFR/CKD (n = 46, 60.5%); age, sex, ethnicity. BMI not available.
- **Reference standard**: amyloid PET visual read (¹⁸F-florbetaben, Siemens Biograph 64 PET/CT).
- **Access**: request.

## 3. CN-CKD cohort (renal-function analysis)
- **Provenance**: Royal Free London NHS FT; ADPKD patients, plasma 2012–2018.
- **Ethics/consent**: PKD Biobank, sponsored by PKD Charity at Royal Free, 05/Q0508/6 (identifier null in sources.yaml).
- **Size**: n = 58 (32 male, 55.2%; mean age 44.4, SD 8.5; aged < 60). CKD-1: 11 (19.0%), CKD-2: 15 (25.9%), CKD-3a: 16 (27.6%), CKD-3b: 9 (15.5%), CKD-4: 7 (12.1%). BMI available n = 40 (69.0%), median 25.0 (IQR 24.0–28.8).
- **Variables**: plasma p-tau217 (Lumipulse); serum creatinine, eGFR, CKD stage; age, sex, BMI, ethnicity.
- **Reference standard**: none (cognitively normal; assumed < 20% background amyloid at age < 60).
- **Access**: request.

## 4. Pre-analytical handling / transport cohort
- **Provenance**: cognitive neurology clinic, NHNN, London.
- **Ethics/consent**: Wolfson CSF study 12/0344 and Biomarkers and Genetics in Dementia study 03/N049 (NRES London, Apr 2003, PI Fox). Written informed consent.
- **Size**: n = 40 (10 per experiment; 2 excluded for incorrect processing → analysis subsets). Transport comparison: 10 amyloid-PET-cohort samples.
- **Variables**: plasma p-tau217 (Lumipulse, ALZpath) under varied handling conditions; age, sex.
- **Access**: request.

See `data/preprocessing.md` for sample-processing details and AD-status derivation.
