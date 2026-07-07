---
title: "Global Societal Burden of Alzheimer's Disease by Severity: a Targeted Literature Review"
authors: [Maria A. Cavaco, Se Ryeong Jang, Christopher Olsen, Carolyn Bodnar, Nicole Ferko]
year: 2025
venue: "Neurology and Therapy (Neurol Ther), 14:1797–1826"
doi: "10.1007/s40120-025-00815-w"
ara_version: "1.0"
domain: "Health economics / cost-of-illness — targeted literature review of the total societal economic burden of Alzheimer's disease (AD) and dementia, stratified by disease severity, care setting, cost category, and region"
keywords: [Alzheimer's disease, dementia, cost of illness, societal burden, caregiver burden, informal care, disease severity, targeted literature review, PRISMA-S, financial delinquency, quality of life, PPPY]
claims_summary:
  - "Total societal costs of AD/dementia typically increase by at least 1.5x (>=50% between consecutive severity levels) with progression from mild to more severe disease stages."
  - "Informal (indirect) caregiving costs comprise close to half of total societal costs, exceeding 50% of total costs in the moderate disease stage in studies with granular cost breakdowns."
  - "The economic burden reported for MCI, though based on limited studies, is appreciable relative to mild AD, with one study showing a 126% cost increase from MCI to mild AD."
  - "Direct costs typically comprise at least one-third (31-52% in mild-stage studies) of total societal costs across disease stages."
  - "Underreported societal costs unique to AD/dementia -- financial delinquencies (scams, missed payments), police call-outs, reduced public tax revenue, and losses in quality of life -- rise from mild to moderate AD and can fall again in severe AD."
  - "Informal caregiving hours per week increase by at least 1.4x from mild to severe disease in community care, and institutional-care direct costs exceed indirect costs, unlike community care."
  - "Costs vary substantially by region and by the dementia staging instrument used (CDR vs. MMSE vs. FAST), complicating cross-study comparison."
abstract: "Alzheimer's disease (AD) is among the costliest of illnesses for the elderly, placing a significant burden on healthcare systems and caregivers. Despite the depth of evidence, reviews lack a holistic assessment of such costs, falling short of illustrating unmet medical needs. The objective of this review was to therefore characterize the total societal economic burden of AD, broken down by care setting and disease severity. A targeted literature search of systematic reviews, cost-of-illness, and observational studies published between 2013 and 2024 was conducted on MEDLINE and Embase to identify articles reporting the economic burden of AD. Grey literature was hand-searched. Both direct and indirect costs were assessed, including societal burdens not often reported by AD-specific cost-of-illness studies such as financial delinquencies. In total, 81 articles were reviewed in depth, including 20 systematic reviews and 61 studies or reports. Findings consistently demonstrated that societal costs of AD or dementia typically increased by at least 50% between consecutive severity levels, increasing with disease progression. Informal caregiving often comprised close to half of societal costs, regardless of care setting, disease severity, or region. While studies reporting costs of mild cognitive impairment (MCI) were limited, the economic burden reported for this stage was appreciable compared to mild AD. Evidence for the impact of AD, as early as MCI, on quality of life (e.g., emotional and mental strain) and personal financial management capabilities was also identified. This review provides a comprehensive overview, from studies spanning over more than a decade, of the substantial societal economic burden associated with AD, across cost categories, care settings, disease stages, and regions. This review may be used to inform health economic evaluations of novel interventions with potential to reduce the enormous and growing global economic burden of AD and dementia."
---

# Global Societal Burden of Alzheimer's Disease by Severity: a Targeted Literature Review

## Overview

This is a targeted literature review (TLR), not a primary empirical study: EVERSANA/Eisai-affiliated authors searched MEDLINE and Embase (per PRISMA-S guidelines) plus hand-searched grey literature for systematic reviews, cost-of-illness studies, and observational studies (2013–2024) reporting the direct and indirect economic burden of AD/dementia broken down by discrete disease severity (MCI, mild, moderate, severe). Out of 3699 screened records, 81 studies were included (59 prospective/retrospective studies, 2 AD reports, 20 systematic reviews/meta-analyses). The review's contribution is not a new statistical estimate but a synthesis framework: it harmonizes heterogeneous severity-staging scales (MMSE, CDR, FAST, GDS, Dependence Scale) into four buckets, extracts costs stratified by care setting (community vs. institutional) and cost type (direct medical, direct non-medical, indirect/informal), and — distinctively — captures under-reported societal costs rarely included in AD cost-of-illness studies: financial delinquencies (scams, missed payments, police call-outs), public fiscal losses (lost taxes, financial aid), and intangible quality-of-life costs. The central empirical finding, repeated across regions and care settings, is that societal costs rise by at least 50–150% between consecutive severity stages, driven substantially by informal caregiving (often ≥50% of total societal cost), while some under-reported costs (heating bills, mobility costs, police call-outs) peak in mild-to-moderate stages and fall in severe AD.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (dementia prevalence/cost scale, review gaps) → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 10 falsifiable claims (C01–C10) with grounded number sources |
| [concepts.md](logic/concepts.md) | 17 technical terms (TLR, PICOS, disease severity staging instrument + its 5 named scales [CDR-SB, FAST, MMSE, GDS, DS], direct costs, indirect costs, costing method, PPPY/PPPM, societal cost, intangible cost, financial delinquency, care setting, cost component taxonomy) |
| [experiments.md](logic/experiments.md) | 6 declarative verification/analysis plans (E01–E06) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's citation footprint (RW blocks + brief entries) |
| [solution/constraints.md](logic/solution/constraints.md) | Scope boundaries, assumptions, limitations (as stated in Discussion) |
| [solution/study_design.md](logic/solution/study_design.md) | TLR methodology: search strategy, PICOS criteria, cost definitions, data extraction/conversion rules, statistical treatment |
| [solution/cost_taxonomy.md](logic/solution/cost_taxonomy.md) | The paper's societal-cost component taxonomy (Fig. 1), reconstructed as a structured hierarchy |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Databases (MEDLINE, Embase), grey literature sources, visualization tools (Excel, RStudio/tidyverse); no code/dataset/trial released |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: literature search/screening funnel, severity-harmonization and cost-normalization decisions, and dead ends (13 nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 6 numbered tables + 7 numbered figures (all filed); notes on unavailable supplementary tables S1–S8 |
| [tables/table1.md](evidence/tables/table1.md) | PICOS criteria for article inclusion in the TLR |
| [tables/table2.md](evidence/tables/table2.md) | Definitions of indirect (informal-care) costing methods |
| [tables/table3.md](evidence/tables/table3.md) | Average societal cost (PPPY) by severity, community vs. institutional care |
| [tables/table4.md](evidence/tables/table4.md) | Average total direct costs (PPPY) by severity and care setting |
| [tables/table5.md](evidence/tables/table5.md) | Unique societal burdens (UK, Germany, China, US) — heating, police call-outs, scams, taxes, intangible costs |
| [tables/table6.md](evidence/tables/table6.md) | Average total indirect costs (PPPY) by severity and care setting |
| [figures/figure1.md](evidence/figures/figure1.md) | Societal cost components taxonomy (diagram) |
| [figures/figure2.md](evidence/figures/figure2.md) | PRISMA flow diagram of study selection |
| [figures/figure3.md](evidence/figures/figure3.md) | Characteristics of included studies (n=81): design, care setting, region |
| [figures/figure4.md](evidence/figures/figure4.md) | Percentage change in societal costs between severity stages, by study/country |
| [figures/figure5.md](evidence/figures/figure5.md) | Breakdown of direct/indirect cost components by severity (n=6 studies) |
| [figures/figure6.md](evidence/figures/figure6.md) | Mean informal caregiver profiles by severity and care setting |
| [figures/figure7.md](evidence/figures/figure7.md) | Range of weekly caregiver hours by severity and care setting |
