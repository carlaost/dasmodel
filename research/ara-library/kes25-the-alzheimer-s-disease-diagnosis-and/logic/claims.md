# Claims

## C01: Lumipulse plasma p-tau217 has high diagnostic accuracy for AD in a CSF-defined cohort
- **Statement**: In the CSF cohort (n = 257, AD status defined by CSF Aβ42/Aβ40 ratio ≤ 0.065), the Lumipulse plasma p-tau217 assay discriminates AD from non-AD with an AUC of 0.947 (95% CI 0.919–0.974).
- **Status**: supported
- **Falsification criteria**: A correctly powered ROC analysis on the same cohort/definition yielding an AUC point estimate materially different from 0.947, or a 95% CI not overlapping the reported interval.
- **Proof**: [E01]
- **Evidence basis**: Table 2 reports Lumipulse p-tau217 AUC = 0.947 (0.919–0.974), P < 0.001 (DeLong) vs age+sex model (AUC 0.673).
- **Interpretation**: Consistent with prior reports that plasma p-tau217 approaches CSF/PET-level diagnostic accuracy.
- **Dependencies**: none
- **Tags**: diagnostic-accuracy, ROC, Lumipulse, CSF
- **Sources**:
  - 0.947 ← Table 2 / abstract «Diagnostic accuracy was similar (area under the ROC Lumipulse 0.947; ALZpath 0.940)» [result]
  - 0.919–0.974 ← Table 2, Lumipulse p-tau217 row «0.947 0.919 0.974» [result]

## C02: The Lumipulse assay outperforms ALZpath on fold-change and indeterminate proportion
- **Statement**: Although the two assays are highly correlated and have statistically indistinguishable AUCs, Lumipulse shows a larger median fold-change between non-AD and AD groups (CSF cohort: 6.7 vs ALZpath 4.2; amyloid PET cohort: 3.9 vs ALZpath 3.2) and a lower proportion of indeterminate results at matched sensitivity/specificity, so Lumipulse was selected as the clinical assay.
- **Status**: supported
- **Falsification criteria**: Head-to-head analysis on the same cohorts showing ALZpath with equal/larger fold-change AND equal/lower indeterminate proportion than Lumipulse.
- **Proof**: [E01, E02]
- **Evidence basis**: §3.2.1 median fold-change Lumipulse 6.7 (Fig S2A) vs ALZpath 4.2 (Fig S2B) in CSF; §3.2.2 Lumipulse 3.9 (Fig S3A) vs ALZpath 3.2 (Fig S3B) in PET; Table 3 intermediate zone 19.4% (Lumipulse) vs 23.4% (ALZpath) in CSF cohort. AUCs not statistically different (DeLong, Table 2/§3.3.1).
- **Interpretation**: Assay differences attributed to different capture/detector antibodies and platforms (§4 Discussion; ref 37).
- **Dependencies**: C01
- **Tags**: assay-comparison, fold-change, indeterminate-zone
- **Sources**:
  - 6.7 ← §3.2.1 «the median fold-change increase in p-tau217 between non-AD and AD participants was 6.7 (Figure S2A ...)» [result]
  - 4.2 ← §3.2.1 «there was a median fold-change increase in p-tau217 between non-AD and AD participants of 4.2 (Figure S2B)» [result]
  - 3.9 ← §3.2.2 «the median fold-change increase in p-tau217 between non-AD and AD participants was 3.9 (Figure S3A ...)» [result]
  - 3.2 ← §3.2.2 «the median fold-change increase in p-tau217 between non-AD and AD participants was 3.2 (Figure S3B)» [result]
  - 19.4 / 23.4 ← Table 3 Intermediate zone % column, Lumipulse 19.4 / ALZpath 23.4 [result]

