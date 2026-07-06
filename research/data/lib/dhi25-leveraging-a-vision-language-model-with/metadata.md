# Leveraging a Vision-Language Model with Natural Text Supervision for MRI Retrieval, Captioning, Classification, and Visual Question Answering

- **Cite key**: Dhi25
- **Authors**: Nikhil J. Dhinagar; S. Thomopoulos; Paul M. Thompson
- **Year**: 2025  (2025-07-01)
- **Journal**: 2025 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)
- **DOI**: 10.1109/EMBC58623.2025.11251809
- **URL**: https://doi.org/10.1109/EMBC58623.2025.11251809
- **Citations**: 2 (2.0/yr)

## Abstract

Large multimodal models are now extensively used worldwide, with the most powerful ones trained on massive, general-purpose datasets. Despite their rapid deployment, concerns persist regarding the quality and domain relevance of the training data, especially in radiology, medical research, and neuroscience. Additionally, healthcare data privacy is paramount when querying models trained on medical data, as is transparency regarding service hosting and data storage. So far, most deep learning algorithms in radiologic research are designed to perform a specific task (e.g., diagnostic classification) and cannot be prompted to perform multiple tasks using natural language. In this work, we introduce a framework based on vector retrieval and contrastive learning to efficiently learn visual brain MRI concepts via natural language supervision. We show how the method learns to identify factors that affect the brain in Alzheimer’s disease (AD) via joint embedding and natural language supervision. First, we pretrain separate text and image encoders using self-supervised learning, and jointly fine-tune these encoders to develop a shared embedding space. We train our model to perform multiple tasks, including MRI retrieval, MRI captioning, and MRI classification. We show its versatility by developing a retrieval and re-ranking mechanism along with a transformer decoder for visual question answering. Clinical Relevance - By learning a cross-modal embedding of radiologic features and text, our approach can learn to perform diagnostic and prognostic assessments in AD research as well as to assist practicing clinicians. Integrating medical imaging with clinical descriptions and text prompts, we aim to provide a general, versatile tool for detecting radiologic features described by text, offering a new approach to radiologic research.
