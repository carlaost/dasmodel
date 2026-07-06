# Claims

All numbers are pooled diagnostic-performance estimates copied exactly from the source (P-scores are
SUCRA-analogous rankings from 0-1; MD = mean difference in AUC vs. the p181_IA reference).

## C01: p-tau217 by mass spectrometry has the highest diagnostic accuracy for amyloid-beta pathology
- **Statement**: For detecting amyloid-beta (Abeta) positivity, mass-spectrometry-derived p-tau217 (p217_MS) achieved the highest rank (P-score = 0.859), followed by the p-tau217 ratio (p217_Ratio, P-score = 0.783) and ALZpath-based p-tau217 immunoassay (p217_ALZpath, P-score = 0.686); standard p-tau181 immunoassay (p181_IA) ranked last (P-score = 0.117). In the forest plot vs. the p181_IA baseline, p217_MS had a mean AUC difference of MD = 0.10 (95% CI 0.04-0.16).
- **Status**: supported
- **Falsification criteria**: Refuted if, under the same NMA on independent cohorts, p181_IA or another isoform outranked p217_MS for Abeta detection, or if p217_MS's AUC advantage over p181_IA were non-significant (95% CI crossing 0).
- **Proof**: [E01]
- **Evidence basis**: Table 2 Outcome 1 P-scores (p217_MS 0.859 > p217_Ratio 0.783 > p217_ALZpath 0.686 > p217_Lumi 0.667 > p217_IA 0.412 > p217_Lilly 0.331 > p231_UGOT 0.145 > p181_IA 0.117); Figure 3A forest plot MDs vs. p181_IA.
- **Interpretation**: All p-tau217 variants and the ratio significantly outperform the older p-tau181 immunoassay standard, which the authors argue is effectively obsolete for high-precision diagnostics.
- **Dependencies**: none
- **Sources**:
  - `0.859` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 1) «p217_MS (0.859)» [result]
  - `0.783` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 2) «p217_Ratio (0.783)» [result]
  - `0.686` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 3) «p217_ALZpath (0.686)» [result]
  - `0.117` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 8) «p181_IA (0.117)» [result]
  - `0.10 (95% CI 0.04-0.16)` ← evidence/figures/figure3.md (Figure 3A) «p217_MS ... 0.10 [ 0.04; 0.16]» [result]
- **Tags**: p-tau217, mass spectrometry, amyloid-beta, AUC, P-score, ranking

## C02: The p-tau217/Abeta42 ratio on automated platforms gives a significant incremental AUC gain over single-analyte assays
- **Statement**: A meta-analysis of the AUC gain from using the p-tau217/Abeta42 ratio instead of single-analyte p-tau217 showed a significant mean difference of 0.025 (95% CI 0.005-0.045), with zero between-cohort heterogeneity (I2 = 0%).
- **Status**: supported
- **Falsification criteria**: Refuted if the pooled incremental AUC gain's 95% CI included 0 (non-significant), or if substantial heterogeneity (high I2) undermined the pooled estimate.
- **Proof**: [E02]
- **Evidence basis**: §3.6 and §4.1 report MD = 0.025 (95% CI 0.005-0.045; I2 = 0%) for the ratio vs. single-analyte comparison (Supplementary Table S2); consistent with the p217_Ratio node ranking 2nd for Abeta detection (P-score = 0.783, Table 2).
- **Interpretation**: The ratio "bridges the performance gap" between automated immunoassays and mass spectrometry, likely because normalizing to Abeta42 corrects for inter-individual differences in protein clearance and constitutive tau levels.
- **Dependencies**: [C01]
- **Sources**:
  - `0.025` ← §3.6 (page 6, body text above §4) «p-tau217 showed a significant mean difference of 0.025 (95% CI: 0.005-0.045)» [result]
  - `0.005-0.045` ← §3.6 (page 6) «(95% CI: 0.005-0.045) (Supplementary Table S2)» [result]
  - `I2 = 0%` ← §3.6 (page 6) «The zero heterogeneity (I2 = 0%) observed in this gain across cohorts» [result]
- **Tags**: p-tau217/Abeta42 ratio, incremental AUC, heterogeneity, automated immunoassay

