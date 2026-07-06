# Related Work

> Grounding: abstract-only. The paper's full reference list is **not available from provided input
> (no full text)**, so the typed dependency graph below reflects only the works that are (a) verified
> in `sources.yaml` / `metadata.md`, or (b) named methods the abstract itself invokes (STFT, CWT,
> ViT, ResNet50, VGG16, CatBoost). It is deliberately partial; the paper's fuller citation footprint
> could not be recovered without the full text.

## RW01: Sedghizadeh, Aghajan & Vahabi — Olfactory-stimulation EEG dataset (MCI/AD)
- **DOI**: 10.17632/sgzbgwjfkr.5 (Mendeley Data)
- **Type**: imports (data)
- **Delta**:
  - What changed: This paper does not release its own recordings; it reuses this public olfactory-EEG cohort (35 seniors — 13 AD, 7 aMCI, 15 healthy — under a rose/lemon olfactory oddball paradigm) as the labelled input to its transform + deep-learning pipeline.
  - Why: Supplies the scarce, task-matched olfactory-evoked EEG needed to test the smell–AD biomarker hypothesis.
- **Claims affected**: C01, C02, C03, C04, C05
- **Adopted elements**: The raw olfactory-evoked EEG recordings and their AD/aMCI/healthy labels (CC BY 4.0, open access).
- **Verification note**: Reuse confirmed via the paper's Semantic Scholar reference list (`metadata.md` "Discovered sources", `sources.yaml` data entry). Not re-verified here — treated as grounded per task instructions.

## RW02: Dosovitskiy et al. — Vision Transformer (ViT)
- **DOI**: arXiv:2010.11929 (not stated in provided input; canonical ViT reference)
- **Type**: imports (method)
- **Delta**:
  - What changed: The ViT image-classification architecture is applied to CWT time-frequency images of olfactory-evoked EEG; it is the best-performing model in this study.
  - Why: Self-attention over image patches is used as an alternative to convolutional inductive bias for classifying EEG-derived images.
- **Claims affected**: C01, C02
- **Adopted elements**: The ViT patch-embedding + self-attention classifier.
- **Verification note**: The abstract names "Vision Transformer (ViT)"; the specific citation/variant used is not available from provided input (no full text).

## RW03: He et al. — ResNet50 (deep residual networks)
- **DOI**: arXiv:1512.03385 (not stated in provided input; canonical ResNet reference)
- **Type**: baseline
- **Delta**:
  - What changed: ResNet50 is used via transfer learning as a CNN baseline on the EEG time-frequency images.
  - Why: Provides a strong pretrained convolutional backbone to compare against ViT.
- **Claims affected**: C02
- **Adopted elements**: Pretrained ResNet50 backbone (transfer learning).
- **Verification note**: Named in the abstract ("transfer learning with ResNet50 yielded 80.69%"); pretraining source/fine-tuning scheme not available from provided input (no full text).

## RW04: Simonyan & Zisserman — VGG16
- **DOI**: arXiv:1409.1556 (not stated in provided input; canonical VGG reference)
- **Type**: baseline
- **Delta**:
  - What changed: VGG16 is used via transfer learning as the weakest-reported CNN baseline on the EEG images.
  - Why: A second pretrained convolutional backbone for comparison.
- **Claims affected**: C02
- **Adopted elements**: Pretrained VGG16 backbone (transfer learning).
- **Verification note**: Named in the abstract ("VGG16 attained 79.82%"); details not available from provided input (no full text).

## RW05: Prokhorenkova et al. — CatBoost
- **DOI**: arXiv:1706.09516 (not stated in provided input; canonical CatBoost reference)
- **Type**: imports (method)
- **Delta**:
  - What changed: CatBoost (gradient-boosted trees) is stacked on top of custom-CNN features as a hybrid image-level classifier.
  - Why: Tests whether a boosted-tree head on learned CNN features improves over the plain CNN.
- **Claims affected**: C02
- **Adopted elements**: The CatBoost gradient-boosting classifier.
- **Verification note**: Named in the abstract ("CNN paired with CatBoost achieved 81.66%"); the CNN feature interface is not available from provided input (no full text).

## Briefer / background citations (not recoverable)
- **STFT and CWT** as signal-transformation techniques are invoked by the abstract but not attributed to a specific citation in the provided input.
- The abstract asserts "a significant correlation between an impaired sense of smell and the onset of early AD" and "recent studies" on deep learning for neurodegenerative diagnosis; the specific supporting references are **not available from provided input (no full text)**.
