# Problem Specification

> Grounding: abstract-only. Observations and gaps use only the supplied metadata/abstract.

## Observations

### O01: Dementia burden in older adults is a public-health issue
- **Statement**: Dementia burden in the elderly is predicted to rise, and dementia among older adults is a crucial public-health issue.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: Burden measurement is needed to support healthcare strategy adjustment.

### O02: The study targets older adults across a long global trend period
- **Statement**: The analysis covers Alzheimer's disease and other dementias among individuals aged 65 and older from 1990 to 2021.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: The work is framed as a long-run burden analysis rather than a single-year prevalence snapshot.

### O03: The analysis spans countries and inequality metrics
- **Statement**: The abstract reports analysis of SDI relationships, frontier analysis across 204 countries, and inequality in age-standardized DALYs using slope inequality and concentration indices.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: The problem is not only global burden estimation; it includes whether burden is equitably distributed relative to social development.

### O04: Global age-standardized rates declined over time
- **Statement**: Globally, age-standardized DALYs and mortality rates for individuals aged 65 and older declined over time.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: Trend interpretation must distinguish age-standardized rate decline from absolute or distributional burden.

### O05: Burden varies with SDI and population distribution
- **Statement**: The abstract reports significant association with SDI, a high-versus-low SDI baseline contrast, and concentration of burden in lower-SDI populations.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: Country development level and population distribution jointly shape the public-health interpretation.

## Gaps

### G01: Healthcare strategy needs burden quantification
- **Statement**: Relevant areas and countries need scientific data to adjust healthcare strategies.
- **Caused by**: O01, O02
- **Existing attempts**: Not available from provided input
- **Why they fail**: Not available from provided input

### G02: SDI-linked inequality must be separated from global trend averages
- **Statement**: A global decline in age-standardized rates does not by itself reveal SDI-associated disparities, frontier gaps, or concentration of burden.
- **Caused by**: O03, O04, O05
- **Existing attempts**: Not available from provided input
- **Why they fail**: Not available from provided input

### G03: Country burden relative to feasible SDI-associated minima is unclear without frontier analysis
- **Statement**: The abstract frames country burden relative to the minimum disease burden associated with SDI.
- **Caused by**: O03, O05
- **Existing attempts**: Not available from provided input
- **Why they fail**: Not available from provided input

## Key Insight
- **Insight**: Dementia burden in older adults should be analyzed jointly as a temporal GBD trend, an SDI-associated burden relationship, a country-level frontier problem, and an inequality distribution problem.
- **Derived from**: O01-O05
- **Enables**: Claims about global rate trends, SDI association, country burden above SDI-associated minima, and lower-SDI concentration of DALY burden.

## Assumptions
- A1: GBD 2021 provides sufficient disease-burden estimates for Alzheimer's disease and other dementias among individuals aged 65 and older.
- A2: SDI is an appropriate social-development scale for comparing dementia burden across countries and populations.
- A3: The slope inequality index and concentration index are appropriate measures for DALY inequality in this setting.
- A4: Full methodological assumptions, covariates, uncertainty models, and case definitions are not available from provided input.
