# Concepts

> Grounding: abstract-only. Definitions of terms explicitly named in the abstract are given at the
> level the abstract supports; standard epidemiological/method definitions are supplied where the
> term is a well-established public-health concept, with any paper-specific parameterization marked
> "Not available from provided input (no full text)."

## Crude Mortality Rate (CMR)
- **Notation**: CMR (per 100,000 population)
- **Definition**: The number of deaths in a population divided by the total population at risk over
  a period, expressed per 100,000. Not adjusted for age structure. In this study, CMRs were
  computed for AD-related deaths among individuals aged 45+ and reported per age band (e.g. the 85+
  band had the highest CMR, 3574.928).
- **Boundary conditions**: Comparable only within a fixed age structure; the paper uses CMR for
  narrow age strata (where age-adjustment is unnecessary) and AAMR for cross-group comparison.
- **Related concepts**: Age-Adjusted Mortality Rate (AAMR), ICD-10 AD coding

## Age-Adjusted Mortality Rate (AAMR)
- **Notation**: AAMR (per 100,000 population)
- **Definition**: A mortality rate standardized to a reference (standard) population's age
  distribution, removing the confounding effect of differing age structures so rates can be compared
  across groups and over time. The overall AD AAMR reported is 90.727; it is the primary comparison
  metric across sex, race/ethnicity, urbanization, region, and state.
- **Boundary conditions**: Requires a standard population; the specific standard (e.g. 2000 US
  standard population) is Not available from provided input (no full text).
- **Related concepts**: Crude Mortality Rate (CMR), Average Annual Percent Change (AAPC)

## Average Annual Percent Change (AAPC)
- **Notation**: AAPC (%)
- **Definition**: A summary measure of trend from joinpoint regression — a weighted average of the
  segment-specific Annual Percent Changes (APCs) over the entire study interval. The reported AAPC
  of 3.18 summarizes the 1999–2020 increase in AD AAMR.
- **Boundary conditions**: Assumes the joinpoint model's log-linear segments; individual joinpoint
  years and segment APCs are Not available from provided input (no full text).
- **Related concepts**: Joinpoint regression, AAMR

## Joinpoint Regression
- **Notation**: —
- **Definition**: A trend-analysis method that fits connected linear segments (on a log scale) to a
  time series of rates and statistically identifies "joinpoints" where the trend changes slope. Used
  here to assess AD mortality trends over 1999–2020 and to derive the AAPC.
- **Boundary conditions**: Number of joinpoints and model-selection settings are Not available from
  provided input (no full text).
- **Related concepts**: AAPC, AAMR

## ICD-10 AD Case Definition
- **Notation**: F01, F03, G30, G31.1
- **Definition**: The set of International Classification of Diseases, 10th revision codes used to
  identify AD-related deaths from death certificates: F01 (vascular dementia), F03 (unspecified
  dementia), G30 (Alzheimer disease), and G31.1 (senile degeneration of brain, not elsewhere
  classified). Applied to decedents aged 45+.
- **Boundary conditions**: Whether these were underlying-cause-only or multiple-cause matches is Not
  available from provided input (no full text); note the code set is broader than G30 alone,
  including dementia codes.
- **Related concepts**: CDC WONDER Multiple Cause of Death database, CMR, AAMR

## CDC WONDER Multiple Cause of Death database
- **Notation**: —
- **Definition**: A public, online CDC data system (Wide-ranging ONline Data for Epidemiologic
  Research) that provides US mortality data derived from death certificates, queryable by
  cause-of-death codes, demographics, and geography. It is the sole data source for this study.
- **Boundary conditions**: Open/public access at https://wonder.cdc.gov/. Certain small-cell
  counts are suppressed by CDC; the study covers 1999–2020.
- **Related concepts**: ICD-10 AD Case Definition, Urbanization Classification, Census Region

## Urbanization Classification
- **Notation**: rural vs urban
- **Definition**: A categorization of decedents' counties along a rural–urban continuum, used to
  compare AD AAMR between rural (95.080) and urban (89.772) areas.
- **Boundary conditions**: The specific classification scheme (e.g. NCHS Urban–Rural Classification
  Scheme categories collapsed to rural/urban) is Not available from provided input (no full text).
- **Related concepts**: Census Region, AAMR

## Census Region
- **Notation**: Northeast, Midwest, South, West
- **Definition**: The four US Census Bureau regions used to aggregate states for geographic
  comparison of AD AAMR. Reported extremes: Midwest highest (96.131), Northeast lowest (78.564).
- **Boundary conditions**: South and West region AAMRs are Not available from provided input (no
  full text).
- **Related concepts**: Urbanization Classification, AAMR
