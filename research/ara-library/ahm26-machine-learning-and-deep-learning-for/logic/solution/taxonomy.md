# Taxonomy of Methods and Comparative Framework

The survey's central organizing contribution: a taxonomy of six model families for AD diagnosis and a
comparative framework across practical dimensions. Grounded in "Taxonomy of Methods" (PDF p.629-633),
Figure 4 (taxonomy), Figure 6 (comparative framework), and Table 1.

## The six method families

### 1. Traditional machine learning
- **Inputs**: handcrafted features (cortical thickness, volumetric measures, texture descriptors,
  clinical variables, brain-network statistics).
- **Classifiers**: SVM, random forest, logistic regression, boosting.
- **Strengths**: interpretable, low-compute, effective in small datasets with careful feature design;
  useful baselines.
- **Limitations**: performance hinges on feature quality; cannot auto-learn hierarchical features;
  handcrafted pipelines vary across studies → poor reproducibility.

### 2. Convolutional neural networks (CNNs)
- **Inputs**: MRI or PET (2D slices → 3D volumes).
- **Strengths**: automatic hierarchical spatial feature learning; strong local pattern capture;
  compatible with transfer learning, ensembles, and multimodal fusion.
- **Limitations**: local receptive fields limit global-context modeling; data-hungry; overfitting risk
  in limited medical datasets.

### 3. Multimodal fusion
- **Inputs**: MRI + PET, optionally cognitive/demographic/genetic/biomarker variables.
- **Fusion strategies**: early (input-level), intermediate/deep (branch-level), late (decision-level),
  attention-based (adaptive modality weighting).
- **Strengths**: complementary structural + metabolic + clinical evidence; mirrors clinical reasoning;
  richer feature interaction beyond concatenation.
- **Limitations**: missing modalities, alignment/preprocessing sensitivity, increased complexity, hard
  cross-study comparison.

### 4. Transformer and hybrid attention models
- **Inputs**: imaging volumes (often 3D MRI); multimodal token sequences.
- **Strengths**: long-range dependency / global-context modeling; adaptive modality weighting in
  multimodal settings; hybrid CNN-transformer combines local + global.
- **Limitations**: data-hungry, compute-intensive, unstable on small datasets; superiority over strong
  CNN baselines not yet established.

### 5. Graph neural networks (GNNs)
- **Inputs**: brain graphs or subject graphs (nodes = regions/subjects/feature groups; edges =
  connectivity/similarity/phenotypic relations).
- **Strengths**: relational / non-Euclidean modeling of network-level degeneration; multimodal
  relational fusion; supports self-explainable variants.
- **Limitations**: sensitive to graph-construction choices (reproducibility); computationally complex;
  sensitive to small samples / noisy connectivity.

### 6. Explainable-AI-oriented models
- **Inputs**: multimodal or image-based.
- **Methods**: post hoc (Grad-CAM, SHAP, saliency, attention visualization); architecture-level
  self-explainable models (relation importance, graph attention).
- **Strengths**: improved transparency and trust; essential for clinical adoption.
- **Limitations**: explanation quality not standardized; visual plausibility ≠ trustworthiness.

## Comparative framework (Figure 6)
Qualitative comparison across five dimensions (transcribed in evidence/figures/figure6.md):

| Family | Typical Input | Key Strength | Main Limitation | Interpretability | Clinical Readiness |
|--------|--------------|--------------|-----------------|------------------|--------------------|
| Traditional ML | handcrafted features | simple and efficient | limited representation learning | moderate | moderate |
| CNN-based | MRI or PET | strong spatial learning | limited global context | low to moderate | moderate |
| Multimodal DL | MRI + PET + clinical | complementary information fusion | missing modality challenge | moderate | high potential |
| Transformer / Hybrid Attention | imaging volumes | global context modeling | data-hungry and complex | moderate | emerging |
| Graph Neural Networks | brain or subject graphs | relational modeling | graph design sensitivity | moderate to high | emerging |
| Explainable-AI-Oriented | multimodal or image-based | improved transparency | explanation quality not standardized | high | high potential |

## General pipeline (Figure 3)
Data acquisition (MRI, PET, clinical, cognitive, genetic/biomarker) → preprocessing (normalization,
registration, skull stripping, segmentation, feature preparation) → representation learning / feature
extraction (handcrafted, CNN-based, transformer-based, graph-based) → multimodal fusion (early /
intermediate / late / attention-based) → prediction/diagnosis (CN vs AD, MCI detection, progression
prediction, multi-class dementia classification) → interpretation/validation (Grad-CAM, SHAP, external
validation, clinical relevance).

## Methodological evolution (Figures 4-5)
Early stage (handcrafted features; SVM/RF) → CNN era (2D → 3D; end-to-end MRI classification) →
multimodal era (MRI+PET fusion; imaging + clinical integration; attention-based fusion) → relational
and global modeling (GNNs; transformer-based / hybrid CNN-transformer) → trustworthy and clinical AI
(explainable AI; external validation; longitudinal prediction; clinically deployable systems).
