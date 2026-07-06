# Concepts

## Health disparity (as a rate ratio, r_obs)
- **Notation**: `r_obs = RR`; by construction `r_obs > 1`
- **Definition**: The AD-risk difference between two subpopulations, measured as the ratio of AD rates (hazard ratio of the disparity indicator `r`). The first subpopulation in a pair is always the higher-risk one, so the observed disparity is numerically ≥ 1. Six disparities are studied: Black–White (BW), White–Native American (WN), Hispanic–White (HW), White–Asian (WA), female–male (FM), and stroke-belt vs non–stroke-belt states (SB).
- **Boundary conditions**: Defined for a subpopulation pair sharing a common baseline hazard `h_0(t)`; approximated by the univariable Cox hazard ratio of the disparity indicator (Table 4, footnote a).
- **Related concepts**: Unexplained disparity, Exposure effect, Vulnerability effect

## Unexplained disparity (R_r)
- **Notation**: `R_r = exp(β_r)`
- **Definition**: The residual part of a disparity not accounted for by the modeled predictors — the disparity-indicator effect that remains in the multivariable Cox model after including all predictors. In the decomposition `r_obs = r_unex · Π_i E_i V_i`, `r_unex = R_r`.
- **Boundary conditions**: `r_unex < r_unob` (unexplained below observed) indicates the predictors genuinely explain part of the disparity; `r_unex > r_unob` indicates the predictors inflate the apparent disparity (observed in WN and WA).
- **Related concepts**: Health disparity, Exposure effect, Vulnerability effect

## Population attributable fraction (PAF) for a subpopulation
- **Notation**: `PAF_0i`, `PAF_1i`
- **Definition**: The fraction of AD risk in a subpopulation attributable to predictor `i`, defined per subpopulation as `PAF_0i = P_0i(R_0i − 1) / [P_0i(R_0i − 1) + 1]` and `PAF_1i = P_1i(R_1i − 1) / [P_1i(R_1i − 1) + 1]`, where `P` is predictor prevalence and `R` the relative risk (`R_0i = exp(β_0i)`, `R_1i = exp(β_1i)`) in the advantaged (0) and disadvantaged (1) subpopulations (Eq. 3).
- **Boundary conditions**: Requires estimated relative risks and prevalences; here extended from single-population PAF to a disparity context.
- **Related concepts**: Exposure effect, Vulnerability effect, Relative risk

## Exposure effect (E_i)
- **Notation**: `E_i = [ (1 + P_1i(R_0i − 1))/(1 + P_0i(R_0i − 1)) · (1 + P_1i(R_1i − 1))/(1 + P_0i(R_1i − 1)) ]^{1/2}`
- **Definition**: The part of predictor `i`'s contribution to a disparity that arises from a higher **prevalence** (`P_1i` vs `P_0i`) of the predictor in one subpopulation, holding per-exposure risk fixed. One of the two multiplicative factors of `f_i` (`f_i = E_i·V_i`, Eq. 6).
- **Boundary conditions**: Isolated from vulnerability only under the averaging/decomposition of Eq. 5–6; dominates the low-income contribution.
- **Related concepts**: Vulnerability effect, PAF, Health disparity

## Vulnerability effect (V_i)
- **Notation**: `V_i = [ (1 + P_1i(R_1i − 1))/(1 + P_1i(R_0i − 1)) · (1 + P_0i(R_1i − 1))/(1 + P_0i(R_0i − 1)) ]^{1/2}`
- **Definition**: The part of predictor `i`'s contribution to a disparity that arises from a higher **risk** (`R_1i` vs `R_0i`) associated with the predictor in one subpopulation, holding prevalence fixed. The second multiplicative factor of `f_i`.
- **Boundary conditions**: Dominates the disease-predictor contributions, especially arterial hypertension and heart failure.
- **Related concepts**: Exposure effect, PAF, Relative risk

## Base Cox proportional-hazards model with disparity indicator
- **Notation**: `h(t, r, x) = h_0(t) exp(β_r r + Σ_i β_0i x_i + Σ_i β_1i r x_i)` (Eq. 1)
- **Definition**: The multivariable Cox model over survival time `t` (time after cohort baseline age), disparity indicator `r ∈ {0,1}`, and binary predictors `x_i`, with a main effect `β_r`, predictor main effects `β_0i`, and disparity×predictor interactions such that `β_1i = β_0i + β_i`. Setting `r = 0/1` yields the two subpopulation-specific hazards (Eq. 2).
- **Boundary conditions**: Proportional-hazards assumption; binary time-independent predictors; shared `h_0(t)`.
- **Related concepts**: Unexplained disparity, PAF, Exposure/Vulnerability effect

## Dual eligibility (Medicare/Medicaid) as low-income indicator
- **Notation**: —
- **Definition**: Simultaneous enrollment in Medicare and Medicaid, used as the binary indicator of low income / low socioeconomic status. It is the single non-disease predictor in the analysis.
- **Boundary conditions**: A proxy for socioeconomic status; measured at baseline (refs 13–16).
- **Related concepts**: Exposure effect, Health disparity

## Stroke belt
- **Notation**: SB
- **Definition**: A group of US states with historically elevated stroke mortality; the SB disparity compares residents of stroke-belt states against residents of states without a common border with the stroke belt (ref 12).
- **Boundary conditions**: Geographic disparity defined at the state-group level; rurality not addressed (§4 limitations).
- **Related concepts**: Health disparity, Cerebrovascular disease

## AD onset ascertainment
- **Notation**: —
- **Definition**: Algorithmic construction of the AD-onset outcome from Medicare claims using a previously published ascertainment algorithm (ref 18), with a confirmation period; the base analysis uses death as independent censoring and a 5-year follow-up.
- **Boundary conditions**: Sensitivity analyses vary the confirmation period (180-day, none) and the outcome (ADRD vs AD).
- **Related concepts**: Sensitivity analysis, Relative risk
