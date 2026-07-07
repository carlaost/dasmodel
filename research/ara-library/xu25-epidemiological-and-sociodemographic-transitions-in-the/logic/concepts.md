# Concepts

## Global Burden of Disease (GBD) study
- **Notation**: GBD 2021
- **Definition**: A research framework and estimation system (Institute for Health Metrics and Evaluation) providing location, year, age, and sex estimates for 371 diseases/injuries and 88 risk factors in 204 countries and territories from 1990 to 2021, derived from household surveys, censuses, hospital records, administrative records, vital statistics, verbal autopsies, and systematic literature search.
- **Boundary conditions**: This paper is a secondary analysis of GBD 2021 data extracted from the Global Health Data Exchange (GHDx); no new primary data were collected. Data quality and estimation methodology inherit all GBD-methodology limitations (§Methods; §Discussion "Limitations").
- **Related concepts**: Socio-demographic index (SDI), Age-standardized rate (ASR)

## Alzheimer's disease and other dementias (ADOD)
- **Notation**: ADOD
- **Definition**: The paper's composite outcome category, following GBD classification, covering Alzheimer's disease and other/related dementias as a single disease-burden entity, quantified via incidence, mortality, and disability-adjusted life-years (DALYs).
- **Boundary conditions**: Prevalence is deliberately excluded from this analysis; only incidence, mortality, and DALYs (each derived through GBD's joint modeling) are examined.
- **Related concepts**: Global Burden of Disease study, Disability-adjusted life-years

## Socio-demographic index (SDI)
- **Notation**: SDI, range 0-1
- **Definition**: The geometric mean of three normalized component indices — lag-distributed income per capita, average educational attainment of people over 15, and the total fertility rate under age 25 — for a given location, used to position countries/regions on a development continuum. All countries/territories are sorted into five SDI quintiles: high SDI (0.8103-1.000), high-middle SDI (0.7120-0.8103), middle SDI (0.6188-0.7120), low-middle SDI (0.4658-0.6188), low SDI (0-0.4658).
- **Boundary conditions**: SDI quintiles and the 21-GBD-region geographic scheme are used as two parallel (not nested) regional-grouping bases in this paper — both are reported side-by-side in Table 1 and Table 2 rather than one being derived from the other.
- **Related concepts**: Restricted cubic spline, Quantile regression, GBD region

## Age-standardized rate (ASR): ASIR / ASDR / ASR-DALYs
- **Notation**: ASIR (age-standardized incidence rate), ASDR (age-standardized death/mortality rate), ASR-DALYs (age-standardized DALY rate); all reported per 100,000 population
- **Definition**: A rate that adjusts for differing age structures across populations or over time, computed as ASR = (Σ aᵢωᵢ / Σ ωᵢ) × 100,000, where aᵢ is the age-specific rate and ωᵢ is the number of persons (or weight) of the same age subgroup in a reference standard population (the GBD world population age standard).
- **Boundary conditions**: Used to enable valid comparison of ADOD burden across populations or time periods that differ in age structure; reported throughout Table 1/Table 2 and Figures 1-4 with 95% uncertainty intervals (UI) or 95% confidence intervals (CI) as applicable.
- **Related concepts**: Joinpoint regression, DALYs

## Disability-adjusted life-years (DALYs)
- **Notation**: DALYs
- **Definition**: A summary burden-of-disease metric computed as the sum of years of life lost (YLL, from premature death) and years lived with disability (YLD). YLL is calculated by subtracting age at death from life expectancy at that age; YLD is calculated by multiplying the prevalence of each disease sequela by its disability weight.
- **Boundary conditions**: Used alongside incidence and mortality as one of the three primary burden measures in this paper; attributable DALYs for risk factors are obtained by multiplying YLL and YLD by the risk factor's population attributable fraction (PAF), then summing.
- **Related concepts**: Age-standardized rate, Population attributable fraction

## Joinpoint regression: APC, EAPC, AAPC
- **Notation**: APC (annual percentage change), EAPC (estimated annual percentage change), AAPC (average annual percentage change)
- **Definition**: A statistical method that fits a segmented log-linear trend, ln(ASR) = α + βx + ε (x = calendar year), to identify "joinpoints" where the trend slope changes; APC = 100×(exp(β)−1) within each identified segment. EAPC evaluates the internal trend within each independent segment of the fitted function; AAPC evaluates the average trend over the entire study period (1990-2021). APC/AAPC is classified as "upward" if the estimate and both 95% CI limits are positive, "downward" if all are negative, and "stable" otherwise.
- **Boundary conditions**: Applied separately to ASIR, ASDR, and ASR-DALYs, for the Global group and each of the five SDI regions, over 1990-2021 (Table 2); segment boundaries (joinpoints) differ by indicator and SDI region (e.g., Global ASIR has 5 segments, Global ASDR has 3).
- **Related concepts**: Age-standardized rate, Restricted cubic spline

## Restricted cubic spline (RCS) with dummy variables for outlier regions
- **Notation**: 4-knot RCS
- **Definition**: A flexible non-linear regression technique (four knot centiles) used to model the association between SDI and ADOD incidence/mortality/DALY rates across all 21 GBD regions and all years 1990-2021, allowing curvature (rather than assuming linearity) in the SDI-burden relationship; dummy variables are included for outlier regions that would otherwise skew the average-relationship fit.
- **Boundary conditions**: Fit at the 21-region × multi-year level (Figure S5, supplementary — not provided with this input); distinct from the quantile regression, which is fit at the 204-country, single-year (2021) cross-sectional level (Fig. 2).
- **Related concepts**: Socio-demographic index, Quantile regression

## Quantile regression
- **Notation**: 5th, 25th, 50th (median), 75th, 95th percentile fits
- **Definition**: A regression technique estimating the linear relationship between different quantiles of the dependent variable (ASIR/ASDR/DALY rate) and the independent variable (SDI), based on minimizing a weighted sum of absolute residuals (asymmetric weighting by quantile τ), rather than only estimating the conditional mean as in ordinary least squares.
- **Boundary conditions**: Applied to the 204-country, 2021 cross-section (Fig. 2) specifically to determine whether the SDI-ASR relationship differs across the distribution (not just the mean) of country-level rates; explicitly chosen over "traditional linear regression models" for this reason (§Methods).
- **Related concepts**: Restricted cubic spline, Socio-demographic index

## Population attributable fraction (PAF) / comparative risk assessment
- **Notation**: PAF = [Σᵢ Pᵢ(RRᵢ−1)] / [Σᵢ Pᵢ(RRᵢ−1) + 1], where Pᵢ = proportion of population exposed to risk level i, RRᵢ = relative risk at level i, n = total number of exposure levels
- **Definition**: The GBD comparative risk assessment method used to estimate, for each of the three studied risk factors (smoking, high BMI, high FPG), the proportion of ADOD burden attributable to that risk factor in a given population, by comparing observed exposure distributions against a theoretical minimum risk exposure distribution (assuming other risk factors' exposure levels remain unchanged).
- **Boundary conditions**: Attributable deaths are calculated as PAF × total disease-specific deaths; attributable DALYs are calculated by multiplying YLL and YLD by the corresponding PAF, then summing. Only three risk factors (smoking, high FPG, high BMI) are examined, "due to the availability of data" — not an exhaustive risk-factor decomposition.
- **Related concepts**: DALYs, Age-standardized rate (ASDR)

## Attributable risk factors: smoking, high fasting plasma glucose (FPG), high body mass index (BMI)
- **Notation**: —
- **Definition**: The three GBD-defined risk factors for which this paper reports ADOD-attributable death and DALY rates, decomposed by sex, SDI region, and GBD region, for 1990 and 2021 (Fig. 3, Fig. 4). High FPG and high BMI are metabolic risk factors; smoking is a behavioral risk factor.
- **Boundary conditions**: Smoking-attributable ASDR is consistently higher in males than females; high-FPG- and high-BMI-attributable ASDR are consistently higher in females than males (C10). All three factors' exposure/relative-risk data feed the same PAF formula.
- **Related concepts**: Population attributable fraction, GBD region
