# Environment

This is a **quantitative epidemiological/statistical estimation study** (survey data collection,
factor-analytic classification, regression-based prediction), **not a software engineering project**.
There is no released software repository and no released dataset accession beyond the underlying
SHARE survey infrastructure itself (confirmed by `sources.yaml`: `code: []`, `data: []`,
`clinical_trials: []`). Accordingly there is **no `src/execution/` code stub** — the paper states its
statistical methodology in prose (Stata/Mplus commands are not printed), and this methodology already
lives in `logic/solution/study_design.md` and `logic/solution/classification_method.md`; manufacturing
a code stub from the prose description would only duplicate it and risk fabricating an API the paper
never specifies.

- **Language/runtime**: Not a programming-language codebase. Statistical analyses conducted with:
  - **Stata**, version 14.2
  - **Mplus**, version 8.10
  ("All statistical analyses were conducted with Stata (version 14.2) and Mplus (version 8.10)," p.4,
  Methods.) No analysis scripts/do-files are published with the paper.
- **Framework/methods**:
  - Factor analysis with Full Information Maximum Likelihood (FIML) estimation (Mplus) for the
    five-domain cognition factor scores used in HCAP classification.
  - Regression-based prediction (Hurd et al. 2013 approach, adapted to a multi-country setting) for
    extending classification to the SHARE parent sample.
  - Pairwise (t-test-style) group-difference significance testing for the age/sex/education
    comparisons in Table 4.
  - Multivariate regression for the comorbidity/lifestyle associations in Figure 1.
- **Hardware**: Not specified in paper (survey-based statistical analysis; no GPU/compute
  infrastructure described).
- **Data sources**:
  - **SHARE (Survey of Health, Ageing and Retirement in Europe)** — Wave 9 parent study (data
    collection October 2021–September 2022), 28 units (27 European countries + Israel). "Data for the
    Survey of Health, Ageing and Retirement in Europe is available for the scientific community at
    https://share-eric.eu/data/" (p.8, Data availability).
  - **SHARE-HCAP** — validation subsample drawn from 5 of the 28 SHARE units (Czech Republic,
    France, Germany, Denmark, Italy), data collected May–November 2022. Distributed as part of the
    same SHARE data-access infrastructure (per the paper's single Data availability statement; no
    separate accession is given for SHARE-HCAP specifically).
  - No other external dataset is used; comorbidity/lifestyle variables (Figure 1) are drawn from
    self-reported doctor's diagnoses recorded across SHARE Waves 1 through 9.
- **Key dependencies**: Not applicable (no software package/library dependencies stated beyond the
  named Stata/Mplus versions above).
- **Protocols**:
  - Written informed consent obtained from all individuals.
  - SHARE and SHARE-HCAP protocols approved by the Ethics Committee of the Max Planck Institute in
    Germany; conducted in accordance with the Declaration of Helsinki.
  - No pre-registration identifier (e.g., PROSPERO, OSF) is stated anywhere in the paper's full
    text — not specified in paper.
- **Random seeds**: Not specified in paper (survey sampling/weighting procedures are described at
  the design level — see `logic/solution/study_design.md` — but no computational random-seed values
  are given).

## Code / Clinical trials
- **Code**: none released (per `sources.yaml`). No GitHub/GitLab/Zenodo/OSF repository referenced
  anywhere in the paper.
- **Clinical trials**: none (per `sources.yaml`). This is an observational survey-based
  epidemiological study, not a registered clinical trial.

## Funding
- US National Institute on Aging (NIA), grant R01 AG056329, for collection and analysis of the
  SHARE-HCAP data.
- EU Commission H2020 framework programme, SHAREDEV3, grant No. 676536, contributing to SHARE-HCAP
  and the SHARE parent study.
- National sources in almost all SHARE countries also supported data collection.
- Open access funding enabled and organized by Projekt DEAL.
- "The funders of the study had no role in study design, data collection, data analysis, data
  interpretation, or writing of the report."

## Supplementary materials referenced but not provided as input
Supplementary Tables S1–S7 and Supplementary Sections S1–S3 are referenced throughout the paper for
additional technical detail (e.g., the full regression specification in S2, the informant-based
proxy-classification rule in S3) but were not included in `paper.pdf` and were not separately
provided — see `evidence/README.md` for the full list. Their contents are not fabricated anywhere in
this ARA.
