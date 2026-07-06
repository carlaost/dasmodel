# Related Work (Typed Dependency Graph)

The review's own positioning is against prior AD-AI surveys (Table 1); its methods layer imports
foundational transformer/attention/fusion works and catalogues the 68 reviewed primary studies. Full
`RW` blocks are given for the 8 prior reviews (the direct predecessors this survey extends/bounds)
and the load-bearing foundational method papers; the 68 reviewed studies and the remaining ~300
references form the broader footprint summarized at the end.

## RW01: Sharma et al., 2022 [16]
- **DOI**: not stated in paper
- **Type**: baseline (prior review)
- **Delta**:
  - What changed: This review adds ViT/CViT, fusion strategies, reproducibility, and frameworks that [16] (ML on multimodal neuroimaging, 230 studies, past ~3 decades) omits.
  - Why: [16] predates the transformer wave.
- **Claims affected**: C11
- **Adopted elements**: motivation for advanced/hybrid AI and multimodal early detection.

## RW02: Odusami et al., 2024 [42]
- **DOI**: not stated in paper
- **Type**: baseline (prior review)
- **Delta**:
  - What changed: [42] reviewed 47 ML studies (2016–2022) on multimodal neuroimaging staging; this review is transformer-specific and adds reproducibility/framework analysis.
  - Why: [42] focuses on classical ML feature fusion.
- **Claims affected**: C11
- **Adopted elements**: evidence that MRI+PET fusion improves MCI-vs-AD discrimination.

## RW03: Nazir et al., 2024 [43]
- **DOI**: not stated in paper
- **Type**: baseline (prior review)
- **Delta**:
  - What changed: [43] examined CNN/RNN DL on MRI/PET/fMRI (147 studies); this review shifts to ViT/CViT and multimodal fusion depth.
  - Why: [43] is a pre-transformer DL survey.
- **Claims affected**: C11
- **Adopted elements**: identified needs — interpretability, standardized benchmarks, better fusion.

## RW04: Toumaj et al., 2024 [40]
- **DOI**: not stated in paper
- **Type**: baseline (prior review)
- **Delta**:
  - What changed: [40] surveyed DL for AD classification (50 studies, 2017–2024) including frameworks; this review deepens transformer-specific and reproducibility coverage.
  - Why: broader DL scope, less transformer focus.
- **Claims affected**: C11
- **Adopted elements**: emphasis on XAI and robust multimodal integration.

## RW05: Valizadeh et al., 2024 [44]
- **DOI**: not stated in paper
- **Type**: baseline (prior review)
- **Delta**:
  - What changed: [44] reviewed DL for MCI→AD progression (78 studies, 2013–2023, CNN/RNN/AE/ensembles); this review covers transformers and links progression to the CViT paradigm.
  - Why: [44] is architecture-agnostic and pre-transformer.
- **Claims affected**: C04, C11
- **Adopted elements**: framing of MCI progression prediction and need for standardized metrics.

## RW06: Hcini et al., 2024 [57]
- **DOI**: not stated in paper
- **Type**: baseline / bounds (prior review)
- **Delta**:
  - What changed: [57] compared CNNs vs ViTs for early AD detection (61 studies, 2019–2024); this review broadens to CViTs, fusion, reproducibility, frameworks at larger scale.
  - Why: [57] is narrower (CNN-vs-ViT comparison).
- **Claims affected**: C09, C11
- **Adopted elements**: advantage of ViTs for long-range dependencies; call for fairness/bias audits.

## RW07: Bravo et al., 2024 [58]
- **DOI**: not stated in paper
- **Type**: baseline (prior review, closest predecessor)
- **Delta**:
  - What changed: [58] focused on ViTs/CNNs for AD using 3D MRI with reproducibility/framework assessment (44 studies, 2016–2024); this review extends to CViTs and multimodal fusion at larger scope (68 studies). Fig. 4 MRI illustration is adapted from [58].
  - Why: [58] is the nearest in spirit but lacks CViT/fusion breadth.
- **Claims affected**: C05, C11
- **Adopted elements**: reproducibility-assessment methodology; multimodal-fusion significance.

## RW08: Nagarajan et al., 2025 [45]
- **DOI**: not stated in paper
- **Type**: baseline (prior review)
- **Delta**:
  - What changed: [45] reviewed DL for AD classification (34 studies, 2005–2024) on single/multimodal neuroimaging; this review is transformer-specific and practice-focused.
  - Why: [45] is broad-DL and mostly classification.
- **Claims affected**: C11
- **Adopted elements**: single vs multimodal framing.

## RW09: Vaswani et al. — Transformer / self-attention [27]
- **DOI**: arXiv:1706.03762
- **Type**: imports
- **Delta**:
  - What changed: provides the scaled-dot-product/MHSA foundation (Eqs. 6–9) underpinning all reviewed models.
  - Why: core mechanism of ViT/CViT.
