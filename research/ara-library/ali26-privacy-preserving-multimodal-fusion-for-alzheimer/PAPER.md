---
title: "Privacy-preserving multimodal fusion for Alzheimer's staging: A federated vision transformer framework with explainable AI"
authors: ["Marwa Ben Gara Ali", "Abir Smiti"]
year: 2026
venue: "Computerized Medical Imaging and Graphics (official journal of the Computerized Medical Imaging Society)"
doi: "10.1016/j.compmedimag.2026.102730"
ara_version: "1.0"
grounding: abstract-only
domain: "Federated learning / medical imaging AI — Alzheimer's disease staging"
keywords: ["federated learning", "Alzheimer's disease staging", "multimodal fusion", "Swin-UNet transformer", "Low-Rank Adaptation (LoRA)", "explainable AI", "privacy-preserving machine learning", "radiomics", "plasma biomarkers", "ADNI"]
claims_summary:
  - "A privacy-preserving federated framework fusing four modalities in a Swin-UNet transformer achieves 80.7% balanced accuracy on an ADNI four-client federation, close to the 82.1% centralized upper bound."
  - "LoRA plus dynamic token gating cuts federated communication overhead by 99% (to 140 KB/round) versus standard federated averaging."
  - "A hierarchical attention fusion mechanism dynamically weights modalities by predictive uncertainty."
  - "A fuzzy-rough hybrid explainability pipeline yields consensus, cross-site interpretations (Dice similarity 0.84) without sharing raw data."
  - "The framework shows superior robustness to simulated domain shifts relative to standard federated baselines."
abstract: "Accurate, early-stage staging of Alzheimer's disease (AD) is critical for therapeutic intervention but is hampered by data privacy regulations, multimodal data heterogeneity, and the \"black-box\" nature of complex Artificial Intelligence (AI) models. To address these interconnected challenges, we introduce a novel, privacy-preserving federated learning framework for robust and interpretable AD staging. Our method integrates four clinically relevant modalities, 3D structural Magnetic Resonance Imaging (MRI), Image Biomarker Standardization Initiative (IBSI)-compliant radiomics, cognitive assessments, and U.S. Food and Drug Administration (FDA) cleared plasma biomarkers, within a parameter-efficient Swin-UNet transformer architecture. Key innovations include: (1) Low-Rank Adaptation (LoRA) and dynamic token gating, reducing communication overhead by 99% (to 140 KB/round) compared to standard federated averaging; (2) A hierarchical attention fusion mechanism that dynamically weights modalities based on predictive uncertainty; and (3) A fuzzy-rough hybrid explainability pipeline that synthesizes client-specific saliency maps into a consensus-driven, clinically coherent interpretation without sharing raw data. Evaluated on a stratified four-client federation derived from the Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort, our framework achieved a state-of-the-art balanced accuracy of 80.7%, closely approaching the centralized upper bound (82.1%) while demonstrating superior robustness to simulated domain shifts and consistent cross-site interpretability (Dice similarity: 0.84). This work establishes a foundational blueprint for the next generation of healthcare AI systems that are simultaneously accurate, efficient, privacy-preserving, and trustworthy, enabling scalable collaboration across distributed clinical networks."
---

# Privacy-preserving multimodal fusion for Alzheimer's staging: A federated vision transformer framework with explainable AI

> **Grounding: abstract-only.** The full text of this paper was unavailable (no licit open-access
> copy — Unpaywall `oa_status: closed`, Europe PMC "Subscription required", `inPMC: N`; publisher
> is Elsevier, PII S0895-6111(26)00033-9, PMID 41723900). This ARA is reconstructed from the
> bibliographic metadata and abstract only. Sections that the abstract does not support are marked
> "Not available from provided input (no full text)". No numbers, tables, or figures were fabricated;
> the only quantitative values present are those stated verbatim in the abstract.

## Overview

The paper proposes a privacy-preserving federated learning framework for staging Alzheimer's
disease (AD). It fuses four clinically relevant modalities — 3D structural MRI, IBSI-compliant
radiomics, cognitive assessments, and FDA-cleared plasma biomarkers — inside a parameter-efficient
Swin-UNet transformer. Three innovations are highlighted: (1) Low-Rank Adaptation (LoRA) with
dynamic token gating to cut federated communication overhead by 99% (to 140 KB/round); (2) a
hierarchical attention fusion mechanism that weights modalities by predictive uncertainty; and (3)
a fuzzy-rough hybrid explainability pipeline that builds consensus, cross-site interpretations
without exchanging raw data. On a stratified four-client federation derived from the ADNI cohort,
the framework reports a balanced accuracy of 80.7% (versus an 82.1% centralized upper bound), with
consistent cross-site interpretability (Dice similarity 0.84) and improved robustness to simulated
domain shifts.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight (abstract-grounded) |
| [claims.md](logic/claims.md) | 5 falsifiable claims (C01–C05) |
| [concepts.md](logic/concepts.md) | 10 technical concepts |
| [experiments.md](logic/experiments.md) | 4 declarative verification plans (E01–E04), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph incl. ADNI data source |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, boundary conditions, limitations |
| [solution/architecture.md](logic/solution/architecture.md) | Framework components as described in the abstract |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Reproducibility; data sources (ADNI, controlled access) | C01 |

No code was located for this work (no repository found via web search). No `src/execution/`
stubs are produced — the method is available only in prose from the abstract (Rule 14).

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 10-node reconstructed research DAG (all `inferred`) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index — no full text, so no tables/figures extracted (completeness N/A) |
