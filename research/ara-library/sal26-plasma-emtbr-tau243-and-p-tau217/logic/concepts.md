# Concepts

> Grounding: abstract-only. Definitions capture the genuine technical terms named in the abstract
> and title. Where a term's precise operational definition (assay, cut-point, staging algorithm)
> would come from the Methods, that detail is "Not available from provided input (no full text)."

## Plasma %p-tau217
- **Notation**: %p-tau217
- **Definition**: The phosphorylation occupancy of tau at threonine-217 measured in blood plasma —
  the ratio of phosphorylated to total tau-217 species — used as a blood-based marker of Alzheimer
  disease pathology and one of the two inputs to the staging model. Exact assay/platform and
  cut-points: Not available from provided input (no full text).
- **Boundary conditions**: Serves in this study both as a component of the combined model and as the
  single-marker comparison model; reported to be less able to identify the intermediate tau stage
  on its own.
- **Related concepts**: eMTBR-tau243, Combined plasma staging model, PET-based biological staging

## eMTBR-tau243
- **Notation**: eMTBR-tau243
- **Definition**: An extracellular microtubule-binding-region (MTBR) tau species ending at residue
  243, measured in plasma — a tau fragment associated with tau aggregation/tangle pathology and the
  second input to the combined staging model. Exact analytical method (mass spectrometry per
  metadata): Not fully available from provided input (no full text).
- **Boundary conditions**: Adds discriminative value for the intermediate tau stage when combined
  with %p-tau217. Standalone performance: Not available from provided input.
- **Related concepts**: Plasma %p-tau217, Intermediate tau stage, Combined plasma staging model

## PET-based biological staging (amyloid + tau)
- **Notation**: —
- **Definition**: A scheme that assigns an Alzheimer disease biological stage from amyloid and tau
  positron emission tomography (PET), serving as the reference standard the plasma model is designed
  to approximate. Exact stage definitions/thresholds: Not available from provided input (no full
  text).
- **Boundary conditions**: Reference standard for concordance analyses in this study.
- **Related concepts**: Combined plasma staging model, Intermediate tau stage, Concordance

## Combined plasma staging model
- **Notation**: —
- **Definition**: A blood-based model that combines %p-tau217 and eMTBR-tau243 to assign an AD
  biological stage approximating the PET-based scheme. Exact model form (thresholds, regression,
  classifier): Not available from provided input (no full text).
- **Boundary conditions**: Compared against a %p-tau217-only model; evaluated in BioFINDER-2 and
  validated in Knight ADRC.
- **Related concepts**: %p-tau217-only model, PET-based biological staging, Intermediate tau stage

## %p-tau217-only model
- **Notation**: —
- **Definition**: The single-marker comparison model that stages AD from plasma %p-tau217 alone,
  used as the baseline the combined model is measured against.
- **Boundary conditions**: Reported to be outperformed by the combined model, particularly at the
  intermediate tau stage.
- **Related concepts**: Combined plasma staging model, Plasma %p-tau217

## Intermediate tau stage
- **Notation**: —
- **Definition**: An intermediate stage of tau pathology within the biological staging scheme; the
  specific stage at which the combined plasma model shows its advantage over the %p-tau217-only
  model. Precise definition of the stage: Not available from provided input (no full text).
- **Boundary conditions**: The regime where single-marker plasma staging is reported to be weakest.
- **Related concepts**: PET-based biological staging, eMTBR-tau243, Combined plasma staging model

## Clinical trial enrichment (biological stratification)
- **Notation**: —
- **Definition**: Use of a biological stage assignment to select or stratify participants for
  treatment or clinical trials — the applied purpose the authors propose for plasma-based staging.
- **Boundary conditions**: Presented as potential/forward-looking utility ("Meaning"), not a
  measured outcome in the abstract.
- **Related concepts**: Combined plasma staging model, PET-based biological staging
