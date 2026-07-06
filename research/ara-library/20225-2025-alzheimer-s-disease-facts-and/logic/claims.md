# Claims

All numbers are copied exactly from the 2025 Alzheimer's Disease Facts and Figures report. Because this is a surveillance/synthesis report (not an experiment), reported statistics carry the `[result]` tag and are grounded to the report section/page (with page-of-119 label) whose verbatim text was opened and confirmed. Status is `supported` where the report presents the figure as an estimate it stands behind.

## C01: Current U.S. prevalence of Alzheimer's dementia (2025)
- **Statement**: An estimated 7.2 million Americans age 65 and older are living with Alzheimer's dementia in 2025; 74% are age 75 or older; about 1 in 9 (11%) of people age 65+ have Alzheimer's dementia, rising from 5.1% at ages 65-74 to 33.4% at age 85+.
- **Status**: supported
- **Falsification criteria**: A population-based re-estimate for 2025 using comparable methods yielding a materially different national count/age distribution would refute it.
- **Proof**: [E01]
- **Evidence basis**: Estimate derived from CHAP prevalence rates applied to 2024 U.S. Census projections (Rajan et al.); age breakdown in Figures 3-4.
- **Interpretation**: A single-site longitudinal source (CHAP) drives the headline number; biomarker-defined prevalence would likely be lower (see C_note in C02 interpretation and G2).
- **Sources**:
  - 7.2 million ← §3.2 p.21 «An estimated 7.2 million Americans age 65 and older are living with Alzheimer's dementia in 2025» [result]
  - 74% age 75+ ← §3.2 p.21 «Seventy-four percent are age 75 or older (Figure 3)» [result]
  - 1 in 9 (11%) ← §3.2 p.21 «About 1 in 9 people (11%) age 65 and older has Alzheimer's dementia» [result]
  - 5.1% to 33.4% ← §3.2 p.21 «from 5.1% of people age 65 to 74 up to 33.4% of people age 85 and older have Alzheimer's dementia (Figure 4)» [result]
- **Dependencies**: none
- **Tags**: prevalence, epidemiology, CHAP

## C02: Projected prevalence growth to 2060
- **Statement**: The number of people age 65+ with Alzheimer's dementia is projected to reach 13.8 million by 2060 (from ~6.1 million in 2020, 8.5M in 2030, 11.2M in 2040, 12.7M in 2050), barring breakthroughs to prevent or cure the disease.
- **Status**: supported
- **Falsification criteria**: Realized future prevalence materially below the projected trajectory (absent a preventive/curative breakthrough) would refute it.
- **Proof**: [E01]
- **Evidence basis**: CHAP-based projection (Rajan et al.); trajectory values read from Figure 7 data labels.
- **Interpretation**: Driven chiefly by growth of the 85+ population (projected 6.7M of the 13.8M, ~48%, by 2060).
- **Sources**:
  - 13.8 million by 2060 ← §3.11.1 p.30 «By 2060, the number of people age 65 and older with Alzheimer's dementia is projected to reach 13.8 million, barring the development of breakthroughs to prevent or cure Alzheimer's disease» [result]
  - 6.1 / 8.5 / 11.2 / 12.7 / 13.8 million (2020/2030/2040/2050/2060) ← Figure 7 p.30 data labels «6.1 … 8.5 … 11.2 … 12.7 … 13.8» [result]
  - 6.7 million (48%) age 85+ by 2060 ← §3.11.2 p.30 «By 2060, 6.7 million people age 85 and older are expected to have Alzheimer's dementia, accounting for about half (48%)» [result]
- **Dependencies**: C01
- **Tags**: projection, prevalence, population-aging

