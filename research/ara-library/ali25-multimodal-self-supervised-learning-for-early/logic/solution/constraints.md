# Constraints, Assumptions, and Limitations

## Boundary conditions
- **Modality pairing**: cross-modal InfoNCE (Eq. 2) requires co-registered MRI–PET at the same visit; when PET is missing, only intra-modal/longitudinal terms and the gating fallback apply.
- **Longitudinal terms**: $\mathcal{L}_{long}$ (Eq. 3) is enabled only where repeat visits exist; the cross-time cross-modal term (Eq. 4) requires longitudinal MRI *and* PET to co-exist (typically only ADNI).
- **Site-adversarial term**: site labels $s_p$ are used only for the domain-adversarial loss and never passed to prediction heads.
- **Subject-level splits**: all folds partition at the subject level so all timepoints of a patient remain in one fold (prevents temporal leakage).
- **MIRIAD**: held out entirely for external longitudinal reliability/sensitivity; never used for pretraining when reported as an external test.

## Assumptions
- Site/scanner variance is separable and removable without discarding disease-relevant signal (adversarial + ComBat).
- A missing training-time modality can be partially compensated by distillation from the available modality (Eq. 11).
- Baseline numbers reflect each method's own reported protocols/metrics "whenever available" (§5) — baselines are re-tabulated, not necessarily re-run under identical conditions on the authors' splits.
- Reported "statistical significance" (abstract, §5) rests on the stated bootstrap-CI/DeLong protocol, but the supporting statistics are not shown.

## Known limitations (stated by the authors, §6)
- Future work is needed to validate with fluid biomarkers, broader scanner/protocol harmonization analyses, and additional clinical metadata — implying the current evaluation does not yet include these.

## Limitations / caveats identified during compilation (not claimed by the authors)
- **No released code or weights.** §3.2 and §3.5 state that "all seeds, preprocessing versions, and split files are released to ensure exact reproducibility," but no repository URL (GitHub/GitLab/Zenodo/OSF) appears in the article, Data Availability Statement, or supplement, and none was found on search (see `sources.yaml`). The reproducibility artifacts are therefore not locatable.
- **Ablations described but not reported.** §3.8 lays out ablations of $\mathcal{L}_{cross}/\mathcal{L}_{long}/\mathcal{L}_{site}$, 2D vs 3D, MRI-only vs MRI+PET, joint vs per-dataset SSL, ComBat toggling, GroupNorm vs DSBN, and histogram-matching removal — but **no ablation result table or figure appears**. The contribution of each component (and thus the empirical value of the unification claim C07) is asserted, not shown.
- **No confidence intervals in tables.** §3.6 specifies 95% bootstrap CIs and the DeLong test, but Tables 3–8 report point estimates only; abstract/§5 claims of "statistically significant" gains are unsupported by shown statistics.
- **Internal numerical inconsistencies (reproduced verbatim, not corrected):**
  - *BioFINDER AD-vs-CN:* prose (p.18) states "the highest balanced accuracy (85.0%) and AUC (0.89)" but **Table 6** lists Proposed = 77.5% BACC / 0.85 AUC (ECE 5.9%). The table's 77.5% is also what the "+1.5% BACC over DiaMond'25 (76.0%)" arithmetic implies; the 85.0%/0.89 figures in the prose appear erroneous.
  - *Calibration (ECE):* Figure 10 legends give ADNI Proposed ECE=2.8%, DiaMond'25=2.9% (and ISBI'23=1.9%, AnatCL=4.0%, SMoCo=4.0%) and BioFINDER Proposed ECE=3.0%; these disagree with the prose ADNI values ("4.2% to 3.9%") and with Table 6's BioFINDER ECE (5.9%).
  - *OASIS-3 / AIBL ECE:* prose cites ECE 6.9% (OASIS-3) and 6.6% (AIBL), but Tables 4 and 5 contain no ECE column.
  - *TADPOLE horizon:* the abstract/text describe MCI→AD conversion generally; §5 states a "3-year horizon" while Table 2 lists TADPOLE as "predict 5 yrs" and tdAUC is reported "@36m".
- **Citation numbering errors** (see `related_work.md`): the ISBI'23 fusion baseline is cited as both [6] and [22]; DIM is attributed to "Jack et al. 2010 [20]"; the GAN synthesis work is labeled "Zhang et al. 2023" but is ref [27] Wang et al. 2024; the TADPOLE paragraph cites "SMoCo [38]" though [38] is the MIRIAD dataset; the Data Availability Statement points to "[27–37]" while dataset refs run [28–38].
- **Hyperparameters partially specified**: loss weights $\lambda_1..\lambda_5$ and $\alpha,\beta,\gamma$ (Eq. 7, 13), embedding dimension $d$, exact backbone choice per experiment, and hardware are not reported.
- **Sample sizes are approximate** in Table 2 (e.g. ADNI ">2000", OASIS-3 "~1100", BioFINDER "~2000"); exact per-group counts used for each result are not given.
