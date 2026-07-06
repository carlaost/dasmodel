---
title: "Plasma eMTBR-tau243 and %p-tau217 for Biological Staging of Alzheimer Disease"
authors: ["Gemma Salvadó", "Kanta Horie", "Nicolas R. Barthélemy", "Suzanne Schindler", "Shorena Janelidze", "Anna Orduña Dolado", "Divya Bali", "Richard Perrin", "John C. Morris", "Tammie Benzinger", "Brian A. Gordon", "Erik Stomrud", "Niklas Mattsson-Carlgren", "Sebastian Palmqvist", "Jacob W. Vogel", "Randall J. Bateman", "Rik Ossenkoppele", "Oskar Hansson"]
year: 2026
venue: "JAMA Neurology"
doi: "10.1001/jamaneurol.2026.1405"
ara_version: "1.0"
grounding: abstract-only
domain: "Alzheimer disease biomarkers / clinical neurology / plasma biomarker staging"
keywords: ["Alzheimer disease", "plasma biomarkers", "%p-tau217", "eMTBR-tau243", "biological staging", "amyloid PET", "tau PET", "BioFINDER-2", "clinical trial enrichment", "blood-based biomarkers"]
claims_summary:
  - "A plasma model combining %p-tau217 and eMTBR-tau243 shows strong concordance with a PET-based amyloid/tau biological staging scheme."
  - "The combined plasma model outperforms a %p-tau217-only model, particularly for identifying the intermediate tau stage."
  - "Advanced plasma stages align with greater clinical severity, other biomarker abnormalities, and greater neuropathologic burden."
  - "Plasma-based staging may offer a scalable, minimally invasive approach to biological stratification of Alzheimer disease (interpretive/forward-looking)."
abstract: "Key Points Question Can plasma %p-tau217 and eMTBR-tau243 be combined to approximate an amyloid and tau positron emission tomography (PET)–based Alzheimer disease biological staging scheme? Findings In 872 BioFINDER-2 participants and 156 independent Knight Alzheimer Disease Research Center participants, a plasma model combining %p-tau217 and eMTBR-tau243 showed strong concordance with PET-based biological staging and outperformed a %p-tau217–only model, particularly for identifying the intermediate tau stage. Advanced plasma stages also aligned with greater clinical severity, other biomarker abnormalities, and neuropathologic burden. Meaning Plasma-based staging may provide a scalable, minimally invasive approach to biological stratification of Alzheimer disease, with potential value for treatment selection and clinical trial enrichment."
---

# Plasma eMTBR-tau243 and %p-tau217 for Biological Staging of Alzheimer Disease

> **Grounding: abstract-only.** The full text of this article was unavailable at compile time — no
> licit open-access rendered PDF exists (green OA, CC BY-NC-ND; readable as HTML on PMC/Europe PMC,
> but Unpaywall `url_for_pdf` is null and the PMC/Europe PMC PDF endpoints return no file). This ARA
> was therefore built from the published **abstract (Key Points)** plus **verified external sources**
> (metadata + `sources.yaml`) ONLY. Numbers, figures, tables, and detailed method content that are
> not present in the abstract are marked "Not available from provided input (no full text)." No
> results have been fabricated.

## Overview

This study asks whether two plasma biomarkers — %p-tau217 (the phosphorylation-occupancy ratio of
tau at threonine-217) and eMTBR-tau243 (an extracellular microtubule-binding-region tau species
ending at residue 243) — can be combined into a blood-based model that reproduces an amyloid- and
tau-PET–based biological staging scheme for Alzheimer disease (AD). In a primary cohort of 872
BioFINDER-2 participants and an independent validation cohort of 156 Knight Alzheimer Disease
Research Center (ADRC) participants, the combined plasma model showed strong concordance with
PET-based staging and outperformed a %p-tau217-only model, most notably at the intermediate tau
stage. More advanced plasma stages were associated with greater clinical severity, other biomarker
abnormalities, and greater neuropathologic burden. The authors position plasma-based staging as a
scalable, minimally invasive route to biological stratification for treatment selection and clinical
trial enrichment.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight (abstract-grounded) |
| [claims.md](logic/claims.md) | 4 claims (C01–C04) with proof pointers |
| [concepts.md](logic/concepts.md) | 7 key technical terms |
| [experiments.md](logic/experiments.md) | 4 directional analysis plans (E01–E04) |
| [related_work.md](logic/related_work.md) | Dependency graph + folded external sources (cohorts, trial) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Study design as reconstructable from abstract |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Cohorts, data access, analytical setup (no code released) | C01–C04 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 9-node research DAG (support_level: inferred where reconstructed) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index — no full text, so no tables/figures extracted |
