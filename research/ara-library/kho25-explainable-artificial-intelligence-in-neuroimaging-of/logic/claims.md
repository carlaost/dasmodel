# Claims

> Grounding: abstract-only. The source abstract reports no quantitative empirical findings, confidence intervals, sample sizes, or performance metrics. Claims are therefore qualitative and cite exact abstract phrases in `metadata.md:13`.

## C01: XAI addresses the interpretability barrier in AD neuroimaging AI
- **Statement**: Explainable Artificial Intelligence addresses the challenge that complexity and lack of interpretability limit clinical applicability of AI models for neuroimaging-based Alzheimer's disease diagnosis.
- **Status**: supported
- **Falsification criteria**: Evidence that interpretability is not a meaningful barrier for clinical use of AD neuroimaging AI, or that XAI methods do not provide actionable insight into model decision-making.
- **Proof**: [E01, E03]
- **Evidence basis**: The abstract explicitly names model complexity and lack of interpretability as clinical barriers and states that XAI addresses them.
- **Interpretation**: This is the review's central translational premise; it is not a measured clinical-outcome result in the provided input.
- **Sources**:
  - interpretability barrier ← `metadata.md:13` «However, the complexity and lack of interpretability of these models limit their clinical applicability.» [input]
  - XAI response ← `metadata.md:13` «Explainable Artificial Intelligence (XAI) addresses this challenge by providing insights into model decision-making, enhancing transparency, and fostering trust in AI-driven diagnostics.» [input]
- **Dependencies**: none
- **Tags**: XAI, interpretability, clinical-applicability, AD-neuroimaging

## C02: The review covers four named XAI technique families
- **Statement**: The review highlights SHAP, LIME, Grad-CAM, and Layer-wise Relevance Propagation as key XAI techniques for AD neuroimaging.
- **Status**: supported
- **Falsification criteria**: The full text omits one of these techniques from substantive review coverage or identifies a materially different technique set as central.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly lists the four technique names.
- **Interpretation**: The abstract does not specify comparative strengths, weaknesses, algorithms, or implementation details for these methods.
- **Sources**:
  - technique list ← `metadata.md:13` «highlighting key techniques such as SHAP, LIME, Grad-CAM, and Layer-wise Relevance Propagation (LRP).» [input]
- **Dependencies**: C01
- **Tags**: SHAP, LIME, Grad-CAM, LRP, review-scope

## C03: XAI applications include biomarkers, progression, and AD-stage distinction across MRI and PET
- **Statement**: The review examines XAI applications for identifying critical biomarkers, tracking disease progression, and distinguishing AD stages using MRI and PET neuroimaging.
- **Status**: supported
- **Falsification criteria**: The full text does not cover one or more of these stated application areas or modalities.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract states these application areas and modalities explicitly.
- **Interpretation**: The provided input does not name specific biomarkers, disease stages, datasets, or imaging features.
- **Sources**:
  - applications and modalities ← `metadata.md:13` «We examine their applications in identifying critical biomarkers, tracking disease progression, and distinguishing AD stages using various imaging modalities, including MRI and PET.» [input]
- **Dependencies**: C02
- **Tags**: biomarkers, disease-progression, AD-staging, MRI, PET

## C04: Dataset, regulatory, and standardization issues are current challenges
- **Statement**: Dataset limitations, regulatory concerns, and standardization issues are current challenges for integrating XAI into clinical practice.
- **Status**: supported
- **Falsification criteria**: Evidence that these issues are not treated as challenges in the article or are already resolved for clinical XAI in AD neuroimaging.
- **Proof**: [E02, E03]
- **Evidence basis**: The abstract directly identifies these three challenge categories.
- **Interpretation**: The abstract does not specify exact dataset limitations, regulatory frameworks, or standardization proposals.
- **Sources**:
  - challenge categories ← `metadata.md:13` «Additionally, we discuss current challenges, including dataset limitations, regulatory concerns, and standardization issues...» [input]
- **Dependencies**: C01, C03
- **Tags**: datasets, regulation, standardization, clinical-integration

## C05: XAI may refine diagnostics, personalize treatment, and advance neuroimaging research
- **Statement**: By bridging AI and clinical interpretability, XAI holds potential to refine AD diagnostics, personalize treatment strategies, and advance neuroimaging-based research.
- **Status**: hypothesis
- **Falsification criteria**: Prospective clinical or research evidence showing that XAI explanations do not improve diagnostic refinement, treatment personalization, or neuroimaging research utility compared with non-explainable AI workflows.
- **Proof**: [E03]
- **Evidence basis**: The abstract presents this as a forward-looking potential, not a demonstrated outcome.
- **Interpretation**: This is a future-facing translational claim; concrete intervention designs and outcome measures are Not available from provided input.
- **Sources**:
  - future potential ← `metadata.md:13` «By bridging the gap between AI and clinical interpretability, XAI holds the potential to refine AD diagnostics, personalize treatment strategies, and advance neuroimaging-based research.» [input]
- **Dependencies**: C01, C04
- **Tags**: future-work, diagnostics, personalized-treatment, neuroimaging-research
