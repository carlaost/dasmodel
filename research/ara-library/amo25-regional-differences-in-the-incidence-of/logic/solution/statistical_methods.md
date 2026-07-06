# Statistical Methods

## Software
- Microsoft Excel and SAS version 9.4 (SAS Institute, Cary, NC) for rate calculation and modeling.
- QGIS version 3.34.13-Prizren for choropleth visualization using TIGER/Line files.

## Incidence estimation
- Incidence = number of new (2021) cases per 100,000 population, computed for each county and PHR.
- Age-adjusted incidence for ADRD-specific diagnoses computed using the **2020 US census as the standard population**.
- Denominators from ACRPE (2020 census / Vintage 2020 / 2020 Demographic Analysis).

## Regression model
- **Poisson regression** with a **log-link** function.
- **Dependent variable**: age-adjusted new-case count by PHR.
- **Independent variable**: PHR (fixed effect).
- **Offset**: natural logarithm of the population at risk — included so the model estimates rates (not raw counts) and to make PHRs of different population sizes comparable.
- **Overall PHR significance**: the Type 3 option estimates the likelihood ratio to assess the overall significance of the PHR effect.

## Effect measure and pairwise comparison
- Regression coefficients (β) are **exponentiated to Incidence Rate Ratios (IRRs)** for cross-PHR comparison and interpretability.
- **Poisson regression with Tukey-adjusted pairwise comparison** used to compare crude incidence by PHRs and ADRD-specific incidence by PHRs.
- Reported: p-values and 95% confidence intervals for the IRRs.
- **Significance threshold**: p < 0.05.

## Missing-data analysis
- Assessed whether excluded missing data (missing county or zip codes) were associated with age, sex, or ADRD-specific diagnosis using the **chi-square test of independence**.
- Effect sizes via **Cramér's V** (0.10 / 0.30 / 0.50 = small / moderate / large).

## Sensitivity analyses
- **Proportional redistribution method**: compares full-sample incidence estimates to complete-case-analysis estimates.
- **Extreme-case analysis**: assigns all cases with missing zip codes to the region with the lowest observed incidence (Midlands) and, separately, to the highest (Pee Dee), to bound the regional estimates.

## Notes on reported statistics (see evidence/tables/table2.md)
- Bolded p-values and 95% CIs in Table 2 denote statistical significance at p < 0.05.
- Some Table 2 cells contain typographic anomalies reproduced verbatim: the VaD "Low Country vs. Upstate" CI "(0.94–0.850)" (lower bound > upper bound) and the AD "Pee Dee vs. Upstate" p-value "<0.0002". These are noted, not corrected.
