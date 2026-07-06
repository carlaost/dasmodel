# Experiments

> Grounding: abstract-only. These are declarative verification plans reconstructed from the
> abstract's claims. They are directional only and contain NO exact numbers (the reported values
> live in claims.md `Sources` and would live in evidence/ if the full text were available). The
> paper's actual experimental protocol (splits, seeds, hyperparameters, class definitions) was not
> available.

## E01: Federated vs centralized AD staging on the ADNI four-client federation
- **Verifies**: C01, C05
- **Setup**:
  - Model: Parameter-efficient Swin-UNet transformer with LoRA + dynamic token gating and
    hierarchical attention fusion (four modalities)
  - Hardware: Not available from provided input (no full text)
  - Dataset: Stratified four-client federation derived from the ADNI cohort (controlled access via
    LONI IDA); modalities = 3D structural MRI, IBSI-compliant radiomics, cognitive assessments,
    FDA-cleared plasma biomarkers
  - System: Federated training across four clients (no raw-data sharing) vs a centralized (pooled)
    upper-bound configuration
- **Procedure**:
  1. Construct the stratified four-client federation from ADNI.
  2. Train the framework in federated mode; train a centralized model on pooled data as the upper bound.
  3. Evaluate balanced accuracy for both configurations on the AD staging task.
  4. Apply simulated domain shifts and re-evaluate to assess robustness against federated baselines.
- **Metrics**: Balanced accuracy (%); relative performance degradation under simulated domain shift
- **Expected outcome**:
  - Federated balanced accuracy is close to (slightly below) the centralized upper bound.
  - The framework degrades less under simulated domain shift than standard federated baselines.
- **Baselines**: Centralized (pooled) training as upper bound; standard federated averaging and other
  federated approaches for robustness comparison
- **Dependencies**: none

## E02: Communication overhead vs standard federated averaging
- **Verifies**: C02
- **Setup**:
  - Model: Swin-UNet transformer with LoRA + dynamic token gating vs the same model under standard
    federated averaging (full-parameter update exchange)
  - Hardware: Not available from provided input (no full text)
  - Dataset: ADNI four-client federation (as E01)
  - System: Federated training loop instrumented to measure bytes transmitted per round
- **Procedure**:
  1. Run federated training with LoRA + dynamic token gating; record per-round payload size.
  2. Run standard federated averaging on the same model; record per-round payload size.
  3. Compute the percentage reduction in communication overhead.
- **Metrics**: Per-round communication payload (KB/round); percentage reduction vs FedAvg
- **Expected outcome**:
  - The LoRA + token-gating configuration transmits far less per round than standard federated
    averaging (a large reduction).
- **Baselines**: Standard federated averaging
- **Dependencies**: none

## E03: Ablation of uncertainty-driven hierarchical attention fusion
- **Verifies**: C03
- **Setup**:
  - Model: Framework with hierarchical attention fusion (uncertainty-weighted) vs variants with
    static/uniform modality fusion
  - Hardware: Not available from provided input (no full text)
  - Dataset: ADNI four-client federation (as E01)
  - System: Federated training holding all else fixed while varying the fusion mechanism
- **Procedure**:
  1. Train with the full uncertainty-driven hierarchical attention fusion.
  2. Train ablated variants (e.g. static fusion, no uncertainty weighting).
  3. Compare staging performance and, where possible, robustness under domain shift.
- **Metrics**: Balanced accuracy; robustness under simulated domain shift; qualitative modality weights
- **Expected outcome**:
  - Removing uncertainty-driven weighting reduces performance and/or robustness relative to the full
    mechanism.
- **Baselines**: Static / uniform modality fusion
- **Dependencies**: E01

## E04: Cross-site interpretability of the fuzzy-rough explainability pipeline
- **Verifies**: C04
- **Setup**:
  - Model: The trained federated framework with the fuzzy-rough hybrid explainability pipeline
  - Hardware: Not available from provided input (no full text)
  - Dataset: ADNI four-client federation (as E01)
  - System: Each client produces saliency maps locally; the pipeline synthesizes a consensus
    interpretation without sharing raw data
- **Procedure**:
  1. Generate client-specific saliency maps at each site.
  2. Synthesize a consensus interpretation via the fuzzy-rough hybrid pipeline (no raw-data exchange).
  3. Measure cross-site interpretability agreement using a Dice-similarity-based metric.
- **Metrics**: Dice similarity (cross-site saliency agreement); qualitative clinical coherence
- **Expected outcome**:
  - Cross-site saliency maps show high agreement (a high Dice similarity), indicating consistent,
    clinically coherent interpretations across clients.
- **Baselines**: Per-client saliency without consensus synthesis (implied)
- **Dependencies**: E01
