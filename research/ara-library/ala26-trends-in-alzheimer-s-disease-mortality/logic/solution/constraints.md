# Constraints — Boundary Conditions, Assumptions, Limitations

> Grounding: abstract-only. The constraints below combine what the abstract states (population,
> window, data source, method) with the well-known limitations of death-certificate / CDC WONDER
> ecological trend studies. Limitations the full text would state explicitly are marked as inferred
> or "Not available from provided input (no full text)".

## Boundary Conditions
- **Population**: US resident deaths, adults aged ≥75 only. Findings do not generalize to younger AD decedents.
- **Time window**: 1999–2020 (ICD-10 era). Pre-1999 and post-2020 trends are out of scope.
- **Outcome definition**: AD as the *underlying* cause of death, intersected with metabolic syndrome-related conditions. Deaths where AD is only a contributing cause are excluded from the primary cohort.
- **Geography**: United States, state- and region-level resolution (county-level suppression rules of CDC WONDER apply; details Not available — no full text).
- **Rate metric**: Age-adjusted mortality rate per 100,000.

## Assumptions
- A1: Death-certificate coding accurately and consistently captures both AD (underlying cause) and metabolic syndrome-related conditions across 1999–2020. (See L1 — coding validity.)
- A2: The chosen standard population makes AAMRs comparable across years and strata. (Standard-population year Not available — no full text.)
- A3: The metabolic syndrome-related condition set is defined a priori and applied uniformly. (Exact code set Not available — no full text.)
- A4: CDC WONDER counts are complete for the study population (national death registration is near-complete).

## Known / Inferred Limitations
- **L1 — Death-certificate coding validity (inferred)**: AD is known to be under- and variably reported on death certificates; secular changes in coding practice and diagnostic awareness can inflate apparent trends. The ≈4.3-fold AAMR rise (C02) may partly reflect ascertainment change rather than true incidence.
- **L2 — Ecological / no individual-level inference (inferred)**: Rates are population-level; no individual causal link between metabolic syndrome and AD mortality can be drawn.
- **L3 — Comorbidity operationalization (inferred)**: "Metabolic syndrome-related conditions" on death certificates is a proxy; certificates do not record a formal metabolic-syndrome diagnosis, so the 444,488 subset (C01) depends on the chosen code set.
- **L4 — Residual confounding (inferred)**: Age adjustment does not remove confounding by comorbidity burden, socioeconomic status, or access, which likely drive the sex, racial, and geographic disparities (C03–C06).
- **L5 — Suppression and small counts (inferred)**: CDC WONDER suppresses cells with fewer than 10 deaths and flags unreliable rates; some strata (e.g., smaller racial groups, low-population states) may be affected. Details Not available — no full text.
- **L6 — Full method detail unavailable (grounding limitation)**: APC/AAPC values, joinpoint years, standard-population reference, exact ICD-10 codes, place-of-death category results, and any confidence intervals are Not available from provided input (no full text).