## C03: p-tau217 by MS is the top marker for advanced Tau-PET staging and for predicting MCI-to-AD-dementia conversion
- **Statement**: p217_MS was superior for identifying advanced Tau-PET pathology (P-score = 0.907, ranked 1st) and for predicting MCI-to-AD-dementia conversion (P-score = 0.821, ranked 1st), followed closely by p217_Ratio (Outcome 2 P-score = 0.814). In the Tau-PET forest plot, p217_MS had the largest AUC improvement over p181_IA (MD = 0.13, 95% CI 0.05-0.22), whereas p181_IA ranked near-last for Tau-PET (P-score = 0.090).
- **Status**: supported
- **Falsification criteria**: Refuted if another biomarker/platform node outranked p217_MS for either Tau-PET recognition or MCI-to-AD progression, or if the p217_MS vs. p181_IA AUC improvement for Tau-PET were non-significant.
- **Proof**: [E03]
- **Evidence basis**: Table 2 Outcome 3 (p217_MS 0.907, rank 1; p217_Lumi 0.723; p181_IA 0.090) and Outcome 2 (p217_MS 0.821, rank 1; p217_Ratio 0.814; p231_UGOT 0.042); Figure 3B forest plot (p217_MS MD 0.13 [0.05; 0.22]; p181_IA P-score 0.090).
- **Interpretation**: Plasma p-tau217 is a high-fidelity proxy for advanced (Braak V-VI) tau pathology, potentially reducing the need for tau-PET scans by 80% (per §4.2, Therriault et al., 2021).
- **Dependencies**: [C01]
- **Sources**:
  - `0.907` ← evidence/tables/table2.md (Table 2, Outcome 3, Rank 1) «p217_MS (0.907)» [result]
  - `0.821` ← evidence/tables/table2.md (Table 2, Outcome 2, Rank 1) «p217_MS (0.821)» [result]
  - `0.814` ← evidence/tables/table2.md (Table 2, Outcome 2, Rank 2) «p217_Ratio (0.814)» [result]
  - `0.090` ← evidence/tables/table2.md (Table 2, Outcome 3, Rank 6) «p181_IA (0.090)» [result]
  - `0.13 (95% CI 0.05-0.22)` ← evidence/figures/figure3.md (Figure 3B) «p217_MS ... 0.13 [ 0.05; 0.22]» [result]
- **Tags**: p-tau217, Tau-PET, MCI-to-AD progression, staging, prognosis

## C04: p-tau231 is the top-ranked marker for early amyloidosis in the preclinical subgroup
- **Statement**: In the preclinical (asymptomatic) subgroup for detecting Abeta pathology (Outcome 1), p-tau231 achieved the highest rank (P-score = 0.66), consistent with it rising earliest in the disease course; across the full-continuum analyses, however, p231_UGOT ranked near-last (Abeta P-score = 0.145; MCI-to-AD P-score = 0.042).
- **Status**: supported
- **Falsification criteria**: Refuted if p-tau231 did not achieve the top rank in the preclinical-stage subgroup, or if stage-stratified analysis showed no early advantage for p-tau231.
- **Proof**: [E04]
- **Evidence basis**: §4.2 states that in the preclinical subgroup (Outcome 1) p-tau231 achieved the highest rank (P-score = 0.66); Table 2 shows p231_UGOT ranks low in the pooled (full-continuum) Outcome 1 (0.145) and Outcome 2 (0.042).
- **Interpretation**: Supports a "relay" hypothesis: p-tau231 is an early "smoke detector" for asymptomatic amyloidosis; as disease progresses p-tau217 takes over as the robust marker of neurofibrillary tangle burden.
- **Dependencies**: none
- **Sources**:
  - `0.66` ← §4.2 (page 7) «in the pre-clinical subgroup (Outcome 1), p-tau 231 achieved the highest rank (P-score = 0.66) for detecting early Abeta pathology» [result]
  - `0.145` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 7) «p231_UGOT (0.145)» [result]
  - `0.042` ← evidence/tables/table2.md (Table 2, Outcome 2, Rank 7) «p231_UGOT (0.042)» [result]
- **Tags**: p-tau231, preclinical, early amyloidosis, relay hypothesis, subgroup

## C05: p-tau217 diagnostic performance is consistent across Han Chinese and Western cohorts
- **Statement**: Meta-analysis of the two large Han Chinese cohorts (Huashan and Greater Bay Area) gave a P-score of 1.00 for p-tau217, indicating it was the top-performing marker across all Asian datasets included; subgroup analyses confirmed consistent p-tau217 performance across Han Chinese and Western cohorts.
- **Status**: supported
- **Falsification criteria**: Refuted if the ethnicity-stratified subgroup analysis showed materially different p-tau217 AUC/rankings between Han Chinese and Western cohorts.
- **Proof**: [E05]
- **Evidence basis**: §4.3 reports a P-score of 1.00 for p-tau217 in the Han Chinese cohorts (Huashan and GBA); the abstract and §3.6 state subgroup analyses confirmed consistent p-tau217 performance across Han Chinese and Western cohorts.
- **Interpretation**: p-tau217 diagnostic performance and cut-offs appear remarkably robust across ethnicities — potentially more so than genetic markers like APOE e4 — which is essential for global implementation of BBMs.
- **Dependencies**: [C01]
- **Sources**:
  - `1.00` ← §4.3 (page 7) «The P-score of 1.00 for p-tau 217 in these cohorts indicates it was the top-performing marker across all Asian datasets included» [result]
- **Tags**: cross-ethnic, Han Chinese, generalizability, p-tau217, subgroup

