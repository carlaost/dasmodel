# Problem Specification

## Observations

### O1: Plasma p-tau217 is the most accurate blood marker for AD, but on research assays
- **Statement**: Plasma p-tau217 consistently discriminates AD from non-AD cognitive disorders with ROC AUCs typically > 0.90, better than p-tau181, approaching CSF/PET accuracy. A recent meta-analysis reported pooled AUC 0.911 (95% CI 0.889–0.924) for p-tau217 vs 0.815 (0.802–0.829) for p-tau181 in cognitively impaired patients.
- **Evidence**: §Background; §Discussion citing meta-analysis [14] (refs 13–15).
- **Implication**: p-tau217 is the target analyte, but most evidence comes from batch/research-use assays (Fujirebio, Quanterix, ALZPath).

### O2: Elecsys p-tau217 data are scarce despite the platform being routine-ready
- **Statement**: The Roche Elecsys system is a fully automated, high-throughput platform already widely available in clinical labs. Elecsys p-tau181 shows moderate-to-high accuracy (AUCs 0.80–0.89, up to 0.93 in panels), and in Oct 2025 the FDA cleared Elecsys p-tau181 as a rule-out test (NPV 97.9%). But data on Elecsys p-tau217 remain scarce.
- **Evidence**: §Background (refs 16–20); meta-analysis [14] did not include Elecsys p-tau217.
- **Implication**: Establishing Elecsys p-tau217 diagnostic performance is a key next step for routine implementation.

### O3: Modifiers of p-tau interpretation are uncertain
- **Statement**: The incremental value of APOE-ε4 testing, the contribution of Aβ42/40 ratios, and the influence of age, renal function, and small-vessel disease (CAA, white-matter hyperintensities) on plasma p-tau vary across cohorts.
- **Evidence**: §Background (refs 21–31).
- **Implication**: A memory-clinic evaluation must also quantify these covariates and add-ons.

### O4: Cross-sectional accuracy is established; real-world prognostic value is not
- **Statement**: Longitudinal studies link higher p-tau217 to faster cognitive decline, but prognostic value in real-world memory-clinic settings remains undetermined.
- **Evidence**: §Background (refs 32–34).
- **Implication**: Baseline p-tau217 should be tested against longitudinal cognition (MoCA).

## Gaps

### G1: No established diagnostic performance for automated Elecsys p-tau217
- **Statement**: There is little head-to-head evidence for plasma p-tau217 measured on the fully automated Roche Elecsys platform against a CSF reference standard in a real-world memory clinic.
- **Caused by**: O1, O2
- **Existing attempts**: Research/batch assays (Fujirebio Lumipulse, ALZpath, Lilly, Janssen SIMOA, WashU MS) benchmarked; Elecsys p-tau181 evaluated; Elecsys p-tau217 largely absent from comparisons.
- **Why they fail**: Batch assays are less suited for routine high-throughput use; Elecsys p-tau217 not yet characterized for diagnostic accuracy, cut-offs, or grey-zone behavior.

### G2: Unclear added value of APOE-ε4 and Aβ42 for classifying borderline cases
- **Statement**: Whether adding blood-based APOE-ε4 carrier status or Aβ42/Aβ42-40 to p-tau217 meaningfully improves discrimination and reduces intermediate ("grey-zone") results is unresolved.
- **Caused by**: O3
- **Existing attempts**: Cohort reports with mixed/modest effects (refs 21–25); Lumipulse p-tau217/Aβ42 FDA-cleared May 2025 [50].
- **Why they fail**: Effects are cohort- and platform-dependent; not tested for Elecsys p-tau217 with a two-cut-off framework.

### G3: Confounding and physiological modifiers not disentangled in memory clinic
- **Statement**: It is unclear whether Elecsys p-tau217 in a typical memory-clinic population reflects disease vs physiological variation (age, sex, renal function, small-vessel disease), and whether cognitive severity confounds diagnostic associations.
- **Caused by**: O3
- **Existing attempts**: Reports of renal-function effects mostly at advanced CKD (refs 26, 29); weak MRI/small-vessel associations (refs 27, 30, 31).
- **Why they fail**: Effects reported at CKD stages/populations not represented; MoCA confounding not addressed.

## Key Insight
- **Insight**: A fully automated, high-throughput Elecsys p-tau217 immunoassay can achieve diagnostic accuracy comparable to the best research/batch p-tau217 assays in a real memory-clinic cohort, and a two-cut-off (grey-zone) framework plus blood-based APOE-ε4 turns high AUC into clinically actionable classification with a small indeterminate zone.
- **Derived from**: O1, O2, O3
- **Enables**: Direct head-to-head evaluation (Elecsys p-tau217 vs Lumipulse p-tau217 vs Elecsys p-tau181) against a CSF reference standard, with cut-off strategies, APOE-ε4/Aβ42 add-ons, cofactor regression, and exploratory longitudinal analysis.

## Assumptions
- A1: CSF biomarkers (Aβ42/40 ratio, total tau, p-tau181; amyloid-PET in a minority) provide a valid reference standard for AD pathology.
- A2: Manufacturer/reference-lab CSF cut-offs (Aβ42/Aβ40 ≤ 0.070, Aβ42 ≤ 722 pg/mL, p-tau181 ≥ 50 pg/mL, total tau ≥ 403 pg/mL) correctly classify AD vs non-AD.
- A3: The CCUG single-centre, predominantly Belgian cohort is representative enough to estimate diagnostic performance (acknowledged limitation: no external validation).
- A4: Plasma-based APOE-ε4 proteotyping (carrier vs non-carrier) is an acceptable surrogate for APOE-ε4 genotype.
- A5: MoCA is an adequate (if limited) longitudinal cognitive outcome for the exploratory decline analysis.
