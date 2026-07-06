# Claims

Load-bearing numbers below carry a `**Sources**` entry with the verbatim matched line from the paper
text or a filed evidence table. `[result]` = a value the study's analysis produced (reported in a
table/figure/text); this is a retrospective diagnostic-accuracy study, so essentially all numbers are
`[result]` values, except pre-set cut-offs/thresholds which are `[input]`.

## C01: Elecsys plasma p-tau217 has excellent diagnostic accuracy for AD vs non-AD
- **Statement**: Plasma p-tau217 measured on the automated Roche Elecsys platform discriminates AD from non-AD cognitive disorders with AUC 0.939 (95% CI 0.895–0.969) at an optimal single cut-off of 0.371 pg/mL (sensitivity 92.2%, specificity 89.2%).
- **Status**: supported
- **Falsification criteria**: An AUC confidence interval overlapping chance or well below 0.90, or sensitivity/specificity substantially below the reported values, in this cohort at this cut-off, would refute it.
- **Proof**: [E01]
- **Evidence basis**: Table 2 (Elecsys p-tau217 row) and Figure 2 ROC curves.
- **Interpretation**: Comparable performance to research/batch assays can be achieved on a routine high-throughput analyser; "excellent" reflects AUC > 0.93 in this single cohort, not external validation.
- **Sources**:
  - AUC 0.939 (0.895–0.969) ← Table 2 «Elecsys p-tau217 | 186 | 0.939 (0.895–0.969) | 0.371 | 92.2% ... | 89.2% ...» [result]
  - cut-off 0.371 pg/mL ← §Results p.5 «Optimal cut-off values were 0.371 pg/mL for Elecsys p-tau217» [input]
  - sensitivity 92.2%, specificity 89.2% ← Table 2 «92.2% (85.3–96.6%) | 89.2% (80.4–94.9%)» [result]
- **Dependencies**: none
- **Tags**: p-tau217, Elecsys, diagnostic-accuracy, AUC

## C02: Elecsys p-tau217 performs comparably to Lumipulse p-tau217
- **Statement**: The diagnostic performance of Elecsys p-tau217 (AUC 0.939) is not statistically different from Fujirebio Lumipulse p-tau217 (AUC 0.950, 95% CI 0.907–0.976; DeLong p = 0.485).
- **Status**: supported
- **Falsification criteria**: A DeLong test showing a significant difference (p < 0.05) between the two p-tau217 AUCs would refute comparability.
- **Proof**: [E01]
- **Evidence basis**: Table 2 (both p-tau217 rows); §Results DeLong p = 0.485.
- **Interpretation**: Elecsys p-tau217 is a viable automated alternative to the batch Lumipulse assay for discrimination, despite differing absolute concentrations (see C07).
- **Sources**:
  - Lumipulse p-tau217 AUC 0.950 (0.907–0.976) ← Table 2 «Lumipulse p-tau217 | 186 | 0.950 (0.907–0.976)» [result]
  - DeLong p = 0.485 ← §Results p.5 «comparable discriminatory performance between the two p-tau217 assays (p = 0.485)» [result]
- **Dependencies**: C01
- **Tags**: comparison, DeLong, Lumipulse, Fujirebio

## C03: Elecsys p-tau217 significantly outperforms Elecsys p-tau181
- **Statement**: Elecsys p-tau217 (AUC 0.939) discriminates AD from non-AD significantly better than Elecsys p-tau181 (AUC 0.903, 95% CI 0.852–0.942; DeLong p = 0.043).
- **Status**: supported
- **Falsification criteria**: A non-significant DeLong test (p ≥ 0.05) or a higher p-tau181 AUC would refute it.
- **Proof**: [E01]
- **Evidence basis**: Table 2 (both Elecsys rows); §Results DeLong p = 0.043.
- **Interpretation**: Consistent with the broader literature that p-tau217 > p-tau181 for AD discrimination, now shown within a single platform.
- **Sources**:
  - Elecsys p-tau181 AUC 0.903 (0.852–0.942) ← Table 2 «Elecsys p-tau181 | 187 | 0.903 (0.852–0.942)» [result]
  - DeLong p = 0.043 ← §Results p.5 «the AUC of Elecsys p-tau181 was significantly lower than that of Elecsys p-tau217 (p = 0.043)» [result]
- **Dependencies**: C01
- **Tags**: p-tau181, comparison, DeLong

