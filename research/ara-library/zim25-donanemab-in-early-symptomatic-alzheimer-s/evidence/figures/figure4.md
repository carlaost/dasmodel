# Figure 4: Brain amyloid plaque

- **Source**: Fig. 4, Zimmer et al. (2025), *J Prev Alzheimers Dis* 13:100446, doi:10.1016/j.tjpad.2025.100446, `paper.pdf` p6
- **Caption**: "Brain amyloid plaque. The effect of donanemab on amyloid plaque was demonstrated by
  (a) mean reduction in amyloid over time between early-start and delayed-start treatment, (b)
  amyloid clearance in participants in the early-start and delayed-start groups at 24, 52, and 76
  weeks after donanemab initiation, and (c) amyloid reaccumulation among participants in the
  early-start group who met treatment course completion criteria by 52 weeks of the
  placebo-controlled period. ***p < 0.001 vs delayed-start treatment; †24 weeks from the start of
  donanemab treatment; ‡52 weeks from the start of donanemab treatment."
- **Screenshot**: figure4.png
- **Figure type**: mixed — panels (a) and (c) are quantitative_plot line charts with error bars;
  panel (b) is a quantitative_plot bar chart with printed data labels
- **Extraction method**: exact_from_labels for panel (b) (percentages printed above each bar) and
  the n= row under panel (c); digitized_estimate for panel (a)'s and panel (c)'s curve/error-bar
  values away from printed reference lines
- **Reading confidence**: high for panel (b); medium-high for panels (a)/(c) (axis gridlines are
  clear at 20-unit/25-unit intervals; the 24.1 CL reference line in panel c is explicitly labeled)

## Visual description

### Panel (a): Amyloid LS mean change over time, early- vs delayed-start
- **Components**: Line chart, y-axis "Amyloid LS mean change (CL)" from +20 to −100 (0 at top,
  decreasing/more-negative = greater reduction, downward), x-axis "Week" (0–154). Vertical dotted
  line at week 76 separates placebo-controlled period from LTE. Gray dashed line = delayed-start
  group (flat near 0 until week 76, since delayed-start participants are on placebo pre-LTE); red
  solid line = early-start group (drops steeply from week 0). Asterisk annotations (***) mark
  p<0.001-vs-delayed-start-treatment comparison points; dagger/double-dagger superscripts mark
  24-week and 52-week post-donanemab-initiation timepoints for delayed-start.
- **Trend**: Early-start line drops sharply from 0 to ≈−63 CL by week 24, continuing to ≈−85 CL by
  week 52, plateauing near ≈−87 to −88 CL from week 76 through week 154. Delayed-start line stays
  flat near 0 through week 76, then mirrors the same steep-drop-then-plateau shape once donanemab
  starts, reaching ≈−63 CL at 24 weeks post-initiation (week 102) and ≈−86 CL at 76 weeks
  post-initiation (week 154) — visually converging with the early-start line's plateau level by
  the end of the LTE.
- **What it conveys**: Near-identical asymptotic amyloid reduction regardless of when donanemab
  treatment starts, when aligned to donanemab-exposure time rather than calendar/trial time.

### Panel (b): Amyloid clearance (<24.1 CL) rates
- **Components**: Grouped bar chart, y-axis "Percentage of Participants with Amyloid <24.1CL
  (95% CI)" (0–100), x-axis grouped by matched exposure timepoint (PC Week: 24/52/76; LTE Week:
  102/130/154). Solid red bars = "PC Period" (placebo-controlled-period donanemab recipients,
  i.e., early-start at that PC week); hatched/textured red bars = "LTE Period" (delayed-start
  recipients at the matched post-initiation LTE week). Exact percentage data labels are printed
  above each bar with error bars (95% CI, not separately labeled with numeric bounds).
- **Data labels (exact, printed)**: 29.7 (PC wk24) / 33.2 (LTE wk102); 66.1 (PC wk52) / 66.7 (LTE
  wk130); 76.4 (PC wk76) / 76.5 (LTE wk154).
- **What it conveys**: Clearance rates at matched donanemab-exposure durations are nearly
  identical between early- and delayed-start participants at all three checkpoints (24/52/76 weeks
  post-initiation), reinforcing panel (a)'s message.

### Panel (c): Amyloid reaccumulation among 52-week completers
- **Components**: Line chart, y-axis "Amyloid Mean Centiloids (SD)" (0–150), x-axis "Week"
  (0–154), vertical dotted line at week 76 separating placebo-controlled period from LTE. A
  horizontal dashed reference line at "24.1 CL" marks the amyloid-negativity/clearance cutoff. A
  text annotation labels the single red line as "Early-start participants who met treatment course
  completion criteria by 52 weeks." Below the x-axis, a row gives sample size n at each week.
- **Trend**: Mean CL starts at ≈92 (week 0, with a wide SD error bar spanning roughly 60–125),
  drops to ≈16 by week 24, to near 0 by week 52 (at or just below the 24.1 CL cutoff line), and
  then rises gradually — reaccumulating — from ≈0 at week 52/76 to ≈11 by week 154, remaining
  below the 24.1 CL cutoff line throughout the plotted window (through week 154).
- **Sample sizes (n=, printed exactly below x-axis)**: week 0: 325; week 24: 324; week 52: 311;
  week 76: 294; week 102: 256; week 130: 227; week 154: 195.

## Data table

### Panel (b) — exact clearance percentages
| Post-initiation week | Group | % achieving clearance (<24.1 CL) |
|---|---|---|
| 24 (PC) / 102 (LTE) | PC-period donanemab | 29.7 |
| 24 (PC) / 102 (LTE) | LTE-period donanemab (delayed-start) | 33.2 |
| 52 (PC) / 130 (LTE) | PC-period donanemab | 66.1 |
| 52 (PC) / 130 (LTE) | LTE-period donanemab (delayed-start) | 66.7 |
| 76 (PC) / 154 (LTE) | PC-period donanemab | 76.4 |
| 76 (PC) / 154 (LTE) | LTE-period donanemab (delayed-start) | 76.5 |

### Panel (c) — sample size by week (exact, printed)
| Week | 0 | 24 | 52 | 76 | 102 | 130 | 154 |
|---|---|---|---|---|---|---|---|
| n | 325 | 324 | 311 | 294 | 256 | 227 | 195 |

## Trend summary
All three panels corroborate that donanemab's biologic amyloid-lowering and clearance effect is
robust and closely similar whether treatment starts early or late (panels a, b), and that
reaccumulation after treatment course completion is slow, keeping the 52-week-completer subset's
mean amyloid level below the 24.1 CL clearance threshold through 154 weeks (panel c). These ground
`logic/claims.md` C07 (panel a, the 86.96/86.01 CL values are stated exactly in text, not
re-derived from the plot), C08 (panel b exact clearance percentages), and C10 (panel c mean level
at 154 weeks, 10.99 [14.41] CL per text — the plotted ≈11 read is consistent with this exact
text-reported value).
