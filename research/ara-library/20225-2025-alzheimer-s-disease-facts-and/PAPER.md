---
title: "2025 Alzheimer's disease facts and figures"
authors: ["Alzheimer's Association"]
year: 2025
venue: "Alzheimer's & Dementia (Alzheimer's Dement. 2025;21:e70235)"
doi: "10.1002/alz.70235"
ara_version: "1.0"
domain: "Epidemiology / public-health surveillance / health economics — Alzheimer's disease and dementia in the United States"
grounding: full-text
keywords: [Alzheimer's dementia, prevalence, incidence, mortality, caregiving, dementia workforce, health care costs, Medicare, Medicaid, biomarkers, early detection, anti-amyloid medications, public attitudes]
claims_summary:
  - "An estimated 7.2 million Americans age 65+ live with Alzheimer's dementia in 2025 (~1 in 9; 11%), rising to a projected 13.8 million by 2060."
  - "Official death certificates recorded 120,122 AD deaths in 2022; AD deaths rose 142.4% from 2000-2022 while most other leading-cause deaths fell; AD ranks as a top-7 cause of death."
  - "In 2024, ~11.9 million unpaid caregivers provided ~19.2 billion hours of care valued at $413.5 billion."
  - "Total 2025 payments for health/long-term/hospice care for people 65+ with dementia are estimated at $384 billion; Medicare/Medicaid cover $246B (64%), out-of-pocket $97B (25%)."
  - "Per-person Medicare payments are ~3x and Medicaid payments ~22x higher for beneficiaries with dementia than without."
  - "The U.S. faces acute dementia-care workforce shortages (e.g., 7,454 certified geriatricians in 2021 vs ~23,953 needed; ~861,000 additional direct care workers needed 2022-2032)."
  - "Alzheimer's risk and prevalence vary by race/ethnicity (19% of Black, 14% of Hispanic vs 10% of White older adults) and sex (two-thirds of people with AD are women)."
  - "Special Report survey (n=1,702, age 45+): 99% consider early diagnosis important, 79% would want to know before symptoms interfere, >9 in 10 would want a simple test, and 64% are aware anti-amyloid medications exist."
  - "Two disease-modifying anti-amyloid drugs (lecanemab, donanemab) slow progression in early-stage disease; as of Jan 1, 2024, 132 disease-modifying trials were underway."
abstract: "This article describes the public health impact of Alzheimer's disease (AD), including prevalence and incidence, mortality and morbidity, use and costs of care, and the ramifications of AD for family caregivers, the dementia workforce, and society. The Special Report discusses Americans' attitudes about early diagnosis and treatment of AD. An estimated 7.2 million Americans age 65 and older live with Alzheimer's dementia today. This number could grow to 13.8 million by 2060, barring the development of medical breakthroughs to prevent or cure AD. Official AD death certificates recorded 120,122 deaths from AD in 2022. Since 2020, when COVID-19 became one of the top 10 causes of death in the United States, AD has ranked as the seventh-leading cause of death. However, 2023 data indicate that Alzheimer's will likely resume its place as the sixth-leading cause of death. Between 2000 and 2022, deaths from stroke, heart disease, and HIV decreased, whereas reported deaths from AD increased by more than 142%. Nearly 12 million family members and other unpaid caregivers provided an estimated 19.2 billion hours of care to people with Alzheimer's or other dementias in 2024. These figures reflect a decline in the number of caregivers compared with a decade earlier and an increase in the amount of care provided by each remaining caregiver. Unpaid dementia caregiving was valued at $413.5 billion in 2024. Its costs, however, extend to unpaid caregivers' increased risk for emotional distress and negative mental and physical health outcomes. Members of the paid health care and broader community-based workforce are involved in diagnosing, treating, and caring for people with dementia. However, the United States faces growing shortages across many segments of the dementia care workforce. Average per-person Medicare payments for services to beneficiaries age 65 and older with AD or other dementias are almost three times as great as payments for beneficiaries without these conditions, and Medicaid payments are more than 22 times as great. Total payments in 2025 for health care, long-term care, and hospice services for people age 65 and older with dementia are estimated to be $384 billion. The Special Report examines how Americans feel about new developments in diagnosing and treating AD."
---

# 2025 Alzheimer's disease facts and figures

## Overview

This is the Alzheimer's Association's annual U.S. statistical report ("2025 Alzheimer's Disease Facts and Figures"), a 119-page synthesis published in *Alzheimer's & Dementia* (2025). It is not an original experimental study; it is an epidemiological / health-economics surveillance report that aggregates public data sources — U.S. Census population projections, the Chicago Health and Aging Project (CHAP), the Health and Retirement Study Harmonized Cognitive Assessment Protocol (HRS-HCAP), the Framingham Heart Study, CDC/NCHS mortality data, the Medicare Current Beneficiary Survey (MCBS), the National 100% Sample Medicare Fee-for-Service claims, the Behavioral Risk Factor Surveillance System (BRFSS), and the Lewin Model — into national and state-level estimates of prevalence, incidence, mortality/morbidity, caregiving, the dementia-care workforce, and the use and costs of care. The 2025 **Special Report** adds a commissioned public-opinion survey (Versta Research / NORC AmeriSpeak; n = 1,702 U.S. adults age 45+) and focus groups on American attitudes toward early detection, diagnosis, and treatment of AD in the era of disease-modifying drugs.

The report is corporately authored by the Alzheimer's Association; individual contributors acknowledged in the report are Joseph Gaugler, Bryan James, Tricia Johnson, Jessica Reimer, Kezia Scales, Sarah Tom, Jennifer Weuve, and Jarmin Yeh.

> **Provenance note on the input file.** The bibliographic record (`metadata.json`) and the supplied `paper.pdf` initially appeared to disagree (an early text extraction surfaced an unrelated ViT/CViT systematic review). On visual rendering, the PDF's page images are unambiguously this Facts-and-Figures report (title page carries DOI 10.1002/alz.70235; 119 pages; all headline figures — 7.2 million, 120,122, $413.5 billion, $384 billion — are present in the rendered pages and the re-extracted text layer, which contains zero content from any other paper). This ARA is a **full-text compile** grounded in the rendered pages and the clean text layer. See `evidence/README.md`.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight motivating the surveillance report |
| [claims.md](logic/claims.md) | 14 falsifiable claims (C01–C14) with grounded numeric sources |
| [concepts.md](logic/concepts.md) | 11 technical terms formally defined |
| [experiments.md](logic/experiments.md) | 9 estimation/analysis plans (E01–E09), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the report's key data sources and anchors |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Estimation methodology, data sources, staging framework |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Analytical environment; all underlying data sources with identifiers and access types | C01–C14 |

No code or released software artifact exists for this report (confirmed in `sources.yaml`); `src/` is limited to `environment.md` per Rule 14 (a prose/analytical synthesis has no capturable source code).

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 15-node research DAG of the report's analytic domains and documented estimation decisions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 26 tables + 27 figures, each with markdown transcription and a rendered PNG |
