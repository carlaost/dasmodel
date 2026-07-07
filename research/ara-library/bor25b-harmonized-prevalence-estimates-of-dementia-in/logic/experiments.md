# Experiments

"Experiments" here generalize to the paper's analytical steps — a validation data collection, a regression-based estimation/prediction step, and several statistical-comparison analyses — rather than computational training runs. All numbers are withheld per the compiler convention; exact values live in `evidence/`.

## E01: SHARE-HCAP validation subsample data collection and classification
- **Verifies**: C12, C13
- **Setup**:
  - Population: individuals aged 65+ in five SHARE countries (Czech Republic, France, Germany, Denmark, Italy), selected to represent East/West/North/South Europe.
  - Sampling: weighted subsample drawn from the SHARE parent study based on word-recall test performance, heavily oversampling low scorers to ensure adequate MCI/dementia representation.
  - Instrument: SHARE-HCAP neuropsychological battery (27 cognitive indicators across five domains: memory, executive functioning, visuospatial skills, language and fluency, orientation) plus an informant report.
  - Classification protocol: factor-score-based threshold rule following Manly et al. (2022), itself based on NIA-AA diagnostic criteria.
- **Procedure**:
  1. Recruit eligible individuals from the five countries; administer the SHARE-HCAP battery May–November 2022.
  2. Derive factor-score estimates for the five cognition domains for each respondent using a normative sample as benchmark.
  3. Classify each respondent as demented, MCI, or normal per the two-domain/1.5-SD/informant-report decision rule (see `logic/solution/classification_method.md`).
  4. Address item nonresponse (concentrated in Italy for three measures) via Full Information Maximum Likelihood (FIML) estimation in the factor analysis.
  5. Tabulate response rate and sample characteristics against the SHARE parent Wave 9 sample.
- **Metrics**: response rate (%); classification prevalence (% normal / MCI / demented, with SE); sample characteristic comparability (age, sex, education, health, income) between subsample and parent sample.
- **Expected outcome**:
  - A validation subsample large enough (thousands of eligible individuals, hundreds to low thousands recruited per country) to support country-level and subsample-level classification with usable standard errors.
  - Sample characteristics broadly comparable to the SHARE parent sample on core demographics (age, sex), supporting the subsample's use as a validation base.