- **Claims affected**: C01, C09
- **Adopted elements**: self-attention, MHSA, encoder architecture.

## RW10: Dosovitskiy et al. — ViT [28]
- **DOI**: arXiv:2010.11929
- **Type**: imports
- **Delta**:
  - What changed: defines the image-as-patches ViT (Eqs. 16–20) that the review's ViT section is built on.
  - Why: the reference architecture for standalone-ViT studies.
- **Claims affected**: C01, C02, C09
- **Adopted elements**: patch/positional embedding, class token, pretraining need.

## RW11: Liu et al. — Swin Transformer [280]
- **DOI**: arXiv:2103.14030
- **Type**: imports
- **Delta**:
  - What changed: hierarchical shifted-window transformer used as a backbone in many serial CViTs (Conv-Swinformer, RST, VGG-TSwinformer).
  - Why: an efficient "vision-only" LVM backbone.
- **Claims affected**: C01
- **Adopted elements**: SW-MHSA, hierarchical feature extraction.

## RW12: Touvron et al. — DeiT [135]
- **DOI**: arXiv:2012.12877
- **Type**: baseline / imports
- **Delta**:
  - What changed: data-efficient ViT training used as a strong transformer baseline (Carcagni et al. [158]) and backbone (RanCom-ViT [202]).
  - Why: addresses ViT data-hunger.
- **Claims affected**: C09
- **Adopted elements**: data-efficient distillation training.

## RW13: Foundational attention/CNN components (SE [130], CBAM [129], Luong [127], Bahdanau [122], Xu [123])
- **DOI**: various (not stated in paper)
- **Type**: imports
- **Delta**:
  - What changed: supply the spatial/channel/soft-hard/global-local/additive-multiplicative attention formalism (Eqs. 1–14) reflected in the CViT attention-integration taxonomy.
  - Why: background for CViT attention integration.
- **Claims affected**: C10
- **Adopted elements**: attention variants and their formal definitions.

## RW14: Foundational fusion-taxonomy sources [47, 174, 175]
- **DOI**: not stated in paper
- **Type**: imports / extends
- **Delta**:
  - What changed: provide the input/intermediate/output fusion-level hierarchy that this review adapts and augments (knowledge-based, hybrid) for ViT/CViT AD models.
  - Why: organizing scaffold for the fusion taxonomy.
- **Claims affected**: C10
- **Adopted elements**: three-level fusion hierarchy.

## RW15: General medical foundation models (BiomedGPT [272], GMAI-VL [273], HuatuoGPT-Vision [274], UMed-LVLM [275], Med-PaLM M [271])
- **DOI**: various (not stated in paper)
- **Type**: bounds (frontier comparators)
- **Delta**:
  - What changed: establish the LVM/LVLM frontier (Table 8) against which AD-specific applications are contrasted, exposing the "largeness" gap.
  - Why: motivate the proposed conceptual LVM and future directions.
- **Claims affected**: C10 (LVM synthesis); informs proposed_lvm.md
- **Adopted elements**: unified pretraining + SFT, MLP-projector/cross-attention fusion, RLCF.

## Reviewed primary studies (the corpus, 68 works)
The review's evidence base is the 68 reviewed studies themselves, tabulated in **Table 4** (22 ViT
studies) and **Table 5** (46 CViT studies), with per-study framework/code/metrics in **Table 6** and
datasets in **Table 7**. Representative AD-specific models used as exemplars throughout include:
ViT-TST [134], ViTAD [195], ViT-GRU [197], RanCom-ViT [202], OViTAD [204], STGTN [205], VTFF [206],
BIGFormer [109], MIMD-3DVT [191], Conv-Swinformer [81], RST [209], ECSNet [31], RepBoTNet-CESA [157],
MC-ViT [210], DE-JANet [102], DAFN [143], 3MT [50], AD-Transformer [49], MCAD [155], CsAGP [156],
MMTFN [147], MDL-Net [193], HAMMF [154], BSFL [177], CT-GAN [194], and the Odusami et al. image-fusion
series [148–151]. These are typed as `baseline`/`extends` relative to the foundational imports above;
their exact metrics are recorded only in `evidence/tables/table4.md` and `table5.md`, never restated
as review claims.

## Broader citation footprint
Beyond the entries above, the paper cites ~312 references spanning: AD epidemiology and biology
[1–17], neuroimaging modalities and preprocessing [70–101], genetics [103–109], reproducibility and
open-science infrastructure (Clinica [243], BIDS [239, 240], medigan [221], licensing [222–224]),
dataset resources [246–258], and privacy/ethics/federated-learning literature [259–312]. These are
captured here as the review's contextual/infrastructure footprint rather than as individual RW blocks
with a technical delta.
