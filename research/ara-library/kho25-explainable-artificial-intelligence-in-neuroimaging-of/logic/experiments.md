# Experiments (Review and Assessment Plans)

> Grounding: abstract-only, directional only. The abstract describes a review but provides no search strategy, inclusion criteria, screening counts, appraisal protocol, datasets, model results, or numerical outcomes. These entries reconstruct only the analysis tasks implied by the abstract.

## E01: Review and map XAI techniques used in AD neuroimaging
- **Verifies**: C01, C02, C03
- **Setup**:
  - Design: Review of XAI in AD neuroimaging.
  - Techniques: SHAP, LIME, Grad-CAM, Layer-wise Relevance Propagation.
  - Modalities: MRI and PET.
  - Search strategy: Not available from provided input.
  - Inclusion/exclusion criteria: Not available from provided input.
- **Procedure**:
  1. Identify AD neuroimaging studies using XAI methods.
  2. Categorize studies by XAI technique.
  3. Map each technique to modality and AD diagnostic application.
- **Metrics**: Technique coverage, modality coverage, application category coverage.
- **Expected outcome**:
  - The review identifies SHAP, LIME, Grad-CAM, and LRP as key XAI methods for AD neuroimaging.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Synthesize XAI applications in AD neuroimaging
- **Verifies**: C03, C04
- **Setup**:
  - Application areas: critical biomarker identification, disease-progression tracking, AD-stage distinction.
  - Imaging modalities: MRI and PET.
  - Study corpus: Not available from provided input.
- **Procedure**:
  1. Extract reported XAI use cases from reviewed studies.
  2. Group applications by biomarker, progression, and staging tasks.
  3. Identify whether applications use MRI, PET, or other neuroimaging modalities.
  4. Record challenges discussed for each application area.
- **Metrics**: Qualitative application categories and challenge categories.
- **Expected outcome**:
  - XAI applications cluster around biomarker identification, progression tracking, and stage distinction, while dataset, regulatory, and standardization barriers remain.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E03: Assess clinical-integration barriers and future directions
- **Verifies**: C01, C04, C05
- **Setup**:
  - Challenge categories: dataset limitations, regulatory concerns, standardization issues.
  - Target context: integration of XAI into clinical practice.
  - Evaluation framework: Not available from provided input.
- **Procedure**:
  1. Summarize clinical interpretability barriers for AI-driven AD diagnostics.
  2. Identify dataset, regulatory, and standardization constraints discussed in the review.
  3. Translate those constraints into future research directions for clinical XAI integration.
- **Metrics**: Qualitative barrier categories and proposed research directions.
- **Expected outcome**:
  - Future work focuses on improving XAI integration into clinical practice and evaluating whether XAI can refine diagnostics, personalize treatment, and support neuroimaging research.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E02
