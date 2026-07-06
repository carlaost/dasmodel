# Environment

This work is a **purely analytical, prose-and-statistics surveillance report**. There is no software repository, no runnable code, no configuration files, and no released dataset accession associated with it (confirmed in the grounded `sources.yaml`: `code: []`, `data: []`, `clinical_trials: []`). Per Rule 14, no code stub is fabricated; `src/` therefore contains only this reproducibility record.

- **Language/runtime**: Analytical — none. Estimates were produced by the report's authors/contractors using external data sources and models (e.g., the Lewin Model); no code is published with the report.
- **Framework**: n/a (statistical estimation and actuarial/microsimulation modeling by third parties; not released).
- **Hardware**: n/a.
- **Random seeds**: n/a.

## Data sources (with identifiers and access type)

| Source | Role | Identifier / access | Access type |
|--------|------|---------------------|-------------|
| Chicago Health and Aging Project (CHAP) | Headline national prevalence, incidence, projections (via Rajan et al.) | Population-based longitudinal cohort, Chicago; via published estimates | Controlled (research cohort) |
| Health and Retirement Study — HCAP | All-cause dementia & MCI prevalence comparison | HRS Harmonized Cognitive Assessment Protocol | Controlled / application (public-use + restricted) |
| Framingham Heart Study | Sex-specific lifetime risk (via Chene et al.) | Longitudinal cohort | Controlled (application) |
| Dhana et al. (state/county prevalence) | State & county prevalence (Table 5, Figure 5) | Published estimates; county data in Supporting Information of alz.13081 | Open (published supplement) |
| CDC / National Center for Health Statistics | Mortality: death counts, rates, cause-of-death trends, place of death | CDC WONDER / NCHS mortality files (underlying cause) | Open (public data) |
| Medicare Current Beneficiary Survey (MCBS) 2018 | Per-person payments by source/service (Tables 16, 18) | CMS MCBS 2018 (unpublished tabulations) | Controlled (restricted CMS data) |
| National 100% Sample Medicare Fee-for-Service 2019 | Utilization & coexisting-condition costs (Tables 19-21, 24) | CMS 100% FFS claims (unpublished tabulations) | Controlled (restricted CMS data) |
| Behavioral Risk Factor Surveillance System (BRFSS) caregiver module 2016, 2020-2023 | Caregiver counts, hours, health status (Tables 9-12) | CDC BRFSS | Open (public data) |
| U.S. Census Bureau population projections (2024) | Population denominators & projections | Census Bureau projections | Open (public data) |
| National Alliance for Caregiving / AARP; U.S. Dept. of Labor; Genworth Cost of Care | Caregiver characteristics; wage benchmarks; long-term-care costs | NAC/AARP surveys; DOL; Genworth 2023 Cost of Care Survey | Open / commercial report |
| The Lewin Group — Lewin Model | Total & projected national costs, payer mix (Figure 15, Table 22) | Proprietary microsimulation model (endnote A11) | Controlled (proprietary model) |
| Projections Central (long-term occupational projections) | Direct-care workforce projections (Table 15) | projectionscentral.org/longterm (accessed Jan 15, 2025) | Open (public data) |
| American Geriatrics Society; Fried & Hall | Geriatrician supply & need (Table 14) | AGS counts; published need model | Open (published) |
| Versta Research / NORC AmeriSpeak panel | Special Report public-attitudes survey (Figures 19-26) | Commissioned probability-panel survey, n=1,702, age 45+, fielded Nov 7-18, 2024 | Controlled (commissioned; microdata not released) |
| L&M Policy Research | Special Report focus groups | 11 groups, 69 participants | Controlled (commissioned) |

## Clinical trials referenced (not registered by this article)
- No clinical trial is registered to or reported by this article; `sources.yaml` lists `clinical_trials: []` and no NCT identifiers appear in the report.
- The report *references* trial infrastructure and counts as context: **ALZ-NET** (Alzheimer's Network for Treatment and Diagnostics; alz-net.org — a voluntary provider-enrolled patient registry, not an NCT trial); 132 disease-modifying and 30 symptomatic trials underway as of Jan 1, 2024 (aggregate counts, individual NCT ids not enumerated in the report); the CMS **GUIDE Model** (a Medicare payment model, launched July 1, 2024, 390 participating organizations); and the NIA **IMPACT Collaboratory** and **National Dementia Workforce Study (NDWS)**. None of these constitutes a released dataset accession.

## Protocols / reporting
- No preregistration or analysis-code release. Estimation methodology is described narratively in the report's sections and endnotes (A1-A16). See `logic/solution/study_design.md`.
- License: Open Access, Creative Commons Attribution-NonCommercial-NoDerivs (CC BY-NC-ND); PMCID PMC12040760; DOI 10.1002/alz.70235.
