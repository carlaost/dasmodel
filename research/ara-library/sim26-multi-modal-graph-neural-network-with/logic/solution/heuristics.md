# Heuristics

## H01: ℓ1-penalty with indicator function to softly enforce scale positivity
- **Rationale**: The heat kernel `e^{-sλ_i}` (Eq. 1) requires `s` to behave as a diffusion scale;
  the paper states the ℓ1 regularization term is added "to impose positive scale for the
  heat-kernel" (§2). Rather than a hard constraint (e.g. reparameterizing `s` through a softplus or
  exponential), the paper penalizes only the negative part of `s^m_n` via an indicator function
  `1_{s<0}` inside the training loss (Eq. 7), so gradient descent is pushed toward, but not strictly
  confined to, positive values.
- **Sensitivity**: Not specified in paper (the weight `α` controlling this penalty's strength is
  not numerically given).
- **Bounds**: Not specified in paper (no stated range for `α` or for how negative `s^m_n` is allowed
  to become before/during training).
- **Code ref**: [`src/execution/gtad_forward.py::loss_fn`]
- **Source**: §2, "Transformer-Guided Scale Update", Eq. (7): "With an ℓ1 norm regularization on
  `s^m_n` to impose positive scale for the heat-kernel, the overall objective function `L` is
  defined as ... where `α` is a user-parameter and `1` is an indicator function."

## H02: Assign one self-attention head per imaging modality (not per generic subspace)
- **Rationale**: Standard multi-head transformers (BERT [5], ViT [6]) split a single input
  representation into multiple heads over learned subspaces. GTAD instead assigns "each head ...
  to an individual modality to integrate long-range information from other nodes, which is not
  captured in the convolution block" (§2). This design choice directly ties each attention head's
  output to a specific, human-interpretable modality (e.g. cortical thickness vs. FDG vs.
  β-Amyloid), which the paper leverages later for the per-modality attention-score interpretability
  results in Fig. 3.
- **Sensitivity**: Not specified in paper (no ablation isolates modality-assigned heads vs. a
  generic multi-head split under otherwise identical settings — Table 2's "position-wise
  attention" comparison uses concatenated features into a single encoder, which is a different
  contrast than a like-for-like multi-head-without-modality-assignment baseline).
- **Bounds**: Requires `M` (number of modalities) to be known and fixed at model-construction time,
  since the number of attention heads is tied to `M`.
- **Code ref**: [`src/execution/gtad_forward.py::modality_wise_attention`, `multi_modal_attention`]
- **Source**: §2, "Modality-wise Self-Attention Block": "Unlike typical use of transformer [5,6],
  each head is assigned to an individual modality to integrate long-range information from other
  nodes, which is not captured in the convolution block."

## H03: Reading trained scale magnitude as a local-vs-distant information-need indicator
- **Rationale**: After training, the paper treats the learned `s^m_n` values as directly
  interpretable: "ROIs with small trained scales require information from neighboring ROIs on the
  classification, ROIs with large scales need distant features as they are less effective
  individually" (§4). This heuristic is used purely for post-hoc interpretation (Fig. 2), not as a
  constraint applied during training.
- **Sensitivity**: Not specified in paper (no sensitivity analysis on how robust the smallest/
  largest-scale ROI ranking is to random seed, fold, or initialization).
- **Bounds**: Not specified in paper (no stated threshold separating "small" from "large" scale;
  the paper reports only a relative ranking, e.g. the 8 smallest per modality in Fig. 2).
- **Code ref**: Not specified — this is a post-hoc interpretive reading of trained parameters, not
  an executable procedure captured in `src/execution/`.
- **Source**: §4, "Discussion on the Scales": "Therefore, while ROIs with small trained scales
  require information from neighboring ROIs on the classification, ROIs with large scales need
  distant features as they are less effective individually."

## H04: Total attention score / Importance Rate as an ROI-relevance ranking heuristic
- **Rationale**: To surface which ROIs matter most, the paper defines "total attention score" as
  how many ROIs give their highest attention weight to a given ROI, then reports the top-5 ROIs by
  this count (expressed as Importance Rate, a percentage) per modality (§4, "Pre-clinical AD via
  ROI Attention"). This converts a dense pairwise attention matrix into a simple per-ROI popularity
  ranking usable for clinical interpretation.
- **Sensitivity**: Not specified in paper (no analysis of how stable the top-5 ranking is across
  folds/seeds).
- **Bounds**: Not specified in paper (no stated minimum IR threshold for "importance"; the paper
  reports a fixed top-5 cutoff per modality).
- **Code ref**: Not specified — this is a post-hoc statistic computed over attention weights, not
  part of the forward-pass reconstruction in `src/execution/`.
- **Source**: §4, "Pre-clinical AD via ROI Attention": "the total attention score is defined as the
  result of calculating how many ROIs give the highest attention score to the corresponding ROI ...
  Importance Rate (IR) indicates how many ROIs pay attention" (Fig. 3 caption).
