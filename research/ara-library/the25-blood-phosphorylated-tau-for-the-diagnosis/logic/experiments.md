# Experiments (Analysis Plans)

> Grounding: abstract-only, directional only. These reconstruct the review's analytical procedures from the abstract's METHODS/FINDINGS. NO exact numbers appear here (they live in claims.md, grounded in the abstract). Procedural detail beyond the abstract is marked "Not available from provided input (no full text)".

## E01: Systematic search, screening, and study inclusion
- **Verifies**: C01, C02, C03, C04, C05
- **Setup**:
  - Design: PRISMA-DTA systematic review, registered with PROSPERO (CRD42023422143).
  - Databases: Embase, MEDLINE, PubMed, Scopus, Web of Science.
  - Search window: articles published from July 1, 1984 up to Dec 9, 2024.
  - Study types: cohort, case-control, cross-sectional, and randomised controlled studies of adults from any setting.
  - Extraction: summary data independently extracted by eight authors.
- **Procedure**:
  1. Search the five databases for studies reporting discriminative accuracy of plasma p-tau biomarkers.
  2. Screen for eligibility; exclude studies lacking a p-tau blood biomarker, lacking an appropriate biological reference standard, lacking diagnostic-accuracy data, including under-18 participants, or reporting duplicate/overlapping data.
  3. Extract 2×2 diagnostic-accuracy data against amyloid-PET, tau-PET, CSF, and neuropathological reference standards.
- **Metrics**: Counts of records identified, assessed, and included; number of unique individuals.
- **Expected outcome**:
  - A large candidate pool is narrowed to a much smaller set of eligible studies contributing tens of thousands of individuals. (Exact counts in problem.md O3, sourced from the abstract.)
- **Baselines**: none (descriptive screening funnel).
- **Dependencies**: none

## E02: Bivariate random-effects meta-analysis of diagnostic accuracy per assay
- **Verifies**: C01, C02, C03, C04, C05
- **Setup**:
  - Model: bivariate random-effects meta-analysis.
  - Stratification: by individual p-tau assay (p-tau217, p-tau181, p-tau205, p-tau212, p-tau231).
  - Reference standards: amyloid-PET, tau-PET, CSF, neuropathology.
- **Procedure**:
  1. Pool paired sensitivity and specificity across studies for each assay.
  2. Derive pooled sensitivity, specificity, diagnostic odds ratio, and AUROC per assay.
  3. Rank assays by discriminative performance.
- **Metrics**: Pooled sensitivity, specificity, diagnostic odds ratio, AUROC (with 95% CIs), per assay.
- **Expected outcome**:
  - One assay (p-tau217) ranks highest on discriminative performance; the others rank below it, with p-tau231 lowest on AUROC/DOR. (Directional; exact pooled values in claims.md.)
- **Baselines**: cross-assay comparison serves as the internal baseline.
- **Dependencies**: E01

## E03: Risk-of-bias assessment (QUADAS-2)
- **Verifies**: C06
- **Setup**:
  - Tool: QUADAS-2.
  - Scope: all included studies.
- **Procedure**:
  1. Rate each included study across QUADAS-2 domains.
  2. Tally the proportion at high risk of bias, noting the dominant reason (threshold derivation).
- **Metrics**: Proportion of studies at high risk of bias; domain-level breakdown.
- **Expected outcome**:
  - A large majority of studies are high risk of bias, driven by not using predefined or externally derived thresholds. (Directional; exact ~90% in claims.md C06.)
- **Baselines**: none.
- **Dependencies**: E01

## E04: Certainty-of-evidence grading (GRADE)
- **Verifies**: C07
- **Setup**:
  - System: GRADE.
  - Scope: pooled diagnostic-accuracy outcomes per assay.
- **Procedure**:
  1. Rate certainty of evidence for each assay's pooled estimates.
  2. Integrate certainty with risk-of-bias findings to frame implementation recommendations.
- **Metrics**: GRADE certainty rating (low/moderate) per assay.
- **Expected outcome**:
  - Certainty is no higher than moderate for the best assays and low for p-tau181, motivating a recommendation for prospective real-world implementation studies. (Directional; per-assay ratings in claims.md.)
- **Baselines**: none.
- **Dependencies**: E02, E03
