---
title: "Blood biomarkers of Alzheimer's disease and progression across different stages of cognitive decline in the community"
authors: ["Martina Valletta", "Davide Liborio Vetrano", "Caterina Gregorio", "Debora Rizzuto", "Bengt Winblad", "Marco Canevelli", "Sarah Andersson", "Matilda Dale", "Claudia Fredolini", "Erika J. Laukka", "Laura Fratiglioni", "Giulia Grande"]
year: 2025
venue: "Nature Communications 16:10412 (2025)"
doi: "10.1038/s41467-025-66728-2"
ara_version: "1.0"
domain: "Clinical epidemiology / population-based longitudinal biomarker study — Alzheimer's disease blood biomarkers and multistate transitions across cognitive decline stages"
grounding: full-text
keywords: [Alzheimer's disease, blood biomarkers, plasma/serum biomarkers, p-tau217, p-tau181, neurofilament light chain, GFAP, amyloid-beta 42/40, mild cognitive impairment, multistate Markov model, hazard ratio, SNAC-K, population-based cohort, dementia progression, MCI reversion]
claims_summary:
  - "In a community cohort of 2148 dementia-free adults followed up to 16 years (mean 9.6 years), 381 (17.7%) had MCI at baseline; 286 (16.2%) developed MCI, 364 (16.9%) developed all-cause dementia (58.2% AD type), and 1101 (51.3%) died during follow-up."
  - "Elevated continuous levels of all six biomarkers except Aβ42/40 were associated with faster, non-linear progression from MCI to all-cause and AD dementia; no biomarker was associated with progression from normal cognition to MCI."
  - "Dichotomized cut-offs: NfL (HR 1.84 all-cause / 2.34 AD dementia) and p-tau217 (HR 1.74 / 2.11) showed the strongest basic-model associations with MCI-to-dementia progression, followed by GFAP; a lower Aβ42/40 ratio was also associated with faster progression."
  - "High p-tau181, NfL, and GFAP were associated with lower hazard of MCI reversion to normal cognition in the basic model; after full adjustment for chronic diseases the p-tau181-reversion association became non-significant."
  - "The hazard of MCI-to-all-cause-dementia progression rose with the number of elevated biomarkers (among p-tau217, NfL, GFAP): HR 2.22 (1.50, 3.28) for three vs none, and even higher for AD dementia (HR 3.71, 2.22, 6.20); reversion hazard fell with more elevated biomarkers (HR 0.26, 0.11, 0.61 for three vs none)."
  - "The fastest MCI-to-dementia progression was seen in individuals with both p-tau217 and NfL elevated (all-cause dementia HR 2.29, 1.62, 3.24; AD dementia HR 3.07, 2.04, 4.60, vs low/low reference)."
  - "Associations were slightly stronger in participants under 78 and in women, but sensitivity analyses (excluding baseline MCI, inverse-probability weighting for attrition, CIND operationalization) were broadly consistent with the main findings."
abstract: "Blood biomarkers of Alzheimer's disease (AD) are promising for dementia prediction, but their association with progression across intermediate stages of cognitive decline in the general population remains unclear. We followed 2148 dementia-free individuals from a Swedish population-based cohort for up to 16 years. Associations between baseline AD blood biomarkers and transitions between normal cognition, mild cognitive impairment (MCI), and dementia were examined. Lower amyloid-β42/40 ratio and higher phosphorylated-tau181 (p-tau181), p-tau217, total-tau, neurofilament light chain (NfL), and glial fibrillary acidic protein (GFAP) were associated with faster progression from MCI to all-cause and AD dementia, with the strongest associations for NfL and p-tau217. Elevated NfL and GFAP were linked to reduced MCI reversion to normal cognition, whereas no biomarker was associated with MCI development from normal cognition. These findings show robust group-level associations and indicate that AD blood biomarkers may help stratify dementia risk at the MCI stage in the community."
---

# Blood biomarkers of Alzheimer's disease and progression across different stages of cognitive decline in the community

## Overview

This is an original epidemiological study (not a review or synthesis report): a population-based longitudinal analysis from the Swedish National study on Aging and Care in Kungsholmen (SNAC-K), published as a 9-page *Nature Communications* Article (2025, 16:10412). The study follows 2148 dementia-free older adults (baseline 2001-2004) for up to 16 years and uses parametric multistate Markov models to estimate hazard ratios (HR) for transitions between normal cognition (NC), mild cognitive impairment (MCI), all-cause dementia, and death, as a function of six baseline serum AD blood biomarkers (Aβ42/40, p-tau181, p-tau217, total-tau, NfL, GFAP) — analyzed both continuously (restricted cubic splines) and dichotomized (predefined cut-offs), individually and in combination.

**Input scope note.** The compiled input is the 9-page main-text PDF only (`paper.pdf`). It contains 2 main-text tables (Table 1, Table 2) and 2 main-text figures (Fig. 1, Fig. 2) — both visually rendered and transcribed below. The paper references extensive Supplementary Information (Figs. S1-S3, Tables S1-S14) that is **not included in the provided input**; every claim that depends on supplementary-only numbers is written directionally, with exact figures marked "Not specified in paper / not available from provided input." No supplementary file was fabricated or estimated.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating the study |
| [claims.md](logic/claims.md) | 13 falsifiable claims (C01-C13) with grounded numeric sources |
| [concepts.md](logic/concepts.md) | 16 technical terms formally defined |
| [experiments.md](logic/experiments.md) | 10 analysis plans (E01-E10), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph over cited biomarker/methods literature |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations and boundary conditions (from Discussion) |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, biomarker assays, MCI operationalization, multistate Markov modeling design |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Analytical environment (R 4.3.1, msm package), data/code availability | C01-C13 |

No runnable code was provided in the input (only the paper PDF); the paper cites an external analysis-code repository (not fetched/captured here per the compiler's input-fidelity rule — see `src/environment.md`). `src/` is therefore limited to `environment.md`.

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 17-node research DAG of the study's analytic sequence and documented modeling decisions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 2 tables + 2 figures, each with markdown transcription and a rendered PNG |
