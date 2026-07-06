# Problem Specification

> Grounding: abstract-only. Observations and gaps are drawn from the paper's abstract
> (`metadata.json` / `metadata.md`) and the verified dataset record (`sources.yaml`). No full
> text was available (the provided PDF is a different paper — see PAPER.md grounding note).

## Observations

### O1: AD is a progressive neurodegenerative disease requiring accurate, early detection
- **Statement**: Alzheimer's disease is "a progressive neurodegenerative condition marked by cognitive decline and memory loss"; the work targets AD severity classification to support "early and accurate Alzheimer's disease detection".
- **Evidence**: Abstract (Background; Conclusion).
- **Implication**: There is clinical demand for reliable automated AD assessment tools.

### O2: AI neuroimaging analysis exists but clinical deployment is limited
- **Statement**: "Despite advancements in AI-driven neuroimaging analysis for AD detection, clinical deployment remains limited due to challenges in model interpretability and usability."
- **Evidence**: Abstract (Background).
- **Implication**: Accuracy alone is insufficient; interpretability and usability gate real-world adoption.

### O3: A large, class-labelled 2D MRI dataset is publicly available
- **Statement**: An augmented Kaggle dataset of 33,984 images spanning four AD severity classes (plus 6,400 original source images) is available and open-access.
- **Evidence**: Abstract ("augmented Kaggle dataset (33,984 images across four AD severity classes)"); `sources.yaml` (verified Kaggle dataset uraninjo, 33,984 augmented + 6,400 original, classes MildDemented / ModerateDemented / NonDemented / VeryMildDemented).
- **Implication**: Supervised severity classification from 2D slices is feasible without collecting a new cohort.

### O4: Explainable-AI methods such as XRAI can produce region-based visual explanations
- **Statement**: "Explainable AI (XAI) frameworks such as XRAI offer potential to bridge this gap by providing clinically meaningful visualizations of model decision-making."
- **Evidence**: Abstract (Background).
- **Implication**: Region-based attribution offers a route to clinician-facing interpretability.

## Gaps

### G1: Lack of interpretable, deployable AD-classification systems
- **Statement**: High-performing AD models are not being deployed clinically because they lack interpretability and a usable clinical interface.
- **Caused by**: O2.
- **Existing attempts**: AI-driven neuroimaging analysis for AD detection (referenced generically in the abstract).
- **Why they fail**: Interpretability and usability challenges (per abstract); specific failure modes not available from provided input (no full text).

### G2: XRAI had not been systematically integrated into MRI-based AD severity classification
- **Statement**: Prior work had not systematically applied XRAI region-based attribution to AD severity classification on MRI + deep learning.
- **Caused by**: O2, O4.
- **Existing attempts**: Not available from provided input (no full text).
- **Why they fail**: The paper positions itself as "the first systematic integration of XRAI into AD severity classification using MRI and deep learning."

### G3: Efficiency vs. accuracy trade-off for clinical use
- **Statement**: Clinical deployment needs models that are both accurate and computationally light enough for real-time use, but this trade-off is under-addressed.
- **Caused by**: O2.
- **Existing attempts**: Comparison of three architectures of differing size (MobileNet-V3 Large, EfficientNet-B4, ResNet-50).
- **Why they fail**: Not available from provided input (no full text); addressed here by favouring the lowest-parameter model (4.2M).

## Key Insight
- **Insight**: Pairing a lightweight, high-accuracy CNN (MobileNet-V3 Large) with XRAI region-based explanations and a Gradio web interface yields an AD-severity classifier that is simultaneously accurate, efficient, interpretable, and clinically deployable.
- **Derived from**: O2, O3, O4.
- **Enables**: A practical, real-time, explainable clinical diagnostic workflow (sub-20-second inference).

## Assumptions
- A1: 2D brain MRI slices carry sufficient signal to classify AD severity into four classes.
- A2: The augmented Kaggle dataset is representative enough that accuracy on it transfers to the original (non-augmented) data and, by extension, to clinical use.
- A3: XRAI region-based attribution maps are clinically meaningful when they overlap known AD-associated neuroanatomy.
- A4: Sub-20-second inference on the deployment hardware is fast enough for real-world diagnostic workflows.
