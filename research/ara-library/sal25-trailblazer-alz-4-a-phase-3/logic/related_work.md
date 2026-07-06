# Related Work — TRAILBLAZER-ALZ 4

Typed dependency graph. RW01 records the trial registration/data source (grounded, verified via sources.yaml). Works with a specific technical delta get full blocks; the remaining citation footprint is captured briefly.

## RW01: TRAILBLAZER-ALZ 4 registration — NCT05108922 (ClinicalTrials.gov)
- **DOI / ID**: NCT05108922
- **Type**: imports (registration + protocol/SAP + data source)
- **Delta**:
  - What: This paper is the primary results report of the registered trial NCT05108922; the registry hosts the full inclusion/exclusion criteria, safety assessments, and further statistical-analysis detail.
  - Why: Prospective registration and protocol/SAP archiving; individual participant data available on request via Vivli.
- **Registry facts** (verified, sources.yaml): "A Phase 3, Open-Label, Parallel-Group, 2-Arm Study to Investigate Amyloid Plaque Clearance With Donanemab Compared With Aducanumab-avwa in Participants With Early Symptomatic Alzheimer's Disease (TRAILBLAZER-ALZ 4)"; phase PHASE3; status COMPLETED; sponsor Eli Lilly and Company; 148 participants; 31 US sites; has_results = true.
- **Claims affected**: C01–C08
- **Adopted elements**: Endpoint definitions, eligibility, dosing, statistical analysis plan.

## RW02: Sims et al., 2023 — TRAILBLAZER-ALZ 2 (JAMA)
- **DOI**: 10.1001/jama.2023.13239
- **Type**: extends
- **Delta**:
  - What: Phase 3 trial showing donanemab reduced amyloid and slowed clinical progression at 18 months; TRAILBLAZER-ALZ 4 extends donanemab evaluation to a direct comparator design and adopts the low–medium tau subpopulation framing and the < 24.1 CL clearance construct.
  - Why: Establishes donanemab efficacy and the tau-stratification approach.
- **Claims affected**: C01, C02, C03, C05
- **Adopted elements**: Low–medium tau definition; clearance definition; biomarker approach.

## RW03: Mintun et al., 2021 — TRAILBLAZER-ALZ (N Engl J Med)
- **DOI**: 10.1056/NEJMoa2100708
- **Type**: extends
- **Delta**:
  - What: Phase 2 donanemab trial that first demonstrated amyloid reduction with clinical signal; ALZ 4 builds on its clearance and tau-subpopulation methodology.
  - Why: Origin of the donanemab clearance/dosing-cessation and tau-stratification paradigm.
- **Claims affected**: C01, C03, C05
- **Adopted elements**: Dosing-cessation criteria concept; low–medium tau subpopulation.

## RW04: Budd Haeberlein et al., 2022 — EMERGE / ENGAGE aducanumab phase 3 (J Prev Alzheimers Dis)
- **DOI**: 10.14283/jpad.2022.30
- **Type**: baseline
- **Delta**:
  - What: The two aducanumab phase 3 trials (EMERGE positive, ENGAGE not) characterizing aducanumab's amyloid and clinical effects; ALZ 4 uses aducanumab (per label) as the active comparator.
  - Why: Defines the comparator's expected amyloid-lowering and ARIA profile.
- **Claims affected**: C01–C08 (comparator arm)
- **Adopted elements**: Aducanumab efficacy/safety expectations.

## RW05: DeMattos et al., 2012 — plaque-specific antibody clears existing plaques (Neuron)
- **DOI**: 10.1016/j.neuron.2012.10.029
- **Type**: imports
- **Delta**:
  - What: Preclinical basis for donanemab's mechanism — a plaque-specific (N3pG) antibody clears existing β-amyloid plaques via microglial phagocytosis.
  - Why: Mechanistic rationale for donanemab's targeting of mature plaques.
- **Claims affected**: C04, C05 (depth/speed of clearance)
- **Adopted elements**: N3pG mechanistic model.

