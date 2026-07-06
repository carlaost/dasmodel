# Related Work & Typed Dependencies

> Grounding: abstract-only. The paper's References list was not available (no full text), so no
> per-citation `RW` blocks can be reconstructed with DOIs. What can be captured faithfully are the
> named methods/standards/data the abstract builds on, and the verified data source from
> `sources.yaml`. Individual cited-work deltas are "Not available from provided input (no full text)".

## RW01: Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort — data source
- **Identifier**: ADNI (Alzheimer's Disease Neuroimaging Initiative)
- **Repository**: LONI Image and Data Archive (adni.loni.usc.edu)
- **Access type**: controlled / request-based (verified in sources.yaml)
- **Type**: baseline (data dependency — provides the evaluation cohort)
- **Delta**:
  - What changed: The authors derive a stratified four-client federation from the ADNI cohort to
    simulate a distributed clinical network; no new dataset or accession was released.
  - Why: To evaluate the federated framework under realistic multi-site AD data.
- **Claims affected**: C01, C02, C03, C04, C05
- **Adopted elements**: The MRI, cognitive-assessment, and biomarker data underlying the four fused
  modalities are drawn from ADNI.
- **Source**: metadata.md abstract + sources.yaml (`data:` entry, `access: controlled`, `verified: true`)

## RW02: Standard federated averaging (FedAvg) — baseline
- **DOI**: Not available from provided input (no full text)
- **Type**: baseline
- **Delta**:
  - What changed: The proposed method replaces full-parameter update exchange with LoRA + dynamic
    token gating, cutting communication overhead by 99% (to 140 KB/round).
  - Why: Standard federated averaging is communication-heavy for large transformer models.
- **Claims affected**: C02
- **Adopted elements**: The federated training paradigm (model-update exchange, no raw-data sharing).

## RW03: Swin transformer / U-Net (Swin-UNet) architecture — imports
- **DOI**: Not available from provided input (no full text)
- **Type**: imports
- **Delta**:
  - What changed: Used as the parameter-efficient backbone for multimodal AD staging; adapted with
    LoRA, dynamic token gating, and hierarchical attention fusion.
  - Why: Transformer encoder–decoder suited to 3D imaging and multimodal fusion.
- **Claims affected**: C01, C03
- **Adopted elements**: The Swin-UNet transformer architecture.

## RW04: Low-Rank Adaptation (LoRA) — imports
- **DOI**: Not available from provided input (no full text)
- **Type**: imports
- **Delta**:
  - What changed: Applied within a federated Swin-UNet to reduce the number of communicated
    parameters per round.
  - Why: Parameter-efficient adaptation lowers communication cost.
- **Claims affected**: C02
- **Adopted elements**: The low-rank adaptation technique.

## RW05: Image Biomarker Standardization Initiative (IBSI) — standard / imports
- **Identifier**: IBSI (Image Biomarker Standardization Initiative)
- **Type**: imports
- **Delta**:
  - What changed: Radiomic features are extracted in an IBSI-compliant manner to ensure reproducible,
    cross-site-comparable features.
  - Why: Standardized radiomics is needed for a multi-site federation.
- **Claims affected**: C01, C03
- **Adopted elements**: IBSI-compliant radiomic feature definitions.

## RW06: FDA-cleared plasma biomarker assays — imports (modality source)
- **Type**: imports
- **Delta**:
  - What changed: FDA-cleared plasma biomarkers are incorporated as one of the four fused modalities.
  - Why: Clinically validated, regulatory-cleared blood biomarkers add a non-imaging signal.
- **Claims affected**: C01, C03
- **Adopted elements**: The plasma-biomarker modality.

## RW07: Fuzzy-set and rough-set theory (explainability foundations) — imports
- **DOI**: Not available from provided input (no full text)
- **Type**: imports
- **Delta**:
  - What changed: Combined into a "fuzzy-rough hybrid" pipeline that synthesizes client-specific
    saliency maps into a consensus interpretation without sharing raw data.
  - Why: To reconcile per-site explanations into a single clinically coherent interpretation.
- **Claims affected**: C04
- **Adopted elements**: Fuzzy-set and rough-set reasoning.

## Full citation footprint
The paper's complete References list is Not available from provided input (no full text). The
entries above capture the methods, standards, baselines, and data the abstract explicitly names;
additional background/prior-art citations could not be recovered.
