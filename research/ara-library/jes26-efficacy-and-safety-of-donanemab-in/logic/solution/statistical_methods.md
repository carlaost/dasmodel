# Statistical Methods

All estimands are described directionally here; exact estimates are in `evidence/`. All analyses
are post-hoc, exploratory, and not controlled for multiplicity.

## Clinical-scale MMRM
- Mixed model for repeated measures assessing all clinical outcomes in the EU-indicated, EU-eligible, and low-medium-tau-indicated populations.
- **Factors**: treatment, visit, baseline tau category, pooled investigator, concomitant symptomatic treatment (acetylcholinesterase inhibitors and/or memantine).
- **Covariates**: baseline age, baseline score.
- **Interactions**: treatment-by-visit, baseline-score-by-visit.
- **CIs**: normal approximation method.

## Conservative hybrid imputation (EMA-required)
- Applied to change-from-baseline differences on clinical scales (and to amyloid CFB per Table 3).
- **Jump-to-reference (J2R)**: replaces a missing value with the reference (placebo) cohort value at that timepoint. Used for missingness due to serious, severe, or symptomatic ARIA (ARIA-E or ARIA-H) or death.
- **Copy increment reference (CIR)**: replaces a missing value with a value estimated to reflect observed change-over-time trends in the reference arm. Used for all other missing causes.
- Because both are reference-derived, they minimise treatment-effect differences and are more conservative than the original methodology (no imputation).
- **Original methodology (comparator, Table 2)**: no formal imputation; adjusted mean CFB, SE, 95% CI, p values via an NCS model with 2 degrees of freedom (basis expansion terms, term-by-treatment interaction, covariates age, pooled investigator, baseline tau category, baseline AChEI/memantine use).

## Percent slowing
- Adjusted mean CFB treatment difference at 76 weeks ÷ adjusted mean CFB with placebo at 76 weeks × 100; 95% CIs via the Delta method.

## Progression risk — Cox proportional hazards (CDR-G)
- Next-stage progression: any increase in CDR-G at two consecutive visits from baseline. Progression to moderate/severe: CDR-G ≥2 at two consecutive visits (baseline CDR-G ≤1).
- Cox model stratified by pooled investigator and baseline tau level; covariates age, AChEI/memantine use, baseline clinical outcome score.
- For the next-stage analysis, discontinuations due to death and ARIA are counted as events; that analysis included participants with missing APOE ε4 genotype data.

## Disease stabilisation — generalized mixed model
- "No progression" = CDR-SB CFB ≤0. Generalized mixed model with factors treatment, visit, treatment-by-visit interaction; covariates age, tau category, AChEI/memantine use, baseline clinical outcome score, and score-by-visit interaction. Estimated proportions with 95% CIs and p values at 52/76 weeks.

## Time saved — time-progression model for repeated measures
- Estimates the difference in time for the placebo arm to reach the same CDR-SB change observed in the donanemab arm at end of the placebo-controlled period (as in Sims et al. [2]).

## Biomarker analyses
- Amyloid PET Centiloid CFB via MMRM (treatment, visit, treatment-by-visit; covariates score, score-by-visit, age, tau category). Amyloid clearance defined as <24.1 CL; clearance percentages with Wilson score CIs; a one-sample frequency test evaluated whether percent amyloid-negative equals 0. Plasma P-tau217 analysed (log10-based) at all timepoints.

## LTE analyses
- Propensity score weighting balances TRAILBLAZER-ALZ 2 arm baseline characteristics against the ADNI external control (per Zimmer et al. [7]). Simultaneous propensity reweighting + J2R/CIR multiple imputation is not methodologically possible → no hybrid imputation applied in the LTE.

## Software
- SAS version 9.4 for most analyses; R version 4.3.0 for some time-based progression analyses.
- TEAEs coded with the Medical Dictionary for Adverse Events (MedDRA) version 25.1.
