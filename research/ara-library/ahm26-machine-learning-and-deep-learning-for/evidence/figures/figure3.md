# Figure 3: General workflow of machine learning and deep learning pipelines for Alzheimer's disease diagnosis

- **Source**: Figure 3, §"Datasets and Input Modalities" (PDF p.628)
- **Caption**: "Figure 3. General workflow of machine learning and deep learning pipelines for Alzheimer's disease diagnosis. The figure illustrates a typical end-to-end pipeline used in Alzheimer's disease diagnosis systems, beginning with multimodal data acquisition and preprocessing, followed by feature learning, multimodal fusion, diagnostic prediction, and interpretation or validation."
- **Screenshot**: figure3.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components** (six left-to-right pipeline stages, each with sub-items):
  1. **Data Acquisition**: MRI; PET; Clinical Data; Cognitive Scores; Genetic / Biomarker Data
  2. **Preprocessing**: Normalization; Registration; Skull stripping; Segmentation; Feature Preparation
  3. **Representation Learning / Feature Extraction**: Handcrafted Features; CNN-Based Features;
     Transformer-Based Features; Graph-Based Features
  4. **Multimodal Fusion**: Early Fusion; Intermediate Fusion; Late Fusion; Attention-Based Fusion
  5. **Prediction / Diagnosis**: Normal control vs AD; MCI Detection; Progression Prediction;
     Multiclass dementia Classification
  6. **Interpretation / Validation**: Grad-CAM; SHAP; External Validation; Clinical Relevance
- **Connections**: Arrows flow left to right stage-to-stage (end-to-end pipeline).
- **Annotations**: Each stage is a titled column box with stacked sub-item boxes.
- **What it conveys**: The canonical end-to-end AD-diagnosis pipeline. Mirrored into
  logic/solution/taxonomy.md ("General pipeline"). Supports C02 and the taxonomy.
