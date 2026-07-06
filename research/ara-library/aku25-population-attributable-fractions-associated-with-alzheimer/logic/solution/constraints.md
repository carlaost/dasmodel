# Constraints — Boundary Conditions, Assumptions, Limitations

> Derived from the conference abstract (`paper.pdf`, pp. 743–744). The source is an abstract with no
> methods section, so most quantitative and procedural boundaries are undocumented and are marked
> "Not specified in the published abstract" rather than guessed.

## Boundary conditions

- **Population**: Older adults in the U.S. Medicare program, represented by a 5% sample of CMS
  administrative claims/enrollment data. Findings apply to Medicare-enrolled older adults, not
  necessarily to non-Medicare or younger populations.
- **Outcome scope**: A *clinical diagnosis* of AD/ADRD recorded in Medicare claims — not
  biomarker- or autopsy-confirmed disease. Undiagnosed or miscoded dementia is outside scope.
- **Predictor scope**: Nine comorbid diseases (heart failure, hypertension, arrhythmia, stroke,
  hypotension, renal disease, depression, traumatic brain injury, diabetes mellitus) plus a
  low-income indicator (dual Medicare eligibility). Risk factors outside this set (genetic, lifestyle,
  environmental) are not modeled.
- **Stratification scope**: Results are reported for the general older-adult population and for
  sex (male/female) and race groups (Black, Asian, Hispanic, White, Native American). The exact
  race/ethnicity categorization scheme is Not specified in the published abstract.

## Assumptions

- **A1 — Outcome validity**: A claims-recorded clinical AD/ADRD diagnosis is a valid event for
  Cox survival modeling.
- **A2 — Low-income proxy**: Dual Medicare/Medicaid eligibility validly indicates low income.
- **A3 — Proportional hazards**: The Cox proportional-hazards assumption holds for the retained
  predictors (not tested/reported in the abstract).
- **A4 — PAF interpretation**: The PAF estimates carry the standard PAF assumptions — correct model
  specification, exposure prevalence estimated from the same population, and a causal/attributable
  reading of the modeled disease→AD/ADRD associations. These assumptions are contestable and are the
  chief interpretive limitation of any PAF.
- **A5 — Representativeness**: The 5% Medicare sample is representative of the target older-adult
  Medicare population for the estimated quantities.

## Known limitations

- **L1 — Abstract-only documentation**: No confidence intervals, standard errors, sample sizes,
  hazard ratios, follow-up windows, calendar years, ICD code definitions, PAF estimator/formula, or
  predictor-selection criterion are reported. Reproducibility from the published item alone is not
  possible; the underlying data are controlled-access (CMS/ResDAC).
- **L2 — Approximate values**: Several headline figures are stated as ranges or approximations
  ("45-50%", ">30%", "approximately 30%", "exceeding 5%", "exceeding 3%"). Downstream use must
  preserve this imprecision (see the `≈`/range wording carried in `logic/claims.md`).
- **L3 — Confounding and causality**: Attributable-fraction language implies preventable burden, but
  residual confounding, reverse causation (e.g., prodromal dementia driving comorbidity diagnosis),
  and diagnostic/ascertainment bias in claims data are not addressed in the abstract and would bias
  PAF estimates.
- **L4 — Competing risk of death**: Older-adult cohorts have high mortality; whether competing risk
  of death was accounted for in the survival/PAF analysis is Not specified in the published abstract.
- **L5 — Subpopulation power / categorization**: Small subpopulations (e.g., Native American,
  Asian) may yield unstable PAF estimates; subgroup sample sizes are not reported.
- **L6 — Dual-eligibility in the final model**: The abstract lists nine *diseases* as the identified
  model but frames low income (dual eligibility) as part of the assessed joint impact; whether
  dual eligibility was retained as a predictor in the final model is Not specified in the published
  abstract.
