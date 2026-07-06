# Experiments (Estimation & Analysis Plans)

For a surveillance/synthesis report, an "experiment" is the estimation or analysis procedure the report uses to produce and support a claim. These are declarative and directional only; exact numbers live in `evidence/` and `claims.md`.

## E01: National and state prevalence/projection estimation (CHAP × Census)
- **Verifies**: C01, C02, C10, C11
- **Setup**:
  - Population source: U.S. Census Bureau 2024 population projections (national and state)
  - Cohort source: Chicago Health and Aging Project (CHAP), a population-based longitudinal study of chronic conditions in older people; state maps from Dhana et al.
  - Comparator: Health and Retirement Study HCAP (all-cause dementia)
  - System: analytical (age/sex/race-stratified prevalence rates applied to population denominators)
- **Procedure**:
  1. Estimate age-, sex-, and race/ethnicity-specific Alzheimer's dementia prevalence from CHAP.
  2. Apply those rates to Census population counts/projections to obtain national and state counts.
  3. Project forward to 2060 under the assumption of no preventive/curative breakthrough.
  4. Report age breakdown and demographic differences.
- **Metrics**: number and percentage of people with Alzheimer's dementia, by age band, sex, race/ethnicity, state, and projection year.
- **Expected outcome**: Prevalence increases with age and over time; women and Black/Hispanic older adults show higher prevalence than men and White older adults, respectively.
- **Baselines**: HRS-HCAP all-cause dementia estimate; prior CHAP editions (Brookmeyer et al. as a lower-bound alternative).
- **Dependencies**: none

## E02: Death-certificate mortality counting and cause-of-death trend analysis
- **Verifies**: C03, C13
- **Setup**:
  - Data: CDC/NCHS final national mortality files (underlying cause of death), 2000-2022; state files for 2022; treatment/pipeline registry counts.
  - System: analytical (ICD underlying-cause tabulation; percentage-change computation across causes)
- **Procedure**:
  1. Tabulate deaths with Alzheimer's disease as underlying cause, nationally and by state, for 2022.
  2. Compute percentage change in AD deaths and comparator causes (heart disease, stroke, HIV, cancers) 2000-2022.
  3. Compute age-specific death rates per 100,000 over time.
  4. Enumerate the disease-modifying / symptomatic trial pipeline as of a fixed date.
