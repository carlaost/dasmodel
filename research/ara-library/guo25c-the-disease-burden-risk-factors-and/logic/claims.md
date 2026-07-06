# Claims

> Grounding: abstract-only. Every load-bearing number is copied verbatim from the abstract in `metadata.md`; qualitative claims are limited to wording supported by the abstract. No full text was available, so no table or figure evidence backs these claims.

## C01: ADOD burden counts increased substantially in Asia from 1990 to 2021
- **Statement**: In Asia from 1990 to 2021, ADOD deaths increased by 297.34 %, DALYs by 249.54 %, incidence by 244.73 %, and prevalence by 250.44 %.
- **Status**: supported
- **Falsification criteria**: Full-text results, GBD extraction code, or corrected estimates showing different percentage increases for deaths, DALYs, incidence, or prevalence over 1990-2021.
- **Proof**: [E01]
- **Evidence basis**: The abstract reports the four percentage increases directly.
- **Interpretation**: The abstract supports a broad increase in ADOD burden counts in Asia across mortality, disability, incidence, and prevalence measures.
- **Sources**:
  - 297.34 %, 249.54 %, 244.73 %, 250.44 % <- metadata.md (abstract Results) «the deaths, DALYs, incidence, and prevalence of ADOD increased by 297.34 %, 249.54 %, 244.73 %, and 250.44 % in Asia from 1990 to 2021.» [result]
- **Dependencies**: none
- **Tags**: ADOD, Asia, disease-burden, GBD, trend

## C02: Age-standardized ADOD rates increased and were higher among females
- **Statement**: From 1990 to 2021 in Asia, the age-standardized rates of incidence, prevalence, death, and DALYs increased in both males and females, and female age-standardized rates were consistently higher than male rates.
- **Status**: supported
- **Falsification criteria**: Full-text sex-stratified ASR series showing non-increasing trends or male rates equal to or higher than female rates for one or more measures during the study period.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly states the trend and sex comparison but does not provide exact ASR values.
- **Interpretation**: Sex-stratified burden patterns appear important for interpretation and intervention planning, but effect sizes are unavailable from provided input.
- **Sources**:
  - sex-stratified ASR pattern <- metadata.md (abstract Results) «The ASRs of incidence, prevalence, death, and DALYs in both males and females, which consistently increased over the study period, showed that the ASRs of all females were consistently higher than those of males in Asia from 1990 to 2021.» [result]
- **Dependencies**: C01
- **Tags**: age-standardized-rates, sex-differences, incidence, prevalence, mortality, DALYs

## C03: Qatar and the United Arab Emirates had the greatest changes in several burden counts
- **Statement**: During 1990-2021, Qatar and the United Arab Emirates witnessed the greatest changes in the number of DALYs, incidence, and prevalence of ADOD.
- **Status**: supported
- **Falsification criteria**: Full-text country rankings showing other countries had greater changes in the number of DALYs, incidence, or prevalence over 1990-2021.
- **Proof**: [E02]
- **Evidence basis**: The abstract names Qatar and the United Arab Emirates for the greatest changes but does not provide values or whether both countries tied or led different metrics.
- **Interpretation**: Country-level burden dynamics may vary sharply across Asia, but the abstract does not expose the denominator or drivers of the country rankings.
- **Sources**:
  - Qatar and UAE greatest changes <- metadata.md (abstract Results) «During the period from 1990 to 2021, Qatar and the United Arab Emirates witnessed the greatest changes in the number of DALYs, incidence, and prevalence.» [result]
- **Dependencies**: C01
- **Tags**: country-ranking, Qatar, United-Arab-Emirates, DALYs, incidence, prevalence

## C04: Afghanistan and China had the highest ASMR in 2021
- **Statement**: Afghanistan and China had the highest age-standardized mortality rate of ADOD in 2021.
- **Status**: supported
- **Falsification criteria**: Full-text 2021 ASMR ranking showing a different country or countries had the highest age-standardized mortality rate.
- **Proof**: [E02]
- **Evidence basis**: The abstract reports the 2021 ASMR ranking qualitatively without exact ASMR values.
- **Interpretation**: The highest mortality-rate burden is not necessarily the same as the greatest change in burden counts; the abstract separates these country-level findings.
- **Sources**:
  - Afghanistan and China ASMR <- metadata.md (abstract Results) «Afghanistan and China had the highest age-standardized mortality rate (ASMR) in 2021.» [result]
- **Dependencies**: C02
- **Tags**: ASMR, Afghanistan, China, mortality, country-ranking

## C05: High fasting blood glucose is the top reported risk factor, with sex-differentiated risk patterns
- **Statement**: High fasting blood glucose is reported as the top risk factor for ADOD onset; females are more susceptible to high body-mass index, while males are more likely to be affected by smoking.
- **Status**: supported
- **Falsification criteria**: Full-text risk-factor attribution results showing a different top risk factor, no sex differentiation for high BMI or smoking, or an interpretation not tied to ADOD onset.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly names the top risk factor and the sex-differentiated high BMI and smoking patterns.
- **Interpretation**: The abstract supports risk-factor prioritization but not detailed causal mechanisms, attributable fractions, or intervention effect estimates.
- **Sources**:
  - risk-factor pattern <- metadata.md (abstract Results) «high fasting blood glucose is the top risk factor for the onset of ADOD. Females are more susceptible to the risk factor of high body-mass index (BMI), while males are more likely to be affected by smoking.» [result]
- **Dependencies**: none
- **Tags**: risk-factors, fasting-blood-glucose, BMI, smoking, sex-differences

## C06: ARIMA forecasting indicates continued upward ADOD burden over the next 30 years
- **Statement**: The ARIMA prediction model analysis indicates that the disease burden of ADOD in Asia will continue an upward trend over the next 30 years.
- **Status**: supported
- **Falsification criteria**: Full-text forecast outputs, model diagnostics, or reproduced ARIMA analyses showing flat or declining projected ADOD burden over the forecast horizon.
- **Proof**: [E04]
- **Evidence basis**: The abstract reports the forecast direction and horizon but not model parameters, confidence intervals, or metric-specific forecasts.
- **Interpretation**: The abstract frames ADOD as a growing future public-health burden in Asia, but forecast uncertainty is not available from provided input.
- **Sources**:
  - next 30 years upward trend <- metadata.md (abstract Results) «According to the analysis of the ARIMA prediction model, the disease burden of ADOD in Asia will continue to show an upward trend in the next 30 years.» [result]
- **Dependencies**: C01
- **Tags**: ARIMA, forecast, future-burden, Asia, public-health-planning
