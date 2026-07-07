---
title: "Donanemab in early symptomatic Alzheimer's disease: results from the TRAILBLAZER-ALZ 2 long-term extension"
authors: [Jennifer A. Zimmer, John R. Sims, Cynthia D. Evans, Emel Serap Monkul Nery, Hong Wang, Alette M. Wessels, Giulia Tronchin, Shoichiro Sato, Lars Lau Raket, Scott W. Andersen, Christophe Sapin, Marie-Ange Paget, Ivelina Gueorguieva, Paul Ardayfio, Rashna Khanna, Dawn A. Brooks, Brandy R. Matthews, Mark A. Mintun]
year: 2025
venue: "The Journal of Prevention of Alzheimer's Disease"
doi: "10.1016/j.tjpad.2025.100446"
ara_version: "1.0"
domain: "Clinical trial long-term extension report — anti-amyloid monoclonal antibody (donanemab) in early symptomatic Alzheimer's disease, phase 3 (TRAILBLAZER-ALZ 2), external-control comparative efficacy + descriptive safety analysis"
keywords: [donanemab, Alzheimer's disease, amyloid, TRAILBLAZER-ALZ 2, long-term extension, CDR-SB, CDR-Global, ADNI external control, limited-duration dosing, ARIA, amyloid reaccumulation, propensity score weighting]
claims_summary:
  - "Early-start donanemab slowed CDR-SB progression vs a weighted ADNI external control by −1.2 points (95% CI, −1.7 to −0.7) at 3 years (36 months)."
  - "Delayed-start donanemab slowed CDR-SB progression vs the weighted ADNI control by −0.8 points (95% CI, −1.3 to −0.3) 76 weeks after donanemab initiation."
  - "Early-start participants had a 27% lower risk of progressing to the next CDR-Global disease stage than delayed-start participants (hazard ratio=0.73 [95% CI, 0.62–0.86]; p<0.001) — described by the authors as the best evidence of clinical meaningfulness from the LTE data."
  - "Amyloid plaque reduction was robust and similarly sized regardless of early- or delayed-start timing (86.96 [0.92] CL vs 86.01 [0.89] CL at a matched 76 weeks post-initiation); >75% of participants in both groups achieved amyloid clearance (<24.1 CL) by 76 weeks post-initiation."
  - "Combining LTE data with three earlier donanemab studies, amyloid plaque reaccumulation after treatment discontinuation was estimated at 2.4 CL/year, described as comparable to the natural history of the disease."
  - "No new safety signals were observed during the LTE versus the established donanemab safety profile; two previously reported deaths occurred during the LTE (one ARIA-E, one intracranial hemorrhage following thrombolytic administration)."
  - "All analyses were exploratory and not controlled for multiplicity (§2.5); the LTE has no internal placebo control, so efficacy is assessed against an external, propensity-score-weighted ADNI comparator cohort."
abstract: "Background: Donanemab significantly slowed clinical progression in participants with early symptomatic Alzheimer's disease (AD) during the 76-week placebo-controlled period of TRAILBLAZER-ALZ 2. Methods: Participants who completed the placebo-controlled period were eligible for the 78-week, double-blind, long-term extension (LTE). Early-start participants were randomized to donanemab in the placebo-controlled period. Delayed-start participants (randomized to placebo) started donanemab in the LTE. Participants who met amyloid treatment course completion criteria were switched to placebo. An external control cohort comprised participants from the AD Neuroimaging Initiative (ADNI). Results: At 3 years, donanemab slowed disease progression on the Clinical Dementia Rating Scale (CDR)-Sum of Boxes (CDR-SB) in early-start participants versus a weighted ADNI control (-1.2 points; 95% confidence interval [CI], -1.7, -0.7). Seventy-six weeks after initiating donanemab, delayed-start participants also demonstrated slower CDR-SB progression versus a weighted ADNI control (-0.8 points; 95% CI, -1.3, -0.3). Participants who completed treatment by 52 weeks demonstrated similar slowing of CDR-SB progression at 3 years. Compared with delayed-start participants, early-start participants demonstrated a significantly lower risk of disease progression on the CDR-Global over 3 years (hazard ratio=0.73; p < 0.001). In both groups, >75% of participants assessed by positron emission tomography 76 weeks after starting donanemab achieved amyloid clearance (<24.1 Centiloids). The addition of LTE data to prior modeling predicted a median reaccumulation rate of 2.4 Centiloids/year. No new safety signals were observed compared to the established donanemab safety profile. Conclusions: Over 3 years, donanemab-treated participants with early symptomatic AD demonstrated increasing clinical benefits and a consistent safety profile, with limited-duration dosing. Trial registration: ClinicalTrials.gov identifier NCT04437511"
---

# Donanemab in Early Symptomatic Alzheimer's Disease: Results from the TRAILBLAZER-ALZ 2 Long-Term Extension

## Overview

This is a **phase 3 clinical-trial long-term extension (LTE) report** (not a computational/ML
paper) describing the 78-week, participant- and investigator-blinded LTE of TRAILBLAZER-ALZ 2
(NCT04437511), a randomized, double-blind, placebo-controlled trial of donanemab in early
symptomatic Alzheimer's disease. The LTE extends the pivotal 76-week placebo-controlled trial
(Sims et al. 2023) to 154 weeks (~3 years) total observation. Because the LTE has no internal
placebo arm, clinical efficacy (CDR-SB) is assessed against a propensity-score-weighted external
control cohort drawn from the Alzheimer's Disease Neuroimaging Initiative (ADNI). Two treatment
sequences are analyzed: "early-start" (randomized to donanemab in the placebo-controlled period,
N=860, 550 dosed in the LTE) and "delayed-start" (randomized to placebo, N=876, 657 dosed in the
LTE). Both groups can be switched to blinded placebo mid-trial upon meeting amyloid-based
treatment course completion criteria (<11 CL single scan / <25 CL two consecutive scans) — the
trial's distinctive limited-duration dosing design. The report covers three-year CDR-SB efficacy,
a CDR-Global disease-stage progression-risk comparison (early- vs delayed-start), amyloid
PET reduction/clearance/reaccumulation trajectories, and descriptive long-term safety by
treatment-sequence group (Table 1). All authors are Eli Lilly and Company employees (sponsor);
per `sources.yaml`/`src/environment.md`, no code repository, dataset, or IPD-access statement is
released with this paper. All analyses were exploratory and not controlled for multiplicity (§2.5,
§4). Numbers throughout this ARA are copied exactly from `paper.pdf`, cross-verified against the
EuropePMC/PMC open-access full text (PMC12869028, CC BY license).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | 5 observations (pivotal 76-week result, limited-duration dosing design, no internal LTE placebo, majority of early-start LTE participants off active drug, delayed-start disease-severity confound) → 3 gaps → key insight → 5 assumptions |
| [claims.md](logic/claims.md) | 12 falsifiable claims (C01–C12) with grounded number sources for every load-bearing value |
| [concepts.md](logic/concepts.md) | 13 technical terms (limited-duration dosing, early-/delayed-start groups, LTE, ADNI external control/propensity weighting, ESS, CDR-SB/CDR-G, MCID inapplicability, amyloid clearance/Centiloids, reaccumulation rate, MMRM, AUC/time-saved, ARIA/OAIR, Cox model) |
| [experiments.md](logic/experiments.md) | 11 declarative analysis plans (E01–E11), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph: 11 full `RW` blocks + 12 briefer entries covering all 23 in-text references |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, 5 assumptions, 9 self-reported limitations (L1–L9) |
| [solution/study_design.md](logic/solution/study_design.md) | Full trial/LTE structure, ADNI external-control construction, outcomes, statistical approach, data provenance |

### Physical Layer (`/src`, `/data`)
| File | Description |
|------|-------------|
| [src/environment.md](src/environment.md) | Analytical environment: WeightIt R package (no version stated), no released code/analysis scripts; data provenance (TRAILBLAZER-ALZ 2 IPD, ADNI, three reaccumulation-model source studies) |
| [data/dataset.md](data/dataset.md) | TRAILBLAZER-ALZ 2 primary dataset (N=1736) and ADNI external comparison dataset (2430 evaluated, 534 eligible, ESS 268/301) |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: 1 root question, design/analysis decisions, 11 experiment nodes, and dead ends/limitations explicitly stated in the paper |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 1 numbered table + 4 numbered figures (all filed, in order); accounts for supplementary Tables S1–S5 and Figs. S1–S8 referenced but not present in the provided 9-page PDF |
| [tables/table1.md](evidence/tables/table1.md) | Safety overview and AEs of special interest during the LTE period, by treatment-sequence group |
| [figures/figure1.md](evidence/figures/figure1.md) | TRAILBLAZER-ALZ 2 trial design (1a) and study dosing over time (1b) |
| [figures/figure2.md](evidence/figures/figure2.md) | CDR-SB LS mean change vs weighted ADNI cohort — early-start (2a), delayed-start (2b), 52-week-completer subset (2c) |
| [figures/figure3.md](evidence/figures/figure3.md) | CDR-Global hazard progression: early- vs delayed-start (Cox model, HR=0.73) |
| [figures/figure4.md](evidence/figures/figure4.md) | Brain amyloid plaque: mean CL reduction (4a), clearance rates (4b), reaccumulation after course completion (4c) |
