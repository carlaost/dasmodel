# Constraints — assumptions, boundary conditions, and limitations

## Boundary conditions
- **Cause**: "Alzheimer's disease" as a single GBD cause (ICD-9 290.0–290.9; ICD-10 G30.0–G30.9);
  no subtype separation.
- **Time**: Historical window 1990–2021 (observed GBD estimates); projected window 2022–2030
  (GAM forecast). 2030 is the reference year for cross-sectional country/region comparisons.
- **Geography**: Global; 5 SDI-tier aggregates; 18 GBD regions (see completeness note below); and
  individual countries (numbers/lists deferred to unreleased Supplementary Tables/Figures for
  region-level ASR extremes and all country-level statistics).
- **Metrics**: ASIR, ASDR, and age-standardized DALY rate; EAPC (%) for both time windows.

## Assumptions (see also logic/problem.md A1–A5)
- GBD 2021 estimates faithfully represent true AD incidence/mortality/DALY burden within their
  published uncertainty.
- GAM-projected 2022–2030 ASRs, extrapolated from the 1990–2021 series, are a valid basis for
  forecasting; no explicit external shock (new therapy approval, pandemic effect, etc.) is
  modeled into the projection.
- Age-standardization removes age-structure confounding across locations/time.
- Significance = 95% CI/UI excludes zero (for EAPC) or a stated significant/highly-significant
  p-value (for Mann-Whitney group comparisons).
- SDI adequately summarizes development level for both the 5-category grouping and the continuous
  per-continent correlation analysis.

## Known limitations (stated by the authors, Discussion, p.7)
- **L1 — Unequal data availability**: "the accuracy of our estimates may be compromised by unequal
  data availability across countries and regions, particularly in lower SDI areas where
  comprehensive Alzheimer's disease surveillance systems and population-based registries are
  lacking," introducing projection uncertainty.
- **L2 — ICD-based case-definition bias**: reliance on GBD data using ICD codes "may lead to biases
  due to variations in diagnostic criteria and healthcare access," potentially underestimating mild
  or asymptomatic cases.
- **L3 — Unmodeled contextual factors**: "the GBD database does not fully account for
  socio-economic changes, cultural variations, or other contextual factors that may influence the
  burden of Alzheimer's disease," requiring cautious interpretation.

## Additional epistemic caveats (compiler-noted, grounded in the text)

- **C-a — Duplicated female EAPC value across distinct measures**: The global projected
  (2022–2030) female incidence-rate EAPC and female death-rate EAPC are both printed as exactly
  −1.03 (95% CI −1.04, −1.02), even though the corresponding male values differ substantially
  (incidence −1.73 vs. death −2.28). See claim C02.

- **C-b — Two identical (R², p) correlation pairs across different continents/measures**: The
  SDI–ASDR correlation reported for Africa (R²=0.099, p=0.0539) is numerically identical to the
  SDI–DALY correlation reported for America (R²=0.099, p=0.0539), and the SDI–ASIR p-value for
  Africa (p=0.0699) is identical to the SDI–ASIR p-value for America (p=0.0699) despite very
  different R² (0.008 vs. 0.088). See claim C08.

- **C-c — Abstract-vs-body-text precision/rounding mismatches**: Several values are printed at
  different precision or with slightly different rounded bounds in the Abstract vs. the Results
  body text: global death-rate EAPC 2022–2030 upper CI bound is −1.83 in the Abstract vs. −1.82 in
  Results §3.1 (Table 1's own value, −1.8254, rounds to −1.83, matching the Abstract but not the
  body text); Serbia's country DALY EAPC is 9.6416 (95% CI 8.86, 10.4333) in the Abstract vs. 9.64
  (8.85, 10.43) in Results §3.4; Bahrain's country DALY EAPC upper CI bound is −69.70 in the
  Abstract vs. −69.69 in Results §3.4; Armenia's country DALY EAPC is −85.41 in the Abstract vs.
  −85.40 in Results §3.4. All reproduced verbatim in `logic/claims.md`.

- **C-d — Methodology citations mismatched to their cited content**: In-text citations supporting
  the ASR formula, EAPC formula, GAM description, and Mann-Whitney U test/formula (Methods §2.2)
  resolve, in the reference list, to GBD sub-studies of unrelated diseases (hepatitis B, cancer,
  alcohol, lower respiratory infection, type-2 diabetes) or, in one case, a journal erratum notice
  rather than a research paper. Full detail in `logic/related_work.md` ("Citation-footprint
  anomaly"). This does not affect the numerical results but affects how much independent
  methodological grounding the paper's own citations provide.

- **C-e — Apparent cross-measure magnitude inconsistency in the 1990/2030 global point values**:
  Results §3.1 states the 1990 global DALY-rate ASR as 644.16, the 1990 death-rate ASR as
  14,775.89, and the 1990 incidence-rate ASR as 4,483.76 (and analogously for 2030: 299.92,
  7,210.92, 2,199.67). Under the standard convention that a DALY rate (which aggregates both
  years-of-life-lost-to-death and years-lived-with-disability) is larger than the corresponding
  death rate for the same cause and year, a death-rate value roughly 23× the DALY-rate value in
  the same year is difficult to reconcile; the paper does not explain the units or provide a
  cross-check. Reproduced verbatim in claim C01 without correction.

- **C-f — Table 1 / Figures 1–4 cover 18 of the standard 21 GBD regions**: Table 1 and Figures 1–3
  list Andean Latin America, Australasia, Caribbean, Central Asia, Central Europe, Central Latin
  America, Central Sub-Saharan Africa, East Asia, Eastern Europe, Eastern Sub-Saharan Africa,
  High-income Asia Pacific, High-income North America, Oceania, Southeast Asia, Southern Latin
  America, Southern Sub-Saharan Africa, Tropical Latin America, and Western Europe — 18 regions.
  The standard GBD regional taxonomy additionally includes North Africa and Middle East, South
  Asia, and Western Sub-Saharan Africa, none of which appear in the provided main-text table or
  figures. Not explained by the authors; not part of the provided input's Supplementary material
  either, so it cannot be determined whether these three regions were omitted from the analysis or
  merely from the main-text display.

- **C-g — Figure 4's stacked bars lack a printed color legend**: Figure 4 ("Sex Percentage for
  Incidence/Deaths/DALYs in 2030") shows green/red stacked bars per location but the rendered page
  does not include a legend identifying which color is male vs. female (unlike Figures 1 and 2,
  which do carry legends). The sex assignment of each color is therefore not verifiable from the
  provided PDF; see `evidence/figures/figure4.md`.

- **C-h — Interpretive vs. evidential**: All mechanism-level explanations (estrogen's protective
  effect, healthcare-seeking behavior, cognitive reserve, urbanization/lifestyle drivers, cultural
  attitudes toward aging) are drawn from the Discussion's narrative framing, not tested by this
  study's own data, and are kept in claim `Interpretation` fields, not `Statement`s.

- **C-i — No causal inference**: All findings are descriptive/associational or extrapolative
  (GAM forecast); the study projects burden trends, not causes of the projected changes.

- **C-j — Eastern Europe's sex-split bar is internally inconsistent across Figure 4's panels**: In
  Figure 4 Panel A (Incidence) and Panel B (Deaths), the Eastern Europe bar renders as 100% one
  color with no visible second-color segment at all — the only location in either panel with no
  visible split. In Panel C (DALYs), the same location's bar shows a visible ≈15–20% second-color
  segment, unlike its own all-one-color appearance in Panels A/B. Not addressed by the authors; not
  resolvable from the provided input (no legend identifies the colors either — see C-g). See
  `evidence/figures/figure4.md`.
