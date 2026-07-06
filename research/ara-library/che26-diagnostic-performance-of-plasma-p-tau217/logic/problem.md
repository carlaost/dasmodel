# Problem Specification

## Observations

### O1: The shift to a biological definition of AD makes blood biomarkers a priority
- **Statement**: The diagnostic criteria for Alzheimer's disease have shifted from a clinical syndrome to a biological construct (the AT(N) framework), emphasizing objective biomarkers of amyloid-beta (Abeta) plaques and tau neurofibrillary tangles. CSF analysis and PET remain the gold standards but their high cost, invasiveness, and limited accessibility hinder widespread use in primary care and population screening.
- **Evidence**: §1 Introduction (Jack Jr et al., 2018; Hansson et al., 2023; Teunissen et al., 2022).
- **Implication**: High-performance blood-based biomarkers (BBMs) are a critical priority for the global AD research community.

### O2: Plasma p-tau isoforms are the most promising BBMs, but the optimal isoform is contested
- **Statement**: Among candidate BBMs, plasma phosphorylated tau (p-tau) species are most promising. Initial studies highlighted p-tau181; more recent evidence suggests p-tau217 and p-tau231 may offer superior accuracy and dynamic range. p-tau217 shows exceptional concordance with CSF/PET; p-tau231 may rise earliest in the preclinical phase; p-tau217 correlates more strongly with longitudinal decline and pathological staging.
- **Evidence**: §1 Introduction (Karikari et al., 2020; Mila-Aloma et al., 2022; Janelidze et al., 2023; Palmqvist et al., 2024; Ashton et al., 2024a,b; Ashton et al., 2021; Mattsson-Carlgren et al., 2023).
- **Implication**: Inconsistent cross-cohort findings sustain an ongoing debate about which isoform is optimal for clinical implementation.

### O3: The analytical platform is a major, unresolved source of heterogeneity
- **Statement**: Immunoprecipitation mass spectrometry (IP-MS) is currently regarded as the benchmark for quantification due to high specificity, but its complexity limits throughput. Novel ultrasensitive immunoassays (Simoa, MSD) and fully automated platforms (Lumipulse) offer greater clinical accessibility. Using the ratio of p-tau to Abeta42 (or non-phospho-tau) may mitigate confounders such as chronic kidney disease.
- **Evidence**: §1 Introduction (Schindler et al., 2019; Ashton et al., 2024a,b; Silva-Spinola et al., 2026; Benedet et al., 2026).
- **Implication**: Platform and measurement method (MS vs. IA; single-analyte vs. ratio) must be compared head-to-head, not assumed equivalent.

### O4: Cross-ethnic performance data are sparse
- **Statement**: Most validation studies were conducted in Western populations; data on biomarker performance in other ethnic groups (particularly Asian populations) remain sparse but are essential for global standardization.
- **Evidence**: §1 Introduction (Mielke et al., 2022; Brickman et al., 2021).
- **Implication**: Generalizability across ethnicities must be tested before global clinical adoption.

### O5: Existing studies are single-center pairwise comparisons
- **Statement**: There is a lack of systematic, quantitative comparisons that simultaneously evaluate different p-tau isoforms, technical platforms, and sample matrices. Most existing studies are single-center or compare limited assay pairs, making it difficult to draw definitive conclusions for clinical guidelines.
- **Evidence**: §1 Introduction (Brum et al., 2023).
- **Implication**: A network approach integrating direct and indirect evidence is needed to rank all options simultaneously.

## Gaps

### G1: No consensus on the optimal p-tau isoform across disease stages
- **Statement**: It is unknown which p-tau isoform (217, 181, or 231) is optimal for detecting Abeta pathology, tau pathology, and predicting cognitive decline, or whether the answer differs by disease stage.
- **Caused by**: O2, O5
- **Existing attempts**: Individual head-to-head studies and pairwise meta-analyses.
- **Why they fail**: They compare limited assay pairs in single cohorts, cannot integrate indirect evidence, and produce inconsistent conclusions.

### G2: No consensus on the optimal analytical platform / matrix
- **Statement**: It is unknown whether MS, automated immunoassay, or ratio-based measurement is optimal, and whether serum is a viable matrix substitute for plasma.
- **Caused by**: O3, O5
- **Existing attempts**: Platform-comparison studies within single cohorts.
- **Why they fail**: No unified ranking spanning platforms and matrices exists.

### G3: Overlapping cohorts threaten the statistical independence of any pooled analysis
- **Statement**: Many high-impact studies reuse the same large longitudinal datasets (BioFINDER-1/2, ADNI, TRIAD, WRAP), so naive pooling would double-count patients and violate statistical independence.
- **Caused by**: O5
- **Existing attempts**: Standard meta-analyses that pool all studies.
- **Why they fail**: They risk overestimating effect sizes by counting the same patients multiple times.

### G4: Unknown generalizability to non-Western populations
- **Statement**: Whether p-tau217 performance holds in Han Chinese cohorts is untested at meta-analytic scale.
- **Caused by**: O4
- **Existing attempts**: A few single-cohort Asian studies.
- **Why they fail**: Not synthesized; underpowered individually.

## Key Insight
- **Insight**: Cast every biomarker+platform combination (e.g., p217_MS, p217_Ratio, p181_IA, p231_UGOT) as a distinct node in a network meta-analysis. This lets direct (head-to-head) and indirect evidence be integrated to rank all options simultaneously with a single reference comparator (p181_IA), across four separate diagnostic outcomes, while a hierarchical cohort-selection rule preserves statistical independence.
- **Derived from**: O5, G1, G2, G3
- **Enables**: A unified P-score (SUCRA-analogous) ranking that resolves the isoform, platform, and matrix debates in one framework, and supports stage-specific clinical recommendations.

## Assumptions
- A1: Reported AUCs (with 95% CIs, or CIs derived from SE / estimated from sample size and p-values) are comparable across studies once mapped to biomarker+platform nodes.
- A2: Selecting the single most comprehensive dataset per cohort yields statistically independent nodes (no patient counted twice).
- A3: A random-effects frequentist NMA (netmeta) adequately accounts for between-study heterogeneity, quantified by the I2 statistic.
- A4: Biologically confirmed reference standards (CSF Abeta42/40, p-tau, or amyloid-/tau-PET) are valid ground truth; studies relying on clinical diagnosis alone are excluded to avoid misclassification bias.
