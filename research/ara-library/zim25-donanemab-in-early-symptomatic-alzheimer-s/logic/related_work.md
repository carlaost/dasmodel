# Related Work (Typed Dependency Graph)

This paper reports the long-term extension (LTE) of TRAILBLAZER-ALZ 2; its dependency footprint is
dominated by the pivotal 76-week trial report (RW02) that it directly extends, the exposure-response
model it updates (RW05), and the ARIA/safety companion analysis (RW06) it references for previously
reported deaths. 23 references total in the source; all are captured below (11 with full `RW`
blocks reflecting a specific technical delta, 12 briefer background/context entries).

## RW01: Hardy & Higgins, 1992 — the amyloid cascade hypothesis (Science)
- **DOI**: 10.1126/science.1566067
- **Type**: imports
- **Delta**:
  - What changed: Foundational disease-mechanism hypothesis (β-amyloid plaque and neurofibrillary tangle accumulation drives progressive cognitive decline) motivating amyloid-targeting therapy.
  - Why: Establishes the mechanistic rationale for donanemab as an anti-amyloid antibody.
- **Claims affected**: background to all claims
- **Adopted elements**: Amyloid cascade disease model.

## RW02: Sims et al., 2023 — TRAILBLAZER-ALZ 2 pivotal 76-week trial (JAMA)
- **DOI**: 10.1001/jama.2023.13239
- **Type**: extends
- **Delta**:
  - What changed: This paper extends the pivotal 76-week placebo-controlled trial with a 78-week LTE (154 weeks total), introducing an external ADNI comparator since the LTE has no internal placebo, and reports long-term (3-year) efficacy/safety and post-discontinuation amyloid/ARIA trajectories not covered by the pivotal report.
  - Why: The pivotal report established 76-week efficacy/safety but could not address durability after limited-duration dosing or effects beyond 18 months.
- **Claims affected**: C01–C12 (trial design, dosing regimen, treatment course completion criteria, eligibility criteria, baseline population characteristics, and the placebo-controlled-period donanemab safety profile against which LTE safety is compared)
- **Adopted elements**: Trial design (NCT04437511), dosing regimen (700 mg × 3 then 1400 mg Q4W), treatment course completion criteria definitions, eligibility criteria, placebo-controlled-period completion rates (17.1%/46.6%/69.2%) and safety profile used as the LTE comparator.

## RW03: van Dyck et al., 2023 — Lecanemab in early Alzheimer's disease (NEJM)
- **DOI**: 10.1056/NEJMoa2212948
- **Type**: baseline
- **Delta**:
  - What changed: An independent randomized trial of a different anti-amyloid antibody (lecanemab), cited alongside donanemab as evidence that sufficient amyloid removal can slow disease progression.
  - Why: Corroborates the class-level rationale that amyloid-plaque removal is disease-modifying.
- **Claims affected**: background to C01, C02
- **Adopted elements**: Class-level evidence for amyloid removal → clinical slowing.

## RW04: Roche Diagnostics, 2023 — Elecsys total-tau CSF method sheet
- **DOI**: — (manufacturer method sheet)
- **Type**: imports
- **Delta**:
  - What changed: Defines the assay used to establish the CSF total-tau/amyloid-β42 ratio >0.28 criterion for ADNI cohort eligibility.
  - Why: Ensures the ADNI comparator cohort has biomarker-confirmed amyloid pathology comparable to trial participants.
- **Claims affected**: O3 (ADNI external control construction), C01, C02
- **Adopted elements**: CSF biomarker threshold for ADNI cohort selection.

## RW05: Gueorguieva et al., 2025 — donanemab exposure-response in early symptomatic AD (Alzheimers Dement)
- **DOI**: 10.1002/alz.70491
- **Type**: extends
- **Delta**:
  - What changed: This paper's amyloid reaccumulation-rate estimate (2.4 CL/year) is produced by incorporating LTE data into the exposure-response model originally built in this reference from four donanemab studies (phase 1b, TRAILBLAZER-ALZ, TRAILBLAZER-EXT, TRAILBLAZER-ALZ 2).
  - Why: Reuses and updates an established cross-study pharmacometric model rather than building a new one.
- **Claims affected**: C10
- **Adopted elements**: Exposure-response modeling framework and prior donanemab-study data underlying the reaccumulation-rate estimate.

## RW06: Zimmer et al., 2025 — ARIA with donanemab: secondary analysis of TRAILBLAZER-ALZ and ALZ 2 (JAMA Neurol)
- **DOI**: 10.1001/jamaneurol.2025.0065
- **Type**: baseline
- **Delta**:
  - What changed: Provides the previously reported detail on the two LTE deaths (ARIA-E; intracranial hemorrhage following thrombolytic administration) that this paper's safety section references rather than re-derives.
  - Why: Avoids re-reporting case-level detail already published in the dedicated ARIA secondary analysis.
- **Claims affected**: C11
- **Adopted elements**: Case-level detail on the two LTE deaths.

## RW07: Jagust & Landau, 2021 — temporal dynamics of β-amyloid accumulation (Neurology, ADNI)
- **DOI**: 10.1212/wnl.0000000000011524
- **Type**: baseline
- **Delta**:
  - What changed: Establishes an independent, natural (untreated) amyloid accumulation-rate benchmark from ADNI.
  - Why: Used as a qualitative comparator for whether the LTE's post-discontinuation reaccumulation rate (2.4 CL/year) is "comparable to the natural history of the disease."
- **Claims affected**: C10
- **Adopted elements**: Natural amyloid accumulation-rate benchmark.

