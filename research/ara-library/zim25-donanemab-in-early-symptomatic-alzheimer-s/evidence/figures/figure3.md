# Figure 3: CDR-G hazard progression — early-start vs delayed-start treatment with donanemab

- **Source**: Fig. 3, Zimmer et al. (2025), *J Prev Alzheimers Dis* 13:100446, doi:10.1016/j.tjpad.2025.100446, `paper.pdf` p5
- **Caption**: "CDR-G hazard progression: early-start vs delayed-start treatment with donanemab.
  Early-start participants showed a 27% reduced risk of progressing to the next clinical stage of
  the disease versus delayed-start participants. Hazard ratio, 95% CI, and p value were calculated
  using a Cox proportional hazards model. The model was stratified by pooled investigator and
  baseline tau level and included baseline covariates of age, CDR-G score, and acetylcholinesterase
  inhibitor/memantine use."
- **Screenshot**: figure3.png
- **Figure type**: quantitative_plot (cumulative-incidence step function)
- **Extraction method**: digitized_estimate for the curve trajectory (values read off gridlines at
  labeled x-axis weeks); exact_from_labels for the boxed hazard-ratio statistic
- **Reading confidence**: high for the hazard-ratio box and axis scale/labels; medium for
  intermediate step-curve values away from major gridlines (curve is a fine-grained step function;
  values below are read at the labeled week gridlines, approximate where not exactly on a step)

## Visual description
- **Components**: A single-panel step (cumulative-incidence) plot. Y-axis: "Percentage of
  participants progressing on CDR-G" (0–70, linear). X-axis: "Week" (0–154, gridlines every 12
  weeks). A vertical dotted line at week 76 separates "Placebo-controlled period" (left) from
  "Long-term extension period" (right). Gray dashed line = delayed-start group; red solid line =
  early-start group. A boxed annotation reads "Hazard ratio (95% CI)ᵃ 0.73 (0.62-0.86); p<0.001."
- **Connections**: Both curves start at 0% at week 0 and rise in discrete steps (consistent with
  CDR-G progression being assessed only at quarterly visits); the delayed-start (gray/red-dashed)
  curve is consistently above (higher cumulative progression than) the early-start (red-solid)
  curve from approximately week 12 onward, with the gap persisting and gradually widening through
  week 154.
- **What it conveys**: A visibly and persistently lower cumulative CDR-Global-progression rate for
  early-start versus delayed-start participants across the entire 154-week (3-year) observation
  window, consistent with the boxed HR=0.73 (i.e., a 27% lower hazard for early-start).

## Data table (approximate step-curve reads at labeled week gridlines, ≈)

| Week | Early-start (%, ≈) | Delayed-start (%, ≈) |
|---|---|---|
| 12 | ≈6 | ≈8 |
| 24 | ≈16 | ≈16 |
| 36 | ≈16 | ≈22 |
| 52 | ≈21 | ≈30 |
| 64 | ≈26 | ≈32 |
| 76 | ≈29 (period boundary) | ≈37 (period boundary) |
| 90 | ≈31 | ≈43 |
| 102 | ≈35 | ≈46 |
| 114 | ≈40 | ≈49 |
| 130 | ≈44 | ≈53 |
| 142 | ≈51 | ≈58 |
| 154 | ≈55 | ≈62 |

Boxed exact statistic (not estimated): **Hazard ratio (95% CI) = 0.73 (0.62–0.86); p<0.001.**

## Trend summary
The early-start curve remains below the delayed-start curve for the entire observation window
after an early crossover period (weeks 0–12, where the curves are nearly coincident), consistent
with a sustained, not merely transient, reduction in disease-stage-progression risk. This figure
directly grounds `logic/claims.md` C04 (HR=0.73 [0.62, 0.86], p<0.001) — the paper explicitly
calls this "the best evidence of clinical meaningfulness from the available LTE data" (§4).
