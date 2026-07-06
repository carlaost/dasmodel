# Claims

These are **synthesis claims**: conclusions the survey draws from the body of literature it reviews,
not results of experiments the authors ran. Status `supported` means "supported by the survey's
synthesis of the cited studies." Load-bearing numbers carry a `**Sources**` entry with a verbatim
quote from the full-text PDF; qualitative claims cite the section they are drawn from.

## C01: Multimodal systems often outperform single-modality systems
- **Statement**: Across the surveyed literature, multimodal systems (especially structural MRI + PET,
  optionally with clinical/cognitive/biomarker variables) often outperform single-modality systems
  because MRI and PET encode complementary structural and metabolic information.
- **Status**: supported
- **Falsification criteria**: A systematic body of head-to-head evaluations showing multimodal
  fusion provides no consistent advantage over well-designed single-modality baselines under matched
  tasks/datasets would refute this.
- **Proof**: [E01, E05]
- **Evidence basis**: The survey repeatedly states MRI and PET are "complementary rather than
  redundant" and that multimodal frameworks "often achieve stronger predictive performance"
  (Lu et al. 2018; Castellano et al. 2024; Qiu et al. 2022); Table 1; Figure 6 lists "complementary
  information fusion" as the key strength of multimodal deep learning.
- **Interpretation**: The advantage is attributed to integrating heterogeneous evidence about
  different disease dimensions, mirroring clinical reasoning — but the survey stresses the benefit is
  conditional (see C04 and constraints).
- **Dependencies**: none
- **Tags**: multimodal-fusion, MRI, PET, complementarity
- **Sources**: qualitative claim ← paper.pdf p.630 §"Multimodal fusion methods" «complementary rather than redundant, which is why multimodal frameworks often achieve stronger» [input]

## C02: The field transitioned from handcrafted-feature ML to end-to-end deep learning
- **Statement**: The literature shows a clear transition from handcrafted-feature machine-learning
  pipelines (SVM, random forest, logistic regression, boosting) to end-to-end deep models (CNNs,
  multimodal fusion, transformer-equipped, graph-based) that learn representations directly from
  neuroimaging and multimodal data.
- **Status**: supported
- **Falsification criteria**: Evidence that handcrafted-feature pipelines remained dominant / that no
  such methodological shift occurred would refute this.
- **Proof**: [E02]
- **Evidence basis**: Abstract; "Taxonomy of Methods" (p.629-633); Figures 4 and 5 depict the
  evolution from handcrafted features → CNN era → multimodal era → relational/global modeling →
  trustworthy/clinical AI.
- **Interpretation**: The shift reflects deep learning's ability to learn hierarchical features
  without expert-driven feature engineering; traditional ML persists as interpretable baselines.
- **Dependencies**: none
- **Tags**: deep-learning, CNN, feature-engineering, methodological-evolution
- **Sources**: qualitative claim ← paper.pdf Abstract «clear transition from handcrafted-feature pipelines to» [input]

## C03: Transformers and GNNs are promising but not yet consistently superior to strong multimodal CNN baselines
- **Statement**: Transformer-equipped and graph-based models expand representational capacity (global
  context; relational/non-Euclidean structure), but the surveyed evidence does not establish that they
  are uniformly superior to strong, well-tuned multimodal CNN baselines across datasets and tasks.
- **Status**: supported
- **Falsification criteria**: A consistent, fair, multi-dataset body of evidence showing transformers
  or GNNs reliably beat strong multimodal CNN baselines under matched conditions would refute the
  "not yet established" framing.
- **Proof**: [E01, E05]
- **Evidence basis**: "Transformer and hybrid attention models" (p.631-632), "Strengths and
  weaknesses of transformers and GNNs" (p.643-645): transformers are "data hungry," GNN performance
  "depends heavily on graph construction choices," and "current evidence is not yet sufficient to
  conclude that they are uniformly better." Figure 6 marks their clinical readiness as "emerging."
- **Interpretation**: Their greatest value may lie in hybrid systems and in expanding the range of
  modelable structure, not in wholesale replacement of CNNs.
- **Dependencies**: C01
- **Tags**: transformers, graph-neural-networks, CNN-baseline, inductive-bias
- **Sources**: qualitative claim ← paper.pdf p.644 §"Strengths and weaknesses of transformers and GNNs" «current evidence is not yet sufficient to conclude that they are uniformly better than» [input]

## C04: Reported accuracy alone is not a reliable indicator of clinical value or cross-study comparability
- **Statement**: Because studies address different tasks (AD vs CN, MCI separation, progression
  prediction, multi-class staging) on differently curated datasets with different splits and
  preprocessing, headline accuracy/sensitivity/specificity/AUC cannot be directly compared and a
  higher number does not imply a more clinically useful model.
- **Status**: supported
- **Falsification criteria**: Demonstrating that reported accuracy is directly comparable across the
  literature and reliably tracks clinical usefulness would refute this.
