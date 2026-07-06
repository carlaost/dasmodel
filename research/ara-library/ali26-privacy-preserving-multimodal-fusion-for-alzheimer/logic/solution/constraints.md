# Constraints, Assumptions & Limitations

> Grounding: abstract-only. Only constraints the abstract states or directly implies are listed as
> grounded; others are explicitly marked as unavailable.

## Boundary conditions
- BC1: Designed for a distributed clinical setting where raw patient data cannot be centralized due
  to privacy regulations (federated, model-update-only exchange).
- BC2: Assumes availability of the four modalities — 3D structural MRI, IBSI-compliant radiomics,
  cognitive assessments, FDA-cleared plasma biomarkers — across participating clients.
- BC3: Evaluated only on a stratified four-client federation derived from ADNI; generalization to
  other cohorts, client counts, or non-ADNI populations is not demonstrated in the abstract.
- BC4: Communication-overhead claim is defined relative to standard federated averaging on the same
  model; the comparison assumes an equivalent FedAvg baseline.

## Assumptions
- A1: The stratified four-client split of ADNI is a valid proxy for real distributed clinical networks.
- A2: Simulated domain shifts adequately approximate real cross-site distribution shift.
- A3: Predictive uncertainty is a useful signal for weighting modalities (premise of the fusion
  mechanism).
- A4: Client-specific saliency maps can be reconciled into a clinically coherent consensus via
  fuzzy-rough reasoning without exchanging raw data.

## Known limitations
- L1: Single-cohort evaluation (ADNI only) — external validity beyond ADNI is not established in the
  abstract.
- L2: Federated balanced accuracy (80.7%) still trails the centralized upper bound (82.1%); a gap
  remains.
- L3: Robustness is shown only against *simulated* domain shifts, not real inter-site shift.
- L4: The specific staging label space, per-class performance, statistical significance, and the
  fairness of the FedAvg communication baseline are Not available from provided input (no full text).
- L5: No public code repository was located for this work (verified in sources.yaml), limiting
  reproducibility.
- L6: ADNI access is controlled/request-based, so reproduction requires a data-use agreement via the
  LONI IDA.
