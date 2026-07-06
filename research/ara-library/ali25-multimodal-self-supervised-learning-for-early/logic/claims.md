# Claims

> All values are point estimates reported by the paper. The paper describes bootstrap 95% CIs and
> DeLong tests in §3.6 but **does not report CIs or test statistics** in any results table; "statistical
> significance" is asserted in the abstract/§5 without accompanying numbers. Numbers are copied
> exactly from the source; internal source inconsistencies are flagged per claim and in
> `solution/constraints.md`.

## C01: State-of-the-art ADNI AD-vs-CN diagnosis
- **Statement**: On the ADNI AD-vs-CN binary diagnosis benchmark the proposed framework attains 93.0% balanced accuracy, 93.6% precision, 93.2% specificity, and 0.96 AUC — the best on every axis among five compared methods, improving balanced accuracy by +0.6% over the prior best DiaMond'25 (92.4%).
- **Status**: supported
- **Falsification criteria**: Under the paper's site-stratified 5-fold CV protocol on ADNI, if the framework's BACC or AUC does not exceed DiaMond'25 (92.4% / 0.95) and the other baselines, or the +0.6% BACC gain does not hold, the claim fails.
- **Proof**: [E01]
- **Evidence basis**: Table 3 lists Proposed = 93.0/93.6/93.2/0.96 vs DiaMond'25 = 92.4/93.0/92.8/0.95; Figure 9a legend confirms Proposed AUC=0.96, DiaMond'25 AUC=0.95.
- **Interpretation**: The +0.6% BACC margin over DiaMond'25 is small; the paper itself notes "even modest accuracy gains translate to meaningful improvements in patient identification" (§5).
- **Dependencies**: none
- **Tags**: diagnosis, ADNI, in-distribution, classification
- **Sources**:
  - 93.0% BACC ← `evidence/tables/table3.md` / paper p.17 «It produces the best balanced accuracy (93.0%), precision (93.6%), and specificity (93.2%), as well as the best discrimination ability with an AUC of 0.96.» [result]
  - +0.6% over DiaMond'25 ← paper p.17 «Compared to DiaMond'25 ... our approach improves balanced accuracy by +0.6%» [result]
  - DiaMond'25 = 92.4 ← `evidence/tables/table3.md` «DiaMond'25 | 92.4 | 93.0 | 92.8 | 0.95» [result]

## C02: Cross-cohort generalization under site-invariant learning
- **Statement**: Trained on ADNI and transferred to unseen cohorts, the framework reaches 78.0% BACC / 0.87 AUC on OASIS-3 and 77.5% BACC / 0.85 AUC on AIBL, the best transfer performance among baselines and exceeding DiaMond'25 by roughly +1.0% (OASIS-3) and +1.5% (AIBL) BACC.
- **Status**: supported
- **Falsification criteria**: If ADNI→OASIS-3 or ADNI→AIBL transfer BACC/AUC does not lead all baselines, or the site-invariance ablation (removing Lsite) does not reduce the transfer gap, the claim fails.
- **Proof**: [E02]
- **Evidence basis**: Table 4 (OASIS-3): Proposed 78.0/78.2/78.4/0.87. Table 5 (AIBL): Proposed 77.5/77.8/77.9/0.85. Both are the top row on all metrics.
- **Interpretation**: Transfer BACC (~77–78%) is far below in-distribution ADNI BACC (93.0%), so "strong generalization" is relative to baselines, not an absolute retention of accuracy.
- **Dependencies**: C01
- **Tags**: generalization, OOD, transfer, site-invariance
- **Sources**:
  - OASIS-3 78.0% / 0.87 ← paper p.17 «achieves the best overall performance, with a balanced accuracy of 78.0% and an AUC of 0.87» [result]
  - AIBL 77.5% / 0.85 ← paper p.18 «BACC of 77.5% and an AUC = 0.85, surpassing DiaMond'25 by +1.5% BACC» [result]

