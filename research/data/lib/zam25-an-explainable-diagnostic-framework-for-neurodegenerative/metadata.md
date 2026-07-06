# An Explainable Diagnostic Framework for Neurodegenerative Dementias via Reinforcement-Optimized LLM Reasoning

- **Cite key**: Zam25
- **Authors**: Andrew Zamai; Nathanaël Fijalkow; Boris Mansencal; Laurent Simon; Eloi Navet; Pierrick Coupé
- **Year**: 2025  (2025-05-26)
- **Journal**: ArXiv
- **DOI**: 10.48550/arXiv.2505.19954
- **URL**: https://doi.org/10.48550/arXiv.2505.19954
- **Citations**: 2 (1.8/yr)

## Abstract

The differential diagnosis of neurodegenerative dementias is a challenging clinical task, mainly because of the overlap in symptom presentation and the similarity of patterns observed in structural neuroimaging. To improve diagnostic efficiency and accuracy, deep learning-based methods such as Convolutional Neural Networks and Vision Transformers have been proposed for the automatic classification of brain MRIs. However, despite their strong predictive performance, these models find limited clinical utility due to their opaque decision making. In this work, we propose a framework that integrates two core components to enhance diagnostic transparency. First, we introduce a modular pipeline for converting 3D T1-weighted brain MRIs into textual radiology reports. Second, we explore the potential of modern Large Language Models (LLMs) to assist clinicians in the differential diagnosis between Frontotemporal dementia subtypes, Alzheimer's disease, and normal aging based on the generated reports. To bridge the gap between predictive accuracy and explainability, we employ reinforcement learning to incentivize diagnostic reasoning in LLMs. Without requiring supervised reasoning traces or distillation from larger models, our approach enables the emergence of structured diagnostic rationales grounded in neuroimaging findings. Unlike post-hoc explainability methods that retrospectively justify model decisions, our framework generates diagnostic rationales as part of the inference process-producing causally grounded explanations that inform and guide the model's decision-making process. In doing so, our framework matches the diagnostic performance of existing deep learning methods while offering rationales that support its diagnostic conclusions.
