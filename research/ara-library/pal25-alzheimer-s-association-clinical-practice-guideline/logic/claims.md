# Claims

All numbers are copied exactly from the guideline text (paper.pdf). Threshold values set by the panel are tagged `[input]`; values produced by the systematic review / meta-analysis or illustrative calculations are tagged `[result]`.

## C01: Triaging-test recommendation
- **Statement**: In patients with objective cognitive impairment presenting for specialized memory-care, a BBM test with at least 90% sensitivity and at least 75% specificity (against a reference standard of CSF AD biomarkers, amyloid PET, or AD neuropathology) can be used as a triaging test in the diagnostic workup of AD. This is a conditional recommendation ("the panel suggests") based on low certainty evidence.
- **Status**: supported (as a conditional, low-certainty recommendation)
- **Falsification criteria**: The claim is disproved if the guideline's stated triaging threshold is not ≥90% Sn and ≥75% Sp, or if the recommendation is not conditional/low-certainty, or if no BBM test achieves these thresholds against the reference standards.
- **Proof**: [E01, E05]
- **Evidence basis**: Table 2 states the recommendation and footnote b defines the threshold; §2.5.1 and Abstract restate it.
- **Interpretation**: A negative triaging result is intended to rule out AD pathology with high probability, while a positive result should be confirmed by another method (CSF or amyloid PET).
- **Dependencies**: C04
- **Sources**:
  - Sn ≥90% (triage) ← paper.pdf Table 2 footnote b / §2.5.1 «The panel defined acceptable diagnostic test accuracy for triaging to be at least 90% sensitivity and 75% specificity for a reference test (CSF AD biomarkers, amyloid PET, or AD neuropathology)» [input]
  - Sp ≥75% (triage) ← paper.pdf §5 Conclusion «BBM tests with ≥90% sensitivity and ≥75% specificity can be used as a triaging test» [input]
  - "conditional recommendation, Low certainty evidence" ← paper.pdf Table 2 «(Conditional recommendation, Low certainty evidence)» [result]
- **Tags**: recommendation, triaging, thresholds, GRADE

## C02: Confirmatory-test recommendation
- **Statement**: In patients with objective cognitive impairment presenting for specialized memory-care, a BBM test with at least 90% sensitivity and at least 90% specificity (against a reference standard of CSF AD biomarkers, amyloid PET, or AD neuropathology) can serve as a confirmatory test — a substitute for CSF analysis or amyloid PET — in the diagnostic workup of AD. This is a conditional recommendation based on low certainty evidence.
- **Status**: supported (as a conditional, low-certainty recommendation)
- **Falsification criteria**: Disproved if the stated confirmatory threshold is not ≥90% Sn and ≥90% Sp, or the recommendation is not conditional/low-certainty.
- **Proof**: [E01, E05]
- **Evidence basis**: Table 2 states the recommendation and footnote e defines the threshold; §2.5.1 and Abstract/Conclusion restate it.
- **Interpretation**: For a confirmatory test, a negative result rules out AD pathology and a positive result confirms it with high probability, without requiring additional biomarker assessment.
- **Dependencies**: C04
- **Sources**:
  - Sn ≥90% (confirmatory) ← paper.pdf Table 2 footnote e «The panel defined acceptable diagnostic test accuracy for confirmatory testing to be at least 90% sensitivity and 90% specificity for a reference test (CSF AD biomarkers, amyloid PET, or AD neuropathology)» [input]
  - Sp ≥90% (confirmatory) ← paper.pdf §5 Conclusion «BBM tests with ≥90% sensitivity and specificity can serve as a substitute for amyloid PET imaging or CSF AD biomarker testing» [input]
- **Tags**: recommendation, confirmatory, thresholds, GRADE

