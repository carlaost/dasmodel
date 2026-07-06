# Environment

This is an **analytical secondary-data study** (systematic review + network meta-analysis). No
primary data were collected, no model was trained, and no analysis code or accessioned dataset was
released by the authors.

- **Language/runtime**: R (Foundation for Statistical Computing). Version not specified in paper.
- **Framework**: `netmeta` R package, version **4.5.2** — random-effects frequentist network
  meta-analysis (§2.5).
- **Hardware**: n/a (statistical synthesis of summary data).
- **Data sources**: extracted summary diagnostic-accuracy statistics (AUC ± 95% CI, sensitivity,
  specificity) from 18 publications / 24 independent datasets / 4,736 participants. Underlying
  cohorts (access controlled/by-request via their consortia):
  - BioFINDER-1 (Janelidze et al., 2023), BioFINDER-PC (Palmqvist et al., 2024)
  - WRAP (Ashton et al., 2024a), SPIN (Ashton et al., 2024b)
  - Clarity AD (Devanarayan et al., 2025), ALZAN (Lehmann et al., 2025)
  - ALFA+ (Mila-Aloma et al., 2022), TRIAD (Benedet et al., 2026)
  - MCSA (Mielke et al., 2022), Coimbra (Silva-Spinola et al., 2026)
  - Huashan and Greater Bay Area (GBA) — Han Chinese cohorts (source studies not separately cited)
  - ADNI, BioFINDER-2, and TRIAD are additionally named as screened overlapping cohorts in the abstract/§2.3.
  See `data/dataset.md` for provenance and access details.
- **Key dependencies**: R + netmeta 4.5.2. CI reconstruction from SE / sample size + p-values where
  95% CIs were unreported (§2.4). Where a comparison AUC was not directly reported it was combined via
  indirect NMA evidence.
- **Protocols**: PRISMA-DTA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses for
  Diagnostic Test Accuracy). Prospectively registered on PROSPERO, **CRD420261327845**. Risk of bias
  assessed with QUADAS-2 (Supplementary Table S1).
- **Random seeds**: n/a (frequentist NMA; no stochastic sampling reported).

## Code availability
No Code Availability statement; no GitHub/GitLab/Zenodo/OSF/Dryad repository is referenced in the
article or found via web search (sources.yaml, verified). As a summary-data NMA, no analysis code was
released — hence no `src/execution/` code files (a `.py` stub reconstructed from the prose methodology
would only duplicate `logic/solution/study_design.md`).

## Data availability (verbatim, page 8)
"The original contributions presented in the study are included in the article/Supplementary
material, further inquiries can be directed to the corresponding author."
