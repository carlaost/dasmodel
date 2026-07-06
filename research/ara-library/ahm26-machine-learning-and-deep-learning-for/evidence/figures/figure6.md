# Figure 6: Comparative framework of major model families in Alzheimer's disease diagnosis

- **Source**: Figure 6, §"Comparison of Representative Studies" (PDF p.637)
- **Caption**: "Figure 6. Comparative framework of major model families in Alzheimer's disease diagnosis. The figure contrasts traditional machine learning, CNN-based models, multimodal deep learning, transformer-based approaches, graph neural networks, and explainable AI-oriented systems in terms of input requirements, core strengths, principal limitations, interpretability, and clinical readiness." (in-image title: "Comparative Framework of Major Model Families in Alzheimer's Disease Diagnosis")
- **Screenshot**: figure6.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
This figure is a comparison **matrix** (rendered as a table image). Cell text transcribed verbatim
from the figure. It is a qualitative comparison (no numeric metrics).

| Model Family | Typical Input | Key Strength | Main Limitation | Interpretability | Clinical Readiness |
|--------------|--------------|--------------|-----------------|------------------|--------------------|
| Traditional Machine Learning | handcrafted features | simple and efficient | limited representation learning | moderate | moderate |
| CNN-Based Models | MRI or PET | strong spatial learning | limited global context | low to moderate | moderate |
| Multimodal Deep Learning | MRI + PET + clinical | complementary information fusion | missing modality challenge | moderate | high potential |
| Transformer / Hybrid Attention Models | imaging volumes | global context modeling | data-hungry and complex | moderate | emerging |
| Graph Neural Networks | brain or subject graphs | relational modeling | graph design sensitivity | moderate to high | emerging |
| Explainable AI-Oriented Models | multimodal or image-based | improved transparency | explanation quality not standardized | high | high potential |

- **What it conveys**: A structured qualitative comparison across the six families on five practical
  dimensions. Directly grounds C01 (multimodal strength), C03 (transformer/GNN "emerging"), and C05
  (explanation quality not standardized). Mirrored in logic/solution/taxonomy.md.
