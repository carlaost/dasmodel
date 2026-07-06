# Related Work (Typed Dependency Graph)

This review is a synthesis, so most references are **included primary studies** (the data sources of
the NMA) or **conceptual anchors** (framework/benchmark references). Full `RW` blocks are given for
works with a specific technical delta or that supply an included dataset; remaining references are
captured briefly to preserve the full citation footprint.

## Review registration (folded-in grounded source)
- **PROSPERO CRD420261327845** — prospective registration of this systematic review/NMA on the
  PROSPERO International Prospective Register of Systematic Reviews (https://www.crd.york.ac.uk/prospero/).
  Access: open. Type: protocol/registration this ARA extends. (sources.yaml, verified; abstract; §2.)

## Included primary studies (data sources of the NMA)

## RW01: Janelidze et al., 2023
- **DOI**: 10.1093/brain/awac333
- **Type**: imports (data source)
- **Delta**:
  - What changed: head-to-head comparison of 10 plasma phospho-tau assays in prodromal AD.
  - Why: selected as the most comprehensive head-to-head dataset for the BioFINDER-1 cohort.
- **Claims affected**: C01, C07
- **Adopted elements**: BioFINDER-1 dataset (N=135; MCI/prodromal AD; p-tau 217/181/231; IP-MS and Simoa; CSF Abeta42/40).

## RW02: Palmqvist et al., 2024
- **DOI**: 10.1001/jama.2024.13855
- **Type**: imports (data source)
- **Delta**:
  - What changed: blood biomarkers to detect AD in primary and secondary care.
  - Why: distinct clinical outcome (primary-care implementation) for the BioFINDER cohort.
- **Claims affected**: C01
- **Adopted elements**: BioFINDER-PC dataset (N=307; primary care SCD/MCI; p-tau217 APS2; IP-MS C2N; CSF Abeta42/40).

## RW03: Ashton et al., 2024a
- **DOI**: 10.1001/jamaneurol.2023.5319
- **Type**: imports (data source) / baseline
- **Delta**:
  - What changed: diagnostic accuracy of a plasma p-tau217 immunoassay for AD pathology.
  - Why: supplies the WRAP cohort and ALZpath immunoassay node; p-tau217 rivals CSF assays.
- **Claims affected**: C01, C07
- **Adopted elements**: WRAP dataset (N=323; preclinical AD/CU; p-tau217; Simoa ALZpath; amyloid-PET).

## RW04: Ashton et al., 2024b
- **DOI**: 10.1101/2024.08.22.24312244
- **Type**: imports (data source)
- **Delta**:
  - What changed: Alzheimer's Association GBSC plasma phospho-tau Round Robin comparison.
  - Why: most comprehensive multi-assay comparison; supplies the SPIN cohort node.
- **Claims affected**: C01, C07
- **Adopted elements**: SPIN dataset (N=195; AD continuum; p-tau217; Simoa ALZpath; CSF Abeta42/40).

## RW05: Devanarayan et al., 2025
- **DOI**: 10.1002/alz.14411
- **Type**: imports (data source)
- **Delta**:
  - What changed: plasma p-tau217 ratio predicts continuous regional brain tau accumulation in amyloid-positive early AD.
  - Why: supplies the p-tau217 ratio node for Tau-PET staging.
- **Claims affected**: C02, C03
- **Adopted elements**: Clarity AD dataset (N=98; MCI and mild AD; p-tau217 Ratio; IP-MS C2N; Tau-PET).

## RW06: Lehmann et al., 2025
- **DOI**: 10.1016/j.ebiom.2025.105805
- **Type**: imports (data source)
- **Delta**:
  - What changed: comparative performance of p-tau181/Abeta42 and p-tau217/Abeta42 ratios vs. individual measurements in detecting brain amyloidosis.
  - Why: supplies the ALZAN cohort and ratio comparison.
- **Claims affected**: C01, C02
- **Adopted elements**: ALZAN dataset (N=423; cognitive complaints; p-tau 217/181; Simoa Fujirebio; CSF Abeta42/40).

## RW07: Mila-Aloma et al., 2022
- **DOI**: 10.1038/s41591-022-01925-w
- **Type**: imports (data source)
- **Delta**:
  - What changed: plasma p-tau231 and p-tau217 as state markers of amyloid-beta pathology in preclinical AD.
  - Why: primary evidence for the "relay" hypothesis (p-tau231 rises earliest); supplies ALFA+ cohort.
- **Claims affected**: C04
- **Adopted elements**: ALFA+ dataset (N=397; preclinical AD/CU; p-tau 217/231; Simoa and MSD; CSF Abeta42/40).

## RW08: Benedet et al., 2026
- **DOI**: 10.1093/clinchem/hvaf162
- **Type**: imports (data source)
- **Delta**:
  - What changed: diagnostic accuracy of serum p-tau217 in AD (serum-vs-plasma equivalence).
  - Why: key evidence that serum is a viable matrix; supplies the serum-focus TRIAD node.
- **Claims affected**: C06
- **Adopted elements**: TRIAD dataset (N=100; AD continuum; p-tau217 serum focus; automated IA; amyloid-PET).

## RW09: Mielke et al., 2022
- **DOI**: 10.1038/s41591-022-01822-2
- **Type**: imports (data source)
- **Delta**:
  - What changed: performance of plasma p-tau181 and p-tau217 in the community (population-based).
  - Why: supplies the large MCSA community cohort; supports ratio normalization rationale.
- **Claims affected**: C01, C02
- **Adopted elements**: MCSA dataset (N=1,051; community CU/MCI/Dem; p-tau 217/181; MSD Lilly; amyloid/tau-PET).

## RW10: Silva-Spinola et al., 2026
- **DOI**: 10.1038/s41598-025-34241-7
- **Type**: imports (data source)
- **Delta**:
  - What changed: plasma p-tau217 quantified by fully automated LUMIPULSE G outperforms p-tau181 in cognitive-complaints patients.
  - Why: supplies the Coimbra cohort and automated-IA (Lumipulse) node.
- **Claims affected**: C01, C07
- **Adopted elements**: Coimbra dataset (N=395; tertiary clinic; p-tau 217/181; automated IA; CSF Abeta42/40).

## RW11: Huashan Cohort (Han Chinese, source study not separately cited)
- **DOI**: Not specified in paper (cohort marked with * in Table 1)
- **Type**: imports (data source)
- **Delta**:
  - What changed: Han Chinese clinic cohort providing cross-ethnic validation.
  - Why: supports generalizability to Asian populations.
- **Claims affected**: C05
- **Adopted elements**: Huashan dataset (N=297; clinic MCI/dementia; p-tau 217/231; AutoIA Lilly; amyloid-PET).

## RW12: GBA Study (Greater Bay Area, Han Chinese, source study not separately cited)
- **DOI**: Not specified in paper (cohort marked with * in Table 1)
- **Type**: imports (data source)
- **Delta**:
  - What changed: Han Chinese community-based cohort providing cross-ethnic validation.
  - Why: supports generalizability to Asian populations.
- **Claims affected**: C05
- **Adopted elements**: Greater-Bay dataset (N=425; community-based CU; p-tau 217/181; AutoIA ALZpath; amyloid-PET).

## Conceptual / methodological anchors

## RW13: Jack Jr et al., 2018
- **DOI**: 10.1016/j.jalz.2018.02.018
- **Type**: imports (framework)
- **Delta**:
  - What changed: NIA-AA research framework — biological definition of AD (AT(N)).
  - Why: grounds the shift from clinical to biomarker-based AD definition motivating the review.
- **Claims affected**: none directly (motivation)
- **Adopted elements**: AT(N) biomarker framework.

## RW14: Karikari et al., 2020
- **DOI**: 10.1016/S1474-4422(20)30071-5
- **Type**: bounds (prior standard)
- **Delta**:
  - What changed: established plasma p-tau181 as a scalable diagnostic/prediction marker.
  - Why: p-tau181 is the prior standard and the review's reference comparator (now argued obsolete).
- **Claims affected**: C08
- **Adopted elements**: p-tau181 as baseline comparator.

## RW15: Ashton et al., 2021
- **DOI**: 10.1007/s00401-021-02275-6
- **Type**: extends
- **Delta**:
  - What changed: plasma p-tau231 as a biomarker for incipient AD, rising earliest in the continuum.
  - Why: underpins the p-tau231 early-amyloidosis / relay hypothesis.
- **Claims affected**: C04
- **Adopted elements**: p-tau231 early-rise evidence.

## RW16: Therriault et al., 2021
- **DOI**: 10.1212/WNL.0000000000011416
- **Type**: imports (quantitative claim source)
- **Delta**:
  - What changed: frequency of biologically defined AD relative to age, sex, APOE e4, cognition.
  - Why: basis for the statement that plasma p-tau217 could reduce the need for tau-PET scans by ~80% (Braak V-VI proxy).
- **Claims affected**: C03
- **Adopted elements**: Tau-PET reduction estimate.

## Background / supporting references (brief)
- **Hansson et al., 2023** (10.1038/s41582-023-00403-3) — blood biomarkers in clinical practice/trials; motivation.
- **Hansson et al., 2022** (10.1002/alz.12756) — Alzheimer's Association appropriate-use recommendations; motivation.
- **Teunissen et al., 2022** (10.1016/S1474-4422(21)00361-6) — blood-based biomarkers toward clinical implementation; motivation and limitations (longitudinal slope).
- **Schindler et al., 2019** (10.1212/WNL.0000000000008081) — high-precision plasma Abeta42/40; supports ratio/MS benchmark.
- **Schindler et al., 2022** (10.1212/WNL.0000000000200358) — effect of race on plasma-based amyloid prediction; cross-ethnic motivation (C05).
- **Schindler et al., 2021** (10.1212/WNL.0000000000012775) — predicting symptom onset in sporadic AD.
- **Suárez-Calvet et al., 2020** (10.15252/emmm.202012921) — novel tau markers T181/T217/T231 rise in initial stages; supports p-tau217 dynamic range (C01).
- **Grothe et al., 2021** (10.1212/WNL.0000000000012513) — automated CSF and novel plasma biomarkers vs. autopsy; supports p-tau217 pathology link (C01).
- **Barthélemy et al., 2020** (10.1084/jem.20200861) — blood plasma p-tau isoforms track CNS change in AD.
- **Bayoumy et al., 2021** (10.1186/s13195-021-00939-9) — clinical/analytical comparison of six Simoa assays for p-tau181/217/231; platform heterogeneity.
- **Brickman et al., 2021** (10.1002/alz.12301) — plasma p-tau181/217 in a multi-ethnic community study; cross-ethnic motivation (C05).
- **Brum et al., 2023** (10.1038/s43587-023-00471-5) — two-step p-tau217 workflow to screen for amyloid; motivates simultaneous NMA (gap).
- **Doré et al., 2022** (10.1002/dad2.12307) — p-tau217+tau vs. NAV4694 amyloid and MK6240 tau PET; supports p-tau217/tau-PET link (C03).
- **Mattsson-Carlgren et al., 2023** (10.1001/jamaneurol.2022.5272) — prediction of longitudinal cognitive decline with plasma biomarkers; prognosis (C03).
- **O'Bryant et al., 2023** (10.1002/alz.12647) — medical comorbidities and ethnicity impact plasma AD biomarkers; supports serum/ethnicity discussion (C05, C06).
- **Rissman et al., 2024** (10.1002/alz.13542) — plasma Abeta42/40 and p-tau217 ratios increase amyloid-PET classification accuracy; supports ratio effect (C02).
- **Thijssen et al., 2021** (10.1038/s41591-020-0762-2) — diagnostic value of plasma p-tau181 in AD and FTLD; p-tau181 limitations (C08).
- **Triana-Baltzer et al., 2021** (10.1002/dad2.12204) — development/validation of a high-sensitivity p-tau217 assay; platform (C07).
- **Wang et al., 2024** (10.1016/j.arr.2024.102507) — neuroimaging and biofluid biomarkers across race/ethnicity; supports robustness vs. genetic markers (C05).
