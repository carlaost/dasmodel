# Constraints, Assumptions, and Limitations

> Grounding: abstract-only. This file records what the provided source supports and what it does not.

## Boundary Conditions

- Disease scope: Alzheimer's disease and other dementias.
- Data source: Global Burden of Disease database.
- Retrospective analysis window: 1990 to 2021.
- Forecast horizon: through 2040.
- Burden metrics: incidence, prevalence, and DALYs.
- Geographic scope: global, regional, and national, with East Asia named in the abstract.
- Stratification dimensions named in the abstract: age, gender, SDI quintile, region.

## Assumptions

- The abstract accurately summarizes full-paper analyses and results.
- The GBD database is the sole data source described in the provided input.
- Joinpoint, age-period-cohort, DALY decomposition, and Bayesian age-period-cohort forecasting are separate analysis components unless the full text states otherwise.

## Known Limitations From Provided Input

- Full text: Not available from provided input.
- Tables and figures: Not available from provided input.
- Exact GBD release/version and extraction settings: Not available from provided input.
- Software packages, versions, random seeds, and code: Not available from provided input.
- Joinpoint model settings, annual percentage changes, confidence intervals, and metric-specific change points: Not available from provided input.
- APC model formula, priors, identifiability constraints, age/period/cohort bins, and posterior diagnostics: Not available from provided input.
- Forecast uncertainty intervals: Not available from provided input.
- Exact national rankings and full regional values: Not available from provided input.
- Intervention effects or tested public-health policies: Not available from provided input.

## Practical Implication

The artifact can support high-level reasoning about the study's reported findings and analysis structure, but it cannot reproduce the analyses or audit numerical tables without the full text, GBD extraction details, and analysis code.
