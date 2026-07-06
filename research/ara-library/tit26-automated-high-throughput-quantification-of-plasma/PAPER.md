---
title: "Automated high-throughput quantification of plasma p-tau217 and APOE-ε4 for Alzheimer's disease diagnosis and cognitive decline in a memory cohort"
authors: ["Jochen Titeca", "Marta Scarioni", "Matthijs Oyaert", "Tim Van Langenhove"]
year: 2026
venue: "Alzheimer's Research & Therapy (2026) 18:99"
doi: "10.1186/s13195-026-01996-8"
ara_version: "1.0"
domain: "Clinical neurology / laboratory medicine — blood-based Alzheimer's disease biomarkers; diagnostic-accuracy and assay method-comparison study"
keywords: ["Alzheimer's disease", "blood biomarkers", "plasma p-tau217", "p-tau181", "APOE-ε4", "amyloid-β42/40", "diagnostic accuracy", "AUC", "two-cut-off grey zone", "cognitive decline"]
claims_summary:
  - "Elecsys p-tau217 discriminates AD vs non-AD with AUC 0.939 (cut-off 0.371 pg/mL; sens 92.2%, spec 89.2%)"
  - "Elecsys p-tau217 comparable to Lumipulse p-tau217 (0.939 vs 0.950; DeLong p=0.485)"
  - "Elecsys p-tau217 significantly outperforms Elecsys p-tau181 (0.939 vs 0.903; p=0.043)"
  - "Adding APOE-ε4 raises Elecsys p-tau217 AUC to 0.970 (p=0.02) and shrinks grey zone 20.0%→11.0%"
  - "Aβ42/Aβ42-40 adjustment gives no significant AUC gain (0.950 vs 0.957) and only modest grey-zone reduction"
  - "Two-cut-off grey zones: 19.9% (Elecsys 217), 11.9% (Lumipulse 217), 33.2% (Elecsys 181)"
  - "The two p-tau217 assays are strongly correlated (rs=0.88) but with proportional/systematic bias (slope 1.363, intercept 0.113)"
  - "Higher baseline p-tau217 relates to lower baseline MoCA and a non-significant faster-decline trend (p=0.07)"
  - "p-tau217 not significantly affected by age, sex, renal function, Fazekas, or CAA"
  - "Elecsys p-tau assays: imprecision 0.5–3.8% (181) / 0.5–8.6% (217); LLOQ 0.32 / 0.10 pg/mL"
  - "Discordant CSF (A+T−N−) profiles are heterogeneous with elevated plasma p-tau217 in a subset"
abstract: "Background: Blood-based biomarkers could improve the precision of Alzheimer's disease (AD) clinical diagnosis and expand access to targeted treatments. We evaluated the diagnostic accuracy of plasma Elecsys p-tau217 (Roche) and compared it with Elecsys p-tau181 (Roche) and Lumipulse p-tau217 (Fujirebio), assessed the added value of APOE-ε4 carrier status, plasma Aβ42 and Aβ42/40, and evaluated associations with longitudinal cognition. Methods: 187 patients from the CCUG biobank, classified as AD (n=103) or non-AD cognitive disorders (n=84) by CSF biomarkers. Plasma Elecsys p-tau181, p-tau217, APOE-ε4 measured on Roche cobas pro e801; p-tau217, Aβ42, Aβ40 on Fujirebio LUMIPULSE G1200. ROC analyses and single/two-cut-off strategies (95% sensitivity/specificity). Results: Elecsys p-tau217 AUC 0.939, comparable to Lumipulse p-tau217 (0.950; p=0.485) and higher than Elecsys p-tau181 (0.903; p=0.043). Two-cut-off intermediate proportions 19.9%/11.9%/33.2%. Adding APOE-ε4 to Elecsys p-tau217 improved AUC (0.970, p=0.02) and reduced intermediates to 11.0%. Aβ42 adjustment did not significantly increase AUC. Higher baseline p-tau217 associated with lower baseline MoCA and a decline trend (p=0.07); age, sex, renal function, Fazekas, CAA not significantly associated. Conclusion: Automated Elecsys p-tau217 shows excellent AD diagnostic accuracy; APOE-ε4 further improves classification while Aβ42 adjustment adds little."
---

