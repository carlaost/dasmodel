# Figure 1 — Lumipulse plasma p-tau217 by disease type / CKD stage (linear and log10)

- **Source**: Figure 1, §3.5 (page 13)
- **Caption**: "Lumipulse plasma p-tau217 measurements, on (A) a linear scale and (B) a log10 scale, in renal function impairment samples (from the CN-CKD cohort including samples at CKD stage 1 [n = 11], stage 2 [n = 15], stage 3a [n = 16], stage 3b [n = 9], stage 4 [n = 7]) compared to AD and non-AD samples (from the CSF cohort with AD [n = 159], and non-AD [n = 98], box plots show median ± IQR; dotted lines represent the 0.153 and 0.422 pg/mL p-tau217 cut-points derived from the CSF cohort, P < 0.001 **** using a Wilcoxon signed-rank test). AD, Alzheimer's disease; CN-CKD, cognitively normal-chronic kidney disease; CSF, cerebrospinal fluid; IQR, interquartile range; p-tau, phosphorylated tau."
- **Screenshot**: figure1.png
- **Figure type**: quantitative_plot (box plots + jittered points)
- **Extraction method**: exact_from_labels (group medians/IQRs stated in §3.5 text; box positions read visually)
- **Reading confidence**: high (numeric medians/IQRs quoted from text)

- **Plot kind**: box (with overlaid scatter)
- **Axes**: (A) X = disease type (categorical), Y = p-tau217 conc. (pg/mL, linear, ~0–3); (B) X = disease type, Y = p-tau217 conc. (pg/mL, log10 scale, ~0.03–3.00). Two horizontal dotted lines mark the 0.153 (lower) and 0.422 (upper) pg/mL cut-points.

### Group median (IQR) plasma p-tau217, pg/mL (from §3.5 text)

| Group | n | Median (IQR) pg/mL |
|---|---|---|
| AD (CSF cohort) | 159 | 0.727 (0.437–1.068) |
| non-AD (CSF cohort) | 98 | 0.108 (0.061) |
| CKD-1 | 11 | 0.119 (0.082–0.190) |
| CKD-2 | 15 | 0.134 (0.106–0.205) |
| CKD-3a | 16 | 0.164 (0.132–0.218) |
| CKD-3b | 9 | 0.208 (0.136–0.257) |
| CKD-4 | 7 | 0.213 (0.145–0.261) |

*non-AD IQR is transcribed as printed in the paper (a single value "0.061" is shown rather than a two-value IQR).*

### Zone placement of CN-CKD samples (CSF-derived cut-points applied)
- Above upper cut-point (0.422 pg/mL): 3/58 = 5.1%
- Intermediate (0.153–0.422 pg/mL): 25/58 = 43.1%
- (Remainder below lower cut-point.)

## Trend summary
AD group is far higher than all other groups (**** P < 0.001 vs non-AD, Wilcoxon signed-rank). Median p-tau217 increases monotonically with CKD stage from CKD-1 (0.119) to CKD-4 (0.213), rising into but rarely above the intermediate zone; most CKD medians sit near or just above the lower cut-point (0.153) and below the upper cut-point (0.422). No CKD group median reaches the AD group level. The log10 panel (B) makes the CKD-stage gradient and separation from AD clearer. No statistically significant association between p-tau217 and CN-CKD after adjustment for age, sex, or BMI (Table S11).
