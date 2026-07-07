# Problem Specification

## Observations

### O1: AD is a large and growing global health and economic burden
- **Statement**: Alzheimer's disease (AD) affects more than 50 million individuals worldwide, a
  number projected to triple by 2050 due to an aging population. Global costs are estimated to
  surpass $1 trillion annually.
- **Evidence**: Introduction, p.2 (refs 1, 2).
- **Implication**: AD burden quantification and forecasting is a high-priority public-health need.

### O2: AD etiology is multifactorial, and epidemiological gaps remain by socio-demographic group and region
- **Statement**: AD risk is driven by a complex interaction of genetic (e.g., APOE ε4),
  environmental (neurotoxins, air pollution), and lifestyle factors (smoking, alcohol, diet),
  plus chronic conditions (hypertension, diabetes, obesity). Despite progress in understanding
  these factors, gaps remain in the disease's epidemiology and its differential impact across
  socio-demographic groups and regions.
- **Evidence**: Introduction, p.2 (refs 5–9).
- **Implication**: Up-to-date, comprehensive global data are needed to inform public-health
  strategy.

### O3: GBD 2021 provides the newest standardized global disease-burden estimates, now including incidence data for dementia modeling
- **Statement**: GBD 2021 (GHDx platform) covers 371 diseases/injuries and 87 risk factors across
  204 countries/territories, integrating surveys, censuses, and vital-registration data with
  updated standard operating procedures. AD-specific incidence data were newly added in GBD 2021,
  sourced from 81 data points across 60 locations, supported by excess-mortality data from cohort
  studies. USA claims data were excluded from dementia modeling "due to their disproportionate
  weight on global prevalence and incidence patterns relative to other input data."
- **Evidence**: Methods §2.1 "Data source", p.2.
- **Implication**: A fresh, GBD-2021-based analysis can incorporate methodological improvements
  (incidence data) not available to prior GBD cycles.

### O4: No published GAM-based projection of global AD burden to 2030, decomposed by sex/region/country/SDI, existed prior to this study (as framed by the authors)
- **Statement**: The study frames its contribution as combining historical (1990–2021) ASR/EAPC
  description with GAM-based forecasting of ASR to 2030, stratified by sex, SDI tier, GBD region,
  and country, plus a correlation analysis of SDI vs. burden by continent.
- **Evidence**: Introduction, p.2.
- **Implication**: The paper positions itself as extending purely descriptive GBD burden papers
  with an explicit forward projection to 2030.

## Gaps

### G1: No integrated 1990–2030 (historical + projected) AD burden picture stratified simultaneously by region, country, sex, and SDI, using GBD 2021
- **Statement**: At the time of writing, comprehensive GBD-2021-based projections of AD incidence,
  death, and DALY rates to 2030 — broken out by all of region, country, sex, and SDI tier in one
  analysis — were not available.
- **Caused by**: O3, O4 (GBD 2021 with incidence data is new; no combined projection existed).
- **Existing attempts**: Prior GBD-cycle descriptive burden papers (implicitly referenced but not
  cited by DOI/author in this paper's reference list — see `logic/related_work.md` for the
  citation-footprint anomaly).
- **Why they fail**: Descriptive papers report only historical 1990–2021 trends; they do not
  forecast to 2030 or apply Mann-Whitney/correlation tests across SDI thresholds and continents.

### G2: Uneven data availability across countries, especially low-SDI settings, weakens estimate precision
- **Statement**: Data availability is unequal across countries/regions, particularly in
  lower-SDI areas lacking comprehensive AD surveillance systems and population-based registries.
- **Caused by**: heterogeneous health-data infrastructure; reliance on ICD-coded records with
  cross-country diagnostic variation.
- **Existing attempts**: GBD's DisMod-MR 2.1 and CODEm modeling impute in the absence of direct
  data.
- **Why they fail**: Modeling cannot substitute for missing primary data; the paper itself
  acknowledges this as a limitation (see `logic/solution/constraints.md`).

## Key Insight
- **Insight**: Applying GAMs to GBD 2021's newly incidence-informed AD estimates, and computing
  EAPC over both the 1990–2021 and 2022–2030 windows at every stratification level the GBD
  provides (sex, SDI, region, country), yields a single forecast picture that can be directly
  compared against the historical EAPC to detect whether decline/rise trends are expected to
  continue, reverse, or accelerate through 2030.
- **Derived from**: O1–O4, G1.
- **Enables**: Identification of which regions/countries are projected to diverge from the global
  declining trend (e.g., Andean Latin America, Cyprus rising vs. Eastern Europe, Bahrain falling
  sharply), and a test of whether SDI is systematically associated with 2030 burden.

## Assumptions
- A1: GBD 2021 estimates (IHME) validly represent true AD incidence, mortality, and DALY burden,
  subject to their published uncertainty intervals.
- A2: Historical 1990–2021 GBD trends, extended via GAM smooth functions of calendar year (and
  implicitly age), are a valid basis for projecting 2022–2030 ASRs; no external shock (e.g., new
  disease-modifying therapy, pandemic) is modeled.
- A3: EAPC (computed from a log-linear regression across the ASR time series per the standard
  GBD/EAPC convention) meaningfully summarizes the average annual trend direction and magnitude
  over each window, with significance determined by whether the 95% CI excludes zero.
- A4: SDI is an adequate composite proxy for a location's socio-economic development level for the
  purpose of grouping countries into "high/low SDI" comparisons and continent-level correlations.
- A5: ICD-9 (290.0–290.9) and ICD-10 (G30.0–G30.9) codes are applied consistently enough across
  GBD input data sources to permit the cross-country/cross-time comparisons the study relies on.
