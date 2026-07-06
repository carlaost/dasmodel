---
title: "Microglial mechanisms drive amyloid-β clearance in immunized patients with Alzheimer’s disease"
authors: ["Lynn van Olst", "Brooke Simonton", "Alex J. Edwards", "Anne V. Forsyth", "Jake Boles", "P. Jamshidi", "Thomas J Watson", "Nate Shepard", "Talia Krainc", "B. Argue", "Ziyang Zhang", "Joshua Kuruvilla", "Lily Camp", "Mengwei Li", "Hang Xu", "Jeanette L. Norman", "Joshua Cahan", "Robert J. Vassar", "Jinmiao Chen", "Rudolph J Castellani", "James A R Nicoll", "D. Boche", "David Gate"]
year: 2025
venue: "Nature medicine"
doi: "10.1038/s41591-025-03574-1"
ara_version: "1.0"
grounding: abstract-only
domain: "Alzheimer's disease immunotherapy / neuroimmunology / spatial transcriptomics"
keywords: ["Alzheimer's disease", "amyloid-β", "Aβ immunization", "microglia", "spatial transcriptomics", "single-cell RNA sequencing", "lecanemab", "TREM2", "APOE", "complement signaling"]
claims_summary:
  - "Spatial transcriptomics identifies distinct microglial states associated with Aβ clearance in immunized AD brain."
  - "High-resolution spatial transcriptomics with single-cell RNA sequencing identifies transcriptional pathways involved in Aβ removal after lecanemab treatment."
  - "TREM2 and APOE are upregulated in microglia across immunization approaches and correlate positively with antibody responses and Aβ removal."
  - "Complement signaling in brain myeloid cells contributes to Aβ clearance after immunization."
  - "The identified transcriptional mechanisms suggest potential molecular targets for enhancing Aβ-targeted immunotherapies."
abstract: "Alzheimer’s disease (AD) therapies utilizing amyloid-β (Aβ) immunization have shown potential in clinical trials. Yet, the mechanisms driving Aβ clearance in the immunized AD brain remain unclear. Here, we use spatial transcriptomics to explore the effects of both active and passive Aβ immunization in the AD brain. We compare actively immunized patients with AD with nonimmunized patients with AD and neurologically healthy controls, identifying distinct microglial states associated with Aβ clearance. Using high-resolution spatial transcriptomics alongside single-cell RNA sequencing, we delve deeper into the transcriptional pathways involved in Aβ removal after lecanemab treatment. We uncover spatially distinct microglial responses that vary by brain region. Our analysis reveals upregulation of the triggering receptor expressed on myeloid cells 2 (TREM2) and apolipoprotein E (APOE) in microglia across immunization approaches, which correlate positively with antibody responses and Aβ removal. Furthermore, we show that complement signaling in brain myeloid cells contributes to Aβ clearance after immunization. These findings provide new insights into the transcriptional mechanisms orchestrating Aβ removal and shed light on the role of microglia in immune-mediated Aβ clearance. Importantly, our work uncovers potential molecular targets that could enhance Aβ-targeted immunotherapies, offering new avenues for developing more effective therapeutic strategies to combat AD. Spatial transcriptomics reveals distinct microglial mechanisms driving amyloid-β clearance in both passively and actively immunized patients with Alzheimer’s disease."
---

# Microglial mechanisms drive amyloid-β clearance in immunized patients with Alzheimer’s disease

> **Grounding: abstract-only.** No full-text PDF, figures, tables, appendices, sample sizes, raw measurements, or code were provided. This ARA is compiled only from `metadata.json` and `metadata.md`. Fields not supported by those inputs are marked "Not available from provided input."

## Overview

This paper studies amyloid-β (Aβ) immunization in Alzheimer’s disease (AD), focusing on why and how Aβ is cleared in immunized human brain tissue. The abstract reports spatial transcriptomics analyses spanning active and passive immunization, comparisons against nonimmunized AD and neurologically healthy controls, and deeper profiling after lecanemab treatment using high-resolution spatial transcriptomics with single-cell RNA sequencing.

The abstract supports a microglial mechanism-centered account: distinct microglial states are associated with Aβ clearance; microglial responses vary by brain region; TREM2 and APOE are upregulated across immunization approaches and positively correlate with antibody responses and Aβ removal; and complement signaling in brain myeloid cells contributes to post-immunization Aβ clearance.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations, gaps, key insight, assumptions from abstract/metadata |
| [claims.md](logic/claims.md) | 5 abstract-grounded claims (C01-C05) |
| [concepts.md](logic/concepts.md) | 10 key technical concepts |
| [experiments.md](logic/experiments.md) | 4 directional analysis plans (E01-E04) |
| [related_work.md](logic/related_work.md) | Abstract-level dependency graph; no reference list available |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and missing full-text details |
| [solution/study_design.md](logic/solution/study_design.md) | Study design reconstructable from the abstract |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Available data modalities and unavailable implementation details | C01-C04 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 5-node source-bounded research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index; no tables or figures available from provided input |
