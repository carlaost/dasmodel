# Stage 1 — Self-Supervised Pretraining Config

Source: §3.3, §3.5. Values transcribed exactly; unspecified fields marked.

## Backbone
- **Value**: 3D ResNet-50 or 3D Swin Transformer + projection MLP (Norm–ReLU–Linear)
- **Rationale**: 3D ResNet for volumetric efficiency; 3D Swin for long-range anatomical dependencies via window self-attention
- **Search range**: {3D ResNet-50, 3D Swin Transformer}
- **Sensitivity**: Not specified in paper (2D vs 3D ablation planned in §3.8; results not reported)
- **Source**: §3.5

## Optimizer
- **Value**: AdamW, learning rate $1\times10^{-3}$
- **Rationale**: Not specified in paper
- **Search range**: Not specified
- **Sensitivity**: Not specified in paper
- **Source**: §3.3, §3.5

## LR schedule
- **Value**: Cosine decay
- **Rationale**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: §3.3, §3.5

## Weight decay
- **Value**: $1\times10^{-4}$
- **Source**: §3.3, §3.5

## Batch size
- **Value**: 32–64
- **Rationale**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: §3.3

## MoCo negative queue size
- **Value**: $\ge 8{,}000$ ($\ge 8$k)
- **Rationale**: Provide many negatives for InfoNCE
- **Source**: §3.3

## Temperature $\tau$
- **Value**: $\tau\in[0.05, 0.2]$
- **Rationale**: Contrastive softmax temperature
- **Search range**: $[0.05, 0.2]$
- **Sensitivity**: Not specified in paper
- **Source**: §3.3

## Loss weights $\lambda_1..\lambda_5$
- **Value**: Not specified in paper (Eq. 7 uses $\lambda_1..\lambda_5$; $\lambda_3$ shown weighting both BYOL and site terms)
- **Rationale**: Selected on a small validation split using linear probes (no fine-tuning)
- **Sensitivity**: Not specified in paper
- **Source**: §3.3, Eq. 7

## In-network normalization
- **Value**: GroupNorm or Domain-Specific BatchNorm (DSBN)
- **Rationale**: Reduce site-specific batch-statistic drift
- **Search range**: {GroupNorm, DSBN}
- **Sensitivity**: Not specified in paper (GroupNorm vs DSBN ablation planned §3.8)
- **Source**: §3.2, §3.5

## Checkpoint selection
- **Value**: Best SSL checkpoint chosen by linear probes on a held-out validation fold
- **Source**: §3.3, §3.7

## Augmentations
- **Value**: Flips, ≤10° rotations, Gaussian blur, ±10% intensity jitter, random 3D crops
- **Rationale**: Medically safe transforms defining intra-modal positives
- **Source**: §3.3

## Embedding dimension $d$
- **Value**: Not specified in paper
- **Source**: §3.1
