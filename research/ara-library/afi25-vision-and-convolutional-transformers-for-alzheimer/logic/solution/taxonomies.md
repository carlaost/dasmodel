# The Four Novel Taxonomies

The review's central conceptual contribution (C10) is a set of four taxonomies used to organize the
68 studies. Structure mirrors Figs. 12, 13, 14, 15.

## 1. Model-architecture taxonomy: ViT vs CViT (Fig. 15)
- **Standalone ViT** (22 studies): pure transformer applied to image patches; strong global modeling, weak inductive bias, data-hungry.
- **Hybrid CViT** (46 studies): CNN + transformer, sub-classified by *architectural integration pattern* (below).

### CViT architectural-integration patterns (Fig. 12/13, §4.4.2)
- **Serial integration** (most prevalent): CNN front-end → tokenize → transformer encoder.
  $F_{cnn}=\phi_{cnn}(X)$ reshaped to tokens $Z_0$, then $Y_{out}=\psi_{vit}(Z_0)$ (Eq. 22). Examples: Conv-Swinformer [81], RST [209], DE-JANet [102], CrossViT [153].
- **Parallel integration**: concurrent CNN and ViT branches, then fused.
  $F_{fused}=f_{fuse}(F_{cnn},F_{vit})$ (Eq. 21). Examples: LCGNet [140], Sait [141], Sait & Nagaraj [187], Menon & Gunasundari [211].
- **Hierarchical integration**: convolution and self-attention interleaved within blocks at multiple scales. Examples: Khatri & Kwon optimized CViT [30], Khatri et al. [145], BraInf [160], MDL-Net [193], MMTFN [147].

### CViT attention-mechanism integration (Fig. 13f–i)
- Spatial attention (DAFN [143]); channel attention (CrossViT [153]); combined channel+spatial (HAMMF/CHAM [154]); cross-attention (MCAD [155], 3MT [50], CsAGP [156]); MHSA replacing convolutions in deep stages (RepBoTNet-CESA [157]).

## 2. Fusion-strategy taxonomy (Fig. 14, §6.1)
- **Input-level (early / signal-level)**: merge raw/co-registered data before feature extraction.
  Channel concat $I_{fused}=\text{Concat}(I_{MRI},I_{PET})$ (Eq. 24), voxel-wise weighted average (Eq. 25), DWT, GLP+SPCNN. Examples: Odusami et al. series [148–151].
  - *Spatial fusion*: a subtype using registration + pyramid decomposition to combine at pixel/voxel level.
- **Intermediate (feature-level)** — the most prevalent/versatile:
  - Single-level (classic/network) fusion: concat high-level features $f_{fused}=[f_1;\dots;f_N]$ (Eq. 27) — e.g. DE-JANet [102].
  - Hierarchical fusion: multi-stage feature combination — MMTFN [147], Dual-3DM3-AD [182].
  - Attention-based fusion: self-/cross-attention over feature tokens (Eqs. 28–29) — MCAD [155], CsAGP [156], AD-Transformer [49].
  - Temporal fusion: fuse features across time points — VGG-TSwinformer [131].
- **Output-level (late / decision-level)**: combine per-model outputs — averaging (Eq. 30), weighted (Eq. 31), majority voting, stacking (Eq. 32). Example: Kadri et al. [188].
- **Knowledge-based fusion** (cross-cutting principle, any level): inject domain priors — clinical/demographic (age, MMSE, ADAS-Cog), biochemical/genetic (CSF, APOE), anatomical (ROI atlases, brain-region/gene knowledge graphs), or multi-task constraints. Can modulate imaging features via learned scale/shift $f'_{img}=\gamma(f_{know})\odot f_{img}+\beta(f_{know})$ (Eq. 33).
- **Hybrid fusion**: explicitly combines >1 level or fundamentally different methodologies:
  - Generative (generator G + classifier C; Eqs. 34–35) — Gao et al. [172], Zuo et al. [177, 194], Liu et al. [192].
  - Graph-based (Graph Transformer over feature graph $V_{fused}=f_{GNN}(V,E)$; Eq. 36) — Zou et al. [109].
  - Multi-level system (weighted primary + auxiliary losses; Eq. 37) — 3MT [50], Kadri et al. [188].
  - Systemic (main pipeline + iterative knowledge-guided loop; Eq. 38) — MDL-Net [193], HAMMF [154].

## 3. Data-modality taxonomy (Figs. 16, 17, 25)
- **Single-modality** vs **multimodal** configuration.
- Single-modality overall: sMRI 31, fMRI 7, PET 3 (Fig. 16b); within ViT (Fig. 17): sMRI 15, PET 2, fMRI 4; within CViT (Fig. 25): sMRI 16, PET 1, fMRI 3.
- Multimodal combinations (Fig. 16a): sMRI+Clinical 7, sMRI+PET 12, sMRI+PET+Clinical 1, sMRI+PET+CT 1, sMRI+PET+CSF 1, sMRI+PET+DTI+fMRI 1, sMRI+SNP+Clinical 2, fMRI+DTI 2, fMRI+SNP 1.

## 4. Diagnostic-objective taxonomy (Fig. 15 leaves)
- **AD classification** (binary AD-vs-CN, multi-class staging, or ND/VMD/MD/MoD severity) — the dominant objective.
- **MCI-to-AD progression prediction** (pMCI vs sMCI) — underexplored.
- **Both** (unified frameworks addressing classification + progression) — ~13% of CViT studies (one single-modality sMRI study [32] and six multimodal [49, 50, 62, 172, 184]).