## RW08: Elhefnawy et al., 2025 — quantifying natural amyloid plaque accumulation using ADNI (J Pharmacokinet Pharmacodyn)
- **DOI**: 10.1007/s10928-024-09959-y
- **Type**: baseline
- **Delta**:
  - What changed: A second, more recent natural-accumulation-rate benchmark from ADNI, complementing RW07.
  - Why: Same comparator role as RW07 for interpreting the 2.4 CL/year reaccumulation estimate.
- **Claims affected**: C10
- **Adopted elements**: Natural amyloid accumulation-rate benchmark.

## RW09: Lansdall et al., 2023 — establishing clinically meaningful change in MCI-due-to-AD outcome measures (J Prev Alzheimers Dis)
- **DOI**: 10.14283/jpad.2022.102
- **Type**: bounds
- **Delta**:
  - What changed: Establishes minimal clinically important difference (MCID) thresholds for CDR-SB and related scales at the individual-patient level.
  - Why: The paper explicitly argues these MCID thresholds are not appropriate for interpreting the LTE's between-group CDR-SB differences, motivating its CDR-G-based and time-saved framings instead.
- **Claims affected**: C04 (motivates why CDR-G, not CDR-SB MCID, is presented as the primary basis for clinical meaningfulness)
- **Adopted elements**: None adopted directly — cited to explain a methodological choice not to rely on MCID for between-group LTE comparison.

## RW10: DiBenedetti et al., 2020 — assessing what matters most to patients with/at risk for AD (Alzheimers Res Ther)
- **DOI**: 10.1186/s13195-020-00659-6
- **Type**: imports
- **Delta**:
  - What changed: Qualitative patient/care-partner research establishing that slowing progression in earlier disease stages is more impactful than equivalent slowing later.
  - Why: Supports interpreting the early- vs delayed-start time-saved gap (C06) as clinically consequential despite its modest absolute size (1.3 months).
- **Claims affected**: C06
- **Adopted elements**: Patient-value framing for earlier-vs-later symptom-progression slowing.

## RW11: Wang et al., 2025 — TRAILBLAZER-ALZ 6 modified titration reduces ARIA-E (J Prev Alzheimers Dis)
- **DOI**: 10.1016/j.tjpad.2025.100266
- **Type**: bounds
- **Delta**:
  - What changed: Shows that a more gradual dose-titration regimen significantly reduces ARIA-E risk compared with the standard TRAILBLAZER-ALZ 2 dosing regimen used in this LTE.
  - Why: Signals that the ARIA rates reported in this paper (Table 1, C11–C12) reflect the older/standard titration and may not represent the risk profile of newer titration approaches.
- **Claims affected**: C11, C12
- **Adopted elements**: Context that a lower-ARIA titration regimen now exists, bounding the generalizability of this paper's safety numbers to the specific dosing regimen studied.

## Additional citations (briefer footprint)
- **[11] Shcherbinin et al., 2022** (10.1001/jamaneurol.2022.2793): association of amyloid reduction after donanemab with tau pathology and clinical outcomes (TRAILBLAZER-ALZ); cited as one of the "previously reported methods" underlying the amyloid-reaccumulation-rate calculation (§2.5.2).
- **[12] Gueorguieva et al., 2023** (10.1002/cpt.2875): donanemab population pharmacokinetics, amyloid plaque reduction, and safety; cited alongside [11] as prior methodology for the reaccumulation-rate calculation.
- **[6] Faria, Alves & Charchat-Fichman, 2015** (10.1590/1980-57642015dn92000009): review of executive-function tests in aging; cited alongside [7] as methodological background for the propensity-weighting/statistical approach.
- **[7] Benedetto et al., 2018** (10.1093/ejcts/ezy167): statistical primer on propensity score matching and alternatives; underlies the propensity score weighting methodology (§2.5.1).
- **[8] Stürmer et al., 2010** (10.1093/aje/kwq198): methodology for handling extreme propensity-score weights (tails of the distribution); underlies the 95th-percentile weight-trimming step (§2.5.1).
- **[9] Navitsky et al., 2018** (10.1016/j.jalz.2018.06.1353): standardization of amyloid quantitation to the Centiloid scale (florbetapir SUVR); underlies the CL scale used throughout.
- **[10] Zeltzer et al., 2025** (10.1001/jamaneurol.2025.2218): concordance between amyloid-PET quantification and visual reads; supports the <24.1 CL clearance threshold as "largely consistent with a negative visual scan."
- **[16] Lansdall et al., 2023**: see RW09 above (duplicate reference number in the source's own numbering context is not applicable — this is reference [16] in-text, corresponding to the same MCID paper).
- **[17] DiBenedetti et al., 2020**: see RW10 above (in-text reference [17]).
- **[18] Hauber et al., 2023** (10.1007/s40120-023-00445-0): quantitative patient-preference analysis; cited alongside [17] for the value of earlier symptom-progression slowing.
- **[19] Raket, 2025** (10.1002/alz.087702): time-based measures for quantifying disease modification in AD; cited as the methodological basis for framing treatment effect via time-progression/time-saved models.
- **[20] Raket et al., 2024** (10.1002/alz.14134): scenarios for long-term efficacy of amyloid-targeting therapies vs natural history; cited for extrapolated severe-dementia-onset delay estimates (0.6/1.9/4.2 years under conservative/intermediate/optimistic assumptions) that motivate updating such models with this LTE's data.
- **[21] Mullins et al., 2025** (10.1002/trc2.70149): donanemab immunogenicity (antidrug antibodies) and its relationship to infusion-related reactions; cited as prior characterization not re-derived here.
- **[23] Klein et al., 2024** (10.1002/alz.13700): donanemab data addressing coverage-with-evidence-development questions; cited to support that TRAILBLAZER-ALZ 2's comorbidity/co-medication profile is consistent with the Medicare population, bearing on generalizability.
