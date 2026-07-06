# Claims

> Grounding: abstract-only. Every load-bearing number below is quoted verbatim from the paper's
> abstract (metadata.json / metadata.md RESULTS section). `**Sources**` entries cite `[abstract]`
> with the matched line, since the full text (and its numbered tables/figures) was not accessible.
> `Proof` references are directional analysis plans in [experiments.md](experiments.md); no
> independent evidence objects could be extracted from the paywalled full text.

## C01: AD-related mortality rose significantly over 1999–2020
- **Statement**: US Alzheimer disease-related age-adjusted mortality increased significantly across
  1999–2020, with an Average Annual Percent Change (AAPC) of 3.18.
- **Status**: supported
- **Falsification criteria**: A joinpoint regression of AD AAMR over 1999–2020 on CDC WONDER data
  yielding a non-significant or negative AAPC, or an AAPC materially different from 3.18.
- **Proof**: [E01]
- **Evidence basis**: Abstract states "Mortality rates increased significantly (AAPC: 3.18)."
- **Interpretation**: A sustained upward trend; the abstract does not report joinpoint segment
  breakpoints or per-segment APCs (not available without full text).
- **Dependencies**: none
- **Tags**: trend, joinpoint, AAPC, mortality
- **Sources**:
  - AAPC 3.18 ← metadata.md RESULTS «Mortality rates increased significantly (AAPC: 3.18).» [result]

## C02: A large AD death burden accumulated, with overall AAMR 90.727
- **Statement**: From 1999 to 2020, 6,697,209 deaths were attributed to AD in the US, corresponding
  to an overall age-adjusted mortality rate of 90.727 per 100,000 population.
- **Status**: supported
- **Falsification criteria**: A CDC WONDER query with the same ICD-10 codes (F01, F03, G30, G31.1),
  ages 45+, 1999–2020 returning a materially different death count or overall AAMR.
- **Proof**: [E02]
- **Evidence basis**: Abstract states the death count and overall AAMR directly.
- **Interpretation**: Establishes the aggregate burden; per-100,000 denominator is the US population
  (age-standardized).
- **Dependencies**: none
- **Tags**: burden, AAMR, death-count
- **Sources**:
  - 6,697,209 deaths ← metadata.md RESULTS «From 1999 to 2020, 6,697,209 deaths were attributed to AD (AAMR: 90.727).» [result]
  - AAMR 90.727 ← metadata.md RESULTS «From 1999 to 2020, 6,697,209 deaths were attributed to AD (AAMR: 90.727).» [result]

## C03: Females had higher AD-related AAMR than males
- **Statement**: Females had a higher AD-related age-adjusted mortality rate (94.31) than males
  (83.23).
- **Status**: supported
- **Falsification criteria**: Sex-stratified AD AAMRs showing males ≥ females, or values materially
  different from 94.31 (female) and 83.23 (male).
- **Proof**: [E03]
- **Evidence basis**: Abstract states "Females had higher AAMRs (94.31) than males (83.23)."
- **Interpretation**: The abstract reports rates, not whether the female excess persists after
  accounting for greater female longevity (not available without full text).
- **Dependencies**: none
- **Tags**: disparity, sex
- **Sources**:
  - Female AAMR 94.31 ← metadata.md RESULTS «Females had higher AAMRs (94.31) than males (83.23).» [result]
  - Male AAMR 83.23 ← metadata.md RESULTS «Females had higher AAMRs (94.31) than males (83.23).» [result]

## C04: AD-related AAMR varied by race/ethnicity, highest in non-Hispanic Black individuals
- **Statement**: By race/ethnicity, AD-related AAMR was highest among non-Hispanic Black individuals
  (94.53), followed by non-Hispanic White (93.73), non-Hispanic American Indian (66.80), Hispanic
  (66.33), and lowest among non-Hispanic Asian individuals (46.16).
- **Status**: supported
- **Falsification criteria**: Race/ethnicity-stratified AD AAMRs producing a different ordering, or
  values materially different from those listed.
- **Proof**: [E03]
- **Evidence basis**: Abstract lists the five race/ethnicity AAMRs and their rank order.
- **Interpretation**: Descriptive disparity; the abstract does not adjust for socioeconomic factors,
  access, or differential diagnosis/reporting (not available without full text).
