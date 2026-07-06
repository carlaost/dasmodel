# Related Work & External Sources

> Grounding: abstract-only. The paper's full reference list is not available from the provided input
> (no full text), so per-citation `RW` blocks with technical deltas cannot be reconstructed
> faithfully. What follows is (a) the verified external resources this study is built on — cohorts,
> the registered trial, and data-sharing artifacts, folded in from `sources.yaml` and metadata — and
> (b) an honest note on the missing citation footprint.

## RW01: Swedish BioFINDER-2 study (primary cohort)
- **DOI**: — (ClinicalTrials.gov NCT03174938)
- **Type**: imports (data source / study infrastructure)
- **Delta**:
  - What changed: This paper uses the BioFINDER-2 cohort as its primary discovery cohort (872
    participants) for developing/evaluating the plasma staging model.
  - Why: Provides paired plasma biomarker, PET, clinical, and (partly) neuropathologic data at scale.
- **Claims affected**: C01, C02, C03, C04
- **Adopted elements**: Cohort participants, biomarker/PET measurements, staging reference standard.
- **Details (verified)**: "The Swedish BioFINDER 2 Study" (acronym BioFINDER2); observational /
  translational study, phase NA, status RECRUITING, enrollment ~2950; sponsor **Skåne University
  Hospital**, collaborator **Lund University**. Verified via ClinicalTrials.gov (`sources.yaml`).

## RW02: Knight Alzheimer Disease Research Center (ADRC) cohort (independent validation)
- **DOI**: —
- **Type**: imports (independent validation data source)
- **Delta**:
  - What changed: Supplies the independent external validation cohort (156 participants) at
    Washington University in St. Louis.
  - Why: Tests generalizability of the plasma staging model beyond BioFINDER-2.
- **Claims affected**: C01, C02
- **Adopted elements**: Independent cohort with plasma, PET, and neuropathologic data.
- **Details (verified)**: Knight ADRC, Washington University in St. Louis; controlled/request access
  (`sources.yaml`).

## RW03: Data Sharing Statement (Supplement 2)
- **DOI**: 10.1001/jamaneurol.2026.1405 (Supplement 2: `jamaneurol-e261405-s002.pdf`)
- **Type**: imports (governance / reproducibility artifact)
- **Delta**:
  - What changed: Defines the terms under which cohort data may be accessed.
  - Why: Establishes that data are available to qualified researchers on reasonable request.
- **Claims affected**: none directly (governance)
- **Adopted elements**: Data-access policy.

## Missing citation footprint (abstract-only)
The scientific citation footprint of this article — prior work on %p-tau217, eMTBR-tau /
microtubule-binding-region tau species, PET-based amyloid/tau biological staging schemes,
blood-based AD biomarker validation, and related staging frameworks — **is not available from the
provided input (no full text)**. Typed dependency blocks for those predecessor works (imports /
extends / bounds / baseline / refutes) cannot be reconstructed without fabrication and are therefore
omitted rather than invented.