## C04: Adding APOE-ε4 improves Elecsys p-tau217 discrimination and shrinks the grey zone
- **Statement**: Adding blood-based APOE-ε4 carrier status to Elecsys p-tau217 in logistic regression raises the AUC from 0.939 to 0.970 (95% CI 0.943–0.992; p = 0.02) and reduces the two-cut-off intermediate proportion from 20.0% to 11.0%.
- **Status**: supported
- **Falsification criteria**: A non-significant AUC change (p ≥ 0.05) or no reduction in intermediate proportion would refute it.
- **Proof**: [E03]
- **Evidence basis**: Table 2 (Elecsys p-tau217 + APOE-ε4 row); Table 3 (intermediate 11.0%); §Results APOE section.
- **Interpretation**: APOE-ε4 mainly reduces diagnostic uncertainty — carriers gain PPV (95–100%), non-carriers gain NPV (up to 98%) — shifting interpretation of intermediate results; broader clinical adoption requires validation and attention to genetic-risk disclosure ethics.
- **Sources**:
  - AUC 0.939 → 0.970 (0.943–0.992), p = 0.02 ← §Results p.6 «for Elecsys p-tau217 (AUC 0.939 to 0.970; p = 0.02)» [result]
  - intermediate 20.0% → 11.0% ← §Results p.6 «Elecsys p-tau217 from 20.0% to 11.0%» [result]
- **Dependencies**: C01
- **Tags**: APOE-e4, logistic-regression, grey-zone

## C05: Aβ42 / Aβ42-40 adjustment adds little discrimination on the Fujirebio platform
- **Statement**: Combining Lumipulse p-tau217 with Aβ42 or the Aβ42/40 ratio does not significantly increase the AUC (0.950 vs 0.957; p = 0.058 for Aβ42, p = 0.322 for Aβ42/40) and only modestly reduces the intermediate proportion (11.9% → 10.0% with Aβ42; 10.5% with Aβ42/40).
- **Status**: supported
- **Falsification criteria**: A statistically significant AUC gain (p < 0.05) from Aβ42/Aβ42-40 adjustment would refute the "limited added value" claim.
- **Proof**: [E04]
- **Evidence basis**: Table 2 (Lumipulse p-tau217, /Aβ42, /(Aβ42/Aβ40) rows); Table 3 intermediates; §Results Aβ42 section.
- **Interpretation**: Aβ42 may help classify some borderline cases depending on cohort/platform, but the incremental benefit over p-tau217 alone was small here.
- **Sources**:
  - AUC 0.950 vs 0.957; p = 0.058 and p = 0.322 ← §Results p.7 «did not result in a statistically significantly increase the AUC (0.950 vs. 0.957; p = 0.058 and p = 0.322, respectively)» [result]
  - intermediates 11.9% vs 10.0% vs 10.5% ← §Discussion p.9 «slightly reduced the proportion of intermediate results (11.9% vs. 10.0% vs. 10.5%)» [result]
- **Dependencies**: C02
- **Tags**: amyloid-beta, Ab42, ratio, grey-zone

## C06: A two-cut-off strategy yields assay-dependent intermediate zones
- **Statement**: Applying 95%-sensitivity and 95%-specificity thresholds produces an intermediate ("grey") zone of 19.9% (37/186) for Elecsys p-tau217 (cut-offs 0.275 / 0.497 pg/mL), 11.9% (22/186) for Lumipulse p-tau217 (0.130 / 0.246 pg/mL), and 33.2% (62/187) for Elecsys p-tau181 (0.936 / 1.505 pg/mL).
- **Status**: supported
- **Falsification criteria**: Recomputing the grey-zone proportions from the stated cut-offs and cohort and getting materially different values would refute it.
- **Proof**: [E02]
- **Evidence basis**: Table 3; §Results two-cut-off section; Figure 3.
- **Interpretation**: The 19.9% grey zone for Elecsys p-tau217 falls within the 15–20% range recommended by the BBM workgroup; illustrates the trade-off between stringency and indeterminate outcomes.
- **Sources**:
  - Elecsys p-tau217 19.9% (37/186), cut-offs 0.275/0.497 ← Table 3 «Elecsys p-tau217 | 0.275 | 0.497 | ... | 19.9%»; §Results p.5 «19.9% (37/186)» [result]/[input]
  - Lumipulse p-tau217 11.9% (22/186), 0.130/0.246 ← Table 3 «Lumipulse p-tau217 | 0.130 | 0.246 | ... | 11.9%» [result]
  - Elecsys p-tau181 33.2% (62/187), 0.936/1.505 ← Table 3 «Elecsys p-tau181 | 0.936 | 1.505 | ... | 33.2%» [result]