- **Proof**: [E03, E05]
- **Evidence basis**: "Why accuracy alone is not enough" (p.640-641); Background (p.624). The survey
  explicitly prioritizes "interpretive depth, methodological structure, and translational value over
  leaderboard-style comparison."
- **Interpretation**: Evaluation standards should weight task difficulty, external validation,
  robustness, and reproducibility alongside conventional metrics.
- **Dependencies**: none
- **Tags**: evaluation, benchmarking, task-heterogeneity, clinical-relevance
- **Sources**: qualitative claim ← paper.pdf p.641 §"Why accuracy alone is not enough" «direct comparison based solely on reported accuracy can be misleading» [input]

## C05: Explainability is widely claimed but methodologically underdeveloped
- **Statement**: Explainability is often presented via a few Grad-CAM/SHAP/attention/saliency
  visualizations but is rarely evaluated for stability, reproducibility, clinical plausibility, or
  cross-cohort consistency; a visually plausible explanation is not necessarily a trustworthy one.
- **Status**: supported
- **Falsification criteria**: Evidence that most surveyed studies rigorously validate explanation
  quality (stability, expert validation, cross-cohort consistency) would refute this.
- **Proof**: [E04]
- **Evidence basis**: "Explainable AI" (p.633-635) and "Explainability and trust" (p.642-643):
  explanations are "often presented without systematic assessment of stability, plausibility,
  reproducibility, or clinical utility"; self-explainable graph models are noted as a shift toward
  architecture-level transparency.
- **Interpretation**: Explainability must be treated as a rigorously evaluated scientific component,
  not a presentation feature; architecture-level (self-explainable) approaches are promising.
- **Dependencies**: none
- **Tags**: explainable-AI, Grad-CAM, SHAP, self-explainable-GNN, trust
- **Sources**: qualitative claim ← paper.pdf p.648 §"Conclusion" «often presented without systematic assessment of stability, plausibility, reproducibility, or clinical» [input]

## C06: Benchmark dependence and limited external validation leave a gap between performance and clinical deployment
- **Statement**: Heavy reliance on a small number of public benchmarks (especially ADNI), combined
  with limited external/cross-site validation, weak reproducibility, class imbalance, and
  missing-modality challenges, means many high-performing research models fall short of dependable
  real-world clinical deployment.
- **Status**: supported
- **Falsification criteria**: Evidence of routine multi-center external validation and demonstrated
  cross-site clinical deployment across the field would refute this.
- **Proof**: [E03]
- **Evidence basis**: "Reproducibility and generalizability" (p.641-642); "Open Challenges"
  (p.645-646); Figure 4 "Key Research Challenges" (dataset dependence on ADNI, limited external
  validation, weak standardization of evaluation, class imbalance).
- **Interpretation**: Robustness to domain shift and reproducible open benchmarking should be central
  evaluation criteria, not secondary concerns.
- **Dependencies**: C04
- **Tags**: benchmark-dependence, ADNI, external-validation, reproducibility, clinical-translation
- **Sources**: qualitative claim ← paper.pdf p.646 §"Open Challenges" «reduces confidence in real-world generalization» [input]

## C07: The survey synthesizes 8 representative primary studies across five methodological groups
- **Statement**: The survey is scoped to approximately 10 to 15 representative studies and names 8
  primary studies (Islam & Zhang 2018; Lu et al. 2018; Golovanevsky et al. 2022; Qiu et al. 2022;
  Zhang et al. 2023; Castellano et al. 2024; Hu et al. 2024; Zhao et al. 2024), organized into five
  broad method groups (traditional ML, convolutional deep learning, multimodal fusion, transformer/
  hybrid-attention, and graph neural networks with explainability components).
- **Status**: supported
- **Falsification criteria**: Any count in this statement not matching the paper's own stated scope
  would refute it.
- **Proof**: [E05]
- **Evidence basis**: Scope section (p.623); Table 1 lists exactly these 8 studies (2018-2024).
- **Interpretation**: A deliberately curated narrative sample, not an exhaustive systematic review.
- **Dependencies**: none
- **Tags**: survey-scope, taxonomy, representative-studies
- **Sources**:
  - "approximately 10 to 15" ← paper.pdf p.623 §"Scope and Selection of Representative Studies" «The paper set was selected to cover approximately 10 to 15 representative and influential studies» [input]
  - 8 named studies ← paper.pdf p.623 «The surveyed studies include work by Islam and Zhang (2018), Lu et al.» [input] (list continues Golovanevsky 2022, Qiu 2022, Zhang 2023, Castellano 2024, Hu 2024, Zhao 2024 on the next lines; all 8 are also rows of Table 1, evidence/tables/table1.md)
  - "five broad groups" ← paper.pdf p.623 §"Scope and Selection of Representative Studies" «five broad groups: traditional machine learning, convolutional deep learning, multimodal fusion,» [input]
