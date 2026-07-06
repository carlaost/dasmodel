# Experiments

> Grounding: abstract-only. These are DIRECTIONAL verification plans reconstructed from the abstract;
> no exact numbers appear here (they live, as far as available, in the abstract-cited claims). The
> paper's actual splits, folds, preprocessing, and hyperparameters are not available from provided
> input (no full text), so Setup fields state what the abstract implies and mark the rest.

## E01: Compare deep classifiers on time-frequency EEG images
- **Verifies**: C01, C02, C04
- **Setup**:
  - Models: Vision Transformer (ViT); custom CNN; custom CNN + CatBoost; ResNet50 (transfer learning); VGG16 (transfer learning)
  - Hardware: Not available from provided input (no full text)
  - Dataset: Olfactory-evoked EEG cohort, 35 seniors (Mendeley DOI 10.17632/sgzbgwjfkr.5), converted to time-frequency images
  - System: Image-classification pipeline over EEG-derived time-frequency images
- **Procedure**:
  1. Transform each subject's olfactory-evoked EEG into time-frequency images (STFT and CWT — see E03).
  2. Train each classifier on the image set (split protocol not available from provided input).
  3. Evaluate each classifier at the image level.
  4. Rank models by image-level accuracy.
- **Metrics**: Classification accuracy (%) at the image level (further metrics not available from provided input).
- **Expected outcome**:
  - The Vision Transformer attains the highest image-level accuracy.
  - CNN+CatBoost > CNN > ResNet50 > VGG16 at the image level (ordering as reported).
- **Baselines**: Custom CNN, CNN+CatBoost, ResNet50, VGG16 (relative to ViT).
- **Dependencies**: E03

## E02: Rank CNN-family baselines at image level
- **Verifies**: C02
- **Setup**:
  - Models: custom CNN, custom CNN + CatBoost, ResNet50 transfer learning, VGG16 transfer learning
  - Hardware: Not available from provided input (no full text)
  - Dataset: Same olfactory-EEG image set as E01
  - System: Image-level evaluation
- **Procedure**:
  1. Hold model input (time-frequency images) fixed across the CNN-family classifiers.
  2. Measure image-level accuracy for each.
  3. Order them and compare against the ViT result from E01.
- **Metrics**: Image-level classification accuracy (%).
- **Expected outcome**:
  - CNN+CatBoost is the strongest CNN-family model; VGG16 is the weakest; all fall below the ViT.
- **Baselines**: The four CNN-family models compared against each other and against ViT.
- **Dependencies**: E01

## E03: Compare EEG-to-image transforms (STFT vs CWT), patient-wise
- **Verifies**: C01, C03
- **Setup**:
  - Transforms: Short-Time Fourier Transform (STFT); Continuous Wavelet Transform (CWT)
  - Models: the classifiers of E01 (ViT emphasized)
  - Dataset: Olfactory-evoked EEG cohort
  - System: Two parallel image pipelines differing only in the transform
- **Procedure**:
  1. Generate STFT-based and CWT-based image sets from the same EEG.
  2. Train/evaluate classifiers on each image set.
  3. Aggregate predictions to the patient level.
  4. Compare patient-wise performance between transforms.
- **Metrics**: Patient-level classification accuracy (%); relative transform ranking.
- **Expected outcome**:
  - CWT yields higher patient-wise performance than STFT; CWT+ViT is the best overall configuration.
- **Baselines**: STFT pipeline as the comparison transform.
- **Dependencies**: none

## E04: Establish olfactory-evoked EEG as an above-chance AD biomarker
- **Verifies**: C04, C05
- **Setup**:
  - Data: Olfactory-evoked EEG (rose/lemon oddball), 35 seniors — 13 AD, 7 aMCI, 15 healthy
  - Models: the full model set of E01
  - System: Diagnostic classification on olfactory-stimulus-evoked EEG
- **Procedure**:
  1. Use olfactory-evoked EEG (not resting-state) as the input signal.
  2. Run the full transform + classifier pipeline.
  3. Confirm that best-model accuracy is well above chance for the class structure.
- **Metrics**: Diagnostic accuracy (%) at patient and image level; comparison against chance.
- **Expected outcome**:
  - Multiple models exceed chance-level accuracy on olfactory-evoked EEG, supporting the biomarker's usefulness for early AD detection.
- **Baselines**: Chance level for the cohort's class distribution (a resting-state or non-olfactory baseline, if any, is not available from provided input — no full text).
- **Dependencies**: E01, E03
