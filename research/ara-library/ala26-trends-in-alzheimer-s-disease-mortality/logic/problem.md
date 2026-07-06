# Problem Specification

> Grounding: abstract-only. Observations below are limited to what the abstract states. Where the
> full text would ordinarily supply detail (exact ICD codes, Joinpoint APC/AAPC values, per-year
> tables), the entry reads "Not available from provided input (no full text)".

## Observations

### O1: AD is a large and rising cause of death among the oldest old
- **Statement**: 2,355,233 deaths with Alzheimer's disease listed as the underlying cause of death occurred among older adults (aged ≥75) in the US from 1999 to 2020.
- **Evidence**: Abstract, Results (CDC WONDER Multiple Cause of Death database).
- **Implication**: AD mortality in the ≥75 population is large enough to support fine-grained stratified trend analysis.

### O2: A substantial subset of AD deaths co-occur with metabolic syndrome conditions
- **Statement**: Of those, 444,488 deaths were related to metabolic syndrome-related conditions (≈18.9% of the 2,355,233; ARA-computed ratio, see note).
- **Evidence**: Abstract, Results.
- **Implication**: Metabolic syndrome comorbidity is a common and quantifiable feature of AD mortality, warranting its own trend analysis. *(ARA-computed: 444,488 / 2,355,233 = 0.18872 ≈ 18.9%. This percentage is derived by the ARA, not stated in the abstract.)*

### O3: AD-with-metabolic-syndrome mortality rose sharply over two decades
- **Statement**: The age-adjusted mortality rate (AAMR) rose from 36.48 in 1999 to 157.93 in 2020 (per 100,000).
- **Evidence**: Abstract, Results.
- **Implication**: An approximately 4.3-fold increase in AAMR over 21 years signals either a genuine rise in burden and/or improved ascertainment/coding of AD and comorbidities on death certificates.

### O4: Persistent sex disparity
- **Statement**: Women consistently had higher AAMRs than men (females: 107.79; males: 79.02).
- **Evidence**: Abstract, Results.
- **Implication**: Sex is an axis of disparity even after age adjustment.

### O5: Racial/ethnic disparity, with a shared early-period peak
- **Statement**: Non-Hispanic African Americans had the highest AAMR among racial groups (121.65); from 1999 to the early-to-mid 2000s all races showed a sharp peak in mortality rates.
- **Evidence**: Abstract, Results.
- **Implication**: Racial disparities coexist with a common temporal artifact/inflection in the early period.

### O6: Marked geographic disparity across states
- **Statement**: Mississippi fell in the top 90th percentile of AAMR while Massachusetts fell in the lower 10th percentile.
- **Evidence**: Abstract, Results.
- **Implication**: Place of residence is strongly associated with AD+metabolic-syndrome mortality, implicating access and structural factors.

## Gaps

### G1: Comorbidity-specific AD mortality trends were not characterized nationally
- **Statement**: Prior national mortality surveillance treats AD broadly; the specific trend of AD deaths co-occurring with metabolic syndrome conditions among the oldest old was not quantified.
- **Caused by**: O1, O2 — the burden is large but its metabolic-syndrome subset was under-described.
- **Existing attempts**: General AD mortality reports and metabolic-syndrome epidemiology, treated separately (Not available from provided input which specific priors — no full text).
- **Why they fail**: They do not isolate the intersection nor its demographic/geographic disparities across 1999–2020.

### G2: Disparities within this intersection were not mapped
- **Statement**: Sex, racial/ethnic, and state-level disparities specific to AD-with-metabolic-syndrome mortality were unquantified.
- **Caused by**: O4, O5, O6.
- **Existing attempts**: Not available from provided input (no full text).
- **Why they fail**: Not available from provided input (no full text).

## Key Insight
- **Insight**: AD and metabolic syndrome share pathophysiology and risk determinants, so the death-certificate record can be mined as a large natural dataset to jointly track their co-mortality and its disparities using age-adjusted rates and Joinpoint trend detection.
- **Derived from**: O1–O6.
- **Enables**: A stratified national trend analysis (E01–E05) that surfaces temporal inflections and equity gaps actionable for intervention targeting.

## Assumptions
- A1: Death-certificate cause-of-death coding (underlying AD + metabolic syndrome-related conditions) reliably identifies the target deaths across 1999–2020.
- A2: Age adjustment (per 100,000) renders rates comparable across years and demographic strata.
- A3: The ≥75 age restriction captures the population of interest for AD mortality.
- A4: Metabolic syndrome-related conditions are operationalized via a defined set of codes/conditions (exact definition: Not available from provided input — no full text).
