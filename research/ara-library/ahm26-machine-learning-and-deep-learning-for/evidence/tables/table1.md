# Table 1 - Comparison of representative studies in Alzheimer's disease diagnosis

**Source**: Table 1, §"Comparison of Representative Studies" (PDF p.638)
**Caption**: "Table 1. Comparison of representative studies in Alzheimer's disease diagnosis."
**Screenshot**: table1.png
**Extraction type**: raw_table

Values transcribed exactly from the source table. This is a qualitative comparison table (no numeric
performance metrics).

| Study | Year | Modality / Data | Core Method | Main Contribution | Main Limitation |
|-------|------|-----------------|-------------|-------------------|-----------------|
| Islam & Zhang | 2018 | MRI | Ensemble CNN | Early influential MRI-based end-to-end CNN diagnosis | Single-modality and earlier-generation benchmark setting |
| Lu et al. | 2018 | MRI + FDG-PET | Multimodal multiscale DNN | Showed the value of multimodal fusion and progression-related prediction | Strong dependence on curated benchmark data |
| Golovanevsky et al. | 2022 | Imaging + genetic + clinical | Attention-based multimodal DL | Adaptive cross-modal weighting beyond simple concatenation | Architecturally complex and less deployment-oriented |
| Qiu et al. | 2022 | Imaging + non-imaging multimodal data | Successive-step multimodal DL | Broad dementia assessment with external validation and interpretation | High complexity and demanding multimodal pipeline |
| Zhang et al. | 2023 | sMRI + PET + phenotypic data | Multi-modal GNN | Integrates relational and phenotypic information in graph form | Graph construction choices can affect reproducibility |
| Castellano et al. | 2024 | 2D/3D MRI + amyloid PET | Uni-modal and multimodal CNNs | Clear comparison of 2D vs 3D and single vs multimodal settings | Mainly centered on one cohort |
| Hu et al. | 2024 | Claims / relational health data | Self-explainable GNN | Built-in interpretability through relation importance | Not a pure neuroimaging diagnosis system |
| Zhao et al. | 2024 | 3D MRI | Transformer-equipped CNN | Hybrid local-global representation learning | Transformer benefit still requires broader validation |
