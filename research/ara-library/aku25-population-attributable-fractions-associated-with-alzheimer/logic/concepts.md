# Concepts

> Genuine technical terms used in the source abstract. Formal definitions draw on standard
> epidemiological/statistical usage; where the abstract itself sets a boundary condition, it is
> noted. Values or formulas not stated in the abstract are marked "Not specified in the published
> abstract".

## Population Attributable Fraction (PAF)
- **Notation**: PAF (also PAR% in the wider literature) — "—" for a formula, since the abstract prints none.
- **Definition**: The proportion of disease outcomes (here, clinical AD/ADRD diagnoses) in a population that would be avoided if a given exposure/risk factor were eliminated, given its prevalence and its association with the outcome. In this study PAFs are computed from multivariable Cox-model risk estimates for the modeled diseases.
- **Boundary conditions**: The exact PAF estimator, exposure-prevalence source, and adjustment set are Not specified in the published abstract. Interpreting a PAF as a causally-avoidable fraction requires the usual PAF assumptions (correct model, no unmeasured confounding, exposure causality) — see constraints.md.
- **Related concepts**: Total PAF, disease-specific PAF (PAF decomposition), Cox proportional hazards model.

## Total PAF and PAF decomposition (disease-specific PAF)
- **Notation**: —
- **Definition**: The **total PAF** is the combined attributable fraction of AD/ADRD explained by the full nine-disease predictor set; the **decomposition** partitions this total into **disease-specific PAFs**, the share attributable to each individual disease (e.g., hypertension 45–50% of total PAF in some subpopulations).
- **Boundary conditions**: The decomposition is reported as percentages "of total PAF" per disease per subpopulation; the exact allocation method (e.g., sequential/average attribution) is Not specified in the published abstract.
- **Related concepts**: Population Attributable Fraction, subpopulation stratification.

## Alzheimer's disease and related dementias (AD/ADRD)
- **Notation**: AD/ADRD
- **Definition**: The study outcome — a clinical diagnosis of Alzheimer's disease or a related dementia, ascertained from Medicare administrative records. "AD" = Alzheimer's disease specifically; "ADRD" broadens to related dementias.
- **Boundary conditions**: Outcome is a *clinical diagnosis* recorded in claims (not autopsy- or biomarker-confirmed). Specific diagnostic (ICD) code definitions: Not specified in the published abstract.
- **Related concepts**: Population Attributable Fraction, Cox proportional hazards model.

## Cox proportional hazards model (univariable / multivariable)
- **Notation**: —
- **Definition**: A semi-parametric survival-regression model relating the hazard of an event (AD/ADRD diagnosis) to covariates. **Univariable** Cox models assess each disease's individual association; **multivariable** Cox models jointly adjust for the selected predictors and produce the risk estimates that feed PAF computation.
- **Boundary conditions**: Proportional-hazards assumption applies. Time scale, censoring rules, tie handling, and covariate coding: Not specified in the published abstract.
- **Related concepts**: Population Attributable Fraction, predictor selection.

## Dual Medicare eligibility (low-income proxy)
- **Notation**: —
- **Definition**: Concurrent enrollment in both Medicare and Medicaid, used in this study as an indicator of low income to assess the joint impact of low socioeconomic status alongside comorbid diseases on AD/ADRD risk.
- **Boundary conditions**: A proxy, not a direct income measure; whether it entered the final nine-disease predictor model is Not specified in the published abstract (the abstract lists nine *diseases* as the identified model).
- **Related concepts**: Medicare 5% sample, health disparities.

## Medicare 5% sample
- **Notation**: —
- **Definition**: A 5% random sample of the U.S. Medicare beneficiary population drawn from CMS administrative claims/enrollment data, described as "high-power" — i.e., large enough to support jointly-adjusted survival modeling and subpopulation PAF decomposition.
- **Boundary conditions**: Exact N, calendar years, and inclusion/exclusion criteria: Not specified in the published abstract. Access is controlled (CMS / ResDAC).
- **Related concepts**: Dual Medicare eligibility, subpopulation stratification.

## Race- and sex-specific subpopulation stratification
- **Notation**: —
- **Definition**: The analytical strategy of computing and decomposing PAFs separately within demographic strata — reported here for males, females, and the Black, Asian, Hispanic, White, and Native American race groups — to reveal heterogeneity in attributable AD/ADRD burden.
- **Boundary conditions**: The specific race/ethnicity categorization scheme and subpopulation sample sizes: Not specified in the published abstract.
- **Related concepts**: PAF decomposition, health disparities.
