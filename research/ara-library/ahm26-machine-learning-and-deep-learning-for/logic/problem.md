# Problem Specification

Domain: computational (machine-learning / deep-learning) diagnosis of Alzheimer's disease (AD)
from neuroimaging and multimodal clinical data. This is a survey; the "problem" below is the
field-level problem the survey synthesizes, not an experiment the authors run.

## Observations

### O1: AD is the leading cause of dementia and hard to detect early
- **Statement**: Alzheimer's disease is the most common cause of dementia; early-stage AD is
  difficult to detect because mild cognitive impairment (MCI) and early AD show subtle and
  overlapping patterns that also overlap with normal aging and other dementias.
- **Evidence**: Introduction (PDF p.623); Background (p.624).
- **Implication**: Motivates computational tools that surface hidden/distributed patterns not
  captured by manual inspection alone.

### O2: MRI and PET carry complementary information
- **Statement**: Structural MRI captures anatomical degeneration (hippocampal atrophy, cortical
  thinning, ventricular enlargement, gray-matter loss); PET (FDG-PET for glucose metabolism, amyloid
  PET for Aβ burden) captures functional/molecular processes that may precede structural change.
  Influential studies show MRI and PET are complementary, not redundant.
- **Evidence**: "Datasets and Input Modalities" (p.625-626); Figures 1, 3.
- **Implication**: Multimodal learning becomes a dominant methodological trend.

### O3: The field moved from handcrafted features to end-to-end deep models
- **Statement**: Research has progressed from traditional ML with handcrafted features (SVM, random
  forest, logistic regression, boosting) to CNNs, multimodal fusion, transformer-equipped, and
  graph-based models that learn representations directly from data.
- **Evidence**: Taxonomy of Methods (p.629-633); Figures 4, 5.
- **Implication**: Establishes the survey's five-group taxonomy and the "evolution" narrative.

### O4: Evaluation across studies is highly heterogeneous
- **Statement**: Studies differ in datasets, diagnostic tasks (AD vs CN, MCI, progression, multi-class
  staging), train/test splits, cross-validation, preprocessing, and inclusion criteria, so accuracy,
  sensitivity, specificity, and AUC cannot be directly compared across papers.
- **Evidence**: Background (p.624-625); "Why accuracy alone is not enough" (p.640-641).
- **Implication**: Reported performance can reflect easier tasks or curated data rather than a
  genuinely superior model.

### O5: The field depends heavily on a few public benchmarks
- **Statement**: Most studies are developed and evaluated primarily on ADNI, with OASIS/OASIS-3 and
  AIBL beginning to broaden the landscape; heavy single-benchmark reliance limits confidence in
  real-world generalization.
- **Evidence**: Background (p.625); "Reproducibility and generalizability" (p.641-642); Figure 1.
- **Implication**: Success on a curated benchmark does not imply readiness for clinical deployment.

### O6: Explainability is commonly presented but rarely rigorously evaluated
- **Statement**: Many studies include one or two Grad-CAM/SHAP/attention/saliency visualizations as
  evidence of interpretability, but seldom assess whether explanations are stable, reproducible,
  clinically plausible, or consistent across cohorts.
- **Evidence**: "Explainable AI" (p.633-635); "Explainability and trust" (p.642-643); Figures 7,
  unnumbered attention/Grad-CAM figures.
- **Implication**: Visual explanation alone does not guarantee trustworthy reasoning.

## Gaps

### G1: No standardized, comparable evaluation across the literature
- **Statement**: There is no shared evaluation protocol; heterogeneous tasks/datasets make
  cross-study numerical comparison unreliable.
- **Caused by**: O4, O5.
- **Existing attempts**: Individual studies report internal accuracy/AUC; a few (Qiu et al. 2022)
  add external validation.
- **Why they fail**: Different tasks and curated benchmarks inflate/deflate numbers incomparably.

### G2: Weak external validation and generalizability
- **Statement**: Cross-site, cross-scanner, cross-population validation is uncommon, so models may
  fail under domain shift.
- **Caused by**: O5.
- **Existing attempts**: Qiu et al. (2022) multi-cohort external validation; Castellano et al. (2024)
  adds OASIS-3.
- **Why they fail**: Routine multi-center validation remains rare across the field.

### G3: Interpretability lacks rigorous, standardized evaluation
- **Statement**: Explanation quality is not systematically measured or validated with domain experts.
- **Caused by**: O6.
- **Existing attempts**: Post hoc methods (Grad-CAM, SHAP, saliency); emerging self-explainable GNNs.
- **Why they fail**: Post hoc explanations can appear convincing even when the model relies on
  spurious/confounding signals.

### G4: Gap between benchmark performance and clinical deployment
- **Statement**: High experimental performance does not translate to routine care unless models
  handle missing modalities, scanner variation, uncertainty, and heterogeneous populations.
- **Caused by**: O4, O5, G1, G2, G3.
- **Existing attempts**: Multimodal and clinically-oriented frameworks (Qiu et al. 2022).
- **Why they fail**: Class imbalance, missing-modality handling, and reproducibility remain weak.

## Key Insight
- **Insight**: Progress in AD diagnosis should be judged not by headline accuracy but by robustness,
  generalizability, interpretability, reproducibility, and clinical relevance; multimodal integration
  and architecture-level explainability are the most clinically promising directions, while
  transformers and GNNs remain promising-but-unsettled relative to strong multimodal CNN baselines.
- **Derived from**: O2, O3, O4, O5, O6.
- **Enables**: A taxonomy-driven, critically-appraised organization of the literature and a future
  roadmap (external validation, robust multimodal fusion, longitudinal/prognostic modeling, rigorous
  explainability, reproducible open benchmarking).

## Assumptions
- A1: A curated set of ~10-15 representative studies (8 named) adequately captures the field's main
  methodological directions (narrative-survey assumption, stated explicitly).
- A2: Methodological contribution and clinical relevance are more informative organizing axes than
  reported accuracy.
- A3: Public benchmark cohorts (ADNI, OASIS-3, AIBL) are representative enough of the field's data
  practices to ground the discussion.
