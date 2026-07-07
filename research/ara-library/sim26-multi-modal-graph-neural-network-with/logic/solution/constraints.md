# Constraints

## Assumptions

- **A1 — Shared graph topology across modalities**: The brain graph (nodes/edges from DTI
  tractography over the Destrieux atlas) is assumed identical across all imaging modalities for a
  given subject; only the nodal *feature* vector `x^m` changes by modality (§3, Dataset).
- **A2 — Well-defined spectral graph**: The normalized Laplacian `L̂` must be real, symmetric, and
  positive semi-definite with a complete orthonormal eigenbasis for the heat-kernel/Fourier
  formulation (Eq. 1–2) to hold (§2, Prelim).
- **A3 — Positive scales**: Node-wise scales `s^m_n` are assumed/required positive; this is
  enforced only *softly* via an ℓ1 penalty with an indicator function in the loss (Eq. 7), not by a
  hard constraint (e.g., no explicit reparameterization such as softplus/exp is stated).
- **A4 — One attention head per modality is sufficient**: The self-attention design assumes a
  single head per modality adequately represents that modality's long-range information, with
  cross-modality mixing deferred to the linear combination `W^Φ` and the feed-forward network
  (§2).
- **A5 — Fixed number of modalities `M` and ROIs `N` per experiment**: `M` and `N` are treated as
  fixed hyperparameters of a given experimental configuration (e.g., `M=2` for paired-modality
  experiments, `M=3` for "All Imaging Features"; `N=160` ROIs throughout).

## Known Limitations (as stated or directly evidenced in the paper)

- **L1 — No released code, weights, or supplementary appendix in this input**: The paper states
  "More details are given in the supplementary" for the experimental setup (§3, Setup), but no
  supplementary material was provided with this ARA's input. Consequently, several implementation
  details (see below) cannot be grounded.
- **L2 — Unspecified hyperparameters**: `Z` (number of adaptive-convolution layers), `P` (number of
  attention layers), `C` (hidden dimension), `α` (ℓ1 penalty weight in Eq. 7), `β` (scale learning
  rate), optimizer choice, batch size, number of training epochs, and the classifier `f_R`'s exact
  architecture are not given anywhere in the 10-page paper.
- **L3 — Ambiguous provenance of Fig. 2/Fig. 3 model instance**: The paper does not state whether
  the interpretability figures (learned scales in Fig. 2, attention scores in Fig. 3) come from the
  "All Imaging Features" model or from separate single/paired-modality models; the column headers
  (Cortical Thickness / β-Amyloid / FDG) suggest per-modality scale/attention values are extracted
  from a model trained with all three modalities present, but this is not stated explicitly.
- **L4 — Ablation modality combination unstated**: §4's ablation study (Table 2) does not restate
  which of the four E01 modality combinations was used to produce the six rows; the reader must
  infer it is representative of the general trend rather than tied to a specific combination.
- **L5 — No statistical significance testing**: Table 1 and Table 2 report only mean ± standard
  deviation over 5 folds; no paired statistical test (e.g., t-test) or confidence interval is
  reported to support "outperformed" language beyond the raw metric comparison.
- **L6 — Single dataset / single population**: All experiments use ADNI only; no external
  validation cohort or out-of-distribution transfer test is reported (contrast with, e.g.,
  multi-cohort AD papers that test OASIS-3/AIBL transfer).
- **L7 — Interpretation is descriptive, not causally validated**: The paper's reading of scale
  magnitude ("small scale ⇒ local reliance, large scale ⇒ distant reliance," §4) and of attention
  Importance Rate as clinical relevance is asserted via correlation with the cited neuroscience
  literature ([9,10,13,16]), not via an independent causal or interventional experiment (e.g., no
  lesion/ROI-ablation validation of the identified ROIs' causal role in the model's predictions).

## Boundary Conditions

- The heat-kernel/spectral formulation (Eq. 1–2) requires the graph Laplacian's eigendecomposition
  to exist and be computed (or approximated) — the paper does not discuss scalability to very
  large `N` (this dataset uses `N=160` ROIs, a modest graph size where full eigendecomposition is
  tractable).
- The described method is specific to *graph-level* classification (predicting a single label
  `Y_t` per subject-graph `G_t`), not node-level or edge-level prediction tasks.
