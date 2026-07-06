# Claims

> Grounding: abstract-only. Every load-bearing number is copied verbatim from `metadata.md` / `metadata.json`. No full text, tables, or figures were available, so the abstract is the sole evidence source.

## C01: Global age-standardized prevalence increased from 1990 to 2021
- **Statement**: The global age-standardized prevalence of Alzheimer's disease and other dementias increased from 672 (95% uncertainty interval: 589 to 764) per 100,000 population in 1990 to 694 (603 to 794) per 100,000 population in 2021, with AAPC 0.09% (95% confidence interval: 0.06% to 0.11%).
- **Status**: supported
- **Falsification criteria**: Re-analysis of GBD 2021 AD and other dementia burden data showing no increase in age-standardized prevalence over 1990-2021, or an AAPC confidence interval inconsistent with the abstract's reported interval.
- **Proof**: [E01]
- **Evidence basis**: Abstract Result reports the 1990 and 2021 prevalence estimates and AAPC.
- **Interpretation**: The prevalence burden rose modestly over the study period; the abstract does not provide causal decomposition beyond the conclusion's partial attribution.
- **Sources**:
  - prevalence 672 (95% uncertainty interval: 589 to 764) per 100,000 population in 1990; 694 (603 to 794) per 100,000 population in 2021; AAPC 0.09% (95% confidence interval: 0.06% to 0.11%) ← metadata.md (Abstract Result) «The global age-standardized prevalence of AD and other dementias increased from 672 (95% uncertainty interval: 589 to 764) per 100,000 population in 1990 to 694 (603 to 794) per 100,000 population in 2021, with AAPCs of 0.09% (95% confidence interval: 0.06% to 0.11%).» [result]
- **Dependencies**: none
- **Tags**: prevalence, AAPC, GBD-2021

## C02: Age-standardized mortality did not change over 1990-2021
- **Statement**: Age-standardized mortality of Alzheimer's disease and other dementias did not change over 1990-2021, with AAPC 0.00% [-0.01% to 0.02%].
- **Status**: supported
- **Falsification criteria**: Re-analysis of the same GBD 2021 outcome showing a materially positive or negative mortality AAPC whose uncertainty interval excludes zero.
- **Proof**: [E02]
- **Evidence basis**: Abstract Result directly reports no change in age-standardized mortality and gives the AAPC interval.
- **Interpretation**: Mortality trends differ from the reported prevalence trend, but exact mortality rates are not available from provided input.
- **Sources**:
  - mortality AAPC 0.00% [-0.01% to 0.02%] ← metadata.md (Abstract Result) «However, age-standardized mortality did not change (AAPCs: 0.00% [−0.01% to 0.02%])» [result]
- **Dependencies**: none
- **Tags**: mortality, AAPC, age-standardized

## C03: Age-standardized DALYs slightly increased over 1990-2021
- **Statement**: Age-standardized DALYs for Alzheimer's disease and other dementias slightly increased from 446 (206 to 958) to 451 (213 to 950) per 100,000 population, with AAPC 0.01% [0.00% to 0.03%].
- **Status**: supported
- **Falsification criteria**: Re-analysis of GBD 2021 DALY data showing no increase or a materially different AAPC interval for 1990-2021.
- **Proof**: [E03]
- **Evidence basis**: Abstract Result reports the DALY estimates and AAPC.
- **Interpretation**: DALYs changed less than prevalence and are described by the authors as only slightly increasing.
- **Sources**:
  - DALYs 446 (206 to 958) to 451 (213 to 950) per 100,000 population; AAPC 0.01% [0.00% to 0.03%] ← metadata.md (Abstract Result) «age-standardized DALYs slightly increased from 446 (206 to 958) to 451 (213 to 950) per 100,000 population (AAPCs: 0.01% [0.00% to 0.03%]).» [result]
- **Dependencies**: none
- **Tags**: DALYs, AAPC, age-standardized

## C04: Peak burden patterns differ by age, SDI, and geography
- **Statement**: Highest prevalence remained in the population aged 65-69 and countries with high-middle SDI such as East Asia (e.g., China), while highest mortality and DALYs were found in the population aged 65-69 and countries with low-middle SDI such as South Asia (e.g., India).
- **Status**: supported
- **Falsification criteria**: Stratified GBD 2021 analysis showing a different age group or SDI/geographic grouping for the reported highest prevalence, mortality, or DALY patterns.
- **Proof**: [E04]
- **Evidence basis**: Abstract Result states these stratified burden patterns.
- **Interpretation**: The same age band is highlighted for multiple outcomes, but SDI/geographic burden differs between prevalence and mortality/DALYs.
- **Sources**:
  - population aged 65-69; high-middle SDI East Asia/China prevalence; low-middle SDI South Asia/India mortality and DALYs ← metadata.md (Abstract Result) «While the highest prevalence remained in population aged 65–69 and the countries with a high-middle sociodemographic index (SDI) such as East Asia (e.g., China), the highest mortality and DALYs were found in population aged 65–69 and the countries with a low-middle SDI such as South Asia (e.g., India).» [result]
- **Dependencies**: C01, C02, C03
- **Tags**: SDI, East-Asia, South-Asia, age-65-69

## C05: High fasting plasma glucose ranked as the highest DALY risk factor
- **Statement**: High fasting plasma glucose ranked as the highest risk factor for DALYs from Alzheimer's disease and other dementias during 1990-2021.
- **Status**: supported
- **Falsification criteria**: Risk-factor attribution analysis from GBD 2021 ranking another risk factor above high fasting plasma glucose for AD and other dementia DALYs over 1990-2021.
- **Proof**: [E03]
- **Evidence basis**: Abstract Result directly names high fasting plasma glucose as the highest-ranked DALY risk factor.
- **Interpretation**: The conclusion suggests controlling high fasting plasma glucose may be needed for reducing DALYs, but intervention effect sizes are not available from provided input.
- **Sources**:
  - high fasting plasma glucose highest risk factor for DALYs during 1990-2021 ← metadata.md (Abstract Result) «High fasting plasma glucose ranked the highest risk factor for DALYs during 1990–2021.» [result]
- **Dependencies**: C03
- **Tags**: risk-factor, fasting-plasma-glucose, DALYs