- **Dependencies**: C01, C03
- **Tags**: two-cut-off, grey-zone, thresholds

## C07: The two p-tau217 assays are strongly correlated but not interchangeable in absolute values
- **Statement**: Elecsys and Lumipulse p-tau217 are strongly correlated (Pearson rs = 0.88, p < 0.0001) but show proportional (Passing–Bablok slope 1.363, 95% CI 1.251–1.484) and systematic (intercept 0.113, 95% CI 0.098–0.133) differences, with Bland–Altman relative differences up to 59% (mean 58.7%; limits of agreement −27.2% to 144.6%).
- **Status**: supported
- **Falsification criteria**: A slope indistinguishable from 1 and intercept indistinguishable from 0 (CIs including those values), or weak correlation, would refute the systematic/proportional-bias claim.
- **Proof**: [E05]
- **Evidence basis**: Figure 1 (panels A and B).
- **Interpretation**: Absolute concentrations are assay-specific; certified reference materials / harmonization are needed before cross-assay cut-offs can be shared.
- **Sources**:
  - rs = 0.88, slope 1.363 (1.251–1.484), intercept 0.113 (0.098–0.133) ← §Results p.5 «proportional (slope = 1.363; 95% CI: 1.251–1.484) and systematic (intercept = 0.113; 95% CI: 0.098–0.133) differences ... (r = 0.88, p < 0.0001)» [result]
  - differences up to 59% ← §Results p.5 «indicated discrepancies of up to 59% between the assays (Fig. 1B)» [result]
- **Dependencies**: C02
- **Tags**: method-comparison, Passing-Bablok, Bland-Altman, harmonization

## C08: Higher baseline Elecsys p-tau217 relates to worse and possibly faster-declining cognition
- **Statement**: Higher baseline Elecsys p-tau217 is associated with lower baseline MoCA (linear regression β = −0.267, p < 0.001) and, among AD patients with follow-up (n = 69, median 2.1 years), shows a non-significant trend toward faster MoCA decline over time (interaction p = 0.07), adjusted for age and sex.
- **Status**: supported
- **Falsification criteria**: No association between baseline p-tau217 and baseline MoCA, or an interaction firmly null/opposite in direction, would refute it.
- **Proof**: [E07, E08]
- **Evidence basis**: §Results "Influence of clinical cofactors" (β = −0.267, p < 0.001) and "Cognitive decline and p-tau217" (n = 69, p = 0.07).
- **Interpretation**: Consistent with p-tau217 reflecting cognitive severity; the longitudinal decline finding is exploratory (MoCA-only, modest subset, p = 0.07 not significant).
- **Sources**:
  - baseline MoCA association p < 0.001, β = −0.267 ← §Results p.7-8 «Significant associations were observed with diagnostic group and baseline MoCA score (p < 0.001, β=-0.267)» [result]
  - decline trend n = 69, median 2.1 years, p = 0.07 ← §Results p.8 «Among AD patients with longitudinal follow-up (n = 69; median follow up 2.1 years) ... trend toward faster cognitive decline over time (p = 0.07)» [result]
- **Dependencies**: C01
- **Tags**: longitudinal, MoCA, cognitive-decline, mixed-effects

## C09: Elecsys p-tau217 is not significantly affected by age, sex, renal function, or small-vessel disease
- **Statement**: In linear regression, baseline Elecsys p-tau217 shows no significant association with age (p = 0.449, β = 0.064), sex (p = 0.054, β = 0.154), renal function/eGFR (p = 0.918, β = −0.009), severe white-matter hyperintensities (Fazekas 3; p = 0.072, β = 0.142), or ≥2 strictly lobar microbleeds indicative of CAA (p = 0.308, β = 0.079); p-tau217 did not differ across eGFR categories (p = 0.07).
- **Status**: supported
- **Falsification criteria**: A significant association (p < 0.05) with any of these cofactors in this cohort would refute the corresponding part.
- **Proof**: [E07]
- **Evidence basis**: §Results "Influence of clinical cofactors"; Table 1 (cofactor distributions).
- **Interpretation**: In a typical memory-clinic population (median age ~70, few advanced-CKD cases; 21 with eGFR < 60, none < 30), p-tau217 reflects disease rather than physiological variation; renal-function null may reflect absence of advanced CKD.
- **Sources**:
  - age p = 0.449 β = 0.064; sex p = 0.054 β = 0.154; eGFR p = 0.918 β = −0.009; Fazekas p = 0.072 β = 0.142; CAA p = 0.308 β = 0.079 ← §Results p.8 «no significant associations were found with age (p = 0.449, β = 0.064), sex (p = 0.054, β = 0.154), renal function (eGFR) (p = 0.918, β=-0.009), severe white-matter hyperintensities (Fazekas score = 3) (p = 0.072, β = 0.142), or the presence of two or more strictly lobar microbleeds indicative of CAA (p = 0.308, β = 0.079)» [result]
  - 21 with eGFR < 60, none < 30 ← §Results p.8 «Twenty-one patients had an eGFR below 60 mL/min/1.73 m² ... and none had an eGFR below 30» [result]
