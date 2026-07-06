# Constraints, Assumptions, and Limitations

## Boundary conditions
- Applies to a **subpopulation pair** sharing a common baseline hazard `h_0(t)`; the disparity is a
  ratio in which `h_0(t)` cancels.
- Predictors are **binary and time-independent**, measured at baseline.
- Outcome is **AD onset within a 5-year follow-up**, with death as independent censoring.
- Cohorts fixed at baseline ages 70, 75, 80, 85; analysis restricted to fee-for-service Medicare
  beneficiaries (>20% Medicare Advantage time excluded).

## Assumptions
- **A1**: Cox proportional-hazards assumption for the base model (Eq. 1).
- **A2**: Correlations among predictors are minimized/negligible — an explicit "initial
  simplification." The four-group prevalence approximation (Eq. 5) assumes negligible correlation
  between conditions; the paper notes this "is not strictly fundamental," and Eqs. 5–6 admit
  corrections proportional to correlation coefficients that make the assumption less critical. It is
  "sufficient if one merely wishes to characterize statistical associations."
- **A3**: Death acts as an independent censoring mechanism.
- **A4 (for causal reading only)**: Causal interpretation of the decomposition requires the standard
  causal-mediation assumptions — (i) no confounding of mediator(s) and outcome; (ii) sequential
  ignorability / non-parametric identifiability (the treatment is ignorable given pre-treatment
  covariates, and the mediator is ignorable given observed treatment and pre-treatment covariates);
  (iii) when more than one mediator is examined, assumptions about their causal ordering /
  interdependence. Absent these, results are statistical associations, not causal effects.

## Known limitations (§4)
- **Administrative-data outcome construction**: the AD outcome is built from a disease-onset
  ascertainment algorithm (ref 18); addressed via sensitivity analyses but not eliminated.
- **Predictor set is limited**; statistical power for **Native Americans** should be improved (small
  counts, e.g., 85 AD cases at age 70 — Table 1).
- **Fee-for-service only**: only traditional Medicare fee-for-service beneficiaries were analyzed;
  comparison with Medicare Advantage beneficiaries is deferred to other work (refs 41–43).
- **Rurality not addressed**: geographic disparities are kept at the state-group level; within-state
  rural/urban variation is not modeled.
- **Depression underdiagnosis** among the Black subpopulation may bias the depression PAF (refs
  38–40) and should be kept in mind when interpreting depression contributions.
- **Correlation among predictors** left as an initial simplification (A2); full correction not
  applied in this implementation.
