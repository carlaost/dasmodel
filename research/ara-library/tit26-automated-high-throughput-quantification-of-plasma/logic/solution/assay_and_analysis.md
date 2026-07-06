# Assay and Statistical Analysis Method

The core "method" of this study is a laboratory measurement protocol plus a statistical analysis
pipeline. Both are described in prose only in the paper (no code, no printed pseudocode), so they are
captured here in `logic/solution/` rather than as `src/execution/` code.

## 1. Pre-analytics — blood collection and storage
- Blood collected in 4 mL K2 EDTA tubes; centrifuged (2000 g × 10 min, 4 °C) within 2 h of extraction.
- Plasma aliquoted into polypropylene cryotubes, stored at −80 °C until analysis (CCUG-Biobank, standardized procedures).
- On analysis day: samples brought to room temperature, mixed, centrifuged 2000 g × 5 min, transferred to instrument cuvettes.

## 2. Plasma biomarker measurement platforms
### Roche cobas pro e801 — Elecsys (ECLIA, electrochemiluminescence immunoassay)
- Elecsys Phospho-Tau (181P) Plasma RUO — lot# 99065201 → p-tau181
- Elecsys Phospho-Tau (217P) Plasma RUO — lot# 990760 → p-tau217
- Elecsys APOE-ε4 Plasma RUO — lot# 99065401 → APOE-ε4 carrier status (proteotyping; carrier vs non-carrier)

### Fujirebio LUMIPULSE G1200 — Lumipulse (CLEIA, chemiluminescent enzyme immunoassay)
- Lumipulse G pTau217 Plasma RUO — lot# 5086 → p-tau217
- Lumipulse G β-Amyloid 1-40-N Plasma RUO — V&V lot# 5 → Aβ40
- Lumipulse G β-Amyloid 1-42-N Plasma RUO — V&V lot# 8 → Aβ42

### CSF biomarkers (reference standard)
- Aβ42, Aβ42/40 ratio, p-tau181, total tau on LUMIPULSE G1200 (Fujirebio, Ghent), measured blinded.

### Ancillary
- Plasma creatinine: Jaffe reaction on cobas pro c703 (Roche); eGFR via CKD-EPI 2009 equation.

## 3. Analytical validation
- **Precision/imprecision**: commercial QC solutions (PreciControl pT181p Elecsys RUO, Phospho-Tau 217P PreciControl Elecsys RUO), CLSI EP15-A3 protocol — 5 measurements in a single run over 5 non-consecutive days.
- **Linearity**: dilution of a high-concentration sample per manufacturer instructions, each dilution in triplicate (mean = correct result).
- **LLOQ**: predefined CV specification of 20%; samples below LLOQ interpreted at the LLOQ value.

## 4. Statistical analysis pipeline
- **Software**: SPSS v29.0 for all analyses except Passing–Bablok and Bland–Altman, done in MedCalc v15.6.1 (Mariakerke, Belgium). Significance threshold p < 0.05.
- **Group comparisons**: χ² (categorical); independent-samples t-test or Mann–Whitney U (continuous, as appropriate). Effect sizes reported (0.2 small, 0.5 medium, 0.8 large). Data as medians (IQR).
- **Diagnostic accuracy**: ROC AUC (95% CI); optimal single cut-offs by maximizing the Youden index; AUCs compared with the DeLong test.
- **APOE-ε4 added value**: binary covariate in logistic regression predicting AD status; AUC comparison.
- **Two-cut-off approach**: cut-offs at 95% sensitivity and 95% specificity, defining an intermediate zone; likelihood ratios computed as sensitivity / (1 − specificity).
- **Method comparison**: Passing–Bablok regression (slope, intercept, 95% CI) and Bland–Altman analysis (relative %).
- **Cofactor influence**: Spearman rank correlation and multivariable linear regression for age, sex, kidney function, APOE-ε4 on biomarker concentrations; MoCA-adjusted logistic regression for confounding by cognitive severity.
- **Longitudinal analysis**: linear mixed-effects models with random intercepts and slopes; baseline p-tau217 × time interaction; adjusted for age, sex, baseline MoCA.

## 5. Diagnostic cut-off outputs (derived)
| Biomarker | Optimal single cut-off (pg/mL) | Two-cut-off lower / upper (pg/mL) |
|-----------|-------------------------------|-----------------------------------|
| Elecsys p-tau217 | 0.371 | 0.275 / 0.497 |
| Elecsys p-tau181 | 1.150 | 0.936 / 1.505 |
| Lumipulse p-tau217 | 0.246 | 0.130 / 0.246 |
| Lumipulse p-tau217/Aβ42 | 0.0115 | 0.0071 / 0.0139 |
| Lumipulse p-tau217/(Aβ42/Aβ40) | 3.891 | 0.912 / 3.841 |

(Full performance metrics for each: `evidence/tables/table2.md` and `table3.md`.)
