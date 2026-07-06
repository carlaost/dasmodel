# Related Work / Dependency Graph

This report is a synthesis that depends primarily on external **data sources** and methodological anchors rather than on prior competing methods. Dependencies are typed as: `imports` (data/estimates used directly), `bounds` (provides comparison/limits), `baseline` (prior edition or alternative estimate), `extends` (builds on a framework). Reference numbers in brackets are the report's own citation numbers. None of these sources is deposited as a citable dataset accession, and no clinical trial is registered by this article (confirmed in `sources.yaml`); identifiers below are program/registry/study names, not accessions.

## RW01: Rajan et al. — Chicago Health and Aging Project (CHAP) prevalence [293]
- **DOI**: Not specified in paper (cited as ref 293)
- **Type**: imports
- **Delta**:
  - What changed: CHAP-derived age/sex/race-specific prevalence rates applied to 2024 Census projections yield the headline 7.2M (2025) and 13.8M (2060) figures.
  - Why: Longitudinal symptom-based ascertainment attempts to capture all cases, avoiding health-system underdiagnosis.
- **Claims affected**: C01, C02, C10, C11
- **Adopted elements**: national/state prevalence counts, age distribution, projection trajectory.

## RW02: Health and Retirement Study — Harmonized Cognitive Assessment Protocol (HRS-HCAP) [173]
- **DOI**: Not specified in paper (ref 173)
- **Type**: bounds
- **Delta**:
  - What changed: Nationally representative all-cause dementia estimate (10% of 65+ in 2016; 4.92M) used as a comparison/lower bound to CHAP's 6.07M Alzheimer's-only estimate.
  - Why: HRS-HCAP additionally requires informant-reported functional impairment, a more stringent threshold that may miss mild cases.
- **Claims affected**: C01
- **Adopted elements**: all-cause dementia and MCI prevalence estimates.

## RW03: Chene et al. — Framingham Heart Study lifetime risk [340]
- **DOI**: Not specified in paper (ref 340)
- **Type**: imports
- **Delta**:
  - What changed: Provides sex-specific lifetime-risk estimates for Alzheimer's dementia at ages 45 and 65 (Figure 6).
  - Why: Long-running cohort with strict DSM-IV / NINCDS-ADRDA diagnostic criteria.
- **Claims affected**: C11
- **Adopted elements**: lifetime-risk estimates by sex.

## RW04: Dhana et al. — state/county prevalence estimates [336]
- **DOI**: Not specified in paper (ref 336)
- **Type**: imports
- **Delta**:
  - What changed: Supplies 2020 state- and county-level prevalence (Table 5, Figure 5) from age/sex/race distributions.
- **Claims affected**: C01, C10
- **Adopted elements**: state prevalence numbers and percentages; top-10 county ranking.

## RW05: CDC / National Center for Health Statistics — mortality data [476, 489, 492, 1033]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Death-certificate underlying-cause counts (120,122 in 2022), cause-of-death trends 2000-2022, age-specific death rates, and place-of-death series.
- **Claims affected**: C03, C13 (mortality context)
- **Adopted elements**: national/state deaths, mortality rates, trend percentages (Tables 6-7; Figures 8-10, 17).

## RW06: Medicare Current Beneficiary Survey 2018 & National 100% Sample Medicare FFS 2019 [485, 941]
- **DOI**: Not specified in paper (unpublished tabulations)
- **Type**: imports
- **Delta**:
  - What changed: Per-person payments by source and service, with/without dementia; utilization (hospital, SNF, ED); coexisting-condition costs (Tables 16, 18, 19, 20, 21, 24).
- **Claims affected**: C08
- **Adopted elements**: per-capita cost tables and utilization rates.

## RW07: The Lewin Group — Lewin Model cost estimates/projections [A11]
- **DOI**: Not specified in paper (endnote A11)
- **Type**: imports
- **Delta**:
  - What changed: Total 2025 payments ($384B), payer mix, and 2050 projection (~$1T).
