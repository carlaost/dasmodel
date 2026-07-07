# Concepts

## Brain Network / Connectome Graph
- **Notation**: `G = {V, E}`, `N` nodes
- **Definition**: An undirected graph representing a subject's brain, where node set `V`
  corresponds to anatomical ROIs and edge set `E` encodes structural connectivity (e.g. number of
  white-matter tracts between ROIs from tractography). A symmetric adjacency matrix `A` and diagonal
  degree matrix `D` are computed from `E`.
- **Boundary conditions**: In this paper, `G` is fixed per subject from DTI tractography and shared
  across all imaging modalities; only nodal features vary by modality (§3).
- **Related concepts**: Graph Laplacian, Normalized Laplacian, ROI

## Graph Laplacian / Normalized Laplacian
- **Notation**: `L = D − A`; `L̂ = D^(-1/2) L D^(-1/2)`
- **Definition**: `L` is the (unnormalized) graph Laplacian, real and positive semi-definite, with
  a complete set of orthonormal eigenvectors `U = [u1|u2|...|uN]` and non-negative eigenvalues
  `0 = λ1 ≤ λ2 ≤ ... ≤ λN`. `L̂` is the symmetric-normalized version, sharing the same eigenstructure
  property (§2, Prelim).
- **Boundary conditions**: Requires `G` undirected so `A` is symmetric.
- **Related concepts**: Brain Network Graph, Heat Kernel, Graph Fourier Transform

## Heat Kernel
- **Notation**: `h_s(p, q) = Σ_{i=1}^{N} e^{-sλ_i} u_i(p) u_i(q)` (Eq. 1)
- **Definition**: A kernel from spectral graph theory that captures a smooth transition between
  nodes `p` and `q`, band-limited by scale `s`. The term `e^{-sλ_i}` acts as a low-pass filter over
  the graph spectrum.
- **Boundary conditions**: Defined via the Laplacian eigenbasis `U`; the scale `s` controls the
  effective bandwidth (larger `s` → smoother/more long-range diffusion; the paper's usage inverts
  this into a *node-wise adaptive* scale, see Adaptive Convolution).
- **Related concepts**: Graph Convolution, Adaptive Convolution Block, Graph Fourier Transform

## Graph Fourier Transform / Graph Convolution
- **Notation**: `x̂ = U^T x`; `h_s * x(p) = Σ_{i=1}^{N} e^{-sλ_i} x̂(i) u_i(p)` (Eq. 2)
- **Definition**: Using the convolution theorem, the graph Fourier transform of signal `x` is
  `x̂ = U^T x`; convolving `x` with the heat kernel `h_s` in the spectral domain and transforming
  back yields the graph-convolution operator whose bandwidth is controlled by scale `s`.
- **Boundary conditions**: Assumes access to the full eigendecomposition of `L̂` (or an
  approximation thereof); the paper does not discuss any spectral approximation/truncation scheme.
- **Related concepts**: Heat Kernel, Adaptive Convolution Block

## Modality-wise Adaptive Convolution Block
- **Notation**: `H^m_z = σ_z(e^{-s^m L̂} H^m_{z-1} W^m_z)` (Eq. 3), for modality `m ∈ {1,...,M}`,
  layer `z ∈ {1,...,Z}`
- **Definition**: The encoder stage of GTAD. For each modality `m`, a stack of `Z` graph-convolution
  layers applies the heat-kernel diffusion `e^{-s^m L̂}` — using a *trainable, node-wise,
  modality-specific* scale vector `s^m ∈ R^N` — to the previous layer's hidden state `H^m_{z-1}`
  (with `H^m_0 = x^m`, the raw modality feature), followed by a learned weight `W^m_z` and
  nonlinearity `σ_z`. This produces the locally-effective (short-range) representation `H^m_Z` per
  modality.
- **Boundary conditions**: `s^m` is constrained positive via an ℓ1-regularization term with an
  indicator function in the training objective (Eq. 7); one independent scale vector is learned per
  modality, i.e., the same ROI can have a different scale for different modalities.
- **Related concepts**: Heat Kernel, Trainable Scale, Transformer-Guided Scale Update

## Trainable (Node-wise, Modality-wise) Scale
- **Notation**: `s^m ∈ R^N` for modality `m`; `s^m_n` = scale at node (ROI) `n` for modality `m`
- **Definition**: A per-node, per-modality scalar parameter controlling the heat-kernel diffusion
  bandwidth at that node. It is initialized and then updated end-to-end via gradient descent on the
  classification loss: `s ← s − β ∂L/∂s` (§2, Transformer-Guided Scale Update).
- **Boundary conditions**: Interpreted post hoc by the paper as inversely related to how "local"
  a node's information need is: small `s^m_n` ⇒ relies on immediate neighbors; large `s^m_n` ⇒
  needs distant/global information (§4, Discussion on the Scales). Initial value / learning-rate
  schedule for `s` are not specified in the paper.
- **Related concepts**: Modality-wise Adaptive Convolution Block, Transformer-Guided Scale Update

