# Experiments and Analyses

> Grounding: abstract-only. These are directional review/analysis plans reconstructed from the abstract's reported findings. No exact numerical results are repeated here; exact values live in `claims.md`.

## E01: Bibliometric corpus mapping
- **Verifies**: C01, C02
- **Setup**:
  - Corpus: AD digital-biomarker studies from Web of Science, PubMed, Embase, IEEE Xplore, and CINAHL.
  - System: Bibliometric analysis workflow. Search strings, dates, screening rules, and software: Not available from provided input.
- **Procedure**:
  1. Search the named databases for AD digital-biomarker studies.
  2. Deduplicate and screen records into the bibliometric corpus.
  3. Extract funding, discipline, institution, country, and author/researcher metadata.
- **Metrics**: Corpus size and counts across funding, discipline, institution, country, and researcher dimensions.
- **Expected outcome**:
  - The analysis maps a broad, multidisciplinary, international research landscape.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: AI-model scoping review
- **Verifies**: C01
- **Setup**:
  - Corpus: AI models within the reviewed AD digital-biomarker literature.
  - Extraction schema: Not available from provided input.
- **Procedure**:
  1. Identify studies containing AI models.
  2. Extract model-level entries for the scoping review.
  3. Classify models by target condition and available reporting fields.
- **Metrics**: Count of scoped AI models and model categories.
- **Expected outcome**:
  - The review isolates an AI-model subset from the broader bibliometric corpus.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E03: Digital-biomarker focus-area classification
- **Verifies**: C03
- **Setup**:
  - Inputs: Included studies and their digital-biomarker modalities/tasks.
  - Taxonomy: Not available from provided input.
- **Procedure**:
  1. Assign studies or models to focus areas.
  2. Summarize prominent areas across the literature.
- **Metrics**: Relative prominence or frequency of focus areas (exact counts not available from provided input).
- **Expected outcome**:
  - Motor activity, neurocognitive testing, eye tracking, and speech analysis emerge as key areas.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E02

## E04: Model-family and performance-reporting assessment
- **Verifies**: C04, C05
- **Setup**:
  - Inputs: Scoped AI models and their reported performance fields.
  - Model-family taxonomy: Not available from provided input.
- **Procedure**:
  1. Classify each scoped AI model by model family.
  2. Record whether performance metrics are reported.
  3. Aggregate performance summaries for AD-focused and MCI models where reported.
- **Metrics**: Dominant model family, reporting completeness, and average discrimination performance by target condition.
- **Expected outcome**:
  - Classical machine learning dominates, many models lack performance reporting, and reported AUC summaries are available for AD-focused and MCI model subsets.
- **Baselines**: Not available from provided input.
- **Dependencies**: E02

## E05: Clinical-readiness checks for validation and calibration
- **Verifies**: C05
- **Setup**:
  - Inputs: Scoped AI-model studies.
  - Criteria: External validation and model calibration presence/absence. Exact definitions: Not available from provided input.
- **Procedure**:
  1. Mark each study for external validation.
  2. Mark each study for model calibration.
  3. Compare these checks against the overall AI-model literature.
- **Metrics**: Counts or proportions of studies with external validation and calibration.
- **Expected outcome**:
  - External validation and calibration are rare, highlighting barriers to clinical integration.
- **Baselines**: Not available from provided input.
- **Dependencies**: E02, E04
