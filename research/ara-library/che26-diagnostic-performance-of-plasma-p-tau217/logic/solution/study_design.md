# Study Design — PRISMA-DTA Systematic Review and Network Meta-Analysis

This file captures the review methodology directionally (search, inclusion, cohort de-overlap, NMA
model, ranking). Pooled numerical results live in `evidence/`; process counts (records screened,
etc.) are transcribed in `evidence/figures/figure1.md` (PRISMA).

## Reporting standard and registration
- Conducted per the PRISMA guidelines for Diagnostic Test Accuracy (PRISMA-DTA).
- Prospectively registered on PROSPERO, registration number **CRD420261327845** (§2 Methods; abstract).

## Search strategy and data sources (§2.1)
- **Databases**: PubMed, Embase, Web of Science, and the Cochrane Library.
- **Date range**: January 1, 2020 to March 2026.
- **Search terms**: controlled vocabulary (MeSH/Emtree) + free text combining three concept groups:
  1. Biomarkers — e.g., "plasma p-tau", "p-tau217", "p-tau181", "p-tau231", "blood-based biomarkers".
  2. Diagnosis/prognosis — e.g., "diagnostic accuracy", "sensitivity", "specificity", "AUC", "prediction".
  3. Disease spectrum — e.g., "Alzheimer's disease", "mild cognitive impairment", "preclinical AD".
- **Language**: no language restrictions.
- **Supplementary searching**: manual screening of reference lists of relevant reviews and of the
  Alzheimer's Association Global Biomarker Standardization Consortium (GBSC) reports.

## Inclusion / exclusion criteria (§2.2)
- **Population**: individuals across the AD continuum — cognitively unimpaired (CU) with AD pathology
  (preclinical AD), MCI, and AD dementia.
- **Index test**: blood-based p-tau biomarkers (plasma or serum) targeting specific phosphorylation
  sites (p-tau217, p-tau181, p-tau231), analyzed on specific platforms (Mass Spectrometry, Simoa,
  Lumipulse, MSD).
- **Reference standard**: a biologically confirmed "gold standard" — CSF biomarkers (Abeta42/40
  ratio, p-tau) or PET (amyloid-PET or tau-PET). Studies relying solely on clinical diagnosis without
  biomarker confirmation were excluded to avoid misclassification bias.
- **Outcome**: reported diagnostic-accuracy metrics — specifically AUC, sensitivity, and specificity.

## Management of overlapping cohorts (§2.3 — "crucial step")
- Problem: many high-impact studies reuse shared datasets (BioFINDER-1/2, ADNI, TRIAD, WRAP); naive
  pooling would violate statistical independence.
- Hierarchical selection rule:
  - For studies on the same cohort, select the publication with the largest sample size OR the most
    comprehensive head-to-head assay comparison (e.g., Janelidze et al., 2023 for BioFINDER and
    Ashton et al., 2024a,b for Round Robin comparisons).
  - Data from the same cohort were included only if they addressed distinct clinical outcomes (e.g.,
    Palmqvist et al., 2024 for primary-care implementation vs. Janelidze et al., 2023 for assay
    technical comparison).
- Result: **24 statistically independent datasets from 18 publications**, ensuring no patient was
  counted twice.

## Data extraction and quality assessment (§2.4)
- Two independent reviewers extracted data with a standardized form: cohort name, sample size, age,
  sex, disease stage, assay platform (IP-MS vs. automated immunoassay), manufacturer (C2N, Fujirebio,
  ALZpath, Lilly), and reference standard.
- For diagnostic accuracy: AUC and its 95% CI were extracted; where CIs were unreported, they were
  calculated from the standard error (SE) or estimated from sample size and p-values.
- Quality/risk of bias: QUADAS-2 (patient selection, index test, reference standard, flow/timing);
  reported in Supplementary Table S1.

## Statistical analysis (§2.5)
- **Method**: random-effects frequentist NMA comparing multiple biomarker classes simultaneously,
  combining direct (head-to-head) and indirect evidence.
- **Network geometry**: node size ∝ sample size; edge thickness ∝ number of direct comparisons; nodes
  categorized by epitope (217 vs. 181) and platform (MS vs. AutoIA).
- **Effect size**: primary effect size = mean difference (MD) in AUC; p-tau181 measured by standard
  immunoassay (p181_IA) set as the reference comparator.
- **Model specification**: random-effects frequentist NMA fitted with the **netmeta** package
  (version 4.5.2) in R (Foundation for Statistical Computing), accounting for between-study
  heterogeneity.
- **Ranking**: P-scores (analogous to SUCRA) computed to rank the diagnostic performance of each
  biomarker; P-scores range 0-1, higher = higher probability of being the best diagnostic test.
- **Subgroup analyses**: stratified by (i) disease stage — preclinical (asymptomatic) vs. symptomatic
  (MCI/dementia); (ii) ethnicity — Han Chinese vs. Western cohorts; (iii) outcome type — Abeta
  pathology (early diagnosis) vs. Tau-PET positivity (staging).
- **Assay-type comparison**: single-analyte vs. ratio-based approaches (e.g., p-tau217/Abeta42).
- **Heterogeneity**: assessed using the I2 statistic.

## Outcomes analyzed (four networks)
1. Outcome 1 — diagnostic accuracy for Abeta pathology (8-node network; Figure 2A).
2. Outcome 2 — progression prediction (MCI-to-AD dementia).
3. Outcome 3 — pathological staging (Tau-PET recognition; 6-node network, Figure 2B).
4. Outcome 4 — technical platform and matrix efficiency (MS vs. AutoIA vs. manual IA; serum vs. plasma).
