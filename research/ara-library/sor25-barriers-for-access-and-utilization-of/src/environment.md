# Environment

This is a **systematic review** (a PRISMA-guided literature search, screening, quality-appraisal, and narrative-synthesis process), **not a computational or wet-lab study**. There is no released software repository, no released dataset with accessions, and no registered clinical trial associated with this work (confirmed by `sources.yaml`: `code: []`, `data: []`, `clinical_trials: []`; and by the paper's own "Data availability" statement: "No datasets were generated or analysed during the current study"). Accordingly there is **no `src/execution/` code stub** — the review methodology is prose/procedural and lives in `logic/solution/study_design.md`; manufacturing a code stub would only duplicate it.

- **Language/runtime**: Analytical/manual — none released. Screening, extraction, and narrative synthesis were performed by the five reviewers and senior reviewer using AI-assisted tooling (Rayyan) and a quality-appraisal instrument (MMAT); no analysis code is published with this review.
- **Framework/methods**:
  - PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines for search/screening/reporting structure.
  - PICO framework for defining eligibility criteria (Table 2).
  - Mixed Methods Appraisal Tool (MMAT), revised 2018 version, for per-study quality scoring.
  - Narrative synthesis (not meta-analysis) for aggregating heterogeneous qualitative/quantitative/mixed-methods findings into barrier-category counts.
- **Hardware**: n/a.
- **Tools**:
  - **Rayyan AI** (https://www.rayyan.ai) — used for duplicate removal and independent, blind title/abstract screening by the five reviewers.
  - **Mixed Methods Appraisal Tool (MMAT)**, revised version — used for per-study quality scoring (0–100%).

## Data sources

- **Literature databases searched** (open, bibliographic): PubMed/MEDLINE (primary), Embase, PsycINFO (EBSCOhost), Health Technology Assessment Database, Web of Science (Clarivate) — searched over the 2013–2023 timeframe. Access: open (database searching).
- **Reference mining**: 4 additional studies identified via reference mining of three prior systematic/narrative reviews (refs 36–38).
- **Primary evidence corpus** (published literature, not an accessioned dataset): **29 included studies** (refs 39–67), each contributing extracted study-characteristics fields (design, methods, population, sample, setting, identified barriers, MMAT score) — transcribed in full in `evidence/tables/table3.md`. No unified dataset is released by this review; extracted data were compiled internally into "an Excel sheet" (per §Methods), which is not released. **No accession identifiers** (no PROSPERO, NCT, or repository ID appears anywhere in the paper's full text).
- **Reference standard for eligibility**: Table 1 (Eligibility criteria) and Table 2 (PICO research string).

## Protocols
- PRISMA-guided review process (identification → screening → eligibility → inclusion; Fig. 1).
- **No preregistration ID (PROSPERO)** is stated anywhere in the paper's full text — not specified in paper.

## Code / Clinical trials
- **Code**: none (per `sources.yaml`). No GitHub/GitLab/Zenodo/OSF/Bitbucket repository.
- **Clinical trials**: none (per `sources.yaml`). No NCT identifier; a systematic review of barriers does not register a trial. (Note: excluding RCTs from the *evidence base* is itself a documented eligibility-criteria decision — see `logic/solution/constraints.md` — distinct from this review not itself being a registered trial.)

## Random seeds
- Not applicable (no released computational pipeline; screening/appraisal performed by human reviewers with AI-assisted tooling).

## Funding
- Italian Ministry of Health, through the project HubLife Science–Digital Health (LSH-DH), PNC-E3-2022-23683267 - DHEAL-COM - CUP E63C22003790001, within the "National Plan for Complementary Investments - Innovative Health Ecosystem" - Unique Investment Code: PNC-E.3.
