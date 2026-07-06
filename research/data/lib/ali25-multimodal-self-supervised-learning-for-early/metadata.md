# Multimodal Self-Supervised Learning for Early Alzheimer’s: Cross-Modal MRI–PET, Longitudinal Signals, and Site Invariance

- **Cite key**: Ali25
- **Authors**: Soumaya Belhaj Ali; Naglaa E. Ghannam; H. Mancy; Basma Gh. Elkilany
- **Year**: 2025  (2025-12-01)
- **Journal**: Diagnostics
- **DOI**: 10.3390/diagnostics15243135
- **URL**: https://doi.org/10.3390/diagnostics15243135
- **Citations**: 3 (5.1/yr)

## Abstract

Background: The early and accurate identification of Alzheimer’s disease (AD) is complicated by a number of factors, such as the diversity of imaging modalities, variability in scanners across multiple sites, and the long-term progression of neurodegeneration. Such modest gains and the range of diagnostic scenarios suggest that robust multimodal applications, which incorporate both structural, molecular, and longitudinal measurements, are required if realistic benefits are to be seen in actual clinical settings. Methods: We introduce a multimodal self-supervised learning (SSL) approach, which learns feature representations of MRI and PET jointly using the cross-modal alignment, longitudinal temporal consistency, and domain-invariant embedding optimization. The approach integrates contrastive learning, scanner harmonization strategies, and missing modality-aware fusion for handling real-world cohort diversity. Six widely used datasets were evaluated, which are made publicly available: ADNI, OASIS-3, AIBL, BioFINDER, TADPOLE, and MIRIAD. Results: The model performed in a state-of-the-art way on all benchmark tasks. On ADNI, it obtained a BACC of 93.0% and an AUC of 0.96 for the binary classification task (AD vs. CN), surpassing recent baselines such as DiaMond’25, SMoCo, and AnatCL with statistically significant performance gain. Strong cross-cohort generalizability was reported (78.0% BACC on OASIS-3 and 77.5% BACC on AIBL). For TADPOLE, for longitudinal prognosis (i.e., MCI → AD conversion), the model yielded an AUC of 0.85 and a C-index of 0.82, which shows better ascendency over previous SSL-based methods. High test–retest consistency was observed on MIRIAD (ICC = 0.91), indicating that instability in volume measurement due to atrophy progression was minimal. Conclusions: The proposed multimodal SSL framework offers effective transferable and domain-robust biomarkers for the early diagnosis of AD and prediction of MCI-to-AD progression. It has strong cross-dataset generalization.

## Discovered sources

- **IDs**: PMID 41464136 · PMCID PMC12732103 · DOI 10.3390/diagnostics15243135
- **PDF**: Open Access (Gold, CC-BY). Downloaded to `paper.pdf` (24 pages, verified `%PDF`). MDPI and PMC direct PDF endpoints were Cloudflare-blocked (returned HTML); the identical OA PDF was retrieved from the Semantic Scholar mirror. Best publisher URL: https://www.mdpi.com/2075-4418/15/24/3135/pdf
- **Code**: None found. The authors state they "release" site-stratified 5-fold CV split files, seeds, and preprocessing versions for reproducibility, but no GitHub/GitLab/Zenodo/OSF/Bitbucket URL appears in the article, the Data Availability Statement, or supplementary material, and a web search returned none. No code artifact could be verified.
- **Data**: Six public secondary-use neuroimaging cohorts, all registration/DUA-gated (access: request) — ADNI, OASIS-3, AIBL, BioFINDER, TADPOLE (ADNI-derived challenge), MIRIAD. The Data Availability Statement only cites these datasets by reference ("openly available in [27–37]"); no new dataset/accession was released.
- **Clinical trials**: None. This is a methods/ML study on existing public cohorts — no interventional trial, NCT id, or PROSPERO registration.
- **Funding**: Prince Sattam Bin Abdulaziz University (PSAU/2025/03/33734).
