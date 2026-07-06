---
title: "Immunoassay detection of multiphosphorylated tau proteoforms as cerebrospinal fluid and plasma Alzheimer's disease biomarkers"
authors: [A. Wojdała, G. Bellomo, L. Gaetani, C. E. Teunissen, L. Parnetti, D. Chiasserini]
year: 2025
venue: "Nature Communications 16:214"
doi: "10.1038/s41467-024-54878-8"
ara_version: "1.0"
domain: "Clinical neurochemistry / fluid biomarkers — Alzheimer's disease diagnostics; sandwich immunoassay (Simoa) method development"
keywords: [Alzheimer's disease, phosphorylated tau, p-tau217, p-tau231, p-tau181, multiphosphorylated tau, Simoa immunoassay, cerebrospinal fluid, plasma biomarker, diagnostic accuracy]
claims_summary:
  - "Two novel Simoa sandwich immunoassays (C231D181, C231D217) specifically detect tau simultaneously phosphorylated at two sites (T181&T231, T217&T231) in CSF and plasma."
  - "CSF p-tau181&231 and p-tau217&231 give high diagnostic accuracy discriminating NDC from all AD continuum stages in both cohorts (CSF AUC range 0.927–1.000)."
  - "Plasma p-tau217&231 shows improved diagnostic performance over single-site plasma p-tau217 or p-tau231 and the highest nominal AUC among plasma markers."
  - "Plasma p-tau181&231 does NOT differentiate AD continuum from controls (negligible effect, d<0.2) and does not correlate with its CSF equivalent."
  - "p-tau217&231 (C231D217) shows the highest median concentration fold change (AD continuum vs NDC) in both CSF and plasma."
  - "CSF vs plasma discrepancy for p-tau181&231 suggests matrix-specific tau processing."
abstract: "Different forms of phosphorylated tau (p-tau) have shown strong potential as Alzheimer's disease (AD) biomarkers in both cerebrospinal fluid (CSF) and plasma. We hypothesized that p-tau proteoforms simultaneously phosphorylated at two different sites may have an increased diagnostic value compared with tau phosphorylated at a single site. Here, we developed two immunoassays detecting CSF and plasma tau simultaneously phosphorylated at both T181 and T231 (p-tau181&231) and at T217 and T231 (p-tau217&231). Subsequently, we measured CSF and plasma p-tau181&231, p-tau217&231, p-tau181, p-tau217, and p-tau231 levels in two cohorts across the AD continuum and in frontotemporal dementia (FTD) patients (discovery n = 55, validation n = 118). CSF and plasma p-tau217&231, p-tau181, p-tau217, and p-tau231 and CSF, but not plasma, p-tau181&231 were significantly elevated in all AD continuum groups vs. Neurological Disease Control group. Notably, plasma p-tau217&231 consistently showed an improved diagnostic performance compared with single-site phosphorylation assays – p-tau217 or p-tau231. The differences observed between CSF and plasma measurements suggest matrix-specific protein processing, underscoring the need for further research on the dynamics of tau phosphorylation pattern along the AD continuum."
---

# Immunoassay detection of multiphosphorylated tau proteoforms as CSF and plasma AD biomarkers

## Overview

This is a biomarker method-development study. The authors built two novel Simoa (single-molecule
array) sandwich immunoassays — **C231D181** (captures p-tau231, detects p-tau181 → measures tau
doubly phosphorylated at T181&T231) and **C231D217** (captures p-tau231, detects p-tau217 →
measures tau doubly phosphorylated at T217&T231). Both require two concurrent phosphorylations to
form a signal-generating immunocomplex. They analytically validated both assays (precision,
dilution linearity, LLOQ/ULOQ, spike-recovery, specificity) and then measured five p-tau species
(p-tau181, p-tau217, p-tau231, p-tau181&231, p-tau217&231) in matched CSF and plasma from two
in-house University of Perugia cohorts across the AD continuum (pre-AD, MCI-AD, AD-dem), plus FTD,
against a Neurological Disease Control (NDC) group (discovery n=55, validation n=118). Key result:
**plasma p-tau217&231** outperforms single-site plasma p-tau217/p-tau231, while **plasma
p-tau181&231** fails to separate groups — a CSF/plasma divergence attributed to matrix-specific tau
processing.

No computational code repository is associated with this paper. Raw assay measurements are released
as a Source Data / Supplementary Information file (open); patient-level cohort data are available
from the corresponding authors on request (in-house Perugia / Amsterdam UMC cohorts).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) |
| [concepts.md](logic/concepts.md) | 12 key technical terms |
| [experiments.md](logic/experiments.md) | 7 declarative verification plans (E01–E07) |
| [related_work.md](logic/related_work.md) | Typed dependency graph + full citation footprint |
| [solution/method.md](logic/solution/method.md) | Assay design + wet-lab protocols (C231D181, C231D217) |
| [solution/study_design.md](logic/solution/study_design.md) | Cohorts, classification, statistical analysis plan |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations, assumptions, boundary conditions |

### Artifact Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Instruments, software, reagents, data sources, ethics | C01, C07 |
| [configs/assay_parameters.md](src/configs/assay_parameters.md) | Assay parameter values (beads, SBG, dilution, curve fit) | C04, C07 |
| [artifacts.md](src/artifacts.md) | The two immunoassays + reagents/calibrator peptides as concrete deliverables | C04, C07 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG (question → method dev → validation → clinical eval) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 1 table + 5 figures |
| tables/table1 | Demographic & clinical profile of both cohorts |
| figures/figure1 | CSF↔plasma correlation heatmaps (Spearman ρ) |
| figures/figure2 | Discovery-cohort diagnostic performance + Cohen's d |
| figures/figure3 | ROC curves, plasma p-tau217/231/217&231 (both cohorts) |
| figures/figure4 | Validation-cohort diagnostic performance + Cohen's d |
| figures/figure5 | Assay design diagrams (C231D181, C231D217) |
