# Figure 4: Taxonomy of Machine Learning and Deep Learning Approaches for Alzheimer's Disease Diagnosis

- **Source**: Figure 4, §"Datasets and Input Modalities" / bridging into "Taxonomy of Methods" (PDF p.628, image on p.629)
- **Caption**: "Figure 4: Taxonomy of Machine Learning and Deep Learning Approaches for Alzheimer's Disease Diagnosis." (in-image title: "Workflow of AI-Based 'Alzheimer's Disease Diagnosis Systems'")
- **Screenshot**: figure4.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components** (an expanded pipeline + taxonomy with eight top columns and two bottom panels):
  - **Data Acquisition**: MRI; PET / FDG-PET / Amyloid PET; Clinical and demographic data; Cognitive
    scores; Phenotypic information
  - **Preprocessing**: Image normalization; Registration / alignment; Skull stripping / segmentation;
    Feature preparation; Data cleaning and harmonization
  - **Modeling Paradigms** (color-grouped): Traditional Machine Learning (handcrafted features; SVM,
    Random Forest, Logistic Regression); CNN-Based Deep Learning (2D CNN, 3D CNN, Volumetric learning);
    Multimodal Fusion (MRI + PET fusion; imaging + non-imaging fusion; feature concatenation / learned
    fusion); Transformer-Based Models (Self-attention; Vision Transformer); Graph Neural Networks
    (brain connectivity graphs; population graphs; graph attention networks); Explainable AI (Grad-CAM,
    SHAP; self-explainable graph models)
  - **Learning and Feature Interaction**: Intra-modality feature learning; Inter-modality feature
    fusion; Attention mechanisms; Cross-attention; Representation learning
  - **Prediction Tasks**: AD vs healthy control; MCI classification; Early diagnosis; Disease staging;
    Risk prediction; Differential diagnosis; Prognosis / progression prediction
  - **Evaluation and Validation**: Accuracy, sensitivity, specificity, AUC; Cross-validation; External
    validation; Multi-cohort testing; Class imbalance consideration; Generalization assessment
  - **Interpretability and Clinical Trust**: Brain-region relevance; Modality importance; Explanation
    stability; Biological plausibility; Clinician trust
  - **Clinical Deployment Goals**: Early diagnosis; Decision support; Robustness; Explainability;
    Generalizable deployment in hospitals
  - **Bottom panel — Key Research Challenges**: Dataset dependence on ADNI; Limited external validation;
    Weak standardization of evaluation; Class imbalance; Limited fairness analysis; Shallow
    interpretability; Clinical translation gap
  - **Bottom panel — Future Directions**: Multi-center validation; Longitudinal modeling; Better
    multimodal fusion; Rigorous explainability; More graph and transformer research; Uncertainty
    estimation; Domain adaptation; Federated / privacy-aware learning
- **Connections**: Left-to-right arrows across the eight column stages; two summary panels beneath.
- **What it conveys**: The paper's full taxonomy of method families plus the challenges/directions that
  frame the critical discussion. Central grounding for logic/solution/taxonomy.md,
  challenges_and_directions.md; supports C02, C03, C05, C06.
