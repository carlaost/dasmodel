# Claims

> Grounding: abstract-only. Every load-bearing number is copied from the supplied abstract in `metadata.md`/`metadata.json`, tagged `[result]`. No full text was available, so no evidence table/figure files back these numbers.

## C01: Global ADRD mortality increased among adults aged 65 years and older
- **Statement**: The global mortality rate of Alzheimer's disease and other dementias among adults aged >=65 years increased by 115%, from 6.5 (95% UI 1.5-18) per 100,000 population in 1991 to 14 (95% UI 3.5-37) per 100,000 population in 2021, with AAPC 1.10% (95%CI 0.45%-1.76%).
- **Status**: supported
- **Falsification criteria**: A reanalysis of the same GBD 2021 ADRD population showing no increase in the global mortality rate among adults aged >=65 years from 1991 to 2021, or materially different estimates outside the reported uncertainty intervals.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract reports mortality rate, uncertainty intervals, percent increase, and AAPC directly.
- **Interpretation**: The paper frames rising mortality as part of an escalating healthcare challenge.
- **Sources**:
  - 115%, 6.5 (95% UI 1.5–18), 14 (95% UI 3.5–37), AAPC 1.10% (95%CI 0.45%−1.76%) <- metadata.md (Abstract) «The global mortality of ADRD among adults aged ≥65 years increased by 115%, from 6.5 (95% UI 1.5–18) per 100,000 population in 1991 to 14 (95% UI 3.5–37) per 100,000 population in 2021, with an Average Annual Percentage Change (AAPC) of 1.10% (95%CI 0.45%−1.76%).» [result]
- **Dependencies**: none
- **Tags**: mortality, ADRD, GBD-2021, AAPC

## C02: Global ADRD prevalence count increased among adults aged 65 years and older
- **Statement**: The prevalence of ADRD among adults aged >=65 years increased by 160% between 1991 and 2021, from 18.7 (95%UI 14.9-23.2) million to 49 (95%UI 38.6-61.2) million.
- **Status**: supported
- **Falsification criteria**: A reanalysis of the same GBD 2021 ADRD population showing no increase in global prevalent-case counts from 1991 to 2021, or materially different estimates outside the reported uncertainty intervals.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract reports the prevalence count increase and endpoints directly.
- **Interpretation**: The abstract attributes the increase largely to expansion of the older-adult population.
- **Sources**:
  - 160%, 18.7 (95%UI 14.9–23.2) million, 49 (95%UI 38.6–61.2) million <- metadata.md (Abstract) «The prevalence of ADRD in adults aged ≥65 years increased by 160% between 1991 and 2021, from 18.7 (95%UI 14.9–23.2) million to 49 (95%UI 38.6–61.2) million.» [result]
- **Dependencies**: none
- **Tags**: prevalence, ADRD, older-adult-population

## C03: Age-standardized ADRD prevalence rate changed slightly between 1991 and 2021
- **Statement**: The age-standardized prevalence of ADRD among adults aged >=65 years increased from 11,977 (95%UI 9,438-14,935) per 100,000 population in 1991 to 12,124 (95%UI 9,489-15,204) per 100,000 population in 2021.
- **Status**: supported
- **Falsification criteria**: A reanalysis showing the age-standardized prevalence rate did not move from the 1991 estimate toward the 2021 estimate, or estimates outside the reported uncertainty intervals.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract reports both age-standardized prevalence endpoints.
- **Interpretation**: Compared with the larger increase in prevalent-case counts, this supports the abstract's framing that population aging is a major driver; the abstract does not provide decomposition details.
- **Sources**:
  - 11,977 (95%UI 9,438–14,935), 12,124 (95%UI 9,489–15,204) <- metadata.md (Abstract) «The aged ≥65 years age-standardized prevalence of ADRD in this age group increased from 11,977 (95%UI 9,438–14,935) per 100,000 population in 1991 to 12,124 (95%UI 9,489–15,204) per 100,000 population in 2021.» [result]
