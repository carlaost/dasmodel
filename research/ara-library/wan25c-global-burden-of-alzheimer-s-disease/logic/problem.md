# Problem Specification

> Grounding: abstract-only. Observations below are copied from or bounded by `metadata.md` and `metadata.json`; no full text was available.

## Observations

### O01: Current burden data are lacking in many places
- **Statement**: The abstract states that "In most countries and territories, current data on the burden of Alzheimer's disease (AD) and other dementias are lacking."
- **Evidence**: `metadata.md`, Abstract Introduction.
- **Implication**: The study is motivated by a need for updated global, regional, and national burden estimates.

### O02: Global age-standardized prevalence increased from 1990 to 2021
- **Statement**: Global age-standardized prevalence increased from 672 (95% uncertainty interval: 589 to 764) per 100,000 population in 1990 to 694 (603 to 794) per 100,000 population in 2021, with AAPC 0.09% (95% confidence interval: 0.06% to 0.11%).
- **Evidence**: `metadata.md`, Abstract Result.
- **Implication**: Prevalence burden rose over the GBD 2021 study window.

### O03: Mortality was stable while DALYs slightly increased
- **Statement**: Age-standardized mortality did not change (AAPC 0.00% [-0.01% to 0.02%]), while age-standardized DALYs slightly increased from 446 (206 to 958) to 451 (213 to 950) per 100,000 population with AAPC 0.01% [0.00% to 0.03%].
- **Evidence**: `metadata.md`, Abstract Result.
- **Implication**: The burden profile is not uniform across prevalence, mortality, and DALYs.

### O04: Burden concentration differs by SDI/geographic grouping
- **Statement**: Highest prevalence remained in population aged 65-69 and countries with high-middle SDI such as East Asia (e.g., China), while highest mortality and DALYs were found in population aged 65-69 and countries with low-middle SDI such as South Asia (e.g., India).
- **Evidence**: `metadata.md`, Abstract Result.
- **Implication**: Inequality analysis is central to interpreting the burden estimates.

### O05: High fasting plasma glucose is the top-ranked DALY risk factor
- **Statement**: High fasting plasma glucose ranked as the highest risk factor for DALYs during 1990-2021.
- **Evidence**: `metadata.md`, Abstract Result.
- **Implication**: The abstract identifies one modifiable risk-factor priority for DALY reduction.

## Gaps

### G01: Missing current country/territory burden data
- **Statement**: The abstract explicitly says current burden data are lacking in most countries and territories.
- **Caused by**: O01.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

### G02: Unequal burden patterns require stratified interpretation
- **Statement**: Global summary trends alone do not capture the different age, SDI, and regional patterns reported for prevalence versus mortality/DALYs.
- **Caused by**: O02, O03, O04.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

## Key Insight

- **Insight**: GBD 2021 burden estimates combined with AAPC trend analysis can characterize AD and other dementia burden trends and inequalities across global, regional, and national levels from 1990 to 2021.
- **Derived from**: O01-O04.
- **Enables**: A source-bounded comparison of prevalence, mortality, DALYs, age group, SDI, geography, and risk-factor priority.

## Assumptions

- A1: GBD 2021 contains extractable disease-burden data for AD and other dementias during 1990-2021.
- A2: AAPCs of age-standardized prevalence, mortality, and DALYs can be used as indicators to evaluate healthcare-system-relevant burden trends.
- A3: Details of GBD case definitions, model structure, uncertainty propagation, and country-level extraction procedures are not available from provided input.
