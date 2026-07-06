# Experiments (Data-Collection & Analysis Plans)

This report is a synthesis of surveillance, administrative, cohort, survey, and modeling data rather than a primary experimental study. Each "experiment" below is the declarative data-collection/analysis procedure the report relies on to produce a claim. **Directional only — no exact numbers** (those live in `evidence/`).

## E01: Population-based prevalence and projection estimation (CHAP + Census)
- **Verifies**: C01, C02, C04, C11
- **Setup**:
  - Data: Chicago Health and Aging Project (CHAP) — single-site community-based longitudinal cohort with systematic re-evaluation; U.S. Census Bureau population projections (2024 vintage). Cross-check: Health and Retirement Study (HRS) Harmonized Cognitive Assessment Protocol (HCAP).
  - System: analytical / epidemiological (no hardware).
- **Procedure**:
  1. Classify CHAP participants as having clinical Alzheimer's dementia by clinical symptoms.
  2. Derive age/sex/race-specific prevalence rates.
  3. Apply rates to Census population counts/projections to obtain national and by-age/by-sex numbers and future-year projections.
  4. For biological (biomarker) prevalence, apply stage-specific biomarker-positivity fractions (from a non-U.S. study and others) to population estimates.
- **Metrics**: Number and percentage of people with clinical Alzheimer's dementia (national, by age, by sex); projected counts by year; rough biomarker-based stage counts.
- **Expected outcome**: A multi-million prevalent population that increases with age and over time; biological definitions yield larger counts than clinical-symptom definitions.
- **Baselines**: HRS-HCAP (stricter, functional-impairment-requiring) estimates; alternative projection methods (e.g., Brookmeyer et al.).
- **Dependencies**: none.

## E02: Mortality surveillance from death certificates (CDC/NCHS)
- **Verifies**: C03
- **Setup**: Data: CDC/NCHS final mortality files (death certificates; CDC WONDER), 2000-2024, all ages and by age group; underlying-cause-of-death coding.
- **Procedure**:
  1. Count deaths with Alzheimer's disease as the underlying cause, by year, age group, and state.
  2. Compute crude death rates per 100,000; compute percentage change vs 2000 and vs other leading causes.
  3. Rank AD among causes of death overall and among those 65+.
- **Metrics**: Number of AD deaths; death rate per 100,000 (overall, by age, by state); percentage change over time; cause-of-death rank.
- **Expected outcome**: AD mortality rises over the period (with a COVID-era peak then decline) while several other leading causes fall; official counts undercount AD's true contribution.
- **Baselines**: Death rates for heart disease, stroke, HIV, cancers (Figure 9); attributable-mortality studies (Rush/ROS, HRS).
- **Dependencies**: none.

## E03: Lifetime-risk estimation by sex (Framingham)
- **Verifies**: C04
- **Setup**: Data: Framingham Heart Study, dementia-free survivors to age 45 and to age 65, followed to 2009; DSM-IV and NINCDS-ADRDA diagnostic criteria.
- **Procedure**:
  1. Follow cohort for incident dementia/Alzheimer's with ≥6-month symptom survival requirement.
  2. Estimate remaining-lifetime probability of clinical Alzheimer's dementia at index ages 45 and 65, by sex.
- **Metrics**: Lifetime risk (%) by sex at ages 45 and 65.
- **Expected outcome**: Higher lifetime risk for women than men at both index ages.
- **Baselines**: Male vs female comparison within the same cohort.
- **Dependencies**: E01.

## E04: Race/ethnicity-stratified prevalence and disparity attribution
- **Verifies**: C05
- **Setup**: Data: CHAP by race/ethnicity; Medicare diagnosis data; APOE genotype frequency studies (Kataoka et al., Belloy et al.).
- **Procedure**:
  1. Estimate prevalence of clinical Alzheimer's dementia by racial/ethnic group.
  2. Compare genetic (APOE) frequencies and adjust for social/economic/health covariates.
- **Metrics**: Prevalence (%) by group; APOE pair frequencies; residual disparity after adjustment.
- **Expected outcome**: Higher prevalence in Black and Hispanic older adults; disparities not explained by genetics and largely attenuated by social/health factors.
- **Baselines**: Non-Hispanic White older adults.
- **Dependencies**: E01.

