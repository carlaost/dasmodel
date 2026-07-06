# Longitudinal Graph Neural Networks for Prognostic Modeling of Alzheimer’s Disease Progression

- **Cite key**: Ash26
- **Authors**: M. Ashimgaliyev; A. Zhumadillayeva; Miras Mussabek; Peiwu Qin
- **Year**: 2026  (2026-03-20)
- **Journal**: 2026 International Conference on Advances in Artificial Intelligence and Machine Learning (AAIML)
- **DOI**: 10.1109/AAIML67890.2026.11498183
- **URL**: https://doi.org/10.1109/AAIML67890.2026.11498183
- **Citations**: 0 (0.0/yr)

## Abstract

Accurately predicting how Alzheimer’s disease progresses from mild cognitive impairment (MCI) remains a major challenge, requiring models capable of capturing subtle, time-dependent changes in brain structure and function. Many existing prognostic methods rely on a single imaging modality or fail to explicitly model changes across multiple assessments, which limits their ability to reflect the complex, evolving nature of neurodegeneration. To address this, we propose a longitudinal graph neural network framework that integrates structural MRI and FDG-PET imaging with follow-up scans to better model disease progression. In this approach, convolutional neural networks are first used to extract region-level image features, which serve as node attributes in a spatiotemporal brain graph. Each node represents an anatomically defined brain region, with edges encoding structural relationships between regions and temporal links connecting the same region across successive timepoints. A graph neural network equipped with edge-wise temporal attention then propagates information through this structure, enabling the model to learn both spatial dependencies and longitudinal patterns of change. We evaluated the method on longitudinal imaging and clinical data from the Alzheimer’s Disease Neuroimaging Initiative, where it consistently outperformed standard convolutional and recurrent neural network baselines, delivering more accurate predictions of MCI-to-AD conversion. Additionally, interpretability analysis identified key prognostic biomarkers, with regions such as the hippocampus and entorhinal cortex emerging as particularly influential in predicting disease progression. These results demonstrate that incorporating longitudinal imaging into a graphbased learning framework can significantly improve prognostic accuracy while providing clinically meaningful insights into the progression of Alzheimer’s disease.
