# Grounding: reconstructed — from explicit paper equations (§3.3–§3.4, Eq. 1–13).
# No code repository was released (see src/environment.md). The functions below reconstruct the
# NOVEL loss mechanisms exactly as the paper's printed equations specify them. Anything the paper
# does not specify (loss weights, encoder bodies, projection dims) is left to the caller or raises
# NotImplementedError rather than being invented.
#
# Notation follows §3.1: z are L2-normalized embeddings in R^d; sim(u,v) = u^T v (cosine, since z is
# unit-norm); temperature tau > 0. Only PyTorch is used.

import torch
import torch.nn.functional as F


def intra_modal_infonce(z: torch.Tensor, z_pos: torch.Tensor, tau: float,
                        queue: torch.Tensor | None = None) -> torch.Tensor:
    """Intra-modal InfoNCE loss (Eq. 1, §3.3).

    Positives are two augmented views of the same scan within one modality (MRI<->MRI or PET<->PET).
    Negatives are the other batch samples B plus an optional MoCo queue M.

        L_intra = - sum_{i in B} log [ exp(sim(z_i, z_i+)/tau)
                                       / sum_{j in B∪M \ {i}} exp(sim(z_i, z_j)/tau) ]

    Args:
        z:      (B, d) L2-normalized anchor embeddings.
        z_pos:  (B, d) L2-normalized positive (second-view) embeddings.
        tau:    softmax temperature (paper: tau in [0.05, 0.2]).
        queue:  (M, d) optional MoCo negative queue, or None.
    """
    pos = torch.sum(z * z_pos, dim=-1, keepdim=True) / tau          # sim(z_i, z_i+)/tau -> (B,1)
    neg_batch = (z @ z.t()) / tau                                   # sim(z_i, z_j)/tau  -> (B,B)
    neg_batch.fill_diagonal_(float("-inf"))                         # exclude self (j != i)
    logits = torch.cat([pos, neg_batch], dim=1)                     # positive at column 0
    if queue is not None:
        neg_queue = (z @ queue.t()) / tau                           # (B, M)
        logits = torch.cat([logits, neg_queue], dim=1)
    target = torch.zeros(z.size(0), dtype=torch.long, device=z.device)
    return F.cross_entropy(logits, target, reduction="sum")


def cross_modal_infonce(z_mri: torch.Tensor, z_pet: torch.Tensor, tau: float,
                        queue_pet: torch.Tensor | None = None,
                        queue_mri: torch.Tensor | None = None) -> torch.Tensor:
    """Symmetric cross-modal InfoNCE (Eq. 2, §3.3), MRI and PET alternating as anchors.

    Positives are co-registered MRI-PET pairs at the same visit (z_mri_i, z_pet_i).

        L_cross = - sum_i log [ exp(sim(z_mri_i, z_pet_i)/tau) / sum_j exp(sim(z_mri_i, z_pet_j)/tau) ]
                  - sum_i log [ exp(sim(z_pet_i, z_mri_i)/tau) / sum_j exp(sim(z_pet_i, z_mri_j)/tau) ]
    """
    def _direction(anchor, other, queue):
        logits = (anchor @ other.t()) / tau                         # (B,B); diagonal = positives
        if queue is not None:
            logits = torch.cat([logits, (anchor @ queue.t()) / tau], dim=1)
        target = torch.arange(anchor.size(0), device=anchor.device)  # positive is column i
        return F.cross_entropy(logits, target, reduction="sum")

    return _direction(z_mri, z_pet, queue_pet) + _direction(z_pet, z_mri, queue_mri)


def longitudinal_consistency(embeddings_by_subject: list[torch.Tensor]) -> torch.Tensor:
    """Within-modality longitudinal consistency (Eq. 3, §3.3).

        L_long = sum_p sum_{t1 != t2 in T_p} || z_{p,t1} - z_{p,t2} ||_2^2

    Enabled only where repeat visits exist. Eq. 4 (cross-time cross-modal) has the same squared-L2
    form and is obtained by passing per-subject cross-modal embeddings.

    Args:
        embeddings_by_subject: list over subjects p; each entry is (T_p, d) visit embeddings.
    """
    total = torch.zeros((), device=embeddings_by_subject[0].device)
    for z_p in embeddings_by_subject:
        if z_p.size(0) < 2:
            continue
        diff = z_p.unsqueeze(0) - z_p.unsqueeze(1)                   # (T_p, T_p, d)
        sq = (diff ** 2).sum(-1)                                     # ||.||_2^2 over pairs
        total = total + sq.sum() - torch.diagonal(sq).sum()         # exclude t1 == t2
    return total


