# Related Work — Typed Dependency Graph

Type legend: `imports` (uses directly), `extends` (builds on/updates), `bounds` (defines methodological limits), `baseline` (comparator), `refutes`. Full `RW` blocks for works with a specific technical delta; brief entries below preserve the paper's full 78-reference footprint.

## RW01: Pahlke SC, et al. — Companion systematic review & meta-analysis (ref 19)
- **DOI**: Not available (Alzheimer's & Dementia, "Submitted")
- **Type**: imports
- **Delta**:
  - What changed: This CPG's entire quantitative evidence base — pooled Sn/Sp per BBM test, sensitivity analyses, and the certainty/evidence profiles — comes from this separately published systematic review of diagnostic test accuracy in cognitively impaired individuals in specialty care.
  - Why: The CPG provides recommendations; the systematic review provides the underlying evidence, kept living via MAGICapp.
- **Claims affected**: C01, C02, C03, C04, C05
- **Adopted elements**: Study selection, meta-analysis of pooled Sn/Sp at Youden cutoff, sensitivity analyses (Tables S2/S3).

## RW02: Schindler SE, Galasko D, Pereira AC, et al. — CEOi acceptable BBM performance (ref 15)
- **DOI**: 10.1038/s41582-024-00977-5 (Nat Rev Neurol, 2024)
- **Type**: extends
- **Delta**:
  - What changed: The Global CEO Initiative (CEOi) recommendations for minimum acceptable BBM test performance were used as the **starting point** for the panel's clinically acceptable Sn/Sp thresholds.
  - Why: To anchor triage/confirmatory thresholds in prior expert opinion before formal EtD deliberation.
- **Claims affected**: C01, C02
- **Adopted elements**: Expert-opinion performance targets; the caution that a poor assay yields a large indeterminate zone under two cutoffs.

## RW03: Hansson O, Edelmayer RM, Boxer AL, et al. — 2022 Alzheimer's Association BBM appropriate use recommendations (ref 18)
- **DOI**: 10.1002/alz.12756 (Alzheimers Dement, 2022)
- **Type**: extends
- **Delta**:
  - What changed: The field's first appropriate-use recommendations for BBMs; this CPG advances beyond appropriate-use recommendations to a formal, systematic-review-grounded, GRADE-based guideline.
  - Why: An appropriate-use recommendation is not a formal CPG (identified gap G1).
- **Claims affected**: C01, C02
- **Adopted elements**: Framing of BBM roles in clinical practice.

## RW04: Jack CR, Andrews JS, Beach TG, et al. — Revised AD diagnosis/staging criteria (ref 3)
- **DOI**: 10.1002/alz.13859 (Alzheimers Dement, 2024)
- **Type**: imports
- **Delta**:
  - What changed: Revised criteria incorporating BBMs into AD diagnosis and staging; provides the biological definition of AD (amyloid/tau) the CPG operates within.
  - Why: Grounds the pathology target that BBMs aim to detect.
- **Claims affected**: C01, C02
- **Adopted elements**: Biomarker-based AD definition.

## RW05: GRADE methodology (refs 25, 27, 28, 29, 30)
- **DOI**: 10.1136/bmj.i2089 (Alonso-Coello et al., EtD frameworks, ref 27); 10.1016/j.jclinepi.2010.07.015 (Balshem et al., rating quality, ref 28); refs 29/30 (going from evidence to recommendations); ref 25 (Guyatt et al., "what is quality of evidence")
- **Type**: imports
- **Delta**:
  - What changed: GRADE certainty rating and the Evidence-to-Decision framework are the methodological engine for both certainty assessment and recommendation formulation (strong vs conditional).
  - Why: Provides a transparent, structured evidence-to-recommendation process.
- **Claims affected**: C01, C02, C05, C07
- **Adopted elements**: Certainty categories (Table 1), EtD factor structure, strong/conditional labeling.

## RW06: Whiting PF, Rutjes AWS, Westwood ME, et al. — QUADAS-2 (ref 78)
- **DOI**: 10.7326/0003-4819-155-8-201110180-00009 (Ann Intern Med, 2011)
- **Type**: bounds
- **Delta**:
  - What changed: QUADAS-2 defines the risk-of-bias appraisal for diagnostic accuracy studies; used to identify the risk-of-bias downgrades that dominated certainty rating-down.
  - Why: Establishes the quality/risk-of-bias assessment standard.
- **Claims affected**: C05
- **Adopted elements**: Risk-of-bias domains for diagnostic accuracy studies.

## RW07: Ashton NJ, Keshavan A, Brum WS, et al. — GBSC plasma phospho-tau Round Robin (ref 23)
- **DOI**: 10.1002/alz.14508 (Alzheimers Dement, 2025)
- **Type**: imports
- **Delta**:
  - What changed: Head-to-head Round Robin results informed the panel's selection of the p-tau species with the strongest evidence base and highest diagnostic accuracy.
  - Why: To prioritize analytes for the review.
- **Claims affected**: C03, C04
- **Adopted elements**: Comparative analyte performance evidence.

## RW08: Head-to-head plasma p-tau217 comparisons (refs 16, 17)
- **DOI**: 10.1093/brain/awae346 (Warmenhoven et al., ref 16, medRxiv preprint); 10.1002/alz.14315 (Schindler et al., ref 17)
- **Type**: baseline
- **Delta**:
  - What changed: Provide direct head-to-head comparisons of leading blood tests, documenting that diagnostic performance varies across available tests.
  - Why: Motivates the brand-agnostic, per-test evaluation (a test = analyte × technology).
- **Claims affected**: C03
- **Adopted elements**: Cross-platform performance-variability evidence.

## RW09: Rohatgi A. — WebPlotDigitizer v4.6 (ref 24)
- **DOI**: Not available (software; https://automeris.io/, v4.6, 2021)
- **Type**: imports
- **Delta**:
  - What changed: Tool used to derive Sn/Sp at Youden's index from published ROC curves when raw data were neither published nor author-provided.
  - Why: Enables data extraction for the meta-analysis (see src/environment.md, E01).
- **Claims affected**: C03, C04
- **Adopted elements**: ROC-curve digitization.

## RW10: Jansen WJ, Janssen O, Tijms BM, et al. — Amyloid prevalence across the AD spectrum (ref 26)
- **DOI**: 10.1001/jamaneurol.2021.5216 (JAMA Neurol, 2022)
- **Type**: imports
- **Delta**:
  - What changed: Evidence that pretest probability / amyloid prevalence varies by clinical presentation, age, and risk factors — underpinning the panel's decision not to report per-test predictive values.
  - Why: Justifies pretest-probability-dependent interpretation (C06).
- **Claims affected**: C06
- **Adopted elements**: Prevalence estimates informing pretest probability.

## RW11: Reporting/development checklists (refs 20, 21)
- **DOI**: BMJ 2016;352:i1152 (AGREE Reporting Checklist, ref 20); CMAJ 2014;186(3):E123-E142 (GIN-McMaster, ref 21)
- **Type**: bounds
- **Delta**:
  - What changed: Define the guideline-development and reporting standards the CPG conformed to.
  - Why: Ensures methodological rigor and transparency.
- **Claims affected**: (methodological — governs the whole guideline)
- **Adopted elements**: AGREE II reporting items; GIN-McMaster development checklist.

## Brief citation footprint (no distinct technical delta beyond the above)

**Background / context**: ref 1 (2025 AD Facts & Figures); ref 2 (Hansson, Nat Med 2021, biomarkers for neurodegenerative disease); ref 4 (Beach et al., accuracy of clinical AD diagnosis); ref 5 (Palmqvist et al., JAMA 2024, BBMs in primary/secondary care — also a primary study); ref 6 (Rabinovici et al., amyloid PET & management, JAMA 2019); ref 7 (Dickerson et al., DETeCD-ADRD guideline); ref 8 (VandeVrede & Schindler, biomarkers in the treatment era); ref 14 (Hansson et al., Nat Aging 2023, BBMs in clinical practice/trials); ref 22 (Rabinovici et al., updated amyloid/tau PET appropriate use criteria); ref 77 (Verberk et al., SABB pre-analytical sample handling — informs feasibility).

**Anti-amyloid therapies requiring biomarker confirmation** (refs 9–13): van Dyck et al. (lecanemab, ref 9); Sims et al. (donanemab TRAILBLAZER-ALZ 2, ref 10); Budd Haeberlein et al. (aducanumab phase 3, ref 11); Cummings et al. (lecanemab appropriate use, ref 12); Rabinovici et al. (donanemab appropriate use, ref 13).

**Primary diagnostic-accuracy studies feeding the systematic review** (49 observational studies; refs 5, 16, 17, 31–76): a body of cross-sectional/longitudinal studies of plasma p-tau217, %p-tau217, p-tau181, p-tau231, and Aβ42/40 versus amyloid PET / CSF / neuropathology across cohorts (e.g., ADNI, AIBL, BioFINDER-related, memory-clinic cohorts). Individually they are the row-level evidence pooled in RW01; none is a distinct methodological dependency of the CPG itself. Type: `baseline`/`imports` (data providers). Affected claims: C03, C04.

## Datasets and Clinical Trials (typed data dependencies)
Per `sources.yaml` (verified; do not re-verify): **no released dataset** and **no registered clinical trial** are associated with this guideline. `code: []`, `data: []`, `clinical_trials: []`.
- **Data dependency (type: imports, access: controlled/aggregated)**: The evidence base is the 49 primary studies' extracted 2×2 accuracy data (TP/TN/FP/FN), aggregated in the companion systematic review (RW01). No accession IDs (no ADNI/UK Biobank/BioFINDER/GEO/SRA/EGA identifier is released by this work).
- **Living-evidence resource (type: imports, access: open)**: MAGICapp guideline instance `nyO1Yj` (https://app.magicapp.org/#/guideline/nyO1Yj) — a hosting/authoring platform for the living guideline and its evidence summary, not a code repository or dataset.
- **No PROSPERO ID, NCT ID, or software repository** appears in the paper's full text.
