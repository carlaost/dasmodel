# Problem Specification

## Observations

### O1: Dementia is already a massive and rapidly growing global burden
- **Statement**: More than 50 million people were living with dementia worldwide as of the cited WHO estimate, with more than 60% living in low- and middle-income countries; this is projected to rise to 139 million by 2050.
- **Evidence**: §Introduction ("there were more than 50 million people living with dementia worldwide, and more than 60% of whom live in low- and middle-income countries [2]. As societies age, this number is expected to increase to 139 million by 2050 according to World Alzheimer Report [4].").
- **Implication**: Both the scale and the low-/middle-income-country concentration of the existing burden create urgency for understanding how ADOD burden differs by development level (SDI) and region.

### O2: The economic burden of ADOD is already very large
- **Statement**: The global economic loss attributed to dementia in 2019 was $1.3 trillion, of which approximately 50% is attributed to informal caregivers (e.g., family members and close friends) who may reduce working hours to provide care.
- **Evidence**: §Introduction ("The economic burden associated with ADOD is quite heavy, with a global economic loss of $1.3 trillion in dementia in 2019, of which approximately 50% of the cost is attributed to the informal caregivers such as family members and close friends... leading to a loss of productivity [2, 3].").
- **Implication**: Because informal caregiving absorbs roughly half of the total economic cost, disparities in disease burden translate directly into disparities in unpaid caregiving burden, which disproportionately affects women (O4).

### O3: This paper's own GBD 2021 secondary analysis quantifies a large and still-rising 2021 burden
- **Statement**: Globally in 2021, ADOD caused 9.84 million incident cases, 1.95 million deaths, and 36.33 million DALYs; ADOD incidence, mortality, and DALYs all increased from 1990 to 2021.
- **Evidence**: Abstract ("Globally, 9.84 million cases of ADOD occurred in 2021, with 1.95 million ADOD-related deaths, causing 36.33 million DALYs... ADOD incidence, mortality and DALYs all increased from 1990 to 2021.").
- **Implication**: This is the paper's own headline empirical finding, motivating the more granular sex/region/SDI-stratified and risk-factor analyses that follow.

### O4: ADOD disproportionately affects women, who are also the predominant caregivers
- **Statement**: ADOD disproportionately affects women, who are more likely to develop ADOD and are also more often the primary caregivers of family members with ADOD, potentially placing a double burden on this population.
- **Evidence**: §Introduction ("ADOD disproportionately affects women, who are more likely to develop ADOD, and women are also tending to be the primary caregivers of families, thus potentially placing a double burden on this population [13].").
- **Implication**: Sex-stratified analysis of incidence, mortality, DALYs, and risk-factor attribution is necessary rather than optional, since a gender-blind analysis would mask this double burden.

### O5: Demographic transition and urbanization in underdeveloped countries are changing ADOD risk
- **Statement**: In underdeveloped countries, demographic transitions and increasing urbanization can lead to changes in local lifestyles, which increases the risk of ADOD.
- **Evidence**: §Introduction ("In underdeveloped countries, demographic transitions and increasing urbanization can lead to changes in local lifestyles, which increases the risk of ADOD [14].").
- **Implication**: Motivates using the socio-demographic index (SDI) — rather than raw geography alone — as the primary axis for comparing burden trajectories, since SDI is designed to capture exactly this kind of development-linked lifestyle/risk transition.

## Gaps

### G1: Disparities in ADOD burden across regions and gender groups persist despite some policy progress
- **Statement**: Although some regions have made progress (one quarter of countries worldwide have implemented dementia policies/programs, approximately half of them in the European region), disparities in disease burden still persist across regions, particularly among gender groups.
- **Caused by**: O1, O3, O4
- **Existing attempts**: National/regional dementia policies and programs (per WHO); prior GBD-based dementia burden studies (refs 20, 21 — GBD 2019 Dementia Forecasting Collaborators; GBD 2016 Dementia Collaborators).
- **Why they fail**: Prior GBD dementia analyses used earlier GBD iterations (2016, 2019) and, per this paper's Discussion, reported different leading risk factors than found here ("Unlike previous GBD estimates [20, 21], high FPG became the most important attributable risk factor for ADOD, especially in high SDI region"), indicating the burden/risk-factor picture has shifted and needs re-characterizing with the latest GBD 2021 data.

