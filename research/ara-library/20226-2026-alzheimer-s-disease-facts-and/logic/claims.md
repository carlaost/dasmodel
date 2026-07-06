# Claims

Falsifiable epidemiological, economic, and survey assertions made by the report. Because this is a descriptive surveillance/economics report (not an experimental study), "Status: supported" means the report presents the value/finding as an estimate derived from the cited data source(s); load-bearing numbers are grounded in the specific figure/table/section where the report states them. `Proof` references the data-collection/analysis "experiments" (E01-E13) in `experiments.md`.

## C01: Prevalence and projected growth of clinical Alzheimer's dementia
- **Statement**: An estimated 7.4 million Americans age 65+ live with clinical Alzheimer's dementia in 2026, projected to reach 13.8 million by 2060 absent prevention/cure breakthroughs.
- **Status**: supported
- **Falsification criteria**: An updated CHAP/Census-based national estimate materially different from 7.4M (2026) or 13.8M (2060), or an alternative population-based method yielding a substantially different count without reconciling the difference.
- **Proof**: [E01]
- **Evidence basis**: Abstract; §3.2; §3.12.1; Figure 4 (7.4M total); Figure 8 (6.1M in 2020 → 13.8M in 2060); Box 1; endnotes A2, A5.
- **Interpretation**: Growth is driven by population aging, not necessarily rising age-specific risk (which may be declining).
- **Dependencies**: C02, C11.
- **Tags**: prevalence, projection, CHAP, aging
- **Sources**:
  - 7.4 million ← §3.2 / Figure 4 «An estimated 7.4 million Americans age 65 and older are living with clinical Alzheimer's dementia in 2026» [result]
  - 13.8 million by 2060 ← §3.12.1 / Figure 8 «the number of people age 65 and older with clinical Alzheimer's dementia is projected to reach 13.8 million» [result]
  - 6.1 million in 2020 ← Figure 8 data label «2020 | 6.1» [result]

## C02: Prevalence rises steeply with age
- **Statement**: The percentage of people with clinical Alzheimer's dementia increases with age: 5.2% at 65-74, 13.8% at 75-84, and 35.8% at 85+.
- **Status**: supported
- **Falsification criteria**: Age-specific prevalence rates from the same CHAP-based method differing materially from 5.2/13.8/35.8%.
- **Proof**: [E01]
- **Evidence basis**: §2.4.1; §3.2; Figure 5.
- **Interpretation**: Age is the dominant (non-modifiable) risk factor; the 85+ segment drives future growth.
- **Dependencies**: C01.
- **Tags**: prevalence, age
- **Sources**:
  - 5.2% / 13.8% / 35.8% ← Figure 5 data labels «65-74 | 5.2% ... 75-84 | 13.8% ... 85+ | 35.8%» [result]; also stated in §2.4.1 «5.2% have Alzheimer's dementia; age 75 to 84, 13.8%; and age 85 or older, 35.8%» [result]

## C03: Rising Alzheimer's mortality against falling other-cause mortality
- **Statement**: 116,022 people died from Alzheimer's disease in 2024 (AD was the 6th-leading cause of death overall, 5th among those 65+); between 2000 and 2024 reported AD deaths rose 134.1% while heart-disease deaths fell 3.8%.
- **Status**: supported
- **Falsification criteria**: CDC/NCHS final 2024 mortality data showing a materially different AD death count or a non-increase over 2000, or a different cause-of-death ranking.
- **Proof**: [E02]
- **Evidence basis**: Abstract; §4.1-4.4; Figure 9 (+134.1% AD; -3.8% heart disease); Figure 10 (rate by year); Tables 6, 7.
- **Interpretation**: The rise reflects both true aging-driven increase and increasing physician reporting of AD on death certificates; official counts still undercount AD's mortality contribution.
- **Dependencies**: none.
- **Tags**: mortality, CDC, death-certificates
- **Sources**:
  - 116,022 deaths in 2024 ← §4.1 / Table 6 total «116,022 people died from Alzheimer's disease in 2024» [result]
  - +134.1% (AD) and -3.8% (heart disease) 2000-2024 ← Figure 9 data labels / §4.2 «increasing 134.1%, while the number of deaths from the number-one cause of death (heart disease) decreased 3.8%» [result]
  - 6th overall / 5th among 65+ in 2024 ← §4 opening «Alzheimer's disease was officially listed as the sixth-leading cause of death in the United States in 2024 ... the fifth-leading cause of death among individuals age 65 and older in 2024» [result]

