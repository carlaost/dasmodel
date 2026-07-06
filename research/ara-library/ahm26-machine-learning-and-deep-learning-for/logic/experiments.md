# Experiments (Survey Analyses)

This is a narrative survey, so "experiments" are the **analysis/synthesis procedures** the survey uses
to test its claims about the field — not empirical runs by the authors. They are declarative and
directional only; no numerical results appear here (the survey reports essentially none, and any that
existed would live in `evidence/`).

## E01: Comparative framework analysis across model families
- **Verifies**: C01, C03
- **Setup**:
  - Object of analysis: six method families (traditional ML, CNN-based, multimodal deep learning,
    transformer/hybrid-attention, GNN, explainable-AI-oriented).
  - Dimensions compared: typical input, key strength, main limitation, interpretability, clinical
    readiness.
  - Source material: surveyed studies + supporting reviews; summarized in Figure 6 and Table 1.
- **Procedure**:
  1. For each family, extract representative studies and characterize inputs and mechanisms.
  2. Score each family qualitatively on the five comparison dimensions.
  3. Contrast multimodal families against single-modality families, and transformer/GNN against
     multimodal-CNN baselines.
- **Metrics**: Qualitative ratings (e.g., interpretability {low, moderate, high}; clinical readiness
  {moderate, emerging, high potential}); relative ordering of families.
- **Expected outcome**:
  - Multimodal families rank higher than single-modality families on complementary-information use.
  - Transformer/GNN families rate as "emerging" rather than dominant relative to multimodal CNNs.
- **Baselines**: Traditional ML and single-modality CNN as reference families.
- **Dependencies**: none

## E02: Methodological-evolution mapping (taxonomy construction)
- **Verifies**: C02
- **Setup**:
  - Object: the historical progression of modeling paradigms for AD diagnosis.
  - Source material: taxonomy sections; Figures 4 (taxonomy) and 5 (evolution timeline).
- **Procedure**:
  1. Order paradigms chronologically from handcrafted-feature ML through CNN, multimodal, relational/
     global (GNN/transformer), to trustworthy/clinical AI.
  2. Identify what each stage added over its predecessor and what limitation motivated the next.
  3. Assemble into a taxonomy of five method groups.
- **Metrics**: Presence/absence of a coherent stage-to-stage transition; coverage of paradigms.
- **Expected outcome**: A clear directional shift from handcrafted features to end-to-end,
  increasingly multimodal and clinically-oriented deep learning.
- **Baselines**: Handcrafted-feature ML as the starting stage.
- **Dependencies**: none

## E03: Evaluation-heterogeneity and generalizability appraisal
- **Verifies**: C04, C06
- **Setup**:
  - Object: evaluation practices across surveyed studies (datasets, tasks, splits, preprocessing,
    external validation).
  - Source material: Background; "Why accuracy alone is not enough"; "Reproducibility and
    generalizability"; "Open Challenges"; Figure 4 key-challenges panel.
- **Procedure**:
  1. Catalogue each study's task type, dataset(s), and whether external/cross-site validation is used.
  2. Assess comparability of reported metrics across differing tasks and curated datasets.
  3. Identify benchmark dependence (ADNI), missing-modality handling, and reproducibility gaps.
- **Metrics**: Comparability of reported metrics; fraction of studies with external validation;
  presence of benchmark dependence and reproducibility weaknesses (qualitative).
- **Expected outcome**: Reported accuracy is not directly comparable across studies; external
  validation is uncommon; benchmark dependence limits real-world generalization.
- **Baselines**: Single-benchmark internal-validation studies.
- **Dependencies**: none

## E04: Explainability-rigor assessment
- **Verifies**: C05
- **Setup**:
  - Object: how explainability is implemented and evaluated across surveyed studies.
  - Source material: "Explainable AI"; "Explainability and trust"; Figure 7 and the unnumbered
    Grad-CAM / attention-heatmap illustrations.
- **Procedure**:
  1. Identify explanation methods used (Grad-CAM, SHAP, saliency, attention, self-explainable GNN).
  2. Assess whether each study evaluates explanation stability, reproducibility, clinical
     plausibility, or cross-cohort consistency.
  3. Distinguish post hoc from architecture-level (self-explainable) approaches.
- **Metrics**: Presence/absence of systematic explanation-quality evaluation (qualitative).
- **Expected outcome**: Explainability is commonly presented but rarely rigorously evaluated;
  self-explainable/architecture-level approaches are an emerging improvement.
- **Baselines**: Post hoc single-heatmap presentation.
- **Dependencies**: none

## E05: Representative-study selection and qualitative comparison (Table 1)
- **Verifies**: C01, C03, C07
- **Setup**:
  - Object: the curated set of 8 primary studies (2018-2024).
  - Source material: Scope section; Table 1 (Study/Year/Modality/Core Method/Main Contribution/Main
    Limitation).
- **Procedure**:
  1. Select ~10-15 representative and influential studies; name 8 primary ones plus supporting reviews.
  2. For each, record modality, core method, main contribution, and main limitation.
  3. Cross-compare to substantiate field-level claims (multimodal advantage; transformer/GNN caution).
- **Metrics**: Coverage of method families; consistency of per-study contribution/limitation summary.
- **Expected outcome**: The curated sample spans the field's main methodological directions and
  supports the survey's synthesis claims.
- **Baselines**: none
- **Dependencies**: E01, E02
