# Concepts

## Intra-modal InfoNCE (instance discrimination)
- **Notation**: $\mathcal{L}_{intra} = -\sum_{i\in B}\log\frac{\exp(\text{sim}(z_i,z_i^+)/\tau)}{\sum_{j\in B\cup M\setminus\{i\}}\exp(\text{sim}(z_i,z_j)/\tau)}$ (Eq. 1)
- **Definition**: A contrastive loss whose positives are two augmented views of the same scan within one modality (MRI↔MRI or PET↔PET); negatives are other samples in the batch $B$ plus an optional MoCo memory queue $M$. Cosine similarity $\text{sim}(u,v)=u^\top v$, temperature $\tau>0$.
- **Boundary conditions**: Applies within a single modality; requires medically safe augmentations (flips, ≤10° rotations, Gaussian blur, ±10% intensity jitter, random 3D crops).
- **Related concepts**: Cross-modal InfoNCE, MoCo queue, temperature scaling.

## Cross-modal MRI↔PET InfoNCE
- **Notation**: $\mathcal{L}_{cross}$ (Eq. 2) — symmetric InfoNCE with MRI and PET alternating as anchors.
- **Definition**: A contrastive alignment loss whose positives are co-registered MRI–PET embeddings $(z^{MRI}_i, z^{PET}_i)$ from the same subject at the same visit; it pulls the two modalities' representations together in the shared embedding space.
- **Boundary conditions**: Requires paired MRI–PET at the same visit; datasets providing MRI±PET (ADNI, OASIS-3, AIBL, BioFINDER) supply positives.
- **Related concepts**: Intra-modal InfoNCE, cross-modal alignment, PET→MRI distillation.

## Longitudinal consistency
- **Notation**: $\mathcal{L}_{long}=\sum_p\sum_{t_1\neq t_2\in T_p}\lVert z^m_{p,t_1}-z^m_{p,t_2}\rVert_2^2,\ m\in\{MRI,PET\}$ (Eq. 3); optional cross-time cross-modal $\mathcal{L}_{long\_x}$ (Eq. 4).
- **Definition**: An L2 penalty encouraging a subject's embeddings across visits to vary smoothly, reflecting a gradual disease trajectory. Enabled only where repeat visits exist (typically ADNI).
- **Boundary conditions**: Requires longitudinal data; disabled for single-timepoint cohorts. The cross-time cross-modal term needs longitudinal MRI *and* PET to co-exist.
- **Related concepts**: BYOL regression, disease trajectory, atrophy sensitivity.

## BYOL-style regression (negative-free stabilization)
- **Notation**: $\mathcal{L}_{byol}=\sum_{i\in B}\lVert q_\omega(z_i)-\text{sg}(z_i^+)\rVert_2^2$ (Eq. 5)
- **Definition**: A self-distillation loss with an online predictor $q_\omega$ and a stop-gradient (sg) target branch, used to stabilize training without negative pairs.
- **Boundary conditions**: Complements contrastive terms; stop-gradient prevents representation collapse.
- **Related concepts**: Intra-modal InfoNCE, PET→MRI distillation.

## Domain-adversarial site invariance (GRL)
- **Notation**: $\mathcal{L}_{site}=\mathbb{E}[\text{CE}(D_\psi(z),s_p)]$ (Eq. 6), optimized through a gradient-reversal layer (GRL).
- **Definition**: A discriminator $D_\psi$ predicts the site/scanner label $s_p$ from embeddings while a GRL reverses its gradient into the encoders, forcing them to remove site-specific signal from the latent space. Site labels are reserved for this term only and are never given to prediction heads.
- **Boundary conditions**: Assumes site variance is separable from disease-relevant variance; complements offline harmonization.
- **Related concepts**: ComBat harmonization, DSBN/GroupNorm, cross-cohort transfer.

## Missing-aware gating late fusion
- **Notation**: $\alpha=\sigma(w^\top[\mathbb{1}_{MRI},\mathbb{1}_{PET}])\in[0,1]$; $e=[\alpha z^{MRI}\ \Vert\ (1-\alpha)z^{PET}\ \Vert\ c]$ (Eq. 8)
- **Definition**: A learned scalar gate $\alpha$ blends MRI and PET embeddings based on availability indicators $\mathbb{1}_{MRI},\mathbb{1}_{PET}$; clinical covariates $c$ are concatenated. When PET is missing, $\alpha\!\to\!1$ so fusion collapses to MRI-only.
- **Boundary conditions**: Late fusion at the embedding level; supports MRI-only inference.
- **Related concepts**: PET→MRI distillation, cross-modal InfoNCE.