## E05: Estimating unpaid-caregiver counts, hours, and economic value (BRFSS + NAC/AARP)
- **Verifies**: C06
- **Setup**: Data: Behavioral Risk Factor Surveillance System (BRFSS) caregiver module (all states since 2016; 2016, 2020-2024 waves); National Alliance for Caregiving (NAC)/AARP survey (for imputing dementia-as-secondary-condition pre-2019); U.S. Census population; state minimum wages; Genworth median home-health-aide costs.
- **Procedure**:
  1. Identify BRFSS respondents caregiving for someone with dementia (as main or secondary condition; impute pre-2019 using NAC/AARP ratio).
  2. Apply caregiving percentages to state adult populations to count caregivers.
  3. Convert reported weekly-hours bands (midpoint method) to annual hours × caregivers.
  4. Value hours at the average of state minimum wage and median home-health-aide wage; sum across states.
- **Metrics**: Number of caregivers; total unpaid hours; economic value (dollars), national and by state.
- **Expected outcome**: Tens of billions of care hours worth hundreds of billions of dollars.
- **Baselines**: Non-dementia caregivers; prior-year Facts and Figures estimates.
- **Dependencies**: none.

## E06: Comparative analysis of caregiver burden and health
- **Verifies**: C07
- **Setup**: Data: BRFSS caregiver health module (by state); National Study of Caregiving / National Health and Aging Trends Study; meta-analyses of caregiver depression/anxiety; comparison groups = non-dementia caregivers and non-caregivers.
- **Procedure**:
  1. Compare self-reported stress, depression, anxiety, chronic conditions, hours, and work impacts between dementia caregivers and comparators.
- **Metrics**: % reporting high/very-high stress; depression/anxiety prevalence; chronic-condition prevalence; hours of care; work-related changes.
- **Expected outcome**: Dementia caregivers show greater burden, worse mental/physical health, and more work disruption than comparators (unadjusted comparisons noted).
- **Baselines**: Non-dementia caregivers; non-caregivers.
- **Dependencies**: E05.

