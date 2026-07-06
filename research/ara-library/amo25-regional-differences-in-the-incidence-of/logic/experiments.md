# Experiments (Analyses)

Declarative analysis plans. Directional only — exact numbers live in `evidence/`. "Experiment" here means an epidemiological estimation/statistical-test procedure.

## E01: Estimate crude ADRD incidence per 100,000 by county and PHR
- **Verifies**: C01
- **Setup**:
  - Data (numerator): SCADR 2021 incident ADRD cases (new cases; year of diagnosis = 2021), N = 18,955 after restricting to ages 50–110.
  - Data (denominator): Annual County Resident Population Estimates (ACRPE), based on the 2020 census / Vintage 2020 estimates.
  - Unit of analysis: county and public health region (PHR = Low Country, Midlands, Pee Dee, Upstate).
  - Tools: Microsoft Excel; SAS 9.4.
- **Procedure**:
  1. Count new 2021 ADRD cases per county and per PHR.
  2. Divide by the corresponding population at risk; scale to per-100,000.
  3. Aggregate counties into PHRs; produce overall regional crude incidence.
  4. Visualize county- and PHR-level crude incidence as choropleths (QGIS 3.34.13-Prizren, TIGER/Line files).
- **Metrics**: crude incidence per 100,000 population (by county, by PHR).
- **Expected outcome**: Crude ADRD incidence is highest in Pee Dee and lowest in Midlands; counties in the Pee Dee fall in the top incidence class.
- **Baselines**: comparison across the four PHRs (no external baseline).
- **Dependencies**: none

## E02: Poisson regression comparing crude incidence across PHRs (pairwise IRRs)
- **Verifies**: C01
- **Setup**:
  - Model: Poisson regression, log-link, dependent = age-adjusted new-case count by PHR; PHR as fixed effect.
  - Offset: natural logarithm of the population at risk (to model rates, not raw counts, across differently sized PHRs).
  - Post-hoc: Tukey-adjusted pairwise comparisons; Type 3 likelihood-ratio test for overall PHR significance.
  - Software: SAS 9.4.
- **Procedure**:
  1. Fit the offset Poisson model with PHR as predictor.
  2. Exponentiate coefficients (β) to incidence rate ratios (IRRs).
  3. Report IRRs with p-values and 95% CIs for all pairwise PHR comparisons.
  4. Assess overall PHR effect via the Type 3 likelihood ratio.
- **Metrics**: IRR, p-value, 95% CI per pairwise comparison; significance threshold p < 0.05.
- **Expected outcome**: All pairwise crude-incidence comparisons across PHRs are statistically significant; direction consistent with Pee Dee highest.
- **Baselines**: pairwise reference PHRs (each region vs each other).
- **Dependencies**: E01

## E03: ADRD-specific (subtype) incidence by PHR, age-adjusted, with Poisson IRRs
- **Verifies**: C02, C03
- **Setup**:
  - Subtypes: Alzheimer's disease (AD), Vascular dementia (VaD), Mixed dementia, Other.
  - Age adjustment: age-adjusted incidence using the 2020 US census as the standard population.
  - Model: same offset Poisson framework as E02, run per subtype; Tukey-adjusted pairwise IRRs.
- **Procedure**:
  1. For each subtype, compute region-level age-adjusted incidence per 100,000.
  2. Fit per-subtype Poisson models; derive pairwise IRRs, p-values, 95% CIs.
  3. Map each subtype's regional incidence (Figures 4–7).
- **Metrics**: subtype-specific incidence per 100,000 per PHR; IRR/p/95% CI per pairwise comparison.
- **Expected outcome**: AD incidence highest in Pee Dee (significantly above each other region); VaD and Mixed highest in Upstate (Midlands-vs-Upstate significant); "Other" highest in Pee Dee and Upstate. Some subtype pairwise contrasts are non-significant.
- **Baselines**: pairwise reference PHRs.
- **Dependencies**: E01, E02

## E04: Age-group-stratified subtype incidence by PHR
- **Verifies**: C05
- **Setup**:
  - Age groups: <65, 65–74, 75–84, 85 and above.
  - Population at risk per PHR × age group from ACRPE.
  - Subtypes AD/VaD/Mixed/Other per cell.
- **Procedure**:
  1. Compute incidence per 100,000 for each PHR × age-group × subtype cell.
  2. Identify, within each age band, the highest- and lowest-incidence PHR per subtype.
  3. Examine the age gradient in AD incidence within PHRs.
- **Metrics**: incidence per 100,000 by PHR × age group × subtype.
- **Expected outcome**: AD incidence rises steeply with age; among 65+ bands AD highest in Pee Dee and VaD/Mixed highest in Upstate; <65 band shows a distinct pattern (AD/Mixed/Other highest in Upstate, VaD highest in Pee Dee).
- **Baselines**: cross-PHR comparison within each age band.
- **Dependencies**: E03

## E05: Descriptive sociodemographic characterization of the analytic cohort
- **Verifies**: C04
- **Setup**:
  - Inclusion: SCADR registrants aged 50–110 with 2021 diagnosis (early-onset captured from age 50).
  - Variables: ADRD subtype, age group, sex (male/female), race (non-Hispanic White / non-Hispanic Black / Other), by overall and by PHR.
- **Procedure**:
  1. Apply the Figure 1 exclusion cascade (year ≠ 2021; age outside 50–110).
  2. Tabulate counts and column percentages overall and per PHR (Table 1).
- **Metrics**: counts and percentages per characteristic.
- **Expected outcome**: cohort predominantly AD, aged 75+, female, and White; regional columns do not sum to overall due to missing regional classification.
- **Baselines**: none (descriptive).
- **Dependencies**: none

## E06: Missing-data assessment and robustness (sensitivity) analyses
- **Verifies**: C06
- **Setup**:
  - Missingness variable: missing county or zip code.
  - Association tests: chi-square test of independence between missingness and (age group, sex, ADRD-specific diagnosis); effect size via Cramér's V (0.10/0.30/0.50 = small/moderate/large).
  - Sensitivity methods: proportional redistribution (full-sample vs complete-case incidence) and extreme-case analysis (assign all missing-zip cases to the lowest-incidence region [Midlands] and to the highest [Pee Dee]).
- **Procedure**:
  1. Test whether missingness is associated with each covariate; report Cramér's V.
  2. Compare full-sample to complete-case incidence via proportional redistribution.
  3. Reassign missing-region cases to extreme regions and re-estimate PHR incidence.
- **Metrics**: chi-square p-values, Cramér's V; relative change in incidence under each scenario.
- **Expected outcome**: missingness associated with age-group and ADRD diagnosis (not completely at random); complete-case analysis underestimates incidence by a consistent amount across PHRs; extreme-case reassignment moves only Midlands and Pee Dee, leaving other PHRs stable → primary estimates robust.
- **Baselines**: complete-case analysis vs full-sample (redistributed) estimates.
- **Dependencies**: E01
