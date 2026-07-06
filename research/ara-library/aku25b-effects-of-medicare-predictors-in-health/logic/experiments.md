# Experiments

## E01: Derive and verify the PAF-based disparity decomposition
- **Verifies**: C01
- **Setup**:
  - Method: Cox proportional-hazards model with disparity indicator and binary predictors (Eq. 1)
  - Data: analytical derivation (no data required for the identity itself)
  - System: define subpopulation-specific hazards (Eq. 2), per-subpopulation PAFs (Eq. 3), average hazards over each subpopulation (Eq. 4–5), and express the observed risk ratio in terms of predictor factors (Eq. 6)
- **Procedure**:
  1. Write the base Cox model with main, predictor, and interaction terms.
  2. Set the disparity indicator to 0 and 1 to obtain the two subpopulation hazards.
  3. Define per-subpopulation PAFs from prevalences and relative risks.
  4. Average each hazard over its subpopulation and take the ratio; confirm the shared baseline hazard cancels.
  5. Show the risk ratio factorizes as `R_r · Π_i f_i` and each `f_i` splits multiplicatively into exposure and vulnerability factors.
- **Metrics**: algebraic identity `f_i = E_i · V_i`; reconstruction of the modeled `RR` from the factors
- **Expected outcome**:
  - The observed risk ratio decomposes exactly into an unexplained part and a product of per-predictor factors, each factoring into exposure and vulnerability, with no baseline-hazard assumption.
- **Baselines**: sequence-of-Cox-models "explanation"; Oaxaca–Blinder / Yun–Powers hazard-rate decomposition; rank-and-replace; conditional decomposition
- **Dependencies**: none

## E02: Estimate predictor prevalences and multivariable hazard ratios in Medicare cohorts
- **Verifies**: C02, C03, C04
- **Setup**:
  - Data: nationally representative 5% sample of US Medicare claims, 1991–2020; four baseline-age cohorts (70, 75, 80, 85); 5-year follow-up
  - Predictors: dual eligibility (low income) plus retained disease predictors (cerebrovascular disease, arterial hypertension, diabetes mellitus, renal disease, heart failure, depression), measured binary at baseline via ascertainment algorithms
  - Outcome: AD onset with death as independent censoring
  - Exclusions: baseline AD/ADRD claims; >20% of study time in Medicare Advantage
- **Procedure**:
  1. Form the four age cohorts and apply exclusion criteria.
  2. Measure baseline prevalence of each predictor per subpopulation.
  3. First-stage screening: drop predictors with no significant disparity contribution across all cohorts.
  4. Fit univariable and multivariable Cox models for each disparity and predictor.
  5. Tabulate subpopulation-specific hazard ratios.
- **Metrics**: baseline prevalence (%) per subpopulation; AD hazard ratios per predictor and subpopulation
- **Expected outcome**:
  - Low-income prevalence is markedly higher in non-White subpopulations; disease predictors show elevated hazard ratios; depression carries the largest per-predictor hazard ratios; four screened conditions contribute negligibly and are excluded.
- **Baselines**: comparison across age cohorts and subpopulations
- **Dependencies**: E01

## E03: Decompose each disparity into exposure and vulnerability contributions by predictor
- **Verifies**: C01, C02, C03, C05, C06
- **Setup**:
  - Inputs: estimated Cox relative risks and baseline prevalences from E02
  - Scope: six disparities × four age cohorts × retained predictors
- **Procedure**:
  1. Compute per-predictor total factors `f_i` and split each into exposure `E_i` and vulnerability `V_i`.
  2. Compute the observed and unexplained disparity for each pair and cohort.
  3. Compare observed vs unexplained to classify each disparity (predictors explain / over-explain / inflate).
  4. Rank predictors by contribution within each disparity; identify the dominant channel (exposure vs vulnerability) for each.
  5. Plot the observed disparity, the unexplained part, and the low-income-adjusted curve across age.
- **Metrics**: total, exposure, and vulnerability factors per predictor; observed vs unexplained disparity; age trends
- **Expected outcome**:
  - Low income contributes mainly through exposure; hypertension mainly through vulnerability; predictors explain part of Black–White and (more than fully) Hispanic–White disparities, but inflate White–Native American and White–Asian; female–male and stroke-belt disparities are less influenced by the examined predictors.
- **Baselines**: within-study cross-disparity comparison; qualitative agreement with a Blinder–Oaxaca analysis of Black–White disparities (ref 21)
- **Dependencies**: E01, E02

## E04: Bootstrap the significance of exposure and vulnerability effects
- **Verifies**: C07
- **Setup**:
  - Method: bootstrap resampling with replacement of the original sample (100 resamples)
  - Scope: all evaluated exposure and vulnerability effects across disparities
- **Procedure**:
  1. Draw 100 bootstrap resamples with replacement.
  2. Re-estimate the Cox model and decomposition on each resample.
  3. Compute standard errors and confidence intervals for each exposure/vulnerability effect.
  4. Count the fraction of significant effects overall and per disparity, separately for exposure and vulnerability.
- **Metrics**: fraction of significant effects (overall and per disparity); standard errors; confidence intervals
- **Expected outcome**:
  - A majority of effects are significant; exposure effects are significant more often than vulnerability effects for most disparities.
- **Baselines**: none
- **Dependencies**: E03

## E05: Sensitivity of the decomposition to outcome ascertainment
- **Verifies**: C08
- **Setup**:
  - Base scheme vs three alternatives: 180-day confirmation period; no confirmation period; ADRD instead of AD as outcome
  - Data: same Medicare cohorts as E02
- **Procedure**:
  1. Re-run AD-onset ascertainment under each alternative scheme.
  2. Re-estimate the Cox model and decomposition.
  3. Compare exposure/vulnerability contributions against the base scheme.
- **Metrics**: differences in exposure and vulnerability contributions relative to the base scheme
- **Expected outcome**:
  - Confirmation-period changes produce negligible differences; using ADRD raises the exposure component and lowers the vulnerability component; overall rankings are stable.
- **Baselines**: base AD-onset ascertainment scheme (ref 18)
- **Dependencies**: E03
