# Problem Specification

> Grounding: abstract-only. Only `metadata.json` and `metadata.md` were provided. Details not present in those files are marked "Not available from provided input".

## Observations

### O01: Global ADRD mortality rate increased among adults aged 65 years and older
- **Statement**: The abstract reports that global ADRD mortality among adults aged >=65 years increased from 1991 to 2021, with an AAPC reported for the period.
- **Evidence**: `metadata.md` abstract: "The global mortality of ADRD among adults aged >=65 years increased by 115%, from 6.5 (95% UI 1.5-18) per 100,000 population in 1991 to 14 (95% UI 3.5-37) per 100,000 population in 2021, with an Average Annual Percentage Change (AAPC) of 1.10% (95%CI 0.45%-1.76%)."
- **Implication**: ADRD mortality is presented as an increasing global burden in the older-adult population.

### O02: Global ADRD prevalence count increased among adults aged 65 years and older
- **Statement**: The abstract reports that global ADRD prevalence among adults aged >=65 years increased between 1991 and 2021.
- **Evidence**: `metadata.md` abstract: "The prevalence of ADRD in adults aged >=65 years increased by 160% between 1991 and 2021, from 18.7 (95%UI 14.9-23.2) million to 49 (95%UI 38.6-61.2) million."
- **Implication**: The study frames ADRD prevalence growth as a major pressure on healthcare systems.

### O03: Age-standardized prevalence changed only slightly in the abstract's reported global rates
- **Statement**: The age-standardized prevalence rate for adults aged >=65 years increased from 1991 to 2021 by a small amount relative to the increase in total prevalent cases.
- **Evidence**: `metadata.md` abstract: "The aged >=65 years age-standardized prevalence of ADRD in this age group increased from 11,977 (95%UI 9,438-14,935) per 100,000 population in 1991 to 12,124 (95%UI 9,489-15,204) per 100,000 population in 2021."
- **Implication**: The abstract's conclusion that prevalence growth is "largely driven by the expanding older adults" is consistent with a much larger increase in counts than in age-standardized prevalence rate.

### O04: Female prevalent-case counts exceeded male counts in both reported years
- **Statement**: The abstract reports more prevalent ADRD cases among women than men in both 1991 and 2021.
- **Evidence**: `metadata.md` abstract: "males: from 6.2 (95%UI 4.8-7.8) million in 1991 to 17.2 (95%UI 13.4-21.6) million in 2021; women: from 12.5 (95%UI 10.0-15.4) million in 1991 to 31.7 (95%UI 25.1-39.6) million in 2021".
- **Implication**: Sex disparities are part of the study's reported burden profile, but causal explanation is not available from provided input.

### O05: The abstract identifies deaths, DALYs, and modifiable risk factors in 2021
- **Statement**: The abstract reports 2021 ADRD deaths and DALYs attributable to dementia in adults aged >=65 years and names high BMI, high fasting glucose, and smoking as modifiable risk factors.
- **Evidence**: `metadata.md` abstract: "In 2021, ADRD in adults aged >=65 years caused 8.02 (95%UI 1.34-22.19) million deaths and 25.38 (95%UI 23.18-71.20) million DALYs attributable to dementia, and high BMI, high fasting glucose, and smoking remained modifiable risk factors in all risk factors."
- **Implication**: The paper links burden measurement to prevention-oriented recommendations, though attributable fractions are not available from provided input.

## Gaps

### G01: Full regional and country disparity results are unavailable
- **Statement**: The abstract says the study analyzes different regions and countries, but the supplied inputs do not provide region- or country-specific results.
- **Caused by**: O01, O02, O03, O04, O05 are all global or sex-stratified abstract-level summaries.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

### G02: Detailed GBD modeling, uncertainty propagation, and risk attribution methods are unavailable
- **Statement**: The abstract names data sources and outcomes but does not provide the full analytic model, case definitions, uncertainty procedures, or risk-attribution fractions.
- **Caused by**: Only abstract/metadata were provided.
- **Existing attempts**: GBD 2021 is named as the data source and framework.
- **Why they fail**: Not available from provided input.

### G03: Evidence objects cannot be enumerated
- **Statement**: No full text, figures, tables, or appendices were provided, so source evidence objects cannot be filed.
- **Caused by**: Only `metadata.json` and `metadata.md` were available.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

## Key Insight
- **Insight**: A global GBD 2021 analysis can characterize ADRD burden among adults aged 65 years and older across time, geography, sex, mortality, prevalence, DALYs, AAPC, and selected modifiable risk factors.
- **Derived from**: O01, O02, O03, O04, O05.
- **Enables**: A public-health framing that pairs burden estimation with recommendations for standardized screening and risk-factor management.

## Assumptions
- A1: The abstract's reported estimates are outputs of the paper's GBD 2021 analysis.
- A2: The phrase "adults aged 65 years and older" defines the population scope for the extracted claims.
- A3: Detailed regional/country values, model parameters, and risk-attributable fractions are not recoverable from the provided inputs.