## E07: Workforce supply-versus-need modeling
- **Verifies**: C08
- **Setup**: Data: American Geriatrics Society geriatrician counts (2021); assumptions (30% of 65+ need geriatrician care; 700 patients per geriatrician); age-specific Alzheimer's prevalence (Figure 5); state 2050 population projections (Weldon Cooper Center); Bureau of Labor Statistics direct-care employment/projections and wages; state occupational projections (Projections Central).
- **Procedure**:
  1. Compute geriatricians needed (overall and to serve those with Alzheimer's) per state for 2050; compare to 2021 supply.
  2. Project home-health/personal-care aide jobs 2022-2032; summarize turnover and wages.
- **Metrics**: Geriatricians available vs needed (by state, national); projected aide-job growth; turnover rate; median wage.
- **Expected outcome**: A large and widening shortfall, worst in rural areas.
- **Baselines**: 2021 supply; comparison across states.
- **Dependencies**: E01.

## E08: Cost estimation (Lewin Model + Medicare/MCBS claims)
- **Verifies**: C09
- **Setup**: Data: Lewin Group model (total 2026/2050 payments by source, with separately added anti-amyloid drug spend); Medicare Current Beneficiary Survey 2018 (Health Care Cost Institute analysis); National 100% Sample Medicare Fee-for-Service 2019; CMS per-capita payment data; CPI medical-care components for inflation to 2025/2026 dollars.
- **Procedure**:
  1. Estimate total payments by payment source for people 65+ with AD/other dementias (2026, projected 2050).
  2. Compute per-person payments by source, service type, coexisting condition, race/ethnicity, and state; compare with/without dementia.
- **Metrics**: Total payments (national, state); per-person payments and with/without-dementia ratios; out-of-pocket burden.
- **Expected outcome**: Costs concentrated in Medicare/Medicaid, per-person payments several-fold higher with dementia, rising toward ~$1T by 2050.
- **Baselines**: Beneficiaries without Alzheimer's/other dementias, same age group.
- **Dependencies**: E01.

## E09: Underdiagnosis assessment
- **Verifies**: C10
- **Setup**: Data: comparison of population-based prevalence (CHAP/HRS) to health-system diagnosis; Medicare beneficiary self-report of being told; MCI diagnosis-rate study.
- **Procedure**:
  1. Contrast the share meeting diagnostic criteria with the share diagnosed/aware; stratify by stage and race/ethnicity.
- **Metrics**: Share undiagnosed; share unaware of diagnosis; MCI diagnosis rate.
- **Expected outcome**: Large undiagnosed/unaware fractions, greatest at mild/MCI stages and among Black and Hispanic older adults.
- **Baselines**: Population prevalence as the reference "true" count.
- **Dependencies**: E01.

## E10: U.S. POINTER randomized controlled trial
- **Verifies**: C13
- **Setup**:
  - Design: multi-site, 2-year randomized controlled trial; >2,100 participants at elevated risk for cognitive decline, racially/ethnically diverse; assigned to peer teams.
  - Arms: structured multidomain lifestyle intervention (38 facilitated peer sessions; prescribed aerobic/resistance/flexibility exercise; MIND-diet adherence; cognitive training; semiannual clinical review of cholesterol, HbA1c, blood pressure) vs self-guided intervention (educational materials; six peer meetings; annual monitoring; no individualized coaching).
- **Procedure**:
  1. Randomize; deliver interventions over 2 years; measure change in cognitive function.
  2. Compare cognitive improvement between arms.
- **Metrics**: Global cognitive composite change (directional/between-group comparison).
- **Expected outcome**: Both arms improve; the structured arm improves significantly more than the self-guided arm.
- **Baselines**: Self-guided arm.
- **Dependencies**: E13.

## E11: U-M National Poll on Healthy Aging (Special Report survey)
- **Verifies**: C14
- **Setup**:
  - Instrument: nationally representative survey of U.S. adults age 40+; n=3,829; fielded Dec 29, 2025-Jan 13, 2026; NORC AmeriSpeak probability panel (Univ. of Chicago); oversamples of American Indian/Alaska Native (n=162), Asian (n=298), Black (n=495), Hispanic (n=485); weighted to Census totals; offered in English online or by phone.
- **Procedure**:
  1. Ask about definitions/importance of brain health, belief in and engagement with brain-health behaviors, interest in POINTER-style programs, decision factors, preferred age to act, and preferred information sources.
  2. Tabulate weighted percentages; stratify by age, gender, race/ethnicity, family history, education, income.
- **Metrics**: % endorsing each perception/behavior/preference; subgroup differences.
- **Expected outcome**: High valuation of brain health but low knowledge and rare clinician conversations; strong program interest gated by cost.
- **Baselines**: Cross-subgroup comparisons.
- **Dependencies**: none.

## E12: Evidence synthesis on anti-amyloid therapies
- **Verifies**: C12
- **Setup**: Data: phase-3 trials of lecanemab and donanemab; ARIA meta-analysis (n=6,315); analyses of long-term progression and IADL independence; real-world eligibility analysis.
- **Procedure**:
  1. Summarize amyloid clearance (TRAC), cognitive/functional slowing vs placebo, progression-risk reduction, ARIA incidence, and eligible-population fraction.
- **Metrics**: Amyloid-negativity conversion; progression-risk reduction; ARIA-E/ARIA-H incidence; % meeting trial eligibility.
- **Expected outcome**: Statistically significant slowing of decline at early stages with meaningful ARIA risk and narrow eligibility.
- **Baselines**: Placebo arms; untreated comparators.
- **Dependencies**: none.

## E13: Attributable-fraction analysis of modifiable risk factors
- **Verifies**: C15
- **Setup**: Data: 2024 Lancet Commission (14 factors, worldwide); U.S. cohort study (>375,000, 8 factors); Multiethnic Cohort Study (~92,000).
- **Procedure**:
  1. Estimate population attributable fractions for eliminating modifiable risk factors, overall and by population subgroup.
- **Metrics**: Population attributable fraction (% of dementia cases attributable), overall and by group.
- **Expected outcome**: A substantial minority-to-near-half of dementia cases attributable to modifiable factors, varying by population.
- **Baselines**: Between-group comparison of attributable fractions.
- **Dependencies**: none.
