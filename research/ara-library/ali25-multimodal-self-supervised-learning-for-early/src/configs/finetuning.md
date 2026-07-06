# Stage 2 — Multi-Task Fine-Tuning Config

Source: §3.4, §3.5. Values transcribed exactly; unspecified fields marked.

## Encoder initialization
- **Value**: Initialized with the best SSL checkpoint (from Stage 1)
- **Rationale**: Transfer SSL-learned representations to downstream tasks
- **Source**: §3.4, §3.7

## Optimizer
- **Value**: AdamW, learning rate $3\times10^{-4}$
- **Rationale**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: §3.5

## LR schedule
- **Value**: Cosine decay
- **Source**: §3.5

## Weight decay
- **Value**: $1\times10^{-4}$
- **Source**: §3.5

## Fusion gate $\alpha$
- **Value**: Learned; $\alpha=\sigma(w^\top[\mathbb{1}_{MRI},\mathbb{1}_{PET}])\in[0,1]$
- **Rationale**: Missing-aware late fusion; $\alpha\to1$ when PET missing → MRI-only
- **Source**: §3.4, Eq. 8

## Diagnosis loss
- **Value**: Class-weighted cross-entropy (weights $w_k$), Eq. 9
- **Rationale**: Handle dataset class imbalance
- **Source**: §3.4, Eq. 9

## Survival loss
- **Value**: Cox partial log-likelihood, Eq. 10 (DeepHit optional per Figure 6)
- **Source**: §3.4, Eq. 10

## Distillation loss
- **Value**: PET→MRI L2 distillation with stop-gradient teacher, Eq. 11 (training-only)
- **Source**: §3.4, Eq. 11

## Joint objective weights $\alpha,\beta,\gamma$
- **Value**: Non-negative; specific values Not specified in paper (Eq. 13)
- **Source**: §3.4, Eq. 13

## Calibration
- **Value**: Post-hoc temperature scaling $T>0$ (Eq. 12), fit on a validation fold, encoder weights frozen
- **Source**: §3.4, §3.7, Eq. 12

## Early stopping
- **Value**: Monitors validation balanced accuracy (diagnosis) and C-index (prognosis)
- **Source**: §3.5

## Sampling
- **Value**: Subject-level, site-aware; longitudinal pairs ($t_1\neq t_2$) included per epoch when available
- **Source**: §3.5
