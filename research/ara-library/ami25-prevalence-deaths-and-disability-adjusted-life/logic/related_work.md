# Related Work — typed dependency graph

The paper cites 66 references. Works with a specific technical delta to this study get full `RW`
blocks; the remaining background/infrastructure/context citations are captured briefly below so the
ARA preserves the full citation footprint. DOIs are given where the paper's reference list provides
enough to identify the work; where only a journal citation is printed, that is recorded instead
("no DOI in source").

## RW01: GBD 2021 core methodology (Lancet 2024)
- **Ref**: [26] "Global incidence, prevalence, YLDs, DALYs, and HALE for 371 diseases and injuries in
  204 countries and territories and 811 subnational locations, 1990–2021: A systematic analysis for
  the GBD Study 2021." Lancet (2024).
- **DOI**: no DOI in source
- **Type**: imports
- **Delta**:
  - What changed: This paper inherits the entire estimation pipeline (DisMod-MR 2.1, MR-BRT, draws,
    UIs, age-standardisation) from GBD 2021; it adds nothing to the method, only the MENA extraction
    and presentation.
  - Why: To obtain internally consistent, comparable burden estimates.
- **Claims affected**: C01–C08 (all)
- **Adopted elements**: full GBD 2021 estimation machinery, case definitions, 1000-draw UIs.

## RW02: Safiri et al. 2023 — prior MENA dementia burden (GBD 2019)
- **Ref**: [6] Safiri, S. et al. "The burden of Alzheimer's disease and other types of dementia in the
  Middle East and North Africa region, 1990–2019." Age Ageing 52(3), 042 (2023).
- **DOI**: no DOI in source (Age Ageing 52(3):afad042)
- **Type**: extends / baseline
- **Delta**:
  - What changed: This paper updates the same region from the GBD 2019 cycle to GBD 2021 and finds a
    directional reversal — the prior work reported a +3.0% prevalence increase (1990–2019) with no
    significant DALY/death change; the present study finds significant decreases (prevalence −4.9%,
    deaths −8.6%, DALYs −7.7%) over 1990–2021.
  - Why: newer cycle + methodological changes (incidence data, redesigned fatal modelling).
- **Claims affected**: C01, C02, C04, C07
- **Adopted elements**: MENA regional framing; comparison anchor (2.5M cases, 70.5k deaths in 2019).

## RW03: Nichols et al. 2019 — global/regional/national dementia burden (GBD 2016)
- **Ref**: [4] Nichols, E. et al. "Global, regional, and national burden of Alzheimer's disease and
  other dementias, 1990–2016." Lancet Neurol. 18(1), 88–106 (2019).
- **DOI**: no DOI in source
- **Type**: baseline
- **Delta**:
  - What changed: Provides the global comparison baseline (global age-standardised prevalence rose
    1.7% since 1990) against which the MENA decrease and the MENA-vs-global ratio are contrasted.
  - Why: to benchmark MENA against global trends.
- **Claims affected**: C07
- **Adopted elements**: global reference trend; DALY-ratio comparison framing.

## RW04: Nichols et al. 2022 — global dementia prevalence + 2050 forecast (GBD 2019)
- **Ref**: [33] Nichols, E. et al. "Estimation of the global prevalence of dementia in 2019 and
  forecasted prevalence in 2050." Lancet Public Health 7(2), e105–e125 (2022).
- **DOI**: no DOI in source
- **Type**: bounds / baseline
- **Delta**:
  - What changed: Supplies the forecast context (rising burden, greatest increase in MENA by 2050,
    persistent female excess) against which this study's observed slight decline is discussed.
  - Why: to contrast projected rises with the observed 1990–2021 decrease.
- **Claims affected**: C01, C05
- **Adopted elements**: forecast narrative; female-excess expectation.

## RW05: Velandia et al. 2022 — dementia-care spending, MENA economic burden
- **Ref**: [20]/[32] Velandia, P. P. et al. "Global and regional spending on dementia care from
  2000–2019 and expected future health spending scenarios from 2020–2050." EClinicalMedicine 45,
  101337 (2022).
- **DOI**: no DOI in source
- **Type**: imports (context)
- **Delta**:
  - What changed: Source of the MENA economic-burden figures (≈$2.1B in 2019, 8.2%/yr growth since
    2000, $57.9B by 2050; global growth 4.5%/yr) used to motivate the study.
  - Why: to establish policy relevance.
- **Claims affected**: motivates problem (O3); no result claim.
- **Adopted elements**: cost estimates cited verbatim.

## RW06: Mobaderi et al. 2024 — risk-factor drivers of AD/dementia mortality (GBD)
- **Ref**: [34] Mobaderi, T., Kazemnejad, A. & Salehi, M. "Exploring the impacts of risk factors on
  mortality patterns of global Alzheimer's disease and related dementias from 1990 to 2021."
  Sci. Rep. 14(1), 15583 (2024).
- **DOI**: no DOI in source
- **Type**: imports (interpretation support)
- **Delta**:
  - What changed: Identifies tobacco and CVD as the most critical modifiable risk factors; used to
    interpret the observed MENA decline (smoking prevalence fell 1990–2019) and the alcohol nuance.
  - Why: to explain the direction of the trend.
- **Claims affected**: C01, C02 (Interpretation only)
- **Adopted elements**: risk-factor ranking; alcohol protective-effect nuance.

## RW07: Brauer et al. 2024 — 88 risk factors (GBD 2021)
- **Ref**: [36] Brauer, M. et al. "Global burden and strength of evidence for 88 risk factors in 204
  countries and 811 subnational locations, 1990–2021." Lancet 403(10440), 2162–2203 (2024).
