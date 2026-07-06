# Claims

> Grounding: abstract-only. Every load-bearing number in a Statement is copied verbatim from `metadata.md` or `metadata.json`; source quotes are tagged `[result]` for article findings and `[input]` for bibliographic metadata. No full text, tables, or figures were provided.

## C01: 2021 global mortality and prevalence were substantial in adults aged 60 years or older
- **Statement**: In 2021, global mortality from AD and other dementias among individuals aged 60 and older reached approximately 1,922,970.75 cases (95% CI: 480,348.08 to 5,104,315.95), and prevalence was 52,560,253.51 cases (95% CI: 41,399,948.84 to 65,633,448.71).
- **Status**: supported
- **Falsification criteria**: Reanalysis of the same GBD 2021 scope showing 2021 mortality or prevalence values outside the reported confidence intervals.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly reports the 2021 global mortality and prevalence counts and confidence intervals.
- **Interpretation**: Establishes the scale of the late-period global dementia burden among adults aged 60 years or older.
- **Sources**:
  - 2021 mortality 1,922,970.75 cases (95% CI: 480,348.08 to 5,104,315.95) ← metadata.md (Abstract) «In 2021, global mortality from AD and other dementias among individuals aged 60 and older reached approximately 1,922,970.75 cases (95% CI: 480,348.08 to 5,104,315.95)» [result]
  - prevalence 52,560,253.51 cases (95% CI: 41,399,948.84 to 65,633,448.71) ← metadata.md (Abstract) «and the prevalence was 52,560,253.51 cases (95% CI: 41,399,948.84 to 65,633,448.71)» [result]
- **Dependencies**: none
- **Tags**: mortality, prevalence, GBD-2021, adults-60-plus

## C02: High BMI and High FPG were prominent risk factors
- **Statement**: High Body Mass Index (BMI) and High Fasting Plasma Glucose (FPG) were prominent risk factors for AD and other dementias in the study's burden analysis.
- **Status**: supported
- **Falsification criteria**: Access to the full risk-attribution results showing that High BMI or High FPG were not prominent relative to other evaluated risk factors.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly names High BMI and High FPG as prominent risk factors.
- **Interpretation**: Risk-factor targeting is part of the intervention framing, but attributable fractions and subgroup patterns are not available from provided input.
- **Sources**:
  - High BMI and High FPG prominent risk factors ← metadata.md (Abstract) «High Body Mass Index (BMI) and High Fasting Plasma Glucose (FPG) were prominent risk factors.» [result]
- **Dependencies**: none
- **Tags**: risk-factors, BMI, fasting-plasma-glucose

## C03: AD cases are projected to increase nearly fourfold by 2050
- **Statement**: Projections suggest a near fourfold increase in AD cases by 2050, driven by population growth and aging, with females disproportionately affected.
- **Status**: supported
- **Falsification criteria**: BAPC projection outputs from the same study scope showing substantially less than near-fourfold growth, different primary drivers, or no disproportionate female impact.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly reports the projection direction, approximate scale, named drivers, and sex-disparity direction.
- **Interpretation**: The projected increase appears demographic in large part, but exact projected case counts and uncertainty intervals are not available from provided input.
- **Sources**:
  - near fourfold increase by 2050 ← metadata.md (Abstract) «Projections suggest a near fourfold increase in AD cases by 2050, driven by population growth and aging, with females disproportionately affected.» [result]
- **Dependencies**: C01
- **Tags**: projection, BAPC, 2050, population-aging, sex-disparity

## C04: Health inequalities persist with higher burdens in high-SDI regions
- **Statement**: Health inequalities persist, with higher disease burdens in high-SDI regions.
- **Status**: supported
- **Falsification criteria**: Full inequality analysis showing no persistent health inequalities or no higher burdens in high-SDI regions.
- **Proof**: [E04]
- **Evidence basis**: The abstract directly states the persistence of health inequalities and names high-SDI regions as carrying higher disease burdens.
- **Interpretation**: The direction is available, but inequality metrics, SDI thresholds, regional rankings, and uncertainty are not available from provided input.
- **Sources**:
  - higher burdens in high-SDI regions ← metadata.md (Abstract) «Health inequalities persist, with higher disease burdens in high-SDI regions.» [result]
- **Dependencies**: none
- **Tags**: health-inequality, SDI, regional-disparity

## C05: COVID-19 impacted mortality unevenly across regions
- **Statement**: The COVID-19 pandemic impacted mortality unevenly, highlighting regional disparities.
- **Status**: supported
- **Falsification criteria**: Pandemic-period observed-versus-expected mortality analysis showing uniform mortality effects across regions or no regional disparity.
- **Proof**: [E05]
- **Evidence basis**: The abstract states that excess mortality was evaluated by comparing actual versus expected deaths and reports uneven pandemic impact on mortality.
- **Interpretation**: The abstract supports an uneven-impact claim but does not provide regional excess-mortality values.
- **Sources**:
  - evaluated excess mortality ← metadata.md (Abstract) «We evaluated excess mortality by comparing actual versus expected deaths during the pandemic.» [result]
  - uneven mortality impact ← metadata.md (Abstract) «The pandemic impacted mortality unevenly, highlighting regional disparities.» [result]
- **Dependencies**: none
- **Tags**: COVID-19, excess-mortality, regional-disparity

## C06: Incidence rates declined from 1990 to 2021 while overall burden remains high and is expected to rise
- **Statement**: Although incidence rates declined from 1990 to 2021, the overall burden of AD and dementias remains substantial and is expected to rise significantly by 2050.
- **Status**: supported
- **Falsification criteria**: Same-scope trend analysis showing non-declining incidence rates from 1990 to 2021, or projections showing no significant burden increase by 2050.
- **Proof**: [E06]
- **Evidence basis**: The abstract directly states the incidence-rate direction and the burden/projection conclusion.
- **Interpretation**: Supports a distinction between incidence-rate trends and absolute future burden; exact ASIR, EAPC, and DALY values are unavailable.
- **Sources**:
  - 1990 to 2021 incidence decline and 2050 burden expectation ← metadata.md (Abstract) «Although incidence rates declined from 1990 to 2021, the overall burden of AD and dementias remains substantial and is expected to rise significantly by 2050.» [result]
- **Dependencies**: C01, C03
- **Tags**: incidence, temporal-trends, EAPC, future-burden