def byol_regression(z: torch.Tensor, z_pos: torch.Tensor, predictor) -> torch.Tensor:
    """BYOL-style negative-free regression with stop-gradient target (Eq. 5, §3.3).

        L_byol = sum_i || q_omega(z_i) - sg(z_i+) ||_2^2

    Args:
        predictor: the online predictor q_omega (an nn.Module supplied by the caller).
    """
    pred = predictor(z)
    target = z_pos.detach()                                         # sg(.) = stop-gradient
    return ((pred - target) ** 2).sum()


def site_adversarial(discriminator, z: torch.Tensor, site_labels: torch.Tensor) -> torch.Tensor:
    """Domain-adversarial site-invariance loss (Eq. 6, §3.3).

        L_site = E[ CE( D_psi(z), s_p ) ]

    A gradient-reversal layer (GRL) is applied to z before D_psi so encoder gradients are reversed;
    the paper does not print the GRL scaling schedule, so it is left to the caller's GRL module.
    Site labels are used ONLY here and never passed to the prediction heads.
    """
    logits = discriminator(z)
    return F.cross_entropy(logits, site_labels)


def total_ssl_loss(l_intra, l_cross, l_byol, l_long, l_long_x, l_site,
                   lam1, lam2, lam3, lam4, lam5) -> torch.Tensor:
    """Weighted total SSL objective (Eq. 7, §3.3), reproduced verbatim.

        L_SSL = lam1 L_intra + lam2 L_cross + lam3 L_byol + lam4 L_long + lam5 L_long_x + lam3 L_site

    Note (verbatim from the paper): lam3 weights BOTH L_byol and L_site. Concrete lambda values are
    'Not specified in paper' and must be supplied by the caller (selected via linear-probe validation).
    """
    return (lam1 * l_intra + lam2 * l_cross + lam3 * l_byol
            + lam4 * l_long + lam5 * l_long_x + lam3 * l_site)


def gated_fusion(z_mri, z_pet, avail_mri, avail_pet, gate_w, clinical):
    """Missing-aware gating late fusion (Eq. 8, §3.4).

        alpha = sigmoid( w^T [1_MRI, 1_PET] )
        e     = [ alpha * z_mri || (1 - alpha) * z_pet || c ]

    When PET is missing (avail_pet = 0), alpha -> 1 so the (1-alpha) branch vanishes -> MRI-only.
    """
    ind = torch.stack([avail_mri, avail_pet], dim=-1).float()       # (..., 2)
    alpha = torch.sigmoid(ind @ gate_w)                             # (...,)
    alpha = alpha.unsqueeze(-1)
    return torch.cat([alpha * z_mri, (1.0 - alpha) * z_pet, clinical], dim=-1)


def diagnosis_ce(logits: torch.Tensor, targets: torch.Tensor, class_weights: torch.Tensor) -> torch.Tensor:
    """Class-weighted cross-entropy diagnosis loss (Eq. 9, §3.4)."""
    return F.cross_entropy(logits, targets, weight=class_weights, reduction="mean")


def cox_partial_loglik(risk: torch.Tensor, times: torch.Tensor, events: torch.Tensor) -> torch.Tensor:
    """Cox partial log-likelihood for the survival head (Eq. 10, §3.4).

        L_cox = - sum_{n: delta_n = 1} [ r_n - log sum_{j in R(T_n)} exp(r_j) ],
        R(T_n) = { j : T_j >= T_n }   (risk set)
    """
    order = torch.argsort(times, descending=True)
    r = risk[order]
    log_cumsum = torch.logcumsumexp(r, dim=0)                       # log sum_{T_j >= T_n} exp(r_j)
    event_mask = events[order].bool()
    return -torch.sum((r - log_cumsum)[event_mask])


def pet_to_mri_distill(z_mri: torch.Tensor, z_pet: torch.Tensor, avail_pet: torch.Tensor) -> torch.Tensor:
    """Training-only PET->MRI distillation (Eq. 11, §3.4).

        L_distill = (1/N) sum_n 1_{PET,n} || z_mri_n - sg(z_pet_n) ||_2^2
    """
    per_sample = ((z_mri - z_pet.detach()) ** 2).sum(-1)            # (N,)
    per_sample = per_sample * avail_pet.float()                     # 1_{PET,n} mask
    return per_sample.mean()


def finetune_objective(l_diag, l_cox, l_distill, alpha, beta, gamma) -> torch.Tensor:
    """Joint multi-task fine-tuning objective (Eq. 13, §3.4).

        L_FT = alpha * L_diag + beta * L_cox + gamma * L_distill,   alpha, beta, gamma >= 0

    Concrete alpha/beta/gamma values are 'Not specified in paper'.
    """
    return alpha * l_diag + beta * l_cox + gamma * l_distill
