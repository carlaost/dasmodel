# Table 4 - Summary of studies using ViTs for AD classification and MCI conversion prediction

**Source**: Table 4, §7, pages 26–28 (spans 3 PDF pages)
**Caption**: "Summary of studies using ViTs for AD classification and MCI conversion prediction"
**Screenshot**: table4.png (caption/first page of the multi-page table)
**Extraction type**: raw_table

All 22 ViT studies transcribed. Values are exact; `–` = not reported in the source. Performance
columns are Accuracy / Sensitivity / Specificity / Precision / AUC. Multi-task rows carry per-task
values inline. "Ext. val" = external-validation cohort (blank/– if none).

| Author [ref] | Year | Task | Modality (type) | Fusion | Dataset | Technique | Classification | Internal val | Ext. val | Accuracy | Sensitivity | Specificity | Precision | AUC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mora-Rubio et al. [161] | 2023 | AD Classification | sMRI (Single) | – | Combined ADNI & OASIS | ViT | AD vs. CN (ViT) | 60–20–20 (T-V-T) | – | 89.02% | 89.02% | 74.01% | – | – |
| Carcagnì et al. [158] | 2023 | AD Classification | sMRI (Single) | – | ADNI2, OASIS1 | CNN (ResNet, DenseNet, EfficientNet) & Transformer (MAE, DeiT) | AD vs. NC (DeiT) | 5-fold CV | – | 77.0% (ADNI2), 74.4% (OASIS1) | – | – | – | 79.00% (ADNI2), 74.00% (OASIS1) |
| Alp et al. [134] | 2024 | AD Classification | sMRI (Single) | – | ADNI1: Complete 1Yr 1.5T; ADNI1: Complete 3Yr 3T | ViT + Time Series Transformer | AD vs. CN | 60–20–20 (T-V-T) | – | 95.169% (1Yr), 99.048% (3Yr) | 95.50% (1Yr), 99.50% (3Yr) | – | – | – |
| Hoang et al. [207] | 2023 | MCI Prediction | sMRI (Single) | – | ADNI | ViT | MCIC vs. MCINC | 90–10 (T-T) | – | 83.27% | 85.07% | 81.48% | – | – |
| Joy et al. [195] | 2025 | AD Classification | sMRI (Single) | – | ADNI | ViTAD | CN vs. EMCI vs. LMCI vs. MCI vs. AD | 85–15 (T-T) | – | 99.98% | 100% | – | 100% | – |
| Mahim et al. [197] | 2024 | AD Classification | sMRI (Single) | – | Kaggle, ADNI | ViT-GRU | ND/VMD/MD/MoD; AD vs. MCI vs. CN | 10-fold CV | – | 99.53% (Dataset 1), 99.26% (ADNI) | 99.53% (D1), 99.26% (ADNI) | 99.76% (D1), 99.45% (ADNI) | 99.54% (D1), 99.27% (ADNI) | – |
| Almufareh et al. [196] | 2023 | AD Classification | sMRI (Single) | – | OASIS1 | ViT | ND vs. VMD vs. MD vs. MoD | 80–20 (T-V) | – | 99.06% | 99.14% | – | 99.06% | – |
| Shah et al. [198] | 2024 | AD Classification | sMRI (Single) | – | Kaggle, ADNI (Kaggle) | BiViT | ND/VMD/MD/MoD (no aug); CN/EMCI/LMCI/MCI/AD (with aug) | train/test split | – | 96.0% (no aug), 45.0% (with aug) | 98.0%, 69.0% | – | 88.0%, 33.0% | 99.0%, 73.0% |
| Alshayeji [199] | 2024 | AD Classification | sMRI (Single) | – | Kaggle | Pre-trained (ViT) | ND vs. VMD vs. MD vs. MoD | 85–15 (T-T) | – | 99.83% | 99.69% | 99.88% | 99.54% | – |
| Hosny et al. [159] | 2024 | AD Classification | sMRI (Single) | – | Kaggle | EfficientViT | ND vs. VMD vs. MD vs. MoD | 5-fold CV | – | 99.24% | 99.38% | – | 99.02% | – |
| Pramanik et al. [200] | 2024 | AD Classification | sMRI (Single) | – | Kaggle | FGI-CogViT | ND vs. VMD vs. MD vs. MoD | 80–20 (T-T) | – | 98.83% | 99.48% | – | 99.52% | – |
| Kurniasari et al. [201] | 2025 | AD Classification | sMRI (Single) | – | Kaggle | ViT | ND vs. VMD vs. MD vs. MoD | 81–9–10 (T-V-T) | – | 98.19% | 96.34% | 98.80% | – | – |
| Lu et al. [202] | 2025 | AD Classification | sMRI (Single) | – | OASIS1 | RanCom-ViT | ND vs. VMD vs. MD vs. MoD | 80–20 (T-T) | – | 99.54% | 98.82% | 99.63% | 99.55% | – |
| Shin et al. [162] | 2023 | AD Classification | 18F-Florbetaben PET (Single) | – | Dong-A University Hospital cohort | ViT | HC vs. (AD + MCI) (Original Data) | 60–20–20 (T-V-T) | – | 80.00% | 60.00% | – | 75.00% | – |
| Khatri and Kwon [166] | 2023 | MCI Prediction | 18F-FDG PET (Single) | – | ADNI1/2/GO | ViT-DINO | MCI-c vs MCI-s | 5-fold CV | – | 92.31% | 90.21% | 95.50% | 93.10% | 96.00% |
| Zhang et al. [203] | 2022 | AD Classification | rs-fMRI (Single) | – | ADNI | KD-Transformer | EMCI vs. HC | 80–20 (T-V) | – | 80.0% | – | – | – | – |
| Sarraf et al. [204] | 2023 | AD Classification | rs-fMRI, sMRI (Single) | – | ADNI | OViTAD | AD vs. HC vs. MCI | 80–10–10 (T-V-T) | – | 87.00% (sMRI), 97.00% (fMRI) | 87.00% (sMRI), 97.00% (fMRI) | – | 81.00% (sMRI), 97.00% (fMRI) | – |
| He et al. [205] | 2024 | AD Classification | rs-fMRI (Single) | – | ADNI-1/2/3 | STGTN | AD vs. NC | 5-fold CV with AE augmentation | – | 92.58% (ADNI-1/2), 92.30% (ADNI3) | 96.88% (ADNI-1/2), 95.81% (ADNI3) | 94.03% (ADNI-1/2), 94.00% (ADNI3) | – | 98.67% (ADNI-1/2), 98.45% (ADNI3) |
| Wang [206] | 2025 | AD Classification | rs-fMRI (BOLD) (Single) | – | ADNI2 | VTFF | HC vs. EMCI vs. LMCI vs. AD | 80–20 (T-T) | – | 84.2% | 81.0% | 94.0% | 85.0% | 88.0% |
| Saoud and AlMarzouqi [163] | 2024 | AD Classification & MCI Prediction | sMRI (Single) | – | ADNI | 3D-ViTs with DBN | AD vs. CN; pMCI vs. sMCI | 80–20 (T-V) | – | 90.00% (AD/CN), 94.00% (pMCI/sMCI) | – | – | – | 91.00% (AD/CN), 95.00% (pMCI/sMCI) |
| Castro-Silva et al. [191] | 2024 | AD Classification | sMRI, Clinical data (Multi) | Intermediate (Single-Level) | ADNI, AIBL, OASIS | MIMD-3DVT | AD vs. CN | 7-fold CV | – | 97.14% | – | – | – | 98.4% |
| Zou et al. [109] | 2024 | AD Classification & MCI Prediction | fMRI, SNP (genetic) (Multi) | Hybrid (Graph-based) | ADNI | BIGFormer | HC vs. AD; sMCI vs. pMCI | 10-fold CV | – | 91.87% (HC/AD), 85.71% (sMCI/pMCI) | 89.74%, 84.62% | 92.86%, 86.67% | – | 94.14%, 88.21% |