## C03: Mortality — official deaths, ranking, and 22-year trend
- **Statement**: 120,122 people died from Alzheimer's disease (underlying cause on death certificates) in 2022; AD was the seventh-leading cause of death across all ages in 2022 (sixth among those 65+); between 2000 and 2022 reported AD deaths increased 142.4% while deaths from most other leading causes fell.
- **Status**: supported
- **Falsification criteria**: Corrected CDC/NCHS mortality files showing a materially different 2022 count or trend would refute it.
- **Proof**: [E02]
- **Evidence basis**: CDC/NCHS final 2022 mortality data; Table 6 (state deaths total = 120,122; U.S. rate 36.0/100,000); Figure 9 percentage-change bars.
- **Interpretation**: The steep AD increase partly reflects population aging and increased reporting of AD on death certificates.
- **Sources**:
  - 120,122 deaths (2022) ← §4.1 p.31 «120,122 people died from Alzheimer's disease in 2022» [result]; corroborated by Table 6 p.35 «Total … 120,122 … 36.0» [result]
  - seventh-leading cause (2022) ← §4 p.31 «Alzheimer's disease was officially listed as the seventh-leading cause of death across all ages in the United States in 2022» [result]
  - 142.4% increase (2000-2022) ← §4.3 p.32 «the number of deaths from Alzheimer's disease as recorded on death certificates more than doubled, increasing 142.4%» [result]; Figure 9 p.33 label «142.4%» [result]
  - all-dementia deaths 292,881 (2022) ← §4.1 p.31 «some form of dementia was the officially recorded underlying cause of death for 292,881 individuals» [result]
- **Dependencies**: none
- **Tags**: mortality, CDC, death-certificates

## C04: Death certificates undercount Alzheimer's-attributable mortality
- **Statement**: Death-certificate counts understate AD-attributable deaths: a study estimated ~500,000 deaths among people 75+ in 2010 were attributable to Alzheimer's dementia, and ~14% of deaths among Americans 70+ (2000-2009) were attributable to dementia while only 5% of certificates listed it as the underlying cause.
- **Status**: supported
- **Falsification criteria**: Autopsy/attributable-risk studies converging on death-certificate counts would refute the undercount claim.
- **Proof**: [E03]
- **Evidence basis**: Rush MAP/ROS attributable-mortality estimate; HRS-based analysis.
- **Interpretation**: Reflects the "blurred distinction between death with dementia and death from dementia."
- **Sources**:
  - ~500,000 deaths 75+ (2010) ← §4.1 p.31 «500,000 deaths among people age 75 and older in the United States in 2010 could be attributed to Alzheimer's dementia» [result]
  - 14% attributable vs 5% certified ← §4.1 p.32 «about 14% of deaths among Americans age 70 and older from 2000 to 2009 were attributable to dementia, while only 5% of death certificates listed dementia as the underlying cause» [result]
- **Dependencies**: C03
- **Tags**: mortality, underreporting, attributable-risk

## C05: Unpaid caregiving — count, hours, and economic value (2024)
- **Statement**: In 2024, approximately 11.9 million family and other unpaid caregivers provided an estimated 19.2 billion hours of care to people with Alzheimer's or other dementias, valued at $413.5 billion (average ~31 hours/week, or 1,612 hours/year, per caregiver).
- **Status**: supported
- **Falsification criteria**: A re-estimate with the same BRFSS/wage methodology yielding a materially different value would refute it.
- **Proof**: [E04]
- **Evidence basis**: BRFSS caregiver module + Census + NAC/AARP + DOL + Genworth; Table 10 (U.S. totals: 11,926 thousand caregivers; 19,161 million hours; $413,454 million).
- **Interpretation**: Value uses a conservative wage (average of state minimum wage and median home-health-aide cost); true burden is likely higher.
- **Sources**:
  - 11.9 million caregivers ← §5.1.5 p.39 «the 11.9 million family and other unpaid caregivers» [result]; Table 10 p.40 «U. S. Total … 11,926» [result]
  - 19.2 billion hours ← §5.1 p.36 «provided an estimated 19.2 billion hours» [result]; Table 10 p.40 «19,161» (millions of hours) [result]
  - $413.5 billion ← §5.1.5 p.39 «$413.5 billion in 2024» [result]; Table 10 p.40 «413,454» (millions of dollars) [result]
  - 31 hours/week; 1,612 hours/year ← §5.1.5 p.39 «an average of nearly 31 hours of care per caregiver per week, or 1,612 hours of care per caregiver per year» [result]
- **Dependencies**: none
- **Tags**: caregiving, economic-value, BRFSS

