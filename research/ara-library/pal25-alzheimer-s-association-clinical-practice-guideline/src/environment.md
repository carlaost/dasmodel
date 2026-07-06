# Environment

This is a **clinical practice guideline** (a systematic-review-grounded, GRADE-based evidence synthesis), **not a computational or wet-lab study**. There is no released software repository, no released dataset with accessions, and no registered clinical trial associated with this work (confirmed by `sources.yaml`: `code: []`, `data: []`, `clinical_trials: []`). Accordingly there is **no `src/execution/` code stub** — the methodology is prose/analytic and lives in `logic/solution/study_design.md`; manufacturing a code stub would only duplicate it.

- **Language/runtime**: Analytical — none released. Meta-analysis of diagnostic test accuracy and GRADE certainty assessment were performed by statisticians/methodologists for the companion systematic review (ref 19); no analysis code is published with this CPG.
- **Framework/methods**:
  - GRADE approach for certainty of evidence and the GRADE Evidence-to-Decision (EtD) framework for recommendations.
  - Diagnostic-test-accuracy meta-analysis to pool sensitivity/specificity per BBM test (single Youden-index cutoff, plus four sensitivity analyses).
  - Reporting/development standards: AGREE II Reporting Checklist (ref 20); GIN-McMaster Guideline Development Checklist (ref 21). Risk of bias per QUADAS-2 (ref 78).
- **Hardware**: n/a.
- **Tools**:
  - **WebPlotDigitizer v4.6** (ref 24, https://automeris.io/) — used to derive Sn/Sp at Youden's index from published ROC curves when raw 2×2 data were neither published nor author-provided.
  - **MAGICapp** platform (https://app.magicapp.org/#/guideline/nyO1Yj) — hosts the living guideline and evidence summary of tests meeting triaging/confirmatory criteria.

## Data sources

- **Literature databases searched** (open, bibliographic): PubMed, Medline, Embase, Cochrane Library — from **2019 through November 3, 2024**. Access: open (database searching).
- **Primary evidence corpus** (controlled/aggregated): **49 observational diagnostic-test-accuracy studies** (refs 5, 16, 17, 31–76) covering **31 assay/analyte combinations** (Table 3). Extracted per study: TP, TN, FP, FN, Sn, Sp at the Youden-index cutoff. Access type: **request/controlled at the individual-study level** — raw data were obtained from (1) publications, (2) authors on request when missing, or (3) ROC-curve digitization. No unified dataset is released by this guideline; **no accession identifiers** (no ADNI / UK Biobank / BioFINDER / GEO / SRA / EGA ID released by this work).
  - Corpus descriptors: mean sample size 560 participants (range 70–2244); mean age across studies 62.6–85.9 years; % male 33.8%–60%; APOE ε4 carriers 27.1%–56.2% across the 32 studies reporting APOE genotyping. **84 otherwise-eligible studies were excluded** for pooling cognitively impaired and unimpaired populations.
- **Companion systematic review** (ref 19; Pahlke SC, et al., Alzheimer's & Dementia, Submitted): the aggregated evidence base (pooled Sn/Sp, sensitivity analyses, evidence profiles). Access: to be published separately; living updates via MAGICapp.
- **Reference standards** used to define AD pathology: CSF AD biomarkers, amyloid PET, or neuropathology.

## Protocols
- Living-guideline update process via MAGICapp; public comment period May 12–May 23; external review by numerous professional organizations and agencies.
- No preregistration ID (PROSPERO) is stated in the paper's full text.

## Code / Clinical trials
- **Code**: none (per sources.yaml). No GitHub/GitLab/Zenodo/OSF/Bitbucket repository.
- **Clinical trials**: none (per sources.yaml). No NCT identifier; a guideline does not register a trial.

## Random seeds
- Not applicable (no released computational pipeline).

## Funding
- Alzheimer's Association (which funded the CPG but was not involved in formulating clinical questions or recommendations). Per external metadata, related NIA/NIH support includes grants R01 AG083874, P30 AG062429, P30 AG072958, and U24 AG082930.
