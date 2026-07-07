# Experiments (verification / analysis plans)

This is a secondary descriptive-and-forecasting epidemiology study: its "experiments" are
extraction, GAM-projection, and comparison procedures over GBD 2021 estimates, not primary data
collection or interventions. Plans below are declarative and directional only — all exact numbers
live in `evidence/`.

## E01: Global historical (1990–2021) and projected (2022–2030) trend extraction
- **Verifies**: C01
- **Setup**:
  - Data: GBD 2021 age-standardized incidence, death, and DALY rates for Alzheimer's disease,
    Global aggregate, annual series 1990–2021.
  - System: GAM applied to the 1990–2021 series to forecast 2022–2030; EAPC computed over both the
    1990–2021 and 2022–2030 windows.
- **Procedure**:
  1. Extract the Global 1990–2021 ASR series for incidence, deaths, and DALYs from GHDx.
  2. Fit a GAM smooth function of calendar year (and age, per the model form) to forecast ASRs for
     2022–2030.
  3. Compute EAPC from the start and end ASR of each window (1990→2021; 2022→2030), with a 95% CI.
  4. Flag a trend as significant if its 95% CI excludes zero.
- **Metrics**: ASR; EAPC (%); 95% CI bounds.
- **Expected outcome**: Global ASRs for incidence, deaths, and DALYs decline over both the
  historical and projected windows, each significantly (CI excludes 0).
- **Baselines**: 1990 ASR (start of historical window); 2021 ASR (start of projected window).
- **Dependencies**: none

## E02: Sex-stratified global projection
- **Verifies**: C02
- **Setup**: Same GBD/GAM pipeline as E01, stratified by sex (male, female); Global aggregate;
  2022–2030 window plus 2030 point ASRs.
- **Procedure**:
  1. Extract male and female ASR series for deaths and incidence.
  2. Fit sex-specific GAMs and compute sex-specific EAPCs for 2022–2030.
  3. Extract 2030 point ASRs (with 95% UI) for death, DALY, and incidence rate, by sex.
  4. Compare male vs. female EAPCs and 2030 ASRs.
- **Metrics**: sex-specific EAPC (%) with 95% CI; sex-specific 2030 ASR with 95% UI.
- **Expected outcome**: Both sexes show a projected decline; male and female EAPCs differ in
  magnitude (as evidenced by the male death vs. incidence EAPC differing substantially — a
  contrast that makes the identical female death/incidence EAPC value worth scrutinizing, see C02).
- **Baselines**: male stratum as reference for the female comparison.
- **Dependencies**: E01

## E03: GBD-region-level EAPC and ASR ranking
- **Verifies**: C03, C04
- **Setup**: Same pipeline; unit = each of 18 GBD regions (+ 5 SDI-tier aggregates + Global) shown
  in Table 1; 2022–2030 EAPC and 2030 point ASR for DALYs (also incidence, deaths).
- **Procedure**:
  1. Extract each region's 2022–2030 DALY EAPC (with 95% CI) from Table 1 / Figure 1.
  2. Rank regions to identify the highest-positive and lowest-negative EAPC.
  3. Extract each region's 2030 DALY ASR (with 95% UI) from Supplementary Tables 2/5 (as cited in
     Results) / Figure 2.
  4. Rank regions to identify highest and lowest 2030 ASR.
- **Metrics**: per-region EAPC with 95% CI; per-region 2030 ASR with 95% UI; rank.
- **Expected outcome**: Latin American sub-regions (Andean, Southern) and the Caribbean show the
  highest (rising) EAPC; Eastern/Central Europe and East Asia the lowest (falling). Sub-Saharan
  African sub-regions and Oceania show the highest 2030 ASR; Eastern/Central Europe and
  High-income Asia Pacific the lowest.
- **Baselines**: Global aggregate (E01).
- **Dependencies**: E01

## E04: Country-level EAPC and ASR ranking
- **Verifies**: C05, C06
- **Setup**: Same pipeline; unit = individual countries (not tabulated in the main article; cited
  from Supplementary Tables 6–9 and Supplementary Figure 1, not part of the provided input);
  2022–2030 EAPC and 2030 point ASR for DALYs.
- **Procedure**:
  1. Extract each country's 2022–2030 DALY EAPC (with 95% CI).
  2. Rank countries to identify the highest-positive and lowest-negative EAPC.
  3. Extract each country's 2030 DALY ASR (with 95% UI).
  4. Rank countries to identify highest and lowest 2030 ASR; inspect the lower tail for
     floor/degenerate values.
- **Metrics**: per-country EAPC with 95% CI; per-country 2030 ASR with 95% UI; rank.
- **Expected outcome**: Cyprus, Serbia, Montenegro show the highest EAPC; Bahrain, Armenia, Qatar
  the lowest. Cyprus, North Macedonia show the highest 2030 ASR; the lowest-ASR countries
  (Armenia, Bulgaria, Romania, Guatemala, Bahrain) converge on a shared near-zero point estimate
  with widely varying upper uncertainty bounds — a pattern consistent with a projection floor for
  sparse-data countries rather than a genuine shared burden level.
- **Baselines**: regional aggregates (E03); each country's own 1990–2021 EAPC.
- **Dependencies**: E03

## E05: SDI-threshold group comparison (Mann-Whitney U)
- **Verifies**: C07
- **Setup**: 2030 projected ASIR, ASDR, and DALY ASR, grouped by SDI ≥0.8 vs <0.8; separately by
  SDI ≥0.7 vs <0.7; separately into five SDI categories (low, low-middle, middle, high-middle,
  high).
- **Procedure**:
  1. Split countries into SDI groups at each threshold (0.8; 0.7) and into the five-category
     scheme.
  2. Compare 2030 ASIR/ASDR/DALY ASR between groups using the Mann-Whitney U test.
  3. Assess whether higher-SDI groups show significantly higher values at each threshold/category.
- **Metrics**: group-wise ASR distributions; U statistic; p-value (exact values deferred to
  Supplementary Figures 2–4, not part of the provided input).
- **Expected outcome**: SDI ≥0.8 (and ≥0.7) group shows significantly higher ASIR/ASDR/DALY ASR
  than the below-threshold group; the five-category breakdown is monotonic (high-SDI highest,
  low-SDI lowest) with "highly significant" p-values throughout.
- **Baselines**: below-threshold / lower-SDI group as reference.
- **Dependencies**: none

## E06: Continent-level SDI–burden correlation analysis
- **Verifies**: C08
- **Setup**: Per-continent (Africa, America, Asia, Europe, Oceania) linear regression / Pearson
  correlation of SDI against 2030 ASIR, ASDR, and DALY ASR.
- **Procedure**:
  1. For each continent, regress 2030 ASIR (then ASDR, then DALY ASR) on SDI across its countries.
  2. Compute R² and p-value for each continent × measure combination.
  3. Rank continents by correlation strength and note which reach conventional significance
     (p<0.05).
- **Metrics**: R²; p-value; direction of association (positive, per the paper's framing).
- **Expected outcome**: Oceania shows the strongest, and only conventionally significant (p<0.05),
  positive SDI–burden correlation for ASIR and DALY ASR; Africa (and, for ASIR, America) show weak
  or negligible correlation; most continent × measure combinations are not significant at p<0.05.
- **Baselines**: none (cross-sectional per-continent regressions, not compared to a null model
  beyond the reported p-value).
- **Dependencies**: E05