# Automated high-throughput quantification of plasma p-tau217 and APOE-ε4 for Alzheimer's disease diagnosis and cognitive decline in a memory cohort

## Overview
This is a retrospective, single-centre diagnostic-accuracy and assay method-comparison study of 187
memory-clinic patients from the Cognitive Centre Ghent University (CCUG) biobank, classified as AD
(n=103) or non-AD (n=84) by a CSF-biomarker reference standard. It establishes the diagnostic
performance of plasma p-tau217 measured on the fully automated, high-throughput Roche Elecsys (ECLIA)
platform, benchmarks it head-to-head against the Fujirebio Lumipulse (CLEIA) p-tau217 assay and
Elecsys p-tau181, and evaluates the added value of blood-based APOE-ε4 carrier status and amyloid
(Aβ42, Aβ42/40) measures. Diagnostic classification uses both a Youden single cut-off and a two-cut-off
"grey-zone" strategy (95% sensitivity/specificity thresholds). Secondary analyses cover analytical
validation, clinical-cofactor influence, discordant-CSF profiles, and an exploratory longitudinal
MoCA-decline analysis. Elecsys p-tau217 achieved AUC 0.939 — comparable to Lumipulse p-tau217 and
superior to Elecsys p-tau181 — and adding APOE-ε4 raised the AUC to 0.970 while halving the
intermediate zone.

No analysis code or public dataset accession exists for this single-cohort study; the sole data
source is the request-access CCUG biobank (Ghent University Hospital).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (O1–O4) → gaps (G1–G3) → key insight → assumptions |
| [claims.md](logic/claims.md) | 11 falsifiable claims (C01–C11) with grounded number sources |
| [concepts.md](logic/concepts.md) | 13 technical concepts (p-tau217/181, APOE-ε4, AUC, Youden, two-cut-off, DeLong, Passing–Bablok, Bland–Altman, AT(N), LLOQ, MoCA, Aβ42/40) |
| [experiments.md](logic/experiments.md) | 9 analysis plans (E01–E09), directional only |
| [related_work.md](logic/related_work.md) | 13 full RW blocks + 41-row footprint table (53 refs total) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, author-stated limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, reference standard, ethics, endpoints, power |
| [solution/assay_and_analysis.md](logic/solution/assay_and_analysis.md) | Assay platforms/lots, analytical validation, full statistical pipeline, cut-off outputs |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [src/environment.md](src/environment.md) | Software (SPSS 29.0, MedCalc 15.6.1), instruments, CCUG data access, reagent lots; no code released | — |
| [data/dataset.md](data/dataset.md) | CCUG biobank provenance, access=request, variables, preprocessing/QC | C09, C10 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 13-node research DAG (1 question, 2 decisions, 9 experiments, 1 dead_end) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 3 tables + 3 figures (main text); supplementary items noted as not-in-PDF |
| [tables/table1.md](evidence/tables/table1.md) | Cohort demographics/clinical characteristics (AD vs non-AD) |
| [tables/table2.md](evidence/tables/table2.md) | Single-cut-off diagnostic performance (all assays ± APOE-ε4) |
| [tables/table3.md](evidence/tables/table3.md) | Two-cut-off diagnostic performance / % intermediates |
| [figures/figure1.md](evidence/figures/figure1.md) | Passing–Bablok + Bland–Altman method comparison |
| [figures/figure2.md](evidence/figures/figure2.md) | ROC curves for the three assays |
| [figures/figure3.md](evidence/figures/figure3.md) | Box-plot distributions by group with cut-off lines |

## Discovered sources (grounded, from sources.yaml — verified)
- **PDF**: gold OA (CC BY-NC-ND), Alzheimer's Research & Therapy, PMC13134085; downloaded from Springer.
- **Code**: none — no Code Availability statement; no GitHub/GitLab/OSF/Zenodo repo found.
- **Data**: CCUG biobank (Ghent University Hospital), access = **request** ("available from the corresponding author on reasonable request"). No public accession.
- **Clinical trials**: none — observational biobank study, no NCT/EudraCT registration.
