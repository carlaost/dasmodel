# Experiments (Analysis Plans)

> Grounding: abstract-only. These are directional analysis plans reconstructed from the abstract's
> reported findings. NO exact numbers appear here (none are available from the provided input in any
> case). Setup detail beyond cohorts is "Not available from provided input (no full text)."

## E01: Concordance of the combined plasma model with PET-based biological staging
- **Verifies**: C01
- **Setup**:
  - Model: Combined plasma staging model (%p-tau217 + eMTBR-tau243)
  - Reference standard: Amyloid- and tau-PET–based biological staging scheme
  - Cohort: BioFINDER-2 primary cohort (872 participants; NCT03174938)
  - System: Plasma biomarker measurement (mass spectrometry per metadata) + statistical staging
    model. Exact assay/model spec: Not available from provided input (no full text).
- **Procedure**:
  1. Assign each participant a PET-based biological stage (reference).
  2. Assign each participant a plasma-based stage from the combined model.
  3. Compare plasma-assigned stage against PET-assigned stage.
- **Metrics**: Concordance / agreement between plasma and PET staging (exact statistic not available
  from provided input).
- **Expected outcome**:
  - The combined plasma model agrees strongly with PET-based staging.
- **Baselines**: %p-tau217-only model (see E02).
- **Dependencies**: none

## E02: Head-to-head comparison of combined model vs %p-tau217-only model
- **Verifies**: C02
- **Setup**:
  - Models: Combined plasma model vs %p-tau217-only model
  - Reference standard: PET-based biological staging
  - Cohort: BioFINDER-2 (872 participants)
  - System: As E01.
- **Procedure**:
  1. Stage participants with each model independently.
  2. Compare each model's concordance with PET-based staging overall.
  3. Compare performance specifically at the intermediate tau stage.
- **Metrics**: Difference in staging concordance between models, overall and at the intermediate tau
  stage (exact margins not available from provided input).
- **Expected outcome**:
  - The combined model outperforms the %p-tau217-only model, with the advantage most pronounced at
    the intermediate tau stage.
- **Baselines**: %p-tau217-only model.
- **Dependencies**: E01

## E03: Association of plasma stage with clinical severity, other biomarkers, and neuropathology
- **Verifies**: C03
- **Setup**:
  - Predictor: Plasma-defined biological stage (from the combined model)
  - Outcomes: Clinical severity measures; other (non-PET) biomarker abnormalities; neuropathologic
    burden. Exact measures: Not available from provided input (no full text).
  - Cohort: BioFINDER-2 and/or Knight ADRC (neuropathology likely from autopsy-linked participants;
    exact allocation not available from provided input).
- **Procedure**:
  1. Group participants by plasma-defined stage.
  2. Compare clinical severity, other biomarker abnormalities, and neuropathologic burden across
     stages.
- **Metrics**: Association/trend of each outcome across increasing plasma stage (exact statistics not
  available from provided input).
- **Expected outcome**:
  - More advanced plasma stages align with greater clinical severity, more biomarker abnormality,
    and greater neuropathologic burden.
- **Baselines**: Comparison across stage groups (no external baseline stated).
- **Dependencies**: E01

## E04: Independent external validation in the Knight ADRC cohort
- **Verifies**: C01, C02
- **Setup**:
  - Models: Combined plasma model (and %p-tau217-only model for comparison)
  - Reference standard: PET-based biological staging
  - Cohort: Knight Alzheimer Disease Research Center (156 independent participants)
  - System: As E01.
- **Procedure**:
  1. Apply the staging model(s) developed/evaluated in BioFINDER-2 to the independent Knight ADRC
     cohort.
  2. Assess concordance with PET-based staging and the combined-vs-%p-tau217-only comparison.
- **Metrics**: Staging concordance in the independent cohort (exact statistic not available from
  provided input).
- **Expected outcome**:
  - Findings from BioFINDER-2 replicate in the independent Knight ADRC cohort.
- **Baselines**: %p-tau217-only model.
- **Dependencies**: E01, E02
