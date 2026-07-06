# Framework Architecture

> Grounding: abstract-only. This reconstructs the component graph from the abstract's description.
> Internal details (layer configs, LoRA rank, gating thresholds, uncertainty estimator, fuzzy-rough
> formulation) are Not available from provided input (no full text).

## Overview
A privacy-preserving federated learning framework for Alzheimer's disease staging. A shared,
parameter-efficient Swin-UNet transformer is trained across four clients (a stratified federation
derived from ADNI) without sharing raw data; only compact model updates are exchanged.

## Components

### 1. Multimodal inputs (per client)
- **Purpose**: Provide the four clinically relevant signals for AD staging.
- **Inputs**: (a) 3D structural MRI; (b) IBSI-compliant radiomics; (c) cognitive assessments;
  (d) FDA-cleared plasma biomarkers.
- **Outputs**: Modality-specific representations fed to the fusion stage.
- **Key design choice**: Combine imaging (MRI, radiomics) with non-imaging clinical signals
  (cognitive, plasma biomarkers).

### 2. Swin-UNet transformer backbone
- **Purpose**: Parameter-efficient shared model processing the multimodal inputs.
- **Inputs**: Modality representations / tokens.
- **Outputs**: Fused representation for the staging head.
- **Interactions**: Adapted with LoRA and dynamic token gating; feeds the hierarchical attention
  fusion.
- **Key design choice**: "Parameter-efficient" backbone chosen to keep communicated parameters small.

### 3. LoRA + dynamic token gating (communication-efficiency layer)
- **Purpose**: Reduce per-round federated communication overhead by 99% (to 140 KB/round) vs standard
  federated averaging.
- **Inputs**: Backbone parameters / tokens.
- **Outputs**: Low-rank adapter updates and gated token subset transmitted each round.
- **Interactions**: Sits on the backbone; determines what is communicated in the federated loop.

### 4. Hierarchical attention fusion
- **Purpose**: Dynamically weight the four modalities based on predictive uncertainty.
- **Inputs**: Per-modality representations + uncertainty estimates.
- **Outputs**: Fused, uncertainty-weighted representation.
- **Key design choice**: Uncertainty-driven weighting (rather than static fusion) — hypothesized to
  drive robustness to domain shift.

### 5. Staging head
- **Purpose**: Produce the AD staging prediction (balanced accuracy is the headline metric).
- **Inputs**: Fused representation.
- **Outputs**: AD stage classification.
- **Details**: Number/definition of stages — Not available from provided input (no full text).

### 6. Fuzzy-rough hybrid explainability pipeline
- **Purpose**: Synthesize client-specific saliency maps into a consensus-driven, clinically coherent
  interpretation without sharing raw data (cross-site Dice similarity 0.84).
- **Inputs**: Per-client saliency maps.
- **Outputs**: Consensus interpretation / saliency.
- **Interactions**: Runs over client-side explanations; no raw-data exchange.

## Data flow (federated round)
1. Each client processes its local multimodal inputs through the Swin-UNet backbone.
2. Hierarchical attention fusion combines modalities using predictive uncertainty.
3. The staging head predicts the AD stage; local training updates the LoRA adapters.
4. Only LoRA adapter updates + gated tokens (≈140 KB) are communicated for aggregation.
5. Separately/offline, client saliency maps are reconciled by the fuzzy-rough pipeline into a
   consensus interpretation — without sharing raw data.

## Structural claim
The architecture asserts that combining a parameter-efficient transformer backbone,
communication-efficient adaptation, uncertainty-driven fusion, and consensus explainability yields a
system that is simultaneously accurate, efficient, privacy-preserving, and trustworthy.