- **Metrics**: death counts, mortality rate per 100,000 (crude), percentage change, cause-of-death ranking, trial counts.
- **Expected outcome**: AD deaths rise sharply while most comparator causes fall or change little; death rates rise most at age 85+.
- **Baselines**: Other leading causes of death (heart disease #1).
- **Dependencies**: none

## E03: Attributable-mortality estimation
- **Verifies**: C04
- **Setup**:
  - Data: Rush Memory and Aging Project / Religious Orders Study; Health and Retirement Study.
  - System: analytical (compare death risk in those with vs. without Alzheimer's dementia)
- **Procedure**:
  1. Estimate excess deaths attributable to Alzheimer's dementia by comparing mortality risk with and without the condition.
  2. Compare attributable estimates against death-certificate underlying-cause counts.
- **Metrics**: attributable deaths; ratio of attributable to certificate-listed deaths.
- **Expected outcome**: Attributable mortality substantially exceeds death-certificate counts.
- **Baselines**: Death-certificate underlying-cause counts (E02).
- **Dependencies**: E02

## E04: Unpaid caregiver count, hours, and economic-value imputation
- **Verifies**: C05
- **Setup**:
  - Data: BRFSS caregiver module (2016, 2020-2023); U.S. Census; National Alliance for Caregiving / AARP; U.S. Department of Labor; Genworth Cost of Care.
  - System: analytical (survey-weighted counts × hours × imputed wage)
- **Procedure**:
  1. Identify unpaid caregivers of people with Alzheimer's/other dementias from BRFSS.
  2. Estimate total caregivers and hours nationally and by state.
  3. Value hours at the average of the state minimum wage and median home-health-aide hourly cost (conservative).
- **Metrics**: number of caregivers, hours of care, imputed dollar value.
- **Expected outcome**: Large national totals; per-caregiver hours have risen while caregiver counts have declined.
- **Baselines**: Prior editions; non-dementia caregivers (hours comparison).
- **Dependencies**: none

## E05: Caregiver health-outcome comparison
- **Verifies**: C06
- **Setup**:
  - Data: Alzheimer's Association caregiver poll; BRFSS; published meta-analyses.
  - System: analytical (compare dementia caregivers vs. non-dementia caregivers vs. non-caregivers)
- **Procedure**:
  1. Measure emotional/physical stress, depression, anxiety, chronic conditions among dementia caregivers.
  2. Compare against non-dementia caregivers and non-caregivers.
- **Metrics**: prevalence of high stress, depression, anxiety, and chronic conditions.
- **Expected outcome**: Dementia caregivers report worse mental and physical health than comparison groups.
- **Baselines**: Non-dementia caregivers; stroke/schizophrenia caregivers.
- **Dependencies**: E04

## E06: Cost-of-care estimation (Lewin Model + MCBS + Medicare claims)
- **Verifies**: C07, C08, C14
- **Setup**:
  - Data: Lewin Model (national total payments/projection); Medicare Current Beneficiary Survey 2018; National 100% Sample Medicare Fee-for-Service 2019; Genworth.
  - System: analytical (payer-source and service-type payment estimation; projection to 2050)
- **Procedure**:
  1. Estimate total 2025 payments and payer mix for people 65+ with dementia.
  2. Compute average per-person payments by source and service, with vs. without dementia.
  3. Project total payments to 2050; assess treatment price/eligibility implications.
- **Metrics**: total and per-person payments (2024/2025 dollars); payer shares; projected totals; treatment price and eligible fraction.
- **Expected outcome**: Costs far higher for people with dementia; large projected growth; treatment access constrained by price and eligibility.
- **Baselines**: Medicare beneficiaries without dementia.
- **Dependencies**: none

## E07: Workforce supply-vs-need projection
- **Verifies**: C09
- **Setup**:
  - Data: American Geriatrics Society (geriatrician counts); Fried & Hall (need model); Projections Central long-term occupational projections; PHI/DOL direct-care data.
  - System: analytical (need = population × complex-need share ÷ patients-per-clinician; compare to supply)
- **Procedure**:
  1. Estimate geriatricians needed (assuming 30% of 65+ need geriatric care, 700 patients each) vs. certified supply, by state and year.
  2. Project direct-care worker demand 2022-2032.
- **Metrics**: geriatricians available vs. needed; direct-care workers needed; wages.
- **Expected outcome**: Persistent, worsening shortages, most acute in rural states.
- **Baselines**: Current supply (2021 geriatricians; 2022 direct-care counts).
- **Dependencies**: none

## E08: Demographic-subgroup prevalence/risk comparison
- **Verifies**: C10, C11
- **Setup**:
  - Data: CHAP; Framingham Heart Study (lifetime risk); multiple cohort/prevalence studies.
  - System: analytical (stratified prevalence and lifetime-risk estimation by sex, race/ethnicity)
- **Procedure**:
  1. Compare Alzheimer's dementia prevalence across sex and racial/ethnic groups.
  2. Estimate sex-specific lifetime risk at ages 45 and 65.
- **Metrics**: prevalence by group; lifetime risk by sex.
- **Expected outcome**: Higher prevalence in women and in Black/Hispanic older adults; lifetime risk higher for women.
- **Baselines**: White older adults; men.
- **Dependencies**: E01

## E09: Public-attitudes survey and focus groups (Special Report)
- **Verifies**: C12
- **Setup**:
  - Sample: 1,702 U.S. adults age 45+, NORC AmeriSpeak probability panel (oversamples: Hispanic n=296, Black n=309, Asian n=282, Native n=166), weighted to Census totals; fielded Nov 7-18, 2024 (Versta Research).
  - Complement: 11 focus groups, 69 participants (L&M Policy Research).
  - System: online/phone survey in English and Spanish.
- **Procedure**:
  1. Measure worry, knowledge, attitudes about early detection/diagnosis, willingness to test, and attitudes toward anti-amyloid treatment and its risks/logistics.
  2. Compare across demographic subgroups and family-history status.
  3. Triangulate with focus-group themes.
- **Metrics**: percentages endorsing each attitude/awareness item, overall and by subgroup.
- **Expected outcome**: High valuation of and interest in early diagnosis and simple testing that exceeds actual knowledge; interest is robust to treatment risk and monthly-infusion logistics.
- **Baselines**: 2022 Special Report MCI survey (trend comparison).
- **Dependencies**: none