## C03: Lumipulse dual cut-points 0.153/0.422 pg/mL give 95% sensitivity, 97% specificity, 19.4% indeterminate in the CSF cohort
- **Statement**: In the CSF derivation cohort, the optimal Lumipulse dual cut-point pair of 0.153 pg/mL (lower) and 0.422 pg/mL (upper) achieves 95% sensitivity and 97% specificity, placing 19.4% of individuals in the intermediate zone, with lower-cut-point NPV 90.4% (95% CI 80.6–95.0), upper-cut-point PPV 97.6% (95% CI 93.2–99.5), and overall accuracy 94.7% for those receiving a definitive low/high classification.
- **Status**: supported
- **Falsification criteria**: Recomputation on the same cohort yielding materially different cut-points or performance metrics at 95% sensitivity / maximized specificity.
- **Proof**: [E03]
- **Evidence basis**: Table 3 (CSF derivation, Lumipulse row) and §3.4.1.
- **Interpretation**: These are the cut-points adopted for the UKAS-accredited NHS laboratory and the planned ADAPT stage-3 trial.
- **Dependencies**: C01
- **Tags**: cut-points, dual-cutpoint, sensitivity, specificity, NPV, PPV
- **Sources**:
  - 0.153 / 0.422 ← abstract «using dual cut-points (0.153/0.422 pg/mL)» and Table 3 Lumipulse Lower 0.153 / Upper 0.422 [result]
  - 95 / 97 ← abstract «Lumipulse p-tau217 achieved 95% sensitivity and 97% specificity» [result]
  - 19.4 ← §3.4.1 «The optimal cut-point pair was 0.153 and 0.422 pg/mL (97% specificity), which gave 19.4% of individuals in the intermediate zone» [result]
  - 90.4 / 97.6 / 94.7 ← §3.4.1 «an NPV of 90.4% (95% CI 80.6–95.0) and a PPV of 97.6% (95% CI 93.2–99.5), with an overall accuracy ... of 94.7%» [result]

## C04: Applying CSF-derived cut-points to the amyloid PET cohort raises the indeterminate proportion above 20%
- **Statement**: When the CSF-derived Lumipulse cut-points (0.153/0.422 pg/mL) are applied to the independent amyloid PET cohort (n = 76), the intermediate zone rises to 34.2%, with lower-cut-point NPV 88.9% (95% CI 65.3–98.6), upper-cut-point PPV 90.6% (95% CI 75.0–98.0), and overall accuracy 90.0%; AUC against PET visual read is lower (Lumipulse 0.879, 95% CI 0.778–0.980).
- **Status**: supported
- **Falsification criteria**: Application to the same PET cohort yielding an intermediate proportion ≤ 20% or materially different NPV/PPV/accuracy.
- **Proof**: [E04]
- **Evidence basis**: §3.4.2, Table 3 (amyloid PET validation, Lumipulse) and Table 2 (PET AUC).
- **Interpretation**: Discordance between amyloid PET visual read and CSF/quantitative measures (5–14% of cases) and differing amyloid/tau burden likely drive the larger indeterminate zone (§4 Discussion).
- **Dependencies**: C03
- **Tags**: external-validation, amyloid-PET, indeterminate-zone
- **Sources**:
  - 34.2 ← abstract «producing indeterminate results in 19.4% (CSF defined) and 34.2% (PET defined)» and §3.4.2 «the resulting percentage of individuals in the intermediate zone was 34.2%» [result]
  - 88.9 / 90.6 / 90.0 ← §3.4.2 «the NPV of the lower cut-point was 88.9% (95% CI 65.3–98.6), and the PPV of the upper cut-point was 90.6% (95% CI 75.0–98.0), achieving an overall accuracy ... of 90.0%» [result]
  - 0.879 ← Table 2 amyloid PET Lumipulse p-tau217 «0.879 0.778 0.980» [result]

