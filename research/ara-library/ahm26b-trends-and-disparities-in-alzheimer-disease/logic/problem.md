# Problem Specification

> Grounding: abstract-only. Observations below are drawn from the abstract's BACKGROUND, METHODS,
> and RESULTS sections. Numbers are quoted verbatim from the abstract; supporting detail that would
> normally come from the full Introduction/Discussion is marked "Not available from provided input
> (no full text)."

## Observations

### O1: AD is a leading US cause of death but its mortality epidemiology is underexplored
- **Statement**: "Alzheimer disease (AD) is a leading cause of mortality in the United States; yet,
  population-level mortality trends and disparities remain underexplored."
- **Evidence**: Abstract, BACKGROUND.
- **Implication**: Motivates a nationwide, long-horizon (1999–2020) descriptive mortality analysis.

### O2: A very large AD death burden accumulated over 1999–2020
- **Statement**: "From 1999 to 2020, 6,697,209 deaths were attributed to AD (AAMR: 90.727)."
- **Evidence**: Abstract, RESULTS.
- **Implication**: Establishes the scale of the public health burden being characterized.

### O3: AD-related mortality increased significantly over the study period
- **Statement**: "Mortality rates increased significantly (AAPC: 3.18)." (Average Annual Percent
  Change of 3.18, from joinpoint regression.)
- **Evidence**: Abstract, RESULTS.
- **Implication**: The burden is not static — it is rising, sharpening the need for intervention.

### O4: Mortality differs by sex, race/ethnicity, and age
- **Statement**: Females had higher AAMR (94.31) than males (83.23). By race/ethnicity, AAMR ranked
  non-Hispanic Black (94.53) > non-Hispanic White (93.73) > non-Hispanic American Indian (66.80) >
  Hispanic (66.33) > non-Hispanic Asian (46.16). Adults aged 85+ had the highest CMR (3574.928).
- **Evidence**: Abstract, RESULTS.
- **Implication**: Demographic disparities exist and are candidate targets for interventions.

### O5: Mortality differs by geography (urbanization, region, state)
- **Statement**: Rural AAMR (95.080) exceeded urban AAMR (89.772). Midwest had the highest regional
  AAMR (96.131); Northeast the lowest (78.564). State AAMRs ranged widely — e.g. South Carolina
  (119.789) and Tennessee (113.624) high vs New York (64.16) and Florida (68.677) low.
- **Evidence**: Abstract, RESULTS.
- **Implication**: Geographic disparities suggest differences in access, diagnosis, and reporting.

## Gaps

### G1: Population-level AD mortality trends and disparities are underexplored
- **Statement**: Despite AD being a leading cause of death, comprehensive nationwide trend and
  disparity characterization was lacking.
- **Caused by**: O1.
- **Existing attempts**: Not available from provided input (no full text — Introduction not accessible).
- **Why they fail**: Not available from provided input (no full text).

### G2: Which demographic and geographic subgroups bear disproportionate AD mortality is unclear
- **Statement**: Absent stratified national estimates, targeting of interventions cannot be prioritized.
- **Caused by**: O1, O4, O5.
- **Existing attempts**: Not available from provided input (no full text).
- **Why they fail**: Not available from provided input (no full text).

## Key Insight
- **Insight**: A large, standardized public-domain death registry (CDC WONDER), queried with a
  defined AD ICD-10 code set over a 22-year window, can quantify both the temporal trend
  (via joinpoint regression) and the cross-sectional disparities of AD mortality at national scale.
- **Derived from**: O1, O2.
- **Enables**: Simultaneous trend estimation (AAPC) and multi-axis disparity stratification (sex,
  race/ethnicity, age, urbanization, region, state).

## Assumptions
- A1: ICD-10 codes F01, F03, G30, and G31.1 adequately capture AD-related deaths on death certificates.
- A2: Restricting to individuals aged 45+ is appropriate for AD-related mortality analysis.
- A3: Death-certificate cause-of-death coding in CDC WONDER is sufficiently accurate/consistent for
  1999–2020 trend comparison.
- A4: Age-adjustment (standard population) makes AAMRs comparable across groups and years.
