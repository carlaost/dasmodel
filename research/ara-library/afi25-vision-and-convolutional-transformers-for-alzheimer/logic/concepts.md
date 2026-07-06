# Concepts

## Vision Transformer (ViT)
- **Notation**: patches $x_p \in \mathbb{R}^{N\times(P^2\cdot C)}$; embeddings $z_0=[x_{class};\hat x]+E_{pos}$
- **Definition**: An adaptation of the Transformer encoder to images: an image $x\in\mathbb{R}^{H\times W\times C}$ is split into $N=HW/P^2$ non-overlapping patches, each linearly projected to a $D$-dim embedding, a learnable class token is prepended, 1D positional embeddings are added, and $L$ transformer-encoder layers (MHSA + MLP with LayerNorm and residuals) process the sequence; the final class-token state is passed to a classification head. (Eqs. 16–20.)
- **Boundary conditions**: Data-hungry with weak inductive bias; typically needs large-scale pretraining (ImageNet-21k, JFT-300M) or data-efficient variants (DeiT).
- **Related concepts**: Self-attention / MHSA, CViT, Swin Transformer, Patch embedding.

## Convolutional Vision Transformer (CViT)
- **Notation**: serial $Y_{out}=\psi_{vit}(Z_0)$ where $F_{cnn}=\phi_{cnn}(X)$; parallel $F_{fused}=f_{fuse}(F_{cnn},F_{vit})$
- **Definition**: A hybrid architecture that deliberately fuses a CNN component (local spatial feature extraction, strong inductive bias) with a transformer component (global context via self-attention). Designed to mitigate pure-ViT data-hunger while retaining global modeling. (§4.4.2.)
- **Boundary conditions**: Increased architectural complexity; the dominant paradigm in the reviewed AD literature (46/68 studies).
- **Related concepts**: Architectural integration pattern, ViT, CNN, Swin Transformer.

## Self-attention (Scaled dot-product) and Multi-Head Self-Attention (MHSA)
- **Notation**: $\text{Attention}(Q,K,V)=\text{softmax}(QK^{T}/\sqrt{d_k})V$ (Eq. 7); MultiHead = Concat(head$_1$…head$_h$)$W^O$ (Eq. 9)
- **Definition**: A mechanism relating all positions within a sequence to produce a contextualized representation; queries/keys/values are learned linear projections of the input, and the output is a similarity-weighted sum of values scaled by $1/\sqrt{d_k}$. MHSA runs $h$ such attentions in parallel over different subspaces.
- **Boundary conditions**: Quadratic $O(n^2)$ cost in sequence length — a bottleneck for high-resolution 3D neuroimaging.
- **Related concepts**: Cross-attention, spatial/channel attention, ViT.

## Cross-attention
- **Notation**: $\text{Attention}(Q_A,K_B,V_B)=\text{softmax}(Q_AK_B^{T}/\sqrt{d_k})V_B$ (Eq. 23)
- **Definition**: A structural adaptation of self-attention where queries come from one sequence/modality and keys/values from another, enabling direct cross-modal information exchange; foundational to multimodal fusion (e.g. MCAD, 3MT, CsAGP).
- **Boundary conditions**: Requires two distinct feature sets; central to attention-based intermediate fusion.
- **Related concepts**: Multimodal fusion, MHSA, MCAD.

## Spatial vs channel attention (CBAM/SE)
- **Notation**: spatial $F'=M_s(F)\otimes F$ (Eq. 12); channel $M_c(F)=\sigma(W_2\,\text{ReLU}(W_1(\text{GAP}(F))))$ (Eq. 14)
- **Definition**: CNN-oriented attention: spatial attention learns a 2D map ($M_s\in\mathbb{R}^{1\times H\times W}$) emphasizing *where* to attend; channel attention learns a 1D vector ($M_c\in\mathbb{R}^{C\times1\times1}$) emphasizing *what* channels matter (canonical Squeeze-and-Excitation block). CBAM applies them sequentially.
- **Boundary conditions**: Operate on intermediate CNN feature maps $F\in\mathbb{R}^{C\times H\times W}$.
- **Related concepts**: CViT attention-mechanism integration, CBAM, SE block.

## Architectural integration pattern (serial / parallel / hierarchical)
- **Notation**: —
- **Definition**: The review's taxonomy of how CNN and transformer components are arranged in a CViT: **Serial** (CNN front-end → transformer; most common), **Parallel** (concurrent CNN and transformer branches then fused), **Hierarchical** (convolution and self-attention deeply interleaved within blocks at multiple scales). Attention-mechanism integration (spatial/channel/cross-attention/MHSA replacement) is a related axis. (§4.4.2, Fig. 12/13.)
- **Boundary conditions**: Applies to hybrid CViT models; serial is the most prevalent pattern.
- **Related concepts**: CViT, multimodal fusion, Feature fusion strategy.

