# Figure 2: ROC curves comparing plasma biomarkers for tau-PET and amyloid status

- **Source**: Figure 2, "Tables and Figures" section, PDF p.44
- **Caption**: "Fig. 2. Receiver Operating Characteristic (ROC) curves comparing the performance of VeraBIND Tau, plasma pTau217, pTau181 (missing data=3), pTau231 (missing data=27), and the Aβ42/Aβ40 ratio (missing data=6) for predicting: A. tau-PET positivity (Braak-like tau-PET stage>0), B. amyloid positivity (Centiloid≥20 or CSF Aβ42≤544 pg/mL)."
- **Screenshot**: figure2.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels
- **Reading confidence**: high

- **Plot kind**: line (ROC curves, 2 panels, 5 series each)
- **Axes**: X = Specificity (unitless, 0–1, reversed axis 1.0→0.0, linear), Y = Sensitivity (unitless, 0–1, linear)

## Panel A — Prediction of tau-PET status (Braak-like tau-PET stage>0)
| Biomarker | AUC (printed in legend) |
|---|---|
| VeraBIND Tau | 0.974 |
| Plasma pTau217 | 0.924 |
| Plasma pTau181 | 0.84 |
| Plasma pTau231 | 0.753 |
| Plasma Aβ42/Aβ40 ratio | 0.768 |

## Panel B — Prediction of amyloid status (Centiloid≥20 or CSF Aβ42≤544 pg/mL)
| Biomarker | AUC (printed in legend) |
|---|---|
| VeraBIND Tau | 0.866 |
| Plasma pTau217 | 0.932 |
| Plasma pTau181 | 0.813 |
| Plasma pTau231 | 0.757 |
| Plasma Aβ42/Aβ40 ratio | 0.82 |

## Trend summary
Panel A: the VeraBIND Tau curve (black) visibly dominates all other curves across nearly the full specificity range, tracking closest to the top-left corner (high sensitivity at high specificity); pTau217 (blue) is second-best; pTau181 (red), Aβ42/Aβ40 (orange), and pTau231 (green) cluster lower, closer to the diagonal chance line at mid-range specificity. Panel B: the ordering changes — pTau217 (blue) now dominates, tracking closest to the top-left corner, with VeraBIND Tau (black) and Aβ42/Aβ40 (orange) next, and pTau181/pTau231 lowest. This crossover between panels A and B is the visual basis for Claim C02 (VeraBIND Tau is tau-specific; pTau217 remains the best amyloid predictor).
