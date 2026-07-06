# Related Work — Typed Dependency Graph

> Note on citation hygiene: the paper's inline citation numbers are inconsistent in several places
> (e.g. the "ISBI 2023" fusion baseline is cited as both [6] and [22]; the GAN cross-modal work is
> attributed to "Zhang et al. (2023)" in Table 1 but reference [27] is Wang et al. 2024; Deep InfoMax
> is attributed to "Jack et al. (2010)" [20] in §2.2 though [20] is the biomarker-cascade paper and DIM
> corresponds to Fedorov et al. [26]; the TADPOLE prognosis paragraph cites "SMoCo [38]" but [38] is
> the MIRIAD dataset). Blocks below map to the works by author/method identity, flagging conflicts.

## RW01: Li et al., 2025 — DiaMond (primary transformer baseline)
- **DOI**: 10.1109/WACV.2025 (WACV 2025, pp. 107–116); ref [6]
- **Type**: baseline
- **Delta**:
  - What changed: DiaMond is a bi-modal ViT using a bi-attention mechanism to fuse MRI and PET, achieving SOTA on AD vs frontotemporal dementia. The proposed work adds longitudinal consistency and explicit domain-adversarial site invariance that DiaMond lacks.
  - Why: to gain cross-cohort robustness and longitudinal reliability beyond a fusion-only transformer.
- **Claims affected**: C01, C02, C03, C04, C06, C07
- **Adopted elements**: MRI–PET fusion motivation; transformer backbone option (3D Swin).

## RW02: Kwak et al., 2023 — SMoCo (PET contrastive baseline)
- **DOI**: 10.3390/bioengineering10101141 (Bioengineering 2023, 10, 1141); ref [1]
- **Type**: baseline
- **Delta**:
  - What changed: SMoCo pretrained a network with MoCo on 612 ADNI amyloid-PET scans (158 MCI converters, 463 non-converters, +443 unlabeled) with a modified contrastive loss pulling future converters together. The proposed method generalizes this to multimodal (adds MRI) and adds longitudinal + site-invariance objectives.
  - Why: SMoCo is modality-specific (PET only) and cannot directly use MRI.
- **Claims affected**: C03, C07
- **Adopted elements**: MoCo negative queue; contrastive pretraining for MCI conversion.

## RW03: Barbano et al., 2024 — AnatCL (anatomical contrastive MRI baseline)
- **DOI**: arXiv:2408.07079; ref [12]
- **Type**: baseline
- **Delta**:
  - What changed: AnatCL is a contrastive method on MRI incorporating anatomical priors (e.g. cortical thickness) for brain-age modeling and disease classification. The proposed method replaces single-modality anatomical priors with cross-modal + longitudinal + site-invariant objectives.
  - Why: to move beyond MRI-only anatomy-aware contrast.
- **Claims affected**: C01, C02, C03, C04
- **Adopted elements**: Contrastive representation learning on structural MRI.

## RW04: Zhang et al., 2023 — Transformer MRI–PET fusion (ISBI'23 baseline)
- **DOI**: 10.1109/ISBI53787.2023 (IEEE ISBI 2023, pp. 1–5); ref [22]
- **Type**: baseline
- **Delta**:
  - What changed: A ViT self-supervised separately on MRI and PET via masked patch prediction, then cross-attention alignment of informative regions. The proposed method adds unified longitudinal, BYOL, and adversarial site-invariance terms and a missing-aware gating fusion.
  - Why: masked-patch + cross-attention alone does not address site shift or longitudinal signal.
- **Claims affected**: C01, C02, C03, C04, C06
- **Adopted elements**: Cross-modal attention/alignment concept; masked-patch pretext.

## RW05: Lew et al., 2023 — MRI-based AT(N) biomarker prediction (Radiology'23 baseline)
- **DOI**: 10.1148/radiol.222441 (Radiology 2023, 309, e222441); ref [10]
- **Type**: baseline
- **Delta**:
  - What changed: A deep network predicting amyloid/tau/neurodegeneration status from MRI. The proposed method predicts the same ATN axes but from an SSL-pretrained multimodal encoder.
  - Why: to compare MRI-only ATN surrogate prediction.
- **Claims affected**: C05
- **Adopted elements**: ATN biomarker-status prediction task definition.

## RW06: Thrasher et al., 2024 — TE-SSL (temporal SSL predecessor)
- **DOI**: arXiv:2407.06852; ref [18]
- **Type**: extends
- **Delta**:
  - What changed: TE-SSL predicts time-to-conversion as a pretext by shuffling MRI time series with an event-occurrence signal, integrating survival into SSL. The proposed longitudinal consistency loss (Eq. 3) captures temporal smoothness without requiring event-time pseudo-labels.
  - Why: TE-SSL blurs self-supervision and weak supervision by needing reliable event-time metadata.
