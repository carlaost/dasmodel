# Claims

> Grounding: abstract-only. Every load-bearing number below is copied verbatim from the article
> abstract (file: `research/data/lib/ala26-trends-in-alzheimer-s-disease-mortality/metadata.md`,
> "## Abstract"). No full text was available, so `**Sources**` cite the abstract line and are tagged
> `[result]` (values the study's analysis produced and reports). Full-text confirmation is `[pending]`
> where noted. No values are carried from memory.

## C01: Metabolic-syndrome subset of AD mortality
- **Statement**: Among 2,355,233 deaths with Alzheimer's disease as the underlying cause among US adults aged ≥75 during 1999–2020, 444,488 were related to metabolic syndrome-related conditions.
- **Status**: supported
- **Falsification criteria**: A re-query of CDC WONDER (underlying cause = AD, ages ≥75, 1999–2020) yielding total or metabolic-syndrome-related death counts materially different from 2,355,233 and 444,488 respectively.
- **Proof**: [E01]
- **Evidence basis**: The abstract reports both counts directly for the study window and population.
- **Interpretation**: The metabolic-syndrome-related subset is roughly one-fifth of AD-underlying-cause deaths in this age group (ARA-computed 444,488/2,355,233 ≈ 18.9%; not stated verbatim in the abstract).
- **Dependencies**: none
- **Sources**:
  - 2,355,233 ← metadata.md §Abstract «There were 2,355,233 deaths documented with AD listed as the underlying cause of death among older adults (aged ≥75)» [result]
  - 444,488 ← metadata.md §Abstract «out of which 444,488 deaths were related to metabolic syndrome-related conditions from 1999 to 2020» [result]
- **Tags**: mortality-count, comorbidity, CDC-WONDER, denominator

## C02: Rising age-adjusted mortality rate over the study window
- **Statement**: The age-adjusted mortality rate (AAMR) for AD with metabolic syndrome-related conditions among adults ≥75 rose from 36.48 per 100,000 in 1999 to 157.93 per 100,000 in 2020.
- **Status**: supported
- **Falsification criteria**: Joinpoint-analyzed CDC WONDER AAMRs for endpoints 1999 and 2020 differing materially from 36.48 and 157.93, or a non-increasing overall trend.
- **Proof**: [E02]
- **Evidence basis**: The abstract states the two endpoint AAMR values and describes the rise as "substantial".
- **Interpretation**: An ≈4.3-fold rise (ARA-computed 157.93/36.48 ≈ 4.33) over 21 years; the abstract does not report the annual percent change (APC) or joinpoint years (Not available — no full text).
- **Dependencies**: C01
- **Sources**:
  - 36.48 ← metadata.md §Abstract «The AAMR rose substantially from 36.48 in 1999 to 157.93 in 2020» [result]
  - 157.93 ← metadata.md §Abstract «The AAMR rose substantially from 36.48 in 1999 to 157.93 in 2020» [result]
- **Tags**: AAMR, temporal-trend, joinpoint

## C03: Sex disparity (women > men)
- **Statement**: Women had consistently higher AAMRs than men over the study period (females: 107.79 per 100,000; males: 79.02 per 100,000).
- **Status**: supported
- **Falsification criteria**: Sex-stratified CDC WONDER AAMRs showing males ≥ females, or values materially different from 107.79 and 79.02.
- **Proof**: [E03]
- **Evidence basis**: The abstract reports the two sex-stratified AAMRs and states women's rates were consistently higher.
- **Interpretation**: The female excess (ARA-computed difference 107.79 − 79.02 = 28.77 per 100,000) is stated as consistent across the window; the abstract does not specify whether these are period-wide averages or a specific year (Not available — no full text).
- **Dependencies**: C02
- **Sources**:
  - 107.79 ← metadata.md §Abstract «Women consistently had higher AAMRs than males (females: 107.79, males: 79.02)» [result]
  - 79.02 ← metadata.md §Abstract «Women consistently had higher AAMRs than males (females: 107.79, males: 79.02)» [result]
- **Tags**: sex-disparity, AAMR

## C04: Racial disparity — highest AAMR in Non-Hispanic African Americans
- **Statement**: Non-Hispanic African Americans had the highest AAMR among all racial groups (121.65 per 100,000).
- **Status**: supported
- **Falsification criteria**: Race-stratified CDC WONDER AAMRs in which another racial group exceeds Non-Hispanic African Americans, or a Non-Hispanic African American AAMR materially different from 121.65.
- **Proof**: [E03]
- **Evidence basis**: The abstract reports 121.65 as the highest among racial groups.
- **Interpretation**: AAMRs for the other racial/ethnic groups are not stated in the abstract (Not available — no full text).
- **Dependencies**: C02
- **Sources**:
  - 121.65 ← metadata.md §Abstract «Non-Hispanic African Americans (121.65) showed the highest mortality rates among all racial groups» [result]
- **Tags**: racial-disparity, AAMR

## C05: Early-period peak shared across races
- **Statement**: From 1999 to the early-to-mid 2000s, all racial groups exhibited a sharp peak in mortality rates.
- **Status**: supported
- **Falsification criteria**: Race-stratified Joinpoint trends lacking an early-period peak/inflection for one or more racial groups over 1999–mid-2000s.
- **Proof**: [E02, E03]
- **Evidence basis**: The abstract explicitly describes a sharp early-period peak common to all races.
- **Interpretation**: The abstract gives no peak year, magnitude, or APC for the peak segment (Not available — no full text); the qualitative "sharp peak" is the only stated detail.
- **Dependencies**: C02, C04
- **Sources**:
  - 1999 to early-to-mid 2000s peak ← metadata.md §Abstract «from 1999 to the early to mid-2000s, all races highlighted a sharp peak in mortality rates» [result]
- **Tags**: temporal-trend, racial-disparity, joinpoint

## C06: Geographic disparity across states
- **Statement**: There was striking geographic variation in AAMR, with Mississippi in the top 90th percentile and Massachusetts in the lower 10th percentile of states.
- **Status**: supported
- **Falsification criteria**: State-level CDC WONDER AAMRs placing Mississippi outside the top decile or Massachusetts outside the bottom decile.
- **Proof**: [E04]
- **Evidence basis**: The abstract names Mississippi (top 90th percentile) and Massachusetts (lower 10th percentile) as the extremes.
- **Interpretation**: Only the two extreme states are named in the abstract; the full state ranking and regional breakdown are Not available from provided input (no full text).
- **Dependencies**: C02
- **Sources**:
  - Mississippi top 90th percentile ← metadata.md §Abstract «with Mississippi in the top 90th percentile and Massachusetts in the lower 10th percentile» [result]
  - Massachusetts lower 10th percentile ← metadata.md §Abstract «with Mississippi in the top 90th percentile and Massachusetts in the lower 10th percentile» [result]
- **Tags**: geographic-disparity, AAMR, state-level
