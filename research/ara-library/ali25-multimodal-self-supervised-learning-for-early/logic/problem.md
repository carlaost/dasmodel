# Problem Specification

## Observations

### O1: Early AD detection is clinically decisive but disease-modifying therapy only helps early
- **Statement**: In 2023 an estimated 6.7 million Americans aged 65+ were living with AD, projected to more than double by 2060; the first disease-modifying anti-amyloid antibodies show "modest slowing of cognitive decline only when administered in early stages of AD."
- **Evidence**: §1, refs [1,2]. About 10–15% of MCI individuals progress to AD each year.
- **Implication**: Early diagnosis at the MCI stage and accurate MCI→AD prognosis are critically important for timely intervention and trial enrollment.

### O2: MRI and PET carry complementary but non-overlapping AD signal
- **Statement**: Structural MRI reveals atrophy (hippocampal/cortical) that appears later, while PET captures earlier functional/molecular pathology (FDG hypometabolism, amyloid burden). Joint MRI+FDG-PET evaluation differentiates AD from other dementias better than either modality alone (Dukart et al.).
- **Evidence**: §1, refs [5,6,7].
- **Implication**: Multimodal integration can raise diagnostic accuracy over unimodal analysis.

### O3: Multi-site variability degrades model generalization
- **Statement**: Large AD cohorts are collected across sites with varying scanners, protocols, and demographics, causing distribution shifts; models "may be overfit to site-specific artifacts or scanner effects, leading to reduced reliability on external data."
- **Evidence**: §1, ref [8].
- **Implication**: Site/domain invariance is required for cross-cohort deployment.

### O4: Prior SSL in AD is fragmented across single modality or single consistency aspect
- **Statement**: SMoCo used contrastive pretraining on 3D amyloid PET only; AnatCL used anatomical-prior contrastive learning on MRI only; DiaMond fused MRI+PET with a bi-attention ViT but without longitudinal or explicit site-invariance objectives. "No prior work has unified all the following elements in one framework: cross-modal MRI–PET learning, longitudinal consistency across patient timepoints, and explicit site/domain-invariance."
- **Evidence**: §1, §2, refs [1,6,10,12].
- **Implication**: A unified objective set is the stated novelty.

### O5: Missing modalities and longitudinal follow-ups complicate integration
- **Statement**: PET (or fMRI) is frequently missing for some subjects (e.g. OASIS-3 has mostly single-timepoint PET); prior DIM-based multimodal SSL requires both modalities present per subject.
- **Evidence**: §1, §2.2, ref [20,26].
- **Implication**: A model must tolerate missing modalities and exploit longitudinal signals where available.

## Gaps

### G1: No single SSL framework unifies cross-modal, longitudinal, and site-invariant learning
- **Statement**: Existing SSL AD methods each address one axis (modality fusion, temporal ordering, or domain shift) but none combine all three.
- **Caused by**: O2, O3, O4.
- **Existing attempts**: SMoCo (PET-only contrastive), AnatCL (MRI anatomical contrastive), TE-SSL (temporal-only MRI), DIM/Fedorov (MRI+fMRI mutual information), DiaMond (MRI+PET ViT fusion), SSL-AD/Kaczmarek (multi-cohort temporal SSL).
- **Why they fail**: Modality-specific methods "cannot directly use MRI data" or PET data; single-cohort methods do not test domain generalization; longitudinal methods require reliable event-time metadata.

### G2: Real-world cohort diversity (missing PET, heterogeneous protocols) breaks fusion models
- **Statement**: Fusion models that assume both modalities and homogeneous acquisition fail on cohorts with missing PET or scanner shift.
- **Caused by**: O3, O5.
- **Existing attempts**: GAN-based cross-modal synthesis (Wang et al.), DIM.
- **Why they fail**: GAN synthesis is unstable and error-prone across sites; DIM requires both modalities present.

### G3: Longitudinal atrophy measurement instability limits early monitoring
- **Statement**: Detecting minimal structural change over short intervals is confounded by measurement noise; test–retest reliability is under-reported for SSL AD models.
- **Caused by**: O1, O5.
- **Existing attempts**: LSOR, SOM2LM interpretable longitudinal maps.
- **Why they fail**: They require multiple timepoints per subject and are not benchmarked for scan–rescan reliability across cohorts.

## Key Insight
- **Insight**: A single 3D-CNN/transformer encoder pair can be pretrained with a *weighted sum of five complementary self-supervised objectives* — intra-modal InfoNCE, cross-modal MRI↔PET InfoNCE, longitudinal consistency, BYOL stabilization, and a domain-adversarial site-invariance term — so that the learned representation is simultaneously modality-aligned, temporally smooth, and site-agnostic; downstream multi-task fine-tuning with missing-aware gating fusion and PET→MRI distillation then transfers this representation to diagnosis, prognosis, and biomarker estimation.
- **Derived from**: O2, O3, O4, O5.
- **Enables**: State-of-the-art in-distribution accuracy, cross-cohort transfer, longitudinal reliability, and MRI-only deployability when PET is absent.

## Assumptions
- A1: Co-registered MRI–PET pairs at the same visit constitute valid cross-modal positives.
- A2: Two augmented views of the same scan, and different visits of the same subject, are valid positives (intra-modal and longitudinal).
- A3: Site/scanner labels contain removable non-biological variance; adversarial removal preserves disease-relevant signal.
- A4: A missing modality at training time can be partially compensated via distillation from the available modality.
- A5: Subject-level (not scan-level) train/val/test splits prevent temporal leakage across folds.
- A6: Reported baseline numbers reflect "each method's reported protocols and metrics whenever available" (§5), i.e. baselines are re-tabulated, not necessarily re-run under identical conditions.
