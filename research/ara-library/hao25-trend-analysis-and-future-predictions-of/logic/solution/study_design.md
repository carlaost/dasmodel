# Study Design

> Grounding: abstract-only. This file captures the analysis design explicitly named in the abstract. Procedural detail beyond the abstract is marked unavailable.

## Data Source and Scope

- **Source**: Global Burden of Disease database.
- **Disease category**: Alzheimer's disease and other dementias.
- **Time period**: 1990 to 2021 for retrospective trend analysis.
- **Forecast horizon**: through 2040.
- **Geography**: global, regional, and national.
- **Measures**: incidence, prevalence, Disability-Adjusted Life Years.

## Analysis Components

### Descriptive burden analysis
- **Purpose**: Compare incidence, prevalence, and DALYs across global, regional, and national levels.
- **Supported outputs from abstract**: increasing global burden, highest burden in East Asia, older-female prevalence pattern.
- **Unavailable detail**: Exact estimates, uncertainty intervals, and rank tables.

### Joinpoint regression
- **Purpose**: Identify significant changes in temporal trends.
- **Supported outputs from abstract**: change years in 1995, 2005, 2011, and 2019; acceleration after 2011 and especially after 2019.
- **Unavailable detail**: Model selection settings, annual percentage changes, and which burden metric(s) each change point applies to.

### Age-period-cohort analysis
- **Purpose**: Analyze age, period, and birth-cohort effects on disease risk.
- **Supported outputs from abstract**: age is a significant risk factor, with sharp risk increase after age 60.
- **Unavailable detail**: Age bands, period bands, cohort bands, link function, priors or constraints.

### DALY-driver decomposition
- **Purpose**: Assess the impact of aging, population growth, and epidemiological changes on DALYs across SDI quintiles.
- **Supported outputs from abstract**: epidemiological changes have a minor global impact but vary by region and gender; aging predominates in high-SDI regions and demographic expansion in low-SDI regions.
- **Unavailable detail**: Decomposition equation, component values, and uncertainty intervals.

### Bayesian age-period-cohort forecasting
- **Purpose**: Predict future burden through 2040.
- **Supported outputs from abstract**: sustained growth; projected 2040 age-standardized incidence and prevalence rates.
- **Unavailable detail**: Priors, posterior diagnostics, forecast intervals, validation method, and implementation software.
