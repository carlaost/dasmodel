# PRA-PoE: Robust Multimodal Alzheimer's Diagnosis with Arbitrary Missing Modalities

- **Cite key**: Yan26e
- **Authors**: Guangqian Yang; Ye Du; Wenlong Hou; Qianli Niu; Shujun Wang
- **Year**: 2026  (2026-05-13)
- **Journal**: 
- **DOI**: 
- **URL**: https://arxiv.org/abs/2605.13081
- **Citations**: 0 (0.0/yr)

## Abstract

Missing modalities are prevalent in real-world Alzheimer's disease (AD) assessment and pose a significant challenge to multimodal learning, particularly when the distribution of observed modality subsets differs between training and deployment. Such missingness pattern mismatch induces a conditional representation shift across modality subsets. Existing approaches that rely on implicit imputation or modality synthesis often fail to explicitly model modality availability and uncertainty, leading to overconfident dependence on synthesized features, reduced robustness, and miscalibrated uncertainty estimates. To address these limitations, we propose PRA-PoE, an incomplete multimodal learning framework that is equipped with Prototype-anchored Representation Alignment (PRA) and an Uncertainty-aware Product of Experts (UA-PoE) fusion mechanism. First, PRA uses learnable global prototypes and availability-conditioned tokens to encode modality availability, distinguish observed from missing modalities, re-synthesize features for missing modalities, and adaptively refine observed representations to align latent spaces across modality subsets, with the goal of reducing representation shift under varying missingness patterns. Second, UA-PoE models each modality as a Gaussian expert and performs closed-form Product of Experts fusion, where experts with higher uncertainty are automatically down-weighted via lower precision, improving uncertainty reliability. We evaluate PRA-PoE under a clinically realistic protocol by training with naturally missing data and testing on all non-empty modality combinations. PRA-PoE consistently outperforms the state-of-the-art across datasets, achieving a 5.4% relative improvement in average accuracy on ADNI and a 10.9% relative gain in average F1 on OASIS-3 over the strongest baseline across all non-empty modality subsets.