## C06: Health burden of caregiving
- **Statement**: Dementia caregiving is associated with substantial harm: 59% of caregivers rate emotional stress as high or very high and 38% rate physical stress high to very high; depression prevalence among dementia caregivers is 30% to 40%, higher than among stroke (19%) or schizophrenia (20%) caregivers.
- **Status**: supported
- **Falsification criteria**: Controlled comparisons showing no elevated distress/depression among dementia caregivers would refute it.
- **Proof**: [E05]
- **Evidence basis**: Alzheimer's Association poll (Figure 12); meta-analyses; BRFSS (Tables 11, 12).
- **Interpretation**: Effects are consistently larger than for non-dementia caregivers, though some studies find a mortality-protective association.
- **Sources**:
  - 59% high/very-high emotional stress ← §5.1.6 p.41 «Fifty-nine percent of family caregivers of people with Alzheimer's or other dementias rated the emotional stress of caregiving as high or very high (Figure 12)» [result]
  - 38% high/very-high physical stress ← §5.1.6 p.43 «38% of Alzheimer's and other dementia caregivers indicate that the physical stress of caregiving is high to very high» [result]
  - depression 30%-40% ← §5.1.6 p.41 «The prevalence of depression is higher among dementia caregivers (30% to 40% as reported in multiple studies)» [result]
- **Dependencies**: C05
- **Tags**: caregiving, mental-health, morbidity

## C07: Total 2025 cost of care and payer mix
- **Statement**: Total payments in 2025 for health care, long-term care, and hospice for people 65+ with Alzheimer's or other dementias are estimated at $384 billion (excluding unpaid care); Medicare and Medicaid are expected to cover $246 billion (64%) and out-of-pocket spending $97 billion (25%).
- **Status**: supported
- **Falsification criteria**: A Lewin-Model re-run or actuarial reconciliation giving materially different totals/shares would refute it.
- **Proof**: [E06]
- **Evidence basis**: Lewin Model (endnote A11); Figure 15.
- **Interpretation**: Costs are projected to reach just under $1 trillion by 2050.
- **Sources**:
  - $384 billion (2025) ← §7 p.57 «Total payments in 2025 … are estimated at $384 billion (Figure 15)» [result]
  - $246 billion / 64% ← §7 p.57 «Medicare and Medicaid are expected to cover $246 billion, or 64%, of the total» [result]
  - $97 billion / 25% ← §7 p.57 «Out-of-pocket spending is expected to be $97 billion, or 25% of total payments» [result]
  - just under $1 trillion by 2050 ← §7.7 p.73 «projected to increase from $384 billion in 2025 to just under $1 trillion in 2050» [result]
- **Dependencies**: none
- **Tags**: cost, Medicare, Medicaid, Lewin-Model

## C08: Per-person Medicare/Medicaid cost differential
- **Statement**: Average per-person payments (2024 dollars) for Medicare beneficiaries 65+ with Alzheimer's or other dementias are nearly three times those without ($44,814 vs $15,053, all sources); average Medicaid payments are 22 times as great ($6,952 vs $313).
- **Status**: supported
- **Falsification criteria**: MCBS re-analysis showing the differentials are not ~3x (all-source) / ~22x (Medicaid) would refute it.
- **Proof**: [E06]
- **Evidence basis**: Medicare Current Beneficiary Survey 2018 (Table 16).
- **Interpretation**: The Medicaid gap is driven largely by long-term nursing-home care that Medicaid, not Medicare, covers.
- **Sources**:
  - ~3x; $44,814 vs $15,053 ← §7.1 p.58 «nearly three times as great … ($44,814 per person for those with dementia compared with $15,053 per person for those without dementia)» [result]; Table 16 p.59 «All sources … 44,814 … 15,053» [result]
  - 22x; $6,952 vs $313 ← §7.3.4 p.67 «Average annual Medicaid payments per person … ($6,952) were 22 times as great as average Medicaid payments for Medicare beneficiaries without Alzheimer's or other dementias ($313)» [result]; Table 16 p.59 «Medicaid … 6,952 … 313» [result]
- **Dependencies**: C07
- **Tags**: cost, per-capita, MCBS

