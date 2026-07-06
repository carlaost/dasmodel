# Problem Specification

## Observations

### O1: Dementia is a top-ranked global cause of disability and death
- **Statement**: In 2019 dementia was responsible for 44 million DALYs globally, ranking as the 7th
  leading cause of death and disability combined and the 3rd leading cause among individuals aged 70+;
  it accounted for about 2.5% of total global DALYs (GBD 2019). AD accounts for 60–80% of all
  dementia cases worldwide.
- **Evidence**: Introduction, p.2 (refs 4, 5); background (refs 1, 7).
- **Implication**: Dementia is a major, high-priority public-health burden warranting region-specific
  quantification.

### O2: Prior MENA-specific estimates were based on older GBD cycles
- **Statement**: Earlier work (Safiri et al. 2023, GBD 2019) reported the MENA region experienced
  2.5 million dementia cases and 70.5 thousand deaths in 2019, with age-standardised point prevalence
  increasing by 3.0% between 1990 and 2019 and no significant change in DALY/death rates.
- **Evidence**: Introduction and Discussion, pp.2, 9 (ref 6).
- **Implication**: An updated analysis using the newest cycle (GBD 2021) is needed to detect whether
  trends have shifted.

### O3: MENA faces rapid ageing and rising AD risk factors
- **Statement**: The MENA population is ageing rapidly (proportion >60 expected to rise substantially
  by 2050); cardiovascular disease and diabetes prevalence — both AD risk factors — are increasing.
  Dementia-care spending in MENA reached ≈$2.1 billion (2019), growing 8.2%/yr since 2000, forecast
  to reach $57.9 billion by 2050 (vs 4.5%/yr global growth).
- **Evidence**: Introduction, p.2 (refs 9, 10, 20).
- **Implication**: A rapid future rise in AD burden is anticipated, raising the value of accurate
  baseline and trend estimates.

### O4: GBD 2021 introduced methodological changes relevant to dementia
- **Statement**: GBD 2021 introduced incidence data in dementia modelling for the first time; since
  GBD 2019 the fatal-modelling approach was redesigned to remove reliance on vital-registration data
  (which showed coding-driven, not epidemiological, mortality shifts) in favour of relative-risk
  estimates from systematic review.
- **Evidence**: Methods (§Case definition / Fatal modelling), pp.2–4 (ref 26).
- **Implication**: New estimates may differ from older cycles, motivating re-analysis.

## Gaps

### G1: No up-to-date GBD-2021 burden estimate for AD/dementia in MENA by country, age, sex, SDI
- **Statement**: At the time of writing there was no comprehensive analysis of AD and other dementia
  prevalence, mortality, and DALY trends in the MENA region from 1990 to 2021 using GBD 2021 data,
  stratified by country, age, sex, and Socio-demographic Index.
- **Caused by**: O2, O4 (prior estimates use older cycles; methods have changed).
- **Existing attempts**: GBD 2019-based MENA analyses (ref 6); global GBD 2016/2019 dementia analyses
  (refs 4, 33); Arab-countries systematic review (ref 23).
- **Why they fail**: They predate GBD 2021, omit the newest methodology, and/or are not MENA-specific
  at the country/age/sex/SDI resolution needed for regional policy.

### G2: Sparse, non-standardised primary dementia data in low- and middle-income MENA settings
- **Statement**: There is a paucity of primary data and inconsistent use of standardised case
  definitions across MENA, especially in low- and middle-income countries, producing wide uncertainty.
- **Caused by**: regional conflicts, weak health-data systems, heterogeneous diagnostic practice.
- **Existing attempts**: GBD modelling techniques to impute in the absence of data.
- **Why they fail**: Modelling cannot overcome the lack of high-quality underlying data; UIs remain
  wide (this is stated as a study limitation, not solved here).

## Key Insight
- **Insight**: Re-expressing the newest GBD 2021 machinery output specifically for the 21 MENA
  countries — as counts and age-standardised rates with 95% UIs, decomposed by country, age, sex, and
  SDI, and benchmarked against global rates and against 1990 — yields an actionable, policy-relevant
  picture that neither the global GBD publications nor the older MENA analyses provide.
- **Derived from**: O1–O4, G1.
- **Enables**: Detection of the direction of the 1990→2021 trend (a slight but significant decline),
  identification of the countries and demographic strata carrying the most burden, and comparison of
  the region against global rates.

## Assumptions
- A1: GBD 2021 estimates (produced by IHME) are a valid representation of true AD/dementia burden in
  MENA, subject to their published uncertainty.
- A2: The GBD case definition of "Alzheimer's disease and other dementias" (DSM III/IV/V or ICD, with
  CDR as the severity reference) is applied consistently enough across locations to permit comparison.
- A3: Age-standardisation permits valid cross-country and cross-time comparison despite differing age
  structures.
- A4: The 95% UIs (2.5th–97.5th percentiles of 1000 posterior draws) adequately capture estimation
  uncertainty; a change is "statistically significant" when its 95% UI excludes zero.
- A5: The Socio-demographic Index is an adequate summary of a country's development level for the
  expected-value comparison in Figure 4.
