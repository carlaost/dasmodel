# Method (abstract-level reconstruction)

> Grounding: abstract-only. This is a reconstruction of the pipeline at the granularity the
> abstract supports, cross-referenced with `sources.yaml`. It is NOT a full method transcription —
> the paper's full text was unavailable (the provided PDF is a different article; see PAPER.md).
> Every step below traces to the abstract or the verified dataset record; unspecified detail is
> marked "Not available from provided input (no full text)".

## Pipeline overview

The system is an end-to-end explainable AD-severity classifier with a clinical web front-end:

1. **Data** → Augmented Alzheimer MRI Dataset (Kaggle, uraninjo): 33,984 augmented 2D MRI images
   across four severity classes, plus 6,400 original source images used for a second evaluation.
2. **Models** → Three CNN architectures trained on the augmented data: MobileNet-V3 Large,
   EfficientNet-B4, ResNet-50.
3. **Evaluation** → Each model evaluated on (a) the augmented test set and (b) the original
   (non-augmented) dataset.
4. **Explainability** → XRAI (Saliency library module) generates region-based attribution maps for
   the classifier's predictions; maps compared to known AD neuroanatomy.
5. **Deployment** → A Gradio web interface wraps the selected model (MobileNet-V3 Large) and the
   XRAI explainer to deliver real-time predictions and visual explanations.

## Components

### Data ingestion
- **Inputs**: 2D axial T1/T2 brain MRI slices, labelled into four severity classes.
- **Preprocessing / augmentation**: The dataset is pre-augmented by the source; the paper's own
  additional preprocessing (resizing, normalization, split ratios) is Not available from provided
  input (no full text).

### Classifier backbones
- **MobileNet-V3 Large** — selected as the deployed model (highest accuracy, fewest parameters: 4.2M).
- **EfficientNet-B4** — comparison architecture.
- **ResNet-50** — comparison architecture.
- Training regime (optimizer, learning rate, epochs, loss, seeds): Not available from provided input (no full text). Framework: PyTorch 2.5.1 + TIMM 1.0.15 (per `sources.yaml`).

### XRAI explainability module
- **Function**: Produces region-based attribution maps ranking image regions by contribution to the
  predicted class. Implemented via the Saliency library's XRAI module (per `sources.yaml`).
- **Evaluation**: Qualitative comparison of highlighted regions to known neuroanatomical patterns of
  AD progression. Parameterization: Not available from provided input (no full text).

### Gradio clinical web interface
- **Function**: Real-time prediction + visual explanation delivery to clinicians; sub-20-second
  inference reported.
- **Hosting / hardware / concurrency**: Not available from provided input (no full text).

## Design rationale (per abstract)
- Favour the lowest-parameter architecture that maximizes accuracy (MobileNet-V3 Large) to reconcile
  the accuracy-vs-efficiency trade-off for clinical use.
- Add XRAI to convert an opaque classifier into a clinician-interpretable tool.
- Wrap everything in a web UI to address the usability barrier to clinical deployment.
