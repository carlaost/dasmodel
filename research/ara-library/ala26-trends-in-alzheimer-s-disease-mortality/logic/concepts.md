# Concepts

> Grounding: abstract-only. Definitions of study-specific terms (AAMR, Joinpoint regression,
> underlying cause of death) are standard epidemiological/CDC WONDER definitions; the paper's own
> operational specifics (exact code sets, standard population year) are "Not available from provided
> input (no full text)".

## Age-Adjusted Mortality Rate (AAMR)
- **Notation**: AAMR (per 100,000 population)
- **Definition**: A mortality rate that has been standardized to a reference age distribution so that rates are comparable across populations and over time without confounding by differing age structures. Reported here per 100,000 population.
- **Boundary conditions**: Applies to the study population (US adults aged ≥75, 1999–2020). The specific standard population used for adjustment is Not specified in the abstract (no full text).
- **Related concepts**: Crude mortality rate, Underlying cause of death, Joinpoint regression

## Alzheimer's Disease (AD) as Underlying Cause of Death
- **Notation**: —
- **Definition**: The disease recorded on the death certificate as the condition that initiated the chain of events leading to death (as opposed to a contributing or immediate cause). Here AD serves as the underlying cause selector for the study cohort.
- **Boundary conditions**: Determined by death-certificate coding (ICD-10 during this era). Exact ICD-10 code(s) used: Not available from provided input (no full text).
- **Related concepts**: Multiple cause of death, Metabolic syndrome-related conditions

## Metabolic Syndrome-Related Conditions
- **Notation**: —
- **Definition**: A cluster of interrelated cardiometabolic conditions (e.g., obesity, hypertension, dyslipidemia, insulin resistance/diabetes) sharing risk determinants and pathophysiology with AD; here used to define the comorbidity subset of AD deaths.
- **Boundary conditions**: Operationalized via a defined set of death-certificate conditions/codes; the exact constituent conditions and codes are Not available from provided input (no full text).
- **Related concepts**: AD as underlying cause of death, Comorbidity

## Joinpoint Regression
- **Notation**: APC / AAPC (annual / average annual percent change)
- **Definition**: A segmented-regression trend-analysis method that fits a series of connected linear segments (on a log scale) to time-series rates, identifying "joinpoints" where the trend slope changes significantly; each segment yields an annual percent change (APC).
- **Boundary conditions**: Used here to detect trend inflections in AAMR over 1999–2020 across demographic, geographic, and place-of-death strata. Number of joinpoints and APC/AAPC values: Not available from provided input (no full text).
- **Related concepts**: AAMR, Temporal trend, Annual percent change

## CDC WONDER Multiple Cause of Death Database
- **Notation**: —
- **Definition**: The CDC's publicly queryable Wide-ranging ONline Data for Epidemiologic Research system providing US mortality data compiled from death certificates, supporting stratification by cause, demographics, geography, and place of death.
- **Boundary conditions**: National coverage of US death certificates; queried here for 1999–2020. Open access at https://wonder.cdc.gov/. No specific query/accession identifier was reported by the authors.
- **Related concepts**: AD as underlying cause of death, AAMR

## Percentile Ranking (Geographic)
- **Notation**: 90th / 10th percentile
- **Definition**: The rank position of a state's AAMR within the distribution of all states; "top 90th percentile" denotes among the highest-rate states, "lower 10th percentile" among the lowest.
- **Boundary conditions**: Applied to state-level AAMRs for the study population. Full state distribution: Not available from provided input (no full text).
- **Related concepts**: Geographic disparity, AAMR

## Place of Death
- **Notation**: —
- **Definition**: A death-certificate variable recording the setting in which death occurred (e.g., medical facility, nursing home/long-term care, hospice, home); analyzed here as one of the trend strata.
- **Boundary conditions**: Category definitions follow CDC WONDER's place-of-death coding. Specific category-level results are Not available from provided input (no full text).
- **Related concepts**: Joinpoint regression, Demographic stratification

## Health Disparity
- **Notation**: —
- **Definition**: Systematic, potentially avoidable differences in health outcomes (here AAMR) across population groups defined by sex, race/ethnicity, or geography.
- **Boundary conditions**: Framed in this study across sex, race/ethnicity, and state; linked in the conclusion to healthcare access and equity.
- **Related concepts**: AAMR, Percentile ranking, Place of death