## C09: Dementia-care workforce shortage
- **Statement**: The U.S. dementia-care workforce cannot meet demand: in 2021 there were only 7,454 certified geriatricians versus ~23,953 needed to serve the ~16.7 million older adults with complex needs, and ~18,142 geriatricians will be needed by 2050; an estimated 861,000 additional direct care workers are needed 2022-2032, with median direct-care wage $16.72/hour in 2023.
- **Status**: supported
- **Falsification criteria**: Workforce-supply data showing geriatrician/direct-care capacity meeting the modeled need would refute it.
- **Proof**: [E07]
- **Evidence basis**: American Geriatrics Society / Fried & Hall (Table 14); Projections Central (Table 15); PHI/DOL direct-care data.
- **Interpretation**: Shortage is most acute in rural areas and specific states (e.g., KY, MS, SC, TN, UT need ≥3x current geriatricians).
- **Sources**:
  - 7,454 geriatricians (2021) vs 23,953 needed ← §6.1.2 p.50 «there were only 7,454 certified geriatricians … at least 23,953 geriatricians were needed» [result]
  - 18,142 needed by 2050 ← §6.1.2 p.50 «an estimated 18,142 geriatricians will be needed … in 2050» [result]
  - 861,000 additional direct care workers ← §6.1.3 p.52 «just over 861,000 additional direct care workers will be needed between 2022 and 2032» [result]
  - $16.72/hour (2023) ← §6.1.3 p.53 «the median wage for direct care workers was $16.72 per hour» [result]
- **Dependencies**: none
- **Tags**: workforce, geriatricians, direct-care

## C10: Racial and ethnic disparities in prevalence/risk
- **Statement**: Alzheimer's dementia prevalence differs by race/ethnicity: CHAP data indicate 19% of Black and 14% of Hispanic adults age 65+ have Alzheimer's dementia versus 10% of White older adults; most studies find Black older adults about twice as likely, and some find Hispanic older adults about 1.5 times as likely, as White older adults.
- **Status**: supported
- **Falsification criteria**: Health/SES-adjusted cohort studies uniformly finding no group differences would refute the unadjusted disparity claim.
- **Proof**: [E08]
- **Evidence basis**: CHAP (Rajan et al.); multiple prevalence studies (§3.8).
- **Interpretation**: Differences are attributed largely to life-course, socioeconomic, and comorbidity factors rather than genetics.
- **Sources**:
  - 19% Black / 14% Hispanic / 10% White ← §3.8 p.28 «Data from the CHAP study indicates 19% of Black and 14% of Hispanic adults age 65 and older have Alzheimer's dementia compared with 10% of White older adults» [result]
  - ~2x (Black) ← §3.8 p.28 «Black older adults are about twice as likely to have Alzheimer's or other dementias as White older adults» [result]
- **Dependencies**: C01
- **Tags**: disparities, race-ethnicity, prevalence

## C11: Sex differences in prevalence
- **Statement**: Almost two-thirds of Americans with Alzheimer's are women; of the 7.2 million people 65+ with Alzheimer's dementia, 4.4 million are women and 2.8 million are men (12% of women vs 10% of men age 65+).
- **Status**: supported
- **Falsification criteria**: Same-age incidence studies plus survival modeling showing equal prevalent counts by sex would refute the descriptive claim.
- **Proof**: [E08]
- **Evidence basis**: CHAP (Rajan et al.), §3.7.
- **Interpretation**: The prevalence difference is attributed largely to women's longer survival; same-age incidence differences are not consistently found.
- **Sources**:
  - 4.4M women / 2.8M men ← §3.7 p.26 «Of the 7.2 million people age 65 and older with Alzheimer's dementia … 4.4 million are women and 2.8 million are men» [result]
  - two-thirds women; 12% vs 10% ← §3.7 p.26 «Almost two-thirds of Americans with Alzheimer's are women … This represents 12% of women and 10% of men age 65 and older» [result]
- **Dependencies**: C01
- **Tags**: sex-differences, prevalence

