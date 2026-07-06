# Dataset — Augmented Alzheimer MRI Dataset (Kaggle)

> Grounding: verified from `sources.yaml` (first-class grounded input, already verified) and the
> paper's abstract. This is the sole external data source for the study.

## Provenance
- **Name**: Augmented Alzheimer MRI Dataset
- **Uploader / curator**: uraninjo (Kaggle user)
- **Identifier / URL**: `kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset`
- **Repository**: Kaggle
- **Cited in paper as**: reference [12] (per `sources.yaml`).
- **Access type**: open (verified live via the Kaggle page, per `sources.yaml`).
- **License**: Not available from provided input (no full text; Kaggle page terms apply).

## Contents
- **Modality**: 2D brain MRI slices, T1/T2 axial.
- **Classes (4, AD severity)**: NonDemented, VeryMildDemented, MildDemented, ModerateDemented.
- **Size**:
  - Augmented images: **33,984** (used for training / augmented test set).
  - Original source images: **6,400** (used for the "original dataset" evaluation).

## Usage in this study
- Models (MobileNet-V3 Large, EfficientNet-B4, ResNet-50) trained on the augmented set.
- Evaluated on both the augmented test set and the original (non-augmented) dataset.
- Train/validation/test split ratios, per-class counts, and preprocessing beyond the source's own augmentation: Not available from provided input (no full text).

## Ethics
- Retrospective analysis of a public dataset. IRB approval and informed consent: "Not applicable"; no clinical-trial or PROSPERO registration (per `sources.yaml`).

## Notes
- The dataset is *pre-augmented by the third-party curator*; the augmentation transforms and the mapping between the 33,984 augmented and 6,400 original images are defined by the Kaggle source, not the paper. Evaluating on both the augmented and original sets is the paper's stated generalization check.
