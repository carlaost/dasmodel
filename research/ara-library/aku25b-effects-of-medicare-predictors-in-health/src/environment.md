# Environment

- **Language/runtime**: Not specified in paper. The analysis is statistical (survival modeling +
  algebraic decomposition + bootstrap); no software stack, package, or version is reported.
- **Framework**: Not specified in paper. Method relies on Cox proportional-hazards estimation and
  the closed-form PAF decomposition (Eqs. 1–6); any Cox-capable statistical environment (e.g., R
  `survival`, SAS, Stata) could implement it, but the paper names none.
- **Hardware**: n/a (not reported; observational secondary-data analysis).
- **Data sources**:
  - **US Medicare administrative claims — nationally representative 5% sample, 1991–2020.**
    - Repository / custodian: Centers for Medicare & Medicaid Services (CMS), accessed via ResDAC
      (Research Data Assistance Center).
    - Access type: **controlled / restricted** — requires a CMS data-use agreement (DUA); not
      publicly downloadable. No public accession/repository identifier exists.
    - Identifier: none (no NCT, PROSPERO, or public accession — this is not a trial or systematic
      review). Source: sources.yaml (verified) + metadata.md.
    - Content used: identified individual trajectories (baseline/final age of follow-up, dates of
      death and disease onset, demographics), binary disease indicators via ascertainment
      algorithms (ref 18), and Medicare/Medicaid dual-eligibility status.
    - External reference datasets cited for population survival curves: CDC WONDER (ref 19) and the
      Human Mortality Database (ref 20).
- **Key dependencies**: Not specified in paper.
- **Protocols**: Analysis protocol described in §2 (cohort construction, exclusions, univariable +
  multivariable Cox models, PAF decomposition, bootstrap, sensitivity analyses). No preregistration
  (PROSPERO/OSF) reported. IRB approval: University Health System Institutional Review Board;
  Declaration of Helsinki (1975, rev. 1983); informed consent not required.
- **Random seeds**: Not specified in paper (bootstrap uses 100 resamples with replacement; seed not
  reported).
- **Code availability**: No Code Availability statement and no public repository
  (GitHub/GitLab/Zenodo/OSF) located (sources.yaml, verified).
