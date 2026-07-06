# Related Work (Typed Dependency Graph)

## RW01: Palmqvist et al., 2025 (Malmö cohort)
- **DOI**: (Alzheimers Dement 2025; ref 25)
- **Type**: baseline / bounds
- **Delta**:
  - What changed: Provides externally derived Lumipulse plasma p-tau217 cut-points (0.22/0.34 pg/mL; and a Malmö CSF Aβ42/p-tau181 < 11.94 AD definition) validated across multiple European memory clinic cohorts.
  - Why: Used as the external comparator against which this study benchmarks its within-cohort cut-points.
- **Claims affected**: C10, C03
- **Adopted elements**: "Malmö" AD-status definition; external cut-points applied to the CSF cohort in a sensitivity analysis.

## RW02: Figdore et al., 2025
- **DOI**: (Alzheimers Dement 2025; ref 16)
- **Type**: baseline
- **Delta**:
  - What changed: Optimized cut-points for clinical interpretation of brain amyloid status using plasma p-tau217 immunoassays (Lumipulse cut-points 0.22/0.34 pg/mL for 95% sens/spec; 92% sens/96% spec at 0.185/0.324; using quantitative amyloid PET ≥ 25 Centiloids and ¹¹C-PiB).
  - Why: External cut-points applied to the amyloid PET cohort as a comparator.
- **Claims affected**: C04
- **Adopted elements**: Cut-point derivation framework and external cut-points for the PET-cohort sensitivity analysis.

## RW03: Arranz et al., 2024
- **DOI**: Alzheimers Res Ther 2024;16:139 (ref 5)
- **Type**: baseline
- **Delta**:
  - What changed: Reported Lumipulse plasma p-tau217 diagnostic performance (95% sens/spec, 19% indeterminate, cut-points 0.186/0.388 pg/mL) in a memory-clinic LP cohort with CSF AD definition (Aβ42/Aβ40 < 0.062).
  - Why: Closely comparable prior derivation; results align with this study's cut-points/indeterminate proportion.
- **Claims affected**: C03
- **Adopted elements**: Dual cut-point framing for the Lumipulse assay.

## RW04: Ashton et al., 2024 — GBSC plasma p-tau Round Robin
- **DOI**: Alzheimers Dement 2024;20:e14508 (refs 6, 38)
- **Type**: bounds
- **Delta**:
  - What changed: Round-robin comparison of plasma p-tau assays showing systematic cross-assay bias and higher Lumipulse fold-change; efforts toward reference materials.
  - Why: Explains why fold-change differs between Lumipulse and ALZpath and why standardization/reference materials are needed.
- **Claims affected**: C02
- **Adopted elements**: Interpretation of inter-assay bias.

## RW05: Pilotto/Warmenhoven/Schindler head-to-head assay comparisons
- **DOI**: refs 17 (Brain 2025;148:408-15), 18 (Alzheimers Dement 2024;20:8074-96), 19 (Brain 2024;148:416-31)
- **Type**: baseline
- **Delta**:
  - What changed: Head-to-head comparisons of Lumipulse vs ALZpath Simoa and other leading blood tests for AD pathology.
  - Why: Establish that both assays perform highly, motivating direct comparison here.
- **Claims affected**: C01, C02
- **Adopted elements**: Assay selection rationale.

## RW06: Inker et al., 2021 — CKD-EPI 2021 eGFR equation
- **DOI**: N Engl J Med 2021;385:1737-49 (ref 27)
- **Type**: imports
- **Delta**:
  - What changed: Race-free creatinine-based eGFR equation used to stage CKD.
  - Why: Method dependency for renal-function staging.
- **Claims affected**: C09
- **Adopted elements**: eGFR computation and CKD staging thresholds.

## RW07: Bornhorst et al., 2025 — CKD effect on p-tau217
- **DOI**: Neurology 2025;104:e210287 (ref 48)
- **Type**: extends / bounds
- **Delta**:
  - What changed: Quantitative assessment of CKD effect on plasma p-tau217.
  - Why: Prior evidence that renal impairment elevates p-tau217; this study confirms elevation into the intermediate zone.
- **Claims affected**: C09
- **Adopted elements**: CKD-confounder framing.

