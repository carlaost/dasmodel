# Machine Learning Based Prognosis of Alzheimer’s Disease Using Multimodal Data

- **Cite key**: Man25b
- **Authors**: Tushar Mane; Gargi Rahane; Atharva Godbole; Aabha Jog
- **Year**: 2025  (2025-12-09)
- **Journal**: 2025 Supercomputing India (SCI)
- **DOI**: 10.1109/SCI68648.2025.11333833
- **URL**: https://doi.org/10.1109/SCI68648.2025.11333833
- **Citations**: 0 (0.0/yr)

## Abstract

The goal of present research paper is to develop a machine learning based approach for prognosis of Alzheimer’s Disease. In the present research MRI scans and ADAS scores of 300+ patients from ADNI1 standardized data collection are used. Each MRI is converted to its feature vector by custom three dimensional CNN. ADAS11 and ADAS13 scores are fit over time and classified into analysis classes labelled as Stable, Slow Decline, Rapid Decline. The model was trained on flattened time series data (each time point including MRI feature vector, ADAS scores) concatenated with other parameters ie. Age, Sex and analysis class label. A trajectory prediction technique was adopted by feeding this flattened time series data to a supervised, Extreme Gradient Boosting (XGBoost) classifier, that achieved research grade evaluations (Average: AUC ROC: 0.813, weighted F1: 0.676, weighted PR AUC: 0.726) with single and multi time point data input even with missing data. The pipeline was executed on GPU-accelerated High Performance Computing (HPC) infrastructure, achieving significant speedup and enabling scalable evaluation across multiple feature subset. Evaluations indicate that the model has strong discriminative power and balanced performance across classes making it a promising baseline for further research.