## Multimodal data fusion levels (input / intermediate / output)
- **Notation**: intermediate concat $f_{fused}=[f_1;\dots;f_N]$ (Eq. 27); late average $p_{fused}=\frac1N\sum p_i$ (Eq. 30)
- **Definition**: Taxonomy of the stage at which modalities are combined: **Input-level (early/signal)** — merge raw/co-registered data (e.g. channel concat, DWT, GLP+SPCNN); **Intermediate (feature-level)** — combine modality-specific features (concat, hierarchical, attention-based; the most prevalent/versatile); **Output-level (late/decision)** — combine per-modality model outputs (averaging, weighted, voting, stacking). **Knowledge-based** fusion (domain priors at any level) and **Hybrid** fusion (combining multiple levels or generative+discriminative/graph methods) are cross-cutting. (§6.1.)
- **Boundary conditions**: Choice is context-dependent; intermediate fusion dominates but faces curse-of-dimensionality.
- **Related concepts**: Cross-attention, temporal/spatial fusion, CViT.

## MCI-to-AD conversion prediction (pMCI vs sMCI)
- **Notation**: —
- **Definition**: The prognostic task of predicting whether a Mild-Cognitive-Impairment patient will progress to AD dementia (progressive MCI, pMCI) or remain stable (stable MCI, sMCI), distinct from cross-sectional AD-stage classification. ~10–15% of MCI individuals progress to AD annually.
- **Boundary conditions**: Clinically vital but underexplored; harder than classification.
- **Related concepts**: AD stage continuum (CN/EMCI/MCI/LMCI/AD), external validation.

## AD clinical continuum (CN → EMCI → MCI → LMCI → AD)
- **Notation**: —
- **Definition**: The NIA-AA research-framework staging of disease progression: Cognitively Normal (CN), Early MCI (EMCI), MCI, Late MCI (LMCI), and AD dementia — with evolving cognitive impairment and biological change (Aβ plaques, tau tangles, atrophy). Some studies use a 4-stage severity labeling (ND, VMD, MD, MoD).
- **Boundary conditions**: Staging labels vary across datasets (ADNI stages vs Kaggle ND/VMD/MD/MoD).
- **Related concepts**: sMRI atrophy, PET biomarkers, MCI conversion.

## Swin Transformer
- **Notation**: SW-MHSA (shifted-window MHSA)
- **Definition**: A hierarchical vision transformer using shifted-window self-attention for efficient multi-scale feature extraction; frequently used as the transformer backbone within serial CViT frameworks (e.g. Conv-Swinformer, RST, VGG-TSwinformer).
- **Boundary conditions**: Serves as a "vision-only" LVM backbone, not inherently multimodal.
- **Related concepts**: CViT, ViT, hierarchical integration.

## PRISMA 2020 systematic-review methodology
- **Notation**: —
- **Definition**: The Preferred Reporting Items for Systematic Reviews and Meta-Analyses (2020) evidence-based reporting framework: define search, search databases, remove duplicates, screen titles/abstracts, full-text eligibility assessment, and inclusion — with a flow diagram (Fig. 2). No PROSPERO registration ID is reported for this review.
- **Boundary conditions**: This review reports adherence to PRISMA 2020 [60]; two independent reviewers with consensus.
- **Related concepts**: Inclusion/exclusion criteria, data extraction, selection bias.

## External validation vs internal validation
- **Notation**: —
- **Definition**: Internal validation evaluates a model on held-out data from the same cohort (k-fold CV or a train/test split); external validation trains on one dataset and tests on a completely separate, unseen cohort. The review treats rigorous external validation as the methodological gold standard for assessing generalizability.
- **Boundary conditions**: Rare in the reviewed literature; distinguishes bias "Category 3" from "Category 1/2".
- **Related concepts**: Dataset bias, accuracy paradox, data leakage.

## Accuracy paradox / illusion of clinical readiness
- **Notation**: —
- **Definition**: The phenomenon whereby exceptionally high accuracy (often >99%) on curated, balanced, internally-validated test sets does not translate to real-world clinical utility — especially for the harder MCI-conversion task. The review argues evaluation must move toward AUC on imbalanced classes, external-cohort performance, and calibration.
- **Boundary conditions**: Especially acute for single-dataset, internally-validated studies (bias Category 1/2).
- **Related concepts**: External validation, dataset bias, data leakage, uncertainty quantification.

## Large Vision Model (LVM) / medical foundation model
- **Notation**: —
- **Definition**: Large-scale (vision or vision-language) models pretrained on massive/curated data with zero-/few-shot capability (e.g. BiomedGPT, GMAI-VL). The review distinguishes true generalist LVLMs from AD-domain usage, where "LVM" typically means a pretrained ViT/Swin backbone used as a fine-tuned feature extractor via transfer learning or domain-specific SSL (e.g. DINO), not an end-to-end medical foundation model.
- **Boundary conditions**: Zero-shot generative LVMs are "largely unexplored" in the reviewed AD literature.
- **Related concepts**: Transfer learning, self-supervised learning, multimodal fusion, DAPT.

## Data leakage
- **Notation**: —
- **Definition**: A methodological flaw where information from the test set (e.g. slices from the same subject, or preprocessing fit on all data) contaminates training, yielding biased, overly optimistic performance. The review screened for it during full-text assessment and flags subject-level splitting as a safeguard.
- **Boundary conditions**: Especially relevant when 3D volumes are sliced into 2D samples or cohorts are merged before splitting.
- **Related concepts**: External validation, subject-level splitting, accuracy paradox.
