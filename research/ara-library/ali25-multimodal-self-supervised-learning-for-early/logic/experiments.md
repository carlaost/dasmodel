# Experiments

Declarative verification plans reconstructed from the paper's Experimental Protocol (§3.7),
Ablations (§3.8), and Results (§5). No exact numbers appear here — see `evidence/` for values.

## E01: In-distribution ADNI AD-vs-CN diagnosis
- **Verifies**: C01, C06
- **Setup**:
  - Model: Two-stage multimodal SSL (3D ResNet-50 or 3D Swin Transformer backbone + projection MLP) pretrained then fine-tuned with gating fusion + diagnosis head
  - Hardware: Not specified in paper
  - Dataset: ADNI (>2000 subjects; CN vs AD subset), MRI ± PET
  - System: Subject-level, site-stratified 5-fold cross-validation; no subject/visit leakage across folds
- **Procedure**:
  1. SSL-pretrain encoders on unlabeled ADNI (+OASIS-3, and AIBL/BioFINDER when licensing permits) optimizing the weighted SSL objective (Eq. 7)
  2. Select best SSL checkpoint by linear probe on a held-out validation fold
  3. Fine-tune with class-weighted cross-entropy diagnosis head (Eq. 9) and gating fusion (Eq. 8)
  4. Fit temperature $T$ (Eq. 12) on validation predictions
  5. Report metrics per fold vs baselines ISBI'23, AnatCL, DiaMond'25, SMoCo
- **Metrics**: Balanced accuracy (%), precision (%), specificity (%), AUC, ECE (%); 95% bootstrap CIs and DeLong AUC test (protocol-stated)
- **Expected outcome**:
  - Proposed leads all baselines on BACC, precision, specificity, and AUC
  - Proposed improves BACC over the prior-best transformer baseline and lowers calibration error
- **Baselines**: ISBI'23, AnatCL, DiaMond'25, SMoCo
- **Dependencies**: none

## E02: Cross-cohort out-of-distribution transfer
- **Verifies**: C02
- **Setup**:
  - Model: Same framework, trained on one cohort and evaluated on another with no site/subject leakage
  - Dataset: Train ADNI → test OASIS-3 (and reverse); additional external tests on AIBL and BioFINDER
  - System: Site-agnostic training (no site labels to prediction heads); site-adversarial term active in pretraining
- **Procedure**:
  1. Pretrain + fine-tune on the source cohort
  2. Apply the two-stage harmonization (histogram matching + ComBat) and DSBN/GroupNorm
  3. Evaluate zero-additional-training on the unseen target cohort
  4. Compare transfer degradation vs baselines
- **Metrics**: Balanced accuracy (%), precision (%), specificity (%), AUC; calibration error (prose)
- **Expected outcome**:
  - Proposed achieves the best transfer BACC/AUC on OASIS-3 and AIBL
  - Site-invariant learning yields smaller performance drop than baselines on unseen cohorts
- **Baselines**: AnatCL, DiaMond'25, ISBI'23, SMoCo
- **Dependencies**: E01

## E03: TADPOLE longitudinal MCI→AD prognosis
- **Verifies**: C03
- **Setup**:
  - Model: Framework with Cox survival head $r_\varphi(e)$ (Eq. 10); DeepHit noted optional in Figure 6
  - Dataset: TADPOLE (219 ADNI rollover subjects), multimodal baselines (MRI, PET, CSF, APOE, cognition), 3-year conversion horizon
  - System: Subject-level splits; survival targets $(T_p,\delta_p)$
- **Procedure**:
  1. Fine-tune with the Cox partial log-likelihood head alongside the diagnosis head (joint objective Eq. 13)
  2. Predict MCI→AD conversion risk over the horizon
  3. Evaluate discrimination and survival calibration vs SSL baselines
- **Metrics**: BACC (%), precision (%), specificity (%), AUC, C-index, time-dependent AUC@36m, integrated Brier score
- **Expected outcome**:
  - Proposed leads on BACC, AUC, C-index, and IBS
  - Explicit longitudinal supervision yields gains over contrastive-only SMoCo
- **Baselines**: SMoCo, ISBI'23, AnatCL, DiaMond'25
- **Dependencies**: none

