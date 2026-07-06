# Concepts

> Abstract-only compile. Definitions are standard epidemiological usage instantiated as this study
> uses each term (grounded in the abstract). Where the paper's own operational nuance would live in
> the full text, that nuance is "Not available from provided input (no full text)".

## Early-onset Alzheimer's disease (EOAD)
- **Notation**: G30.0 (ICD-10-CM underlying-cause-of-death code)
- **Definition**: Alzheimer's disease with symptom onset before age 65, identified in this study as deaths with ICD-10-CM code G30.0 recorded as the underlying cause of death.
- **Boundary conditions**: "Early-onset" refers to *age at onset* (< 65), not age at death; in this cohort mean age at death was 69.8 years (see C05). Ascertainment depends entirely on death-certificate coding.
- **Related concepts**: Late-onset Alzheimer's disease, Underlying cause of death, ICD-10-CM coding

## Late-onset Alzheimer's disease (LOAD)
- **Notation**: G30.1 (ICD-10-CM code)
- **Definition**: Alzheimer's disease with onset at or after age 65, coded G30.1; used here as the comparator in a sensitivity analysis against EOAD trends.
- **Boundary conditions**: Serves as an internal control for generic AD-coding drift over the same source and period.
- **Related concepts**: Early-onset Alzheimer's disease, Sensitivity analysis

## Age-adjusted mortality rate (AAMR)
- **Notation**: AAMR (per 1,000,000 population in this study)
- **Definition**: A mortality rate standardized to a fixed age distribution (standard population), removing the confounding effect of differing age structures across groups/years, allowing valid comparison of mortality across subgroups and time.
- **Boundary conditions**: Comparability assumes a consistent standard population across all extractions (CDC WONDER default US 2000 standard population, per convention — exact standard not stated in abstract).
- **Related concepts**: Rate ratio, Annual percent change

## Annual percent change (APC)
- **Notation**: APC (reported +19.96%)
- **Definition**: The average per-year percentage change in a rate over a segment, estimated from the slope of a log-linear model fitted to the rate time series (here via Joinpoint regression).
- **Boundary conditions**: Assumes log-linear trend within a Joinpoint segment; the number of joinpoints/segments underlying the +19.96% is not stated in the abstract.
- **Related concepts**: Joinpoint regression, Age-adjusted mortality rate

## Joinpoint regression
- **Notation**: —
- **Definition**: A segmented log-linear regression method that identifies statistically significant change points ("joinpoints") in a rate time series and estimates an APC for each segment; standard for cancer/mortality trend surveillance.
- **Boundary conditions**: Requires a rate series over time; segment count is data-driven. Software/settings not specified in the abstract.
- **Related concepts**: Annual percent change, Temporal trend

## Rate ratio (RR)
- **Notation**: RR (e.g., 1.50, 95% CI 1.40-1.59 for female vs male)
- **Definition**: The ratio of the age-adjusted mortality rate in one group to that in a reference group; RR > 1 indicates higher mortality in the index group.
- **Boundary conditions**: Interpreted with its 95% confidence interval; excludes 1.0 to be considered a significant disparity.
- **Related concepts**: Age-adjusted mortality rate, Demographic disparity

## Underlying cause of death (UCD)
- **Notation**: UCD
- **Definition**: The disease or injury that initiated the chain of events leading directly to death, as recorded on the death certificate; the basis on which this study attributes deaths to EOAD (G30.0).
- **Boundary conditions**: Restricting to UCD (vs. multiple/contributing causes) yields a conservative count; deaths where EOAD is a contributing but not underlying cause are excluded.
- **Related concepts**: ICD-10-CM coding, CDC WONDER

## ICD-10-CM coding (G30.0 / G30.1)
- **Notation**: G30.0 (EOAD), G30.1 (LOAD)
- **Definition**: The International Classification of Diseases, 10th Revision, Clinical Modification codes used to classify cause of death; G30.0 = "Alzheimer's disease with early onset", G30.1 = "Alzheimer's disease with late onset".
- **Boundary conditions**: Classification accuracy depends on certifier practices; misclassification between G30.0/G30.1/G30.9 (unspecified) can bias trends.
- **Related concepts**: Underlying cause of death, EOAD, LOAD

## CDC WONDER
- **Notation**: —
- **Definition**: The CDC's Wide-ranging Online Data for Epidemiologic Research platform, providing publicly available, de-identified US mortality data derived from death certificates, queryable by cause, demographics, geography, and year.
- **Boundary conditions**: Suppresses/flags small cell counts for confidentiality; subgroup rates with fewer than a threshold of deaths may be unreliable or unreported. Access: open/public.
- **Related concepts**: Underlying cause of death, Age-adjusted mortality rate
