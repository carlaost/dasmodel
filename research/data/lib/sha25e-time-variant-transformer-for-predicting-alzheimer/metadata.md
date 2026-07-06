# Time-Variant Transformer for Predicting Alzheimer's Disease Progression from Longitudinal Data

- **Cite key**: Sha25e
- **Authors**: Habiba Assem Sharaf; Mohamed Kholief; H. Said
- **Year**: 2025  (2025-11-25)
- **Journal**: 2025 35th International Conference on Computer Theory and Applications (ICCTA)
- **DOI**: 10.1109/ICCTA68914.2025.11519825
- **URL**: https://doi.org/10.1109/ICCTA68914.2025.11519825
- **Citations**: 1 (1.6/yr)

## Abstract

Alzheimer's disease gradually affects cognitive functions such as memory, reasoning, and daily activities. Although transformer-based models have improved disease progression forecasting, they often face limitations in handling uneven visit times, incomplete records, and diverse data modalities. This study introduces a Time-Visit Transformer (TVT) tailored to predict Alzheimer's progression by explicitly modeling the timing gaps between patient follow-ups. TVT (i) encodes each visit, (ii) augments representations with Time2Vec to capture the temporal phase and scale, (iii) adjusts attention using the real-time intervals between visits delta-Time-FiLM, and (iv) incorporates site-specific context through Relational-FiLM. An attention layer then reads the sequence of visits in order and can gracefully handle missing entries. In head-to-head evaluations on longitudinal cohorts, TVT achieves an AUC-ROC of 0.9331 for conversion from cognitively normal (CN) to mild cognitive impairment (MCI), and 0.9529 for MCI to Alzheimer's disease (AD), demonstrating a time-sensitive model suitable for practical clinical use.
