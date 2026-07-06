# Experiments (Analysis Plans)

> Grounding: abstract-only, directional only. These reconstruct the study's analytical procedures from the abstract. Exact numerical results are kept in `claims.md`; procedural details not in the abstract are marked "Not available from provided input".

## E01: Assemble GBD 2021 ADRD burden dataset for adults aged 65 years and older
- **Verifies**: C01, C02, C03, C06
- **Setup**:
  - Data framework: Global Burden of Disease and Risk Factors Study 2021.
  - Population: adults aged >=65 years.
  - Geography: 21 regions and 204 countries and territories.
  - Time window: 1991-2021.
  - Data sources: vital registration systems, published scientific literature and surveys, and health-service encounters.
  - Model/software: Not available from provided input.
- **Procedure**:
  1. Obtain dementia data on deaths, excess mortality, prevalence, and incidence from the named GBD 2021 sources.
  2. Restrict analysis to individuals aged >=65 years across the stated regions, countries, and territories.
  3. Prepare burden metrics and risk-factor-attributable fractions for ADRD.
- **Metrics**: Availability and coverage of mortality, prevalence, incidence, excess mortality, and risk-factor inputs; data completeness details not available from provided input.
- **Expected outcome**:
  - A global older-adult ADRD burden dataset covering 1991-2021 is available for trend and disparity analyses.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Estimate global burden trends in ADRD among adults aged 65 years and older
- **Verifies**: C01, C02, C03, C04, C05
- **Setup**:
  - Dataset: GBD 2021 ADRD dataset assembled in E01.
  - Outcomes: age-standardized prevalence, deaths, DALYs, AAPC, sex-stratified prevalent-case counts.
  - Population: adults aged >=65 years.
- **Procedure**:
  1. Estimate mortality, prevalence, age-standardized prevalence, deaths, and DALYs for ADRD among adults aged >=65 years.
  2. Compare 1991 and 2021 global estimates.
  3. Stratify prevalent-case counts by sex for the reported endpoints.
  4. Summarize trend direction with AAPC where available.
- **Metrics**: Mortality rate, prevalence count, age-standardized prevalence rate, deaths, DALYs, AAPC, uncertainty intervals.
- **Expected outcome**:
  - Mortality and total prevalence increase over the study window; female prevalent-case counts exceed male counts; age-standardized prevalence changes less than total prevalence.
- **Baselines**: 1991 estimates serve as the temporal baseline.
- **Dependencies**: E01

## E03: Attribute ADRD burden metrics to selected modifiable risk factors
- **Verifies**: C06
- **Setup**:
  - Dataset: GBD 2021 ADRD burden estimates from E01/E02.
  - Risk factors: high BMI, high fasting glucose, smoking.
  - Population: adults aged >=65 years.
- **Procedure**:
  1. Estimate fractions of ADRD burden metrics attributable to the three named risk factors.
  2. Use the attributable-fraction results to inform prevention-oriented recommendations.
  3. Report risk-factor results across the paper's geographic scope.
- **Metrics**: Attributable fractions for ADRD burden metrics; exact fractions not available from provided input.
- **Expected outcome**:
  - The named risk factors remain relevant modifiable contributors to ADRD burden and motivate risk-factor management recommendations.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E02
