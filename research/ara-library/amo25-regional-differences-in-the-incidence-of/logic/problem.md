# Problem Specification

## Observations

### O1: South Carolina's older-adult population is growing rapidly
- **Statement**: The proportion of South Carolina residents aged 65+ increased from 14% to 19% (2021), with about one in five residents being 65 or older.
- **Evidence**: Introduction, citing ref (10) (Live Healthy South Carolina, 2024).
- **Implication**: ADRD burden — which "mostly affect[s] older adults" and has no cure — is set to rise as the population ages.

### O2: ADRD burden is large and rising, and is underdiagnosed
- **Statement**: In the US a new dementia case is diagnosed every ~65 s (globally every ~3 s); ADRD is underdiagnosed in America, most common among minority older adults, and a large proportion of Americans with ADRD do not know they have it.
- **Evidence**: Introduction, citing refs (6, 7, 8, 9).
- **Implication**: Registry-based incidence surveillance is needed but will underestimate true burden.

### O3: Place and social vulnerability plausibly modify ADRD risk
- **Statement**: Where one resides may influence the likelihood of being diagnosed with ADRD; high social vulnerability index is linked to inequitable access to health/essential services. The Pee Dee PHR has the highest social vulnerability index in SC (poverty, transport, housing) and is predominantly rural.
- **Evidence**: Introduction & Discussion, citing refs (10, 11, 13, 14, 26).
- **Implication**: Incidence should be characterized at a regional (PHR) resolution to expose disparities.

### O4: SCADR is the oldest and most comprehensive US dementia registry, but regional incidence had never been characterized
- **Statement**: The South Carolina Alzheimer's Disease Registry (SCADR) has collected ADRD data since 1988 and is described as the oldest and most comprehensive registry in the US; yet ADRD incidence by SC public health region had not been estimated.
- **Evidence**: Introduction & Discussion ("This study is the first to characterize the incidence of ADRD by PHRs in South Carolina using the SCADR data").
- **Implication**: A tractable data source exists to fill the regional-incidence gap.

## Gaps

### G1: No characterization of ADRD incidence by South Carolina public health region
- **Statement**: The regional (PHR-level) incidence of ADRD — overall and by dementia subtype — was unknown for South Carolina.
- **Caused by**: O1, O3, O4
- **Existing attempts**: National/state estimates (CDC, Alzheimer's Association reports) and diagnostic-intensity studies (ref 11) exist, but not SCADR-based PHR-level incidence.
- **Why they fail**: They do not resolve within-state regional heterogeneity across SC's four PHRs, nor use the SCADR registry.

### G2: Regional disparities and their correlates are not quantified
- **Statement**: Whether ADRD incidence differs significantly across PHRs — and how that relates to rurality/socioeconomic vulnerability — was not established for SC.
- **Caused by**: O3
- **Existing attempts**: Rural–urban diagnostic-prevalence studies elsewhere (refs 38–40); neighborhood-cognition reviews (28).
- **Why they fail**: Not specific to SC PHRs or the SCADR; do not provide age-adjusted incidence rate ratios across these regions.

## Key Insight
- **Insight**: Combining SCADR 2021 incident cases (numerators) with Census-based Annual County Resident Population Estimates (denominators) and modeling counts with Poisson regression using log-population as an offset yields comparable age-adjusted incidence rate ratios across PHRs of very different sizes — turning a case registry into a regional-disparity surveillance instrument.
- **Derived from**: O3, O4
- **Enables**: Statistically testing whether crude and type-specific ADRD incidence differ across the four PHRs and mapping the geography of that difference.

## Assumptions
- A1: SCADR 2021 incident cases (physician/neurologist ICD-10-CM diagnoses) validly represent new ADRD diagnoses in SC for 2021.
- A2: ACRPE / 2020-census-based population estimates are valid denominators and standard population for age adjustment.
- A3: Records with missing county/zip (n = 3,910) can be treated in sensitivity analyses (proportional redistribution; extreme-case reassignment) without invalidating the primary regional estimates.
- A4: Diagnosed-and-registered incidence approximates the pattern of true incidence, acknowledging underreporting/underdiagnosis (see constraints.md).
