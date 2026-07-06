# Problem Specification

> Grounding: abstract-only. Source references cite `metadata.md` lines 11-13 and `metadata.json` lines 4-13. No full text was available.

## Observations

### O01: AD is a major clinical and health-system burden
- **Statement**: Alzheimer's disease is described as a significant global health challenge that affects millions and imposes substantial burdens on healthcare systems.
- **Evidence**: `metadata.md:13` "Alzheimer's disease (AD) remains a significant global health challenge..."
- **Implication**: Diagnostic improvement in AD is clinically meaningful, but the abstract provides no burden statistics.

### O02: AI has changed neuroimaging-based AD diagnosis
- **Statement**: The abstract states that advances in AI, especially deep learning and machine learning, have revolutionized neuroimaging-based AD diagnosis.
- **Evidence**: `metadata.md:13` "Advances in artificial intelligence (AI), particularly in deep learning and machine learning..."
- **Implication**: The review is situated around AI-assisted interpretation of neuroimaging rather than non-imaging biomarkers or purely clinical diagnosis.

### O03: Model complexity and low interpretability limit clinical applicability
- **Statement**: Complex and poorly interpretable models limit clinical applicability.
- **Evidence**: `metadata.md:13` "However, the complexity and lack of interpretability of these models limit their clinical applicability."
- **Implication**: Interpretability is treated as a translational bottleneck, not merely a technical preference.

### O04: XAI is positioned as the response to the interpretability bottleneck
- **Statement**: XAI provides insights into model decision-making, enhances transparency, and fosters trust in AI-driven diagnostics.
- **Evidence**: `metadata.md:13` "Explainable Artificial Intelligence (XAI) addresses this challenge..."
- **Implication**: The paper's organizing insight is that explanation methods can bridge technical AI performance and clinical interpretability.

## Gaps

### G01: Clinical interpretability gap
- **Statement**: AI models for AD neuroimaging can be powerful but insufficiently interpretable for clinical application.
- **Caused by**: O02, O03
- **Existing attempts**: Deep learning and machine learning for neuroimaging-based AD diagnosis.
- **Why they fail**: The abstract only states complexity and lack of interpretability; detailed failure modes are Not available from provided input.

### G02: Integration gap for clinical practice
- **Statement**: XAI integration into clinical practice remains incomplete.
- **Caused by**: O03, O04
- **Existing attempts**: Use of named XAI techniques such as SHAP, LIME, Grad-CAM, and LRP.
- **Why they fail**: Dataset limitations, regulatory concerns, and standardization issues are named as current challenges; details are Not available from provided input.

## Key Insight

- **Insight**: XAI can bridge AI model decision-making and clinical interpretability in AD neuroimaging by making diagnostic model behavior more transparent.
- **Derived from**: O03, O04
- **Enables**: A review organized around XAI techniques, imaging modalities, AD-relevant applications, challenges, and future directions for clinical integration.

## Assumptions

- A1: Neuroimaging-based AD diagnosis uses AI models whose decisions require explanation for clinical adoption.
- A2: Named XAI techniques can be meaningfully applied to AD neuroimaging workflows.
- A3: The abstract's terms "MRI and PET" indicate review coverage of those modalities, but specific datasets, scanners, cohorts, and preprocessing pipelines are Not available from provided input.
