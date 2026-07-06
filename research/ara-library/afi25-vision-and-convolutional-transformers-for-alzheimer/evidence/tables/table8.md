# Table 8 - Systematic Comparison of Representative LVM-related Models for Medical and AD-Specific Diagnosis

**Source**: Table 8, §11, pages 77–78
**Caption**: "Systematic Comparison of Representative LVM-related Models for Medical and AD-Specific Diagnosis. This table contrasts general medical foundation models with AD-specific applications reviewed in this survey, focusing on architectural design, data fusion mechanisms, and training paradigms. Acronyms: DAPT (Domain-Adaptive Pretraining), SFT (Supervised Fine-Tuning), RL (Reinforcement Learning), RLCF (Reinforcement Learning from Clinical Feedback), TFS (Trained from Scratch), MLP-P (MLP Projector Layer), Concat-Enc (Token Concatenation + Unified Encoder), X-Attn (Cross-Attention)"
**Screenshot**: table8.png
**Extraction type**: raw_table

### Category A: General Medical Foundation Models (Illustrative Examples)
| Model | Core architecture | Model size (Params) | Input modalities | Fusion mechanism | Pretraining data / scale | Adaptation / Fine-tuning strategy |
|---|---|---|---|---|---|---|
| BiomedGPT [272] | Encoder-Decoder Transformer | 182M | Vision (Multiple), Text | Inherent in Generative Framework | 14+ Public Medical Datasets | Unified Pretraining + SFT |
| GMAI-VL [273] | LLaVA-style (ViT + LLM) | 7B | Vision (Multiple), Text | MLP-P | GMAI-VL-5.5M (5.5M pairs) | 3-Stage (Alignment + IT) |
| HuatuoGPT-Vision [274] | LLaVA-style (ViT + LLM) | 34B | Vision (Multiple), Text | MLP-P | PubMedVision (1.3M VQA) | DAPT via "Unblinded" Pipeline |
| UMed-LVLM [275] | MedVInT-based (Encoder + LLM) | ~7B | Vision (Multiple), Text | Alignment via RL Rewards | MAU Dataset (5.8k images) | 2-Stage (SFT + RL) |

### Category B: AD-Specific Applications (From This Survey)
| Model | Core architecture | Model size (Params) | Input modalities | Fusion mechanism | Pretraining data / scale | Adaptation / Fine-tuning strategy |
|---|---|---|---|---|---|---|
| ViT-TST [134] | Dual Transformer (ViT + TST) | Not Specified | sMRI (single-modality) | Sequential Modeling | General-domain (ImageNet) | Standard SFT on ADNI |
| AD-Transformer [49] | Hybrid CNN-Transformer | Not Specified | sMRI, Clinical, Genetic | Concat-Enc | TFS on ADNI (1651 subjects) | End-to-end Training |
| 3MT [50] | Hybrid CNN-Transformer | Not Specified | sMRI, Clinical | Cascaded X-Attn | General-domain (Pretrained Backbones) | SFT on ADNI (816 subjects) with Modality Dropout |
| MCAD [155] | Hybrid CNN-Transformer | Not Specified | sMRI, PET, CSF | Dual-Stream X-Attn | TFS on ADNI (467 subjects) | End-to-end Training with Alignment Loss |
| BIGFormer [109] | Graph Transformer | Not Specified | rs-fMRI, Genetic (SNP) | Graph-based Attention | TFS on ADNI (708 subjects) | End-to-end Training |
