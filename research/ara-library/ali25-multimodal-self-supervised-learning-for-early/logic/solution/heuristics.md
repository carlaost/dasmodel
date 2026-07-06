# Heuristics — Stated Implementation Choices

Only heuristics explicitly stated by the paper are listed. Values not given are "Not specified in paper".

## H01: Subject-level, site-aware sampling to prevent leakage
- **Rationale**: All train/val/test splits are performed at the subject level so every timepoint of a patient stays in one fold, preventing temporal leakage; sampling is site-aware.
- **Sensitivity**: Not specified in paper (framed as a correctness requirement, not a tuned knob)
- **Bounds**: All folds; longitudinal pairs ($t_1\neq t_2$) included per epoch when available
- **Code ref**: Not specified
- **Source**: §3.1, §3.5, §3.7

## H02: Missing-aware gating fallback to MRI-only
- **Rationale**: The learned gate $\alpha=\sigma(w^\top[\mathbb{1}_{MRI},\mathbb{1}_{PET}])$ drives $\alpha\!\to\!1$ (so $(1-\alpha)\!\to\!0$) when PET is missing, enabling robust MRI-only inference in clinics where PET is scarce.
- **Sensitivity**: Not specified in paper
- **Bounds**: $\alpha\in[0,1]$; late fusion at embedding level
- **Code ref**: Not specified
- **Source**: §3.4, Eq. 8, Figure 5

## H03: Train-time PET→MRI distillation for MRI-only deployment
- **Rationale**: When both modalities are present in training, distilling stop-gradient PET embeddings into the MRI pathway (Eq. 11) retains molecular knowledge for later MRI-only inference.
- **Sensitivity**: Not specified in paper
- **Bounds**: Active only for subjects with PET; training-only (not at inference)
- **Code ref**: [src/execution/ssl_losses.py](../../src/execution/ssl_losses.py)
- **Source**: §3.4, Eq. 11

## H04: BYOL stop-gradient to prevent collapse without negatives
- **Rationale**: A BYOL-style predictor with a stop-gradient target branch stabilizes training without negative pairs, complementing the contrastive terms.
- **Sensitivity**: Not specified in paper
- **Bounds**: Stop-gradient applied to the target branch
- **Code ref**: [src/execution/ssl_losses.py](../../src/execution/ssl_losses.py)
- **Source**: §3.3, Eq. 5

## H05: Two-stage harmonization applied identically across a subject's timepoints
- **Rationale**: Histogram matching then ComBat (with age/sex protected) removes scanner/site effects while preserving anatomy; applying the identical transform to all of a subject's visits preserves longitudinal consistency.
- **Sensitivity**: high — §3.8 plans to remove histogram matching / ComBat / both and measure cross-site impact (results not reported)
- **Bounds**: Per modality; ADNI-derived reference template for histogram matching
- **Code ref**: Not specified
- **Source**: §3.2

## H06: Medically safe augmentations only
- **Rationale**: Restrict augmentations to transforms that do not destroy diagnostic anatomy — flips, ≤10° rotations, Gaussian blur, ±10% intensity jitter, random 3D crops — to define valid intra-modal positives.
- **Sensitivity**: Not specified in paper
- **Bounds**: Rotation ≤10°; intensity jitter ±10%
- **Code ref**: Not specified
- **Source**: §3.3

## H07: Linear-probe checkpoint selection
- **Rationale**: The best SSL checkpoint is chosen by linear probes (no fine-tuning) on a held-out validation fold, decoupling representation quality from downstream head training.
- **Sensitivity**: Not specified in paper
- **Bounds**: Small validation split
- **Code ref**: Not specified
- **Source**: §3.3, §3.7

## H08: Post-hoc temperature scaling with frozen encoders
- **Rationale**: Temperature $T$ (Eq. 12) is fit on validation predictions after training, without updating encoder weights, to produce calibrated probabilities for risk communication.
- **Sensitivity**: Not specified in paper
- **Bounds**: $T>0$
- **Code ref**: Not specified
- **Source**: §3.4, Eq. 12
