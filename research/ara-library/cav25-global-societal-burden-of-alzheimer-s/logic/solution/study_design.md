# Study Design

## Objective
- Characterize the total societal economic burden of AD, broken down by care setting and disease severity, through a targeted literature review (TLR).
- Explore four research topics: (1) cost of care across disease stages; (2) cost of community care versus institutional care; (3) characterization of caregiver burden costs as part of indirect costs; (4) characterization of societal cost burdens reflecting dementia-related deteriorating capabilities to carry out everyday tasks.

## Search Strategy
- **Databases**: MEDLINE and Embase, searched according to PRISMA-S (Preferred Reporting Items for Systematic reviews and Meta-Analyses literature search extension) guidelines.
- **Timeframe**: January 1, 2013 to June 12, 2024, for systematic reviews, meta-analyses, cost-of-illness, and observational studies in the English language reporting costs of MCI or discrete AD stages (mild to severe) in adults.
- **Two-pronged search**: (1) an AD-specific search (3531 hits); (2) a secondary, broader-dementia search expanding the population criterion to any dementia (168 hits), run "to optimize the capture of studies reporting on costs related to AD."
- **Grey literature**: Hand-searched in parallel (patient advocacy reports, organisation websites, citation searching); yielded 113 additional records sought via a separate identification stream (per Fig. 2).
- **Ethics**: No ethics approval required, as the review analyzes only previously published literature.

## Screening and Selection Process (Fig. 2, PRISMA flow diagram)
- Database stream: 4925 total records identified (Medline 1513 + Embase 3412) in the AD-specific search minus 1394 duplicates; 357 total records (Medline 180 + Embase 177) in the broader-dementia search minus 189 duplicates; 3699 total records screened; 3247 excluded at screening; 452 records sought for retrieval and assessed for eligibility; 367 excluded for "not quantitative or no discrete severity groupings," 1 excluded as non-English, 8 excluded for study design; 76 studies included from the database stream (59 articles, 1 report, 16 SLRs).
- Grey-literature stream: 113 additional records identified (9 websites, 3 organisations, 101 via citation searching/expanded population criteria); 13 records sought for retrieval, 112 not retrieved; 5 records assessed for eligibility; 7 excluded for no quantitative/defined severity categories, 1 excluded for population; 5 additional records included (1 report, 4 SLRs).
- **Total included**: 81 studies (59 prospective/retrospective articles + 2 AD reports [1 database-stream + 1 grey-literature-stream] + 20 SLRs/meta-analyses [16 database-stream + 4 grey-literature-stream]).
- **Screening process**: Single reviewer screened titles/abstracts against PICOS criteria (Table 1); full-text articles of potentially relevant citations retrieved and reviewed by the same single reviewer for formal inclusion; a second reviewer performed selective quality-assurance checking; a third independent reviewer resolved disagreements between reviewers 1 and 2.

## Cost Definitions (Methods, "Definitions of Cost Types")
- **Direct medical costs**: Healthcare expenditures — inpatient medical care, outpatient care, medications (AD-specific and for comorbidities).
- **Direct non-medical costs**: Financial aid received by caregivers and social costs for patients (institutional care, daycare, caregiver respite), plus recently published categories not typically considered in AD economic analysis (police call-outs, financial delinquencies).
- **Indirect costs**: Primarily caregiver's loss of productivity/leisure time due to time spent caring for or supervising the patient, and, where reported, the patient's own loss of productivity. Four costing methods considered: opportunity, replacement, human capital, and friction costing (Table 2). Most studies considered costs incurred by a single or primary caregiver only. Also includes recently reported burdens: quality-of-life (QoL) losses (mental/emotional strain) and public fiscal losses incurred by patient and caregiver.
- See [logic/solution/cost_taxonomy.md](cost_taxonomy.md) for the full cost-component hierarchy (Fig. 1).

## Data Extraction and Standardization Rules (Methods, "Data Extraction")
- Cost data extracted as reported, with **no modification of cost year or currency**.
- Unit standardization: PPPM (per person per month) costs multiplied by 12 to obtain PPPY (per person per year); caregiver burden units converted to hours per person per week.
- Where a cost was reported as a range within a severity category, the **median value** was calculated and reported.
- Percentage change in societal cost when progressing from MCI→mild, mild→moderate, or moderate→severe AD was calculated for studies reporting broken-down costs.
- Disease severity harmonization for reporting purposes, regardless of the study's original staging scale: MCI = studies defining a health state as "very mild"; moderate = mild-to-moderate AD; severe = moderately severe/severe AD and "very severe" AD.
- Caregiver profile metrics (mean age, % female, relationship to patient, living arrangement, employment status) averaged across studies reporting each metric per severity bucket.
- Weekly informal caregiving-hour ranges visualized via stacked bagplots (lower/upper bound by setting and disease stage).
- Cost-component proportions (for studies with granular breakdowns) individually calculated per study by dividing each component by the total summed cost for that severity, then normalized across studies by dividing by the total sum of proportions for that severity.

## Visualization / Analysis Tools
- Microsoft Excel and RStudio version 4.4.1, using the R packages dplyr, ggplot2, and the broader tidyverse, plus ggalluvial for alluvial-style plots (Methods, citing refs. [38–41]).

## Data Availability
- "All data generated or analyzed during this study are included in this published article/as supplementary information files." Supplementary tables S1–S8 (referenced throughout the Results, e.g., Table S1a/b for search strategy details, Table S2 for study characteristics, Tables S3/S5/S6/S7/S8 for extended severity/region/setting breakdowns, Figure S1/S2 for extended cost-breakdown figures) are **not included in the provided `paper.pdf`** and are therefore not captured in this ARA's evidence layer beyond what the main text quotes from them (see [evidence/README.md](../../evidence/README.md)).
