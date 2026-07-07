# Related Work

This paper's 27-item reference list spans three roles: (1) the nine compared baseline methods used
in Table 1/Table 2, (2) mechanisms imported into GTAD's own architecture (heat-kernel spectral
theory, transformer self-attention, residual connections, layer norm), and (3) background
citations motivating the brain-network-graph problem framing or supporting the post-hoc ROI
interpretation in §4. Full `RW` blocks are given for works with a specific technical delta relative
to GTAD (baselines + core imported mechanisms); the remaining background citations are listed
briefly at the end.

## RW01: Sim, Jeon, Choi, Wu, Kim — LSAP (AAAI 2024) [18]
- **DOI**: Not specified in paper (AAAI Proceedings vol. 38, pp. 4882–4890, 2024)
- **Type**: extends / baseline
- **Delta**:
  - What changed: LSAP ("Learning to approximate adaptive kernel convolution on graphs") is the
    authors' own prior work introducing a learned/approximated adaptive-kernel graph convolution.
    GTAD extends this line by (a) making the scale explicitly node-wise *and* modality-wise
    (`s^m ∈ R^N` per modality), and (b) adding a downstream modality-wise transformer/self-attention
    block that LSAP does not have, to additionally capture long-range/global structure.
  - Why: LSAP alone (as a diffusion-based method) still underperforms graph-transformer baselines in
    Table 1 (e.g. 0.911–0.934 accuracy vs. DIFFormer/SGFormer's 0.930–0.959), motivating the addition
    of global attention on top of adaptive local diffusion.
- **Claims affected**: C01, C02
- **Adopted elements**: The core idea of a *learned, adaptive* kernel scale (vs. a fixed heat-kernel
  scale as in GraphHeat/GDC/ADC) is carried over and extended into GTAD's Modality-wise Adaptive
  Convolution Block.

## RW02: Kipf & Welling — GCN (ICLR 2017) [12]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: GCN uses fixed (non-diffusion, non-adaptive) first-order spectral graph
    convolution; GTAD replaces this with an adaptively-scaled heat-kernel diffusion plus attention.
  - Why: GCN's homophily-based local aggregation "ineffectively aggregate[s] information from
    distant neighborhoods" (§1).
- **Claims affected**: C01
- **Adopted elements**: General graph-convolution formalism (spectral convolution via graph
  Laplacian) as a conceptual predecessor.

## RW03: Veličković et al. — GAT (ICLR 2018) [22]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: GAT uses local attention over immediate neighbors (not a global transformer, not
    an adaptive diffusion scale); GTAD's self-attention operates over all ROIs (long-range) per
    modality.
  - Why: Attention-based methods including GAT-style local attention are described as exhibiting
    "deficiencies in capturing node-centric information" (§1).
- **Claims affected**: C01
- **Adopted elements**: none beyond the general attention concept.

## RW04: Xu, Shen, Cao, Cen, Cheng — GraphHeat (IJCAI 2019) [26]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: GraphHeat uses a heat-kernel graph convolution with a fixed (non-trainable,
    non-node-wise) scale; GTAD makes the scale trainable, node-wise, and modality-wise, and adds the
    transformer block.
  - Why: A single global scale cannot capture per-ROI, per-modality local/global variation.
- **Claims affected**: C01
- **Adopted elements**: The heat-kernel formulation (Eq. 1) underlying GTAD's adaptive convolution
  is the same spectral-graph-theory construct GraphHeat uses.

## RW05: Gasteiger, Weißenberger, Günnemann — GDC (NeurIPS 2019) [7]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: GDC (Graph Diffusion Convolution) generalizes diffusion-based graph convolution
    (e.g. via personalized PageRank or heat kernel) but with a globally fixed diffusion, not a
    trainable node/modality-wise scale or a downstream attention mechanism.
  - Why: Table 1 shows GDC is often the *weakest* diffusion-based baseline (e.g. 0.842 accuracy on
    Cortical Thickness & FDG), motivating GTAD's adaptive, learned alternative.
- **Claims affected**: C01
- **Adopted elements**: none beyond the general diffusion-convolution concept.

## RW06: Zhao, Dong, Ding, Kharlamov, Tang — ADC (NeurIPS 2021) [27]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: ADC (Adaptive Diffusion in GNNs) introduces adaptivity to the diffusion process,
    but the paper's results indicate this alone (without a downstream transformer) still trails
    graph-transformer baselines.
  - Why: Motivates that adaptivity in the diffusion/convolution stage is necessary but not
    sufficient — a downstream transformer for global mixing is still needed (per Table 1 and Table 2
    ablation logic).
- **Claims affected**: C01, C02
- **Adopted elements**: The general notion of adapting diffusion parameters during training.

## RW07: Wu, Zhao, Li, Wipf, Yan — NodeFormer (NeurIPS 2022) [24]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: NodeFormer is a scalable graph-structure-learning transformer for node
    classification; it provides global attention but, per the paper's framing, "often disregard[s]
    sufficient expressive power of the central nodes, lacking interpretation of the result" (§1) —
    i.e., no explicit node-centric local mechanism analogous to GTAD's per-node scale.
  - Why: Motivates pairing global attention with an explicit local (per-node) mechanism.
- **Claims affected**: C01
- **Adopted elements**: none beyond the general graph-transformer paradigm.

