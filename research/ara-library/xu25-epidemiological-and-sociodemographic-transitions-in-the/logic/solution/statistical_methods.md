# Statistical Methods (Study Design)

This is the "method" of the work: a GBD 2021 secondary-analysis pipeline combining descriptive tabulation, joinpoint trend regression, restricted cubic splines, and quantile regression, plus a comparative-risk-assessment (PAF) decomposition for three attributable risk factors. (Mirrors §Materials and methods.)

## Data source
- **Source**: Global Burden of Disease, Injuries, and Risk Factors Study (GBD) 2021, queried from the Global Health Data Exchange (GHDx, http://ghdx.healthdata.org/).
- **Coverage**: Location, year, age, and sex estimates for 371 diseases/injuries and 88 risk factors, in 204 countries/territories, 1990-2021.
- **Underlying GBD input sources**: household surveys, censuses, hospital records, administrative records, vital statistics, verbal autopsies, and systematic literature search (per refs 15-16; described in more detail in the paper's own Supplementary Material, not provided with this input).
- **Outcome variables extracted**: incidence, deaths, DALYs, and corresponding age-standardized rates (ASRs), by sex (both, male, female), risk factor, and SDI region, 1990-2021, with 95% uncertainty intervals (UI).

## Regional/development groupings
- **SDI (socio-demographic index)**: geometric mean of lag-distributed income per capita, average educational attainment (age 15+), and total fertility rate under age 25, for a given location; range 0-1. Quintile cut-points: high SDI (0.8103-1.000), high-middle SDI (0.7120-0.8103), middle SDI (0.6188-0.7120), low-middle SDI (0.4658-0.6188), low SDI (0-0.4658).
- **GBD region**: the world divided into 21 regions by geographical location (plus 7 super-regions grouping subsets of the 21 regions, as shown in Table 1).
- Both grouping schemes are used in parallel throughout ("To further explore the regional differences of these indicators, we used both metrics as the basis for regional grouping" — §Methods).

## Age standardization
- Formula: ASR = (Σᵢ aᵢωᵢ / Σᵢ ωᵢ) × 100,000 (i = 1...A age groups), where aᵢ is the age-specific rate and ωᵢ is the number of persons (or weight) of the same age subgroup in the GBD world population age standard.
- Reported per 100,000 population, enabling comparison across populations/time periods with differing age structures.

## Temporal trend estimation: joinpoint regression
- Model: ln(ASR) = α + βx + ε, where x = calendar year; fit as a segmented ("joinpoint") regression to identify years at which the trend slope changes.
- **APC** (annual percentage change) = 100 × (exp(β) − 1), computed per identified segment; **EAPC** evaluates the internal trend within each independent segment; **AAPC** evaluates the average trend over the whole 1990-2021 period.
- 95% CI computed from the underlying linear regression model.
- Classification rule: APC/AAPC is "upward" if the estimate and both 95% CI limits are positive; "downward" if all are negative; otherwise "stable."
- Applied separately to ASIR, ASDR, and ASR-DALYs, for the Global group and each of the five SDI regions (Table 2).

## SDI-burden association: restricted cubic splines (RCS)
- Model: RCS with four knot centiles, used to flexibly model the (potentially non-linear) association of incidence, mortality, and DALY rates with SDI.
- Dummy variables included for outlier regions that would otherwise skew the fit, to better capture the average relationship for each SDI group.
- Fit using GBD estimates from all 21 regions across all years 1990-2021 (Figure S5 — supplementary, not provided with this input; the finding is grounded here via the main-text prose description, `logic/claims.md` C05).

## SDI-burden association: quantile regression
- Model: minimum weighted absolute deviation estimator, min_β Σ wτ|yₜ − α| decomposed as (1−τ)Σ_{yᵢ<α}|yₜ−α| + τΣ_{yᵢ≥α}|yₜ−α|, where wτ is the quantile weight and yₜ is the sum of absolute weighted deviations for quantile τ.
- Fit at the 5th, 25th, 50th (median), 75th, and 95th percentiles, alongside an overall mean-trend line with 95% CI.
- Applied to the 204-country, 2021 cross-section, by sex, for ASIR, ASDR, and ASR-DALYs vs. SDI (Fig. 2).
- Rationale (explicit, §Methods): quantile regression "can estimate the linear relationship between different quantiles of dependent and independent variables, and can observe the changes in regression coefficients under different distributions of dependent variables in a more detailed manner, giving it an advantage over traditional linear regression models."

## Risk-factor attribution: comparative risk assessment (population attributable fraction, PAF)
- Risk factors analyzed: smoking, high fasting plasma glucose (FPG), high body mass index (BMI) — chosen "due to the availability of data" (§Discussion "Limitations"), not an exhaustive risk-factor set.
- PAF formula: PAF = [Σᵢ₌₁ⁿ Pᵢ(RRᵢ−1)] / [Σᵢ₌₁ⁿ Pᵢ(RRᵢ−1) + 1], where Pᵢ = percentage of population exposed to risk level i, n = total number of exposure levels, RRᵢ = relative risk at level i.
- Assumption: exposure levels of other risk factors are held unchanged when estimating any single factor's attributable burden (i.e., factors are attributed independently, not via a joint/interactive model).
- Attributable deaths = PAF × total ADOD deaths. Attributable DALYs = PAF × (years of life lost [YLL] + years lived with disability [YLD]), where YLL = life expectancy at age of death minus age at death, and YLD = prevalence of each disease sequela × its disability weight.
- Output: absolute number and ASRs of ADOD deaths/DALYs attributable to each of the three risk factors, globally and by SDI region/GBD region, for 1990 and 2021 (Fig. 3, Fig. 4).
- Method reference: "The specific methods are outlined in the previous study [17]" (GBD 2021 Risk Factors Collaborators) — this paper reuses that study's PAF methodology and underlying exposure/relative-risk data rather than deriving new relative-risk estimates.

## Software
- R (version 3.6.0) was used for all statistical description and analyses (§Methods "Statistical analysis").

## No registered protocol
- No PROSPERO registration, trial registration, or other protocol pre-registration identifier appears anywhere in the paper's full text — not specified in paper. Ethical approval was deemed not applicable, since all GBD 2021 data sources are publicly listed at the Global Health Data Exchange website.
