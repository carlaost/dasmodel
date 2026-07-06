# Problem Specification

> Grounding: abstract-only. Source references point to `metadata.md`; no full text, tables, or
> figures were available.

## Observations

### O01: Midlife vascular risk is associated with dementia risk
- **Statement**: The abstract states that midlife vascular risk factors are associated with elevated dementia risk, but the total contribution of midlife and late-life vascular risk factors to incident dementia is uncertain.
- **Evidence**: `metadata.md:13-18`.
- **Implication**: The motivating problem is not whether vascular risks matter at all, but how much incident dementia can be attributed to modifiable vascular risk factors at different ages and in different subgroups.

### O02: The study uses long ARIC follow-up
- **Statement**: The analysis is a prospective cohort analysis of ARIC using 33 years of follow-up from 1987-2020.
- **Evidence**: `metadata.md:21-22`.
- **Implication**: The cohort structure supports estimating dementia incidence over long aging intervals, including outcomes by age 80 and after age 80.

### O03: Attributable dementia fraction by age 80 varies by age at risk-factor measurement
- **Statement**: The abstract reports attributable fractions by age 80 of 21.8% for risk factors at age 45-54 years, 26.4% for age 55-64 years, and 44.0% for age 65-74 years.
- **Evidence**: `metadata.md:33-34`.
- **Implication**: The attributable contribution reported in the abstract is not uniform across age windows.

### O04: Post-80 attributable fractions are much smaller in the abstract result
- **Statement**: The abstract reports that only 2% to 8% of dementia cases after age 80 were attributable to these factors.
- **Evidence**: `metadata.md:33-34`.
- **Implication**: The abstract distinguishes dementia by age 80 from dementia after age 80; extrapolating by-age-80 effects to later incident dementia would be unsupported.

## Gaps

### G01: Total contribution across midlife and late-life vascular risk was uncertain
- **Statement**: Before this analysis, the total contribution of vascular risk factors in midlife and late life with incident dementia was uncertain.
- **Caused by**: O01.
- **Existing attempts**: Prior association evidence linking midlife vascular risks to elevated dementia risk is acknowledged by the abstract.
- **Why they fail**: Association evidence alone does not quantify the proportion of incident dementia attributable to the modifiable risk factors at the specified ages.

### G02: Subgroup differences needed quantification
- **Statement**: The study aimed to examine differences by APOE e4 genotype, self-reported race, and sex.
- **Caused by**: O01 and the objective in `metadata.md:17-18`.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

### G03: Detailed methods and evidence objects are unavailable in this artifact
- **Statement**: The provided input contains only metadata and abstract text, not the full article.
- **Caused by**: Input limitation.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: No PDF, tables, figures, model specifications, appendix, or code were provided.

## Key Insight
- **Insight**: Estimating population attributable fractions for having at least one modifiable vascular risk factor at specific age windows can translate vascular-risk associations into a public-health quantity for incident dementia by age 80 and after age 80.
- **Derived from**: O01, O02, O03, O04.
- **Enables**: Age-windowed and subgroup-aware claims about the attributable contribution of vascular risk factors, while preserving the abstract's causal caveat.

## Assumptions
- A1: The abstract's reported population attributable fractions are treated as study results, not independently re-estimated.
- A2: Causal mitigation language is conditional because the conclusion explicitly says "Assuming causal relationships."
- A3: Exposure definitions, outcome ascertainment, model covariates, missing-data handling, and sensitivity analyses are not available from provided input beyond the abstract statements.
