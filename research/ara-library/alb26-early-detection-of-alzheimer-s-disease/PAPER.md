---
title: "Early Detection of Alzheimer's Disease Using Vision Transformers on CWT-Transformed EEG Signals in Response to Olfactory Stimuli"
authors: ["Azhar Hatem Jebur Albaidhani", "Gorkem Serbes", "H. Ilhan"]
year: 2026
venue: "IEEE Access"
doi: "10.1109/ACCESS.2026.3652249"
ara_version: "1.0"
grounding: abstract-only
domain: "Biomedical signal processing / deep learning for neurodegenerative-disease diagnosis (EEG, olfactory-evoked responses)"
keywords: ["Alzheimer's disease", "early detection", "EEG", "olfactory stimuli", "Continuous Wavelet Transform", "Short-Time Fourier Transform", "Vision Transformer", "CNN", "transfer learning", "time-frequency representation"]
claims_summary:
  - "CWT time-frequency images with a Vision Transformer give the highest patient-level accuracy (91.43%)."
  - "The same CWT+ViT configuration gives the highest image-level accuracy (85.18%), above CNN+CatBoost, CNN, ResNet50 and VGG16."
  - "CWT yields higher patient-wise performance than STFT as the EEG-to-image transformation."
  - "EEG recorded in response to olfactory stimuli is a usable biomarker for early AD detection via deep learning."
abstract: "Alzheimer's disease (AD) is a progressive neurodegenerative disorder that significantly impairs cognitive function, which can potentially hinder global healthcare systems. Early and accurate diagnosis of AD is imperative for effective intervention and treatment to take place. Electroencephalography (EEG) is a non-invasive method for monitoring brain activity, which can open opportunities for the early detection of AD through associated biomarkers. Recent studies have revealed a significant correlation between an impaired sense of smell and the onset of early AD. Our approach analyzes EEG signals generated in response to olfactory stimuli to leverage this biomarker and enhance classification accuracy. Despite admirable progress in Artificial Intelligence (AI) and deep learning for diagnosing neurodegenerative diseases, obstacles such as scarce datasets, model generalization, and suboptimal feature extraction hinder the practical application of these techniques for AD detection. The objective of this study is to develop a reliable approach for the early detection of AD by leveraging EEG data. This can be achieved by analysing EEG data using signal transformation techniques, such as the Short-Time Fourier Transform (STFT) and Continuous Wavelet Transform (CWT), and implementing advanced deep learning models. Our results show that patient-wise performance was highest using the CWT. In this configuration, the Vision Transformer (ViT) produced the best diagnostic accuracy (91.43% at the patient level and 85.18% at the image level). In the context of image-level evaluation, the custom Convolutional Neural Network (CNN) paired with CatBoost achieved 81.66% accuracy; the CNN reached 81.25%; transfer learning with ResNet50 yielded 80.69%; and VGG16 attained 79.82%."
---

# Early Detection of Alzheimer's Disease Using Vision Transformers on CWT-Transformed EEG Signals in Response to Olfactory Stimuli

> **Grounding note**: This ARA was compiled **abstract-only**. No licit open-access full text was
> available to the compiler — IEEE Access is gold OA but Unpaywall exposes `url_for_pdf=null` and
> IEEE Xplore serves a bot shell, so `paper.pdf` was never downloaded (see `sources.yaml`). Content
> below is grounded in the abstract (`metadata.md`) and the verified `sources.yaml` discovery record.
> Everything the abstract does not support is explicitly marked "Not available from provided input
> (no full text)". No figures, tables, or numbers beyond those printed in the abstract have been
> extracted or invented.

## Overview

The paper addresses early detection of Alzheimer's disease (AD) from electroencephalography (EEG)
recorded while subjects are exposed to **olfactory stimuli**, exploiting the reported link between
impaired olfaction and early AD. Raw EEG is converted to time-frequency images via two transforms —
Short-Time Fourier Transform (STFT) and Continuous Wavelet Transform (CWT) — and the resulting
images are classified with several deep-learning models (a custom CNN, CNN+CatBoost, ResNet50 and
VGG16 transfer learning, and a Vision Transformer). The headline result is that **CWT images
classified by a Vision Transformer** give the best performance: 91.43% patient-level and 85.18%
image-level accuracy. The study reuses a public olfactory-EEG dataset (Mendeley Data,
DOI 10.17632/sgzbgwjfkr.5; 35 seniors — 13 AD, 7 aMCI, 15 healthy — recorded under a rose/lemon
olfactory oddball paradigm).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) |
| [concepts.md](logic/concepts.md) | 10 technical terms formally defined |
| [experiments.md](logic/experiments.md) | 4 directional verification plans (E01–E04) |
| [related_work.md](logic/related_work.md) | Typed dependency graph incl. reused dataset |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |
| [solution/method.md](logic/solution/method.md) | Pipeline: EEG → STFT/CWT image → DL classifier |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, evaluation levels, models compared |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Runtime, data sources, dependencies (abstract-only) |
| [../data/dataset.md](data/dataset.md) | Reused olfactory-EEG dataset provenance |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 10-node research DAG (reconstructed from abstract; explicit + inferred nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index — N/A: no full text, so no tables/figures extracted |
