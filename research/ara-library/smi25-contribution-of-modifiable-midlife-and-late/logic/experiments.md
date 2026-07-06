# Experiments and Analyses

> These are declarative reconstructions of analyses described by the abstract, not executable
> scripts. Exact numerical results are intentionally omitted here and kept in `claims.md`.

## E01: Estimate dementia-by-80 attributable fractions by age-window exposure
- **Verifies**: C01
- **Setup**:
  - Cohort: ARIC participants with complete exposure and covariate data.
  - Exposure: Having at least one of hypertension, diabetes, or current smoking at the age-window baseline.
  - Outcome: Incident dementia by age 80 years.
  - Age windows: 45-54 years, 55-64 years, and 65-74 years.
  - Model/covariates: Not available from provided input.
- **Procedure**:
  1. Set baseline by age at vascular risk factor measurement.
  2. Classify participants by presence of at least one vascular risk factor.
  3. Estimate population attributable fractions for incident dementia by age 80 for each age window.
- **Metrics**: Population attributable fraction and confidence interval.
- **Expected outcome**: Attributable fractions show a sizeable contribution by age 80 and differ by age at measurement.
- **Baselines**: No vascular risk factor group or counterfactual no-exposure scenario; details not available from provided input.
- **Dependencies**: none

## E02: Characterize age-window analytic samples and dementia case counts
- **Verifies**: C02
- **Setup**:
  - Cohort: ARIC participants contributing to each age-window analysis.
  - Outcome: Incident dementia by age 80 years.
  - Demographics: Sex and self-reported race are reported in aggregate in the abstract.
  - Inclusion criteria: Complete exposure and covariate data; further details not available from provided input.
- **Procedure**:
  1. Count eligible participants in each age-window analysis.
  2. Summarize sex and race composition for each analytic sample.
  3. Count dementia cases by age 80 in each analytic sample.
- **Metrics**: Participant count, demographic composition, dementia case count.
- **Expected outcome**: The three age-window analyses have different denominators and case counts.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E03: Estimate subgroup-specific attributable fractions
- **Verifies**: C03
- **Setup**:
  - Cohort: ARIC age-window analytic samples.
  - Exposure: At least one vascular risk factor.
  - Outcome: Incident dementia by age 80 years.
  - Subgroups: APOE e4 genotype, self-reported race, and sex.
  - Interaction or stratification model: Not available from provided input.
- **Procedure**:
  1. Stratify or otherwise compare attributable fractions by APOE e4 carrier status, race, and sex.
  2. Estimate subgroup-specific population attributable fractions by relevant age windows.
  3. Compare subgroup ranges directionally.
- **Metrics**: Subgroup-specific population attributable fraction ranges.
- **Expected outcome**: Higher attributable fractions are observed in the subgroup categories named in the abstract.
- **Baselines**: Complementary subgroup categories; exact comparator details not available from provided input.
- **Dependencies**: E01

## E04: Estimate attributable fractions for dementia after age 80
- **Verifies**: C04
- **Setup**:
  - Cohort: ARIC participants contributing follow-up after age 80.
  - Exposure: At least one vascular risk factor by age at measurement.
  - Outcome: Incident dementia after age 80 years.
  - Model/covariates: Not available from provided input.
- **Procedure**:
  1. Separate dementia events occurring after age 80 from events by age 80.
  2. Estimate post-80 population attributable fractions for the vascular risk-factor grouping.
  3. Compare post-80 results directionally with by-age-80 estimates.
- **Metrics**: Population attributable fraction range after age 80.
- **Expected outcome**: Post-80 attributable fractions are much smaller than by-age-80 attributable fractions.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01
