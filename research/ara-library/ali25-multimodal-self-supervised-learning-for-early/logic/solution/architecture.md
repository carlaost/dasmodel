# Architecture

Source: §3.5, Figures 3–6. This is a component/dataflow description; the paper provides a schematic
(Figure 4, 5, 6) but no released code.

## Components

### MRI encoder $f^{MRI}_\theta$ and PET encoder $f^{PET}_{\theta'}$
- **Purpose**: Map 3D MRI / PET volumes to modality-specific feature representations.
- **Inputs**: Preprocessed, harmonized 3D volumes $x^{MRI}_{p,t}, x^{PET}_{p,t}\in\mathbb{R}^{H\times W\times D}$.
- **Outputs**: Feature maps → projection head.
- **Key design choices**: Backbone is **3D ResNet-50** (efficiency, strong volumetric performance) **or 3D Swin Transformer** (window-based self-attention for long-range anatomical dependencies; stated superior to earlier medical transformers like MedViT). Two separate encoders (one per modality).

### Projection head $g_\phi$
- **Purpose**: Project encoder features to an $\ell_2$-normalized embedding $z\in\mathbb{R}^d$.
- **Inputs**: Encoder features.
- **Outputs**: Normalized embedding used by all SSL losses.
- **Key design choices**: Projection MLP with **Norm–ReLU–Linear** structure.

### In-network normalization
- **Purpose**: Reduce site-specific batch-statistic drift.
- **Key design choices**: **GroupNorm** or **Domain-Specific BatchNorm (DSBN)** (ablated in §3.8).

### SSL objective block (Stage 1)
- **Purpose**: Compute the five self-supervised losses (Eq. 1–6) and their weighted sum (Eq. 7).
- **Inputs**: Embeddings $z$ from both encoders, optional MoCo queue $M$, site labels $s_p$.
- **Interactions**: The site discriminator $D_\psi$ receives embeddings through a gradient-reversal layer; BYOL predictor $q_\omega$ produces predictions with a stop-gradient target.

### Missing-aware gating fusion (Stage 2)
- **Purpose**: Blend MRI and PET embeddings into a fused vector $e$ tolerant to missing PET.
- **Inputs**: $z^{MRI}, z^{PET}$, availability indicators $\mathbb{1}_{MRI},\mathbb{1}_{PET}$, clinical covariates $c$.
- **Outputs**: Fused representation $e=[\alpha z^{MRI}\Vert(1-\alpha)z^{PET}\Vert c]$ (Eq. 8).
- **Key design choices**: Learned scalar gate $\alpha=\sigma(w^\top[\mathbb{1}_{MRI},\mathbb{1}_{PET}])$; late fusion at embedding level; MRI-only when PET absent.

### Diagnosis head $h_\psi$
- **Purpose**: Output class logits $l\in\mathbb{R}^K$ for AD/CN (and multi-class CN/EMCI/LMCI/AD).
- **Inputs**: Fused $e$. **Outputs**: Logits → class-weighted CE (Eq. 9) → temperature-scaled probabilities (Eq. 12).

### Survival head $r_\varphi$
- **Purpose**: Produce a risk score $r$ for MCI→AD prognosis.
- **Inputs**: Fused $e$. **Outputs**: Risk score → Cox partial log-likelihood (Eq. 10). DeepHit noted optional (Figure 6).

### PET→MRI distillation path
- **Purpose**: Transfer molecular (PET) information into the MRI encoder for MRI-only deployment.
- **Inputs**: Paired $z^{MRI}, z^{PET}$ (PET as stop-gradient teacher).
- **Outputs**: Distillation loss (Eq. 11), training-only.

### Harmonization pipeline (offline, pre-encoder)
- **Purpose**: Reduce scanner/site intensity variability.
- **Design**: Two-stage — (1) whole-brain histogram matching to an ADNI-derived reference template; (2) ComBat with site/scanner as batch variable and age/sex as protected covariates. Applied per modality and identically across a subject's timepoints.

## Dataflow (execution order)
Raw MRI/PET → preprocessing → harmonization → augmentation → dual encoders → projection heads →
**Stage 1** SSL losses (intra, cross, longitudinal, BYOL, site-adversarial) → pretrained weights →
**Stage 2** initialize encoders → gating fusion (+ clinical covariates) → diagnosis (CE) & prognosis
(Cox) heads (+ PET→MRI distillation) → temperature-scaling calibration → **Stage 3** evaluation
(ID 5-fold CV / OOD transfer / MIRIAD reliability).

## Optimization (§3.5)
- SSL: AdamW, lr $1\times10^{-3}$; Fine-tuning: AdamW, lr $3\times10^{-4}$.
- Both: cosine LR schedule, weight decay $1\times10^{-4}$.
- Subject-level, site-aware sampling; longitudinal pairs ($t_1\neq t_2$) included per epoch when available.
- Early stopping monitors validation balanced accuracy (diagnosis) and C-index (prognosis).