## C04: Women bear a disproportionate share of Alzheimer's
- **Statement**: Almost two-thirds of Americans with Alzheimer's are women; of 7.4M people 65+ with clinical AD dementia, 4.5M are women and 2.9M are men; estimated lifetime risk at age 45 is 19.5% (women) vs 10.3% (men).
- **Status**: supported
- **Falsification criteria**: Sex-specific prevalence/lifetime-risk estimates from the same sources not showing a female excess.
- **Proof**: [E01, E03]
- **Evidence basis**: §3.8; Figure 7 (lifetime risk by sex); Table 9.
- **Interpretation**: The excess is substantially attributable to women's greater longevity and possible survival bias in men; whether age-specific incidence differs by sex is unclear.
- **Dependencies**: C01.
- **Tags**: sex-differences, lifetime-risk, Framingham
- **Sources**:
  - 4.5M women / 2.9M men ← §3.8 «4.5 million are women and 2.9 million are men» [result]
  - lifetime risk age 45: 19.5% women / 10.3% men ← Figure 7 data labels «45 | 10.3% | 19.5%» [result]

## C05: Racial and ethnic disparities in prevalence, driven by social/health factors
- **Statement**: Black (19%) and Hispanic (14%) older adults have higher clinical Alzheimer's dementia prevalence than White older adults (10%); genetic factors do not account for these differences, which are attributed largely to social, economic, and health conditions.
- **Status**: supported
- **Falsification criteria**: Rigorous analyses adjusting for social/health factors that leave a large unexplained racial gap, or genetic evidence explaining the gap.
- **Proof**: [E04]
- **Evidence basis**: §3.9 (CHAP: 19% Black, 14% Hispanic, 10% White); Table 4 (APOE frequencies); Table 24 (spending by race).
- **Interpretation**: Disparities also manifest in diagnosis rates and cost/utilization patterns (e.g., higher Medicare payments for Black beneficiaries).
- **Dependencies**: C01.
- **Tags**: disparities, race-ethnicity, social-determinants
- **Sources**:
  - 19% Black / 14% Hispanic / 10% White ← §3.9 «19% of Black and 14% of Hispanic adults age 65 and older have clinical Alzheimer's dementia compared with 10% of White older adults» [result]

## C06: Scale and economic value of unpaid caregiving
- **Statement**: In 2025, 12.7 million (12,734 thousand) family and other unpaid caregivers provided an estimated 19.6 billion (19,608 million) hours of care, valued at $446.3 billion ($446,312 million).
- **Status**: supported
- **Falsification criteria**: A re-derivation from BRFSS/NAC-AARP inputs and the stated valuation method yielding a materially different national hours or dollar total.
- **Proof**: [E05]
- **Evidence basis**: Abstract; §5.1.5; Table 10 U.S. totals; endnotes A7, A8, A9.
- **Interpretation**: Value is a conservative estimate (average of state minimum wage and median home-health-aide wage); it excludes lost productivity and caregiver health costs.
- **Dependencies**: none.
- **Tags**: caregiving, economic-value, BRFSS
- **Sources**:
  - 12,734 thousand caregivers / 19,608 million hours / $446,312 million ← Table 10 U.S. Total row «U.S. Total | 12,734 | 19,608 | 446,312» [result]; also §5.1.5 «12.7 million family and other unpaid caregivers ... provided an estimated 19.6 billion hours ... $446.3 billion in 2025» [result]

