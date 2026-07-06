# Concepts

> Grounding: abstract-only. Definitions reflect terms used in the abstract; detailed operational definitions are not available from provided input.

## Alzheimer's Disease and Other Dementias
- **Notation**: ADOD
- **Definition**: The disease category analyzed for burden, risk factors, and future predictions in Asia.
- **Boundary conditions**: Exact GBD case definitions and included dementia subtypes are not available from provided input.
- **Related concepts**: Global Burden of Disease Study 2021, incidence, prevalence, mortality, DALYs.

## Global Burden of Disease Study 2021
- **Notation**: GBD 2021
- **Definition**: The data source from which ADOD data in Asia from 1990 to 2021 were collected.
- **Boundary conditions**: Extraction protocol, uncertainty handling, and country inclusion rules are not available from provided input.
- **Related concepts**: disease burden, age-standardized rates, DALYs.

## Disease Burden
- **Notation**: --
- **Definition**: The abstract's umbrella outcome framing for ADOD impact, including incidence, prevalence, mortality, and DALYs.
- **Boundary conditions**: Metric-specific forecast outputs and uncertainty intervals are not available from provided input.
- **Related concepts**: incidence, prevalence, mortality, DALYs, ARIMA.

## Age-Standardized Rate
- **Notation**: ASR
- **Definition**: A rate adjusted for age structure, used in the abstract for incidence, prevalence, death, and DALYs.
- **Boundary conditions**: Standard population and computation formula are not available from provided input.
- **Related concepts**: ASMR, sex-stratified trends, Joinpoint regression.

## Age-Standardized Mortality Rate
- **Notation**: ASMR
- **Definition**: The age-standardized death rate for ADOD; the abstract reports Afghanistan and China as having the highest ASMR in 2021.
- **Boundary conditions**: Exact ASMR values and ranking table are not available from provided input.
- **Related concepts**: mortality, age-standardized rates, country ranking.

## Disability-Adjusted Life-Years
- **Notation**: DALYs
- **Definition**: A disease-burden metric analyzed as both number and age-standardized rate for ADOD.
- **Boundary conditions**: Components, uncertainty intervals, and country-specific values are not available from provided input.
- **Related concepts**: disease burden, prevalence, mortality, Joinpoint regression.

## Joinpoint Regression
- **Notation**: --
- **Definition**: The trend-analysis method the abstract says was performed to evaluate temporal trends from 1990 to 2021.
- **Boundary conditions**: Joinpoint settings, segment estimates, and software are not available from provided input.
- **Related concepts**: AAPC, ASR, temporal trend.

## Average Annual Percent Change
- **Notation**: AAPC
- **Definition**: A trend summary calculated in the study to evaluate changes during 1990-2021.
- **Boundary conditions**: Exact AAPC values and confidence intervals are not available from provided input.
- **Related concepts**: Joinpoint regression, trend analysis.

## Auto-Regressive Integrated Moving Average Prediction Model
- **Notation**: ARIMA
- **Definition**: The forecasting model used to assess ADOD trends in Asia over the next 30 years.
- **Boundary conditions**: ARIMA order, stationarity checks, training/validation splits, forecast intervals, and metric-specific outputs are not available from provided input.
- **Related concepts**: forecasting, disease burden, future prediction.
