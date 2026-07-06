# Experiments

> Grounding: abstract-only. These are directional verification plans reconstructed from the
> abstract's Methods/Results summary and the verified dataset record. They contain NO exact
> numbers (those live in claims.md / would live in evidence/). Full experimental protocol
> (splits, epochs, optimizer, hardware) was not available from provided input (no full text) and
> is marked accordingly.

## E01: Comparative training and evaluation of three CNN architectures (augmented test set)
- **Verifies**: C01, C02
- **Setup**:
  - Models: MobileNet-V3 Large, EfficientNet-B4, ResNet-50
  - Hardware: Not available from provided input (no full text)
  - Dataset: Augmented Alzheimer MRI Dataset (Kaggle, uraninjo) — 33,984 augmented 2D MRI images across four severity classes
  - System: PyTorch 2.5.1, TIMM 1.0.15 (per `sources.yaml`)
- **Procedure**:
  1. Train each of the three architectures on the augmented Kaggle dataset.
  2. Evaluate each trained model on the augmented test set.
  3. Record classification accuracy and total parameter count per model.
  4. Rank models by accuracy and by parameter count.
- **Metrics**: Classification accuracy (%); model parameter count (millions). Additional metrics (precision/recall/F1/confusion matrices) not available from provided input (no full text).
- **Expected outcome**:
  - MobileNet-V3 Large ranks highest on augmented-test accuracy.
  - MobileNet-V3 Large has the fewest parameters of the three.
- **Baselines**: EfficientNet-B4 and ResNet-50 serve as the comparison architectures.
- **Dependencies**: none

## E02: Generalization evaluation on the original (non-augmented) dataset
- **Verifies**: C01
- **Setup**:
  - Models: the three trained architectures from E01 (primary interest: MobileNet-V3 Large)
  - Hardware: Not available from provided input (no full text)
  - Dataset: Original (non-augmented) Alzheimer MRI images — 6,400 source images across four classes (per `sources.yaml`)
  - System: PyTorch 2.5.1, TIMM 1.0.15
- **Procedure**:
  1. Take the models trained on the augmented data.
  2. Evaluate them on the original (non-augmented) dataset.
  3. Compare accuracy on the original dataset against accuracy on the augmented test set.
- **Metrics**: Classification accuracy (%) on the original dataset.
- **Expected outcome**:
  - MobileNet-V3 Large maintains high accuracy on the original dataset (directionally comparable to, or higher than, its augmented-test accuracy), indicating generalization beyond the augmented distribution.
- **Baselines**: Augmented-test accuracy from E01 for the same models.
- **Dependencies**: E01

## E03: XRAI explainability and neuroanatomical alignment assessment
- **Verifies**: C03, C05
- **Setup**:
  - Model: best classifier (MobileNet-V3 Large)
  - Explainer: XRAI (Saliency library XRAI module, per `sources.yaml`)
  - Dataset: brain MRI slices across the four severity classes
- **Procedure**:
  1. Generate XRAI region-based attribution maps for classified MRI slices.
  2. Overlay / compare the highlighted regions against known neuroanatomical patterns of AD progression.
  3. Qualitatively assess whether attributions concentrate on AD-relevant anatomy.
- **Metrics**: Qualitative correspondence between attributed regions and known AD neuroanatomy. Quantitative overlap metric (if any) not available from provided input (no full text).
- **Expected outcome**:
  - XRAI attributions align with regions known to be affected in AD progression, supporting clinical interpretability.
- **Baselines**: Known neuroanatomical AD-progression patterns (clinical prior).
- **Dependencies**: E01

## E04: Deployment latency and confidence on the Gradio web interface
- **Verifies**: C04
- **Setup**:
  - System: Gradio-based web clinical interface wrapping the MobileNet-V3 Large classifier and XRAI explainer
  - Hardware: Not available from provided input (no full text)
  - Inputs: brain MRI slices spanning all four AD severity levels
- **Procedure**:
  1. Submit MRI inputs through the deployed web interface.
  2. Measure end-to-end inference time (prediction + explanation) per input.
  3. Record the model's classification confidence per severity level.
- **Metrics**: End-to-end inference latency (seconds); classification confidence per severity class.
- **Expected outcome**:
  - End-to-end inference completes within a low, clinically acceptable latency (the paper's stated target is sub-20 seconds) with high confidence across all four severity levels. (Exact latency/confidence values live in claims.md / would live in evidence.)
- **Baselines**: None stated.
- **Dependencies**: E01, E03
