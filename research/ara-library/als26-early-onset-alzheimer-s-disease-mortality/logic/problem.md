# Problem Specification

> Abstract-only compile. Observations and gaps below are grounded in the published abstract
> (`metadata.md`). Detail beyond the abstract (e.g. per-year rates, subgroup denominators) is
> "Not available from provided input (no full text)".

## Observations

### O1: EOAD mortality has risen steeply over 2015-2024
- **Statement**: Reported EOAD age-adjusted mortality rate rose from 0.14 to 2.59 per 1,000,000 population between 2015 and 2024, with an annual percent change of +19.96%.
- **Evidence**: Abstract, Results (CDC WONDER, ICD-10-CM G30.0; Joinpoint regression).
- **Implication**: Motivates a formal trend/disparity characterization of EOAD mortality at the population level.

### O2: EOAD deaths show a female predominance
- **Statement**: Among 4890 EOAD-related deaths, 63.7% were female; females had higher mortality than males (RR = 1.50, 95% CI 1.40 to 1.59).
- **Evidence**: Abstract, Results.
- **Implication**: Signals a sex disparity requiring quantification and interpretation.

### O3: Racial/ethnic and regional concentration of mortality
- **Statement**: Non-Hispanic White individuals and residents of the Midwest exhibited the highest EOAD mortality rates.
- **Evidence**: Abstract, Results.
- **Implication**: Points to structural disparities in diagnosis, coding, and access to care.

### O4: Age-at-death distribution centers in the 65-74 band
- **Statement**: Mean age at death was 69.8 years, with the greatest number of deaths occurring between ages 65 and 74.
- **Evidence**: Abstract, Results.
- **Implication**: Characterizes the population dying with an EOAD underlying-cause code (note: G30.0 codes *onset* before 65, not age at death).

### O5: EOAD rose faster than late-onset AD
- **Statement**: The increase in late-onset Alzheimer's disease (G30.1) mortality was lower than that of EOAD.
- **Evidence**: Abstract, Results (sensitivity analysis).
- **Implication**: Suggests the EOAD rise is not merely a reflection of a general AD-coding increase.

## Gaps

### G1: Sparse population-level data on EOAD mortality trends and disparities
- **Statement**: "Population-level data on trends and disparities in early-onset Alzheimer's disease (EOAD) mortality are limited." (abstract, Background)
- **Caused by**: EOAD's relative rarity, historical under-recognition, and lack of dedicated surveillance relative to late-onset AD (O1, O5).
- **Existing attempts**: Not available from provided input (no full text) — the abstract cites no prior population-level EOAD-mortality series.
- **Why they fail**: Not available from provided input (no full text).

### G2: Unknown magnitude and structure of demographic disparities in EOAD mortality
- **Statement**: The extent of sex, racial/ethnic, regional, and age disparities in EOAD mortality is not established at the population level.
- **Caused by**: O2, O3, O4.
- **Existing attempts**: Not available from provided input (no full text).
- **Why they fail**: Not available from provided input (no full text).

## Key Insight
- **Insight**: National death-certificate data (CDC WONDER) coded by ICD-10-CM G30.0 can be mined to produce the first population-level characterization of EOAD mortality trends and disparities, with G30.1 (late-onset) as an internal comparator to distinguish EOAD-specific signal from generic AD-coding drift.
- **Derived from**: O1, O5, G1.
- **Enables**: A design combining age-adjusted rates + Joinpoint trend analysis + rate-ratio disparity comparisons within a single administrative data source.

## Assumptions
- A1: Underlying-cause-of-death coding with ICD-10-CM G30.0 validly identifies EOAD deaths in CDC WONDER.
- A2: CDC WONDER age-adjusted mortality rates are comparable across years and subgroups (consistent standard population).
- A3: Observed increases reflect (at least in part) real and/or recognition/coding changes rather than pure random variation — Joinpoint regression is used to test trend significance.
- A4: G30.1 (late-onset AD) serves as a valid comparator for the same data source and period.
