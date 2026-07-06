---
title: "Population Attributable Fractions Associated with Alzheimer's Disease Risk Factors"
authors: [Igor Akushevich, Arseniy Yashkin, Svetlana Ukraintseva, Anatoliy Yashin, Julia Kravchenko]
year: 2025
venue: "Innovation in Aging, Vol. 9, Suppl. 2 (Gerontological Society of America 2025 Annual Scientific Meeting abstract)"
doi: "10.1093/geroni/igaf122.2529"
ara_version: "1.0"
domain: "Epidemiology / gerontology — observational cohort study of Alzheimer's disease and related dementia (AD/ADRD) risk factors using Medicare administrative data"
keywords: [Alzheimer's disease, ADRD, population attributable fraction, PAF, Cox proportional hazards, Medicare, risk factors, health disparities, hypertension, depression, stroke]
claims_summary:
  - "A nine-disease multivariable Cox model (heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, TBI, diabetes mellitus) captures the primary determinants of AD/ADRD risk variation."
  - "The fraction of the total PAF explained by the predictors increases with age."
  - "Hypertension, stroke, and depression are the strongest disease-specific PAF contributors across all subpopulations."
  - "Hypertension reaches 45-50% of total PAF for Black, Asian, and Hispanic subpopulations."
  - "Stroke is the primary contributor for males (>30%); depression is highest among females and White individuals (~30%)."
  - "Hypertension and depression are the leading contributors for Native Americans (both ~30%)."
  - "Heart failure is the fourth strongest contributor for all subpopulations, exceeding 5% for Native Americans."
  - "Additional contributors with PAFs >3% include hypotension (males), diabetes (Asian, Hispanic), arrhythmia (males), and TBI (Black, Asian)."
abstract: "Although numerous risk factors for Alzheimer's disease (AD) and related dementias (ADRD) have been identified, their combined influence on risk remains uncertain. In this study, we leverage a high-power 5%-sample of the Medicare population to assess the joint impact of AD/ADRD risk-related diseases and low income—as indicated by dual Medicare eligibility—on the risk of clinical diagnosis of AD/ADRD. We leveraged the univariable and multivariable Cox models for estimating AD/ADRD risks, identified most powerful predictors, and constructed predictive multivariable models for AD/ADRD risks, and evaluated their population attributable fractions (PAFs) for the general populations of older adults and race- and sex-specific subpopulations. The identified model included nine diseases—heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, traumatic brain injury, and diabetes mellitus—as primary determinants of variation in AD/ADRD risk. The fraction of the total PAF explained by the predictors increased with age. The decomposition of the total PAF in terms of disease-specific PAFs showed that hypertension, stroke, and depression provided the strongest contribution for all subpopulations: Hypertension reached 45-50% of total PAF for Black, Asian, and Hispanic subpopulations. Stroke was the primary contributor for males (>30%); depression was highest among females and White individuals (approximately 30%). Hypertension and depression were the leading contributors for Native Americans (both approximately 30%). Heart Failure was the fourth strongest contributor for all subpopulations, with the contribution exceeding 5% for Native American individuals. Additional noteworthy contributors with PAFs exceeding 3% included hypotension (males), diabetes (Asian, Hispanic), arrhythmia (males), and TBI (Black, Asian)."
grounding: full-text
---

# Population Attributable Fractions Associated with Alzheimer's Disease Risk Factors

## Overview

This ARA is compiled from the **complete published source**, which is a two-page conference
abstract (Gerontological Society of America 2025 Annual Scientific Meeting, published in *Innovation
in Aging* Vol. 9, Suppl. 2, Dec 2025, pp. 743–744, open access CC BY, PMCID PMC12761288). The
published item contains an author block and abstract narrative only — **it has no methods section,
no numbered tables, no figures, no references, and no appendices**. Every value reproduced in this
ARA is transcribed exactly from that abstract text; methodological detail beyond what the abstract
states is marked "Not specified in the published abstract" and is **not** fabricated.

The study leverages a 5% sample of the U.S. Medicare population (CMS administrative
claims/enrollment data; controlled access via ResDAC) to quantify how a set of comorbid diseases —
plus low income proxied by dual Medicare eligibility — jointly drive the risk of a clinical AD/ADRD
diagnosis. Univariable and multivariable Cox proportional-hazards models identify a nine-disease
predictor set; population attributable fractions (PAFs) are then computed and decomposed into
disease-specific contributions overall, by age, and across race- and sex-specific subpopulations.
The headline epidemiological finding is that hypertension, stroke, and depression dominate the
attributable burden, with pronounced heterogeneity across race and sex groups.

## Grounding note

`grounding: full-text` — the entire published PDF was read (2 pages, 0 embedded images). The source
document is itself only a conference meeting abstract, so the "full text" available is the abstract.
The evidence layer therefore files no tables or figures because **the source contains none**
(evidence-completeness is N/A, documented in `evidence/README.md`). No underlying data, code, or
supplementary materials were released or referenced.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 9 falsifiable claims (C01–C09) |
| [concepts.md](logic/concepts.md) | 7 key technical terms (PAF, PAF decomposition, AD/ADRD, Cox model, dual eligibility, Medicare 5% sample, subpopulation stratification) |
| [experiments.md](logic/experiments.md) | 4 declarative analysis plans (E01–E04) |
| [related_work.md](logic/related_work.md) | Typed dependency graph (data-source dependency + citation-footprint note) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Observational Cox + PAF-decomposition study design |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [src/environment.md](src/environment.md) | Analytical environment, data source access | — |
| [data/dataset.md](data/dataset.md) | Medicare 5% sample provenance and access | C01–C09 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 8-node research DAG (reconstructed from the abstract narrative) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Evidence index; documents that the source (a conference abstract) contains no numbered tables or figures (completeness N/A) |