## C05: Adding demographic/clinical covariates does not significantly improve AUC over p-tau217 alone
- **Statement**: Adding age and sex (and, where available, serum creatinine and BMI) as covariates to plasma p-tau217 logistic models does not produce a statistically significant improvement in AUC over p-tau217 alone in either cohort (DeLong tests P > 0.05; AIC reduction < 20).
- **Status**: supported
- **Falsification criteria**: A DeLong test showing a significant AUC improvement (P < 0.05) or AIC reduction ≥ 20 from adding these covariates in the same models.
- **Proof**: [E05]
- **Evidence basis**: Table 2 (Age+sex+Lumipulse AUC 0.950 vs Lumipulse 0.947; Age+sex+ALZpath 0.946 vs 0.940); §3.3.1–3.3.2 state additions were "not significantly different"/"did not alter the result"; Tables S3, S4.
- **Interpretation**: Plasma p-tau217 carries the diagnostic signal; covariate adjustment is not required for the diagnostic model.
- **Dependencies**: C01
- **Tags**: covariates, AUC, DeLong, AIC
- **Sources**:
  - 0.950 / 0.947 ← Table 2 «Age + sex + Lumipulse p-tau217 0.950 ... Lumipulse p-tau217 0.947» [result]
  - not significant ← §3.3.1 «a combined model including age, sex, and Lumipulse p-tau217 gave an AUC of 0.950 (95% CI 0.925–0.974), not significantly different to Lumipulse p-tau217 alone» [result]

## C06: Plasma p-tau217 is robust to pre-analytical sample handling variations
- **Statement**: Across four pre-analytical handling experiments (pre-centrifugation delay at room temperature and at 2–8°C, post-centrifugation delay/storage, and freeze–thaw cycles; n = 10 per experiment), the median relative change in plasma p-tau217 from baseline did not exceed the ±10% clinically significant threshold for either the Lumipulse or ALZpath assay.
- **Status**: supported
- **Falsification criteria**: A handling condition producing a median relative change exceeding ±10% from baseline on either assay.
- **Proof**: [E06]
- **Evidence basis**: §3.6, Figure 2 (A–D), Tables S10, S12. Statistically significant differences existed for ALZpath in Experiment 1 (Friedman P = 0.007) and Lumipulse in Experiment 3 (P = 0.0047), but the median changes stayed within ±10%.
- **Interpretation**: A recommended sample-handling protocol (≤3 h RT or 24 h refrigerated before centrifugation; up to 2 weeks at −20°C; up to 4 freeze–thaw cycles) was derived for trial sites.
- **Dependencies**: none
- **Tags**: pre-analytical, stability, robustness, sample-handling
- **Sources**:
  - ±10% not exceeded ← §3.6 «Across all four experiments, the median relative change across conditions did not exceed the ± 10% threshold considered likely to be clinically significant (Figure 2)» [result]
  - P = 0.0047 ← §3.6 «In Experiment 3 (post-centrifugation delay, Figure 2C), a significant difference was observed between post-centrifugation delay groups (P = 0.0047 ...)» [result]

## C07: Lumipulse plasma p-tau217 is robust to assay kit lot-to-lot variability
- **Statement**: Across four Lumipulse kit lots (v1: 4128, 5066; v2: 5084, 5086) tested on a subset of n = 30 CSF-cohort samples, p-tau217 measurements correlate strongly (Spearman rho > 0.95); 3/30 individuals had discordant clinical classifications across lots, none within the same kit lot.
- **Status**: supported
- **Falsification criteria**: A kit-lot comparison showing rho ≤ 0.95 or systematic (consistently significant) deviation of Passing–Bablok regression lines from identity attributable to lot.
- **Proof**: [E07]
- **Evidence basis**: §3.7, Figure S4.
- **Interpretation**: Cut-points are likely stable across lots over the trial's recruitment period; discordances arose across assay versions rather than within a version.
- **Dependencies**: none
- **Tags**: lot-to-lot, reproducibility, Lumipulse
- **Sources**:
  - rho > 0.95 ← §3.7 «We reported strong correlations (rho > 0.95) in plasma p-tau217 measurements across kit lots» [result]
  - 3 of 30 ← §3.7 «Three out of 30 individuals had discordant classifications across lots relative to the established dual cut-points; discordances did not occur due to the same kit lot» [result]

