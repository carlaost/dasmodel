# Concepts

> Grounding: abstract-only. Definitions combine the abstract's usage with standard field definitions
> of the named techniques. Where the paper's specific parameterization would be needed (e.g. LoRA
> rank, gating thresholds), it is marked "Not available from provided input (no full text)".

## Privacy-preserving federated learning framework
- **Notation**: —
- **Definition**: A machine-learning setup in which multiple clinical sites (clients) collaboratively
  train a shared model by exchanging model updates rather than raw patient data, so that data
  never leaves each site. Here instantiated as a stratified four-client federation derived from ADNI.
- **Boundary conditions**: Applies when data-privacy regulations prevent centralizing patient data;
  assumes clients can communicate model parameters/updates each round.
- **Related concepts**: Standard federated averaging, Low-Rank Adaptation, hierarchical attention fusion

## Swin-UNet transformer architecture
- **Notation**: —
- **Definition**: A parameter-efficient vision-transformer backbone (Swin transformer encoder in a
  U-Net-style encoder–decoder) used as the shared model that ingests and processes the multimodal AD
  inputs. Described in the abstract as "parameter-efficient."
- **Boundary conditions**: Suited to 3D structural MRI and image-derived inputs; exact layer/window
  configuration — Not available from provided input (no full text).
- **Related concepts**: 3D structural MRI, dynamic token gating, hierarchical attention fusion

## Low-Rank Adaptation (LoRA)
- **Notation**: —
- **Definition**: A parameter-efficient adaptation technique that injects low-rank trainable matrices
  into a large model so only a small number of parameters are updated (and thus communicated). Used
  here to shrink per-round federated communication.
- **Boundary conditions**: Reduces communicated parameters; LoRA rank and target layers — Not
  available from provided input (no full text).
- **Related concepts**: Dynamic token gating, communication overhead, Swin-UNet transformer

## Dynamic token gating
- **Notation**: —
- **Definition**: A mechanism that selectively activates/transmits a subset of tokens (or their
  updates) dynamically, further reducing the information communicated per federated round.
- **Boundary conditions**: Gating criterion/threshold — Not available from provided input (no full text).
- **Related concepts**: Low-Rank Adaptation, communication overhead

## Hierarchical attention fusion
- **Notation**: —
- **Definition**: A fusion mechanism that combines the four modalities using attention arranged
  hierarchically, dynamically weighting each modality according to predictive uncertainty.
- **Boundary conditions**: Applies to the four-modality setting; uncertainty estimator and hierarchy
  levels — Not available from provided input (no full text).
- **Related concepts**: Predictive uncertainty, multimodal fusion, attention

## Predictive uncertainty (modality weighting)
- **Notation**: —
- **Definition**: A per-modality (or per-prediction) measure of model confidence used to weight each
  modality's contribution in the fusion step — higher uncertainty implies lower weight.
- **Boundary conditions**: Uncertainty quantification method — Not available from provided input
  (no full text).
- **Related concepts**: Hierarchical attention fusion, robustness to domain shift

## Fuzzy-rough hybrid explainability pipeline
- **Notation**: —
- **Definition**: An explainability method combining fuzzy-set and rough-set reasoning to synthesize
  client-specific saliency maps into a single consensus-driven, clinically coherent interpretation
  without exchanging raw data.
- **Boundary conditions**: Operates on client-side saliency maps (not raw data); the fuzzy/rough
  membership and consensus formulation — Not available from provided input (no full text).
- **Related concepts**: Saliency map, Dice similarity, cross-site interpretability

## IBSI-compliant radiomics
- **Notation**: —
- **Definition**: Quantitative image features extracted from medical images following the Image
  Biomarker Standardization Initiative (IBSI) conventions, ensuring reproducible feature definitions
  across sites. One of the four fused modalities.
- **Boundary conditions**: Requires standardized image-feature extraction; specific feature set —
  Not available from provided input (no full text).
- **Related concepts**: 3D structural MRI, multimodal fusion

## FDA-cleared plasma biomarkers
- **Notation**: —
- **Definition**: Blood-plasma-based AD biomarkers whose assays have U.S. FDA clearance, used as one
  of the four fused modalities alongside imaging and cognitive assessments.
- **Boundary conditions**: Which specific biomarkers/assays — Not available from provided input
  (no full text).
- **Related concepts**: Cognitive assessments, multimodal fusion

## Balanced accuracy
- **Notation**: —
- **Definition**: The average of per-class recall (sensitivity) across the AD staging classes; the
  paper's headline performance metric (80.7% federated, 82.1% centralized), robust to class imbalance.
- **Boundary conditions**: Number of staging classes — Not available from provided input (no full text).
- **Related concepts**: AD staging, Dice similarity
