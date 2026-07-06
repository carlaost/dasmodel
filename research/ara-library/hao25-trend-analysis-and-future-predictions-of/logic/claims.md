# Claims

> Grounding: abstract-only. Claims are drawn strictly from the provided abstract and metadata. Every load-bearing number in a `Statement` is quoted verbatim from `metadata.md` and tagged `[result]`. Full tables, figures, uncertainty intervals, and model diagnostics are not available from provided input.

## C01: Global burden increased, with East Asia highest on the reported burden metrics
- **Statement**: From 1990 to 2021, the global burden of Alzheimer's disease and other dementias significantly increased, and East Asia had the highest incidence, prevalence, and DALYs among the regions named in the abstract.
- **Status**: supported (per abstract; exact values not available from provided input)
- **Falsification criteria**: Reanalysis of the same GBD data showing no significant global increase over 1990-2021, or showing that East Asia did not have the highest incidence, prevalence, and DALYs under the paper's regional definitions.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly states a significant global increase and identifies East Asia as the highest-burden region for incidence, prevalence, and DALYs.
- **Interpretation**: East Asia is highlighted as a priority region, but the abstract does not provide exact regional rates, counts, or uncertainty intervals.
- **Sources**:
  - 1990 to 2021 ← metadata.md (Abstract) «analyze trends in the epidemiology of AD and other dementias from 1990 to 2021» [input]
  - "significantly increased" and East Asia highest ← metadata.md (Abstract) «The global burden of AD and other dementias has significantly increased, with the highest incidence, prevalence, and DALYs observed in East Asia» [result]
- **Dependencies**: none
- **Tags**: GBD, regional burden, incidence, prevalence, DALYs, East Asia

## C02: Prevalence increased notably among females over 65 compared with males
- **Statement**: A notable increase in prevalence was observed in females over 65 years compared to males.
- **Status**: supported (per abstract; exact sex-stratified prevalence values not available from provided input)
- **Falsification criteria**: Sex- and age-stratified GBD results showing no higher or notable prevalence increase among females over 65 relative to males under the paper's definitions.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly reports a notable prevalence increase in females over 65 compared to males.
- **Interpretation**: Gender- and age-aware planning is warranted, but the magnitude and statistical uncertainty are not available from provided input.
- **Sources**:
  - over 65 years ← metadata.md (Abstract) «A notable increase in prevalence was observed in females over 65 years compared to males» [result]
- **Dependencies**: C01
- **Tags**: prevalence, sex differences, aging, female, older adults

## C03: Trend changes occurred in 1995, 2005, 2011, and 2019 with acceleration after 2011 and 2019
- **Statement**: Joinpoint regression identified substantial trend changes in 1995, 2005, 2011, and 2019, with noticeable acceleration after 2011 and especially after 2019.
- **Status**: supported (per abstract; annual percentage changes not available from provided input)
- **Falsification criteria**: Joinpoint analysis on the same series failing to identify these change years or failing to show acceleration after 2011 and 2019.
- **Proof**: [E02]
- **Evidence basis**: The abstract states the Joinpoint years and acceleration pattern directly.
- **Interpretation**: The disease-burden trajectory is not a simple linear increase; it contains identifiable phases. The abstract does not specify which metric(s) each Joinpoint applies to.
- **Sources**:
  - 1995, 2005, 2011, and 2019; post-2011 and after 2019 acceleration ← metadata.md (Abstract) «Joinpoint regression analysis revealed substantial changes in trends in 1995, 2005, 2011, and 2019, with a noticeable acceleration post-2011, especially after 2019» [result]
- **Dependencies**: C01
- **Tags**: Joinpoint regression, trend change, acceleration, temporal epidemiology

## C04: Age is a significant risk factor, with risk rising sharply after 60
- **Statement**: Age was a significant risk factor for Alzheimer's disease and other dementias, with a sharp increase in risk after 60 years of age.
- **Status**: supported (per abstract; exact risk ratios not available from provided input)
- **Falsification criteria**: Age-period-cohort or equivalent analysis showing no significant age effect or no sharp increase after age 60.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly reports the age effect and the post-60 increase.
- **Interpretation**: Age-specific burden is central to forecasts and intervention targeting, but no age-specific rate table is available from provided input.
- **Sources**:
  - after 60 years of age ← metadata.md (Abstract) «Age was a significant risk factor, with a sharp increase in risk after 60 years of age» [result]
- **Dependencies**: C01
- **Tags**: age effect, age-period-cohort, risk factor, older adults

## C05: Bayesian age-period-cohort modeling projects sustained growth through 2040
- **Statement**: Bayesian age-period-cohort modeling predicts sustained growth through 2040, with age-standardized incidence and prevalence rates projected to reach 144.85 and 821.80 per 100,000, respectively.
- **Status**: supported (per abstract; uncertainty intervals not available from provided input)
- **Falsification criteria**: Replication of the stated Bayesian age-period-cohort forecast using the paper's data and settings yielding materially different 2040 age-standardized incidence or prevalence rates, or no sustained growth.
- **Proof**: [E04, E05]
- **Evidence basis**: The abstract directly reports the forecasting model class, time horizon, projected rates, and broad demographic drivers.
- **Interpretation**: The forecast attributes regional driver differences to aging populations in high-SDI regions and demographic expansion in low-SDI regions, but exact decomposition values are not available.
- **Sources**:
  - 2040, 144.85, 821.80 per 100,000 ← metadata.md (Abstract) «Bayesian age-period-cohort modeling predicts sustained growth through 2040, with age-standardized incidence and prevalence rates projected to reach 144.85 and 821.80 per 100,000 respectively» [result]
- **Dependencies**: C03, C04
- **Tags**: forecasting, Bayesian age-period-cohort, age-standardized incidence, age-standardized prevalence, 2040
