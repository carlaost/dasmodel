# Architecture (GTAD)

Grounded in Figure 1 and §2 of the paper (see `evidence/figures/figure1.md` for the visual
transcription). GTAD is an end-to-end pipeline of three stages, trained jointly by
backpropagating the classification loss all the way back to the per-modality diffusion scales.

## Components

### 1. Graph Input
- **Purpose**: Provide the per-subject brain graph and per-modality nodal features.
- **Inputs**: A subject's normalized graph Laplacian `L̂ ∈ R^{N×N}` (shared across modalities) and a
  set of modality features `X = {x^m}_{m=1}^{M}` defined on the same `N` nodes.
- **Outputs**: `(L̂, x^m)` pairs, one per modality `m`, fed to `M` parallel encoders.
- **Design choice**: The graph structure itself (edges/topology) is identical across modalities for
  a given subject — only the nodal feature vector changes per modality (§3).

### 2. Adaptive Convolution Block (×M encoders, ×Z layers each)
- **Purpose**: Produce a locally-effective (short-range) representation per modality by learning
  how far each node's diffusion should reach.
- **Inputs**: `L̂`, `x^m`, and a trainable initial scale vector `s^m ∈ R^N` per modality `m`.
- **Outputs**: `H^m_Z` — the modality-`m` node embedding after `Z` stacked adaptive-convolution
  layers.
- **Interactions**: Each of the `M` modality-specific encoder branches runs independently and in
  parallel (no cross-modality mixing yet at this stage); their `s^m` values are each updated by
  the loss gradient flowing back from the classifier (dotted "Scale Update" path in Fig. 1).
- **Key design choice**: A per-layer heat-kernel diffusion `e^{-s^m L̂}` — with `s^m` node-wise and
  trainable — replaces the fixed-scale diffusion used in prior diffusion-based GNNs (GraphHeat,
  GDC, ADC).

### 3. Self-Attention Block (×P layers)
- **Purpose**: Mix the `M` modality-specific local representations globally across all ROIs,
  producing a single graph-level representation that captures long-range dependencies.
- **Inputs**: `{H^m_Z}_{m=1}^{M}` used as `Q, K, V` for the first attention layer (`B_0`).
- **Outputs**: `B_P` — the transformer output after `P` stacked layers of
  {multi-head self-attention → add & norm → feed-forward → add & norm}.
- **Interactions**: Internally, `M` attention heads are used, **one per modality** (not a generic
  split of a single feature space) — each head's `Q^m, K^m, V^m` come from that modality's
  embedding; the `M` heads' outputs are concatenated and linearly mixed (`W^Φ`) before being fed
  into the feed-forward network. Residual connections and layer normalization stabilize training.
- **Key design choice**: Assigning attention heads to modalities (rather than to arbitrary
  representation subspaces) explicitly preserves a per-modality interpretability channel (used in
  §4, Fig. 3) while still enabling cross-modality/cross-ROI information flow through the shared
  `W^Φ` mixing and feed-forward network.

### 4. Classifier + Loss
- **Purpose**: Produce the final 3-way (CN/SMC/EMCI) graph-label prediction and the training signal.
- **Inputs**: `B_P` (transformer output for the whole graph).
- **Outputs**: `Ŷ_tj` — softmax class probabilities (Eq. 6); cross-entropy + ℓ1-scale-positivity
  loss `L` (Eq. 7).
- **Interactions**: `L` is backpropagated through the classifier, the self-attention block, and
  each modality's adaptive convolution block, including into the scale vectors `s^m` (via
  `s ← s − β ∂L/∂s`), closing the "Scale Update" loop shown in Fig. 1.
- **Key design choice**: A single end-to-end objective jointly trains local (scale) and global
  (attention) mechanisms rather than pretraining/freezing either stage.

## Data Flow Summary

```
Graph Input (L̂, {x^m})
   │
   ├─▶ [per modality m] Adaptive Convolution Block (×Z layers, scale s^m) ──▶ H^m_Z
   │                                                                            │
   └────────────────────────────────────────────────────────────────────────────┤
                                                                                 ▼
                                                          Self-Attention Block (×P layers,
                                                          one head per modality)  ──▶ B_P
                                                                                 │
                                                                                 ▼
                                                                       Classifier f_R ──▶ Ŷ
                                                                                 │
                                                                                 ▼
                                                                          Loss L (Eq. 7)
                                                                                 │
                                            (backprop) ◀────────────────────────┘
                                            updates: classifier, attention weights,
                                            per-modality W^m_z, and scales s^m
```

## Not specified in paper
- Exact values of `Z` (number of adaptive-convolution layers), `P` (number of attention layers),
  `C` (hidden dimension), number of attention heads beyond "one per modality", feed-forward network
  width, or the classifier `f_R`'s architecture (e.g. number of layers/units).