- **Claims affected**: C03, C07
- **Adopted elements**: Longitudinal/temporal signal for prognosis.

## RW07: Ouyang et al., 2024 — SOM2LM (multimodal longitudinal maps)
- **DOI**: 10.1007/978-3-031-72086-4 (MICCAI 2024, LNCS 15002, pp. 400–410); ref [24]
- **Type**: extends
- **Delta**:
  - What changed: SOM2LM builds self-organized MRI and amyloid-PET longitudinal maps (ADNI, 741 subjects) aligned along the disease timeline (PET changes earlier, MRI later), enabling cross-modal prediction and joint prognosis. The proposed method learns cross-modal + longitudinal alignment via contrastive/consistency losses instead of SOMs.
  - Why: SOMs need longitudinal MRI and PET and are limited by synchronous multimodal follow-up availability.
- **Claims affected**: C03, C07
- **Adopted elements**: Cross-modal longitudinal alignment concept; PET-before-MRI temporal ordering intuition.

## RW08: Ouyang et al., 2023 — LSOR (longitudinal SOM MRI)
- **DOI**: 10.1007/978-3-031-43907-0 (MICCAI 2023, LNCS 14220, pp. 279–289); ref [19]
- **Type**: bounds
- **Delta**:
  - What changed: LSOR learns an interpretable 2D SOM embedding stratified by brain age with longitudinal-trajectory consistency (ADNI, 632 subjects). Provides a reference point for interpretable longitudinal SSL that the proposed method aims to match/exceed on pMCI vs sMCI.
  - Why: LSOR requires multiple timepoints per subject and custom stabilization.
- **Claims affected**: C03
- **Adopted elements**: Longitudinal-trajectory consistency principle.

## RW09: Fedorov et al., 2024 — Deep InfoMax multimodal SSL (DIM)
- **DOI**: 10.1016/j.neuroimage.2023.120485 (NeuroImage 2024, 285, 120485); ref [26]
- **Type**: extends
- **Delta**:
  - What changed: DIM maximizes mutual information between paired MRI and rs-fMRI features on OASIS-3, discovering cross-modal links without labels. The proposed method uses cross-modal InfoNCE for MRI–PET and adds missing-modality handling.
  - Why: DIM requires both modalities present per subject and was tested on a single homogeneous dataset (no domain generalization). (Paper misattributes DIM to "Jack et al. 2010 [20]" in §2.2.)
- **Claims affected**: C02, C05, C07
- **Adopted elements**: Cross-modal mutual-information / alignment objective.

## RW10: Wang et al., 2024 — GAN cross-modal synthesis + diagnosis
- **DOI**: 10.1016/j.media.2023.103032 (Med. Image Anal. 2024, 91, 103032); ref [27] (labeled "Zhang et al. 2023" in Table 1)
- **Type**: bounds
- **Delta**:
  - What changed: A cycle-consistent GAN generates missing PET from MRI while diagnosing AD, improving MRI-only classification. The proposed method instead handles missing PET via a gating gate + PET→MRI distillation (Eq. 11) rather than image synthesis.
  - Why: GAN synthesis is unstable and error-prone across sites.
- **Claims affected**: C05, C07
- **Adopted elements**: Missing-modality compensation objective (achieved by distillation, not synthesis).

## RW11: Kaczmarek et al., 2025 — SSL-AD multi-cohort temporal SSL
- **DOI**: arXiv:2509.10453; ref [23]
- **Type**: extends
- **Delta**:
  - What changed: Aggregated four datasets (ADNI, MCSA, HABS, NIFD; >3100 subjects) for temporal SSL with adversarial normalization, learning site-agnostic features. The proposed work adds cross-modal MRI–PET and BYOL terms and evaluates on six cohorts.
  - Why: to combine multi-cohort domain-invariance with cross-modal fusion.
- **Claims affected**: C02, C07
- **Adopted elements**: Multi-cohort aggregation + adversarial normalization for site invariance.

## RW12: Gryshchuk et al., 2025 — Contrastive SSL MRI (SimCLR)
- **DOI**: 10.3389/fninf.2025.1527582 (Front. Neuroinform. 2025, 19, 1527582); ref [13]
- **Type**: baseline
- **Delta**:
  - What changed: Pretrained a ResNet on 2694 MRIs (ADNI/AIBL/FTLDNI) via instance-wise contrastive loss, reaching 82% balanced accuracy AD/CN (80% external). Motivates the intra-modal InfoNCE component and the multi-cohort robustness target.
  - Why: single-timepoint, no longitudinal or multimodal signal.
- **Claims affected**: C01, C02
- **Adopted elements**: Instance-wise contrastive MRI pretraining; multi-cohort saliency evaluation.

