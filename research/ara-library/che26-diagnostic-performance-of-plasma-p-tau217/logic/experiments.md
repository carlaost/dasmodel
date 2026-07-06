# Experiments (Analysis Plans)

These are the review/meta-analytic analyses that generate the paper's findings, stated
directionally. NO exact numbers appear here — pooled estimates live in `evidence/`.

## E01: Network meta-analysis of diagnostic accuracy for amyloid-beta positivity
- **Verifies**: C01, C08
- **Setup**:
  - Design: PRISMA-DTA systematic review + random-effects frequentist network meta-analysis (NMA).
  - Nodes: biomarker+platform combinations for Abeta detection (8 nodes: p217_MS, p217_Ratio, p217_ALZpath, p217_Lumi, p217_IA, p217_Lilly, p231_UGOT, p181_IA).
  - Reference comparator: p181_IA (standard p-tau181 immunoassay).
  - Data: extracted AUCs (with 95% CIs, or CIs derived from SE / estimated from N and p-values) from the included datasets.
  - Reference standard: CSF Abeta42/40 or amyloid-PET.
- **Procedure**:
  1. Build the Abeta network geometry (node size ∝ participants, edge thickness ∝ head-to-head comparisons).
  2. Fit a random-effects NMA (netmeta) combining direct and indirect evidence.
  3. Compute each node's mean AUC difference vs. the p181_IA baseline (forest plot).
  4. Rank all nodes by P-score (SUCRA analog).
- **Metrics**: Mean difference (MD) in AUC vs. baseline with 95% CI; P-score ranking; I2 heterogeneity.
- **Expected outcome**:
  - p-tau217 variants (especially MS and ratio) rank above p-tau181 and p-tau231 for Abeta detection.
  - Standard p-tau181 immunoassay ranks lowest.
- **Baselines**: p181_IA reference comparator.
- **Dependencies**: none

## E02: Meta-analysis of the incremental AUC gain from the p-tau217/Abeta42 ratio
- **Verifies**: C02
- **Setup**:
  - Design: pairwise meta-analysis of within-study AUC differences (ratio vs. single-analyte p-tau217) on automated platforms.
  - Data: paired AUCs for ratio and single-analyte measurements from cohorts reporting both.
- **Procedure**:
  1. For each cohort, compute the AUC difference (p-tau217/Abeta42 ratio minus single-analyte p-tau217).
  2. Pool the differences with a random-effects model.
  3. Quantify heterogeneity (I2).
- **Metrics**: Pooled incremental AUC gain (MD) with 95% CI; I2.
- **Expected outcome**:
  - The ratio yields a significant positive incremental AUC gain over single-analyte assays.
  - Between-cohort heterogeneity is negligible.
- **Baselines**: single-analyte p-tau217 on automated platforms.
- **Dependencies**: E01

## E03: NMA for advanced Tau-PET recognition and MCI-to-AD-dementia progression
- **Verifies**: C03, C08
- **Setup**:
  - Design: two separate outcome networks — (a) Tau-PET positivity recognition (6 nodes: p217_MS, p217_Lumi, p217_Lilly, p217_Ratio, p217_IA, p181_IA); (b) MCI-to-AD-dementia progression prediction.
  - Reference comparator: p181_IA.
  - Reference standard: tau-PET (staging); clinical progression MCI→AD dementia (prognosis).
- **Procedure**:
  1. Build each outcome's network geometry.
  2. Fit random-effects NMA per outcome.
  3. Forest plot of AUC improvement vs. p181_IA (Tau-PET); rank nodes by P-score for both outcomes.
- **Metrics**: MD in AUC vs. baseline with 95% CI; P-score ranking per outcome.
- **Expected outcome**:
  - p-tau217 by MS ranks first for both Tau-PET recognition and MCI-to-AD progression.
  - p-tau181 fails to reliably discriminate Tau-PET status (near-lowest rank).
- **Baselines**: p181_IA.
- **Dependencies**: E01

## E04: Disease-stage subgroup analysis (preclinical vs. symptomatic)
- **Verifies**: C04
- **Setup**:
  - Design: subgroup NMA stratified by disease stage — preclinical (asymptomatic) vs. symptomatic (MCI/dementia).
  - Nodes: same biomarker+platform nodes as the primary Abeta network, including p231_UGOT.
- **Procedure**:
  1. Partition datasets by disease stage.
  2. Re-run the Abeta-detection NMA within the preclinical subgroup.
  3. Re-run within the symptomatic subgroup as a sensitivity check on the primary ranking.
  4. Rank nodes by P-score within each subgroup.
- **Metrics**: Stage-stratified P-score rankings.
- **Expected outcome**:
  - p-tau231 achieves the top rank for early amyloidosis in the preclinical subgroup.
  - p-tau217 (MS) remains top-performing in the symptomatic subgroup (stability check).
- **Baselines**: full-continuum ranking (E01).
- **Dependencies**: E01

## E05: Ethnicity subgroup analysis (Han Chinese vs. Western cohorts)
- **Verifies**: C05
- **Setup**:
  - Design: subgroup meta-analysis stratified by ethnicity, isolating the two large Han Chinese cohorts (Huashan, Greater Bay Area) vs. Western cohorts.
  - Data: p-tau217 AUCs from Asian vs. Western datasets.
- **Procedure**:
  1. Partition datasets by cohort ethnicity.
  2. Pool p-tau217 performance within the Han Chinese cohorts and within the Western cohorts.
  3. Compare rankings/AUCs across the two strata.
- **Metrics**: Stratum-specific P-score / AUC for p-tau217.
- **Expected outcome**:
  - p-tau217 performance and rankings are consistent across Han Chinese and Western cohorts.
- **Baselines**: Western-cohort performance.
- **Dependencies**: E01

## E06: Technical platform and matrix efficiency NMA (MS vs. AutoIA vs. manual IA; serum vs. plasma)
- **Verifies**: C06, C07
- **Setup**:
  - Design: NMA of platform/matrix efficiency (Outcome 4) with nodes p217_MS, p217_AutoIA, p217_Serum, p217_IA, p181_IA.
  - Data: AUCs categorized by platform (MS / automated IA / manual IA) and matrix (serum / plasma).
- **Procedure**:
  1. Build the platform/matrix network geometry.
  2. Fit random-effects NMA; produce SUCRA ranking curves.
  3. Rank platforms and matrices by P-score.
- **Metrics**: Platform/matrix P-score ranking.
- **Expected outcome**:
  - Mass spectrometry ranks first for precision.
  - Automated immunoassays outrank manual immunoassays.
  - Serum p-tau217 is comparable to plasma.
- **Baselines**: manual immunoassay; plasma matrix.
- **Dependencies**: E01
