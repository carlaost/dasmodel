# Claims

> Grounding: abstract-only. The abstract reports no model accuracies, sample sizes, dataset counts, table values, or figure evidence. Claims therefore stay qualitative except for explicit metadata values and the review window. Every load-bearing number is tied to a verbatim source quote.

## C01: The review focuses on recent MRI/PET deep learning multimodal fusion work for AD
- **Statement**: This 2025 review systematically surveys deep learning-based multimodal fusion of MRI and PET images for Alzheimer's disease research, with a particular focus on studies published in 2021-2025.
- **Status**: supported
- **Falsification criteria**: The full text shows that the review is not about deep learning-based MRI/PET fusion for AD, or that it does not focus on the 2021-2025 publication window.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly states the topic, modalities, disease area, and publication window.
- **Interpretation**: The paper is best represented as a field review rather than as a primary empirical study.
- **Sources**:
  - 2025 ← `metadata.md:5` «- **Year**: 2025  (2025-04-01)» [input]
  - 2021-2025 ← `metadata.md:13` «with a particular focus on studies published in the past five years (2021-2025)» [input]
- **Dependencies**: none
- **Tags**: review, multimodal fusion, MRI, PET, Alzheimer's disease, deep learning

## C02: MRI and PET are complementary for AD diagnosis and research
- **Statement**: The abstract claims that combined MRI and PET use offers complementary structural and metabolic information for comprehensive Alzheimer's disease understanding and precise diagnosis.
- **Status**: supported
- **Falsification criteria**: Evidence from the full text shows the authors do not treat MRI and PET as complementary, or that the review does not use complementarity as a rationale for multimodal fusion.
- **Proof**: [E02]
- **Evidence basis**: The abstract explicitly names MRI and PET and states the structural/metabolic complementarity rationale.
- **Interpretation**: Fusion is motivated by different information types rather than by modality redundancy.
- **Sources**:
  - "structural and metabolic information" ← `metadata.md:13` «The complementarity of these modalities in structural and metabolic information offers a unique advantage for comprehensive disease understanding and precise diagnosis.» [input]
- **Dependencies**: none
- **Tags**: MRI, PET, modality complementarity, diagnosis

## C03: The review covers the main technical pipeline and model families for MRI/PET fusion
- **Statement**: The abstract states that the review introduces AD-related data sources, preprocessing, feature extraction, performance metrics, multimodal fusion techniques, and deep learning models and variants.
- **Status**: supported
- **Falsification criteria**: The full text omits one or more of these stated review components, or the components are only mentioned in the abstract without substantive review content.
- **Proof**: [E01, E03]
- **Evidence basis**: The abstract lists the review components directly.
- **Interpretation**: The paper aims to be a structured survey across data, processing, evaluation, fusion, and model-design layers.
- **Sources**:
  - "data preprocessing and feature extraction methods" ← `metadata.md:13` «It first introduces the main sources of AD-related data, along with data preprocessing and feature extraction methods.» [input]
  - "performance metrics and multimodal fusion techniques" ← `metadata.md:13` «Then it summarizes performance metrics and multimodal fusion techniques.» [input]
  - "deep learning models and their variants" ← `metadata.md:13` «Next, it explores the application of various deep learning models and their variants in multimodal fusion tasks.» [input]
- **Dependencies**: C01
- **Tags**: review taxonomy, preprocessing, feature extraction, performance metrics, model variants

## C04: The review identifies data scarcity, imbalance, and inter-institutional heterogeneity as key field challenges
- **Statement**: The abstract identifies data scarcity, data imbalance, and inter-institutional data heterogeneity as key challenges for deep learning-based MRI/PET multimodal fusion in AD research.
- **Status**: supported
- **Falsification criteria**: The full text does not discuss these as key challenges, or replaces them with a different challenge set not captured by the abstract.
- **Proof**: [E04]
- **Evidence basis**: The abstract lists these challenges explicitly.
- **Interpretation**: The field's limiting factors are not only algorithmic; data availability, class balance, and cross-site distribution shift are central concerns.
- **Sources**:
  - "data scarcity and imbalance, inter-institutional data heterogeneity" ← `metadata.md:13` «including data scarcity and imbalance, inter-institutional data heterogeneity, etc.» [input]
- **Dependencies**: C01, C03
- **Tags**: data scarcity, class imbalance, heterogeneity, generalization, future work