- **Dependencies**: C02
- **Tags**: age-standardization, prevalence-rate, population-aging

## C04: Female prevalent-case counts exceeded male counts in both reported years
- **Statement**: ADRD prevalent-case counts among adults aged >=65 years were higher for women than men in both 1991 and 2021: males increased from 6.2 (95%UI 4.8-7.8) million to 17.2 (95%UI 13.4-21.6) million, while women increased from 12.5 (95%UI 10.0-15.4) million to 31.7 (95%UI 25.1-39.6) million.
- **Status**: supported
- **Falsification criteria**: A reanalysis showing male prevalent-case counts equal to or exceeding female counts in either reported endpoint, or endpoint estimates outside the reported uncertainty intervals.
- **Proof**: [E02]
- **Evidence basis**: The abstract reports sex-stratified prevalent-case counts for 1991 and 2021.
- **Interpretation**: The result indicates a sex disparity in counts; the abstract does not provide age-structure adjustment by sex or causal explanation.
- **Sources**:
  - male 6.2 (95%UI 4.8–7.8) million, male 17.2 (95%UI 13.4–21.6) million, women 12.5 (95%UI 10.0–15.4) million, women 31.7 (95%UI 25.1–39.6) million <- metadata.md (Abstract) «males: from 6.2 (95%UI 4.8–7.8) million in 1991 to 17.2 (95%UI 13.4–21.6) million in 2021; women: from 12.5 (95%UI 10.0–15.4) million in 1991 to 31.7 (95%UI 25.1–39.6) million in 2021» [result]
- **Dependencies**: C02
- **Tags**: sex-disparity, prevalence, female-burden

## C05: In 2021, ADRD caused substantial deaths and DALYs among adults aged 65 years and older
- **Statement**: In 2021, ADRD among adults aged >=65 years caused 8.02 (95%UI 1.34-22.19) million deaths and 25.38 (95%UI 23.18-71.20) million DALYs attributable to dementia.
- **Status**: supported
- **Falsification criteria**: A reanalysis of GBD 2021 ADRD in adults aged >=65 years showing 2021 deaths or DALYs outside the reported uncertainty intervals.
- **Proof**: [E02]
- **Evidence basis**: The abstract reports 2021 death and DALY estimates directly.
- **Interpretation**: The abstract uses these burden estimates to motivate healthcare-system concern; detailed DALY components are not available from provided input.
- **Sources**:
  - 8.02 (95%UI 1.34–22.19) million deaths, 25.38 (95%UI 23.18–71.20) million DALYs <- metadata.md (Abstract) «In 2021, ADRD in adults aged ≥65 years caused 8.02 (95%UI 1.34–22.19) million deaths and 25.38 (95%UI 23.18–71.20) million DALYs attributable to dementia» [result]
- **Dependencies**: none
- **Tags**: deaths, DALYs, burden

## C06: The abstract identifies high BMI, high fasting glucose, and smoking as modifiable risk factors
- **Statement**: The abstract identifies high BMI, high fasting glucose, and smoking as three modifiable risk factors considered for ADRD burden metrics among adults aged >=65 years.
- **Status**: supported
- **Falsification criteria**: Full-text methods showing these three risk factors were not included in the paper's ADRD risk-attribution analysis, or that the abstract's statement is erroneous.
- **Proof**: [E01, E03]
- **Evidence basis**: The abstract names the risk factors in the outcomes/methods description and again states they remained modifiable risk factors.
- **Interpretation**: The paper recommends strengthening management of risk-factor elements; specific attributable fractions are not available from provided input.
- **Sources**:
  - three risk factors: high BMI, high fasting glucose, smoking <- metadata.md (Abstract) «the fractions of these metrics that were attributable to three risk factors (high BMI, high fasting glucose, and smoking) that met GBD» [result]
  - remained modifiable risk factors <- metadata.md (Abstract) «high BMI, high fasting glucose, and smoking remained modifiable risk factors in all risk factors» [result]
- **Dependencies**: none
- **Tags**: risk-factors, high-BMI, fasting-glucose, smoking
