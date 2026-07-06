---
title: "An Explainable Web-Based Diagnostic System for Alzheimer's Disease Using XRAI and Deep Learning on Brain MRI"
authors: [Serra Aksoy, Arij Daou]
year: 2025
venue: "Diagnostics (MDPI)"
doi: "10.3390/diagnostics15202559"
ara_version: "1.0"
grounding: abstract-only
domain: "Explainable AI / medical neuroimaging / Alzheimer's disease severity classification from brain MRI"
keywords: [Alzheimer's disease, explainable AI, XRAI, deep learning, brain MRI, MobileNet-V3, EfficientNet-B4, ResNet-50, severity classification, Gradio]
claims_summary:
  - "MobileNet-V3 Large attains the highest AD-severity classification accuracy among the three tested CNNs (99.18% augmented test set; 99.47% original dataset)."
  - "MobileNet-V3 Large uses the fewest parameters (4.2M), making it the most computationally efficient and clinically suitable of the three architectures."
  - "XRAI region-based attribution maps align with known neuroanatomical patterns of AD progression, enhancing clinical interpretability."
  - "The Gradio web interface delivers sub-20-second inference with high classification confidence across all four AD severity levels."
  - "This is the first systematic integration of XRAI into AD severity classification using MRI and deep learning."
abstract: "Background: Alzheimer's disease (AD) is a progressive neurodegenerative condition marked by cognitive decline and memory loss. Despite advancements in AI-driven neuroimaging analysis for AD detection, clinical deployment remains limited due to challenges in model interpretability and usability. Explainable AI (XAI) frameworks such as XRAI offer potential to bridge this gap by providing clinically meaningful visualizations of model decision-making. Methods: This study developed a comprehensive, clinically deployable AI system for AD severity classification using 2D brain MRI data. Three deep learning architectures MobileNet-V3 Large, EfficientNet-B4, and ResNet-50 were trained on an augmented Kaggle dataset (33,984 images across four AD severity classes). The models were evaluated on both augmented and original datasets, with integrated XRAI explainability providing region-based attribution maps. A web-based clinical interface was built using Gradio to deliver real-time predictions and visual explanations. Results: MobileNet-V3 achieved the highest accuracy (99.18% on the augmented test set; 99.47% on the original dataset), while using the fewest parameters (4.2M), confirming its efficiency and suitability for clinical use. XRAI visualizations aligned with known neuroanatomical patterns of AD progression, enhancing clinical interpretability. The web interface delivered sub-20 second inference with high classification confidence across all AD severity levels, successfully supporting real-world diagnostic workflows. Conclusion: This research presents the first systematic integration of XRAI into AD severity classification using MRI and deep learning. The MobileNet-V3-based system offers high accuracy, computational efficiency, and interpretability through a user-friendly clinical interface. These contributions demonstrate a practical pathway toward real-world adoption of explainable AI for early and accurate Alzheimer's disease detection."
---

# An Explainable Web-Based Diagnostic System for Alzheimer's Disease Using XRAI and Deep Learning on Brain MRI

> **GROUNDING NOTE — abstract-only compile.** Full text was unavailable: the provided
> `paper.pdf` did not contain this paper. The file downloaded from the Europe PMC render
> endpoint (cited in `sources.yaml` as PMC12564920) is a **different article** — Afifi et al.,
> *Vision and convolutional transformers for Alzheimer's disease diagnosis: a systematic review*,
> Brain Informatics (2026) 13:1, DOI 10.1186/s40708-025-00286-7 (92-page review; 0 mentions of
> XRAI/Gradio/Aksoy/Daou, 93 mentions of "Afifi"). No licit OA copy of the target Aks25 article
> could be verified for this compile. This ARA is therefore grounded ONLY in the verified
> abstract (`metadata.json` / `metadata.md`) and the verified discovered sources
> (`sources.yaml`). No figures or tables were extracted (they belong to a different paper).
> Method-level detail beyond the abstract is marked "Not available from provided input (no full
> text)". No numbers are fabricated; every number below is quoted verbatim from the abstract or
> from the verified dataset record in `sources.yaml`.

## Overview

The paper describes a clinically deployable, explainable deep-learning system for classifying
Alzheimer's disease (AD) severity from 2D brain MRI. Three CNN architectures (MobileNet-V3 Large,
EfficientNet-B4, ResNet-50) were trained on an augmented Kaggle MRI dataset (33,984 images, four
severity classes) and evaluated on both the augmented and the original datasets. XRAI — a
region-based explainable-AI attribution method — was integrated to produce clinically meaningful
saliency maps, and a Gradio web interface was built for real-time prediction and visual
explanation. Per the abstract, MobileNet-V3 Large gave the best accuracy (99.18% augmented test;
99.47% original) with the fewest parameters (4.2M), sub-20-second inference, and XRAI maps
consistent with known AD neuroanatomy. The authors frame this as the first systematic integration
of XRAI into MRI-based AD severity classification.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight (abstract-level) |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) |
| [concepts.md](logic/concepts.md) | 8 key technical terms |
| [experiments.md](logic/experiments.md) | 4 directional verification plans (E01–E04) |
| [related_work.md](logic/related_work.md) | Typed dependency graph (RW01–RW07) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |
| [solution/method.md](logic/solution/method.md) | Abstract-level method reconstruction |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Runtime/framework/data-source reproducibility record | — |
| [data/dataset.md](data/dataset.md) | Kaggle Augmented Alzheimer MRI Dataset (verified) | C01, C02 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 9-node reconstructed research DAG (mostly inferred) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index — no tables/figures extracted (no full text; N/A) |
