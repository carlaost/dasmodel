# Environment

> Grounding: abstract-only. No analysis code was released for this study, and the full text
> (Methods/Supplement) was unavailable at compile time. Software versions, assay platforms, staging
> algorithm, and seeds are "Not available from provided input (no full text)."

- **Language/runtime**: Analytical — no public code released. Analyses relied on mass-spectrometry
  plasma biomarker measurements and standard statistical modeling (per metadata); exact
  language/tooling not available from provided input.
- **Framework**: Not available from provided input (no full text; no code repository found).
- **Hardware**: n/a (biomarker assays + statistical analysis; no compute detail available).
- **Data sources**:
  - **BioFINDER-2** — primary cohort, 872 participants. Identifier: ClinicalTrials.gov **NCT03174938**
    ("The Swedish BioFINDER 2 Study"). Repository/governance: Swedish BioFINDER study (biofinder.se);
    sponsor Skåne University Hospital, collaborator Lund University. Access: **request** (controlled;
    available to qualified researchers on reasonable request). Verified.
  - **Knight ADRC** — independent validation cohort, 156 participants. Repository: Knight Alzheimer
    Disease Research Center, Washington University in St. Louis. Identifier: none. Access:
    **request** (controlled). Verified.
  - Data Sharing Statement: article Supplement 2 (`jamaneurol-e261405-s002.pdf`).
- **Key dependencies**: Not available from provided input (no full text).
- **Protocols**: Observational cohort study; index tests = plasma %p-tau217 and eMTBR-tau243;
  reference standard = amyloid/tau PET biological staging. Detailed analysis protocol /
  preregistration: Not available from provided input.
- **Random seeds**: Not available from provided input (no full text).

## Code availability
No public analysis-code repository (GitHub/GitLab/Zenodo/OSF) was found for this paper (`sources.yaml`
`code: []`). Because the source provides no concrete code and no printed pseudocode/equations, no
`src/execution/` stub is created (per compiler Rule 14: prose-only methods are not re-encoded as
code). The method is described in `logic/solution/study_design.md`.