- **Dependencies**: none
- **Tags**: disparity, race, ethnicity
- **Sources**:
  - NH Black 94.53, NH White 93.73, NH American Indian 66.80, Hispanic 66.33, NH Asian 46.16 ← metadata.md RESULTS «Non-Hispanic Black individuals had the highest AAMR (94.53), followed by non-Hispanic White (93.73), non-Hispanic American Indian (66.80), Hispanic (66.33), and non-Hispanic Asian individuals (46.16).» [result]

## C05: Mortality burden concentrated in the oldest age group (85+)
- **Statement**: Individuals aged 85 years and older had the highest crude mortality rate (CMR) for
  AD, 3574.928 per 100,000.
- **Status**: supported
- **Falsification criteria**: Age-stratified CMRs showing a younger group exceeding the 85+ group,
  or an 85+ CMR materially different from 3574.928.
- **Proof**: [E03]
- **Evidence basis**: Abstract states "Individuals aged 85 years and older had the highest CMR
  (3574.928)."
- **Interpretation**: Consistent with AD as an age-related disease; this is a crude (not
  age-adjusted) rate, appropriate for a single narrow age band.
- **Dependencies**: none
- **Tags**: disparity, age, CMR
- **Sources**:
  - 85+ CMR 3574.928 ← metadata.md RESULTS «Individuals aged 85 years and older had the highest CMR (3574.928).» [result]

## C06: Rural areas had higher AD-related AAMR than urban areas
- **Statement**: Rural areas had a higher AD-related AAMR (95.080) than urban areas (89.772).
- **Status**: supported
- **Falsification criteria**: Urbanization-stratified AD AAMRs showing urban ≥ rural, or values
  materially different from 95.080 (rural) and 89.772 (urban).
- **Proof**: [E04]
- **Evidence basis**: Abstract states "Rural areas had higher AAMRs (95.080) than urban areas
  (89.772)."
- **Interpretation**: Suggests rural access/diagnostic differences; the abstract does not report the
  urbanization classification scheme (not available without full text).
- **Dependencies**: none
- **Tags**: disparity, urbanization, geography
- **Sources**:
  - Rural AAMR 95.080, Urban AAMR 89.772 ← metadata.md RESULTS «Rural areas had higher AAMRs (95.080) than urban areas (89.772).» [result]

## C07: AD-related AAMR varied by census region, highest in Midwest, lowest in Northeast
- **Statement**: Among census regions, the Midwest had the highest AD-related AAMR (96.131) and the
  Northeast had the lowest (78.564).
- **Status**: supported
- **Falsification criteria**: Region-stratified AD AAMRs showing a different highest/lowest region,
  or values materially different from 96.131 (Midwest) and 78.564 (Northeast).
- **Proof**: [E04]
- **Evidence basis**: Abstract states "The Midwest had the highest AAMR (96.131), whereas the
  Northeast had the lowest (78.564)."
- **Interpretation**: The abstract reports only the extreme regions; South and West values are not
  given (not available without full text).
- **Dependencies**: none
- **Tags**: disparity, region, geography
- **Sources**:
  - Midwest AAMR 96.131, Northeast AAMR 78.564 ← metadata.md RESULTS «The Midwest had the highest AAMR (96.131), whereas the Northeast had the lowest (78.564).» [result]

## C08: Substantial state-level variation in AD-related AAMR
- **Statement**: State-level AD-related AAMRs varied substantially, with South Carolina (119.789) and
  Tennessee (113.624) among the highest and New York (64.16) and Florida (68.677) among the lower.
- **Status**: supported
- **Falsification criteria**: State-stratified AD AAMRs showing these states clustered together, or
  values materially different from those listed.
- **Proof**: [E04]
- **Evidence basis**: Abstract states "States such as South Carolina (119.789) and Tennessee
  (113.624) had higher AAMRs compared with New York (64.16) and Florida (68.677)."
- **Interpretation**: The abstract names only four illustrative states; the full state ranking is not
  available without full text.
- **Dependencies**: none
- **Tags**: disparity, state, geography
- **Sources**:
  - SC 119.789, TN 113.624, NY 64.16, FL 68.677 ← metadata.md RESULTS «States such as South Carolina (119.789) and Tennessee (113.624) had higher AAMRs compared with New York (64.16) and Florida (68.677).» [result]
