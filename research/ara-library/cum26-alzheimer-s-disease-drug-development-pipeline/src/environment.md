# Environment

This is an **analytical / registry-census study**; there is no experimental apparatus, no trained
model, and no released code repository associated with the paper. Reproducibility rests on the data
source, the query/curation pipeline, and the classification ontology.

- **Language/runtime**: Analytical — no released software. Data pulled via the ClinicalTrials.gov
  API and stored/queried in a **PostgreSQL** relational database.
- **Framework**: Rule-based programming plus manual expert curation for trial identification and
  characterization (UNLV Clinical Trial Observatory / Cleveland Clinic Laboratory of Network
  Medicine). No public code artifact was found for this specific paper (`sources.yaml` code: []).
- **Hardware**: n/a.
- **Data sources** (access type + identifiers; grounded in `sources.yaml`, verified):
  - **ClinicalTrials.gov AD trial registry** — primary source, **open** access, identifier
    `clinicaltrials.gov`; accessed via API on Index Date 2026-01-01; >30 key JSON fields parsed;
    158 drugs across 192 AD trials. Verified.
  - **alzpipeline.com / UNLV Clinical Trial Observatory** — **open** access, identifier
    `alzpipeline.com`; summary pipeline data (per Data Availability Statement). Verified live.
  - **Alzheimer's Disease Data Initiative — AD Workbench (Gates Ventures)** — **request** access,
    no identifier; planned data deposit. Not yet verified.
  - **DrugBank** (https://go.drugbank.com/) — reference used to classify agents as repurposed vs novel.
  - **ALZFORUM** and the published literature — supplementary sources for mechanism-of-action / CADRO
    assignment.
  - **Flagship clinical trials (verified subset of ~190 cited NCTs)**: NCT05026866 (donanemab,
    TRAILBLAZER-ALZ 3), NCT03887455 (lecanemab, Clarity AD), NCT04468659 (lecanemab, AHEAD 3-45),
    NCT05463731 (remternetug, TRAILRUNNER-ALZ 1), NCT04777396 (semaglutide, EVOKE), NCT05531526
    (AR1001, Polaris-AD), NCT06709014 (buntanetap/Posiphen), NCT05564169 (masitinib, AB21004).
    All ClinicalTrials.gov, access open, verified. See `data/dataset.md` and `logic/related_work.md`.
- **Key dependencies**: ClinicalTrials.gov API; DrugBank; the Common Alzheimer's Disease Research
  Ontology (CADRO).
- **Protocols**: Fixed Index Date (1 January 2026); inclusion/exclusion and classification rules per
  `logic/solution/study_design.md`; methodology continuous with the annual review series (2024, 2025).
- **Random seeds**: n/a (deterministic census, not a stochastic computation).
- **Consent/ethics**: Not applicable — all data derive from an anonymized publicly available registry;
  no individual participant-level data.