## C07: Dementia caregiving is more burdensome and health-damaging than non-dementia caregiving
- **Statement**: Dementia caregivers report higher stress (59% rate emotional stress high/very high), higher depression prevalence (30-40%) and more chronic conditions than non-dementia caregivers, and provide more care (92 vs 65 hours/month).
- **Status**: supported
- **Falsification criteria**: Comparative caregiver studies showing no excess burden/health harm for dementia vs non-dementia caregivers.
- **Proof**: [E06]
- **Evidence basis**: §5.1.6; Figure 12 (59% emotional, 38% physical); Figure 11; Figure 13; Tables 11, 12.
- **Interpretation**: Differences arise because dementia caregivers spend more time and assume more/complex tasks.
- **Dependencies**: C06.
- **Tags**: caregiver-health, burden, depression
- **Sources**:
  - 59% emotional stress high/very high ← Figure 12 / §5.1.6 «Fifty-nine percent of family caregivers ... rated the emotional stress of caregiving as high or very high» [result]
  - 92 vs 65 hours/month ← §5.1.4 «providing 27 hours more care per month on average (92 hours versus 65 hours) than caregivers of people without dementia» [result]
  - depression 30-40% ← §5.1.6 «The prevalence of depression is higher among dementia caregivers (30% to 40% as reported in multiple studies)» [result]

## C08: The dementia care workforce is insufficient and worsening
- **Statement**: In 2021 there were far fewer geriatricians than needed (Table 14 U.S. total 7,066; text states 7,454 certified) versus ~23,953 needed in 2021 and 32,521 projected needed by 2050; direct-care turnover is ~79% (home care) to ~99% (nursing assistants) with a 2024 median wage of $17.36/hr.
- **Status**: supported
- **Falsification criteria**: Workforce data showing supply meeting projected need, or turnover/wage figures materially different from those cited.
- **Proof**: [E07]
- **Evidence basis**: §6.1.1; §6.1.3; Table 14; Table 15.
- **Interpretation**: Shortages are worst in rural areas and threaten capacity to deliver biomarker testing and anti-amyloid therapy.
- **Dependencies**: C01.
- **Tags**: workforce, geriatricians, direct-care
- **Sources**:
  - 23,953 needed / 7,454 certified in 2021 ← §6.1.1 «at least 23,953 geriatricians were needed to care for them ... there were only 7,454 certified geriatricians in 2021» [result]
  - Table 14 U.S. total 7,066 (2021) and 32,521 (2050, all needing care) ← Table 14 U.S. Total row «7,066 | 14,656 | 32,521» [result]  (NOTE: an internal source discrepancy — text 7,454 vs table 7,066 — is preserved verbatim; see table14.md)
  - direct-care median wage $17.36/hr (2024); turnover 79%/99% ← §6.1.3 «the median wage for direct care workers was $17.36 per hour ... median rate of 79% annually for direct care workers providing home care and 99% for nursing assistants in nursing homes» [result]

## C09: Costs are large, concentrated in public programs, and rising
- **Statement**: Total 2026 payments for people 65+ with AD/other dementias are estimated at $409 billion (Medicare+Medicaid = $263B, 64%; out-of-pocket $103B, 25%); per-person total payments are ~3x higher for Medicare beneficiaries with dementia ($46,141 vs $15,499) and Medicaid payments ~22x ($7,158 vs $322).
- **Status**: supported
- **Falsification criteria**: A re-run of the Lewin Model / MCBS analysis giving a materially different 2026 total or per-person ratio.
- **Proof**: [E08]
- **Evidence basis**: Abstract; §7 opening; §7.1; Figure 15 ($409B pie); Table 16; Tables 18-24.
- **Interpretation**: Total cost is projected to approach ~$1 trillion by 2050; excludes the value of unpaid caregiving (C06).
- **Dependencies**: C01, C05.
- **Tags**: costs, Medicare, Medicaid, Lewin-model
- **Sources**:
  - $409 billion total 2026; $263B (64%) Medicare+Medicaid; $103B (25%) out-of-pocket ← §7 opening / Figure 15 «Total payments in 2026 ... estimated at $409 billion ... Medicare and Medicaid are expected to cover $263 billion, or 64% ... Out-of-pocket spending is expected to be $103 billion, or 25%» [result]
  - $46,141 vs $15,499 (all sources); $7,158 vs $322 (Medicaid) ← Table 16 rows «All sources | 46,141 | 15,499» and «Medicaid | 7,158 | 322» [result]

