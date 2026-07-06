# Claims

> Grounding: abstract-only. Every load-bearing number is copied from the provided `metadata.md` abstract. No full text, tables, figures, or supplements were provided, so the abstract is the sole evidence source.

## C01: Global age-standardized DALYs and mortality declined over time
- **Statement**: Globally, age-standardized DALYs and mortality rates for individuals aged 65 and older with Alzheimer's disease and other dementias declined over 1990 to 2021.
- **Status**: supported
- **Falsification criteria**: Reanalysis of the same GBD 2021 target population showing no decline, or an increase, in either global age-standardized DALYs or mortality rates over 1990 to 2021.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly states that global age-standardized DALYs and mortality rates for individuals aged 65 and older declined over time.
- **Interpretation**: The global age-standardized rate trend improves despite the abstract's public-health framing that dementia burden in the elderly is predicted to rise.
- **Sources**:
  - 1990 to 2021 target period ← metadata.md:13 «We analyzed the disease burden of Alzheimer’s disease and other dementias among individuals aged 65 and older from 1990 to 2021» [input]
  - decline over time ← metadata.md:13 «Globally, age-standardized DALYs and mortality rates for individuals aged 65 and older have declined over time.» [result]
- **Dependencies**: none
- **Tags**: DALYs, mortality, age-standardized rates, GBD 2021

## C02: Dementia burden is significantly associated with SDI
- **Statement**: The disease burden of Alzheimer's disease and other dementias among adults aged 65 and older is significantly associated with SDI.
- **Status**: supported
- **Falsification criteria**: Reanalysis showing no statistically meaningful association between SDI and dementia burden in the same population and period.
- **Proof**: [E02]
- **Evidence basis**: The abstract states that disease burden is significantly associated with SDI after analyzing mortality rates and DALYs with SDI.
- **Interpretation**: Socio-demographic development is a central stratifier for interpreting dementia burden, not merely a descriptive country grouping.
- **Sources**:
  - association with SDI ← metadata.md:13 «We find that the disease burden of dementia is significantly associated with SDI.» [result]
- **Dependencies**: none
- **Tags**: SDI, disease burden, DALYs, mortality

## C03: High-SDI countries have higher baseline burden than low-SDI countries
- **Statement**: High-SDI countries have 169% higher baseline levels of dementia burden than low-SDI countries at their current level of social development.
- **Status**: supported
- **Falsification criteria**: Frontier or SDI-stratified reanalysis estimating a substantially different high-SDI versus low-SDI baseline burden contrast.
- **Proof**: [E02, E03]
- **Evidence basis**: The abstract reports the 169% high-SDI versus low-SDI baseline contrast directly.
- **Interpretation**: Higher SDI is associated with higher baseline dementia burden in the authors' model, while the abstract separately notes that population distribution concentrates burden in lower-SDI populations.
- **Sources**:
  - 169% higher baseline burden ← metadata.md:13 «High SDI countries have 169% higher baseline levels of dementia burden compared to low SDI countries, as estimated based on their current level of social development.» [result]
- **Dependencies**: C02
- **Tags**: high SDI, low SDI, frontier analysis, baseline burden

## C04: Inequality analysis locates burden in lower-SDI populations despite DALYs increasing with SDI
- **Statement**: Although the overall trend of DALYs for dementia increases with SDI, the burden is primarily concentrated in populations with lower SDI because non-developed countries account for the majority of the population.
- **Status**: supported
- **Falsification criteria**: Inequality analysis showing that age-standardized DALYs are not concentrated in lower-SDI populations, or that population distribution does not support the stated concentration pattern.
- **Proof**: [E04]
- **Evidence basis**: The abstract states both the increasing DALY trend with SDI and the concentration of burden in lower-SDI populations.
- **Interpretation**: The result distinguishes rate-level association with SDI from population-weighted distribution of burden.
- **Sources**:
  - DALYs increase with SDI and concentrate in lower-SDI populations ← metadata.md:13 «while the overall trend of DALYs for dementia increases with SDI, the burden is primarily concentrated in populations with lower SDI, as non-developed countries account for the majority of the population.» [result]
- **Dependencies**: C02
- **Tags**: health inequality, DALYs, SDI, population distribution

## C05: Most countries exceed their SDI-associated minimum burden, with low/middle-SDI burden increasing and gaps narrowing
- **Statement**: The dementia burden in most countries is higher than the minimum disease burden associated with their SDI; low- and middle-SDI countries show an increasing burden trend, and the burden gap among SDI regions is continuously narrowing.
- **Status**: supported
- **Falsification criteria**: Country-level frontier analysis showing most countries at or below their SDI-associated minimum burden, or trend analysis showing no increase in low/middle-SDI countries and no narrowing of gaps across SDI regions.
- **Proof**: [E03, E04]
- **Evidence basis**: The abstract states these three findings directly.
- **Interpretation**: The frontier result suggests possible reducible burden relative to SDI-associated minima, while the trend result points to converging cross-SDI gaps.
- **Sources**:
  - most countries above minimum burden ← metadata.md:13 «The burden of disease in most countries is higher than the minimum disease burden associated with SDI in those countries.» [result]
  - low and middle SDI increasing trend ← metadata.md:13 «The burden of disease in low and middle SDI countries has been showing an increasing trend.» [result]
  - SDI-region gap narrowing ← metadata.md:13 «The gap in disease burden among regions with different SDI levels is also continuously narrowing.» [result]
- **Dependencies**: C02, C03, C04
- **Tags**: frontier analysis, low SDI, middle SDI, burden gap

## C06: Dementia significantly reduces healthy life expectancy among adults aged 65 and older
- **Statement**: The global population aged 65 and older experiences a significant reduction in healthy life expectancy due to dementia.
- **Status**: supported
- **Falsification criteria**: Reanalysis of GBD 2021 or comparable burden data showing no significant reduction in healthy life expectancy attributable to dementia among adults aged 65 and older.
- **Proof**: [E01]
- **Evidence basis**: The abstract states this healthy-life-expectancy impact directly.
- **Interpretation**: This claim translates the DALY/mortality burden into a public-health consequence for older adults; the abstract does not provide exact healthy-life-expectancy loss values.
- **Sources**:
  - significant reduction in healthy life expectancy ← metadata.md:13 «The global population aged 65 and older experiences a significant reduction in healthy life expectancy due to dementia.» [result]
- **Dependencies**: C01
- **Tags**: healthy life expectancy, dementia burden, older adults