## RW08: Pre-analytical stability literature (SABB / GBSC guidelines)
- **DOI**: refs 33 (Kurz 2021), 34 (Ashton 2021), 35/42 (Verberk 2022; Gouda 2023), 43 (Verberk 2025 GBSC protocol)
- **Type**: extends
- **Delta**:
  - What changed: Prior characterizations of pre-analytical handling effects on blood AD biomarkers and consensus handling guidelines.
  - Why: This study confirms and extends stability findings (adds −20°C 2-week storage and Bio-Freeze transport) for the specific assays.
- **Claims affected**: C06, C08
- **Adopted elements**: ±10% clinically significant change threshold; handling-factor design.

## RW09: FDA clearance of Lumipulse G p-tau217/Aβ42 ratio
- **DOI**: ref 26 (FDA 2022); refs 49,50
- **Type**: bounds
- **Delta**:
  - What changed: FDA approved the Lumipulse G p-tau217/Aβ42 ratio as a plasma test for AD diagnosis in symptomatic patients ≥ 55; and an "FDA" CSF definition (Aβ42/Aβ40 < 0.073) is used as a sensitivity-analysis reference.
  - Why: Contextualizes the choice to deploy p-tau217 alone rather than the ratio.
- **Claims affected**: C03, C05
- **Adopted elements**: "FDA" AD-status definition.

## Brief citations (full footprint, no distinct technical delta)
- Hansson et al. 2022 (ref 1) — Alzheimer's Association appropriate-use recommendations for blood biomarkers.
- Barthélemy/Ossenkoppele/Therriault (refs 2,3,4) — evidence for plasma p-tau accuracy; systematic review/meta-analysis.
- Therriault 2023 (ref 10), Mattsson-Carlgren 2020 (ref 11), Aguillon 2023 (ref 12), Brickman 2021 (ref 13), Milà-Alomà 2022 (ref 14), Yakoub 2024 (ref 15) — longitudinal/predictive/multi-ethnic plasma p-tau217 evidence.
- Mendes 2024 (ref 9), Mielke 2022 (ref 21), Wojdala 2024 (ref 37) — assay comparisons and antibody-epitope differences.
- Brum 2023 (ref 20) — two-step workflow using plasma p-tau217 to screen for amyloid-β positivity (dual cut-point / two-step framing).
- Folstein 1975 (ref 23) — MMSE; NICE 2024 (ref 24) — MMSE severity cut-offs; Hsieh 2013 (ref 29) — ACE-III validation.
- Loreto 2023/2021 (refs 30,31), Jansen 2022 (ref 32), Bucci 2021 (ref 39), La Joie 2023 (ref 40) — amyloid PET reading/quantitation and prevalence.
- Donepezil/NICE TA217 (ref 22), Keshavan 2022 (ref 28) — clinical/CSF background.
- Schöll 2024 (ref 47), Kjaergaard 2025 (ref 44), Jacobs 2025 (ref 45), Mohammadi 2025 (ref 46) — practical implementation, ethnic/BMI/obesity effects on blood biomarkers.

---

## Data-source dependencies (cohorts — verified from sources.yaml; access = request)

| Cohort | Ethics/ID | Repository | Access | Role |
|--------|-----------|------------|--------|------|
| Wolfson CSF study | 12/0344 | UCL (on request from corresponding author) | request | CSF cohort + pre-analytical experiments |
| Biomarkers and Genetics in Dementia study | 03/N049 | UCL (on request from corresponding author) | request | Pre-analytical handling experiments |
| Imperial Amyloid PET Cohort Study | 20/LO/0442 | Imperial College London (on request) | request | Amyloid PET validation cohort + transport comparison |
| Polycystic Kidney Disease (PKD) Biobank / CN-CKD cohort | 05/Q0508/6 (identifier null in sources.yaml) | UCL / Royal Free (on request) | request | Renal-function (CN-CKD) analysis |

All four are controlled/on-request UK cohorts (no open GEO/SRA/EGA/Dryad/figshare accessions).
Data-availability: anonymized data on request from qualified academic investigators after proposal
approval and a signed data access agreement (contact a.keshavan@ucl.ac.uk). See `src/environment.md`.
