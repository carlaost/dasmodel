---
title: "Effects of Medicare predictors in health disparities in the risk of Alzheimer's disease"
authors: [Igor Akushevich, Arseniy Yashkin, Julia Kravchenko]
year: 2025
venue: "Alzheimer's & Dementia: Translational Research & Clinical Interventions (TRCI) 2025;11:e70078"
doi: "10.1002/trc2.70078"
ara_version: "1.0"
grounding: full-text
domain: "Epidemiology / health-disparities methodology (survival analysis, population attributable fraction)"
keywords: [Alzheimer's disease risk, decomposition methods, exposure and vulnerability effects, health disparities, hypertension, Medicare, population attributable fraction, risk-related diseases, Cox proportional hazards, dual eligibility]
claims_summary:
  - "A PAF-based Cox decomposition splits any disparity exactly into per-predictor exposure x vulnerability factors, with no baseline-hazard assumption (C01)."
  - "Low income (dual eligibility) is the main predictor of most AD-risk disparities, acting through the exposure channel (C02)."
  - "Vulnerability to arterial hypertension is the dominant disease predictor of the disparities (C03)."
  - "Cerebrovascular disease and depression are notable secondary predictors (C04)."
  - "Predictors explain ~half the Black-White disparity, over-explain Hispanic-White, and inflate White-Native American and White-Asian disparities (C05)."
  - "Female-male and stroke-belt disparities are less influenced by the examined predictors (C06)."
  - "A majority (57.4%) of exposure/vulnerability effects are significant; exposure is significant more often than vulnerability (C07)."
  - "Results are stable across outcome-ascertainment sensitivity analyses (C08)."
abstract: "Disparities in Alzheimer's disease (AD) and related dementias (ADRD) persist across race/ethnicity, sex, and US geographic regions, but limited quantitative information exists to explain how specific predictors contribute to these disparities. Many traditional methods lack precision in addressing both exposure (higher prevalence of a predictor) and vulnerability (higher risk associated with a predictor) effects. This study introduces an approach that leverages population attributable fraction (PAF) to analyze and explain AD/ADRD disparities using Medicare data. Applied to a nationally representative 5% sample of US Medicare adults aged 70, 75, 80, and 85, across six disparities (Black-White, Hispanic-White, Native American-White, Asian-White, female-male, and stroke-belt vs non-stroke-belt states), low income and vulnerability to arterial hypertension were the primary contributors, with cerebrovascular diseases and depression as notable secondary predictors. Income-related disparities were exposure-driven while hypertension's effect was largely vulnerability-driven; racial disparities (Black-White, Hispanic-White) were most affected by income and hypertension, while female-male and stroke-belt disparities were less influenced. The approach offers a framework for explaining disparities and designing targeted interventions."
---

# Effects of Medicare predictors in health disparities in the risk of Alzheimer's disease

## Overview

This methods-and-application paper introduces a **population-attributable-fraction (PAF) based
decomposition** of health disparities inside a Cox proportional-hazards model, and applies it to a
5% nationally representative sample of US Medicare claims (1991–2020) to explain disparities in
Alzheimer's disease (AD) risk. For a subpopulation pair, the observed risk ratio factorizes as
`RR = R_r · Π_i f_i`, and each predictor factor decomposes **exactly and multiplicatively** into an
**exposure effect** `E_i` (from differences in predictor prevalence) and a **vulnerability effect**
`V_i` (from differences in per-exposure risk); the shared baseline hazard cancels, so the split
needs no baseline-hazard assumption. Across six disparities and four age cohorts (70, 75, 80, 85),
**low income (Medicare/Medicaid dual eligibility)** is the leading contributor and acts through
exposure, while **arterial hypertension** is the dominant disease predictor and acts through
vulnerability; cerebrovascular disease and depression are notable secondary predictors. The
predictors explain roughly half the Black–White disparity and more than fully explain the
Hispanic–White disparity, but *inflate* the White–Native American and White–Asian disparities;
female–male and stroke-belt disparities are little influenced. Findings imply that income-related
disparities call for socioeconomic intervention and hypertension-related disparities call for
managing vulnerability (better hypertension control).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (O1–O4) → gaps (G1–G2) → PAF-decomposition key insight → assumptions |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) with grounded sources |
| [concepts.md](logic/concepts.md) | 9 technical terms (disparity, unexplained disparity, PAF, exposure/vulnerability effects, base Cox model, dual eligibility, stroke belt, AD ascertainment) |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph (RW01–RW08) + full brief citation footprint |
| [solution/method.md](logic/solution/method.md) | PAF decomposition: Eqs. 1–6, analysis pipeline |
| [solution/study_design.md](logic/solution/study_design.md) | Cohorts, disparities, predictors, estimation, sensitivity, ethics |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions (incl. causal-mediation caveats), limitations |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [src/environment.md](src/environment.md) | Reproducibility: data source (CMS/ResDAC controlled), no code repo, protocols | — |
| [src/execution/decomposition.py](src/execution/decomposition.py) | Reconstructed closed-form PAF exposure/vulnerability decomposition (Eqs. 3, 6) | C01 |
| [data/dataset.md](data/dataset.md) | Medicare 5% sample provenance, access, variables, predictors | C02, C05 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [trace/exploration_tree.yaml](trace/exploration_tree.yaml) | 11-node research DAG (question → decisions → experiments; 2 dead ends: screened conditions, WN/WA non-explanation) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 4 tables + 1 figure (all main-text numbered objects) |
| [tables/table1.md](evidence/tables/table1.md) | Sample sizes and AD cases by cohort/subpopulation |
| [tables/table2.md](evidence/tables/table2.md) | Baseline predictor prevalences (%) |
| [tables/table3.md](evidence/tables/table3.md) | Paired multivariable-Cox AD hazard ratios |
| [tables/table4.md](evidence/tables/table4.md) | Total = exposure × vulnerability decomposition, six disparities |
| [figures/figure1.md](evidence/figures/figure1.md) | Observed / unexplained / low-income-adjusted disparity vs age |
