# Related Work / Typed Dependencies

> Grounding: abstract-only. The paper's full References list was NOT available (the provided PDF
> is a different article — see PAPER.md). The dependencies below are reconstructed from the
> abstract and the verified `sources.yaml`. DOIs/citation details that are not in the provided
> input are marked "Not available from provided input (no full text)". Entries RW01 (dataset) and
> RW07 (preprint) are directly verified from `sources.yaml`; RW02–RW06 are architectures/tools
> named in the abstract, with their canonical identities noted as standard field knowledge.

## RW01: Kaggle "Augmented Alzheimer MRI Dataset" (uraninjo)
- **DOI**: Not available (dataset). Identifier: kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset
- **Type**: imports (data source)
- **Delta**:
  - What changed: This paper consumes the dataset as-is for training/evaluation; it does not modify the dataset's construction.
  - Why: Provides a large, class-labelled 2D MRI corpus (33,984 augmented + 6,400 original images, 4 severity classes) enabling supervised AD severity classification without collecting a new cohort.
- **Claims affected**: C01, C02
- **Adopted elements**: The four-class severity labels (NonDemented, VeryMildDemented, MildDemented, ModerateDemented) and the augmented + original image splits. Verified open-access via `sources.yaml`.

## RW02: MobileNet-V3 Large (architecture)
- **DOI**: Not available from provided input (no full text). (Canonical origin: Howard et al., "Searching for MobileNetV3", ICCV 2019 — standard field knowledge, not from the provided input.)
- **Type**: imports (backbone architecture)
- **Delta**:
  - What changed: Applied to 4-class AD severity classification on 2D MRI; selected as the deployed model for its efficiency.
  - Why: Lightweight (4.2M parameters per abstract) yet highest-accuracy of the three tested.
- **Claims affected**: C01, C02, C04
- **Adopted elements**: The MobileNet-V3 Large architecture as an image classifier.

## RW03: EfficientNet-B4 (architecture)
- **DOI**: Not available from provided input (no full text). (Canonical origin: Tan & Le, "EfficientNet", ICML 2019 — standard field knowledge, not from the provided input.)
- **Type**: baseline (comparison architecture)
- **Delta**:
  - What changed: Trained/evaluated on the same AD dataset as a comparison point.
  - Why: To benchmark MobileNet-V3 Large against a mid-size efficient architecture.
- **Claims affected**: C01
- **Adopted elements**: The EfficientNet-B4 architecture as a classifier baseline.

## RW04: ResNet-50 (architecture)
- **DOI**: Not available from provided input (no full text). (Canonical origin: He et al., "Deep Residual Learning", CVPR 2016 — standard field knowledge, not from the provided input.)
- **Type**: baseline (comparison architecture)
- **Delta**:
  - What changed: Trained/evaluated on the same AD dataset as a comparison point.
  - Why: To benchmark against a widely used deeper residual CNN.
- **Claims affected**: C01
- **Adopted elements**: The ResNet-50 architecture as a classifier baseline.

## RW05: XRAI / Saliency library (explainability method)
- **DOI**: Not available from provided input (no full text). (Canonical origin: Kapishnikov et al., "XRAI: Better Attributions Through Regions", ICCV 2019 — standard field knowledge; implementation via the Saliency library per `sources.yaml`, not from the paper's own reference list which was unavailable.)
- **Type**: imports (explainability method)
- **Delta**:
  - What changed: Integrated into an AD-severity MRI classifier to produce region-based attribution maps; claimed as the first such systematic integration (C05).
  - Why: To provide clinically meaningful, region-level visual explanations.
- **Claims affected**: C03, C05
- **Adopted elements**: The XRAI region-ranking attribution algorithm (Saliency library module).

## RW06: Gradio (web interface framework)
- **DOI**: Not available (software library).
- **Type**: imports (deployment infrastructure)
- **Delta**:
  - What changed: Used to build a real-time web clinical interface delivering predictions + XRAI explanations.
  - Why: To make the model clinically usable with sub-20-second interactive inference.
- **Claims affected**: C04
- **Adopted elements**: The Gradio app framework for the clinical UI.

## RW07: bioRxiv preprint of the same work
- **DOI**: 10.1101/2025.08.16.670652
- **Type**: extends (same authors' preprint of this work)
- **Delta**:
  - What changed: A preprint version of the same study exists; the Diagnostics article is the peer-reviewed publication.
  - Why: Recorded for provenance; per `sources.yaml` the preprint surfaces no code link.
- **Claims affected**: C01–C05 (same underlying study)
- **Adopted elements**: Same methodology and results.

---

**Coverage note**: The paper's remaining citation footprint (background AD epidemiology, prior
AI-for-AD studies, XAI literature) could not be captured because the full text and its References
list were not available from the provided input.
