---
title: "TRAILBLAZER-ALZ 4: A phase 3 trial comparing donanemab with aducanumab on amyloid plaque clearance in early, symptomatic Alzheimer's disease"
authors: ["Stephen Salloway", "Andrew Pain", "Elly Lee", "Michelle Papka", "Margaret B. Ferguson", "Hong Wang", "Haoyan Hu", "Ming Lu", "Ena Oru", "Paul A. Ardayfio", "Deirdre B. Hoban", "Emily C. Collins", "Dawn A. Brooks", "John R. Sims"]
year: 2025
venue: "Alzheimer's & Dementia (Alzheimer's Dement. 2025;21:e70293)"
doi: "10.1002/alz.70293"
ara_version: "1.0"
domain: "Clinical trials — Alzheimer's disease / amyloid-targeting immunotherapy"
keywords: ["donanemab", "aducanumab", "amyloid plaque clearance", "amyloid-related imaging abnormalities", "ARIA", "florbetapir PET", "Centiloid", "phase 3 RCT", "early symptomatic Alzheimer's disease", "active comparator"]
claims_summary:
  - "C01: Donanemab superior to aducanumab on 6-month AP clearance in the overall population (37.9% vs 1.6%, P<0.001) — co-primary."
  - "C02: Donanemab superior on 6-month AP clearance in the low–medium tau subpopulation (38.5% vs 3.8%, P=0.008) — co-primary."
  - "C03: Donanemab superior on AP clearance at 12 and 18 months (overall and low–medium tau)."
  - "C04: Donanemab reaches AP clearance faster (median 359 vs 568 days, P<0.001)."
  - "C05: Donanemab produces greater absolute and percent amyloid lowering at 6/12/18 months."
  - "C06: Plasma biomarker differences favor donanemab early but attenuate to non-significance by 18 months; no NfL treatment effect."
  - "C07: Faster/deeper amyloid clearance did NOT increase ARIA frequency or risk (ARIA numerically lower with donanemab; time-to-ARIA-E P=0.438)."
  - "C08: No deaths; overall safety/tolerability consistent with prior reports, with distinct AE signatures per arm."
abstract: "The phase 3, open-label TRAILBLAZER-ALZ 4 study compared the effect of donanemab versus aducanumab on amyloid plaque (AP) clearance in participants with early symptomatic Alzheimer's disease. Participants (n = 148) were randomized 1:1 to intravenous donanemab (700 mg every 4 weeks for three doses, then 1400 mg every 4 weeks thereafter) or aducanumab (per label). AP was measured with florbetapir F 18 PET; AP clearance was defined as < 24.1 Centiloids. At 6, 12, and 18 months, AP clearance was achieved in 37.9%, 70.0%, and 76.8% of donanemab-treated participants versus 1.6%, 24.6%, and 43.1% of aducanumab-treated participants (P < 0.001). Median time to clearance was 359 versus 568 days (P < 0.001). ARIA-edema/effusion occurred in 23.9% and 34.8% of donanemab- and aducanumab-treated participants, respectively. Donanemab treatment resulted in earlier and greater AP clearance compared to aducanumab; ARIA frequencies were consistent with prior studies. Clinical trial registration: NCT05108922."
---

# TRAILBLAZER-ALZ 4: A phase 3 trial comparing donanemab with aducanumab on amyloid plaque clearance in early, symptomatic Alzheimer's disease

## Overview
TRAILBLAZER-ALZ 4 (NCT05108922) is the first study to directly compare two amyloid-targeting therapies (ATTs). This 76-week, randomized, open-label, active-comparator phase 3 trial (148 participants, 31 US sites, sponsor Eli Lilly) tested the superiority of donanemab versus aducanumab on brain amyloid plaque (AP) clearance (< 24.1 Centiloids by florbetapir F18 PET) in early symptomatic Alzheimer's disease. Donanemab was superior on both co-primary endpoints (6-month AP clearance in the overall population and the low–medium tau subpopulation) and on the key secondary endpoints (time to clearance, mean amyloid lowering at 6/12/18 months). Plasma biomarker changes favored donanemab early but were not statistically significant at 18 months. Critically, the greater and faster amyloid clearance with donanemab did NOT translate into increased ARIA — ARIA-E/H were numerically lower with donanemab and time-to-first-ARIA-E did not differ between arms.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps (no direct ATT comparator; ARIA-vs-clearance relationship) → key insight |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) with grounded number sources |
| [concepts.md](logic/concepts.md) | 10 technical terms (AP clearance, Centiloid, ARIA-E/H, low–medium tau, gated multiplicity, MMRM/ANCOVA, plasma biomarkers, …) |
| [experiments.md](logic/experiments.md) | 6 prespecified analysis plans (E01–E06), directional only |
| [solution/study_design.md](logic/solution/study_design.md) | Trial design: arms, endpoints, population, analysis flow |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, author-stated limitations |
| [related_work.md](logic/related_work.md) | Typed dependency graph (8 full RW blocks + brief citation footprint) |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [src/environment.md](src/environment.md) | SAS v9.4 analyses, PET/MRI pipeline, registration NCT05108922; no code repo | C01–C08 |
| [data/dataset.md](data/dataset.md) | Lilly IPD via Vivli (access=request), variables, consent/ethics | C01–C08 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 11-node research DAG (question → design decisions → endpoint experiments → safety → 1 dead_end) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 3 tables + 5 figures (each with markdown + .png) |
| [tables/table1.md](evidence/tables/table1.md) | Baseline demographics/clinical characteristics |
| [tables/table2.md](evidence/tables/table2.md) | Mean change in amyloid PET (6/12/18 months) |
| [tables/table3.md](evidence/tables/table3.md) | Summary of adverse events |
| [figures/figure1.md](evidence/figures/figure1.md) | CONSORT participant-flow diagram |
| [figures/figure2.md](evidence/figures/figure2.md) | Co-primary AP clearance at 6 months |
| [figures/figure3.md](evidence/figures/figure3.md) | AP clearance at 12/18 months + time-to-clearance KM |
| [figures/figure4.md](evidence/figures/figure4.md) | Plasma biomarkers (p-tau217/181, GFAP, NfL) |
| [figures/figure5.md](evidence/figures/figure5.md) | Time to first ARIA-E (Kaplan–Meier) |
