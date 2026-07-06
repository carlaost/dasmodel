# Method: PAF-based decomposition of health disparities in a Cox model

The method extends the population attributable fraction (PAF) to disparities within a Cox
proportional-hazards model, expressing an observed disparity as an unexplained part times a
product of per-predictor factors, each of which splits exactly into an **exposure** and a
**vulnerability** effect. Source: §2 Methods, Eqs. 1–6.

## Mathematical formulation

**Base model (Eq. 1)** — Cox model over time `t` (time after cohort baseline age), disparity
indicator `r`, and binary predictors `x_i`:

```
h(t, r, x) = h_0(t) · exp( β_r·r + Σ_i β_0i·x_i + Σ_i β_1i·r·x_i )
```

`r = 1` marks the higher-risk subpopulation of the pair; `i` enumerates predictors; `x` is the
predictor vector.

**Subpopulation-specific hazards (Eq. 2)** — set `r = 1` (disadvantaged) and `r = 0` (advantaged):

```
h(t, 1, x) = h_0(t) · R_r · Π_i R_1i^{x_i}
h(t, 0, x) = h_0(t) ·       Π_i R_0i^{x_i}
```

with relative risks `R_r = exp(β_r)`, `R_0i = exp(β_0i)`, `R_1i = exp(β_1i)`, and
`β_1i = β_0i + β_i`. The baseline hazard `h_0(t)` is common to both subpopulations, so it cancels
when the ratio of the two hazards is taken — no baseline-hazard assumption is needed.

**Per-subpopulation PAF (Eq. 3)**:

```
PAF_0i = P_0i·(R_0i − 1) / [ P_0i·(R_0i − 1) + 1 ]
PAF_1i = P_1i·(R_1i − 1) / [ P_1i·(R_1i − 1) + 1 ]
```

where `P_0i`, `P_1i` are baseline prevalences of predictor `i` in the advantaged and disadvantaged
subpopulations.

**Averaged hazards (Eq. 4)** — averaging Eq. 2 over the individuals of each subpopulation:

```
h̄(t, 1, x) = R_r · h_0(t) / Π_i (1 − PAF_1i)
h̄(t, 0, x) =        h_0(t) / Π_i (1 − PAF_0i)
```

**Two-predictor averaging illustration (Eq. 5)** — for predictors a, b the four prevalence groups
(11, 10, 01, 00) have approximate prevalences `P_a·P_b`, `P_a(1−P_b)`, `(1−P_a)P_b`,
`(1−P_a)(1−P_b)` under negligible a–b correlation; averaging gives
`h̄(t,1,x) = R_r·h_0(t) / [ (1 − PAF_1a)(1 − PAF_1b) ]`.

**Observed risk ratio and decomposition (Eq. 6)**:

```
RR = R_r · Π_i f_i ,   f_i = (1 − PAF_0i)/(1 − PAF_1i)
                          = [ 1 + P_1i(R_1i − 1) ] / [ 1 + P_0i(R_0i − 1) ]
                          = E_i · V_i

E_i = { [1 + P_1i(R_0i − 1)] / [1 + P_0i(R_0i − 1)] · [1 + P_1i(R_1i − 1)] / [1 + P_0i(R_1i − 1)] }^{1/2}

V_i = { [1 + P_1i(R_1i − 1)] / [1 + P_1i(R_0i − 1)] · [1 + P_0i(R_1i − 1)] / [1 + P_0i(R_0i − 1)] }^{1/2}
```

Each factor `f_i` is thus decomposed into two contributions: the **exposure effect** `E_i` (arising
from differences in predictor prevalence `P_1i` vs `P_0i`) and the **vulnerability effect** `V_i`
(arising from differences in per-exposure risk `R_1i` vs `R_0i`). The decomposition is exact and
requires no methodological assumptions beyond those inherent to Cox modeling.

## Reading the decomposition
- `RR` (observed disparity) is approximated by the univariable hazard ratio of the disparity
  indicator (Table 4 footnote a).
- `R_r` (unexplained disparity) is the multivariable disparity-indicator effect `exp(β_r)`.
- `r_obs = r_unex · Π_i E_i V_i`. When `r_unex < r_unob` the predictors explain part of the
  disparity; when `r_unex > r_unob` they inflate the apparent disparity.

## Analysis pipeline (§2–3)
1. Univariable Cox model per disparity → observed disparity (hazard ratio of the indicator).
2. Multivariable Cox model with low income + candidate diseases → `R_r`, `R_0i`, `R_1i`.
3. First-stage screening: drop the four candidate conditions with no significant contribution
   across all cohorts (rheumatic heart disease, systemic hypotension, chronic liver disease,
   traumatic brain injury), retaining six diseases + low income.
4. Compute `f_i`, `E_i`, `V_i` per predictor, cohort, and disparity (Table 4).
5. Bootstrap (100 resamples) for standard errors, confidence intervals, and significance.
6. Sensitivity analyses over AD-onset ascertainment and ADRD outcome.

## Complexity
Not specified in paper. The paper states the method is "straightforward to implement: once the Cox
model and predictor prevalences are estimated, exposure and vulnerability effects can be derived
using explicit expressions" (§4).
