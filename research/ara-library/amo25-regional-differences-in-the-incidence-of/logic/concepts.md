# Concepts

## ADRD (Alzheimer's Disease and Related Dementias)
- **Notation**: —
- **Definition**: Umbrella category for dementia arising from progressive neurodegeneration with impairment in ≥2 cognitive domains (memory, language, executive function, attention) that significantly interferes with daily functioning. In this registry it is classified into four categories: Alzheimer's disease (AD), Vascular dementia (VaD), Mixed dementia, and Other medical conditions (alcohol dementia, drug-induced dementia, dementia with other conditions, dementia with Lewy bodies, Pick's disease, frontotemporal dementia).
- **Boundary conditions**: Registry cases are identified/diagnosed by a physician/neurologist following a healthcare visit and coded with ICD-10-CM; the study restricts to registrants aged 50–110 with a 2021 diagnosis.
- **Related concepts**: Alzheimer's disease, Vascular dementia, Mixed dementia, SCADR, Incidence

## Public Health Region (PHR)
- **Notation**: —
- **Definition**: One of the four administrative regions into which South Carolina is divided — Low Country, Midlands, Pee Dee, and Upstate — each with distinct social and cultural attributes affecting residents' well-being. The independent variable of the study.
- **Boundary conditions**: Cases with missing county/zip cannot be assigned a PHR (n = 3,910). Pee Dee is predominantly rural and has the highest social vulnerability index in SC.
- **Related concepts**: County, Social Vulnerability Index, Incidence Rate Ratio

## Incidence (per 100,000 population)
- **Notation**: cases per 100,000
- **Definition**: The number of new ADRD cases (diagnosed in 2021) divided by the population at risk, scaled to 100,000, computed for each county and PHR.
- **Boundary conditions**: "New cases" = year of diagnosis 2021 in the SCADR; denominators from ACRPE. Reflects diagnosed/registered incidence, an underestimate of true incidence.
- **Related concepts**: Age-adjusted incidence rate, Population at risk, ACRPE

## Age-adjusted incidence rate
- **Notation**: —
- **Definition**: Incidence standardized to a reference age distribution so regions with different age structures are comparable; ADRD-specific incidence was age-adjusted using the 2020 US census as the standard population.
- **Boundary conditions**: Applied to ADRD-specific (subtype) incidence; crude incidence is not age-adjusted.
- **Related concepts**: Incidence, Standard population, Age group

## Incidence Rate Ratio (IRR)
- **Notation**: IRR = exp(β)
- **Definition**: The ratio of incidence rates between two PHRs, obtained by exponentiating the Poisson regression coefficient (β); IRR > 1 indicates higher incidence in the index region relative to the reference. Reported with p-value and 95% CI.
- **Boundary conditions**: Statistically significant at p < 0.05; Tukey-adjusted for multiple pairwise comparisons.
- **Related concepts**: Poisson regression with offset, Public Health Region

## Poisson regression with population offset
- **Notation**: log(E[count]) = β·PHR + log(population); log-link
- **Definition**: A count model in which the expected number of new cases is modeled as a function of PHR, with the natural logarithm of the population at risk included as an offset so the model estimates rates rather than raw counts across differently sized regions. A Type 3 option estimates the likelihood ratio for overall PHR significance.
- **Boundary conditions**: Treats PHR as a fixed effect; fitted in SAS 9.4.
- **Related concepts**: Incidence Rate Ratio, Offset variable, Likelihood ratio

## Social Vulnerability Index
- **Notation**: —
- **Definition**: A composite index of a community's susceptibility to adverse health outcomes, determined by factors including poverty and lack of access to transportation and housing; high values are linked to inequitable access to healthcare and essential services.
- **Boundary conditions**: Used interpretively; the Pee Dee PHR has the highest social vulnerability index in South Carolina.
- **Related concepts**: Public Health Region, Rurality

## SCADR (South Carolina Alzheimer's Disease Registry)
- **Notation**: —
- **Definition**: Statewide ADRD case registry, in existence since 1988, described as the oldest and most comprehensive dementia registry in the US. Collects year of diagnosis, entry year, diagnosis location, current age, ADRD subtype, county/zip of residence, date of birth, source of inclusion, month/year of death, underlying cause of death, sex, race, and time in the registry. Cases assembled from inpatient hospitalizations, emergency departments, vital records, state health plans, and other claims data.
- **Boundary conditions**: Case-identifying core data set is used for matching/deduplication/linkage; access is by request under licenses/restrictions.
- **Related concepts**: ACRPE, ICD-10-CM, ADRD

## ACRPE (Annual County Resident Population Estimates)
- **Notation**: —
- **Definition**: US Census Bureau county-level population estimates used as denominators for incidence; incorporate the 2020 census, Vintage 2020 estimates, and 2020 Demographic Analysis estimates.
- **Boundary conditions**: County-level; provides population at risk and (2020 census) the standard population for age adjustment.
- **Related concepts**: Incidence, TIGER/Line files, Age-adjusted incidence rate

## Cramér's V
- **Notation**: V
- **Definition**: An effect-size measure for association between categorical variables (here, missingness vs age-group/sex/diagnosis), with 0.10, 0.30, 0.50 interpreted as small, moderate, and large.
- **Boundary conditions**: Reported alongside chi-square tests in the missing-data analysis.
- **Related concepts**: Chi-square test of independence, Missing data

## Sensitivity analysis (proportional redistribution & extreme-case)
- **Notation**: —
- **Definition**: Robustness checks for missing regional data — proportional redistribution reallocates missing-region cases proportionally to compare full-sample vs complete-case incidence; extreme-case analysis assigns all missing-zip cases to the lowest- (Midlands) and highest- (Pee Dee) incidence regions to bound the estimates.
- **Boundary conditions**: Used to test stability of PHR incidence estimates under different missingness assumptions.
- **Related concepts**: Missing data, Cramér's V, Incidence

## TIGER/Line files
- **Notation**: —
- **Definition**: US Census Bureau geographic/topological shapefiles used to render the county- and PHR-level choropleth maps (Figures 2–7) in QGIS.
- **Boundary conditions**: Public/open geographic data; used for visualization only.
- **Related concepts**: ACRPE, Public Health Region
