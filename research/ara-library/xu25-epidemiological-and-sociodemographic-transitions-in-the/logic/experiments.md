# Experiments (Verification / Analysis Plans)

These are declarative plans reconstructed from the paper's §Methods and §Results structure. They are directional only — exact numerical results live in `evidence/`. "Experiment" here means the analytic procedures a GBD secondary-analysis / epidemiological-transition study uses to characterise its evidence base: descriptive tabulation, joinpoint trend segmentation, spline/quantile modeling of an SDI-burden association, and a comparative risk assessment (PAF) decomposition.

## E01: Descriptive characterization of ADOD incidence, mortality, and DALY burden by sex, SDI region, and GBD region (1990, 2010, 2021)
- **Verifies**: C01, C03, C11
- **Setup**:
  - Data: GBD 2021 estimates of ADOD incidence, deaths, DALYs, and corresponding ASRs, by location/year/age/sex, extracted from the Global Health Data Exchange (GHDx).
  - Strata: both sexes, male, female; SDI region (5 quintiles); GBD region (21 regions); super-region.
  - Years reported: 1990, 2010, 2021 (Table 1).
- **Procedure**:
  1. Extract incident case counts and ASIR (with 95% UI) for 1990, 2010, and 2021, for the overall population, by sex, by SDI region, by super-region, and by GBD region.
  2. Compute the estimated total percentage change (ETPC) of ASIR from 1990 to 2021 for each stratum.
  3. Compare absolute levels and ETPC direction/magnitude across sexes, SDI regions, and GBD regions to identify the highest- and lowest-burden strata and any regional rank changes between 1990 and 2021.
- **Metrics**: incident case counts (×10³, with 95% UI); ASIR per 100,000 (with 95% UI); ETPC of ASIR 1990-2021 (with 95% UI); regional rank order.
- **Expected outcome**: Global incidence rises modestly overall; burden is higher in females than males; burden level and trend direction vary substantially by SDI region and GBD region, with some regions gaining and others losing rank between 1990 and 2021. NEVER exact numbers here — see `evidence/tables/table1.md`.
- **Baselines**: none (descriptive characterization, not a comparative intervention study).
- **Dependencies**: none

## E02: Joinpoint regression trend-segmentation of ASIR/ASDR/ASR-DALYs by SDI region, 1990-2021
- **Verifies**: C02, C06, C07, C08
- **Setup**:
  - Model: segmented log-linear regression, ln(ASR) = α + βx + ε (x = calendar year), fit separately to ASIR, ASDR, and ASR-DALYs time series for the Global group and each of the five SDI regions.
  - Software: R (version 3.6.0).
- **Procedure**:
  1. For each SDI region (Global, High, High-middle, Middle, Low-middle, Low) and each of the three ASR indicators, fit a joinpoint (segmented) regression over 1990-2021, identifying the years at which the trend slope changes.
  2. Compute the EAPC (with 95% CI) for each identified segment, and the AAPC (with 95% CI) for the entire 1990-2021 period.
  3. Classify each segment/period as "upward" (APC and both 95% CI limits > 0), "downward" (all < 0), or "stable" (otherwise).
  4. Compare AAPC magnitudes and signs across SDI regions and across the three ASR indicators (incidence vs. mortality vs. DALYs) to identify which regions/indicators are rising fastest, falling fastest, or reversing direction in their most recent segment.
