# Claims

> Grounding: abstract-only. Every load-bearing number in a Statement is copied from `metadata.md`
> and paired with a verbatim source quote tagged `[result]`. No full-text evidence tables or
> figures were available.

## C01: Vascular risk factors account for substantial dementia incidence by age 80 across age windows
- **Statement**: In ARIC, the fraction of dementia by age 80 attributable to at least 1 vascular factor was 21.8% (95% CI, 14.3%-29.3%) for risk factors at age 45-54 years, 26.4% (95% CI, 19.1%-33.6%) at age 55-64 years, and 44.0% (95% CI, 30.9%-57.2%) at age 65-74 years.
- **Status**: supported
- **Falsification criteria**: Re-analysis of the same ARIC exposure windows and dementia-by-80 outcome yielding population attributable fractions outside the reported confidence intervals, or showing the abstract's age-window labels/results were incorrect.
- **Proof**: [E01]
- **Evidence basis**: The Results section of the abstract reports the three population attributable fractions and confidence intervals directly.
- **Interpretation**: The attributable contribution by age 80 is sizeable and appears larger for the 65-74-year measurement window in the abstract results; the abstract does not provide model details needed to infer mechanisms.
- **Sources**:
  - 21.8% (95% CI, 14.3%-29.3%), 26.4% (95% CI, 19.1%-33.6%), and 44.0% (95% CI, 30.9%-57.2%) ← metadata.md:34 «The fraction of dementia by 80 years attributable to at least 1 vascular factor at age 45 to 54 years was 21.8% (95% CI, 14.3%-29.3%), at 55 to 64 years was 26.4% (95% CI, 19.1%-33.6%), and at 65 to 74 years was 44.0% (95% CI, 30.9%-57.2%).» [result]
- **Dependencies**: none
- **Tags**: population-attributable-fraction, dementia-by-80, ARIC, vascular-risk

## C02: The analytic samples and dementia cases differ by age-window analysis
- **Statement**: The abstract reports analytic sample sizes of 7731, 12274, and 6787 participants for risk-factor measurement windows 45-54, 55-64, and 65-74 years, respectively, with 801, 995, and 422 dementia cases by age 80.
- **Status**: supported
- **Falsification criteria**: Full-text tables or reproducible cohort code showing different analytic sample sizes or dementia case counts for the same age-window analyses.
- **Proof**: [E02]
- **Evidence basis**: The Results section gives participant counts and dementia case counts for the three age-window analyses.
- **Interpretation**: The three analyses are not a single identical participant set; downstream agents should preserve the age-window-specific denominators rather than combining them.
- **Sources**:
  - 7731, 12274, 6787 participants; 801, 995, 422 cases ← metadata.md:34 «A total of 7731 participants were included in analysis of risk factors measured at age 45 to years (4494 female [58%]; 2207 Black [29%]; 5524 White [71%]), 12 274 contributed to analysis of risk factors measured at age 55 to 64 years (6698 female [55%]; 2886 Black [24%]; 9388 White [76%]), and 6787 contributed to analysis of risk factors measured at age 65 to 74 years (3764 female [56%], 1375 Black [20%]; 5412 White [80%]). There were 801, 995, and 422 dementia cases by 80 years, respectively.» [result]
- **Dependencies**: none
- **Tags**: analytic-sample, dementia-cases, age-window

## C03: Attributable fractions were higher in specified subgroups
- **Statement**: The abstract reports higher attributable fractions for APOE e4 noncarriers at age 55 years and older (range, 33.3%-61.4%), Black individuals at age 45 years and older (range, 25.5%-52.9%), and female individuals at age 55 years and older (range, 29.2%-51.3%).
- **Status**: supported
- **Falsification criteria**: Full-text subgroup tables or reproducible analyses showing the subgroup ranges or subgroup direction are not as reported in the abstract.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly states the subgroup categories and ranges.
- **Interpretation**: The abstract supports subgroup heterogeneity in reported attributable fractions, but not the detailed subgroup denominators, interaction tests, or causal mechanisms.
- **Sources**:
  - APOE e4 noncarriers 33.3%-61.4%, Black individuals 25.5%-52.9%, female individuals 29.2%-51.3% ← metadata.md:34 «Attributable fractions for these factors were higher in apolipoprotein ε4 noncarriers at age 55 years and older (range, 33.3%-61.4%), Black individuals at age 45 years and older (range, 25.5%-52.9%), and female individuals at age 55 years and older (range, 29.2%-51.3%).» [result]
- **Dependencies**: C01
- **Tags**: subgroup-analysis, APOE-e4, race, sex

## C04: Post-80 dementia cases had low attributable fractions for the studied factors
- **Statement**: Only 2% to 8% of dementia cases after age 80 were attributable to the studied vascular risk factors.
- **Status**: supported
- **Falsification criteria**: Full-text or reproducible post-80 analyses showing attributable fractions materially outside the reported 2% to 8% range.
- **Proof**: [E04]
- **Evidence basis**: The abstract states the post-80 attributable fraction range directly.
- **Interpretation**: The vascular risk contribution reported for dementia by age 80 should not be assumed to apply to dementia after age 80.
- **Sources**:
  - 2% to 8% ← metadata.md:34 «Only 2% to 8% of dementia cases after 80 years were attributable to these factors.» [result]
- **Dependencies**: C01
- **Tags**: post-80-dementia, attributable-fraction, age-stratification