- **Baselines**: none (this is the paper's own primary data collection, not a comparison against a prior method).
- **Dependencies**: none

## E02: Regression-based extension of HCAP classification to SHARE-parent cognition items (Hurd et al. approach)
- **Verifies**: C06
- **Setup**:
  - Sample: the SHARE-HCAP validation subsample (with known HCAP classification from E01) intersected with a set of cognitive, health, and demographic variables available in both SHARE-HCAP and the SHARE parent study (orientation in time, immediate/delayed word recall, serial 7s, animal naming; ADL+IADL sum).
  - Method: multi-country adaptation of the regression-based approach developed by Hurd et al. (2013), relating the HCAP classification outcome to the shared cognition/health/demographic variables, weighting the SHARE-parent cognition items by their relation to the SHARE-HCAP classification.
- **Procedure**:
  1. Fit the regression relating HCAP-classified cognitive status to the shared variable set within the validation subsample.
  2. Generate predicted probabilities of normal/MCI/demented status for the same validation-subsample individuals using only the shared variables (i.e., without directly using the full HCAP battery).
  3. Compare predicted vs. directly classified prevalence, by country and for the pooled subsample (Table 2).
- **Metrics**: agreement between classified and predicted % normal/MCI/demented, at subsample and per-country level.
- **Expected outcome**: Predicted prevalence should closely track directly classified prevalence at both the country and pooled-subsample level, providing evidence that the regression-based extension is valid before applying it to the much larger SHARE parent sample where no direct HCAP classification exists.
- **Baselines**: the direct HCAP classification itself (E01) serves as the reference/gold-standard comparison.
- **Dependencies**: E01

## E03: Full-sample prediction and country-level prevalence aggregation
- **Verifies**: C01, C02, C03, C04
- **Setup**:
  - Sample: SHARE parent Wave 9 analytical sample (individuals aged 65+ across 28 SHARE units, excluding those with missing data).
  - Method: apply the regression equation from E02 to predict, for each individual, probabilities of being normal / MCI / demented, using the same demographic, cognition, and health variables as in the validation subsample.
  - Distinguish three respondent groups: those completing cognition items directly, those assessed only via informant proxy report (handled via a separate informant-based rule, not part of this experiment), and those excluded for missing data.
- **Procedure**:
  1. For each individual able to complete the cognition items, compute predicted probabilities of normal/MCI/demented status via the Step-E02 regression equation.
  2. Average individual-level probabilities within each of the 28 SHARE units (countries + Israel) to obtain country-specific prevalence rates and standard errors.
  3. Aggregate across all 28 units to obtain the pooled 28-unit average prevalence.
  4. Compare the resulting cross-national pattern against prior (non-HCAP-validated) European and global estimates.
- **Metrics**: country-level and pooled prevalence (%, with SE) for MCI and dementia; cross-national range and regional grouping.
- **Expected outcome**: A wide cross-national range in prevalence, with the highest rates concentrated in Mediterranean and Southeastern European countries and generally higher levels than reported in prior non-HCAP-validated studies.
- **Baselines**: prior European/global prevalence estimates (EURODEM, EuroCoDe, Alzheimer Europe, OECD, GBD; see `logic/related_work.md`).
- **Dependencies**: E02

## E04: Comparison against the original Langa-Weir (LW) scale
- **Verifies**: C05
- **Setup**:
  - Same SHARE parent Wave 9 analytical sample as E03.
  - Alternate scale: the original Langa-Weir summary score (immediate + delayed word recall [0–20], serial 7s [0–5], backwards counting [0–2]), with dementia defined as score 0–6 and normal as 12–27 (the 7–11 range termed "CIND" by Langa-Weir, compared conceptually to MCI).
- **Procedure**:
  1. Compute the LW summary score for each individual in the SHARE parent Wave 9 sample.
  2. Classify individuals into normal/CIND("MCI")/demented using the fixed LW cutoffs.
  3. Aggregate to country-level and pooled prevalence, alongside the HCAP-validated estimates from E03.
  4. Compare central tendency (average prevalence) and dispersion (coefficient of variation) between the two scales.
- **Metrics**: country-level and pooled LW-based prevalence (%, SE); coefficient of variation of Demented,% across countries, for both scales.
- **Expected outcome**: LW-based prevalence should be generally lower than HCAP-validated prevalence but show relatively larger cross-national dispersion (higher coefficient of variation), attributed to the narrower set of cognitive measures underlying the LW scale.
- **Baselines**: the HCAP-validated estimates from E03 serve as the comparison baseline.
- **Dependencies**: E03

## E05: Group-difference analysis by age, sex, and education
- **Verifies**: C07, C08
- **Setup**:
  - Sample: SHARE parent Wave 9 analytical sample (N=47,193 per Table 3/4), stratified into age bands (65–69 through 90+), sex, and education levels (≤primary school through ≥college degree).
  - Method: pairwise difference-of-means (t-test-style) comparisons between each group and the adjacent group within the same stratification variable, separately for Normal/MCI/Demented prevalence; sex comparisons age-adjusted, education comparisons age- and sex-adjusted.
- **Procedure**:
  1. Compute mean prevalence (with SE) of normal/MCI/demented status within each age band, sex, and education subgroup.
  2. Test each subgroup against its adjacent subgroup (e.g., 70–74y vs 65–69y; Some high school vs ≤Primary school) for statistically significant differences.
  3. Summarize the direction and significance pattern across all three stratifying variables.
- **Metrics**: subgroup prevalence (%, SE); pairwise p-values for each cognitive-status outcome.
- **Expected outcome**: Prevalence of dementia should increase monotonically and significantly with age; MCI prevalence should be higher in women than men (age-adjusted) with no corresponding sex difference in dementia; both MCI and dementia prevalence should decrease monotonically and significantly with increasing education (age- and sex-adjusted).
- **Baselines**: none (internal cross-tabulation of the paper's own estimation results).
- **Dependencies**: E03

## E06: Multivariate regression of dementia probability on comorbidities and lifestyle factors
- **Verifies**: C09, C10
- **Setup**:
  - Sample: SHARE respondents across Waves 1 through 9, linking predicted probability of dementia to self-reported doctor's diagnoses of comorbid conditions (stroke, diabetes, high blood pressure, high blood cholesterol) and lifestyle factors (physical activity, smoking, excessive alcohol use), plus self-rated health and a EURO-D depression score.
  - Method: multivariate regression conditional on age, sex, and education.
- **Procedure**:
  1. Link each individual's estimated probability of being demented (from the E03 pipeline) to self-reported doctor's-diagnosis history across Waves 1–9.
  2. Estimate the association of each comorbidity/lifestyle factor with dementia probability, holding age, sex, and education constant.
  3. Test each association for statistical significance (95% CI excluding zero).
- **Metrics**: percentage-point change in probability of being demented per factor, with 95% confidence interval.
- **Expected outcome**: Stroke, depression, diabetes, smoking, and poorer self-rated health should show statistically significant positive associations with dementia probability; physical activity should show a statistically significant negative (protective) association; high blood pressure, high cholesterol, and excessive alcohol should show no statistically significant association once conditioned on the other factors.
- **Baselines**: none (a single regression specification; no alternative model is compared in the source).
- **Dependencies**: E03

## E07: Education-standardization counterfactual simulation
- **Verifies**: C11
- **Setup**:
  - Sample: SHARE parent Wave 9 analytical sample, same as E03/E05.
  - Method: the same regression-based prediction approach as E03, but replacing each individual's actual education level with the average education level across all 27 European countries and Israel, holding all other covariates at their actual values.
- **Procedure**:
  1. For each individual, recompute the predicted probability of being demented substituting the 28-unit-average education level for their actual education.
  2. Aggregate the counterfactual probabilities to country level, exactly as in E03.
  3. Compare the resulting counterfactual cross-national distribution of dementia prevalence to the actual (E03) distribution.
- **Metrics**: counterfactual country-level dementia prevalence (%); comparison of cross-national range/spread between actual and counterfactual distributions.
- **Expected outcome**: The counterfactual cross-national variation in dementia prevalence should be dramatically smaller than the actual variation, indicating that differences in childhood education levels across countries account for a large share of the observed cross-national variation.
- **Baselines**: the actual (non-counterfactual) country-level prevalence from E03.
- **Dependencies**: E03, E05
