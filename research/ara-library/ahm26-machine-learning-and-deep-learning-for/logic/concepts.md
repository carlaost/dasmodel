# Concepts

Genuine technical terms defined by the survey (or used with a specific technical sense in it).

## Structural MRI vs. PET modalities
- **Notation**: —
- **Definition**: Structural magnetic resonance imaging (MRI) is a non-invasive modality capturing
  anatomical degeneration (hippocampal atrophy, cortical thinning, ventricular enlargement, gray-matter
  loss). Positron emission tomography (PET) captures functional/molecular processes: FDG-PET measures
  cerebral glucose metabolism; amyloid PET measures amyloid-beta deposition. The survey treats them as
  complementary (structural vs metabolic) rather than redundant sources.
- **Boundary conditions**: MRI reveals structure; molecular abnormalities detectable on PET may precede
  visible structural change. Complementarity is the rationale for multimodal fusion (C01).
- **Related concepts**: Multimodal fusion, Benchmark cohorts (ADNI/OASIS/AIBL).

## Disease stages: CN, MCI, AD, and MCI-to-AD conversion
- **Notation**: CN / MCI / AD
- **Definition**: Diagnostic categories: cognitively normal (CN) controls, mild cognitive impairment
  (MCI, an intermediate heterogeneous stage), and Alzheimer's disease (AD) dementia. A key clinical
  task is predicting which MCI patients will convert to AD. Some studies also distinguish
  non-Alzheimer dementias.
- **Boundary conditions**: Binary AD-vs-CN is the easiest task; MCI separation and progression
  prediction are harder and more clinically relevant; multi-class staging is most demanding.
- **Related concepts**: Task/dataset heterogeneity, Accuracy-alone insufficiency.

## Traditional (handcrafted-feature) machine learning
- **Notation**: —
- **Definition**: Pipelines that extract handcrafted features (cortical thickness, volumetric
  measures, texture descriptors, clinical variables, brain-network statistics) and feed them to
  classifiers such as SVM, random forest, logistic regression, or boosting.
- **Boundary conditions**: Interpretable and low-compute; strong when feature engineering is
  clinically guided; limited when disease patterns are subtle/distributed; poor reproducibility due to
  varying feature pipelines.
- **Related concepts**: CNN, Methodological evolution (C02).

## Convolutional neural network (CNN)
- **Notation**: —
- **Definition**: Deep network that learns hierarchical spatial features directly from imaging via
  convolutional filters and pooling; used as 2D slice-based and 3D volumetric models for AD
  classification.
- **Boundary conditions**: Strong local spatial feature extraction; inherently local receptive
  fields limit global-context modeling; needs substantial data and regularization to avoid overfitting
  in medical settings.
- **Related concepts**: Transformer/self-attention, Multimodal fusion, GNN.

## Multimodal fusion (early / intermediate / late / attention-based)
- **Notation**: —
- **Definition**: Combining multiple information sources (MRI, PET, cognitive, demographic, genetic,
  biomarker). Fusion strategies: early fusion (combine raw/low-level features at input); intermediate/
  deep fusion (modality-specific branches merged mid-network); late fusion (combine per-modality
  decisions); attention-based fusion (adaptively weight modalities).
- **Boundary conditions**: Benefits depend on data quality, subject-level alignment, preprocessing
  consistency, and missing-modality handling; naive concatenation is weaker than learned fusion.
- **Related concepts**: Attention mechanism, GNN relational fusion, C01.

## Transformer / self-attention and hybrid CNN-transformer models
- **Notation**: —
- **Definition**: Architectures using attention/self-attention to model long-range dependencies and
  global context. Hybrid CNN-transformer models use a CNN front-end for local/textural features and a
  transformer for global contextual interactions among learned features.
- **Boundary conditions**: Data-hungry and compute-intensive; risky on small medical datasets; often
  require transfer learning or CNN-derived inductive biases; superiority over strong CNN baselines not
  yet established (C03).
- **Related concepts**: Attention-based fusion, CNN, GNN.

## Graph neural network (GNN)
- **Notation**: —
- **Definition**: Networks operating on non-Euclidean graph structures where nodes may be brain
  regions, subjects, or feature groups and edges encode anatomical connectivity, functional similarity,
  imaging relationships, or phenotypic associations. Suited to relational/network-level modeling of
  the brain and to multimodal relational fusion.
- **Boundary conditions**: Performance depends heavily on graph-construction choices (node/edge
  definitions), affecting reproducibility; sensitive to small samples and noisy connectivity.
- **Related concepts**: Multimodal fusion, Self-explainable GNN, C03.

## Explainable AI: post hoc vs. self-explainable (architecture-level)
- **Notation**: —
- **Definition**: Methods that surface which inputs drive predictions. Post hoc methods (Grad-CAM,
  SHAP, saliency maps, attention visualization) are applied after training. Self-explainable /
  architecture-level approaches (e.g., self-explainable GNNs with relation importance) build
  interpretability into the model design itself.
- **Boundary conditions**: A visually plausible explanation is not necessarily trustworthy; post hoc
  explanations can appear convincing while the model relies on spurious/confounding signals.
  Explanation quality is rarely evaluated for stability/plausibility/reproducibility (C05).
- **Related concepts**: Trust, GNN, Evaluation rigor.

## Benchmark dependence, external validation, and domain shift
- **Notation**: —
- **Definition**: Benchmark dependence is over-reliance on a small number of curated public datasets
  (especially ADNI). External validation tests a model on data from different institutions, scanners,
  or populations. Domain shift is the distributional difference (resolution, contrast, scanner, field
  strength, protocol) that degrades performance when a model is deployed elsewhere.
- **Boundary conditions**: Success on one benchmark does not imply clinical readiness; routine
  cross-site validation remains uncommon (C06).
- **Related concepts**: Reproducibility, Class imbalance, Clinical translation.
