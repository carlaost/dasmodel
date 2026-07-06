# ADFound: A Foundation Model for Diagnosis and Prognosis of Alzheimer's Disease

- **Cite key**: Yan25
- **Authors**: Guangqian Yang; Kangrui Du; Zhihan Kelvin Yang; Ye Du; E. Cheung; Yongping Zheng; Mo Yang; Zoe Kourtzi; C. Schönlieb; Shujun Wang
- **Year**: 2025  (2025-06-03)
- **Journal**: IEEE journal of biomedical and health informatics
- **DOI**: 10.1109/JBHI.2025.3576436
- **URL**: https://doi.org/10.1109/JBHI.2025.3576436
- **Citations**: 6 (5.5/yr)

## Abstract

Alzheimer's disease (AD) is an incurable neurodegenerative disorder characterized by progressive cognitive and functional decline. Consequently, early diagnosis and accurate prediction of disease progression are of paramount importance and inherently complex, necessitating the integration of multi-modal data. However, most existing methods are task-specific models that lack generalization ability, addressing only one task at a time and failing to simultaneously assess disease diagnosis and progression. In this paper, we introduce ADFound, the first foundation model for AD that serves as a basis for various downstream tasks, such as diagnosis and prognosis, with high generalization capability. ADFound leverages a substantial amount of unlabeled 3D multi-modal neuroimaging, including paired and unpaired data, to achieve its objectives. Specifically, ADFound is developed upon the Multi-modal Vim encoder by Vision Mamba block to capture long-range dependencies inherent in 3D multi-modal medical images. To efficiently pre-train ADFound on unlabeled paired and upaired multi-modal neuroimaging data, we proposed a novel self-supervised learning framework that integrates multi-modal masked autoencoder (MAE) and contrastive learning. The multi-modal MAE aims to learn local relations among modalities by reconstructing images with unmasked image patches. Additionally, we introduce a Dual Contrastive Learning for Multi-modal Data to enhance the discriminative capabilities of multi-modal representations from intra-modal and inter-modal perspectives. Our experiments demonstrate that ADFound outperforms stateof-the-art methods across a wide range of downstream tasks relevant to the diagnosis and prognosis of AD. Furthermore, the results indicate that our foundation model can be extended to more modalities, such as non-image data, showing its versatility. The code is available at https: //github.com/guangqianyang/ADFound.git.
