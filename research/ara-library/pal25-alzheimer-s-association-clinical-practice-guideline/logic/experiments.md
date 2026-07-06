# Experiments (Verification / Analysis Plans)

These are declarative plans reconstructed from the guideline's Methods (§2) and the companion systematic review it relies on (ref 19). They are directional only — exact numerical results live in `evidence/`. "Experiment" here means the analytic procedures a diagnostic-accuracy systematic review and a GRADE guideline use to test each claim.

## E01: Systematic review + diagnostic-accuracy meta-analysis (single Youden cutoff)
- **Verifies**: C01, C02, C03, C04
- **Setup**:
  - Design: Systematic review of diagnostic test accuracy of plasma BBMs vs reference standards, feeding a GRADE guideline.
  - Population: Individuals with objective cognitive impairment (MCI or dementia) in specialized care; combined impaired+unimpaired-population studies excluded.
  - Index tests: plasma p-tau217, %p-tau217, p-tau181, p-tau231, Aβ42/40 (analyte × technology combinations).
  - Reference standards: CSF AD biomarkers, amyloid PET, or AD neuropathology.
  - Data sources: PubMed, Medline, Embase, Cochrane Library, searched 2019 through November 3, 2024.
- **Procedure**:
  1. Search databases; screen and select studies (methodologists); extract TP, TN, FP, FN, Sn, Sp at the Youden-index cutoff.
  2. Where raw data missing, request from authors; where still missing, derive Sn/Sp at Youden's index from ROC curves using WebPlotDigitizer.
  3. Meta-analyze per BBM test to obtain pooled Sn and Sp at the single Youden cutoff.
  4. Judge each test against the triaging (Sn ≥90%, Sp ≥75%) and confirmatory (Sn ≥90%, Sp ≥90%) thresholds.
- **Metrics**: pooled sensitivity (%), pooled specificity (%), count of tests meeting each threshold.
- **Expected outcome**:
  - Wide variability in pooled Sn/Sp across tests; a subset of tests meets or exceeds the thresholds at a single cut-point while many do not.
  - NEVER exact numbers (see evidence/tables and the companion review).
- **Baselines**: Reference standards (CSF, amyloid PET, neuropathology).
- **Dependencies**: none

## E02: Sensitivity analyses on cutoff/data-handling robustness
- **Verifies**: C03
- **Setup**: Same corpus as E01; four alternative analytic configurations.
- **Procedure**:
  1. Reported data only, using any cutoff for the index test.
  2. Reported data using any cutoff plus data derived from ROC curves at Youden's index when missing.
  3. Fix specificity cutoff at 75% (triaging) and recompute sensitivity.
  4. Fix sensitivity cutoff at 90% (confirmatory) and recompute specificity.
- **Metrics**: pooled Sn/Sp under each configuration; stability of threshold-meeting status.
- **Expected outcome**: Directional assessment of how robust each test's threshold status is to cutoff choice and missing-data handling. Results reported in Table S3 (Supporting Information).
- **Baselines**: Main Youden-index analysis (E01).
- **Dependencies**: E01

## E03: GRADE certainty-of-evidence assessment
- **Verifies**: C05
- **Setup**: Per-test evidence profiles across the five GRADE domains.
- **Procedure**:
  1. For each test, assess risk of bias, indirectness, inconsistency, imprecision, and publication bias.
  2. Rate certainty separately for Sn and Sp, weighting Sn for triaging and Sp for confirmatory contexts.
  3. Summarize certainty per test in Evidence Profiles.
- **Metrics**: certainty category per test (high / moderate / low / very low) for Sn and Sp; dominant downgrade domain; presence/absence of publication bias.
- **Expected outcome**: Certainty concentrated at the lower end (low to very low for threshold-meeting tests), dominated by risk-of-bias downgrades; publication bias not detected.
- **Baselines**: GRADE certainty categories (Table 1).
- **Dependencies**: E01

## E04: Predictive-value analysis across pretest probabilities
- **Verifies**: C06
- **Setup**: Analytic (Bayesian) calculation, not an empirical study.
- **Procedure**:
  1. Fix Sn/Sp at the triage thresholds (90%/75%) and at the confirmatory thresholds (90%/90%).
  2. Compute PPV and NPV at pretest probabilities of 20%, 50%, and 80%.
- **Metrics**: PPV (%) and NPV (%) at each pretest probability.
- **Expected outcome**: PPV rises and NPV falls as pretest probability increases; the same test yields materially different predictive value across populations. Exact values in evidence / §2.5.1.
- **Baselines**: none
- **Dependencies**: none

## E05: Evidence-to-Decision (EtD) framework assessment
- **Verifies**: C01, C02, C07, C08
- **Setup**: GRADE EtD framework for diagnostic test accuracy; panel deliberation informed by the systematic review plus non-systematic searches, health-economist input, and patient/advisory-group (ESAG) and public-comment input.
- **Procedure**:
  1. For each EtD factor — test accuracy, certainty, balance of benefits/harms, values/preferences, resources, cost-effectiveness, equity, acceptability, feasibility — document judgments and supporting evidence (Table S1).
  2. Blind the panel to test names until recommendations were drafted.
  3. Derive the direction and strength (conditional) of each recommendation and the good practice statement.
- **Metrics**: qualitative EtD judgments per factor; recommendation direction and strength.
- **Expected outcome**: Balance of effects favors BBM use when a threshold-meeting test is used by a trained specialist; recommendations are conditional; a good practice statement constrains use to after comprehensive clinical evaluation.
- **Baselines**: Reference standards (CSF, PET) and no-testing.
- **Dependencies**: E01, E03

## E06: Cost / cost-effectiveness comparison of BBM tests
- **Verifies**: C07
- **Setup**: Non-systematic literature review plus publicly available price sources; methodologists working with health economists.
- **Procedure**:
  1. Compare prices of commercially available BBM tests using publicly available sources.
  2. Review peer-reviewed cost-effectiveness studies of BBM testing in the AD diagnostic workup.
  3. Summarize resource savings versus PET/CSF and assess whether a cost-effectiveness judgment is possible.
- **Metrics**: relative cost of BBMs vs PET/CSF; availability of cost-effectiveness evidence.
- **Expected outcome**: BBMs cost substantially less than PET; resource savings judged moderate; cost-effectiveness could not be judged due to insufficient/variable data.
- **Baselines**: PET and CSF costs.
- **Dependencies**: E05
