# Claims

> Abstract-only compile. Every load-bearing number is grounded in the published abstract, which is
> stored verbatim in `metadata.md` (line 13, the single "## Abstract" paragraph) and `metadata.json`
> (`abstract` field). Because no full text was available, the abstract is the primary source; values
> are tagged `[result]` (study-reported outputs). Per-subgroup denominators, confidence intervals
> beyond the sex RR, and per-year rates are "Not available from provided input (no full text)".

## C01: EOAD mortality rose steeply, 2015-2024
- **Statement**: The reported age-adjusted EOAD mortality rate (per 1,000,000 population) increased from 0.14 in 2015 to 2.59 in 2024, an annual percent change of +19.96%.
- **Status**: supported
- **Falsification criteria**: Re-extracting CDC WONDER G30.0 AAMRs for 2015 and 2024 yields materially different endpoint values, or a Joinpoint fit yields an APC that is not +19.96% (and not statistically significant), for the same query specification.
- **Proof**: [E01]
- **Evidence basis**: Abstract states endpoint AAMRs and the APC directly. No per-year series or Joinpoint CI/segment count is available from the abstract.
- **Interpretation**: A ~19-20%/yr rise is dramatic and, combined with C06, is read by the authors as reflecting improving recognition/coding of EOAD as much as (or more than) true incidence change — the abstract frames it as "reported" mortality.
- **Dependencies**: none
- **Sources**:
  - 0.14 ← `metadata.md:13` «mortality increased from 0.14 to 2.59 per 1,000,000 between 2015 and 2024» [result]
  - 2.59 ← `metadata.md:13` «mortality increased from 0.14 to 2.59 per 1,000,000 between 2015 and 2024» [result]
  - +19.96% ← `metadata.md:13` «(annual percent change: +19.96%)» [result]
- **Tags**: mortality-trend, joinpoint, AAMR, EOAD

## C02: Females had higher EOAD mortality than males
- **Statement**: Females experienced higher EOAD age-adjusted mortality than males, with a rate ratio of 1.50 (95% CI 1.40 to 1.59); females accounted for 63.7% of the 4890 EOAD-related deaths.
- **Status**: supported
- **Falsification criteria**: The female-to-male AAMR rate ratio computed from the same CDC WONDER extraction falls outside 1.40-1.59, or the 95% CI includes 1.0 (no sex difference), or the female death share differs materially from 63.7%.
- **Proof**: [E02]
- **Evidence basis**: Abstract reports the RR, its 95% CI, total deaths (4890), and female percentage (63.7%) directly.
- **Interpretation**: The authors read the female excess as part of a broader disparity pattern; whether it reflects true incidence, differential survival, or diagnostic/coding differences cannot be resolved from the abstract.
- **Dependencies**: none
- **Sources**:
  - 4890 ← `metadata.md:13` «Among 4890 EOAD-related deaths (63.7% female)» [result]
  - 63.7% ← `metadata.md:13` «Among 4890 EOAD-related deaths (63.7% female)» [result]
  - RR = 1.50 ← `metadata.md:13` «1.50, 95% CI: 1.40 to 1.59» [result] (source renders the preceding "RR =" with thin-space characters; value quoted from the ", 1.50, 95% CI…" segment to preserve verbatim match)
  - 95% CI 1.40 to 1.59 ← `metadata.md:13` «1.50, 95% CI: 1.40 to 1.59» [result]
- **Tags**: sex-disparity, rate-ratio, EOAD

## C03: Non-Hispanic White individuals had the highest EOAD mortality
- **Statement**: Among racial/ethnic groups, Non-Hispanic White individuals exhibited the highest EOAD age-adjusted mortality rates.
- **Status**: supported
- **Falsification criteria**: A CDC WONDER extraction by race/ethnicity shows a group other than Non-Hispanic White with the highest EOAD AAMR over 2015-2024.
- **Proof**: [E03]
- **Evidence basis**: Abstract states "Non-Hispanic White individuals ... exhibited the highest mortality rates." Exact per-group AAMRs and RRs are not available from the abstract.
- **Interpretation**: The authors frame racial patterning as evidence of inequity in EOAD diagnosis/coding and access to care; a higher *reported* rate can reflect greater access to diagnosis rather than higher true burden.
- **Dependencies**: none
- **Sources**:
  - Non-Hispanic White highest ← `metadata.md:13` «Non-Hispanic White individuals and residents of the Midwest exhibited the highest mortality rates» [result]
- **Tags**: racial-disparity, race-ethnicity, EOAD

## C04: Midwest residents had the highest EOAD mortality
- **Statement**: Among US census regions, residents of the Midwest exhibited the highest EOAD age-adjusted mortality rates.
- **Status**: supported
- **Falsification criteria**: A CDC WONDER extraction by census region shows a region other than the Midwest with the highest EOAD AAMR over 2015-2024.
- **Proof**: [E04]
- **Evidence basis**: Abstract states "residents of the Midwest exhibited the highest mortality rates." Exact per-region AAMRs are not available from the abstract.
- **Interpretation**: Regional patterning is read as a geographic disparity; the abstract does not decompose urban/rural or state-level drivers.
- **Dependencies**: none
- **Sources**:
  - Midwest highest ← `metadata.md:13` «Non-Hispanic White individuals and residents of the Midwest exhibited the highest mortality rates» [result]
- **Tags**: regional-disparity, geography, EOAD

## C05: Deaths concentrated at ages 65-74; mean age at death 69.8 years
- **Statement**: The mean age at death for EOAD-coded decedents was 69.8 years, with the greatest number of deaths occurring in the 65-74 age band.
- **Status**: supported
- **Falsification criteria**: A CDC WONDER extraction yields a mean age at death materially different from 69.8 years, or a modal age band other than 65-74.
- **Proof**: [E05]
- **Evidence basis**: Abstract reports the mean age at death (69.8) and the modal age band (65-74) directly.
- **Interpretation**: Because ICD-10-CM G30.0 codes *early onset* (onset before age 65) rather than early death, a mean age at death near 70 is internally consistent (death follows onset by years); the ARA reproduces the abstract's figures without adjustment (Rule 7/honesty).
- **Dependencies**: none
- **Sources**:
  - 69.8 years ← `metadata.md:13` «The mean age at death was 69.8 years» [result]
  - 65 and 74 ← `metadata.md:13` «the greatest number of deaths occurring between the ages of 65 and 74 years» [result]
- **Tags**: age-at-death, age-distribution, EOAD

## C06: EOAD mortality rose faster than late-onset AD mortality
- **Statement**: Over 2015-2024, the increase in late-onset Alzheimer's disease (ICD-10-CM G30.1) mortality was lower than the increase in EOAD (G30.0) mortality.
- **Status**: supported
- **Falsification criteria**: A parallel CDC WONDER extraction for G30.1 shows an APC/increase equal to or greater than that for G30.0 over the same period.
- **Proof**: [E06]
- **Evidence basis**: Abstract states, in a sensitivity analysis, that the LOAD increase "was lower than that of EOAD." No numeric LOAD APC is given in the abstract.
- **Interpretation**: The authors use this contrast to argue the EOAD rise is EOAD-specific rather than an artifact of general AD-coding growth; the magnitude of the difference is not quantified in the abstract.
- **Dependencies**: [C01]
- **Sources**:
  - LOAD increase lower than EOAD ← `metadata.md:13` «the increase in late-onset Alzheimer's disease mortality was lower than that of EOAD» [result]
- **Tags**: sensitivity-analysis, LOAD, comparison, EOAD
