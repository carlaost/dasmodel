# Related Work and Methodological Dependencies

> Grounding: abstract-only. The full reference list is Not available from provided input (no full text). This file captures the methodological standards, registration, and source-corpus dependencies that the abstract and the verified sources record (sources.yaml/metadata.md) explicitly name. It folds in the discovered sources: no code, no released dataset, no clinical trials; one review-protocol registration.

## RW01: PROSPERO systematic-review protocol registration — CRD42023422143
- **DOI**: n/a (registry record: https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=422143)
- **Type**: bounds
- **Delta**:
  - What changed: Pre-registered the review question, eligibility criteria, and analysis plan a priori, constraining the conducted review.
  - Why: PROSPERO registration reduces reporting bias and post-hoc protocol deviation for systematic reviews.
- **Claims affected**: C01–C07 (all; the registration governs the whole review)
- **Adopted elements**: Prospective protocol registration (a systematic-review protocol registry — NOT a ClinicalTrials.gov interventional trial; no NCT identifier is associated).

## RW02: PRISMA-DTA reporting guideline
- **DOI**: 10.1001/jama.2017.19163 (McInnes et al., 2018 — PRISMA-DTA statement)
- **Type**: imports
- **Delta**:
  - What changed: The review's reporting and flow (identification → eligibility → inclusion) follow the PRISMA-DTA standard for diagnostic-accuracy reviews.
  - Why: Standardised, transparent reporting of diagnostic test accuracy syntheses.
- **Claims affected**: C01–C05
- **Adopted elements**: PRISMA-DTA flow and reporting checklist.

## RW03: QUADAS-2 risk-of-bias tool
- **DOI**: 10.7326/0003-4819-155-8-201110180-00009 (Whiting et al., 2011)
- **Type**: imports
- **Delta**:
  - What changed: Applied QUADAS-2 to rate risk of bias across the 113 included studies.
  - Why: Domain-based, validated appraisal of diagnostic-accuracy study quality.
- **Claims affected**: C06
- **Adopted elements**: QUADAS-2 domains (patient selection, index test, reference standard, flow and timing).

## RW04: GRADE certainty-of-evidence framework
- **DOI**: 10.1136/bmj.39489.470347.AD (Guyatt et al., 2008 — GRADE)
- **Type**: imports
- **Delta**:
  - What changed: Rated certainty of the pooled diagnostic-accuracy evidence (low/moderate) per assay.
  - Why: Transparent grading of the confidence in effect estimates.
- **Claims affected**: C01–C05, C07
- **Adopted elements**: GRADE certainty levels applied to DTA outcomes.

## RW05: Bivariate random-effects DTA meta-analysis methodology
- **DOI**: 10.1016/j.jclinepi.2005.02.022 (Reitsma et al., 2005 — bivariate model) [attribution inferred from the standard method named in the abstract; exact citation Not available from provided input]
- **Type**: imports
- **Delta**:
  - What changed: Used a bivariate random-effects model to jointly pool sensitivity and specificity and derive summary DOR and AUROC.
  - Why: Correctly accounts for the correlation between sensitivity and specificity across studies.
- **Claims affected**: C01–C05
- **Adopted elements**: Bivariate random-effects pooling.

## Source corpus (folded-in data dependency)
- **113 included primary diagnostic-accuracy studies (29,625 unique individuals)** — the underlying evidence base. These appear only as citations within the review; no individual-level dataset was released (sources.yaml `data: []`; Europe PMC `hasData = "N"`). Individual study DOIs/PMIDs: Not available from provided input (no full text).

## Discovered-sources summary (from sources.yaml)
- **Code repositories**: none (`code: []`) — no GitHub/GitLab/Zenodo/OSF repository; expected for a DTA meta-analysis.
- **Datasets**: none (`data: []`) — no GEO/SRA/EGA/ArrayExpress accessions or data-repository DOIs; no released dataset.
- **Clinical trials**: none (`clinical_trials: []`) — no NCT identifier; the only registration is the PROSPERO review protocol CRD42023422143 (RW01).
- **Open-access PDF**: not downloadable — sole OA location is a submitted-version landing page at Aarhus University Pure (https://pure.au.dk/portal/en/publications/6b1f1918-f394-414e-b72d-9a062ca3cec5); published version paywalled at The Lancet Neurology.
