# Problem Specification

## Observations

### O1: AD/ADRD disparities persist across race/ethnicity, sex, and geography
- **Statement**: Observed AD hazard-ratio disparities at baseline age 70 are 1.65 (Black–White), 1.26 (White–Native American), 1.21 (Hispanic–White), 1.40 (White–Asian), 1.24 (female–male), and 1.58 (stroke-belt vs non–stroke-belt states); all `>1` by construction (the higher-risk subpopulation is placed first in each pair).
- **Evidence**: Table 4 (observed disparity rows); §1 Introduction; refs 5–10.
- **Implication**: Disparities are large and heterogeneous in mechanism, motivating a decomposition that attributes them to specific, actionable predictors.

### O2: Low-income (dual-eligibility) prevalence is far higher in non-White subpopulations
- **Statement**: At baseline age 70, Medicare/Medicaid dual-eligibility prevalence is 7.9% (White) vs 24.8% (Black), 29.0% (Native American), 50.9% (Hispanic), and 44.1% (Asian).
- **Evidence**: Table 2 (Low income/dual eligibility rows).
- **Implication**: A large exposure differential exists for low income — a difference in predictor *prevalence* between subpopulations, distinct from any difference in *risk per exposed individual*.

### O3: Some predictors differ in disparity mechanism (prevalence vs risk)
- **Statement**: Hypertension prevalence is higher in Black (65.0%) than White (53.0%) at age 70 (Table 2), yet in the decomposition the Black–White hypertension effect is carried almost entirely by vulnerability (e.g., age 75 `1.16 = 1.01 * 1.14`), with exposure ≈ 1.00 (Table 4).
- **Evidence**: Table 2, Table 4.
- **Implication**: Prevalence differences (exposure) and per-exposure risk differences (vulnerability) are distinct pathways that a disparity-explaining method must separate.

### O4: Conventional methods conflate or cannot capture both pathways
- **Statement**: A predictor is conventionally said to "explain" a disparity if the disparity-group coefficient shrinks when the predictor is added to a Cox model; but estimating separate Cox models with different predictor sets makes unobserved baseline-hazard differences produce hazard ratios that "do not reflect true differences in rates," results depend on the order predictors are added, and such methods capture only vulnerability (parameter differences), missing exposure (prevalence) effects.
- **Evidence**: §1 Introduction (final two paragraphs, p. 2).
- **Implication**: A new estimator is needed that is order-independent, cancels the baseline hazard, and yields both exposure and vulnerability contributions.

## Gaps

### G1: No quantitative attribution of AD/ADRD disparities to specific predictors
- **Statement**: "limited quantitative information exists to explain how specific predictors contribute to these disparities" (Abstract).
- **Caused by**: O1, O4.
- **Existing attempts**: sequence-of-Cox-models "explanation"; rank-and-replace approaches; Oaxaca–Blinder / Yun–Powers hazard-rate decomposition; Pollard decomposition; conditional decomposition; parametric g-formula.
- **Why they fail**: order-dependence; restrictive technical assumptions; capture only the vulnerability (parameter) channel; unobserved baseline-hazard differences distort hazard ratios (O4).

### G2: Exposure and vulnerability effects are not jointly estimable without restrictive assumptions
- **Statement**: Disparities can be generated both by higher predictor prevalence (exposure) and higher per-exposure risk (vulnerability), but "there are no simple and standard empirical or regression-based approaches" to identify and quantify both pathways without introducing notable methodological and evaluation-related biases.
- **Caused by**: O3, O4.
- **Existing attempts**: traditional Cox-parameter comparisons (vulnerability only).
- **Why they fail**: they capture only differences in model parameters (vulnerability), not differences in risk-factor prevalence (exposure), "which cannot be captured by such methods but should be accounted for in intervention planning."

## Key Insight
- **Insight**: Extend the notion of population attributable fraction (PAF) to disparities inside a Cox proportional-hazards model. Averaging the subpopulation-specific hazards over each subpopulation expresses the observed risk ratio as `RR = R_r · Π_i f_i` with `f_i = (1 − PAF_0i)/(1 − PAF_1i)`, and each factor decomposes **exactly and multiplicatively** into an exposure effect `E_i` and a vulnerability effect `V_i` (`f_i = E_i · V_i`). Because the ratio is taken, the shared baseline hazard `h_0(t)` cancels — no assumptions about baseline hazards are needed.
- **Derived from**: O2, O3, O4.
- **Enables**: order-independent attribution of each predictor's contribution to a disparity, split into exposure (prevalence) and vulnerability (per-exposure risk) channels, computed from the estimated Cox parameters and predictor prevalences alone.

## Assumptions
- A1: Predictors are binary and time-independent, measured at baseline (§2).
- A2: The disparity indicator `r` and the shared baseline hazard `h_0(t)` are common to both subpopulations of a pair (Eq. 1–2); the ratio construction cancels `h_0(t)`.
- A3: Correlations among predictors are minimized/negligible (an "initial simplification"; the four-group prevalence approximation in Eq. 5 assumes negligible correlation between conditions a and b). Subsequent corrections in Eq. 5–6 can relax this.
- A4: Death is treated as independent censoring; individuals with baseline AD/ADRD claims, or >20% of study time in Medicare Advantage, are excluded (§2).
- A5: Causal interpretation of the decomposition would additionally require the standard causal-mediation assumptions (no confounding of mediator–outcome, sequential ignorability, mediator ordering); the study frames its results as statistical associations unless these hold (§4).
