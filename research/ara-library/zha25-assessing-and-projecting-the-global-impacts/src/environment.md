# Environment

This is a **secondary, analytical study** — no primary experiment, no released code. The authors
did not publish an analysis code repository (confirmed: no code-availability statement in the
article; verified `sources.yaml` `code: []`, no GitHub/GitLab/Zenodo/OSF repository found in the
paper text). The environment below is what the paper states plus the verified data source.

- **Language/runtime**: Not specified in paper. (The GAM, EAPC, and Mann-Whitney computations are
  described mathematically in Methods §2.2 but no software/package/language is named — e.g., no
  mention of R, Python, Stata, or specific GAM packages such as `mgcv`.)
- **Framework**: Not specified in paper. Underlying estimation is IHME's GBD pipeline software
  (CODEm; DisMod-MR 2.1), run by IHME, not by the authors.
- **Hardware**: Not specified in paper.
- **Data sources**:
  - **Global Burden of Disease (GBD) Study 2021**, accessed via the **Global Health Data Exchange
    (GHDx)** platform's GBD tool — the sole data source. Covers 371 diseases/injuries and 87 risk
    factors across 204 countries/territories.
  - **Access type**: OPEN (publicly available); the paper states "this study is based on a
    publicly available database and does not require ethical approval" (Methods §2.1, p.2) and
    reiterates this in the Ethics statement (p.4).
  - **Identifier**: GBD 2021 (cause = Alzheimer's disease; ICD-9 290.0–290.9 / ICD-10 G30.0–G30.9;
    locations = Global, 5 SDI tiers, 18 GBD regions, individual countries; years 1990–2021
    observed, 2022–2030 projected).
  - No NCT clinical-trial identifier, no PROSPERO registration, no data-accession numbers apply
    (this is not a trial or a systematic review; verified `sources.yaml` `clinical_trials: []`).
  - See [../data/dataset.md](../data/dataset.md) for full provenance.
- **Key dependencies**: GBD 2021 GHDx exports. Upstream: CODEm, DisMod-MR 2.1 (IHME). Downstream
  (this paper's own analysis): GAM fitting, EAPC computation, Mann-Whitney U test, Pearson
  correlation / linear regression — package/library not named.
- **Protocols**: No preregistration/PROSPERO. Ethics: "Ethical approval was not required for the
  studies involving humans because the data is publicly available... Written informed consent for
  participation was not required" (Ethics statement, p.4). Uses only publicly available,
  aggregate GBD estimates.
- **Random seeds**: Not specified in paper.
- **Funding**: "This study was supported by Shuyun Li Famous Doctor Workshop in Ningbo" (Funding,
  p.4). No role of the GBD/Gates Foundation funding chain is discussed by the authors.
- **Identifiers**: DOI 10.3389/fpubh.2024.1453489. Received 25 June 2024; accepted 26 December
  2024; published 15 January 2025. Open access under CC BY 4.0 (© 2025 Zhang, Chai and Wang).
- **Supplementary material**: The article references Supplementary Tables 1–9 and Supplementary
  Figures 1–5 (per-country/region breakdowns, SDI-threshold group figures, correlation figures).
  These were **not part of the provided input** (only `paper.pdf`, the 11-page main article, was
  supplied) — see `evidence/README.md` for the full accounting of what could and could not be
  verified.