### G2: The relationship between socio-demographic development (SDI) and ADOD burden had not been characterized with combined joinpoint, quantile-regression, and spline methods at both the regional and 204-country level
- **Statement**: The study aims to assess the association between socio-demographic index (SDI) and disease burden, examining whether SDI's relationship to ADOD incidence, mortality, and DALYs is linear, and whether that relationship differs across quantiles of the burden distribution.
- **Caused by**: O3, O5
- **Existing attempts**: Prior studies used joinpoint regression or simple correlation approaches to SDI (e.g., ref 19 for other non-communicable diseases); none combined joinpoint segmentation (temporal trend), restricted cubic splines (regional/temporal SDI association), and quantile regression (204-country, cross-sectional 2021 SDI association) together for ADOD specifically.
- **Why they fail**: A single mean-trend or linear-correlation approach cannot capture (a) segmented temporal trend changes (joinpoint), or (b) whether the SDI-burden relationship differs across the distribution of country-level rates (quantile regression) rather than only in the mean.

### G3: Risk-factor attribution patterns for ADOD by sex, region, and SDI level were not well characterized in prior GBD-based work
- **Statement**: The GBD 2021 risk-factor decomposition for ADOD attributable to smoking, high BMI, and high fasting plasma glucose (FPG), broken out by sex and SDI region/GBD region over 1990-2021, had not previously identified high FPG as the leading attributable risk factor.
- **Caused by**: O3
- **Existing attempts**: GBD 2019 Dementia Forecasting Collaborators (ref 20) reported smoking as predominant among males and high BMI as predominant among females as the leading risk factors.
- **Why they fail**: These earlier analyses used earlier GBD data vintages and, per this paper, do not reflect the current (GBD 2021) finding that high FPG has overtaken these as the leading risk factor, especially in high-SDI regions.

## Key Insight
- **Insight**: The association between socio-demographic development (SDI) and ADOD burden is not uniform across incidence, mortality, and DALYs — it is directionally different by burden measure and non-linear by SDI level and by burden-rate quantile. Specifically, ADOD incidence increases more rapidly with SDI in areas that have historically shown lower incidence, while in regions with higher mortality/DALY burden, those indicators decrease relatively faster as SDI increases — meaning the "SDI transition" simultaneously worsens relative incidence burden and improves relative mortality/DALY burden as countries develop, with distinct regional/gender risk-factor signatures (rising metabolic risk via high FPG/BMI, falling behavioral risk via smoking) underlying the mortality/DALY pattern.
- **Derived from**: O3, O5, G2, G3
- **Enables**: A joinpoint-regression + quantile-regression + restricted-cubic-spline analytic strategy across 1990-2021, 21 GBD regions/204 countries, and three sex strata, paired with a comparative risk assessment (population attributable fraction) decomposition of ADOD deaths/DALYs into smoking, high BMI, and high FPG contributions — providing a basis for region/SDI-tailored ADOD prevention policy rather than a single global recommendation.

## Assumptions
- A1: GBD 2021 estimates (incidence, mortality, DALYs, risk-factor attribution) are accepted as the reference data source, with all attendant GBD-methodology limitations (modeled estimates from surveys, censuses, hospital/administrative records, vital statistics, verbal autopsies, and systematic literature search, not direct universal surveillance).
- A2: SDI quintile boundaries are fixed at the values reported in §Methods: high SDI (0.8103-1.000), high-middle SDI (0.7120-0.8103), middle SDI (0.6188-0.7120), low-middle SDI (0.4658-0.6188), low SDI (0-0.4658).
- A3: The world is divided into 21 GBD regions based on geographical location, used alongside the 5 SDI quintiles as the two parallel regional-grouping schemes.
- A4: The analysis is restricted to three attributable risk factors — smoking, high fasting plasma glucose (FPG), and high body mass index (BMI) — "due to the availability of data," not because these are asserted to be the only risk factors relevant to ADOD.
- A5: Prevalence of ADOD is deliberately excluded from this analysis; only incidence, mortality, and DALYs (derived through GBD's joint modeling) are analyzed.
- A6: R version 3.6.0 was used for all statistical description and analyses (joinpoint regression, quantile regression, restricted cubic splines).
- A7: Ethical approval was deemed not applicable because GBD 2021's underlying data sources are all publicly listed at the Global Health Data Exchange website.