## C10: Alzheimer's and other dementias are substantially underdiagnosed
- **Statement**: A large share of people meeting diagnostic criteria are undiagnosed; only about half of Medicare beneficiaries with a dementia diagnosis report being told; one estimate finds only 8% of older Americans with MCI receive a diagnosis.
- **Status**: supported
- **Falsification criteria**: Health-system data showing diagnosis rates approaching population prevalence, or MCI diagnosis rates far above 8%.
- **Proof**: [E09]
- **Evidence basis**: §3.3.
- **Interpretation**: Underdiagnosis is greatest at the earliest (mild/MCI) stages and among Black and Hispanic older adults; biological (biomarker) definitions would further widen the diagnosed-vs-eligible gap.
- **Dependencies**: C01.
- **Tags**: underdiagnosis, MCI, disparities
- **Sources**:
  - ~half told of diagnosis ← §3.3 «only about half of Medicare beneficiaries who have a diagnosis of Alzheimer's or another dementia in their Medicare billing records report being told of the diagnosis» [result]
  - 8% of MCI diagnosed ← §3.3 «only 8% of older Americans living with MCI receive a diagnosis» [result]

## C11: Biological (biomarker) definitions imply a much larger affected population
- **Statement**: Under biomarker-based definitions, roughly 4.5M Americans 65+ have dementia due to AD (stages 4-6), ~4.2M have MCI due to AD (stage 3), and ~19M (≈30% of older adults) fall somewhere in stages 1-6 of the AD continuum.
- **Status**: hypothesis
- **Falsification criteria**: U.S. population-based biomarker studies yielding materially different stage-specific counts than the report's rough extrapolations.
- **Proof**: [E01]
- **Evidence basis**: Box 1 (§3.1); Tables 1, 3A-3C; §2.1.1 (biomarkers).
- **Interpretation**: These are explicitly labeled rough initial estimates, based largely on a non-U.S. (Norwegian) study and clinic-based samples, carrying substantial uncertainty (Assumption A5).
- **Dependencies**: C01.
- **Tags**: biomarkers, biological-definition, staging, uncertainty
- **Sources**:
  - ~4.5M (stages 4-6), ~4.2M (stage 3), ~19M (stages 1-6, ~30%) ← Box 1 «roughly 4.5 million Americans ... dementia due to Alzheimer's disease» / «roughly 7% – or 4.2 million older Americans – may have MCI due to Alzheimer's disease» / «sums to approximately 19 million Americans age 65 and older, or 30% of all older Americans» [result]

## C12: Anti-amyloid therapies (lecanemab, donanemab) slow early-stage progression
- **Statement**: Lecanemab and donanemab, approved for MCI/mild dementia (stages 3-4) with confirmed elevated beta-amyloid, change AD's underlying biology and slow decline; e.g., earlier donanemab initiation reduced risk of progression to the next stage by 27%.
- **Status**: supported
- **Falsification criteria**: Clinical-trial evidence showing no significant slowing of cognitive/functional decline vs placebo, or failure to clear amyloid.
- **Proof**: [E12]
- **Evidence basis**: §2.3.1; Figure 1 (treatment landscape); refs 43-49.
- **Interpretation**: Benefits may be imperceptible short-term; effectiveness beyond 18-month trials is not fully established; ARIA is a notable risk; only ~8% of a real-world MCI/dementia sample met trial eligibility in one estimate.
- **Dependencies**: none.
- **Tags**: treatment, anti-amyloid, lecanemab, donanemab, ARIA
- **Sources**:
  - donanemab earlier initiation reduced progression risk 27% ← §2.3.1 «earlier initiation of the drug reduced the risk of progression to the next stage of Alzheimer's disease by 27%» [result]
  - ARIA-E 9.5% / ARIA-H 17.5% (meta-analysis, n=6,315) ← §2.3.1 «the pooled incidence of ARIA-E ... was 9.5%, and the pooled incidence of ARIA-H ... was 17.5%» [result]

