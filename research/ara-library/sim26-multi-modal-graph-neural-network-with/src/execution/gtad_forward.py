# Grounding: reconstructed — from paper §2, Eq. 1-7 (no repository or code release
# accompanies this paper; every numeric constant / shape below not stated in the
# equations is left unimplemented rather than guessed).
#
# This is a minimal, non-runnable structural reconstruction of the GTAD forward pass
# and loss, using only the symbols and operations the paper explicitly states.
# Values such as Z (# conv layers), P (# attention layers), C (hidden dim),
# alpha (loss weight), beta (scale learning rate), and the classifier f_R's
# architecture are NOT specified in the paper, so those sites raise
# NotImplementedError("Not specified in paper") rather than inventing values.

from typing import List, Dict
import torch
from torch import Tensor


def heat_kernel_diffusion(L_hat: Tensor, s_m: Tensor) -> Tensor:
    """Eq. 1-2: heat-kernel diffusion operator exp(-s^m * L_hat).

    Args:
        L_hat: normalized graph Laplacian, shape (N, N).
        s_m: trainable per-node scale for modality m, shape (N,).

    Returns:
        Diffusion operator, shape (N, N).

    Source: §2, "Prelim: Graph Kernel Convolution" and Eq. (1)-(2).
    The paper does not specify whether s^m scales L_hat elementwise, per-row,
    or via a diagonal matrix exponential — this detail is not given, so the
    exact tensor contraction is left unspecified.
    """
    raise NotImplementedError(
        "Not specified in paper: exact tensor form of e^{-s^m L_hat} "
        "(diagonal scaling vs. matrix exponential) is not given in §2."
    )


def adaptive_convolution_layer(
    H_prev: Tensor, L_hat: Tensor, s_m: Tensor, W_m_z: Tensor, sigma_z
) -> Tensor:
    """Eq. 3: H^m_z = sigma_z( e^{-s^m L_hat} H^m_{z-1} W^m_z ).

    Args:
        H_prev: previous layer embedding H^m_{z-1}, shape (N, d_{z-1}).
        L_hat: normalized graph Laplacian, shape (N, N).
        s_m: trainable per-node scale for modality m, shape (N,).
        W_m_z: trainable weight matrix for layer z, modality m.
        sigma_z: nonlinear activation function (not named in paper).

    Returns:
        H^m_z, shape (N, d_z).

    Source: §2, Eq. (3).
    """
    diffusion = heat_kernel_diffusion(L_hat, s_m)
    return sigma_z(diffusion @ H_prev @ W_m_z)


def modality_wise_attention(
    Q_m: Tensor, K_m: Tensor, V_m: Tensor, C: int
) -> Tensor:
    """Eq. 4: phi(Q^m, K^m, V^m) = softmax(Q^m K^{mT} / sqrt(C)) V^m.

    Args:
        Q_m, K_m, V_m: per-modality query/key/value, each shape (N, C).
        C: hidden-unit dimension (value not specified in paper).

    Returns:
        Per-modality attention output h^m, shape (N, C).

    Source: §2, "Modality-wise Self-Attention Block", Eq. (4).
    """
    scores = (Q_m @ K_m.transpose(-2, -1)) / (C ** 0.5)
    weights = torch.softmax(scores, dim=-1)
    return weights @ V_m


def multi_modal_attention(
    heads: List[Tensor], W_Phi: Tensor
) -> Tensor:
    """Combine per-modality attention heads: Phi(Q,K,V) = [h1|h2|...|hM] W_Phi.

    Args:
        heads: list of M per-modality attention outputs h^m, each (N, C).
        W_Phi: trainable mixing weight matrix.

    Source: §2, "Modality-wise Self-Attention Block" (unnumbered equation
    following Eq. 4).
    """
    concatenated = torch.cat(heads, dim=-1)
    return concatenated @ W_Phi


def transformer_layer(B_prev: Tensor, phi_out: Tensor, layer_norm, feed_forward) -> Tensor:
    """Eq. 5: B_p = f_L[f_L[B_{p-1} + Phi(B_{p-1})] + Psi(f_L[B_{p-1} + Phi(B_{p-1})])].

    Args:
        B_prev: previous attention-block output B_{p-1}.
        phi_out: Phi(B_{p-1}) from `multi_modal_attention`.
        layer_norm: layer-normalization callable f_L[.] (Ba et al. [1]).
        feed_forward: feed-forward network Psi(.) (architecture not specified
            in paper beyond "multiple linear transformations with a
            non-linear activation function in between").

    Source: §2, Eq. (5).
    """
    residual_1 = layer_norm(B_prev + phi_out)
    residual_2 = layer_norm(residual_1 + feed_forward(residual_1))
    return residual_2


def classify(B_P: Tensor, f_R) -> Tensor:
    """Eq. 6: Y_hat_tj = f_R(B_P)_tj / sum_{j'} f_R(B_P)_tj'.

    Args:
        B_P: final transformer output for the graph.
        f_R: classifier head (architecture not specified in paper).

    Returns:
        Softmax class probabilities Y_hat.

    Source: §2, "Transformer-Guided Scale Update", Eq. (6).
    """
    logits = f_R(B_P)
    return torch.softmax(logits, dim=-1)


def loss_fn(
    Y: Tensor, Y_hat: Tensor, scales: Dict[str, Tensor], alpha: float
) -> Tensor:
    """Eq. 7: L = -(1/T) sum_t sum_j Y_tj ln(Y_hat_tj)
               + alpha * (1/M) sum_m sum_n 1[s^m_n < 0] * |s^m_n|.

    Args:
        Y: one-hot true labels, shape (T, J).
        Y_hat: predicted class probabilities, shape (T, J).
        scales: dict mapping modality name -> scale vector s^m, shape (N,).
        alpha: user-parameter weighting the scale-positivity penalty
            (value not specified in paper).

    Returns:
        Scalar loss L.

    Source: §2, Eq. (7). Update rule s <- s - beta * dL/ds (beta = learning
    rate, value not specified in paper) is applied by the optimizer, not
    implemented here.
    """
    cross_entropy = -(Y * torch.log(Y_hat)).sum(dim=-1).mean()
    M = len(scales)
    penalty = sum(
        (s_m.clamp(max=0).abs()).sum() for s_m in scales.values()
    ) / M
    return cross_entropy + alpha * penalty
