# Figure 2: Clinical efficacy measured by change from baseline in the CDR-SB score

- **Source**: Fig. 2, Zimmer et al. (2025), *J Prev Alzheimers Dis* 13:100446, doi:10.1016/j.tjpad.2025.100446, `paper.pdf` p5
- **Caption**: "Clinical efficacy measured by change from baseline in the CDR-SB score. Efficacy
  was measured by change from baseline in the CDR-SB score versus the external weighted ADNI
  control cohort for participants in the (a) early-start group, (b) delayed-start group, and (c)
  early-start group who met treatment course completion criteria based on amyloid positron
  emission tomography by 52 weeks of the placebo-controlled period. Propensity score weights were
  estimated for the ADNI cohort with the average treatment effect among the treated estimand using
  the inverse probability weighting method from the generalized linear model. Change from baseline
  in the CDR-SB score was estimated using a mixed model for repeated measures using ADNI weights."
- **Screenshot**: figure2.png
- **Figure type**: quantitative_plot (line chart with error bars, three panels) plus an embedded
  data table under each panel
- **Extraction method**: exact_from_labels (all treatment-difference values, CIs, and sample
  sizes/ESS are printed as a table directly under each panel's plot)
- **Reading confidence**: high

## Visual description
- **Components**: Three line-chart panels, each plotting "CDR-SB score LS mean change (SE)"
  (y-axis, inverted — 0 at top, 6 at bottom, arrow labeled "Worsening" pointing down) against
  "Month" (x-axis, 0–36), split into "Placebo-controlled period" (months 0–18) and "Long-term
  extension period" (months 18–36) by a vertical dotted line at month 18.
  - **(a) Early-start group**: Red solid line = early-start group; blue solid line = ADNI cohort;
    gray dashed line = internal placebo group (shown only through month 18, i.e., through the
    placebo-controlled period, since placebo participants are relabeled delayed-start after LTE
    entry). A bracket at month ~20 shows an interim delta of −0.6 (−0.9, −0.3); a bracket at
    month 36 shows the final delta of −1.2 (−1.7, −0.7).
  - **(b) Delayed-start group**: Red dashed line labeled "Delayed-start donanemab treatment"
    (dashed because it begins only at month 18/LTE entry) = delayed-start group; blue solid line =
    ADNI cohort (separately weighted for this comparison). Bracket at month 36 shows delta of −0.8
    (−1.3, −0.3).
  - **(c) Early-start subset (52-week completers)**: Red solid line = early-start group who met
    treatment course completion criteria by 52 weeks; blue solid line = ADNI cohort. Interim
    bracket at month ~20: −0.7 (−1.0, −0.3); month-36 bracket: −1.3 (−1.9, −0.7).
- **Connections/annotations**: Below each panel, a data table gives "Early/Delayed start vs ADNI
  difference (95% CI)" and sample sizes ("Early-start group (N)"/"Delayed-start group (N)"/
  "Placebo group (N)"/"ADNI cohort (ESS)") at months 0, 6, 12, 18, 24, 36 (panel a additionally
  shows month 18 vs 24 transition values; panel c also at months 0/6/12/18/24/36).
- **What it conveys**: In all three panels, the treated-group line diverges progressively further
  from (below, i.e., less-worsening than) the ADNI cohort line as follow-up extends, with the gap
  widening monotonically from month 6 through month 36 — visual confirmation of a growing
  treatment effect rather than a fixed offset.

## Data table (all values exact, read from the printed sub-panel tables)

### Panel (a) — Early-start vs ADNI
| Month | Difference (95% CI) | Early-start N | ADNI ESS | Placebo N |
|---|---|---|---|---|
| 0 | — | 794 | 268 | 840 |
| 6 | −0.2 (−0.3, −0.1) | 731 | 255 | 783 |
| 12 | −0.5 (−0.7, −0.3) | 650 | 237 | 714 |
| 18 | −0.6 (−0.9, −0.3) | 604 | 200 | 680 |
| 24 | −1.0 (−1.3, −0.6) | 507 | 183 | — |
| 36 | −1.2 (−1.7, −0.7) | 417 | 122 | — |

### Panel (b) — Delayed-start vs ADNI
| Month | Difference (95% CI) | Delayed-start N | ADNI ESS |
|---|---|---|---|
| 0 | — | 655 | 301 |
| 6 | −0.03 (−0.2, 0.1) | 636 | 287 |
| 12 | −0.02 (−0.2, 0.2) | 634 | 267 |
| 18 | −0.1 (−0.5, 0.3) | 645 | 224 |
| 24 | −0.6 (−0.9, −0.3) | 579 | 206 |
| 36 | −0.8 (−1.3, −0.3) | 458 | 139 |

### Panel (c) — Early-start (52-week completers) vs ADNI
| Month | Difference (95% CI) | Early-start N (52-week completers) | ADNI ESS |
|---|---|---|---|
| 0 | — | 323 | 268 |
| 6 | −0.3 (−0.5, −0.1) | 316 | 255 |
| 12 | −0.6 (−0.8, −0.3) | 303 | 237 |
| 18 | −0.7 (−1.0, −0.3) | 289 | 200 |
| 24 | −1.1 (−1.5, −0.7) | 250 | 183 |
| 36 | −1.3 (−1.9, −0.7) | 198 | 122 |

## Trend summary
All three panels show a monotonically widening negative (favoring donanemab) LS-mean-difference
gap from month 6 to month 36, with N declining over follow-up in both the treated and ADNI
comparator groups (attrition), and ADNI ESS declining faster in relative terms as weighting
precision degrades. These exact values ground `logic/claims.md` C01 (panel a, month 36),
C02 (panel b, month 36), and C03 (panel c, month 36).