## C03: TADPOLE longitudinal MCI→AD prognosis
- **Statement**: On the TADPOLE MCI→AD conversion benchmark (3-year horizon) the framework achieves 84.0% BACC, 0.85 AUC, 0.82 C-index, 0.82 tdAUC@36m, and 0.16 integrated Brier score — best across nearly all metrics, with +3% BACC and +0.03 AUC over SMoCo.
- **Status**: supported
- **Falsification criteria**: If C-index or tdAUC@36m does not exceed the SSL baselines (SMoCo, DiaMond'25), or IBS is not the lowest, the claim fails.
- **Proof**: [E03]
- **Evidence basis**: Table 7: Proposed 84.0/84.2/84.3/0.85/0.82/0.82/0.16; SMoCo 81.0/.../0.82/0.79/0.79/0.18; DiaMond'25 82.5/.../0.84/0.80/0.82/0.17. Figure 9b legend confirms Proposed AUC=0.85.
- **Interpretation**: DiaMond'25 already matches the proposed tdAUC@36m (0.82); the margin is largest on BACC and IBS.
- **Dependencies**: none
- **Tags**: prognosis, survival, TADPOLE, C-index, longitudinal
- **Sources**:
  - 84.0% / 0.85 / 0.82 ← paper p.18–19 «with 84.0% BACC, 0.85 AUC, and a 0.82 C-index» [result]
  - tdAUC@36m 0.82 vs 0.79 ← paper p.19 «The improved tdAUC@36m (0.82 vs. 0.79 for SMoCo)» [result]
  - IBS 0.16 ← paper p.19 «the lowest integrated Brier score (0.16)» [result]
  - +3% BACC / +0.03 AUC over SMoCo ← paper p.19 «our approach achieves +3% gain in BACC and +0.03 AUC» [result]

## C04: High test–retest reliability and atrophy sensitivity on MIRIAD
- **Statement**: On MIRIAD (held-out scan–rescan reliability cohort) the framework attains 87.0% BACC, 0.88 AUC, test–retest ICC = 0.91, and atrophy sensitivity 76.5% — the highest reliability among compared methods, beating DiaMond'25 by +2% BACC and +2.5% atrophy sensitivity.
- **Status**: supported
- **Falsification criteria**: If ICC ≤ the best baseline (DiaMond'25 ICC=0.89) or atrophy sensitivity does not lead, the claim fails.
- **Proof**: [E04]
- **Evidence basis**: Table 8: Proposed 87.0/87.2/87.4/0.88/0.91/76.5; DiaMond'25 85.0/.../0.86/0.89/74.0.
- **Interpretation**: ICC 0.91 vs 0.89 (DiaMond'25) indicates modestly higher scan–rescan consistency; the reliability metric is distinct from diagnostic accuracy.
- **Dependencies**: none
- **Tags**: reliability, ICC, MIRIAD, atrophy, test-retest
- **Sources**:
  - 87.0% / 0.88 / ICC 0.91 / 76.5% ← paper p.18 «the best balanced accuracy (87.0%) and AUC (0.88), as well as the highest test–retest intraclass correlation (ICC = 0.91) and atrophy sensitivity (76.5%)» [result]
  - +2% BACC / +2.5% sensitivity over DiaMond'25 ← paper p.18 «against DiaMond'25 by +2% BACC and by +2:5% in terms of sensitivity» [result]

## C05: MRI-based ATN biomarker prediction on BioFINDER
- **Statement**: On BioFINDER the framework predicts ATN biomarker status from MRI, improving over Radiology'23 on amyloid (83.0% vs 79.0% BACC) and tau (75.0% vs 73.0% BACC) and matching it on neurodegeneration (0.86 AUC; 85.5% vs 86.0% BACC).
- **Status**: supported
- **Falsification criteria**: If amyloid or tau BACC does not exceed Radiology'23, or neurodegeneration AUC differs materially, the claim fails.
- **Proof**: [E05]
- **Evidence basis**: Table 6 rows — Amyloid: Radiology'23 79.0/.../0.79; Proposed 83.0/.../0.83. Tau: Radiology'23 73.0/.../0.73; Proposed 75.0/.../0.75. Neurodegeneration: Radiology'23 86.0/.../0.86; Proposed 85.5/.../0.86.
- **Interpretation**: Non-invasive MRI surrogates for amyloid/tau could reduce reliance on PET/CSF; neurodegeneration BACC is actually slightly lower (85.5 vs 86.0) though AUC ties at 0.86.
- **Dependencies**: none
- **Tags**: biomarker, ATN, amyloid, tau, BioFINDER
- **Sources**:
  - amyloid 83% vs 79%, tau 75% vs 73%, neurodeg 0.86 ← paper p.18 «amyloid (83% vs. 79%) and tau (75% vs. 73%) and comparable performance on neurodegeneration status (0.86 AUC)» [result]

## C06: Improved probability calibration
- **Statement**: The framework reports the lowest expected calibration error (ECE) among compared methods on the tabulated cohorts, e.g. 5.9% on BioFINDER AD-vs-CN (vs 6.2–7.8% for baselines).
- **Status**: supported
- **Falsification criteria**: If the proposed ECE is not the lowest in a cohort where it is compared, the claim fails.
- **Proof**: [E07]
- **Evidence basis**: Table 6 ECE column (AD vs CN): Proposed 5.9%, ISBI'23 6.2%, DiaMond'25 7.1%, AnatCL 7.2%, SMoCo 7.8%. Text also cites OASIS-3 ECE 6.9% and AIBL ECE 6.6% (prose only; not in Tables 4/5).
- **Interpretation**: **Internal inconsistency**: the ECE values in Figure 10 legends (ADNI Proposed 2.8%, DiaMond'25 2.9%; BioFINDER Proposed 3.0%) disagree with the prose ADNI values (4.2%→3.9%) and with the Table 6 BioFINDER value (5.9%). Treated as a supported-but-inconsistent claim; see constraints.md.
- **Dependencies**: C05
- **Tags**: calibration, ECE, reliability
- **Sources**:
  - BioFINDER Proposed ECE 5.9% ← `evidence/tables/table6.md` «Proposed | 77.5 | 77.8 | 77.9 | 0.85 | 5.9» [result]
  - ADNI ECE 4.2%→3.9% (prose) ← paper p.17 «reduces calibration error from 4.2% to 3.9%» [result]
  - Figure 10 legend ECE (conflicting) ← `evidence/figures/figure10.md` «Proposed (ECE=2.8%) ... DiaMond'25 (ECE=2.9%)» [result]

## C07: First unified cross-modal + longitudinal + site-invariant SSL framework
- **Statement**: The work is presented as the first framework to unify, in a single SSL pipeline, cross-modal MRI–PET learning, longitudinal consistency across patient timepoints, and explicit site/domain-invariance.
- **Status**: hypothesis
- **Falsification criteria**: Identifying a prior published framework that jointly implements all three axes (cross-modal fusion, longitudinal consistency, and explicit domain-adversarial site invariance) in one SSL pipeline would refute the novelty claim.
- **Proof**: [E06]
- **Evidence basis**: §1 asserts "no prior work has unified all the following elements in one framework: cross-modal MRI–PET learning, longitudinal consistency across patient timepoints, and explicit site/domain-invariance"; the literature review (§2, Table 1) documents that each prior method covers only a subset. This is a novelty/positioning claim, not an empirical result.
- **Interpretation**: The claim is architectural/positional; the ablation study (§3.8) that would isolate each objective's contribution is described but its results are not reported, so the *value* of the unification is not empirically quantified in the paper.
- **Dependencies**: C01, C02, C03, C04
- **Tags**: novelty, unification, positioning
- **Sources**:
  - unification claim ← paper p.3 «no prior work has unified all the following elements in one framework: cross-modal MRI–PET learning, longitudinal consistency across patient timepoints, and explicit site/domain-invariance» [result]
