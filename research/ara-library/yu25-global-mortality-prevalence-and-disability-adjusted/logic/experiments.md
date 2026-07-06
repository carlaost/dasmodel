# Experiments and Analyses

> These are declarative analyses reconstructed from the abstract. Exact numerical results are intentionally omitted here; claim-level numbers live in `claims.md`.

## E01: Estimate 2021 mortality and prevalence burden
- **Verifies**: C01
- **Setup**:
  - Data: GBD 2021.
  - Population: Adults aged 60 years or older.
  - Outcomes: Mortality and prevalence of AD and other dementias.
  - System: Joinpoint Regression model, StataMP 18, and R 4.4.1 are named for plots and tables; detailed pipeline not available from provided input.
- **Procedure**:
  1. Extract global burden estimates for adults aged 60 years or older.
  2. Summarize mortality and prevalence with uncertainty intervals.
  3. Report global late-period case counts.
- **Metrics**: Mortality cases and prevalence cases with uncertainty intervals.
- **Expected outcome**: Global mortality and prevalence indicate a substantial dementia burden in adults aged 60 years or older.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Attribute prominent risk factors
- **Verifies**: C02
- **Setup**:
  - Data: GBD 2021 risk-factor information.
  - Population: Adults aged 60 years or older with AD and other dementias.
  - Risk factors: High BMI and High FPG are named in the abstract.
  - System: Not available from provided input.
- **Procedure**:
  1. Analyze risk-factor contributions for AD and other dementias.
  2. Identify prominent risk factors.
  3. Relate findings to intervention priorities.
- **Metrics**: Risk-factor prominence or attributable burden; exact measures not available from provided input.
- **Expected outcome**: High BMI and High FPG emerge as prominent risk factors.
- **Baselines**: Other risk factors not available from provided input.
- **Dependencies**: none

## E03: Project future AD cases
- **Verifies**: C03, C06
- **Setup**:
  - Data: GBD 2021 historical burden series.
  - Model: Bayesian Age-Period-Cohort techniques.
  - Population: Adults aged 60 years or older; sex-disaggregated outputs implied by the abstract.
- **Procedure**:
  1. Fit BAPC projection model to historical burden data.
  2. Project AD case burden.
  3. Interpret drivers including population growth and aging.
  4. Compare projected burden by sex.
- **Metrics**: Projected AD case burden and directional sex disparity.
- **Expected outcome**: Projected cases rise substantially, with females disproportionately affected.
- **Baselines**: Historical burden trajectory.
- **Dependencies**: E01

## E04: Analyze health inequality across regions
- **Verifies**: C04
- **Setup**:
  - Data: GBD 2021 regional burden estimates.
  - Stratifier: SDI region category, including high-SDI regions.
  - Outcomes: Disease burden metrics named in the abstract.
  - System: Not available from provided input.
- **Procedure**:
  1. Analyze health inequality across regions.
  2. Compare burden levels across SDI strata.
  3. Identify regions with higher burden.
- **Metrics**: Inequality measures and regional burden comparisons; exact metrics not available from provided input.
- **Expected outcome**: Higher burdens are found in high-SDI regions and persistent inequalities are observed.
- **Baselines**: Other SDI strata; exact comparison set not available from provided input.
- **Dependencies**: E01

## E05: Compare actual versus expected pandemic deaths
- **Verifies**: C05
- **Setup**:
  - Data: Observed pandemic-period deaths and expected deaths.
  - Population: Adults aged 60 years or older with AD and other dementias.
  - System: Not available from provided input.
- **Procedure**:
  1. Estimate expected deaths during the pandemic period.
  2. Compare actual deaths against expected deaths.
  3. Stratify or compare results by region.
- **Metrics**: Excess mortality and regional heterogeneity.
- **Expected outcome**: Mortality impact is uneven across regions.
- **Baselines**: Expected deaths during the pandemic.
- **Dependencies**: E01

## E06: Assess temporal trends and burden drivers
- **Verifies**: C06, C03
- **Setup**:
  - Data: GBD 2021 time series.
  - Trend measure: EAPC.
  - Decomposition factors: Population growth, aging, and epidemiological shifts.
  - System: Joinpoint Regression model, StataMP 18, and R 4.4.1 are named; details not available from provided input.
- **Procedure**:
  1. Calculate temporal trends for burden rates.
  2. Use decomposition analysis to examine population growth, aging, and epidemiological shifts.
  3. Relate historical trends to projected future burden.
- **Metrics**: EAPC, rate trend direction, and decomposed contributions.
- **Expected outcome**: Incidence rates decline over the historical window while overall burden remains substantial and future burden rises.
- **Baselines**: Earlier years in the historical series.
- **Dependencies**: E01
