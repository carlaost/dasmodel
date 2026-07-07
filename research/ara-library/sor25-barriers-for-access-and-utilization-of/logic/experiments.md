# Experiments (Verification / Analysis Plans)

These are declarative plans reconstructed from the review's Methods (§Methods) and Results structure. They are directional only — exact numerical results live in `evidence/`. "Experiment" here means the analytic procedures a PRISMA-guided systematic review uses to build and characterise its evidence base: a multi-database literature search and screening pipeline, a standardised quality-appraisal pass, and a narrative-synthesis/thematic-categorisation pass over the included studies.

## E01: Multi-database systematic search and PRISMA screening pipeline
- **Verifies**: C01, C02
- **Setup**:
  - Design: PRISMA-guided systematic review search and screening.
  - Databases: PubMed/MEDLINE (primary), Embase, PsycINFO (EBSCOhost), Health Technology Assessment Database, Web of Science (Clarivate).
  - Timeframe: publications from 2013 to 2023.
  - Search string: PICO-based ("Alzheimer Disease" OR "Dementia") AND ("Barrier*" OR "Access" OR "Healthcare" OR "Health Care Utilization") AND ("Europ*" [MeSH]) AND (2013/01/01–2023/12/31).
  - Reviewers: five reviewers (MS, CF, MM, FE, IS) for screening; senior reviewer (RP) for conflict resolution.
  - Tooling: Rayyan AI for duplicate removal and blind title/abstract screening.
- **Procedure**:
  1. Run the PICO-based search string against the primary database (PubMed/MEDLINE), then adapt and re-run against secondary databases (Embase, PsycINFO, HTA Database, Web of Science).
  2. Remove duplicates using Rayyan; add records identified via reference mining of three prior systematic reviews.
  3. Independently screen titles/abstracts against the eligibility criteria (Table 1); exclude irrelevant records.
  4. Conduct full-text review of the remaining publications, applying the same eligibility criteria; resolve reviewer conflicts via the senior reviewer.
  5. Extract pivotal information from each included study into a structured spreadsheet.
- **Metrics**: count of records identified, deduplicated, screened, excluded (with reasons), and finally included at each PRISMA stage.
- **Expected outcome**:
  - A funnel from thousands of initially identified records down to a small set of studies meeting all Europe-specific, barrier-focused, non-RCT eligibility criteria.
  - Exclusions concentrate at the title/abstract stage (bulk irrelevance) and, among full-text-reviewed papers, at the "did not analyse barriers" reason.
  - NEVER exact numbers here — see `evidence/tables/table1.md`, `evidence/figures/figure1.md`.
- **Baselines**: none (this is a search/screening procedure, not a comparative study).
- **Dependencies**: none

## E02: MMAT quality appraisal of included studies
- **Verifies**: C03
- **Setup**:
  - Tool: Mixed Methods Appraisal Tool (MMAT), revised 2018 version.
  - Scope: all 29 included studies, scored 0–100% according to their specific design (qualitative / quantitative / mixed-methods) criteria.
  - Reviewers: same five reviewers who conducted screening/extraction.
- **Procedure**:
  1. For each included study, identify its design category (qualitative, quantitative descriptive, or mixed-methods) to select the appropriate MMAT criteria set.
  2. Score each criterion; compute an overall percentage score for the study (for mixed-methods studies, take the score of the weakest component as the overall score).
  3. Flag studies scoring below the 50% threshold for closer scrutiny of how their limitations may affect interpretation of their reported barriers, without automatic exclusion.
- **Metrics**: per-study MMAT percentage score (0–100%); count/proportion of studies at or below the 50% threshold.
- **Expected outcome**: The large majority of included studies achieve the maximum score, with a small minority of mixed-methods/quantitative studies scoring lower due to identifiable sampling, non-response, or reporting limitations. Exact per-study scores in `evidence/tables/table3.md`.
- **Baselines**: MMAT's own qualitative/quantitative/mixed-methods criteria sets serve as the internal reference standard (no external baseline tool used).
- **Dependencies**: E01

## E03: Narrative synthesis and thematic categorisation of identified barriers
- **Verifies**: C04, C10
- **Setup**:
  - Corpus: the 29 included studies' extracted "Identified Barriers" field (Table 3).
  - Approach: narrative synthesis (not meta-analysis, given heterogeneous qualitative/quantitative/mixed designs).
- **Procedure**:
  1. Read each included study's reported barriers and assign it to one or more of the five/six thematic barrier categories (organisational; informational/educational; cultural/stigma-related; logistical; financial).
  2. Aggregate per-category study counts and map them onto the countries/regions (Northern, Western, Southern, Eastern Europe) in which the underlying studies were conducted.
  3. Separately identify and report barrier findings specific to minority/migrant populations within the included studies (e.g., Sikh, Bangladeshi, Somali, Pakistani, Turkish, Polish, Croatian, Indian, Middle Eastern, Eastern European communities).
- **Metrics**: per-category study count (n); qualitative description of category-specific barrier mechanisms per region.
- **Expected outcome**: Organisational barriers are the most prevalent category; barriers recur across Northern, Western, and Southern Europe with region-specific emphases (e.g., minority/migrant-specific cultural barriers concentrated in UK/Denmark/Norway studies). NEVER exact numbers here — see `evidence/tables/table3.md` and `logic/claims.md` C04/C10.
- **Baselines**: none (descriptive narrative synthesis).
- **Dependencies**: E01

## E04: Study-characteristics tabulation and cross-tabulation
- **Verifies**: C05, C06, C07, C08, C09
- **Setup**:
  - Corpus: the 29 included studies.
  - Fields extracted per study (Table 3): first author/year/citation, nation(s) of study, study design, methods, population, sample size/composition, care setting(s), identified barriers, MMAT quality score.
- **Procedure**:
  1. Tabulate each study's metadata fields into a single structured table (Table 3).
  2. Cross-tabulate studies by publication year, country/region, study design/method, population-group combination, and care-setting combination.
  3. Report counts and, where relevant, note combinations spanning multiple categories (e.g., multi-country studies, multi-population studies, multi-setting studies).
- **Metrics**: counts of studies per year, per country/region, per design/method type, per population-group combination, per care-setting combination.
- **Expected outcome**: The evidence base skews qualitative, UK-concentrated, and home-based-care-focused, with a recent (2020–2021) publication concentration. NEVER exact numbers here — see `evidence/tables/table3.md` and `logic/claims.md` C05–C09.
- **Baselines**: none (descriptive tabulation).
- **Dependencies**: E01
