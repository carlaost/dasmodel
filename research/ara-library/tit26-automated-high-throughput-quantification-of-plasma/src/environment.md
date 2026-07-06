# Environment

- **Language/runtime**: Analytical — no programming runtime released. Statistical analysis performed in commercial GUI/statistical software (no scripts published).
- **Statistical software**:
  - SPSS v29.0 (IBM) — all analyses except method comparison
  - MedCalc v15.6.1 (Mariakerke, Belgium) — Passing–Bablok regression and Bland–Altman analysis
- **Laboratory instruments**:
  - Roche cobas pro e801 Elecsys immunochemistry analyser (ECLIA) — plasma p-tau181, p-tau217, APOE-ε4
  - Fujirebio LUMIPULSE G1200 (CLEIA) — plasma p-tau217, Aβ42, Aβ40; and CSF Aβ42, Aβ42/40, p-tau181, total tau
  - Roche cobas pro c703 — plasma creatinine (Jaffe reaction); eGFR via CKD-EPI 2009
- **Hardware (compute)**: n/a (no computational modelling)
- **Data sources**:
  - **Cognitive Centre Ghent University (CCUG) biobank** (Ghent University Hospital) — the sole data source. Prospective biobank (initiated 2021) of blood + CSF + clinical/neuropsychological/imaging data from memory-clinic patients. n = 187 included (AD 103 / non-AD 84; + 16 discordant excluded). **Access: request-only** — per the article's Data Availability statement (verbatim): "The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request." Verified in sources.yaml (access = request, verified = true). No public dataset accession (GEO/SRA/EGA/PRIDE/Dryad/figshare) exists for this single-cohort study.
- **Key reagents (RUO lots)**: Elecsys Phospho-Tau (181P) lot# 99065201; Elecsys Phospho-Tau (217P) lot# 990760; Elecsys APOE-ε4 lot# 99065401; Lumipulse G pTau217 lot# 5086; Lumipulse G β-Amyloid 1-40-N V&V lot# 5; Lumipulse G β-Amyloid 1-42-N V&V lot# 8. QC: PreciControl pT181p and Phospho-Tau (217P) PreciControl (Roche RUO).
- **Protocols**: CLSI EP15-A3 (precision verification); Declaration of Helsinki; ethics ONZ-2024-0422 (Ghent University Hospital). CSF reference cut-offs per reference-lab standards.
- **Code availability**: No analysis code was released. No Code Availability statement in the article; targeted search (per sources.yaml) found no associated GitHub/GitLab/OSF/Zenodo repository. Because the method is described in prose and executed in commercial statistical software (no repo, no printed pseudocode), no `src/execution/` code stub is created — doing so would fabricate an API the source does not provide (compiler Rule 14).
- **Clinical-trial registration**: None. Observational biobank study; no NCT/EudraCT number reported.
- **Random seeds**: n/a (no stochastic computation).
