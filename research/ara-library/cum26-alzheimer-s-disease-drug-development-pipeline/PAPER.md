---
title: "Alzheimer's disease drug development pipeline: 2026"
authors: ["Jeffrey L. Cummings", "Yadi Zhou", "Yuxin Yang", "Kate Zhong", "Jorge Fonseca", "Amanda Leisgang Osse", "Feixiong Cheng"]
year: 2026
venue: "Alzheimer's & Dementia: Translational Research & Clinical Interventions (TRCI) 12(2):e70251"
doi: "10.1002/trc2.70251"
ara_version: "1.0"
domain: "Clinical drug development / neurology — annual survey of the Alzheimer's disease therapeutic pipeline"
keywords: ["Alzheimer's disease", "drug development pipeline", "clinical trials", "CADRO", "disease-targeting therapy", "symptom-targeted therapy", "amyloid", "tau", "inflammation", "repurposed drugs", "biomarkers", "ClinicalTrials.gov"]
claims_summary:
  - "On the Index Date of 1 January 2026 the active AD pipeline comprised 158 drugs in 192 clinical trials."
  - "By therapeutic purpose, 39% are small-molecule DTTs, 34% biologic DTTs, 18% cognition-enhancing STTs, and 10% NPS-targeting STTs (73% DTTs overall)."
  - "Trials are distributed across phases: 36 drugs/54 trials in Phase 3, 84/89 in Phase 2, 45/49 in Phase 1."
  - "Currently active trials require 54,728 participants, of which 38,417 (70%) are needed for Phase 3."
  - "The biopharmaceutical industry sponsors 59% of all AD trials, including 72% of Phase 3 trials."
  - "Repurposed agents represent 35% of drugs in trials (38% of trials)."
  - "17 CADRO pathophysiology categories are targeted; neurotransmitter receptors (24%), inflammation/immune (18%) and amyloid (16%) are the most common."
  - "The pipeline grew from 182 trials/138 drugs (2025) to 192/158 (2026), a ~35–40% increase in trials and agents since 2017."
  - "50% of trials use a biomarker for eligibility and 27% use a biomarker as a primary outcome."
  - "Over 2017–2026 the amyloid-targeting share of the pipeline fell from ~33% to ~20% while tau and inflammation/immune each rose from ~6% to ~20%."
abstract: "INTRODUCTION: Discovery and development of new therapies for Alzheimer's disease (AD) are urgently needed to address the world's growing population of individuals on the AD pathophysiological continuum. Clinicaltrials.gov is a resource for studying drugs in development for treatment of AD. RESULTS: There are currently 158 drugs in 192 AD trials. Of the agents in trials, 39% are small molecule disease targeting therapies (DTTs); 34% are biologic DTTs; 18% are cognition enhancing symptom targeted therapies (STTs); and 10% are STTs being developed to treat neuropsychiatric symptoms of AD. Currently active trials require 54,728 participants of which 38,417 are in Phase 3. The biopharmaceutical industry sponsors 59% of AD trials including 72% of Phase 3 trials. Repurposed drugs represent 35% of the drugs in trials. DISCUSSION: The AD drug development pipeline has a growing number of trials and drugs in trials. A diverse array of AD pathophysiological processes is being addressed by drugs in trials."
---

# Alzheimer's disease drug development pipeline: 2026

## Overview

This is the annual review (a continuation of the Cummings-led AD pipeline series) of the entire
Alzheimer's disease drug development pipeline as registered on ClinicalTrials.gov, using an Index
Date of 1 January 2026. It is a **survey / registry-analysis paper**, not a single experiment:
the authors enumerate every active AD trial and candidate drug, classify each agent by therapeutic
purpose (disease-targeting therapy [DTT] vs symptom-targeted therapy [STT]) and by Common
Alzheimer's Disease Research Ontology (CADRO) mechanistic category, and report the composition of
the pipeline by phase, mechanism, sponsor, geography, biomarker use, participant demand, and
repurposing status. The 2026 pipeline holds **158 drugs across 192 trials** (36 drugs/54 trials in
Phase 3; 84/89 in Phase 2; 45/49 in Phase 1). Its central findings concern the *composition and
trajectory* of the pipeline rather than the efficacy of any single drug.

Claims are therefore stated at the level the review supports — proportions and counts of the
pipeline's constituents — and the "experiments" describe the counting/classification methodology
directionally. Exact numbers are preserved in the evidence layer (Tables 1–3 enumerate every agent;
Figures 1–5 summarize the composition and 10-year trajectory).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (unmet need, growth) → gaps → survey rationale |
| [claims.md](logic/claims.md) | 10 falsifiable claims (C01–C10) about pipeline composition/trajectory |
| [concepts.md](logic/concepts.md) | 9 core terms (DTT, STT, CADRO, MoA, repurposed drug, Index Date, active trial, biomarker context of use, AD continuum) |
| [experiments.md](logic/experiments.md) | 8 declarative counting/classification analyses (E01–E08) |
| [related_work.md](logic/related_work.md) | 10 references + data-source dependency graph (ClinicalTrials.gov, alzpipeline.com, AD Workbench, DrugBank) |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations, assumptions, boundary conditions |
| [solution/study_design.md](logic/solution/study_design.md) | Data collection, classification rules, inclusion/exclusion methodology |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment; data sources with access type + IDs; flagship NCTs |
| [data/dataset.md](data/dataset.md) | Provenance of the registry-derived pipeline dataset |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG of the survey's analysis questions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 3 tables + 5 figures |
| [tables/table1.md](evidence/tables/table1.md) | Table 1 — 36 Phase 3 agents (54 trials) |
| [tables/table2.md](evidence/tables/table2.md) | Table 2 — 84 Phase 2 agents (89 trials) |
| [tables/table3.md](evidence/tables/table3.md) | Table 3 — 45 Phase 1 agents (49 trials) |
| [figures/figure1.md](evidence/figures/figure1.md) | Figure 1 — radial map of all agents by phase and CADRO class |
| [figures/figure2.md](evidence/figures/figure2.md) | Figure 2 — Phase 3 MoA by therapeutic purpose and CADRO |
| [figures/figure3.md](evidence/figures/figure3.md) | Figure 3 — CADRO categories by phase (stacked bar) |
| [figures/figure4.md](evidence/figures/figure4.md) | Figure 4 — Phase 2 MoA by therapeutic purpose and CADRO |
| [figures/figure5.md](evidence/figures/figure5.md) | Figure 5 — 10-year trajectory of trials/agents and target-class shares |
