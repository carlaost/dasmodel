---
title: "Alzheimer’s disease patient brain extracts induce multiple pathologies in novel vascularized neuroimmune organoids for disease modeling and drug discovery"
authors: [Yanru Ji, Xiaoling Chen, Zhen Wang, Connor Joseph Meek, Jenna Lillie McLean, Yang Yang, Chongli Yuan, Jean-Christophe Rochet, Fei Liu, Ranjie Xu]
year: 2025
venue: "Molecular Psychiatry"
doi: "10.1038/s41380-025-03041-w"
ara_version: "1.0"
grounding: abstract-and-metadata-only
domain: "Neurodegenerative disease modeling - human pluripotent stem cell organoids"
keywords: [Alzheimer's disease, sporadic AD, vascularized neuroimmune organoids, hPSC, brain extracts, amyloid beta, tau, neuroinflammation, Lecanemab, drug discovery]
claims_summary:
  - "The paper reports a human hPSC-based vascularized neuroimmune organoid model containing neurons, microglia, astrocytes, and blood vessels."
  - "The paper reports that sporadic AD brain extracts induce multiple AD-like pathologies in these organoids four weeks post-exposure."
  - "The paper reports that Lecanemab treatment reduces amyloid burden while elevating vascular inflammation response in AD brain-extract-exposed organoids."
abstract: "Alzheimer’s Disease (AD) is the most common cause of dementia, afflicting 55 million individuals worldwide, with limited treatment available. Current AD models mainly focus on familial AD (fAD), which is due to genetic mutations. However, models for studying sporadic AD (sAD), which represents over 95% of AD cases without specific genetic mutations, are severely limited. Moreover, the fundamental species differences between humans and animals might significantly contribute to clinical failures for AD therapeutics that have shown success in animal models, highlighting the urgency to develop more translational human models for studying AD, particularly sAD. In this study, we developed a complex human pluripotent stem cell (hPSC)-based vascularized neuroimmune organoid model, which contains multiple cell types affected in human AD brains, including human neurons, microglia, astrocytes, and blood vessels. Importantly, we demonstrated that brain extracts from individuals with sAD can effectively induce multiple AD pathologies in organoids four weeks post-exposure, including amyloid beta (Aβ) plaque-like aggregates, tau tangle-like aggregates, neuroinflammation, elevated microglial synaptic pruning, synapse/neuronal loss, and impaired neural network activity. Proteomics analysis also revealed disrupted AD-related pathways in our vascularized AD neuroimmune organoids. Furthermore, after treatment with Lecanemab, an FDA-approved antibody drug targeting Aβ, AD brain extracts exposed organoids showed a significant reduction of amyloid burden, along with an elevated vascular inflammation response. Thus, the vascularized neuroimmune organoid model provides a unique opportunity to study AD, particularly sAD, under a pathophysiological relevant three-dimensional (3D) human cell environment. It also holds great promise to facilitate AD drug development, particularly for immunotherapies."
---

# Alzheimer’s disease patient brain extracts induce multiple pathologies in novel vascularized neuroimmune organoids for disease modeling and drug discovery

> **Grounding note: abstract/metadata only.** No full-text PDF, figures, tables, methods, supplements, or raw data were provided. This ARA is compiled only from `metadata.json` and `metadata.md`. Fields not supported by those files are marked "Not available from provided input". No table or figure evidence files are created because no numbered source objects were available to enumerate or extract.

## Overview

This paper reports a human pluripotent stem cell (hPSC)-based vascularized neuroimmune organoid model for Alzheimer's disease (AD), especially sporadic AD (sAD). The abstract frames the need as a translational modeling gap: AD affects 55 million individuals worldwide, sAD represents over 95% of AD cases, and animal-to-human species differences may contribute to clinical failures.

The reported model contains neurons, microglia, astrocytes, and blood vessels. According to the abstract, brain extracts from individuals with sAD induce multiple AD-like pathologies in the organoids four weeks after exposure, including amyloid beta (Aβ) plaque-like aggregates, tau tangle-like aggregates, neuroinflammation, elevated microglial synaptic pruning, synapse/neuronal loss, impaired neural network activity, and disrupted AD-related proteomic pathways. The abstract also reports that Lecanemab reduced amyloid burden while elevating vascular inflammation response in AD brain-extract-exposed organoids.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, and assumptions from abstract/metadata |
| [claims.md](logic/claims.md) | 3 falsifiable claims (C01-C03) |
| [concepts.md](logic/concepts.md) | 7 key technical terms |
| [experiments.md](logic/experiments.md) | 3 directional verification plans (E01-E03) |
| [related_work.md](logic/related_work.md) | 3 source-bounded dependency entries |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and unavailable method details |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Reproducibility environment and missing artifact inventory | C01-C03 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 4-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Empty evidence ledger; no numbered tables or figures available from provided input |
