---
title: "The Alzheimer's Disease Diagnosis and Plasma Phospho-Tau217 (ADAPT) study stage 1: Validating clinical cut-points against CSF and amyloid PET"
authors: [A. Keshavan, Katharine Wiltshire, Ryan Wee, Irene Gorostiaga Belio, K. Tucker, Melanie Hart, Michael P. Lunn, Michael C. B. David, Laura Rizzo, O. Sadeghi-Alavijeh, Patricia Wilson, Daniel P. Gale, Amanda J. Heslegrave, Henrik Zetterberg, Nick C. Fox, Paresh Malhotra, Jonathan M. Schott]
year: 2025
venue: "Alzheimer's & Dementia (Journal of the Alzheimer's Association)"
doi: "10.1002/alz.71147"
ara_version: "1.0"
domain: "Clinical neurology / Alzheimer's disease blood-based biomarkers — diagnostic biomarker validation"
keywords: [plasma p-tau217, Alzheimer's disease, blood biomarker, Lumipulse, ALZpath, cerebrospinal fluid, amyloid PET, diagnostic cut-points, chronic kidney disease, pre-analytical stability]
claims_summary:
  - "Lumipulse plasma p-tau217 discriminates AD with AUC 0.947 in a CSF-defined cohort (C01)."
  - "Lumipulse outperforms ALZpath on fold-change and indeterminate proportion; selected as clinical assay (C02)."
  - "Dual cut-points 0.153/0.422 pg/mL give 95% sensitivity, 97% specificity, 19.4% indeterminate in CSF cohort (C03)."
  - "Applying CSF cut-points to amyloid PET cohort raises indeterminate zone to 34.2% (C04)."
  - "Adding age/sex/creatinine/BMI does not significantly improve AUC over p-tau217 alone (C05)."
  - "Plasma p-tau217 is robust to pre-analytical handling (≤10% change) (C06)."
  - "Lumipulse p-tau217 is robust to kit lot-to-lot variability (rho > 0.95) (C07)."
  - "Sub-zero (−20°C) transport is comparable to −80°C storage (rho 0.998) (C08)."
  - "CKD elevates p-tau217 into the intermediate zone but rarely to AD-positive; no independent association after adjustment (C09)."
  - "Within-cohort cut-points outperform external Malmö cut-points (C10)."
abstract: "We validated plasma phosphorylated tau (p-tau)217 cut-points for Alzheimer's disease (AD) diagnosis using two commercial assays in two biomarker-defined cohorts and examined influences of pre-analytical factors and chronic kidney disease (CKD) on p-tau217 concentrations. Lumipulse (Fujirebio) and ALZpath (Quanterix) assays quantified plasma p-tau217 in symptomatic patients (AD status by CSF n = 257; amyloid PET n = 76). ROC analyses established ≥ 95% sensitivity/specificity cut-points. Separate cohorts evaluated pre-analytical handling/transport (n = 40/10) and cognitively normal (CN)-CKD individuals (n = 58). Diagnostic accuracy was similar (AUC Lumipulse 0.947; ALZpath 0.940). Lumipulse achieved 95% sensitivity and 97% specificity using dual cut-points (0.153/0.422 pg/mL), producing indeterminate results in 19.4% (CSF defined) and 34.2% (PET defined). P-tau217 was stable across handling conditions and kit lots, and mostly low-to-intermediate in CN-CKD. Lumipulse plasma p-tau217, now available in a UKAS-accredited NHS laboratory, will be used in a randomized trial of p-tau217 result disclosure in memory services."
---

# The Alzheimer's Disease Diagnosis and Plasma Phospho-Tau217 (ADAPT) study stage 1

## Overview
This is **stage 1** of the UK multi-center ADAPT programme: an observational diagnostic
biomarker-validation study. It derives and validates clinically usable plasma p-tau217 cut-points
for two commercial assays (Lumipulse/Fujirebio and ALZpath/Quanterix) against two independent
reference standards — CSF Aβ42/Aβ40 (derivation cohort, n = 257) and amyloid PET visual read
(validation cohort, n = 76) — using a **dual cut-point** scheme (lower = 95% sensitivity,
upper = maximized/95% specificity, with an intermediate "indeterminate" zone). It further
characterizes the robustness of plasma p-tau217 to pre-analytical handling (n = 40) and transport
(n = 10), assay kit lot-to-lot variability, and the confounding influence of chronic kidney disease
(CN-CKD cohort, n = 58) and BMI. The Lumipulse assay (dual cut-points 0.153/0.422 pg/mL) was
selected and implemented in a UKAS-accredited NHS laboratory, to be used in the planned ADAPT
stage-3 randomized controlled trial of result disclosure. There is **no code repository**; all data
are UK cohorts with controlled/on-request access. Funding: ARUK-BBC2023-002 (Blood Biomarker Challenge).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight (dual cut-point) → assumptions |
| [claims.md](logic/claims.md) | 10 falsifiable diagnostic claims (C01–C10) with grounded numbers |
| [concepts.md](logic/concepts.md) | 9 technical concepts (p-tau217, dual cut-point, assays, CKD/eGFR, fold-change, …) |
| [experiments.md](logic/experiments.md) | 9 analysis plans (E01–E09), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph (RW01–RW09 + brief footprint) + cohort data-source table |
| [solution/study_design.md](logic/solution/study_design.md) | Full observational study design, cohorts, assays, workflow |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, 9 stated limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | Recommended sample-handling protocol (H01–H05) |

### Physical / Artifact Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [src/environment.md](src/environment.md) | Software (R, Python 3.6), assay platforms, cohorts (access=request), funding | all |
| [data/dataset.md](data/dataset.md) | 4 cohorts: provenance, ethics IDs, size, variables, access | C01–C10 |
| [data/preprocessing.md](data/preprocessing.md) | Sample processing, AD-status label derivation, eGFR/CKD staging, stats | C01–C10 |

*No `src/execution/` code stub: the paper describes no algorithm/code and no repository exists (Rule 14).*

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 21-node research DAG (7 questions, 8 experiments, 3 decisions, 3 dead ends; all explicit) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 3 tables + 2 figures (main text); supporting-info S-objects accounted for |
| [tables/table1.md](evidence/tables/table1.md) | Participant demographics (CSF + PET cohorts) |
| [tables/table2.md](evidence/tables/table2.md) | ROC AUCs ± covariates |
| [tables/table3.md](evidence/tables/table3.md) | Cut-point performance (derivation + validation) |
| [figures/figure1.md](evidence/figures/figure1.md) | p-tau217 by AD/non-AD/CKD stage |
| [figures/figure2.md](evidence/figures/figure2.md) | Relative change across pre-analytical conditions |
