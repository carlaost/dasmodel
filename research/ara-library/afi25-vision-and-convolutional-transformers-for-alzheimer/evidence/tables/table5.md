# Table 5 - Summary of studies using CViTs for AD classification and MCI conversion prediction

**Source**: Table 5, §8, pages 28–31 (spans 4 PDF pages)
**Caption**: "Summary of studies using CViTs for AD classification and MCI conversion prediction"
**Screenshot**: table5.png (caption/first page of the multi-page table)
**Extraction type**: raw_table

All 46 CViT studies transcribed. Values exact; `–` = not reported. Performance columns are
Accuracy / Sensitivity / Specificity / Precision / AUC, with dataset qualifiers inline. "Int." =
internal validation; "Ext." = external-validation cohort. Where source multi-value cells are densely
laid out, running-text corroboration (§8.1–8.2) was used; the screenshot (table5.png) is authoritative.

| Author [ref] | Year | Task | Modality (type) | Fusion | Dataset | Technique | Integration | Classification | Int. val | Ext. | Accuracy | Sensitivity | Specificity | Precision | AUC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kadri et al. [153] | 2021 | AD Class | sMRI (Single) | – | ADNI, OASIS | CrossViT + WRSE-Net + ProGAN | Serial & (Channel Attention) | AD vs. MCI vs. CN | – | – | 99.0% | – | – | – | – |
| Zhu et al. [160] | 2022 | AD Class | sMRI (Single) | – | ADNI | BraInf | Hierarchical | AD vs. NC | 10-fold CV | – | 97.97% | 97.74% | 98.17% | 98.16% | – |
| Huang et al. [209] | 2023 | AD Class | sMRI (Single) | – | ADNI, AIBL | RST | Serial | AD vs. NC | 70–10–20 (T-V-T) | AIBL | 99.59% (ADNI), 94.01% (AIBL) | 99.59% (ADNI) | 99.58% (ADNI) | 99.83% (ADNI) | – |
| Hu et al. [81] | 2023 | AD Class | sMRI (Single) | – | ADNI, OASIS | Conv-Swinformer | Serial | AD vs. CN | 70–15–15 (T-V-T) | OASIS | 93.56% (ADNI), 92.31% (OASIS) | 93.81% (ADNI) | 93.31% (ADNI) | – | 97.49% (ADNI), 94.17% (OASIS) |
| Hu et al. [131] | 2023 | MCI Prediction | sMRI (Single) | Intermediate (Temporal) | ADNI | VGG-TSwinformer | Serial | pMCI vs. sMCI | 65–20–15 (T-V-T) | – | 77.20% | 79.97% | 71.59% | – | 81.53% |
| Xin et al. [31] | 2023 | AD Class | sMRI (Single) | – | ADNI, AIBL | ECSnet | Serial | AD vs. CN | 5-fold CV | AIBL | 93.9% (ADNI), 93.9% (AIBL) | 92.5% (ADNI), 91.1% (AIBL) | 94.7% (ADNI), 94.4% (AIBL) | – | 96.4% (ADNI), 96.3% (AIBL) |
| Zhao et al. [32] | 2023 | AD Class & MCI Pred | sMRI (Single) | – | ADNI, AIBL | IDA-Net | Hierarchical | AD vs. NC; pMCI vs. sMCI | 60–20–20 (T-V-T) | AIBL | 92.7%/90.9% (AD/NC); 83.5%/81.2% (pMCI/sMCI) | 91.9%/90.3%; 80.2%/79.00% | 94.6%/93.5%; 85.5%/83.5% | – | 97.2%/96.1%; 87.7%/85.4.9% |
| Khatri et al. [145] | 2024 | AD Class | sMRI (Single) | – | ADNI | MBConv + PConv + IRFFN | Hierarchical | AD vs. HC | 10-fold CV | – | 97.29% | 95.96% | 96.15% | 97.14% | – |
| Khatri and Kwon [30] | 2024 | AD Class | sMRI (Single) | – | ADNI | Optimized CViT | Hierarchical | AD vs. HC | 90–10 (T-T) | – | 95.37% | 91.09% | 100% | – | – |
| Li et al. [144] | 2024 | AD Class | sMRI (Single) | – | ADNI | LD-MILCT | Serial | AD vs CN (TD) | 10-fold CV | – | 91.0% | 90.3% | 95.7% | – | – |
| Zhang et al. [157] | 2024 | AD Class | sMRI (Single) | – | ADNI | RepBoTNet-CESA | Serial & MHSA | AD vs. NC | 5-fold CV | – | 96.58% | 96.23% | – | 97.26% | – |
| Huang and Qiu [210] | 2024 | AD Class | sMRI (Single) | – | ADNI, OASIS3 | MC-ViT | Serial | AD vs. NC | 37.5–12.5–50 (ADNI) | OASIS3 | 90.07% (ADNI), 77.80% (OASIS3) | 90.22% (ADNI), 82.76% (OASIS3) | – | – | 95.57% (ADNI), 86.32% (OASIS3) |
| Poonia and Al-Alshaikh [152] | 2024 | AD Class | sMRI (Single) | – | ADNI | (InceptionV3, VGG19, ResNet50, DenseNet121) + ViT | Serial & (Late fusion) | Early vs. Mild vs. High vs. Normal | 10-fold CV; 70–30 (T-T) | – | 96% (InceptionV3+ViT) | 90% | – | 94% | – |
| Sait [141] | 2024 | AD Class | sMRI (Single) | – | OASIS, Kaggle | LeViT + EfficientNet B7 | Parallel | ND vs. VMD vs. MD vs. MoD | OASIS 70–15–15 | Kaggle | 99.8% | 99.4% | 99.8% | – | 0.99 |
| Sait and Nagaraj [187] | 2024 | AD Class | sMRI (Single) | – | Kaggle, OASIS (Kaggle) | CCT-Linformer + TT-Performer | Parallel | ND vs. VMD vs. MD vs. MoD | Kaggle 70–15–15 | OASIS (20% T) | 99.2% (Kaggle), 98.8% (OASIS) | 98.9% (Kaggle), 98.1% (OASIS) | 98.6% (Kaggle), 97.5% (OASIS) | 98.9% (Kaggle), 97.9% (OASIS) | – |
| Menon and Gunasundari [211] | 2024 | AD Class | sMRI (Single) | – | Kaggle | DenseNet-121 + ViT | Parallel | ND vs. VMD vs. MD vs. MoD | – | – | 93.0% (ViT), 99.0% (Fusion) | 93.0% (ViT), 99.0% (Fusion) | – | 93.0% (ViT), 99.0% (Fusion) | – |
| Rehman et al. [165] | 2024 | AD Class | 18F-FDG PET (Single) | – | ADNI | ResGLPyramid | Hierarchical | AD vs. NC | 10-fold CV | – | 97.00% | 96.10% | 97.50% | – | 96.90% |
| Zuo et al. [212] | 2023 | AD Class | fMRI (Single) | – | ADNI | DAGAE + GCN classifier | Serial | LMCI vs. NC (GCN) | 5-fold CV | – | 85.33% | 84.00% | 86.67% | – | 86.42% |
| Zhou et al. [140] | 2024 | AD Class | rs-fMRI (Single) | – | ADNI | LCGNet | Parallel | AD vs. NC | 5-fold CV | – | 95.3% | 93.3% | 96.7% | – | 96.5% |
| Zhang et al. [146] | 2024 | AD Class | rs-fMRI (Single) | – | ADNI2, ADNI3, OASIS, HUASHAN-MCI | HFBN (ST-GCFE (GCN) + HNFM (Transformer)) | Hierarchical | MCI vs. NC | 5-fold CV | – | 83.7% (ADNI2), 89.9% (OASIS) | 91.3% (ADNI2), 76.7% (OASIS) | 70.1% (ADNI2), 96.7% (OASIS) | – | 80.7% (ADNI2), 81.2% (OASIS) |
| Dai et al. [102] | 2023 | AD Class | sMRI, Clinical Data (Multi) | Intermediate (Single-Level) | ADNI1, ADNI2 | DE-JANet | Serial | AD vs. NC | ADNI1 | ADNI2 | 97.22% (ADNI2) | 98.08% (ADNI2) | 96.43% (ADNI2) | 96.23% (ADNI2) | – |
| Chen et al. [142] | 2025 | AD Class | sMRI, Clinical Data (Multi) | Intermediate (Single-Level) | ADNI | MMDF + ViT + CNN | Parallel | AD vs. CN vs. MCI | 70–20–10 (T-V-T) | – | 97.65% | 96.40% | – | 96.98% | – |
| Illakiya et al. [183] | 2023 | MCI Prediction | sMRI, Clinical data (Multi) | Intermediate (Single-Level) | ADNI | Swin Transformer + DCPAN + ADF | Parallel | pMCI vs sMCI | 4-fold CV | – | 70.21% (Swin), 79.8% (Fusion) | 66.86% (Swin), 80.23% (Fusion) | 67.64% (Swin), 76.66% (Fusion) | – | – |
| Luo and He [143] | 2024 | MCI Prediction | sMRI, Neurocognitive Metadata (Multi) | Intermediate (Single-Level) | ADNI1, ADNI2 | DAFN | Serial & (Spatial Attention) | pMCI vs. sMCI | 5-fold CV | – | 81.34% | 85.0% | 78.0% | – | 87.4% |
| Liu et al. [50] | 2023 | AD Class & MCI Pred | sMRI, Clinical Data (Multi) | Hybrid (Multi-Level System) | ADNI, AIBL | 3MT | Serial | AD vs. CN; MCI→AD conversion | 5-fold CV | AIBL; ADNI2 | 99.4%/96.3% (AD/CN); 83.33% (ADNI2, conversion) | 100.0%/97.5% | 98.9%/90.3% | – | 99.7%/98.4%; 89.89% (conversion) |
| Gao et al. [184] | 2023 | AD Class & MCI Pred | T1w-sMRI, Clinical Data (Multi) | Intermediate (Single-Level) | ADNI1, ADNI2 | CNN-Transformer | Serial | AD vs. NC; pMCI vs. sMCI | ADNI1 (with aug) | ADNI2 | 90.5% (AD/NC); 73.6% (pMCI/sMCI) | 84.6%; 59.1% | 95.0%; 82.1% | – | 93.9%; 73.7% |
| Zhang et al. [62] | 2024 | AD Class & MCI Pred | Clinical, T1w-MRI, AV45-PET (Multi) | Intermediate (Hierarchical) | ADNI, OASIS3, NACC, C-PAS | CNNs + Image-Tabular Cross-Transformer | Hierarchical & (Cross Attention) | CN vs. MCI vs. DE (COG); sMCI vs. pMCI (MCIC) | 5-fold CV (merged) | C-PAS | 77.9% (Int), 66.1% (C-PAS); 76.1% (MCIC) | 76.3% (Int), 65.3% (C-PAS); 69.0% (MCIC) | 88.1% (Int), 79.3% (C-PAS); 79.3% (MCIC) | – | 90.9% (Int), 80.3% (C-PAS); 81.7% (MCIC) |
| Liu et al. [192] | 2024 | AD Class | T1w-sMRI, SNP (Genetic), Clinical (Multi) | Hybrid (Generative) | ADNI, UK Biobank, 441 SNPs | STAA | Serial | AD vs. NC | 5-fold CV | – | 87.2% (MRI), 69.7% (SNP) | 82.3% (MRI), 62.5% (SNP) | 91.1% (MRI), 75.4% (SNP) | – | 92.0% (MRI), 71.1% (SNP) |
| Yu et al. [49] | 2024 | AD Class & MCI Pred | sMRI, Clinical, Genetic (Multi) | Intermediate (Single-Level) | ADNI-1/2/GO | AD-Transformer | Serial | AD vs NC; pMCI vs sMCI | 5-fold CV | – | 95.9% (AD/NC); 75.3% (pMCI/sMCI) | 95.6%; 74.5% | 96.1%; 75.5% | – | 99.3%; 84.5% |
| Kadri et al. [178] | 2022 | AD Class | sMRI, PET (FDG-PET) (Multi) | Input-Level | ADNI | EfficientNet V2 + ViT | Serial | AD vs. MCI vs. CN | – | – | 96.0% | – | – | – | – |
| Gao et al. [172] | 2023 | AD Class & MCI Pred | T1w-sMRI, T2w-sMRI, PET (Multi) | Hybrid (Generative) | ADNI1, ADNI2, OASIS3 | MLG-GAN + Mul-T | Serial | AD vs. CN; pMCI vs. sMCI | ADNI1 | ADNI2 | 94.4% (AD/CN); 77.8% (pMCI/sMCI) | 93.0%; 75.4% | 95.5%; 79.6% | – | 97.6%; 82.8% |
| Tang et al. [156] | 2023 | AD Class | sMRI, PET (FDG-PET) (Multi) | Intermediate (Attention-Based) | ADNI | CsAGP | Serial & (Cross Attention) | AD vs. CN | 60–20–20 (T-V-T) | – | 99.04% | 97.96% | 99.54% | – | 99.80% |
| Odusami et al. [148] | 2023 | AD Class | sMRI, PET (FDG-PET) (Multi) | Input-Level | ADNI | VGG16 + ViT | Serial | AD vs. EMCI | 5-fold CV | – | 81.25% (MRI), 93.75% (PET) | – | – | – | – |
| Odusami et al. [149] | 2023 | AD Class | sMRI, FDG-PET (Multi) | Input-Level | ADNI, OASIS, AANLIB | Mobile ViT (MViTv3) | Serial | AD vs CN | – | ADNI, OASIS, AANLIB | 99.00% (AANLIB), 96.00% (ADNI) | 98.44% (AANLIB), 94.12% (ADNI) | 99.00% (AANLIB), 97.00% (ADNI) | – | – |
| Odusami et al. [151] | 2024 | AD Class | sMRI, FDG-PET (Multi) | Input-Level | ADNI1, OASIS | Image Fusion (GLP + SPCNN) + (MViT) + (QDO) | Serial | AD vs. CN | 60–40 (T-V) | OASIS | 94.73% (ADNI MRI), 80.00% (OASIS MRI) | 90.70% (ADNI MRI), 90.00% (OASIS MRI) | 100.00% (ADNI MRI), 70.00% (OASIS MRI) | – | – |
| Odusami et al. [150] | 2024 | AD Class | sMRI, FDG-PET (Multi) | Input-Level | ADNI, OASIS, AANLIB | MViTv3 | Serial | AD vs CN | 70–20–10 (T-V-T) | – | 99.25% (ADNI), 99.50% (AANLIB), 96.00% (OASIS) | – | – | – | – |
| Khan et al. [182] | 2024 | AD Class | sMRI, PET (FDG-PET) (Multi) | Intermediate (Hierarchical) | ADNI | Dual-3DM3-AD | Hierarchical | AD vs. CN | 10-fold CV | – | 98.3% | 97.4% | 97.8% | – | – |
| Miao et al. [147] | 2024 | AD Class | sMRI, PET (FDG-PET) (Multi) | Intermediate (Hierarchical) | ADNI | MMTFN | Hierarchical | AD vs. NC | 5-fold CV | – | 94.61% | 92.92% | – | 93.89% | 99.30% |
| Tang et al. [181] | 2024 | AD Class | sMRI, PET (FDG-PET) (Multi) | Intermediate (Hierarchical) | ADNI | Transformer + 3DCNN | Serial | AD vs. CN | 10-fold CV | – | 98.10% | 95.82% | 96.75% | 99.09% | 98.35% |
| Qiu et al. [193] | 2024 | AD Class | sMRI (GM, WM), PET (FDG-PET) (Multi) | Hybrid (Systemic) | ADNI-1/2/3, AIBL | MDL-Net | Hierarchical | AD vs. CN | 10-fold CV | AIBL | 96.37% (ADNI), 90.91% (AIBL) | 97.40% (ADNI), 92.05% (AIBL) | 95.38% (ADNI), 87.88% (AIBL) | – | 98.48% (ADNI), 96.13% (AIBL) |
| Liu et al. [154] | 2024 | AD Class | MRI (GM, WM, CSF), PET (Multi) | Hybrid (Systemic) | ADNI | HAMMF | Serial & (Channel & Spatial Attention) | AD vs. NC | 5-fold CV | – | 93.15% | 93.15% | – | 93.57% | 93.15% |
| Zhang et al. [155] | 2023 | AD Class | sMRI, PET (FDG-PET), CSF (Multi) | Intermediate (Attention-Based) | ADNI | MCAD | Serial & (Cross Attention) | AD vs. CN | 5-fold CV | – | 91.07% | 91.03% | 91.07% | – | 94.07% |
| Kadri et al. [169] | 2023 | AD Class | MRI, PET, CT (Multi) | Intermediate (Single-Level) | OASIS-1/3, ADNI | Swin Transformer + Enhanced EfficientNetB0; Modified CoAtNet | Parallel; Serial | ND vs. VMD vs. MD vs. MoD | – | – | 93.23% (OASIS MRI, Swin+EffNet), 97.33% (OASIS MRI, CoAtNet) | 93.86%; 97.34% | – | 93.52%; 97.35% | – |
| Kadri et al. [188] | 2025 | AD Class | MRI, PET, DTI, sfMRI (Multi) | Hybrid (Multi-Level System) | ADNI, OASIS | Transformer Hybrid Model | Serial | AD vs. MCI vs. CN | – | – | 99.98% (ADNI), 99.91% (OASIS) | – | – | – | – |
| Zuo et al. [177] | 2023 | AD Class | DTI, rs-fMRI (Multi) | Hybrid (Generative) | ADNI | BSFL | Serial & (Cross Attention) | LMCI vs. NC | 10-fold CV | – | 94.30% | 93.42% | 95.12% | – | 98.12% |
| Zuo et al. [194] | 2023 | AD Class | fMRI, DTI (Multi) | Hybrid (Generative) | ADNI | CT-GAN | Serial & (Cross Attention) | LMCI vs. AD (Brainnetcnn) | 5-fold CV | – | 95.19% | 95.24% | 95.12% | – | 94.27% |

Note: study [32] AUC "85.4.9%" is reproduced verbatim as printed (an apparent typo in the source).