## RW08: Wu, Yang, Zhao, He, Wipf, Yan — DIFFormer (ICLR 2023) [23]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: DIFFormer is a scalable graph transformer induced by energy-constrained diffusion
    — conceptually closest in spirit to GTAD (diffusion + transformer), but without GTAD's explicit
    trainable per-node, per-modality scale or modality-assigned attention heads.
  - Why: DIFFormer is the second-strongest baseline in Table 1 (e.g. 0.930–0.954 accuracy), the
    closest competitor GTAD must beat to support C01.
- **Claims affected**: C01
- **Adopted elements**: The general idea of coupling diffusion processes with transformer-style
  global mixing.

## RW09: Wu, Zhao, Yang, Zhang, Nie, Jiang, Bian, Yan — SGFormer (NeurIPS 2024) [25]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: SGFormer simplifies/empowers transformers for large-graph representations; it is
    the strongest baseline in Table 1 (e.g. 0.941–0.959 accuracy) but still lacks an explicit
    node-wise adaptive local mechanism and multi-modal-specific attention heads.
  - Why: The closest overall competitor to GTAD; GTAD's margin over SGFormer (e.g. 0.945 vs 0.941 on
    CT & β-Amyloid; 0.963 vs 0.951 on All Imaging Features) is the tightest in Table 1.
- **Claims affected**: C01
- **Adopted elements**: none beyond the general simplified-transformer-for-graphs paradigm.

## RW10: Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin — Transformer (NeurIPS 2017) [21]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: GTAD's Modality-wise Self-Attention Block directly reuses the scaled dot-product
    multi-head self-attention formulation (`QK^T/√C`, softmax, feed-forward, residual + layer norm)
    from this paper, but reassigns "each head ... to an individual modality" rather than a generic
    representation split (§2) — the paper explicitly notes this is "unlike typical use of the
    transformer [5,6]".
  - Why: Off-the-shelf transformer self-attention is the mechanism for capturing long-range/global
    graph structure that convolution/diffusion alone cannot.
- **Claims affected**: C01, C03
- **Adopted elements**: Scaled dot-product attention, multi-head structure, feed-forward network,
  residual connections + layer norm (Eq. 4–5 directly instantiate this architecture).

## Brief entries (background / foundational / interpretive citations without a GTAD-specific technical delta)

- **Ba, Kiros, Hinton — Layer Normalization (NeurIPS 2016) [1]** — imports: `f_L[·]` in Eq. 5 is
  standard layer normalization.
- **He, Zhang, Ren, Sun — Deep Residual Learning / ResNet (CVPR 2016) [8]** — imports: the residual
  connections in Eq. 5 (`B_{p-1} + Φ(B_{p-1})`) follow this design.
- **Chung — Spectral Graph Theory (1997) [2]** — imports: theoretical basis for the heat kernel
  (Eq. 1) and Laplacian eigendecomposition used throughout §2.
- **Oppenheim, Willsky, Nawab, Ding — Signals and Systems (1997) [14]** — imports: cited for the
  convolution theorem underlying the graph Fourier transform (Eq. 2).
- **Destrieux, Fischl, Dale, Halgren — Automatic Parcellation (NeuroImage 2010) [3]** — imports: the
  160-ROI (148 cortical + 12 sub-cortical) atlas used to define graph nodes (§3, Dataset).
- **Thie — Understanding SUVR (J. Nuclear Medicine 2004) [20]** — imports: definition of the
  Standard Uptake Value Ratio used for the FDG-PET modality feature (§3, Dataset).
- **Devlin, Chang, Lee, Toutanova — BERT (2019) [5]** and **Dosovitskiy et al. — ViT (ICLR 2021)
  [6]** — bounds: cited as the "typical use of transformer" that GTAD's per-modality-head attention
  deliberately departs from (§2, Modality-wise Self-Attention Block).
- **DeTure, Dickson — Neuropathological diagnosis of AD (2019) [4]**, **Stam et al. — MEG
  functional connectivity in AD (2009) [19]**, **Ryyppö et al. — ROIs as nodes of dynamic functional
  brain networks (2018) [17]**, **Kim, Adluru, Chung, Okonkwo, Johnson, Bendlin, Singh — Multi-
  resolution statistical analysis of brain connectivity in preclinical AD (2015) [11]** — background:
  cited in the Introduction to motivate using brain connectomes/graphs for early AD detection (§1).
- **Park, Hwang, Kim, Chung, Wu, Kim — Convolving directed graph edges via Hodge Laplacian
  (MICCAI 2023) [15]** — background: cited alongside [11] as prior brain-network-graph analysis work
  from an overlapping set of authors; no specific technical delta versus GTAD is stated in this
  paper.
- **de Jong et al. — Putamen/thalamus volume reduction in AD (Brain 2008) [9]**, **Rao et al. —
  Hippocampus in AD review (2022) [16]**, **Khazaee, Ebrahimzadeh, Babajani-Feremi — AD via
  resting-state fMRI and graph theory (2015) [10]**, **Liu et al. — dACC–lingual gyrus connectivity
  in AD with depression (2017) [13]** — background: cited in §4 to support the neuroscientific
  plausibility of the ROIs (putamen, hippocampus, lingual gyrus) that GTAD's trained scales/attention
  scores identify as important (supports the *Interpretation* fields of C04/C05, not independently
  verified by this ARA).