## PET→MRI distillation
- **Notation**: $\mathcal{L}_{distill}=\frac{1}{N}\sum_n \mathbb{1}_{PET,n}\lVert z^{MRI}_n-\text{sg}(z^{PET}_n)\rVert_2^2$ (Eq. 11)
- **Definition**: A training-only loss (active when PET is present) that pulls the MRI embedding toward the stop-gradient PET (teacher) embedding, transferring molecular information into the MRI pathway to support robust MRI-only deployment.
- **Boundary conditions**: Applied only during training and only for subjects with PET; not used at inference.
- **Related concepts**: Missing-aware gating, cross-modal InfoNCE, BYOL.

## ComBat harmonization
- **Notation**: —
- **Definition**: An offline batch-effect correction that uses site/scanner as the batch variable and biological covariates (age, sex) as protected covariates to remove non-biological site effects while retaining disease-relevant variability. Applied after whole-brain histogram matching to an ADNI-derived reference template.
- **Boundary conditions**: Applied separately per modality and identically across all timepoints of a subject to preserve longitudinal consistency.
- **Related concepts**: Histogram matching, DSBN/GroupNorm, site invariance.

## Domain-Specific BatchNorm (DSBN) / GroupNorm
- **Notation**: —
- **Definition**: In-network normalization used to reduce site-specific batch-statistic drift; DSBN maintains per-domain batch statistics while GroupNorm normalizes over channel groups independent of batch composition.
- **Boundary conditions**: Complements offline harmonization; ablated (GroupNorm vs DSBN) in §3.8.
- **Related concepts**: ComBat, site invariance.

## Balanced accuracy (BACC / BAC)
- **Notation**: $\text{BAC}=\tfrac12(\text{TPR}+\text{TNR})$ (Eq. 14)
- **Definition**: The average of true-positive rate (sensitivity) and true-negative rate (specificity); used as the primary diagnosis metric because of class imbalance.
- **Boundary conditions**: Reported with 95% bootstrap CIs and DeLong AUC comparison in the stated protocol (though CIs are not tabulated).
- **Related concepts**: AUC, specificity, expected calibration error.

## Harrell's C-index
- **Notation**: $C=\frac{1}{|P|}\sum_{(i,j)\in P}\mathbb{1}[(T_i<T_j)\wedge(r_i>r_j)]$, $P=\{(i,j):\delta_i=1,T_i<T_j\}$ (Eq. 15)
- **Definition**: Concordance index for survival prediction — the fraction of comparable subject pairs whose predicted risk order matches their observed event-time order. Used for MCI→AD prognosis.
- **Boundary conditions**: Requires survival targets $(T_p,\delta_p)$ (time to conversion, event/censor indicator).
- **Related concepts**: Cox partial log-likelihood, time-dependent AUC, integrated Brier score.

## Integrated Brier Score (IBS)
- **Notation**: $\text{IBS}=\frac{1}{\tau}\int_0^\tau \text{Brier}(t)\,dt$ (Eq. 16), computed with IPCW.
- **Definition**: Time-integrated squared error between predicted survival probability and observed status, weighted by inverse probability of censoring; lower is better.
- **Boundary conditions**: Standard survival-analysis calibration/accuracy metric.
- **Related concepts**: C-index, time-dependent AUC, ECE.

## Expected Calibration Error (ECE)
- **Notation**: $\text{ECE}=\sum_{m=1}^{M}\frac{|B_m|}{N}\,|\text{acc}(B_m)-\text{conf}(B_m)|$ (Eq. 17), $M$ equal-mass bins.
- **Definition**: The average gap between predicted confidence and empirical accuracy across probability bins; lower means better-calibrated probabilities. The model applies post-hoc temperature scaling (Eq. 12) to improve it.
- **Boundary conditions**: Reported on ADNI and BioFINDER (Figure 10); values differ between the tables/prose and figure legends (see constraints.md).
- **Related concepts**: Temperature scaling, balanced accuracy, reliability curves.
