# Problem Specification

> Grounding: abstract-only. Observations, gaps, and insight are reconstructed from the abstract and
> bibliographic metadata; the paper's full motivating narrative was not available. Where the abstract
> does not supply detail, fields read "Not available from provided input (no full text)".

## Observations

### O1: Early AD staging is clinically critical but obstructed by privacy regulations
- **Statement**: Accurate, early-stage staging of Alzheimer's disease is critical for therapeutic
  intervention but is hampered by data privacy regulations.
- **Evidence**: Abstract (metadata.md, "Abstract"): "Accurate, early-stage staging of Alzheimer's
  disease (AD) is critical for therapeutic intervention but is hampered by data privacy regulations…".
- **Implication**: Clinical data cannot be freely centralized across sites, motivating a
  privacy-preserving (federated) approach.

### O2: AD-relevant data is multimodal and heterogeneous
- **Statement**: Relevant clinical signal is spread across at least four modalities — 3D structural
  MRI, IBSI-compliant radiomics, cognitive assessments, and FDA-cleared plasma biomarkers.
- **Evidence**: Abstract: "…integrates four clinically relevant modalities, 3D structural Magnetic
  Resonance Imaging (MRI), Image Biomarker Standardization Initiative (IBSI)-compliant radiomics,
  cognitive assessments, and U.S. Food and Drug Administration (FDA) cleared plasma biomarkers…".
- **Implication**: A single-modality model is insufficient; fusion must handle data heterogeneity.

### O3: Complex AI models are "black boxes," limiting clinical trust
- **Statement**: The black-box nature of complex AI models is an obstacle to clinical adoption for
  AD staging.
- **Evidence**: Abstract: "…and the \"black-box\" nature of complex Artificial Intelligence (AI)
  models."
- **Implication**: Interpretability/explainability is a first-class requirement, not an add-on.

### O4: Standard federated averaging incurs high communication overhead
- **Statement**: Standard federated averaging is the baseline against which the proposed method's
  communication cost is measured; the proposed method reduces overhead by 99% (to 140 KB/round).
- **Evidence**: Abstract: "…reducing communication overhead by 99% (to 140 KB/round) compared to
  standard federated averaging."
- **Implication**: Communication cost is a practical bottleneck for distributed clinical training.

## Gaps

### G1: No single approach is simultaneously accurate, private, efficient, and trustworthy
- **Statement**: Existing AD-staging AI does not jointly satisfy accuracy, privacy preservation,
  communication efficiency, and clinical interpretability.
- **Caused by**: O1, O2, O3, O4
- **Existing attempts**: Centralized multimodal models (accurate but privacy-violating); standard
  federated averaging (private but communication-heavy per O4); black-box models (per O3).
- **Why they fail**: Not available from provided input (no full text) beyond the abstract's framing
  that these challenges are "interconnected."

### G2: Federated multimodal fusion must weight heterogeneous modalities without central data
- **Statement**: Fusing four heterogeneous modalities across sites requires dynamic modality
  weighting that cannot rely on pooled data.
- **Caused by**: O1, O2
- **Existing attempts**: Static/uniform modality fusion (implied baseline).
- **Why they fail**: Not available from provided input (no full text).

### G3: Explainability must be reconciled across sites without sharing raw patient data
- **Statement**: Producing a single clinically coherent interpretation across federated clients is
  hard when raw data (and thus raw saliency inputs) cannot leave each site.
- **Caused by**: O1, O3
- **Existing attempts**: Per-client saliency maps that are not reconciled.
- **Why they fail**: Not available from provided input (no full text).

## Key Insight
- **Insight**: Parameter-efficient adaptation (LoRA + dynamic token gating) plus
  uncertainty-driven hierarchical attention fusion can deliver near-centralized accuracy under
  federation, while a fuzzy-rough hybrid pipeline reconciles per-client saliency into a consensus
  interpretation — all without sharing raw data.
- **Derived from**: O1, O2, O3, O4
- **Enables**: A federated Swin-UNet framework that is accurate (80.7% balanced accuracy vs 82.1%
  centralized), efficient (140 KB/round), and interpretable (Dice similarity 0.84 across sites).

## Assumptions
- A1: A stratified four-client federation derived from ADNI is representative of the distributed
  clinical setting the method targets.
- A2: The four modalities (MRI, radiomics, cognitive assessments, plasma biomarkers) are available
  (or partially available) at participating clients.
- A3: Domain shift across sites can be meaningfully approximated by "simulated domain shifts."
- A4: Details of the AD staging label space (number of stages/classes) — Not available from
  provided input (no full text).