## C06: Serum p-tau217 is a viable matrix, performing comparably to plasma
- **Statement**: Serum p-tau217 (p217_Serum) ranked 3rd for technical platform/matrix efficiency (P-score = 0.568), demonstrating comparable diagnostic potential to plasma-based assays and indicating serum is a viable matrix where rapid plasma processing is unavailable.
- **Status**: supported
- **Falsification criteria**: Refuted if serum p-tau217 showed materially lower AUC/ranking than plasma p-tau217 in the matrix-efficiency analysis.
- **Proof**: [E06]
- **Evidence basis**: Table 2 Outcome 4 (p217_Serum P-score = 0.568, rank 3); §3.5 states serum p-tau217 (P-score = 0.568) demonstrated comparable diagnostic potential to plasma-based assays; §4.4 cites the Benedet et al. 2026 (TRIAD) dataset as compelling evidence of serum-plasma equivalence.
- **Interpretation**: Serum's status as the standard matrix in routine hospital chemistry has logistical benefits, allowing easier integration into existing diagnostic workflows.
- **Dependencies**: none
- **Sources**:
  - `0.568` ← evidence/tables/table2.md (Table 2, Outcome 4, Rank 3) «p217_Serum (0.568)» [result]
- **Tags**: serum, matrix, p-tau217, clinical implementation

## C07: Mass spectrometry is the gold-standard platform; automated immunoassays outperform manual ones
- **Statement**: For technical platform and matrix efficiency (Outcome 4), mass spectrometry (p217_MS) ranked 1st (P-score = 0.953) as the gold standard for precision; automated immunoassays (p217_AutoIA, e.g., Lumipulse) ranked 2nd (P-score = 0.706) and significantly outperformed manual immunoassays (p217_IA, P-score = 0.268); standard p181_IA ranked last (P-score = 0.006).
- **Status**: supported
- **Falsification criteria**: Refuted if a non-MS platform outranked MS for precision, or if automated and manual immunoassays showed no ranking separation.
- **Proof**: [E06]
- **Evidence basis**: Table 2 Outcome 4 (p217_MS 0.953 > p217_AutoIA 0.706 > p217_Serum 0.568 > p217_IA 0.268 > p181_IA 0.006); §3.5 corroborates (MS 0.953; AutoIA/Lumipulse 0.706; manual IAs 0.268).
- **Interpretation**: Automated immunoassays (Lumipulse) are the superior non-MS approach, offering a diagnostic accuracy sufficient for routine clinical use while MS remains the analytical gold standard.
- **Dependencies**: [C01]
- **Sources**:
  - `0.953` ← evidence/tables/table2.md (Table 2, Outcome 4, Rank 1) «p217_MS (0.953)» [result]
  - `0.706` ← evidence/tables/table2.md (Table 2, Outcome 4, Rank 2) «p217_AutoIA (0.706)» [result]
  - `0.268` ← evidence/tables/table2.md (Table 2, Outcome 4, Rank 4) «p217_IA (0.268)» [result]
  - `0.006` ← evidence/tables/table2.md (Table 2, Outcome 4, Rank 5) «p181_IA (0.006)» [result]
- **Tags**: mass spectrometry, automated immunoassay, Lumipulse, platform, precision

## C08: Standard p-tau181 immunoassay is effectively obsolete for high-precision AD diagnostics
- **Statement**: Standard p-tau181 immunoassay (p181_IA) consistently ranked lowest or near-lowest across outcomes (Abeta P-score = 0.117; MCI-to-AD P-score = 0.159; Tau-PET P-score = 0.090; platform efficiency P-score = 0.006) — i.e., P-score < 0.20 across all four outcomes — and its AUC advantage over baseline was non-significant where measured; p-tau181 failed to reliably discriminate Tau-PET status.
- **Status**: supported
- **Falsification criteria**: Refuted if p181_IA achieved a mid- or high-rank (P-score > 0.20) on any of the four outcomes, or if it significantly outperformed a p-tau217 variant on any outcome.
- **Proof**: [E01, E03]
- **Evidence basis**: Table 2 shows p181_IA at or near the bottom of every outcome (0.117 / 0.159 / 0.090 / 0.006); §3.4 notes p-tau181 failed to reliably discriminate Tau-PET status (P-score = 0.090); §4.1 concludes p-tau181 is effectively obsolete for high-precision AD diagnostics (P-score < 0.20).
- **Interpretation**: While p-tau181 was once the standard, the results support that it is effectively obsolete for high-precision AD diagnostics.
- **Dependencies**: [C01, C03]
- **Sources**:
  - `0.117` ← evidence/tables/table2.md (Table 2, Outcome 1, Rank 8) «p181_IA (0.117)» [result]
  - `0.159` ← evidence/tables/table2.md (Table 2, Outcome 2, Rank 6) «p181_IA (0.159)» [result]
  - `0.090` ← evidence/tables/table2.md (Table 2, Outcome 3, Rank 6) «p181_IA (0.090)» [result]
  - `0.006` ← evidence/tables/table2.md (Table 2, Outcome 4, Rank 5) «p181_IA (0.006)» [result]
  - `< 0.20` ← §4.1 (page 7) «our results (P-score < 0.20) suggest it is effectively obsolete for high-precision AD diagnostics» [result]
- **Tags**: p-tau181, obsolescence, baseline comparator, ranking
