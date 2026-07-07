# Algorithm / Formal Derivation

All equations below are transcribed exactly as given in §2 of the paper.

## 1. Preliminaries: Graph Laplacian and Heat Kernel

An undirected graph `G = {V, E}` with `N` nodes has adjacency matrix `A` and diagonal degree
matrix `D`. The graph Laplacian is

```
L = D − A
```

which is real and positive semi-definite, with a complete orthonormal eigenbasis
`U = [u1|u2|...|uN]` and non-negative eigenvalues `0 = λ1 ≤ λ2 ≤ ... ≤ λN`; the same holds for the
normalized Laplacian

```
L̂ = D^(-1/2) L D^(-1/2)
```

The heat kernel between nodes `p` and `q`, spanned by `U`, is

```
h_s(p, q) = Σ_{i=1}^{N} e^{-s λ_i} u_i(p) u_i(q)                         (Eq. 1)
```

`e^{-s λ_i}` acts as a low-pass filter, with smoothness controlled by scale `s`. Using the graph
Fourier transform `x̂ = U^T x`, the graph convolution of signal `x(p)` with filter `h_s` is

```
h_s * x(p) = Σ_{i=1}^{N} e^{-s λ_i} x̂(i) u_i(p)                          (Eq. 2)
```

whose bandwidth is controlled by `s`.

## 2. Modality-wise Adaptive Convolution Block

Given `L̂ ∈ R^{N×N}`, features `X = {x^m}_{m=1}^{M}` on `N` nodes from `M` modalities, trainable
multi-variate scales `{s^m}_{m=1}^{M}` with `s^m ∈ R^N`, and graph label `Y`, each modality-`m`
encoder stacks `Z` layers of:

```
H^m_z = σ_z( e^{-s^m L̂} H^m_{z-1} W^m_z )                                (Eq. 3)
```

where `H^m_0 = x^m`, `W^m_z` is a trainable weight matrix, and `σ_z` is a nonlinear activation.
`s^m` is trainable to capture each node's local characteristic per modality.

## 3. Modality-wise Self-Attention Block

The `M` embeddings `{H^m_Z}_{m=1}^{M}` feed a multi-head self-attention module (adapted from the
transformer [21]), with **each head assigned to one modality**. For modality `m`, query/key/value
`Q^m, K^m, V^m ∈ R^{N×C}` (C = hidden-unit dimension) give per-modality attention value

```
ϕ(Q^m, K^m, V^m) = σ( Q^m K^{mT} / √C ) V^m                               (Eq. 4)
```

(`σ` here = softmax.) The multi-modal attention function averages/mixes across modalities:

```
Φ(Q, K, V) = [h1 | h2 | ... | hm] W^Φ,   h^m = ϕ(Q^m W^{Qm}, K^m W^{Km}, V^m W^{Vm})
```

where `W^{Qm}, W^{Km}, W^{Vm}, W^Φ` are trainable weight matrices. A feed-forward network `Ψ(·)`
(multiple linear transforms + nonlinearity), residual connections, and layer normalization `f_L[·]`
produce, over `P` stacked attention layers:

```
B_p = f_L[ f_L[B_{p-1} + Φ(B_{p-1})] + Ψ(f_L[B_{p-1} + Φ(B_{p-1})]) ]      (Eq. 5)
```

with `{H^m_Z}_{m=1}^{M}` used as `Q, K, V` for `B_0`.

## 4. Transformer-Guided Scale Update (Classifier + Loss)

Given a set of graphs `{G_t}_{t=1}^{T}` with labels `{Y_t}_{t=1}^{T}`, the classifier `f_R(·)`
maps `B_P` to a prediction via softmax:

```
Ŷ_tj = f_R(B_P)_tj / Σ_{j'∈J} f_R(B_P)_tj'                                (Eq. 6)
```

(`J` = number of classes.) To update scale `s^m_n` at node `n` for modality `m`, the objective
combines cross-entropy with an ℓ1 penalty enforcing positive scales:

```
L = −(1/T) Σ_{t=1}^{T} Σ_{j=1}^{J} Y_tj ln Ŷ_tj  +  α (1/M) Σ_{m=1}^{M} Σ_{n=1}^{N} 1_{s<0} |s^m_n|   (Eq. 7)
```

(`α` = user parameter; `1` = indicator function.) Scales are updated by gradient descent:

```
s ← s − β ∂L/∂s
```

(`β` = learning rate.)

## Pseudocode (reconstructed from Eq. 1–7; illustrative only — see `src/execution/gtad_forward.py`
for the grounded, typed reconstruction)

```
Input: L̂ (N×N normalized Laplacian), {x^m}_{m=1..M} (N-dim feature per modality),
       trainable {s^m}_{m=1..M} (N-dim scale per modality), label Y

for m in 1..M:
    H = x^m
    for z in 1..Z:
        H = σ_z( exp(-s^m ⊙ L̂) @ H @ W^m_z )     # Eq. 3 (⊙/@ operator semantics not specified)
    H_Z[m] = H

B = stack(H_Z[1..M])                              # used as Q,K,V for B_0
for p in 1..P:
    per-modality heads: h^m = softmax(Q^m K^{mT} / sqrt(C)) V^m     # Eq. 4
    Phi = concat(h^1..h^M) @ W_Phi
    B = LayerNorm(B + Phi)
    B = LayerNorm(B + FeedForward(B))              # Eq. 5

Y_hat = softmax(f_R(B))                            # Eq. 6
L = cross_entropy(Y, Y_hat) + alpha * mean_m( sum_n( 1[s<0] * |s^m_n| ) )   # Eq. 7
s ← s − beta * dL/ds                                # gradient step on scales
```

## Complexity Analysis

Not specified in paper. The paper does not state time/space complexity for the heat-kernel
diffusion (which, if computed via full eigendecomposition, is `O(N^3)` per graph — a standard fact
about spectral methods but not asserted by this paper) or for the self-attention block (which,
following standard transformer scaling, would be `O(N^2)` per attention layer per modality — again
not asserted by the paper itself).
