# Experiments (Analysis Plans)

> Grounding: abstract-only. These are declarative analysis plans reconstructed from the analyses named in the abstract. Exact numerical results are kept in claims, not here. Unreported operational detail is marked "Not available from provided input".

## E01: Global burden trend analysis, 1990-2021
- **Verifies**: C01, C06
- **Setup**:
  - Data source: GBD 2021
  - Population: Individuals aged 65 and older with Alzheimer's disease and other dementias
  - Period: 1990-2021
  - Geography: Global; country/regional details not available from provided input
- **Procedure**:
  1. Extract age-standardized DALYs and mortality rates for the target population over the study period.
  2. Estimate global temporal trends in these measures.
  3. Determine whether each rate declines or increases over time.
  4. Assess whether dementia substantially reduces healthy life expectancy in the target population.
- **Metrics**: Direction of change in age-standardized DALYs and mortality rates.
- **Expected outcome**:
  - Global age-standardized DALYs and mortality rates decline over time.
  - Dementia substantially reduces healthy life expectancy among adults aged 65 and older.
- **Baselines**: Earlier years in the 1990-2021 trend period.
- **Dependencies**: none

## E02: SDI association analysis for mortality and DALYs
- **Verifies**: C02, C03
- **Setup**:
  - Data source: GBD 2021 plus SDI strata or country-level SDI values
  - Outcomes: Mortality rates and DALYs
  - Exposure/stratifier: SDI
  - Statistical model: Not available from provided input
- **Procedure**:
  1. Relate dementia mortality rates and DALYs to SDI.
  2. Compare baseline dementia burden by SDI level.
  3. Assess whether burden differs between high-SDI and low-SDI countries.
- **Metrics**: Association direction and relative SDI-stratified baseline burden.
- **Expected outcome**:
  - Dementia burden is significantly associated with SDI.
  - High-SDI countries have higher baseline burden than low-SDI countries.
- **Baselines**: Low-SDI countries for the high-versus-low SDI contrast.
- **Dependencies**: E01

## E03: Frontier analysis across countries
- **Verifies**: C03, C05
- **Setup**:
  - Data source: GBD 2021
  - Units: 204 countries
  - Frontier definition: Minimum disease burden associated with SDI
  - Model details: Not available from provided input
- **Procedure**:
  1. Estimate an SDI-associated frontier or minimum burden level across countries.
  2. Compare each country's observed dementia burden with the SDI-associated minimum.
  3. Summarize whether countries lie above the minimum burden associated with their SDI.
- **Metrics**: Country position relative to SDI-associated minimum burden; SDI-stratified baseline contrast.
- **Expected outcome**:
  - Most countries have burden above the minimum associated with their SDI.
- **Baselines**: SDI-associated minimum disease burden.
- **Dependencies**: E02

## E04: Health inequality analysis of age-standardized DALYs
- **Verifies**: C04, C05
- **Setup**:
  - Data source: GBD 2021
  - Outcome: Age-standardized DALYs for Alzheimer's disease and other dementias
  - Inequality measures: Slope inequality index and concentration index
  - Population weighting details: Not available from provided input
- **Procedure**:
  1. Quantify inequality in age-standardized DALYs using the slope inequality index.
  2. Quantify concentration of DALY burden using the concentration index.
  3. Relate inequality findings to SDI and population distribution.
  4. Assess trends in low/middle-SDI burden and gaps across SDI regions.
- **Metrics**: Direction of DALY gradient with SDI, concentration of burden, and direction of change in SDI-region gaps.
- **Expected outcome**:
  - DALYs increase with SDI overall, but burden is concentrated in lower-SDI populations.
  - Low- and middle-SDI burden increases while cross-SDI gaps narrow.
- **Baselines**: SDI-ranked population distribution and earlier time points in the study period.
- **Dependencies**: E02, E03
