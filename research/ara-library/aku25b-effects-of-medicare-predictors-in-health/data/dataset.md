# Dataset

## US Medicare administrative claims — 5% nationally representative sample (1991–2020)
- **Provenance / custodian**: Centers for Medicare & Medicaid Services (CMS), accessed through
  ResDAC (Research Data Assistance Center).
- **Access**: **controlled / restricted** — requires a CMS data-use agreement (DUA); not publicly
  downloadable. No public repository or accession identifier. (Verified in sources.yaml.)
- **Sample**: nationally representative **5% sample** of the US Medicare population.
- **Time span**: 1991–2020 (2000–2020 used for cohort formation and follow-up; 1991–2000 used for
  look-back).
- **Unit / structure**: individual longitudinal trajectories with identified initial/final age of
  follow-up, dates of death and disease onset, and basic demographic characteristics.
- **Cohorts derived**: baseline ages 70, 75, 80, 85 (Table 1). Baseline counts per subpopulation
  range from thousands (Native American: 8719 at age 70) to > 1.4 million (White: 1,457,165 at age
  70). See evidence/tables/table1.md for full counts.
- **Outcome variable**: AD onset within a 5-year follow-up, ascertained algorithmically from claims
  (ref 18); death treated as independent censoring.
- **Exclusions**: prevalent AD/ADRD at baseline; > 20% of study time in Medicare Advantage
  (fee-for-service restriction).
- **Ethics / consent**: IRB-approved (University Health System IRB); Declaration of Helsinki (1975,
  rev. 1983); informed consent not required (secondary de-identified claims analysis).
- **External reference data (not the analysis cohort)**: CDC WONDER (ref 19) and the Human Mortality
  Database (ref 20) are cited for baseline-population survival curves.

## Variables
- **Disparity indicators** (binary `r`): Black, Hispanic, Native American, Asian (vs White); female
  (vs male); stroke-belt residence (vs non–stroke-belt), per the six disparity pairs.
- **Low income**: Medicare/Medicaid dual eligibility (binary).
- **Disease predictors** (binary, time-independent at baseline; ascertainment per ref 18):
  - Retained (6): cerebrovascular disease (stroke), arterial hypertension, diabetes mellitus, renal
    disease, heart failure, depression.
  - Screened out (4, no significant contribution across cohorts): rheumatic heart disease, systemic
    hypotension, chronic liver disease, traumatic brain injury.
  - The full 10-disease candidate list is in Table S1 (supporting information; not in the provided
    main-text PDF).
- Baseline prevalences of the retained predictors by subpopulation and age are tabulated in
  evidence/tables/table2.md.

## Preprocessing / feature construction
- Cohort assembly by baseline age with a 1991–2000 look-back window.
- Binary disease-presence flags at baseline via published Medicare ascertainment algorithms (ref
  18); no continuous covariates reported.
- First-stage predictor screening (drop 4 non-contributing conditions).
- No further normalization/QC steps are reported (Not specified in paper beyond the above).
