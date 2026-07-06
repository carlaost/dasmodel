# Experiments (Analysis Plans)

> Declarative reconstruction of the analytical pipeline described (at a high level) in the abstract.
> Directional only — NO exact numbers (those live in `logic/claims.md` with their source quotes).
> Procedural detail the abstract omits is marked "Not specified in the published abstract".

## E01: Univariable Cox screening of candidate AD/ADRD risk-related diseases
- **Verifies**: C01
- **Setup**:
  - Model: Univariable Cox proportional-hazards models, one per candidate disease.
  - Hardware: Not specified in the published abstract (analytical/statistical computation).
  - Dataset: Medicare 5% sample (CMS administrative claims/enrollment data); outcome = clinical AD/ADRD diagnosis.
  - System: Not specified in the published abstract.
- **Procedure**:
  1. Define the AD/ADRD outcome and follow-up time from Medicare records (code definitions not specified).
  2. Fit a univariable Cox model for each candidate risk-related disease (and the dual-eligibility low-income indicator).
  3. Rank candidates by strength of individual association to identify the "most powerful predictors".
- **Metrics**: Per-disease hazard ratios / association strength (units: hazard ratio); statistical significance.
- **Expected outcome**:
  - A subset of diseases shows the strongest individual associations with AD/ADRD risk and is carried forward to the multivariable stage.
- **Baselines**: Each disease against the null (no association).
- **Dependencies**: none

## E02: Multivariable Cox model construction and predictor identification
- **Verifies**: C01
- **Setup**:
  - Model: Multivariable Cox proportional-hazards model jointly adjusting for selected predictors.
  - Dataset: Medicare 5% sample; outcome = clinical AD/ADRD diagnosis.
  - System: Not specified in the published abstract.
- **Procedure**:
  1. Take candidates surviving univariable screening (E01).
  2. Fit multivariable Cox models, applying the study's selection criterion (criterion not specified) to arrive at the final predictor set.
  3. Confirm the identified model comprises the nine diseases as jointly retained primary determinants.
- **Metrics**: Adjusted hazard ratios; model fit / predictive performance (specifics not specified).
- **Expected outcome**:
  - A compact multivariable model retaining the nine diseases as the primary determinants of AD/ADRD risk variation.
- **Baselines**: Univariable estimates from E01; comparison of predictor subsets.
- **Dependencies**: E01

## E03: Total-PAF computation and age-stratified analysis
- **Verifies**: C02, C03
- **Setup**:
  - Model: PAF estimation built on the multivariable Cox risk estimates (E02).
  - Dataset: Medicare 5% sample; general population of older adults, stratified by age.
  - System: Not specified in the published abstract.
- **Procedure**:
  1. Compute the total PAF explained by the nine-disease predictor set for the general older-adult population.
  2. Decompose the total PAF into disease-specific PAFs.
  3. Repeat across age strata to assess how the explained fraction varies with age.
- **Metrics**: Total PAF (%); disease-specific PAF shares (% of total PAF); explained fraction by age stratum.
- **Expected outcome**:
  - The explained fraction of total PAF rises across increasing age strata.
  - Hypertension, stroke, and depression emerge as the largest disease-specific contributors overall.
- **Baselines**: Comparison across age strata; disease-specific vs total PAF.
- **Dependencies**: E02

## E04: Race- and sex-specific PAF decomposition
- **Verifies**: C03, C04, C05, C06, C07, C08, C09
- **Setup**:
  - Model: PAF decomposition (as in E03) applied within demographic strata.
  - Dataset: Medicare 5% sample, stratified into sex (male/female) and race groups (Black, Asian, Hispanic, White, Native American).
  - System: Not specified in the published abstract.
- **Procedure**:
  1. For each race- and sex-specific subpopulation, compute total PAF and decompose into disease-specific PAFs.
  2. Rank disease-specific PAF contributions within each subpopulation.
  3. Identify the leading contributor(s) and secondary contributors per subpopulation.
- **Metrics**: Disease-specific PAF shares (% of total PAF) per subpopulation; contributor rankings.
- **Expected outcome**:
  - Leading contributor differs by subpopulation: hypertension dominates in Black/Asian/Hispanic groups; stroke leads for males; depression leads for females and White individuals; hypertension and depression co-lead for Native Americans; heart failure ranks fourth throughout; a subpopulation-specific tail (hypotension, diabetes, arrhythmia, TBI) follows.
- **Baselines**: Cross-subpopulation comparison; general-population ranking from E03.
- **Dependencies**: E03