## Modality-wise Self-Attention Block
- **Notation**: `ϕ(Q^m, K^m, V^m) = σ(Q^m K^{mT} / √C) V^m` (Eq. 4); multi-attention
  `Φ(Q,K,V) = [h1|h2|...|hm] W^Φ`, `h^m = ϕ(Q^m W^{Qm}, K^m W^{Km}, V^m W^{Vm})`
- **Definition**: A transformer-style self-attention module (adapted from Vaswani et al. [21]) in
  which **each attention head is assigned to one imaging modality** rather than being a generic
  multi-head split of one feature space. Query/Key/Value `Q^m, K^m, V^m ∈ R^{N×C}` are derived from
  the modality-wise embeddings `{H^m_Z}` output by the adaptive convolution block. This lets the
  model jointly attend to information "from different modalities across various ROIs in long-range"
  (§2).
- **Boundary conditions**: `C` is "the dimension for hidden units" — its exact value is not given
  in the paper. Attention here provides the global (long-range) complement to the block above.
- **Related concepts**: Modality-wise Adaptive Convolution Block, Transformer Block, Attention
  Score / Importance Rate

## Transformer (Attention) Block with Residuals and Layer Norm
- **Notation**: `B_p = f_L[f_L[B_{p-1} + Φ(B_{p-1})] + Ψ(f_L[B_{p-1} + Φ(B_{p-1})])]` (Eq. 5),
  stacked over `P` layers, with `{H^m_Z}` used as `Q, K, V` for `B_0`
- **Definition**: The full attention-block layer combining the modality-wise multi-head
  self-attention `Φ(·)`, a feed-forward network `Ψ(·)`, residual connections [8], and layer
  normalization `f_L[·]` [1], producing output `B_P` after `P` stacked layers — the paper's
  "comprehensive context across all nodes."
- **Boundary conditions**: `P` (number of stacked attention layers) is not specified numerically in
  the paper.
- **Related concepts**: Modality-wise Self-Attention Block, Classifier

## Transformer-Guided Scale Update / Overall Objective
- **Notation**: `Ŷ_tj = f_R(B_P)_tj / Σ_{j'∈J} f_R(B_P)_tj'` (Eq. 6, softmax classifier);
  `L = −(1/T) Σ_t Σ_j Y_tj ln Ŷ_tj + α (1/M) Σ_m Σ_n 1_{s<0} |s^m_n|` (Eq. 7);
  update rule `s ← s − β ∂L/∂s`
- **Definition**: The end-to-end training objective: cross-entropy between true graph label `Y_tj`
  and predicted `Ŷ_tj` (from classifier `f_R` applied to transformer output `B_P`), plus an ℓ1
  penalty on negative scale values (via indicator `1_{s<0}`) that pushes `s^m_n` to stay positive
  (required for the heat-kernel to be well-defined). Gradient descent with learning rate `β` updates
  the modality-specific scales jointly with all other network weights.
- **Boundary conditions**: `α` ("user-parameter") and `β` (learning rate) values are not specified
  numerically in the paper.
- **Related concepts**: Trainable Scale, Modality-wise Adaptive Convolution Block

## Attention Score / Total Attention Score / Importance Rate (IR)
- **Notation**: IR (%) reported per ROI in Fig. 3
- **Definition**: For a given modality, the *total attention score* at an ROI is defined as "the
  result of calculating how many ROIs give the highest attention score to the corresponding ROI"
  (§4). The *Importance Rate* is this quantity expressed as "how many ROIs pay attention," i.e., the
  fraction/percentage of all ROIs whose highest attention score points to the given ROI.
- **Boundary conditions**: Defined only for the trained model's attention weights on the "All
  Imaging Features" or per-modality set (paper does not disambiguate which trained model instance
  produced Fig. 3's scores). Reported per modality (Cortical Thickness, β-Amyloid, FDG).
- **Related concepts**: Modality-wise Self-Attention Block, ROI

## Standard Uptake Value Ratio (SUVR)
- **Notation**: SUVR
- **Definition**: A standardized measure of regional metabolic/tracer intensity from PET imaging,
  used here for FDG-PET (metabolic intensity) [20]. β-Amyloid protein burden is likewise measured
  from Amyloid-PET.
- **Boundary conditions**: Definition and computation are cited to [20] (Thie, 2004) rather than
  derived in this paper; exact SUVR reference-region normalization is not specified in this paper.
- **Related concepts**: Modality (imaging biomarker), ROI

## Destrieux Atlas Parcellation
- **Notation**: 148 cortical + 12 sub-cortical = 160 ROIs
- **Definition**: An anatomical cortical/sub-cortical parcellation scheme [3] used to partition each
  subject's brain into 160 discrete ROIs, which become the graph nodes for all subjects (§3,
  Dataset).
- **Boundary conditions**: Applied identically across all subjects/modalities in this paper's
  experiments.
- **Related concepts**: Brain Network Graph, ROI
