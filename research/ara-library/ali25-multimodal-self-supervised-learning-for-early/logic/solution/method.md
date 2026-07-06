# Method — Two-Stage Multimodal SSL Pipeline

Source: §3 (Proposed Methodology), Figures 3, 4, 5, 6.

## Problem setup (§3.1)
Subjects $p\in\{1,\dots,P\}$ with visits $t\in T_p$. At each visit: co-registered 3D volumes
$x^{MRI}_{p,t},x^{PET}_{p,t}\in\mathbb{R}^{H\times W\times D}$, optional clinical covariates
$c_{p,t}\in\mathbb{R}^q$, diagnosis label $y_{p,t}\in\{0,\dots,K-1\}$ (e.g. CN/EMCI/LMCI/AD), and a
site/scanner label $s_p\in\{1,\dots,S\}$. For prognosis, survival targets $(T_p,\delta_p)$ where $T_p$
is months-to-conversion and $\delta_p\in\{0,1\}$ indicates conversion (1) or censoring (0).

Two modality-specific encoders $f^{MRI}_\theta, f^{PET}_{\theta'}$ and a projection head $g_\phi$ map a
volume $x$ to an $\ell_2$-normalized embedding $z=g_\phi(f_\vartheta(x))/\lVert g_\phi(f_\vartheta(x))\rVert_2\in\mathbb{R}^d$.
Cosine similarity $\text{sim}(u,v)=u^\top v\in[-1,1]$; temperature $\tau>0$.

All train/val/test splits are done strictly at the **subject level** so all timepoints of a patient
stay in the same fold (no temporal leakage).

## Stage 1 — Self-supervised pretraining (§3.3, Figure 4)
Medically safe 3D augmentations (flips, ≤10° rotations, Gaussian blur, ±10% intensity jitter, random
3D crops) define three families of positives:
1. **Intra-modal** — two augmented views of the same scan (MRI↔MRI, PET↔PET).
2. **Cross-modal** — co-registered MRI–PET pairs at the same visit.
3. **Longitudinal** — same subject across visits (MRI↔MRI, PET↔PET).

Five objectives are optimized (details and equations in `algorithm.md`):
- Intra-modal InfoNCE (Eq. 1)
- Cross-modal symmetric InfoNCE with MRI/PET alternating anchors (Eq. 2)
- Longitudinal consistency (Eq. 3) + optional cross-time cross-modal coupling (Eq. 4)
- BYOL-style regression with predictor $q_\omega$ and stop-gradient target (Eq. 5)
- Domain-adversarial site invariance via discriminator $D_\psi$ and gradient-reversal layer (Eq. 6)

Combined as a weighted sum $\mathcal{L}_{SSL}=\lambda_1\mathcal{L}_{intra}+\lambda_2\mathcal{L}_{cross}+\lambda_3\mathcal{L}_{byol}+\lambda_4\mathcal{L}_{long}+\lambda_5\mathcal{L}_{long\_x}+\lambda_3\mathcal{L}_{site}$ (Eq. 7).
(As printed, $\lambda_3$ weights both $\mathcal{L}_{byol}$ and $\mathcal{L}_{site}$ — reproduced verbatim from the source.)

Execution order (Figure 4): Step 0 input volumes → Step 1 medical-safe augmentations → Step 2
encoders + projection heads (3D ResNet/Swin + MLP) → Steps 3–6 SSL objectives → Step 7 site-invariance
(GRL → site discriminator) → Step 8 total SSL loss → Step 9 pretrained weights → initialize Stage 2.
Data-pool assignment (Figure 6): unlabeled SSL pool = ADNI, OASIS-3, AIBL, BioFINDER; labeled
fine-tuning = ADNI (diagnosis & MCI→AD), OASIS-3, TADPOLE (prognosis labels); MIRIAD reliability-only.

## Stage 2 — Multi-task fine-tuning (§3.4, Figure 5)
Encoders are initialized with the best SSL checkpoint. **Missing-aware gating late fusion**: a learned
gate $\alpha=\sigma(w^\top[\mathbb{1}_{MRI},\mathbb{1}_{PET}])$ blends modalities into
$e=[\alpha z^{MRI}\Vert(1-\alpha)z^{PET}\Vert c]$ (Eq. 8). When PET is missing, $\alpha\!\to\!1$ so
$(1-\alpha)\!\to\!0$ and inference is MRI-only.

Heads:
- **Diagnosis head** $h_\psi$: logits $l=h_\psi(e)\in\mathbb{R}^K$, class-weighted cross-entropy (Eq. 9).
- **Survival head** $r_\varphi(e)$: risk score for Cox partial log-likelihood (Eq. 10); Figure 6 notes DeepHit optional.
- **PET→MRI distillation** (Eq. 11): training-only L2 pulling MRI embedding toward stop-gradient PET embedding for subjects with PET.
- **Temperature scaling** (Eq. 12): post-hoc calibration on validation, encoder weights frozen.

Joint objective $\mathcal{L}_{FT}=\alpha\mathcal{L}_{diag}+\beta\mathcal{L}_{cox}+\gamma\mathcal{L}_{distill}$ (Eq. 13), non-negative $\alpha,\beta,\gamma$.
(The symbol $\alpha$ is overloaded: the fusion gate in Eq. 8 and a loss weight in Eq. 13 — reproduced from the source.)

## Stage 3 — Evaluation (§3.6, §3.7)
- In-distribution: subject-level, site-stratified 5-fold CV.
- OOD: train ADNI → test OASIS-3 and reverse; external AIBL/BioFINDER when available.
- Reliability: MIRIAD held out for scan–rescan ICC (ICC3,1), within-subject CV, and SRM.
- Metrics: BACC (Eq. 14), AUC, F1, sensitivity@fixed-specificity; C-index (Eq. 15), tdAUC(t), IBS (Eq. 16, IPCW); ECE (Eq. 17). 95% bootstrap CIs and DeLong AUC comparison are stated.
