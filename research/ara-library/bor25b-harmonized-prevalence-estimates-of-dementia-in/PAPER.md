---
title: "Harmonized prevalence estimates of dementia in Europe vary strongly with childhood education"
authors: [Axel Börsch-Supan, Salima Douhou, Marcela C. Otero, Beatrice Baaba Tawiah]
year: 2025
venue: "Scientific Reports"
doi: "10.1038/s41598-025-97691-z"
ara_version: "1.0"
domain: "Epidemiology — cross-national dementia/MCI prevalence estimation and validation using the Survey of Health, Ageing and Retirement in Europe (SHARE) and the Harmonized Cognitive Assessment Protocol (HCAP)"
keywords: [dementia, MCI, prevalence, SHARE, HCAP, cross-national comparison, education, epidemiology, Europe, cognitive impairment]
claims_summary:
  - "Dementia prevalence among individuals 65+ ranges from 4.5% (Abstract) / 4.6% (Table 3) in Switzerland to 22.7% in Spain; MCI ranges from 17.2% in Sweden to 31.1% in Portugal."
  - "Averaged across all 28 SHARE units, HCAP-validated dementia prevalence is 10.9% (SE=0.1) and MCI prevalence is 23.9% (SE=0.2)."
  - "Prevalence is concentrated in Mediterranean and Southeastern Europe, described as much higher than previously reported in these regions; lowest MCI prevalence (~17%) clusters in Austria, Germany, Sweden, Denmark, Switzerland."
  - "The HCAP-validated scale produces higher average prevalence but relatively less cross-national dispersion than the original Langa-Weir scale (coefficient of variation for Demented,%: 0.46 vs. 0.80)."
  - "A regression-based prediction (Hurd et al. approach) closely replicates the direct HCAP classification within the validation subsample (72.6/20.4/7.0% classified vs. 71.5/21.5/7.0% predicted for normal/MCI/demented)."
  - "Dementia/MCI risk rises significantly with age and falls significantly with childhood education (all p<0.0001); women have higher age-adjusted MCI risk than men but no significant dementia-risk difference (p=0.153)."
  - "Stroke (+7.2pp), depression (EURO-D>4, +4.0pp), and diabetes (+0.8pp) are significant dementia risk factors; physical activity is protective and smoking is a risk factor; blood pressure, cholesterol, and excessive alcohol show no significant association conditional on the others."
  - "A counterfactual simulation equalizing childhood education across countries dramatically compresses the cross-national variation in dementia prevalence, presented as the paper's central explanatory finding."
abstract: "Up-to-date, strictly cross-nationally comparable and nationally representative data on cognitive health are essential for our understanding of the dementia-related challenges in healthcare, to detect shortcomings in healthcare systems and to design effective prevention strategies. Such data have been missing in Europe. We use the most recent 2022 wave of the strictly harmonized Survey of Health, Ageing and Retirement in Europe (SHARE, 47,773 individuals age 65 and older) to obtain prevalence estimates of mild cognitive impairment and dementia for 27 European countries and Israel in 2022. The novelty of the paper is to validate these estimates using the Harmonized Cognitive Assessment Protocol (HCAP) as a validation tool. These new data exhibit much higher prevalence rates of dementia in the Mediterranean and Southeastern European countries and a much larger variation of cognitive impairment across Europe and Israel than previously known. Dementia prevalence ranges from 4.5% in Switzerland to 22.7% in Spain, MCI prevalence from 17.2% in Sweden to 31.1% in Portugal. Most of this variation can be explained by differences in education when respondents were young. Prevalence rates vary plausibly with other risk factors such as age and comorbidities associated with dementia."
---

# Harmonized Prevalence Estimates of Dementia in Europe Vary Strongly with Childhood Education

## Overview

This is a **quantitative epidemiological study** (survey-based cross-national prevalence
estimation, not a computational/ML-training paper) that uses Wave 9 (2021–2022) of the Survey of
Health, Ageing and Retirement in Europe (SHARE, N=47,733 individuals aged 65+ across 27 countries
and Israel) to produce prevalence estimates of mild cognitive impairment (MCI) and dementia. Its
central methodological novelty is validating these estimates against the internationally harmonized
Harmonized Cognitive Assessment Protocol (HCAP), administered to a 5-country validation subsample
(Czech Republic, France, Germany, Denmark, Italy; N=2,687), and using a regression-based approach
(Hurd et al. 2013) to extend that validated classification to the full 28-unit SHARE parent sample
(analytical N=47,193). The paper reports much higher and more geographically varied prevalence than
previously known — dementia ranging from 4.5%/4.6% (Switzerland) to 22.7% (Spain), MCI from 17.2%
(Sweden) to 31.1% (Portugal) — and its central explanatory finding is that differences in childhood
education levels across countries account for most of this cross-national variation. It has no
released code, dataset accession beyond the SHARE data-access portal, or registered clinical trial
(per `sources.yaml`: `code: []`, `data: []`, `clinical_trials: []`).

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | 6 observations (dementia burden, non-harmonized prior estimates, SHARE/HCAP design) → 3 gaps → key insight (HCAP as a validation base) → 4 assumptions |
| [claims.md](logic/claims.md) | 13 falsifiable claims (C01–C13) with grounded number sources, including 2 flagged internal source inconsistencies |
| [concepts.md](logic/concepts.md) | 12 technical terms (SHARE, SHARE-HCAP, HCAP, Manly et al. classification, Hurd et al. regression, MCI, dementia, Langa-Weir scale, ISCED, FIML, EURO-D, coefficient of variation) |
| [experiments.md](logic/experiments.md) | 7 declarative verification/analysis plans (E01–E07) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's 36 in-text references (7 full RW blocks + briefer entries covering the rest) |
| [solution/constraints.md](logic/solution/constraints.md) | Scope boundaries, 4 assumptions, authors' stated limitations, and 4 flagged internal source inconsistencies |
| [solution/study_design.md](logic/solution/study_design.md) | The four-step estimation pipeline: validation sampling → HCAP classification → regression-based relation → full-sample prediction, plus the Langa-Weir comparison and counterfactual-simulation methodology |
| [solution/classification_method.md](logic/solution/classification_method.md) | Manly et al. (2022) factor-score/informant-report decision rule for classifying normal/MCI/demented |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Statistical software (Stata 14.2, Mplus 8.10), SHARE/SHARE-HCAP data access, ethics approval, funding; no code/dataset/trial released |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG: 1 root question, sampling/classification/regression/comparison decisions and experiments, and dead ends (20 nodes) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 4 numbered tables + 2 numbered figures (all filed, in order) |
| [tables/table1.md](evidence/tables/table1.md) | Sample characteristics: SHARE Wave 9 vs. SHARE-HCAP subsample |
| [tables/table2.md](evidence/tables/table2.md) | Classified vs. predicted normal/MCI/demented prevalence within the SHARE-HCAP subsample |
| [tables/table3.md](evidence/tables/table3.md) | Main result: HCAP-validated vs. Langa-Weir prevalence for 27 countries + Israel |
| [tables/table4.md](evidence/tables/table4.md) | Group differences in prevalence by age, sex, and education, with pairwise p-values |
| [figures/figure1.md](evidence/figures/figure1.md) | Coefficient plot: comorbidity/lifestyle associations with dementia probability |
| [figures/figure2.md](evidence/figures/figure2.md) | Actual vs. education-equalized counterfactual dementia prevalence, 27 countries + Israel |