## RW06: ADUHELM (aducanumab-avwa) US prescribing information, 2021 (ref 10)
- **DOI / ID**: FDA label 761178s000lbl
- **Type**: imports
- **Delta**:
  - What: Defines the comparator dosing regimen (weight-based, per label) used for the aducanumab arm.
  - Why: Comparator administered "per label."
- **Claims affected**: C01–C08 (comparator dosing)
- **Adopted elements**: Aducanumab dose schedule.

## RW07: Navitsky et al., 2018 — Centiloid standardization of florbetapir SUVR (Alzheimers Dement)
- **DOI**: 10.1016/j.jalz.2018.06.1353
- **Type**: imports
- **Delta**:
  - What: Method to standardize florbetapir SUVR to the Centiloid scale; underpins the < 24.1 CL clearance threshold and eligibility cutoffs.
  - Why: Provides the quantitative amyloid scale.
- **Claims affected**: C01–C05
- **Adopted elements**: Centiloid conversion; clearance threshold basis (with ref 17).

## RW08: Joshi et al., 2015 — semi-automated florbetapir PET quantification (J Nucl Med)
- **DOI**: 10.2967/jnumed.114.153494
- **Type**: imports
- **Delta**:
  - What: Semi-automated method for quantifying F18 florbetapir PET (motion correction, template alignment, cortical SUVR with whole-cerebellar reference).
  - Why: Defines the imaging-processing pipeline.
- **Claims affected**: C01–C05
- **Adopted elements**: PET processing pipeline.

## Additional citation footprint (brief)
- **Hardy & Higgins, 1992 (Science, 10.1126/science.1566067)** — amyloid cascade hypothesis; background (imports).
- **Selkoe, 2000 (JAMA, 10.1001/jama.283.12.1615)** — amyloid origins of AD; background.
- **Jack et al., 2018 (Alzheimers Dement, 10.1016/j.jalz.2018.02.018)** — NIA-AA research framework defining biological AD; used for Aβ/diagnostic framing.
- **Jeremic et al., 2021 (Ageing Res Rev, 10.1016/j.arr.2021.101496)** — review of anti-Aβ strategies; background.
- **Aisen et al., 2020 (J Prev Alzheimers Dis, 10.14283/jpad.2020.24)** — future of anti-amyloid trials; background.
- **Vogt et al., 2023 (Int J Mol Sci, 10.3390/ijms24043895)** — history of Aβ immunotherapies; background.
- **Plotkin & Cashman, 2020 (Neurobiol Dis, 10.1016/j.nbd.2020.105010)** — passive immunotherapy targeting Aβ/tau; background.
- **Ferrero et al., 2016 (Alzheimer's Dement N Y, 10.1016/j.trci.2016.06.002)** — first-in-human aducanumab; comparator mechanism (imports).
- **Biogen, 2024** — aducanumab discontinuation announcement; motivates limitation on clinical relevance.
- **Albert et al., 2011 (Alzheimers Dement, 10.1016/j.jalz.2011.03.008)** — MCI diagnostic criteria; eligibility definition.
- **Clark et al., 2012 (Lancet Neurol, 10.1016/S1474-4422(12)70142-4)** — florbetapir PET vs autopsy neuritic plaques; validates clearance threshold (with ref 18).
- **Fleisher et al., 2020 (JAMA Neurol, 10.1001/jamaneurol.2020.0528)** — flortaucipir PET vs postmortem AD changes; tau-subpopulation basis.
- **Pontecorvo et al., 2019 (Brain, 10.1093/brain/awz090)** — longitudinal flortaucipir across the AD spectrum; tau-subpopulation basis.
- **Barakos et al., 2022 (J Prev Alzheimers Dis, 10.14283/jpad.2022.21)** — detection/management of ARIA; ARIA framing.
- **Barakos et al., 2013 (AJNR, 10.3174/ajnr.A3500)** — MRI features of ARIA; ARIA framing.
- **Wise-Brown et al., 2024 (EClinicalMedicine, 10.1016/j.eclinm.2024.102693)** — promoting diversity in AD trials; supports diversity limitation.