- **Claims affected**: C07
- **Adopted elements**: national cost total, payer shares, Figure 15, Medicaid state totals (Table 22).

## RW08: BRFSS caregiver module + NAC/AARP + DOL + Genworth [A7, A8, A9, 518, 519, 992]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Caregiver counts, hours, imputed value, and state-level caregiving/health tables (Tables 9-12); long-term-care cost benchmarks.
- **Claims affected**: C05, C06
- **Adopted elements**: caregiver totals, hours, value, health-status tables.

## RW09: Jack et al. — 2024 revised diagnostic/staging criteria [53]
- **DOI**: Not specified in paper (ref 53)
- **Type**: extends
- **Delta**:
  - What changed: Provides the clinical (0-6), biological (A-D via PET), and integrated staging framework adopted in the Overview (Tables 3A, 3B, 3C).
- **Claims affected**: C13 (treatment eligibility keyed to stages 3-4)
- **Adopted elements**: staging schema.

## RW10: American Geriatrics Society & Fried & Hall — workforce need model [807, 809, 813, 816]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Geriatrician counts and need estimates by state (Table 14); assumption of 700 patients/geriatrician and 30% complex-need share.
- **Claims affected**: C09
- **Adopted elements**: workforce supply/need figures.

## RW11: Projections Central — long-term occupational projections [Table 15 source]
- **DOI**: n/a (projectionscentral.org, accessed Jan 15, 2025)
- **Type**: imports
- **Delta**:
  - What changed: Home-health/personal-care aide job projections 2022-2032 (Table 15).
- **Claims affected**: C09
- **Adopted elements**: direct-care workforce growth projections.

## RW12: 2024 Lancet Commission on dementia prevention, intervention, and care [73, 124]
- **DOI**: Not specified in paper (refs 73, 124)
- **Type**: imports
- **Delta**:
  - What changed: 14 modifiable risk factors whose elimination might prevent nearly half of dementia cases worldwide (Figure 2 context).
- **Claims affected**: (background to problem.md G1/modifiable-risk concept)
- **Adopted elements**: modifiable risk-factor taxonomy.

## RW13: Versta Research / NORC AmeriSpeak — 2025 Special Report survey
- **DOI**: n/a (commissioned survey; probability panel)
- **Type**: imports
- **Delta**:
  - What changed: Primary attitudinal data (n=1,702, age 45+) underpinning the entire Special Report.
- **Claims affected**: C12
- **Adopted elements**: all survey percentages (Figures 19-26).

## RW14: RAND Corporation — anti-amyloid capacity/eligibility modeling [1056, 1060]
- **DOI**: Not specified in paper
- **Type**: bounds
- **Delta**:
  - What changed: Projects that capacity constraints and strict eligibility (only ~8% meeting lecanemab criteria; ~2.1M developing dementia while on wait lists 2020-2040) limit real-world treatment reach.
- **Claims affected**: C14
- **Adopted elements**: eligibility fraction and capacity-constraint estimates.

## Broader citation footprint (brief)
The report cites 1,000+ references. Beyond the anchors above, its footprint includes: FDA drug-approval and appropriate-use documentation for lecanemab/donanemab and ARABLE/ARIA management [55-58, 60, 1063]; the 2017/2019/2020/2022/2024 Facts and Figures Special Reports used for trend comparison [320, 805, 904, 1062, 1064, 1072]; APOE-genetics literature [83-102]; U.S. Census population projections [289, 290, 468, 469]; Global Burden of Disease/DALY estimates [477]; the RAISE Family Caregivers Act and CMS GUIDE Model policy documents [782-784]; collaborative-care model evaluations (Alzheimer's and Dementia Care Program, Care Ecosystem, Healthy Aging Brain Center, KAER) [714, 896-903]; and end-of-life/hospice and long-term-care financing sources [983-1016]. These are background, policy, or infrastructure references without a distinct competing-method delta.
