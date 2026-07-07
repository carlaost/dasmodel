# Dataset — GBD 2021 (Alzheimer's disease, global + SDI/region/country strata)

## Provenance
- **Name**: Global Burden of Disease (GBD) Study 2021.
- **Producer**: Institute for Health Metrics and Evaluation (IHME).
- **Access point**: Global Health Data Exchange (GHDx) platform's GBD tool.
- **Access type**: OPEN / publicly available (stated in Methods §2.1, p.2, and Ethics statement,
  p.4; verified in `sources.yaml`).
- **Verified**: yes, at the level of the main-article Table 1 and Figures 1–4 (rendered and
  transcribed directly from the provided PDF). The per-country and per-region ASR/EAPC values
  quoted in Results §§3.3–3.5 running text are **not independently re-verifiable** from the
  provided input, because they are sourced (per the paper's own citations) from Supplementary
  Tables/Figures that were not supplied — see `evidence/README.md`.

## Selection / scope for this study
- **Cause**: Alzheimer's disease (ICD-9 290.0–290.9; ICD-10 G30.0–G30.9).
- **Locations**: Global; 5 SDI-tier aggregates (High, High-middle, Middle, Low-middle, Low); 18
  GBD regions (see `logic/solution/constraints.md` C-f for the 3 standard GBD regions not shown in
  the main text); individual countries (only extremal countries are named in running text — full
  country-level table not provided).
- **Years**: 1990–2021 (observed, from GBD); 2022–2030 (projected, via GAM).
- **Stratifiers**: sex (male, female, combined); SDI (continuous, and 5-category + 2-threshold
  groupings); GBD region; country; continent (for the SDI-correlation analysis).

## Variables extracted / computed
- Age-standardized incidence rate (ASIR), age-standardized death rate (ASDR), age-standardized
  DALY rate — each with a 95% uncertainty interval (UI), for 1990–2021 (observed) and, via GAM,
  2022–2030 (projected).
- EAPC (%) with 95% CI, computed separately for 1990–2021 and 2022–2030, at every stratification
  level above.
- SDI value per country/continent (composite of per-capita income, education, fertility rate).
- Mann-Whitney U test statistics/p-values for SDI-threshold group comparisons (exact values
  deferred to Supplementary Figures 2–4, not provided).
- R² / p-value for per-continent SDI-vs-burden linear regression / Pearson correlation (values
  given for ASIR, ASDR, DALY ASR — see claim C08).

## Case definition (as inherited from GBD 2021)
- ICD-9: 290.0 (senile dementia), 290.1 (presenile dementia), 290.9 (unspecified senile dementia).
- ICD-10: G30.0 (early onset), G30.1 (late onset), G30.8 (other), G30.9 (unspecified).
- AD-specific GBD 2021 modeling newly incorporated incidence data (81 data points, 60 locations)
  and excluded USA claims data from dementia modeling. See `logic/solution/study_design.md` §2.

## Licensing / ethics
- Aggregate, de-identified modeled estimates; publicly available; no ethical approval or informed
  consent required per the authors (Ethics statement, p.4).
- Article open access under CC BY 4.0.

## Size / granularity
- The main article surfaces: Global + 5 SDI tiers + 18 GBD regions × 3 measures (ASIR, ASDR, DALY)
  × 2 time windows (EAPC) in Table 1; 2030 ASR by the same 24 location rows in Figure 2; 1990–2030
  annual ASR trajectories by SDI tier in Figure 3; 2030 sex-percentage splits by the same 24
  location rows in Figure 4. Country-level EAPC/ASR values (Cyprus, Serbia, Bahrain, Armenia, etc.)
  are given only for the extremes, in running text — the full per-country table is not part of the
  provided input (Supplementary Tables 6–9, Supplementary Figure 1).

## Preprocessing
- No preprocessing by the authors beyond selection/extraction, GAM projection, EAPC computation,
  and descriptive plotting; all underlying data cleaning, modeling, and uncertainty propagation are
  performed upstream by IHME (CODEm, DisMod-MR 2.1; see `logic/solution/study_design.md` §2). No
  separate `preprocessing.md` is warranted.
