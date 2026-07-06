---
title: "Efficacy and safety of donanemab in the European eligible population: TRAILBLAZER-ALZ 2 post-hoc analyses"
authors: ["Frank Jessen", "Grazia Dell'Agnello", "Jennifer A. Zimmer", "Christophe Sapin", "Sascha Dichter", "Erin Doty", "Stéphane Epelbaum", "Cynthia D. Evans", "Paula M. Hauck", "Rashna Khanna", "Dawn A. Brooks", "John R. Sims", "Federica Agosta"]
year: 2026
venue: "The Journal of Prevention of Alzheimer's Disease 13 (2026) 100605"
doi: "10.1016/j.tjpad.2026.100605"
ara_version: "1.0"
domain: "Clinical trials / neurology — Alzheimer's disease disease-modifying therapy (post-hoc subgroup analysis)"
keywords: ["donanemab", "Alzheimer's disease", "APOE ε4", "EU-eligible population", "TRAILBLAZER-ALZ 2", "ARIA", "amyloid clearance", "CDR-SB", "conservative hybrid imputation", "propensity weighting"]
claims_summary:
  - "C01: 18% slowing of iADRS decline at 76 weeks (conservative imputation), difference 2.3 [0.7, 3.9], p=0.005."
  - "C02: CDR-SB difference −0.7 [−1.0, −0.4], p<0.001, a 28% slowing."
  - "C03: 40.3% lower risk of next-stage progression (HR 0.597) and 47.2% lower risk to moderate dementia (HR 0.528)."
  - "C04: Significant benefit on 5 of 6 CDR-SB domains (community affairs p=0.052)."
  - "C05: 37% vs 22% no CDR-SB progression at 52 weeks (p<0.001); 25% vs 18% at 76 weeks."
  - "C06: Progression delayed by 4.9 months overall, 6.9 months in low-medium tau."
  - "C07: Amyloid reduced −75.8 CL; clearance 33.5%/69.7%/80.5% at weeks 24/52/76; P-tau217 reduced."
  - "C08: ARIA-E 19.5%, IRR 8.0%, no ARIA-related deaths; any ARIA 32.0% vs 36.8% overall population."
  - "C09: LTE treatment effect increased over 154 weeks; early-start 29% lower progression risk vs delayed-start."
  - "C10: Benefit consistent across imputation methods (CDR-SB 28.2% vs 30.8%) and with the overall population (28.9%)."
abstract: "Background: In the EU, donanemab is indicated in adults with early symptomatic Alzheimer's disease who are apolipoprotein E ε4 non-carriers or heterozygotes; among these, patients without superficial siderosis at baseline, uncontrolled hypertension, or anticoagulant use are eligible. Objective: To assess efficacy and safety of donanemab in the EU-eligible population. Methods: A post-hoc conservative hybrid imputation method was implemented for clinical efficacy analyses during the TRAILBLAZER-ALZ 2 placebo-controlled period. In the 78-week long-term extension (LTE), early-start and delayed-start groups were compared to a propensity-weighted external control; participants were switched to placebo after meeting amyloid-based treatment course completion criteria. Results: By 76 weeks, donanemab-treated EU-eligible participants had a mean CDR-Sum of Boxes change-from-baseline difference from placebo of −0.7 points (95% CI −1.0, −0.4) and a 40.3% lower risk of disease progression to the next stage (per CDR-Global). Treatment benefit increased over 154 weeks for non-carriers and heterozygotes, including those meeting treatment course completion criteria by 52 or 76 weeks. In the placebo-controlled period, 119 (19.5%) and 49 (8.0%) donanemab-treated eligible participants experienced ARIA-edema/effusion and infusion-related reactions, respectively. Safety findings were similar among donanemab-treated participants in the placebo-controlled period and LTE delayed-start group. Conclusions: Consistent with previous TRAILBLAZER-ALZ 2 and LTE findings, donanemab significantly slowed disease progression compared to controls with a manageable safety profile in non-carriers and heterozygotes."
---

# Efficacy and safety of donanemab in the European eligible population: TRAILBLAZER-ALZ 2 post-hoc analyses

## Overview

This is a **post-hoc secondary analysis** of the phase 3 TRAILBLAZER-ALZ 2 trial (NCT04437511;
sponsor Eli Lilly and Company), re-analysing the trial dataset restricted to the **EU-eligible
population** — APOE ε4 non-carriers/heterozygotes without baseline superficial siderosis,
anticoagulant use, or uncontrolled hypertension — i.e., the patients expected to be treated in
European clinical practice. Clinical-scale efficacy over the 76-week placebo-controlled period is
estimated with the EMA-required **conservative hybrid J2R/CIR imputation** (and the original
methodology for comparison); progression is analysed with Cox models, disease stabilisation and
time-saved with mixed/time-progression models, and biomarkers (amyloid PET, P-tau217) with MMRM.
Long-term durability (154 weeks) is examined in the LTE against a propensity-weighted ADNI external
control. The paper shows that excluding ε4 homozygotes and contraindicated patients lowers ARIA
burden (~5% lower than the overall population, no ARIA-related deaths) while preserving efficacy
consistent with the overall trial. All analyses are exploratory and not controlled for multiplicity.

There is **no released code** (analytical study; SAS 9.4 + R 4.3.0). Trial individual participant
data are available **on request via Vivli**; the LTE external control comes from **ADNI**.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 10 falsifiable claims (C01–C10) with grounded number sources |
| [concepts.md](logic/concepts.md) | 14 technical concepts (populations, imputation, ARIA, scales, LTE) |
| [experiments.md](logic/experiments.md) | 8 analysis plans (E01–E08), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph (11 RW blocks + 8 briefer citations) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, 8 stated limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Trial design, analysis populations, LTE structure |
| [solution/statistical_methods.md](logic/solution/statistical_methods.md) | MMRM, J2R/CIR imputation, Cox, mixed/time-progression models |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [src/environment.md](src/environment.md) | Analytical env (SAS 9.4, R 4.3.0), Vivli/ADNI data access, NCT04437511 | all |
| [data/dataset.md](data/dataset.md) | TRAILBLAZER-ALZ 2 IPD (Vivli, request) + ADNI external control | all |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG (all explicit; 2 dead ends for LTE-method infeasibility) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 4 tables + 2 figures |
| [tables/table1.md](evidence/tables/table1.md) | Demographics/baseline (EU-eligible) |
| [tables/table2.md](evidence/tables/table2.md) | Imputation-method impact on 76-week clinical outcomes |
| [tables/table3.md](evidence/tables/table3.md) | CDR-G HRs, no-progression, amyloid outcomes |
| [tables/table4.md](evidence/tables/table4.md) | Safety summary (TEAEs, ARIA, IRR) |
| [figures/figure1.md](evidence/figures/figure1.md) | Clinical outcomes on 5 scales + CDR-SB domains forest |
| [figures/figure2.md](evidence/figures/figure2.md) | Time saved (overall 4.9 mo; low-medium tau 6.9 mo) |
