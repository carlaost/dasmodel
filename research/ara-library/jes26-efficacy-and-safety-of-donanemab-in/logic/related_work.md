# Related Work (Typed Dependency Graph)

The paper is a post-hoc secondary analysis; its dependency footprint is dominated by the parent
trial (RW02) and the LTE report (RW07), plus the methodological imputation references and the EU/UK
regulatory documents.

## RW01: Mintun et al., 2021 (donanemab in early AD, phase 2)
- **DOI**: 10.1056/NEJMoa2100708
- **Type**: imports
- **Delta**:
  - What changed: Establishes donanemab's efficacy signal in early AD that the phase 3 program builds on.
  - Why: Foundational evidence that donanemab slows cognitive/functional decline.
- **Claims affected**: background to C01–C08
- **Adopted elements**: Drug mechanism and early efficacy rationale.

## RW02: Sims et al., 2023 — TRAILBLAZER-ALZ 2 primary report (JAMA)
- **DOI**: 10.1001/jama.2023.13239
- **Type**: extends
- **Delta**:
  - What changed: This paper re-analyses the same trial dataset restricted to the EU-eligible subpopulation under the EMA-required conservative estimand; the primary report characterised the overall/indicated populations.
  - Why: To produce estimates specific to the European population actually treated in practice.
- **Claims affected**: C01–C10 (parent trial, methods, overall-population comparators; 28.9% CDR-SB slowing benchmark; low-medium tau definition; time-progression model)
- **Adopted elements**: Trial design, dosing, treatment-course completion, clinical scales, tau stratification, time-progression model, overall-population ARIA rate (36.8%).

## RW03: Electronic Medicines Compendium — Kisunla SmPC (UK), 2025
- **DOI**: — (https://www.medicines.org.uk/emc/product/16014/smpc)
- **Type**: bounds
- **Delta**:
  - What changed: UK indication (non-carriers/heterozygotes) with modestly different contraindications from the EU.
  - Why: Contextualises the eligibility definition.
- **Claims affected**: O1 (population definition)
- **Adopted elements**: UK label population framing.

## RW04: EMA — Kisunla assessment report, 2025
- **DOI**: — (EMA EPAR public assessment report)
- **Type**: bounds
- **Delta**:
  - What changed: Regulatory assessment underpinning EU approval.
  - Why: Basis for the EU-indicated population and the required conservative imputation.
- **Claims affected**: O3, C01, C02, C10
- **Adopted elements**: EMA benefit–risk framing.

## RW05: EMA — Kisunla product information (SmPC), 2026
- **DOI**: — (EMA product information)
- **Type**: bounds
- **Delta**:
  - What changed: EU indication and approved (gradual) titration dosing regimen.
  - Why: This report complements the SmPC with EU-eligible efficacy/safety data.
- **Claims affected**: O1, L7
- **Adopted elements**: EU indication definition; approved titration.

## RW06: Cogswell et al., 2025 — ARIA imaging recommendations (AJNR)
- **DOI**: 10.3174/ajnr.A8469
- **Type**: imports
- **Delta**:
  - What changed: Provides ARIA monitoring/practice context and the ε4-allele/ARIA-risk relationship.
  - Why: Supports the rationale for excluding ε4 homozygotes.
- **Claims affected**: O2, C08
- **Adopted elements**: ARIA risk–ε4 dose relationship.

## RW07: Zimmer et al., 2026 — TRAILBLAZER-ALZ 2 LTE (J Prev Alzheimers Dis)
- **DOI**: 10.1016/j.tjpad.2025.100446
- **Type**: extends
- **Delta**:
  - What changed: This paper reports LTE non-carrier/heterozygote efficacy/safety and reuses the propensity-weighted ADNI external-control methodology from Zimmer et al.
  - Why: To provide long-term durability evidence for the target subgroup.
- **Claims affected**: C09
- **Adopted elements**: LTE design, propensity score weighting method, ADNI external control.

## RW08: Carpenter, Roger & Kenward, 2013 — MI framework for protocol deviation (J Biopharm Stat)
- **DOI**: 10.1080/10543406.2013.834911
- **Type**: imports
- **Delta**:
  - What changed: Methodological basis for reference-based multiple imputation (J2R).
  - Why: Underpins the conservative hybrid imputation.
- **Claims affected**: methods for C01, C02, C04, C10
- **Adopted elements**: J2R imputation framework.

## RW09: Mallinckrodt et al., 2012 — estimands/estimators in longitudinal trials (Pharm Stat)
- **DOI**: 10.1002/pst.1536
- **Type**: imports
- **Delta**:
  - What changed: Structured approach to choosing estimands/estimators, informing CIR and the hybrid choice.
  - Why: Justifies the conservative imputation strategy.
- **Claims affected**: methods for C01, C02, C04, C10
- **Adopted elements**: Estimand/estimator selection.

## RW10: Wang et al., 2025 — modified titration reduces ARIA (Alzheimers Dement)
- **DOI**: 10.1002/alz.70062
- **Type**: bounds
- **Delta**:
  - What changed: TRAILBLAZER-ALZ 6 modified titration lowers ARIA-E further (41% relative risk reduction at 24 weeks).
  - Why: Indicates clinical-practice dosing will be safer than the trial regimen used here.
- **Claims affected**: C08, L7
- **Adopted elements**: Titration/ARIA context.

## RW11: Wang et al., 2025 — TRAILBLAZER-ALZ 6 18-month results (J Prev Alzheimers Dis)
- **DOI**: 10.1016/j.tjpad.2025.100266
- **Type**: bounds
- **Delta**:
  - What changed: Longer-term modified-titration ARIA-E/amyloid results.
  - Why: Reinforces the practice-dosing safety context.
- **Claims affected**: C08, L7
- **Adopted elements**: Modified-titration ARIA outcomes.

## Additional citations (briefer footprint)
- **[10] Buracchio et al., 2025** (10.1002/trc2.70113): U.S. regulatory perspective on clinical meaningfulness; motivates the restricted-range interpretation of wide scales (L8).
- **[11] DiBenedetti et al., 2020** (10.1186/s13195-020-00659-6): qualitative study of what matters most to patients/care partners; motivates value of slowing progression.
- **[12] Hauber et al., 2023** (10.1007/s40120-023-00445-0): quantitative analysis of patient priorities; same motivation.
- **[13] Jessen et al., 2024** (10.14283/jpad.2024.153): EADC position statement; societal cost argument for delaying progression.
- **[16] Elhefnawy et al., 2025** (10.1007/s10928-024-09959-y): natural amyloid accumulation using ADNI; benchmark for post-treatment amyloid reaccumulation.
- **[17] Jagust & Landau, 2021** (10.1212/WNL.0000000000011524): temporal dynamics of β-amyloid accumulation; reaccumulation benchmark.
- **[18] Potashman et al., 2021** (10.1007/s40120-021-00272-1): AD progression rates (NACC data); context for stage-dependent decline (L4).
- **[19] Trudel et al., 2025** (10.1002/alz.70624): clinical progression rates by biological AD stage; same context.