- **DOI**: no DOI in source
- **Type**: imports (context)
- **Delta**:
  - What changed: Supplies the quantified risk-factor context (tobacco-attributable burden fell 35%
    worldwide 1990–2021; hypertension/high-BMI/high-FPG burdens rising) for the Discussion.
  - Why: to situate MENA risk-factor trends globally.
- **Claims affected**: C01, C02 (Interpretation)
- **Adopted elements**: global risk-factor trend figures.

## Briefer citations (background / context / infrastructure — no distinct technical delta)

Grouped by role; entries list ref number, short descriptor, and relevance.

**AD/dementia pathophysiology and risk factors (background):**
- [1] 2020 Alzheimer's disease facts and figures — AD 60–80% of dementia; risk factors.
- [2] Querfurth & LaFerla 2010, NEJM — AD pathology (amyloid-β, tau).
- [3] Livingston et al. 2020, Lancet Commission — dementia prevention/intervention/care.
- [40] Dintica & Yaffe 2022 — epidemiology and risk factors for dementia.
- [37] Venkataraman et al. 2017 — alcohol and AD.
- [38] Loscalzo et al. 2022 (Harrison's) — vascular dementia.
- [39] Shahbandi et al. 2022 — stroke burden in MENA (GBD 2019).

**Global/regional dementia burden estimates (comparison context):**
- [5] Vos et al. 2020 — GBD 2019, 369 diseases (dementia ≈2.5% global DALYs).
- [27] Steinmetz et al. 2024 — nervous-system disorders GBD 2021 (AD 2nd in DALYs age 60+).
- [28] GBD 2021 collaborators — global mortality from dementia (new method, GBD 2019).
- [29] Amini et al. 2019 — YLDs from AD in Asian/North African countries.
- [30] Li et al. 2022 — global/regional/national AD burden 1990–2019 (+161% cases).
- [31] Nichols & Vos 2021 — global dementia prevalence forecast to 2050.
- [43] Javaid et al. 2021 — AD epidemiology, rising global burden and forecasts.
- [66] Kyu / GBD collaborators 2024 — global burden 1950–2021 and COVID-19 impact.

**MENA demography, health systems, economics (motivation context):**
- [8] UN 2019 — World Population Ageing.
- [9] Abyad 2021 — ageing in MENA.
- [10] Boutayeb 2010 — communicable/non-communicable disease burden in developing countries.
- [11] Arezki et al. 2020 (World Bank) — MENA post-COVID integration.
- [12] WHO 2018 — NCD country profiles.
- [18] Skaria 2022 — economic/societal burden of AD.
- [19] Aranda et al. 2021 — impact of dementia (disparities, costs).
- [21] Tham et al. 2018 — integrated health care in Asia.
- [22] Blasi et al. 2002 — end-of-life care in dementia.
- [23] El-Metwally et al. 2019 — AD/dementia epidemiology in Arab countries (systematic review).
- [24] Weidner & Barbarino 2019 — state of dementia research.
- [25] Katoue et al. 2022 — MENA healthcare-system development.
- [41] Polyzos et al. 2022 — demographic change and growth in MENA.
- [42] Yüceşahin & Tulga 2017 — demographic/social change in MENA.

**COVID-19 and dementia (limitation context):**
- [13] Brown et al. 2020 — COVID-19 impact on AD/dementia.
- [14] Sabetkish & Rahmani 2021 — overall COVID-19 healthcare impact.
- [15] Suárez-González et al. 2021 — COVID-19 isolation effects on dementia cognition.

**Caregiver / societal burden:**
- [16] Mohamed et al. 2010 — caregiver burden in AD.
- [17] Burns 2000 — the burden of AD.

**Smoking / modifiable risk factors:**
- [35] Reitsma et al. 2021 — smoking prevalence and attributable burden (GBD 2019).
- [59] Mukadam et al. 2024 — changes in dementia prevalence/incidence and risk factors.
- [60] Ritchie et al. 2024 — PREVENT Dementia programme baseline.
- [61] Bransby et al. 2024 — modifiability of dementia risk factors.

**Sex differences, cognitive reserve, genetics (female-excess interpretation):**
- [44] Swargiary 2024 — global life-expectancy trends.
- [45] Seifarth et al. 2012 — sex and life expectancy.
- [46] Power et al. 2018 — neuropathological pathways and age-related dementia risk.
- [47] Stern 2012 — cognitive reserve in ageing and AD.
- [48] Farfel et al. 2013 — low education and cognitive reserve.
- [49] Giacomucci et al. 2022 — gender differences in cognitive reserve.
- [50] Wilson et al. 2019 — education and cognitive reserve in old age.
- [51] Le Carret et al. 2005 — education and cognitive-reserve hypothesis in AD.
- [52] Subramaniapillai et al. 2021 — sex/gender differences in cognitive/brain reserve.
- [53] Ward et al. 2022 — frailty, lifestyle, genetics and dementia risk.
- [54] Lourida et al. 2019 — lifestyle and genetic risk with dementia incidence.
- [55] Uddin et al. 2019 — APOE and AD.
- [56] Zhong & Weisgraber 2009 — ApoE4 structure and AD.
- [57] Ungar et al. 2014 — ApoE, gender, and AD interaction.
- [58] Subramaniapillai et al. 2021 — sex differences in brain aging with APOE4 risk.
- [62] Shah et al. 2016 — research priorities to reduce global dementia burden.
- [63] Bamford & Walker 2012 — women and dementia.

**Interventions / policy:**
- [64] Williams et al. 2019 — interventions for carer burden (systematic review/meta-analysis).
- [65] Lisko et al. 2021 — preventing dementia and disability in older adults.