## C08: Sub-zero transport is comparable to −80°C storage for plasma p-tau217
- **Statement**: In 10 samples, Lumipulse p-tau217 measurements from plasma stored/transported at −20°C in a Bio-Freeze device correlate excellently with those stored/transported at −80°C (Spearman rho = 0.998) with no systematic bias.
- **Status**: supported
- **Falsification criteria**: A comparison of the two transport conditions showing rho materially below 0.998 or a systematic bias between conditions.
- **Proof**: [E08]
- **Evidence basis**: §3.8, Figure S5.
- **Interpretation**: Enables temperature-controlled transport (e.g., Bio-Freeze) without dry ice in the ADAPT stage-3 trial.
- **Dependencies**: none
- **Tags**: transport, temperature, stability
- **Sources**:
  - rho = 0.998 ← §3.8 «an excellent correlation was observed between Lumipulse p-tau217 measurements from samples stored and transported at −20°C and −80°C (rho = 0.998)» [result]

## C09: CKD elevates plasma p-tau217 into the intermediate zone but not typically to AD-positive levels
- **Statement**: In 58 cognitively normal ADPKD/CKD (stage 1–4) individuals aged < 60, Lumipulse plasma p-tau217 rose with CKD stage (median rising from CKD-1 0.119 to CKD-4 0.213 pg/mL) with 43.1% (25/58) falling in the intermediate zone (0.153–0.422 pg/mL) and only 5.1% (3/58) above the upper cut-point; there was no statistically significant association between p-tau217 and CN-CKD after adjustment for age, sex, or BMI.
- **Status**: supported
- **Falsification criteria**: A significant independent association of CKD status with elevated p-tau217 to AD-positive levels after covariate adjustment, or a materially different intermediate/high proportion in the same cohort.
- **Proof**: [E09]
- **Evidence basis**: §3.5, Figure 1 (A/B), Table S11.
- **Interpretation**: Extra caution is advised interpreting p-tau217 in patients with ≤ CKD-3a (eGFR < 60); serum creatinine should be assessed (§4 Discussion).
- **Dependencies**: C03
- **Tags**: CKD, renal-function, confounders, intermediate-zone
- **Sources**:
  - 43.1% / 5.1% ← §3.5 «Three (i.e., 5.1%) of the CN-CKD stage 1 through 4 samples tested above the upper cut-point of 0.422 pg/mL and 25 (i.e., 43.1%) tested in the intermediate zone between 0.153 and 0.422 pg/mL» [result]
  - 0.119 ← §3.5 «CKD-1 0.119 (0.082–0.190) pg/mL» [result]
  - 0.213 ← §3.5 «CKD-4 0.213 (0.145–0.261) pg/mL» [result]
  - no significant association ← §3.5 «There was no statistically significant association between p-tau217 and CN-CKD ... after adjustment for age, sex, or BMI» [result]

## C10: Within-cohort derived cut-points outperform externally derived (Malmö) cut-points
- **Statement**: Applying the external Malmö-derived Lumipulse cut-points (0.22 lower / 0.34 upper pg/mL) to the CSF cohort gives lower sensitivity (91.4% vs 95%), lower NPV (87.1% vs 90.5% at 62.7% AD prevalence), and reduced accuracy across definitions (88.8–91.5%) compared with the within-cohort derived cut-points (accuracy 93.3–94.0%).
- **Status**: supported
- **Falsification criteria**: An analysis showing the external Malmö cut-points match or exceed within-cohort cut-points on sensitivity, NPV, and accuracy on the same cohort.
- **Proof**: [E03]
- **Evidence basis**: §3.4.1 (Malmö sensitivity analysis).
- **Interpretation**: Supports deriving cohort-specific cut-points for the target population rather than importing external thresholds.
- **Dependencies**: C03
- **Tags**: external-cutpoints, Malmö, generalizability
- **Sources**:
  - 91.4% vs 95% ← §3.4.1 «the sensitivity of the external lower cut-point was lower (91.4% vs. 95%)» [result]
  - 88.8–91.5% vs 93.3–94.0% ← §3.4.1 «accuracy was reduced across all definitions using the Malmö cut-points (88.8%–91.5%) compared to the accuracy afforded by the within-cohort derived cut-points (93.3%–94.0%)» [result]