## C03: High variability in diagnostic test accuracy across evaluated tests
- **Statement**: Across all 31 evaluated BBM tests, pooled sensitivity ranged from 49.31% to 91.41% and pooled specificity ranged from 61.54% to 96.72%; many commercially available tests do not meet the panel's thresholds, especially using a single cutoff.
- **Status**: supported
- **Falsification criteria**: Disproved if the reported pooled Sn/Sp ranges differ from these values, or if the majority of tests did meet thresholds at a single cutoff.
- **Proof**: [E01, E02]
- **Evidence basis**: §3.4 reports the pooled ranges across all 31 tests; §3.2 states 31 tests were evaluated; Abstract/Conclusion note many tests do not meet thresholds with a single cutoff.
- **Interpretation**: Because many plasma tests fall short with a single cut-point, the field is moving toward alternate paradigms such as two-cutoff approaches.
- **Dependencies**: none
- **Sources**:
  - pooled Sn range 49.31%–91.41% ← paper.pdf §3.4 «Across all 31 tests, pooled Sn ranged from 49.31% to 91.41%» [result]
  - pooled Sp range 61.54%–96.72% ← paper.pdf §3.4 «and Sp ranged from 61.54% to 96.72%» [result]
  - 31 tests ← paper.pdf §3.2 «31 different BBM tests were evaluated in our systematic review» [result]
- **Tags**: diagnostic-accuracy, variability, meta-analysis

## C04: Some tests meet or exceed the thresholds at a single cut-point
- **Statement**: Some tests did meet or exceed the panel's established thresholds, meaning a single cut-point achieved 90% Sn and 75% Sp for triaging or 90% Sn and Sp for confirmatory testing.
- **Status**: supported
- **Falsification criteria**: Disproved if no test achieved the triaging or confirmatory thresholds at a single cut-point.
- **Proof**: [E01]
- **Evidence basis**: §3.4 states some tests met or exceeded thresholds; the panel remained brand-agnostic and did not name which tests.
- **Interpretation**: The existence of threshold-meeting tests is what makes the conditional recommendations actionable; the systematic review (MAGICapp) lists which tests meet criteria.
- **Dependencies**: C03
- **Sources**:
  - "some tests did meet or exceed" thresholds (90% Sn / 75% Sp triage; 90% Sn and Sp confirmatory) ← paper.pdf §3.4 «some tests did meet or exceed the panel's established thresholds, meaning a single cut-point achieved the thresholds of 90% Sn and 75% Sp for triaging or 90% Sn and Sp for confirmatory testing» [result]
- **Tags**: diagnostic-accuracy, thresholds

## C05: Certainty of evidence is low to very low for threshold-meeting tests
- **Statement**: Certainty of the evidence for test accuracy across all tests ranged from moderate to very low; for tests meeting the panel's predetermined accuracy thresholds, certainty ranged from low to very low. Most tests were rated down largely due to serious risk of bias; publication bias was not detected for any test.
- **Status**: supported
- **Falsification criteria**: Disproved if the reported certainty range differs, or if the dominant rating-down domain was not risk of bias, or if publication bias was detected.
- **Proof**: [E03]
- **Evidence basis**: §3.5 reports the certainty ranges, the dominant risk-of-bias downgrade, and the absence of detected publication bias.
- **Interpretation**: Because certainty is poor, a future study could shift pooled estimates enough to change whether a test meets thresholds.
- **Dependencies**: C03
- **Sources**:
  - overall certainty "moderate to very low" ← paper.pdf §3.5 «The certainty of the evidence for test accuracy across all tests ranged from moderate to very low» [result]
  - threshold-meeting certainty "low to very low" ← paper.pdf §3.5 «for tests meeting the panel's predetermined thresholds for accuracy, certainty ranged from low to very low» [result]
  - publication bias not detected ← paper.pdf §3.5 «Publication bias was not detected for any of the tests» [result]
- **Tags**: GRADE, certainty, risk-of-bias

