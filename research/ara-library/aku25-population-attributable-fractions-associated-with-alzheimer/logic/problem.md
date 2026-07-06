# Problem Specification

> Source: conference abstract (Innovation in Aging 2025, Vol. 9, Suppl. 2, pp. 743–744). All
> observation numbers are transcribed verbatim from the abstract text. Where the abstract does not
> state a value, the field reads "Not specified in the published abstract".

## Observations

### O1: Many AD/ADRD risk factors are known but their joint effect is uncertain
- **Statement**: "Although numerous risk factors for Alzheimer's disease (AD) and related dementias (ADRD) have been identified, their combined influence on risk remains uncertain."
- **Evidence**: Abstract, opening sentence (p. 743).
- **Implication**: Individual risk-factor associations do not translate into a quantified, jointly-adjusted picture of how much of the population's AD/ADRD burden is attributable to each factor.

### O2: A large administrative cohort is available
- **Statement**: The study uses "a high-power 5%-sample of the Medicare population" as its data source; low income is operationalized through dual Medicare eligibility.
- **Evidence**: Abstract (p. 743). Exact sample size N, follow-up window, calendar years, and ICD code definitions: Not specified in the published abstract.
- **Implication**: The scale of Medicare data supports jointly-adjusted survival modeling and PAF estimation for demographic subpopulations that are usually under-powered.

### O3: Nine comorbid diseases dominate AD/ADRD risk variation
- **Statement**: "The identified model included nine diseases—heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, traumatic brain injury, and diabetes mellitus—as primary determinants of variation in AD/ADRD risk."
- **Evidence**: Abstract (p. 744).
- **Implication**: A tractable predictor set explains the bulk of the modeled attributable risk, enabling PAF decomposition.

### O4: The explained fraction of total PAF rises with age
- **Statement**: "The fraction of the total PAF explained by the predictors increased with age."
- **Evidence**: Abstract (p. 744). Numeric PAF-vs-age values: Not specified in the published abstract.
- **Implication**: The predictor set accounts for a progressively larger share of attributable AD/ADRD risk in older age strata.

### O5: Attributable burden is heterogeneous across race and sex
- **Statement**: Disease-specific PAF contributions differ sharply by subpopulation — e.g., hypertension reaches 45–50% of total PAF for Black, Asian, and Hispanic subpopulations; stroke is the primary contributor for males (>30%); depression is highest among females and White individuals (~30%).
- **Evidence**: Abstract (p. 744).
- **Implication**: A single population-average PAF ranking masks clinically important disparities; prevention priorities differ by demographic group.

## Gaps

### G1: No quantified joint / attributable contribution of AD/ADRD risk-related diseases
- **Statement**: Prior work identifies risk factors individually but has not quantified their combined, jointly-adjusted contribution to the population-level risk of clinical AD/ADRD diagnosis.
- **Caused by**: O1
- **Existing attempts**: Univariable associations and hazard ratios for isolated risk factors (the abstract does not enumerate specific prior studies).
- **Why they fail**: Isolated associations neither adjust for co-occurring diseases nor translate into a population-attributable share, so they cannot rank prevention targets.

### G2: Subpopulation-specific attributable burden unquantified
- **Statement**: The degree to which specific diseases drive AD/ADRD risk differs across race- and sex-specific subpopulations, but this decomposition has not been quantified at scale.
- **Caused by**: O2, O5
- **Existing attempts**: Population-average risk-factor analyses.
- **Why they fail**: Population-average estimates obscure the subpopulation heterogeneity that the abstract demonstrates (e.g., hypertension dominating in Black/Asian/Hispanic groups vs depression in White individuals).

## Key Insight
- **Insight**: Combining a high-power Medicare 5% sample with univariable-then-multivariable Cox modeling to select a compact nine-disease predictor set, and then decomposing the *total* PAF into *disease-specific* PAFs stratified by age, race, and sex, converts scattered risk-factor associations into a ranked, population-level, subpopulation-resolved attributable-burden map for AD/ADRD.
- **Derived from**: O1, O2, O3, O5
- **Enables**: Identification of the leading modifiable attributable contributors (hypertension, stroke, depression) and quantification of how those priorities shift across demographic groups.

## Assumptions
- A1: A clinical AD/ADRD diagnosis recorded in Medicare administrative data is a valid outcome for survival modeling.
- A2: Dual Medicare eligibility is a valid proxy for low income.
- A3: The nine selected diseases (identified via the modeling procedure) capture the primary determinants of AD/ADRD risk variation in this cohort.
- A4: PAFs computed from the multivariable Cox model reflect the population-level attributable share of the modeled diseases (contingent on the causal/exposure assumptions inherent to PAF estimation — see constraints.md).
- A5 (documentation gap): The precise predictor-selection criterion, PAF estimator/formula, exposure-prevalence source, adjustment covariates, and confidence intervals are Not specified in the published abstract.
