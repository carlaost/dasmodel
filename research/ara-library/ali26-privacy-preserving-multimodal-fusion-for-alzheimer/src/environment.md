# Environment

> Grounding: abstract-only. Runtime, framework, and hardware details are not stated in the abstract
> and no code repository was found, so most fields are unavailable. Data-source access is verified
> from sources.yaml.

- **Language/runtime**: Not available from provided input (no full text; no code repository located)
- **Framework**: Not available from provided input (no full text). The method is a deep-learning
  transformer (Swin-UNet + LoRA), implying a Python deep-learning stack, but no version is stated.
- **Hardware**: Not available from provided input (no full text)
- **Data sources**:
  - **Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort** — identifier `ADNI`; repository:
    LONI Image and Data Archive (adni.loni.usc.edu); **access: controlled / request-based** (data-use
    agreement required); verified in sources.yaml (`verified: true`). Used as a stratified four-client
    federation. No new dataset or accession was released by the authors.
  - Modalities drawn from / aligned to ADNI: 3D structural MRI; IBSI-compliant radiomics; cognitive
    assessments; FDA-cleared plasma biomarkers.
- **Key dependencies**: Not available from provided input (no full text)
- **Protocols**: Federated learning across four clients with model-update exchange only (no raw-data
  sharing); simulated domain-shift evaluation. Exact protocol (rounds, local epochs, aggregation)
  Not available from provided input (no full text). No preregistration or clinical-trial registration
  (no NCT id; verified in sources.yaml `clinical_trials: []`).
- **Random seeds**: Not available from provided input (no full text)

## Code availability
No code repository (GitHub/GitLab/Zenodo/OSF) was located via web search (sources.yaml `code: []`).
A GitHub user "marwabentaleb" surfaced during discovery but is a different person (Marwa BEN TALEB
ALI, unrelated repos) and does not host this work. No `src/execution/` stubs are provided because
the method is available only in prose from the abstract — reconstructing code would fabricate APIs
(Rule 14).

## Data/code availability statement
No explicit Data Availability or Code Availability statement was found in the available metadata
(Elsevier landing, Europe PMC, PubMed).