## C06: Predictive values depend strongly on pretest probability
- **Statement**: A test at the triage thresholds (Sn 90%, Sp 75%) would have a PPV of 47%, 78%, or 94% and NPV of 97%, 88%, 65% at pretest probabilities of 20%, 50%, or 80% respectively; a test at the confirmatory thresholds (Sn 90%, Sp 90%) would have a PPV of 69%, 90%, or 97% and NPV of 97%, 90%, 69% at pretest probabilities of 20%, 50%, or 80%.
- **Status**: supported
- **Falsification criteria**: Disproved if the illustrative PPV/NPV values differ from those stated, or if PPV/NPV were shown to be independent of pretest probability.
- **Proof**: [E04]
- **Evidence basis**: §2.5.1 provides the illustrative PPV/NPV values across three pretest probabilities; the panel chose not to report predictive values for individual tests because they depend on pretest probability.
- **Interpretation**: The same test yields very different clinical value depending on the population's pretest probability, motivating the good practice statement to weigh pretest probability per patient (C08).
- **Dependencies**: C01, C02
- **Sources**:
  - triage PPV 47%/78%/94%, NPV 97%/88%/65% ← paper.pdf §2.5.1 «a test with a Sn of 90% and Sp of 75% (our "triage" thresholds) would have a PPV of 47%, 78%, or 94%, and NPV of 97%, 88%, 65%, when applied in a population with a pretest probability of 20%, 50%, or 80%» [result]
  - confirmatory PPV 69%/90%/97%, NPV 97%/90%/69% ← paper.pdf §2.5.1 «A test with a Sn of 90% and Sp of 90% (our "confirmatory" thresholds) would have a PPV of 69%, 90%, or 97%, and NPV of 97%, 90%, 69%, when applied in a population with a pretest probability of 20%, 50%, or 80%» [result]
- **Tags**: predictive-value, pretest-probability

## C07: BBMs offer moderate resource savings relative to PET/CSF
- **Statement**: The panel judged savings to be moderate for BBMs compared to PET scans or CSF analysis; BBMs generally cost significantly less, often 70% to 90% lower than PET imaging, though exact price varies by country and setting.
- **Status**: supported
- **Falsification criteria**: Disproved if the guideline did not report the 70%–90%-lower cost figure or judged savings as large/none rather than moderate.
- **Proof**: [E05, E06]
- **Evidence basis**: §3.10 Resources required reports the moderate-savings judgment and the 70%–90%-lower cost figure. §3.11 notes cost-effectiveness could not be judged due to insufficient data.
- **Interpretation**: When used as a triage followed by confirmation, overall costs may rise; if BBMs replace more expensive confirmatory tests, moderate savings may result.
- **Dependencies**: none
- **Sources**:
  - BBMs "70% to 90% lower than PET imaging" ← paper.pdf §3.10 «BBMs generally cost significantly less, often 70% to 90% lower than PET imaging» [result]
  - savings judged "moderate" ← paper.pdf §3.10 «The panel judged savings to be moderate for BBMs compared to PET scans or CSF analysis» [result]
- **Tags**: resources, cost, EtD

## C08: Good practice statement — BBM only after comprehensive clinical evaluation
- **Statement**: A BBM test should not be obtained before a comprehensive clinical evaluation by a healthcare professional, and test results should always be interpreted within the clinical context; clinicians should consider each patient's pretest probability of AD pathology when deciding whether to use a BBM test.
- **Status**: supported
- **Falsification criteria**: Disproved if the guideline did not issue this good practice statement or permitted BBM testing as a standalone substitute for clinical evaluation.
- **Proof**: [E05]
- **Evidence basis**: Table 2 "Good practice statement" states this verbatim; the Abstract and Conclusion reinforce that BBMs do not substitute for comprehensive clinical evaluation.
- **Interpretation**: BBMs are part of a full diagnostic workup, not a diagnostic shortcut; over-reliance risks underdiagnosis of treatable non-AD conditions (§3.7).
- **Dependencies**: C06
- **Sources**:
  - good practice statement ← paper.pdf Table 2 «A BBM test should not be obtained before a comprehensive clinical evaluation by a healthcare professional, and test results should always be interpreted within the clinical context» [result]
- **Tags**: good-practice, clinical-context, pretest-probability