## E04: MIRIAD test–retest reliability and atrophy sensitivity
- **Verifies**: C04
- **Setup**:
  - Model: Same framework; MIRIAD held out entirely (never used for pretraining when reported as external test)
  - Dataset: MIRIAD (69 adults: 46 AD, 23 CN), T1 MRI, scanned up to eight times over 2 years on the same 1.5T system
  - System: Scan–rescan reliability protocol
- **Procedure**:
  1. Compute test–retest ICC (ICC3,1) and within-subject coefficient of variation on repeat scans
  2. Compute standardized response mean (SRM) / atrophy sensitivity for detecting longitudinal change
  3. Compare reliability vs baselines
- **Metrics**: BACC (%), AUC, test–retest ICC, atrophy sensitivity (%), within-subject CV, SRM
- **Expected outcome**:
  - Proposed attains the highest ICC and atrophy sensitivity
  - Higher reliability than transformer/contrastive baselines
- **Baselines**: ISBI'23, AnatCL, DiaMond'25, SMoCo
- **Dependencies**: none

## E05: BioFINDER ATN biomarker prediction from MRI
- **Verifies**: C05
- **Setup**:
  - Model: Framework fine-tuned to predict amyloid (A+/−), tau (T+/−), and neurodegeneration (N+/−) status
  - Dataset: BioFINDER (~2000; MRI, amyloid & tau PET, CSF)
  - System: MRI-based prediction of ATN status as surrogate of PET/CSF pathology
- **Procedure**:
  1. Fine-tune classification heads for each ATN axis
  2. Compare MRI-based predictions against the Radiology'23 AT(N) baseline
- **Metrics**: BACC (%), precision (%), specificity (%), AUC, ECE (%)
- **Expected outcome**:
  - Proposed exceeds Radiology'23 on amyloid and tau BACC and matches on neurodegeneration
- **Baselines**: Radiology'23 (AnatCL/DiaMond'25/ISBI'23/SMoCo for AD-vs-CN sub-table)
- **Dependencies**: none

## E06: SSL-component and harmonization ablations (described, results not reported)
- **Verifies**: C07
- **Setup**:
  - Model: Framework variants with individual components removed
  - Dataset: Same cohorts and splits as the main model (for direct comparison)
  - System: Identical optimization settings across ablations
- **Procedure**:
  1. Ablate $\mathcal{L}_{cross}$, $\mathcal{L}_{long}$, and $\mathcal{L}_{site}$ in isolation
  2. Compare 2D vs 3D backbones; MRI-only vs MRI+PET; joint-dataset SSL vs per-dataset SSL
  3. Toggle ComBat; compare GroupNorm vs DSBN; remove histogram matching, remove ComBat, remove both
  4. Disable longitudinal losses for cohorts lacking repeat visits (temporal sensitivity)
  5. Compare cohort-level intensity distributions before/after harmonization
- **Metrics**: In-distribution accuracy, cross-cohort generalization, longitudinal stability; magnitude of site drift
- **Expected outcome**:
  - Each of cross-modal, longitudinal, and site-invariance objectives contributes positively
  - 3D > 2D; MRI+PET > MRI-only; joint SSL > per-dataset SSL; harmonization reduces site drift
  - **NOTE**: The paper *describes* this ablation plan (§3.8) but reports NO ablation result tables or figures; the component contributions are therefore asserted but not empirically shown.
- **Baselines**: Ablated variants of the proposed model (self-comparison)
- **Dependencies**: E01

## E07: Calibration reliability analysis
- **Verifies**: C06
- **Setup**:
  - Model: Framework with post-hoc temperature scaling (Eq. 12)
  - Dataset: ADNI and BioFINDER (AD vs CN)
  - System: Reliability curves over equal-mass probability bins
- **Procedure**:
  1. Fit temperature $T$ on a validation fold
  2. Bin predictions and compute ECE (Eq. 17)
  3. Plot reliability curves vs perfect calibration and vs baselines
- **Metrics**: Expected calibration error (%); reliability curve proximity to the diagonal
- **Expected outcome**:
  - Proposed is closest to perfect calibration with the lowest ECE across bins
  - **NOTE**: reported ECE values are internally inconsistent between Figure 10 legends and the tables/prose (see constraints.md)
- **Baselines**: ISBI'23, AnatCL, DiaMond'25, SMoCo, Radiology'23
- **Dependencies**: E01
