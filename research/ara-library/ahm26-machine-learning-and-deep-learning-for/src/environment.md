# Environment

- **Language/runtime**: Not applicable — this is a **narrative literature survey**. It runs no code
  and produces no computational artifact. No programming language, framework, or runtime is used or
  reported.
- **Framework**: None. The paper prints no algorithms, pseudocode, or equations of its own; there is
  therefore **no `src/execution/` code** (per ARA rules, prose-only methods are not re-encoded as
  stubs — the method/taxonomy content lives in `logic/solution/`).
- **Hardware**: n/a (no experiments, no training, no inference).
- **Data sources**: The survey releases **no new dataset**. It discusses public benchmark neuroimaging
  cohorts belonging to the reviewed literature. These are recorded here as the data sources the field
  (and this survey) relies on. Access details verified in `sources.yaml` (first-class grounded input;
  not re-verified here):
  - **ADNI — Alzheimer's Disease Neuroimaging Initiative**. Identifier: `ADNI`. Repository: LONI IDA
    (adni.loni.usc.edu). Access: **request** (registration / data-use agreement). Role: the dominant
    benchmark; provides longitudinal/cross-sectional imaging, cognitive, demographic, and biomarker
    data across diagnostic groups.
  - **OASIS / OASIS-3 — Open Access Series of Imaging Studies**. Identifier: `OASIS-3`. Repository:
    OASIS Brains (oasis-brains.org). Access: **request**. Role: broadens the evaluation landscape;
    structural imaging + clinical/cognitive data (used e.g. by Castellano et al., 2024).
  - **AIBL — Australian Imaging, Biomarker & Lifestyle Study**. Identifier: `AIBL`. Repository: LONI
    IDA / aibl.org.au. Access: **request**. Role: multimodal, biomarker-informed modeling.
  - Modalities discussed generically: structural MRI (T1/T2), FDG-PET, amyloid PET, plus non-imaging
    variables (age, sex, education, APOE genetic risk, cognitive scores, biomarkers).
- **Key dependencies**: None (no software stack).
- **Protocols**: Narrative survey; **no** preregistration / systematic-review protocol (explicitly not
  a systematic review; no PROSPERO id). No search-string or PRISMA flow reported.
- **Random seeds**: n/a.
- **Code / model availability**: None. No GitHub/GitLab/Zenodo/OSF/figshare repository is associated
  with the paper (per `sources.yaml`: `code: []`). No formal Code or Data Availability statement.
- **Clinical trials**: None. No NCT or PROSPERO registration in abstract or full text
  (`sources.yaml`: `clinical_trials: []`).