- **Dependencies**: C01
- **Tags**: cofactors, renal-function, CAA, Fazekas, confounding

## C10: The Elecsys p-tau assays have acceptable analytical precision and low LLOQ
- **Statement**: Analytical imprecision (CV) ranged 0.5–3.8% for Elecsys p-tau181 and 0.5–8.6% for Elecsys p-tau217 (CLSI EP15-A3, 5 measurements/day over 5 non-consecutive days); linearity was maintained down to 0.30 pg/mL (p-tau181) and 0.12 pg/mL (p-tau217); LLOQ was 0.32 pg/mL (p-tau181) and 0.10 pg/mL (p-tau217, at 20% CV).
- **Status**: supported
- **Falsification criteria**: Measured CVs materially exceeding the reported ranges, or an LLOQ far above the stated values, would refute it.
- **Proof**: [E06]
- **Evidence basis**: §Results "Precision, linearity and limit of quantification" (values also in Supplemental Table 1 / Supplementary Figure S1, not in provided PDF).
- **Interpretation**: Precision is consistent with other immunoassay platforms (SIMOA, MSD, CLEIA); supports routine use.
- **Sources**:
  - imprecision 0.5–3.8% (p-tau181), 0.5–8.6% (p-tau217) ← §Results p.5 «imprecision for p-tau181 ranged from 0.5 to 3.8%, whereas for p-tau217 it ranged from 0.5 to 8.6%» [result]
  - linearity 0.30 / 0.12 pg/mL; LLOQ 0.32 / 0.10 pg/mL ← §Results p.5 «Linearity was maintained down to 0.30 pg/mL and 0.12 pg/mL ... The LLOQ was estimated at 0.32 pg/mL for p-tau181 and 0.10 pg/mL for p-tau217» [result]
- **Dependencies**: none
- **Tags**: analytical-validation, precision, LLOQ, linearity

## C11: Discordant CSF (A+T−N−) profiles are heterogeneous, with elevated plasma p-tau217 in a subset
- **Statement**: The 16 excluded discordant-CSF cases (15 A+T−N−, 1 other) differed clearly from AD across plasma p-tau (p < 0.001) and resembled non-AD overall, but were heterogeneous: applying the Elecsys p-tau217 single cut-off, 62.5% were below and 37.5% above the threshold; reclassifying them as AD changed AUC/sensitivity/specificity only modestly.
- **Status**: supported
- **Falsification criteria**: Uniform (non-heterogeneous) plasma p-tau217 in discordant cases, or a large shift in optimal cut-off when reclassified, would refute it.
- **Proof**: [E09]
- **Evidence basis**: §Results "Discordant CSF biomarker profiles" (sensitivity analysis in Supplementary Table 5, not in provided PDF).
- **Interpretation**: Elevated plasma p-tau217 despite normal CSF tau may reflect early amyloid-continuum tau pathophysiology; supports robustness of the main cut-offs and cautious interpretation of isolated plasma elevations.
- **Sources**:
  - 15 A+T−N−, 1 other; p < 0.001 vs AD ← §Results p.7 «amyloid abnormal without CSF tau abnormality (A + T−N−, ... n = 15) or other discordant AT(N) profiles (n = 1). Overall, discordant cases differed clearly from the AD group across plasma p-tau measures (p < 0.001)» [result]
  - 62.5% below / 37.5% above threshold ← §Results p.7 «62.5% discordant cases were below and 37.5% were above the threshold» [result]
- **Dependencies**: C01
- **Tags**: discordant-CSF, ATN, sensitivity-analysis