- **Metrics**: number and year-boundaries of joinpoint segments per region/indicator; per-segment EAPC (95% CI); whole-period AAPC (95% CI); significance flag (P<0.05).
- **Expected outcome**: SDI regions diverge in trend direction and magnitude across the three burden indicators — some regions show opposite-signed trends for incidence vs. mortality/DALYs, and some regions' most recent segment reverses the sign of their earlier segments. NEVER exact numbers here — see `evidence/tables/table2.md`.
- **Baselines**: none (the study's own prior GBD dementia analyses, refs 20-21, are referenced qualitatively as points of comparison in the Discussion, not as a re-run statistical baseline).
- **Dependencies**: E01

## E03: Restricted cubic spline modeling of the SDI-ASR association across 21 regions, 1990-2021
- **Verifies**: C05
- **Setup**:
  - Model: restricted cubic spline (RCS) with four knot centiles, with dummy variables included for outlier regions that would otherwise skew the fit.
  - Data: GBD estimates from all 21 GBD regions, across all years 1990-2021, for ASIR, ASDR, and ASR-DALYs, stratified by sex (both, male, female).
  - Software: R (version 3.6.0).
- **Procedure**:
  1. Pool region-year observations for each of the three ASR indicators, by sex.
  2. Fit a 4-knot RCS regression of the ASR indicator on SDI, including dummy variables for outlier regions.
  3. Characterize the fitted curve's shape (monotonic vs. non-monotonic, and where any inflection/plateau/reversal occurs along the SDI axis) separately for both-sexes, male, and female fits.
- **Metrics**: fitted spline curve shape (qualitative: rising/falling/plateauing/reversing) as a function of SDI, by sex and by ASR indicator.
- **Expected outcome**: The SDI-ASIR association is non-linear and differs by sex — a male-specific plateau/decline above a mid-range SDI threshold and a female-specific acceleration above a threshold are both anticipated based on the paper's prose description. NEVER exact numbers here — the underlying plot (Figure S5) is supplementary material not provided with this input; see `logic/claims.md` C05 for the directional description grounded directly in the main-text prose.
- **Baselines**: none (descriptive spline fit, no comparator model).
- **Dependencies**: E01

## E04: Quantile regression of country-level SDI vs. age-standardized rates, 204 countries, 2021
- **Verifies**: C04, C05
- **Setup**:
  - Data: 204 countries/territories, 2021 cross-section, ASIR/ASDR/ASR-DALYs vs. SDI, by sex (both, male, female).
  - Model: quantile regression at the 5th, 25th, 50th (median), 75th, and 95th percentiles, alongside an overall mean-trend fit with 95% CI.
- **Procedure**:
  1. For each of the 9 sex×indicator panels (3 sexes × {ASIR, ASDR, ASR-DALYs}), plot each of the 204 countries as a point (sized by its incident-case/death/DALY count) against its 2021 SDI value.
  2. Fit an overall mean trend line (with 95% CI shading) and five quantile-regression lines (5th/25th/50th/75th/95th percentile) to each panel.
  3. Identify the highest-incident-case-count countries and characterize how the spread between low- and high-percentile fitted lines varies across the SDI range (i.e., whether variability in the SDI-ASR relationship differs across quantiles).
- **Metrics**: per-panel quantile-regression fitted lines (5th/25th/50th/75th/95th); named highest-case-count countries and their SDI values; qualitative description of the mean-trend curve shape per panel.
- **Expected outcome**: The SDI-ASR relationship, resolved at the 204-country level, shows a materially non-linear (not straight-line) trend, differing by burden measure (ASIR trending upward with SDI; ASDR/ASR-DALYs showing a shallower "valley" shape), with wider quantile-spread at the extremes of the SDI range than in the middle. NEVER exact per-country numbers here — see `evidence/figures/figure2.md` and `logic/claims.md` C04/C05.
- **Baselines**: none (descriptive cross-sectional regression, no comparator model).
- **Dependencies**: E01

## E05: Comparative risk assessment (population attributable fraction) decomposition of ADOD deaths/DALYs by risk factor, sex, and region
- **Verifies**: C09, C10, C12, C13
- **Setup**:
  - Risk factors: smoking, high fasting plasma glucose (FPG), high body mass index (BMI) — the three risk factors for which GBD 2021 data were available for ADOD.
  - Method: GBD comparative risk assessment (PAF formula; see `logic/concepts.md` "Population attributable fraction"), assuming other risk factors' exposure levels are held constant.
  - Strata: sex (both, male, female); SDI region (5 quintiles); GBD region (21 regions); years 1990 and 2021 (Fig. 4) and full 1990-2021 trend (Fig. 3).
- **Procedure**:
  1. For each risk factor, obtain relative-risk (RR) data and population exposure-level distributions from GBD 2021, and the theoretical minimum risk exposure distribution for that factor.
  2. Compute the PAF for each risk factor, stratum, and year using the PAF formula.
  3. Multiply the PAF by total ADOD deaths (for attributable deaths) and by the sum of YLL and YLD (for attributable DALYs), for each stratum and year.
  4. Compare attributable ASDR/DALY-rate magnitudes and 1990-2021 trend direction across risk factors, sexes, SDI regions, and GBD regions to identify the leading risk factor and any sex- or region-specific extremes.
- **Metrics**: attributable ASDR and DALY rate per 100,000, by risk factor × sex × SDI-region/GBD-region × year; 1990-2021 trend direction per risk factor.
- **Expected outcome**: High FPG is expected to be the leading 2021 risk factor for ADOD deaths/DALYs, with an increasing 1990-2021 trend, alongside a rising high-BMI trend and a falling smoking trend; risk-factor attribution is expected to be sex-differentiated (smoking higher in males, FPG/BMI higher in females) and to show identifiable regional extremes (highest/lowest burden regions per risk factor). NEVER exact numbers here — see `evidence/figures/figure3.md`, `evidence/figures/figure4.md`, and `logic/claims.md` C09/C10/C12/C13.
- **Baselines**: the paper's own prior-GBD-vintage comparison (refs 20-21) is referenced qualitatively (smoking/BMI predominance in GBD 2019) as a point of contrast, not re-run as a statistical baseline in this paper.
- **Dependencies**: E01