## RW13: Caron et al., 2021 — Emerging properties in self-supervised ViTs (DINO)
- **DOI**: 10.1109/ICCV48922.2021 (ICCV 2021, pp. 9630–9640); ref [9]
- **Type**: imports
- **Delta**:
  - What changed: Foundational SSL work motivating representation learning from unlabeled images.
  - Why: grounds the general SSL premise for medical imaging.
- **Claims affected**: C07
- **Adopted elements**: Self-supervised representation-learning paradigm.

## Additional citations (brief — background / clinical / infrastructure / datasets)

- **RW14 — Van Dyck et al., 2023 [2]** (N. Engl. J. Med. 388, 9–21): Lecanemab efficacy in early AD; motivates early diagnosis (background, O1).
- **RW15 — Cummings et al., 2020 [3]** (Alzheimers Dement. TRCI 6, e12050): AD drug pipeline; background on prognosis importance.
- **RW16 — Illakiya et al., 2023 [4]** (Bioengineering 10, 714): AHANet MRI classification; background.
- **RW17 — Lu et al., 2022 [5]** (Front. Aging Neurosci. 14, 826622): two-stage MCI→AD conversion prediction; background.
- **RW18 — Dukart et al., 2011 [7]** (PLoS ONE 6, e18111): combined FDG-PET + MRI improves dementia differentiation; grounds O2 (multimodal benefit).
- **RW19 — Tran et al., 2025 [8]** (BioMedInformatics 5, 20): robustness/generalizability strategies in neuroimaging DL; grounds O3 (site shift).
- **RW20 — Dwivedi et al., 2022 [11]** (IEEE Multimed. 29, 45–55): multimodal fusion DL; source of ADNI sample figures (Figure 2).
- **RW21 — Yan et al., 2019 [16]** (Nucl. Med. Commun. 40, 242–248): amyloid-PET features for MCI conversion; cited re SMoCo loss.
- **RW22 — Khatri & Kwon, 2023 [17]** (Bioengineering 10, 1225): explainable ViT SSL on FDG-PET; unimodal PET SSL background.
- **RW23 — Jack et al., 2010 [20]** (Lancet Neurol. 9, 119–128): dynamic biomarker cascade model (background; misattributed as DIM source in §2.2).
- **RW24 — Kwak et al., 2024 [21]** (medRxiv): cross-modal mutual knowledge distillation for incomplete modalities; related to PET→MRI distillation motivation.
- **RW25 — Kang et al., 2024 [14]** (NeuroImage 297, 120737): disentangled AD atrophy heterogeneity via self-supervised autoencoding; interpretable-latent-space background.
- **RW26 — Gong et al., 2024 [15]** (Biomed. Signal Process. Control 96, 106572): patch-based SSL augmentation (PD-SIM); intra-modal augmentation background.
- **RW27 — Yin et al., 2022 [25]** (IJCNN 2022): SMIL-DeiT self-supervised ViT + MIL (~93% AD/CN); patch-level SSL background.
- **RW28 — Weber et al., 2021 [28]** (Alzheimers Dement. TRCI 7, e12226): ADNI-3 dataset description (data source).
- **RW29 — LaMontagne et al., 2019 [29]** (medRxiv): OASIS-3 dataset (data source).
- **RW30 — Leon-Llamas et al., 2021 [30]** (Int. J. Environ. Res. Public Health 18, 1549): hippocampal subfield MRI study (cited near OASIS-3).
- **RW31 — Rebsamen et al., 2020 [31]** (Hum. Brain Mapp. 41, 4804–4814): DL cortical-thickness estimation (DL+DiReCT); source of Figure 7 processing.
- **RW32 — Fowler et al., 2021 [32]** (J. Alzheimers Dis. Rep. 5, 443–468): AIBL 15-year progress (2359 adults) (data source).
- **RW33 — Ellis et al., 2009 [33]** (Int. Psychogeriatr. 21, 672–687): AIBL baseline methodology (1112 individuals) (data source).
- **RW34 — Binette et al., 2025 [34]** (JAMA Neurol. 82, 666): revised AD biological/clinical staging (BioFINDER context).
- **RW35 — Ossenkoppele et al., 2025 [35]** (Nat. Aging 5, 883–896): plasma p-tau217 + tau-PET predict decline (BioFINDER context).
- **RW36 — Hernandez et al., 2022 [36]** (PLoS ONE 17, e0264695): explainable AI on top-3 TADPOLE methods (benchmark context).
- **RW37 — Marinescu et al., 2021 [37]** (Mach. Learn. Biomed. Imaging 1, 1–60): TADPOLE challenge results (data source / benchmark; 33 teams, 92 algorithms).
- **RW38 — Malone et al., 2013 [38]** (NeuroImage 70, 33–36): MIRIAD public release (data source).