## C12: Public attitudes toward early detection and treatment (Special Report survey)
- **Statement**: In a survey of 1,702 U.S. adults age 45+, 99% said diagnosing Alzheimer's in early stages is important, 79% would want to know they had Alzheimer's before symptoms interfere with daily activities, more than 9 in 10 would want a simple test if available (91% presymptomatic, 95% postsymptomatic), and 64% were aware anti-amyloid medications that slow progression exist.
- **Status**: supported
- **Falsification criteria**: A comparably designed probability-panel survey yielding materially lower interest/awareness figures would refute it.
- **Proof**: [E09]
- **Evidence basis**: Versta Research / NORC AmeriSpeak probability panel, fielded Nov 7-18, 2024 (§8.6, Figures 19-26).
- **Interpretation**: Interest greatly exceeds knowledge (only 16% say they know a lot about AD; 9% know much about biomarker tests).
- **Sources**:
  - 99% early diagnosis important ← §8.6.1 p.76 «Nearly all (99%) Americans said it is important to diagnose Alzheimer's in the early stages of the disease» [result]
  - 79% want to know before symptoms interfere ← §8.6.1 p.76 «Nearly 4 in 5 Americans (79%) would want to know if they had Alzheimer's disease before experiencing symptoms or before symptoms interfere with daily activities» [result]
  - 91% presymptomatic / 95% postsymptomatic want simple test ← §8.6.1 p.76 «91% would want testing before symptoms appear (presymptomatic). - 95% would want testing when experiencing early symptoms (postsymptomatic)» [result]
  - 64% aware of anti-amyloid medications ← §8.6.2 p.77 «Nearly 2 in 3 Americans (64%) knew that anti-amyloid medications targeting underlying causes to slow disease progression exist» [result]
- **Dependencies**: none
- **Tags**: special-report, survey, public-attitudes, early-detection

## C13: Disease-modifying and symptomatic treatments and the trial pipeline
- **Statement**: Two FDA-approved anti-amyloid drugs — lecanemab (Leqembi) and donanemab (Kisunla) — change the underlying biology of Alzheimer's and slow decline in individuals with MCI or mild dementia (stages 3-4) and confirmed elevated beta-amyloid; as of January 1, 2024, 132 clinical trials were underway testing additional disease-modifying therapies and 30 trials testing agents for cognitive/behavioral/neuropsychiatric symptoms.
- **Status**: supported
- **Falsification criteria**: Evidence that the named drugs do not slow decline in the approved population, or a materially different pipeline count, would refute it.
- **Proof**: [E02] (pipeline/treatment landscape descriptive verification via cited trial registry counts)
- **Evidence basis**: §2.7.1; Figure 1 (FDA-approved treatments); Cummings et al. pipeline count.
- **Interpretation**: Aducanumab (Aduhelm), the first such approval (2021), was discontinued in 2024.
- **Sources**:
  - lecanemab & donanemab slow progression (stages 3-4) ← §2.7.1 p.10 «The drugs lecanemab (Leqembi) and donanemab (Kisunla) change the underlying biology of Alzheimer's disease and delay disease progression … approved for use in individuals with mild cognitive impairment (MCI) or mild dementia due to Alzheimer's (stages 3 and 4)» [result]
  - 132 disease-modifying trials (Jan 1, 2024) ← §2.7.1 p.11 «As of January 1, 2024, 132 clinical trials were underway testing additional disease-modifying therapies» [result]
  - 30 symptom trials ← §2.7.1 p.12 «As of January 1, 2024, 30 clinical trials were underway testing new agents to treat Alzheimer's cognitive, behavioral and neuropsychiatric symptoms» [result]
- **Dependencies**: none
- **Tags**: treatment, anti-amyloid, clinical-trials, pipeline

## C14: Anti-amyloid treatment market price and eligibility constraints
- **Statement**: The current market price of anti-amyloid treatment is $26,500 per person per year, and strict eligibility criteria sharply limit who can receive it — one study found only 8% of a dementia/MCI sample with a positive amyloid PET scan would meet lecanemab trial inclusion/exclusion criteria.
- **Status**: supported
- **Falsification criteria**: Documentation of a materially different list price or a much larger eligible fraction under trial criteria would refute it.
- **Proof**: [E06]
- **Evidence basis**: §7.7.1 (market price; RAND/eligibility modeling).
- **Interpretation**: Affordability and capacity constraints (infusion centers, PET/MRI monitoring) further restrict real-world access.
- **Sources**:
  - $26,500 per person per year ← §7.7.1 p.73 «the current market price of treatment is high, at $26,500 per person per year» [result]
  - 8% meet criteria ← §7.7.1 p.73 «only 8% of the sample would meet the lecanemab clinical trial inclusion and exclusion criteria» [result]
- **Dependencies**: C13
- **Tags**: treatment-access, cost, eligibility
