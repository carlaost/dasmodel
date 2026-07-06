# Study Design

> Grounding: abstract-only. This file captures only design elements explicitly named in the abstract.

## Study Aim

Assess global and regional burden and trends of Alzheimer's disease and other dementias in adults aged 60 years or older from 1990 to 2021, with focus on the COVID-19 pandemic's impact on mortality, prevalence, and DALYs.

## Data Source

- Global Burden of Disease 2021.
- Raw data extraction procedure: Not available from provided input.
- Case definitions: Not available from provided input.

## Outcomes

- Age-standardized death rates.
- Incidence rates.
- Prevalence rates.
- Disability-adjusted life years.
- Excess mortality during the pandemic.
- Health inequality across regions.

## Analytic Components

### Historical burden analysis
- **Purpose**: Estimate burden from 1990 to 2021.
- **Inputs**: GBD 2021 data.
- **Outputs**: ASDR, ASIR, ASPR, DALYs, mortality, prevalence.
- **Unavailable details**: Exact extraction, stratification schema, and uncertainty modeling.

### Temporal trend analysis
- **Purpose**: Assess temporal trends.
- **Method**: Estimated Annual Percentage Change.
- **Software named**: Joinpoint Regression model Version 4.8.0.1.
- **Unavailable details**: Regression form, joinpoint settings, and trend coefficients.

### Projection analysis
- **Purpose**: Model future AD cases to 2050.
- **Method**: Bayesian Age-Period-Cohort techniques.
- **Unavailable details**: Priors, cohort construction, age bands, and uncertainty intervals.

### Pandemic excess mortality analysis
- **Purpose**: Evaluate COVID-19 mortality impact.
- **Method**: Compare actual versus expected deaths during the pandemic.
- **Unavailable details**: Counterfactual model and regional excess estimates.

### Decomposition analysis
- **Purpose**: Examine contributions of population growth, aging, and epidemiological shifts.
- **Unavailable details**: Formula, component estimates, and subgroup outputs.

### Health inequality analysis
- **Purpose**: Highlight disparities in health status and resource access across regions.
- **Unavailable details**: Inequality metric, region list, and SDI thresholds.
