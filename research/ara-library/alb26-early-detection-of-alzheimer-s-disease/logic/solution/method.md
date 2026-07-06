# Method — Olfactory-evoked EEG → time-frequency image → deep classifier

> Grounding: abstract-only. This is a **prose-level reconstruction** of the pipeline as described in
> the abstract. The paper describes the method in natural language in the provided input; no code,
> pseudocode, equations, or hyperparameters are available, so none are re-encoded (per Rule 14 the
> method lives here in `logic/`, not as a fabricated `src/` stub). Fields the abstract does not
> support read "Not available from provided input (no full text)".

## Pipeline overview

The approach converts olfactory-evoked EEG into images and classifies them:

1. **Input signal** — EEG recorded from seniors while exposed to olfactory stimuli (a rose/lemon
   olfactory oddball paradigm in the reused cohort). Olfaction is chosen because impaired smell
   correlates with early AD, so the evoked EEG is expected to carry a discriminative biomarker.
2. **Time-frequency transformation** — Each EEG segment is transformed into a 2-D time-frequency
   image using one of two transforms, evaluated as alternatives:
   - **Short-Time Fourier Transform (STFT)** → spectrogram (fixed-resolution).
   - **Continuous Wavelet Transform (CWT)** → scalogram (multi-resolution). CWT gave the best
     patient-wise performance.
3. **Image classification** — The time-frequency images are fed to deep-learning image classifiers:
   - **Vision Transformer (ViT)** — best overall (best patient-level and image-level accuracy).
   - **Custom CNN** — convolutional baseline.
   - **Custom CNN + CatBoost** — CNN features fed to a gradient-boosted-tree classifier.
   - **ResNet50** — transfer-learning CNN backbone.
   - **VGG16** — transfer-learning CNN backbone.
4. **Evaluation at two granularities**:
   - **Image level** — accuracy over individual time-frequency images.
   - **Patient level** — predictions aggregated per subject (the more clinically meaningful level;
     CWT was highest here). The exact aggregation rule (e.g. majority vote over a patient's images)
     is not available from provided input (no full text).

## Design choices (from the abstract)

- Two transforms (STFT, CWT) are compared rather than committing to one — CWT selected on
  patient-wise performance.
- Both a from-scratch model (custom CNN), hybrid model (CNN+CatBoost), transfer-learning CNNs
  (ResNet50, VGG16), and an attention-based model (ViT) are compared — ViT selected as best.
- Results are reported at both image and patient level, foregrounding the patient level.

## Not available from provided input (no full text)

- EEG preprocessing (filtering, artifact rejection, epoching, channel selection).
- Transform parameters (STFT window/hop; CWT mother wavelet, scales; image size, colormap).
- Model configuration (ViT patch size / pretraining; CNN architecture; transfer-learning
  freeze/fine-tune scheme; CatBoost feature source and hyperparameters).
- Train/validation/test split, cross-validation scheme, class grouping (how aMCI is handled),
  loss, optimizer, epochs, and any class-imbalance handling.
- Metrics beyond accuracy (sensitivity, specificity, AUC, confusion matrices).
