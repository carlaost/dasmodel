# Environment

This is an industry-sponsored phase 3 clinical trial. There is no released software/code repository; the "environment" is the trial infrastructure, statistical software, and imaging pipeline.

- **Language/runtime**: SAS version 9.4 (SAS Institute Inc.) — all statistical analyses and the power/sample-size simulation.
- **Framework**: n/a (statistical analysis in SAS). Analysis models: logistic regression (co-primary), ANCOVA (6-mo mean change), MMRM (12/18-mo mean change; biomarkers), Kaplan–Meier + log-rank (time-to-event).
- **Hardware**: n/a (clinical trial). Imaging: florbetapir F18 and flortaucipir F18 PET; safety MRI (centrally read).
- **Data sources**:
  - Trial registration: NCT05108922 (ClinicalTrials.gov) — TRAILBLAZER-ALZ 4, Phase 3, COMPLETED, sponsor Eli Lilly and Company; 148 participants, 31 US sites; has posted results. Hosts full inclusion/exclusion criteria, safety assessments, and additional statistical detail (ClinicalTrials.gov/study/NCT05108922). Verified via sources.yaml.
  - Individual participant data: available on request via Vivli (www.vivli.org), access = request/controlled — see `data/dataset.md`.
- **Key dependencies**: florbetapir PET quantification pipeline (Joshi et al. 2015; motion correction → template alignment → cortical SUVR with whole-cerebellar reference → Centiloid conversion, Navitsky et al. 2018); flortaucipir PET (MUBADA SUVR) for tau subpopulation.
- **Protocols**: Study protocol + statistical analysis plan approved by an independent ethics committee/IRB at each of 31 US sites; conducted per Declaration of Helsinki and ICH-GCP; written informed consent obtained. Trial initiated 2021-09-24, completed 2023-09-19 (76 weeks). Prospectively registered (NCT05108922).
- **Random seeds**: Not applicable / not specified (randomization 1:1, stratified by amyloid level and APOE ε4 status; simulation for power run in SAS v9.4).

## Code availability
No Code Availability statement and no software/code repository (GitHub/GitLab/Zenodo/OSF) exists for this trial (expected for an industry-sponsored clinical trial; verified via sources.yaml). Consequently there is no `src/execution/` or `src/configs/` — no concrete code artifact exists to capture, and the analysis methodology is described in prose in `logic/solution/study_design.md` (Rule 14: prose-only method is not re-encoded as a stub).
