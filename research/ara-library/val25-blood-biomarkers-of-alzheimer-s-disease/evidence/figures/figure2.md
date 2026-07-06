# Figure 2 — HR by number of elevated biomarkers (p-tau217, NfL, GFAP)

**Source**: `paper.pdf` p.4 (main text, bottom half), rendered at 5x scale to `figure2.png`. Data-label values were legible directly on the plot and cross-checked against the body text (p.4-5).

**Caption (verbatim)**: "Fig. 2 | Hazard ratio (HR) of progression from normal cognition (NC) to mild cognitive impairment (MCI), reversion from MCI to NC, and progression from MCI to all-cause dementia, depending on number of elevated blood biomarkers of Alzheimer's disease (AD), among p-tau217, NfL and GFAP. Centre and error bars represent Hazard Ratios (HR) with 95% Confidence Intervals (CI), derived from multistate Markov models, using age as time scale and adjusted for sex, education, chronic kidney disease, heart diseases, cerebrovascular disease, anemia and obesity. Cut-offs: 0.134 pg/mL for p-tau217, 20.171 pg/mL for NfL and 142.515 pg/mL for GFAP. N transitions/participants for each group: from NC to MCI, none 148/832, one 81/449, two 50/427, three 32/440; from MCI to NC, none 143/832, one 80/449, two 47/427, three 23/440; from MCI to all-cause dementia, none 39/832, one 58/449, two 108/427, three 159/440. MCI mild cognitive impairment, NC normal cognition, p-tau217 phosphorylated tau 217, NfL neurofilament light chain, GFAP glial fibrillary acidic protein. Color schemes for number of elevated biomarkers: none: gray; one: light blue; two: medium blue; three: dark blue."

## Figure type
`quantitative_plot` — three forest plots (point estimate + 95% CI error bar), one per transition, each with 4 rows (none/one/two/three elevated biomarkers), log-scale x-axis (0.2-5).

## Extraction method and reading confidence
- **Extraction method**: `exact_from_labels` — every HR and its 95% CI is printed directly on the plot as a data label (e.g., "HR 1.41 (0.98, 2.02)"), and independently corroborated in the body text for the "three vs none" contrasts.
- **Reading confidence**: high.

## Panel transcription

### From NC to MCI (fully adjusted; reference = None elevated)
| Number elevated | HR (95% CI) | N transitions/participants |
|---|---|---|
| None | Ref. | 148/832 |
| One | 1.25 (0.71, 2.17) | 81/449 |
| Two | 0.99 (0.52, 1.89) | 50/427 |
| Three | 0.84 (0.44, 1.63) | 32/440 |

### From MCI to NC (reversion; fully adjusted; reference = None elevated)
| Number elevated | HR (95% CI) | N transitions/participants |
|---|---|---|
| None | Ref. | 143/832 |
| One | 0.95 (0.49, 1.84) | 80/449 |
| Two | 0.70 (0.30, 1.62) | 47/427 |
| Three | 0.26 (0.11, 0.61) | 23/440 |

### From MCI to all-cause dementia (fully adjusted; reference = None elevated)
| Number elevated | HR (95% CI) | N transitions/participants |
|---|---|---|
| None | Ref. | 39/832 |
| One | 1.41 (0.98, 2.02) | 58/449 |
| Two | 2.36 (1.61, 3.46) | 108/427 |
| Three | 2.22 (1.50, 3.28) | 159/440 |

## Notes
- All panels adjusted for sex, education, chronic kidney disease, heart disease, cerebrovascular disease, anemia, and obesity (the "fully adjusted" tier).
- The MCI→all-cause-dementia panel is non-monotonic between "two" (HR 2.36) and "three" (HR 2.22) elevated biomarkers — this is transcribed faithfully as printed on the figure/reported in text; it is not an extraction error and is not smoothed over.
- Feeds claim C07.