## C13: Structured multidomain lifestyle intervention protects cognition (U.S. POINTER)
- **Statement**: In the U.S. POINTER randomized controlled trial (>2,100 participants, 2 years), both a structured and a self-guided multidomain lifestyle program improved cognition, with the structured group achieving significantly greater improvement (cognitive scores equivalent to being up to two years younger).
- **Status**: supported
- **Falsification criteria**: Trial results (Baker et al.) showing no significant between-group difference favoring the structured intervention.
- **Proof**: [E10]
- **Evidence basis**: §2.4.3; §8.2; Figures 3, 20; ref 268 (Baker et al.).
- **Interpretation**: First large-scale U.S. RCT to show an accessible multidomain lifestyle intervention can protect cognitive function in a diverse population; motivates community brain-health programs.
- **Dependencies**: C15.
- **Tags**: prevention, RCT, lifestyle, POINTER, MIND-diet
- **Sources**:
  - structured > self-guided, ~2 years younger; >2,100 participants ← §8.2 «the structured group having a statistically-significant greater improvement in cognition ... cognitive scores equivalent to those of people who were up to two years younger» and «the multi-site trial randomized more than 2,100 study participants» [result]

## C14: Americans value brain health but lack knowledge and clinician guidance (2026 Special Report)
- **Statement**: In a nationally representative survey of adults 40+ (n=3,829), 99% viewed brain health as equally or more important than physical health and 88% said maintaining it is very important, yet only 9% reported knowing "a lot" about how to maintain it and only 14% had discussed brain health with their physician.
- **Status**: supported
- **Falsification criteria**: A comparably designed representative survey showing high self-reported brain-health knowledge or frequent provider conversations.
- **Proof**: [E11]
- **Evidence basis**: §8.4-8.6; Figures 21-27; Table 25; §8.6 (survey methods, n=3,829, Dec 29 2025-Jan 13 2026, NORC AmeriSpeak).
- **Interpretation**: A knowledge-to-action and clinical-integration gap; strong interest (73%) in POINTER-style programs, gated mainly by cost.
- **Dependencies**: none.
- **Tags**: survey, brain-health, knowledge-gap, special-report
- **Sources**:
  - 99% equally/more important; 88% very important; 9% know "a lot"; 14% discussed with provider ← §8.5.1/§8.6 «99% viewed brain health as equally or more important than physical health ... 88% said maintaining brain health as they age is very important ... fewer than 1 in 10 (9%) reported knowing 'a lot' ... only 14% of adults have discussed this topic with their provider» [result]
  - n=3,829, Dec 29 2025-Jan 13 2026 ← §8.6 «A survey of 3,829 U.S. adults age 40 and older was conducted from December 29, 2025, to January 13, 2026» [input]

## C15: A large fraction of dementia is attributable to modifiable risk factors
- **Statement**: The 2024 Lancet Commission identified 14 modifiable risk factors that, if eliminated, might prevent nearly half of dementia cases worldwide; a U.S. study of >375,000 people estimated ~37% of dementia cases were associated with eight modifiable factors (led by midlife obesity, physical inactivity, low education).
- **Status**: supported
- **Falsification criteria**: Attributable-fraction analyses finding modifiable factors account for a negligible share of dementia.
- **Proof**: [E13]
- **Evidence basis**: §2.4.2; Figure 2; §8.1; refs 65, 105.
- **Interpretation**: Attributable fractions vary by population (e.g., 33% Latino, 14% Japanese American in one U.S. cohort); provides the rationale for prevention (C13).
- **Dependencies**: none.
- **Tags**: risk-factors, prevention, attributable-fraction, Lancet
- **Sources**:
  - 14 factors ~half of cases (Lancet 2024) ← §2.4.2 «identified 14 modifiable risk factors that, if eliminated, might prevent nearly half of dementia cases worldwide» [result]
  - ~37% associated with 8 factors (>375,000 participants) ← §2.4.2 «a study involving more than 375,000 participants estimated that nearly 37% of dementia cases were associated with eight modifiable risk factors» [result]
