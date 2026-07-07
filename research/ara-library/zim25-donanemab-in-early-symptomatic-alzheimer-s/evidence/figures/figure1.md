# Figure 1: TRAILBLAZER-ALZ 2 overview — (a) study design and (b) study dosing

- **Source**: Fig. 1, Zimmer et al. (2025), *J Prev Alzheimers Dis* 13:100446, doi:10.1016/j.tjpad.2025.100446, `paper.pdf` p2
- **Caption**: "TRAILBLAZER-ALZ 2 overview: (a) study design and (b) study dosing. (a) The study
  design of TRAILBLAZER-ALZ 2 allowed for participants receiving donanemab to switch to blinded
  placebo infusions at 24, 52, 76, 102, or 130 weeks if they met treatment course completion
  criteria based on amyloid PET. (b) The percentage of donanemab infusions in participants
  randomized to donanemab (ie, early-start group) continued to decline as treatment course
  completion criteria based on amyloid PET were met. A similar trend was observed among
  participants randomized to placebo (ie, delayed-start group) who switched to donanemab during
  the LTE period."
- **Screenshot**: figure1.png
- **Figure type**: mixed — panel (a) is a diagram (trial-design flow chart) carrying exact
  participant counts; panel (b) is a quantitative_plot (stacked bar chart over time)
- **Extraction method**: exact_from_labels (panel a counts are printed on the diagram; panel b
  bar-height transitions are read from gridlines, described qualitatively — no data-label
  percentages are printed on the bars themselves)
- **Reading confidence**: high (panel a); medium (panel b — visual trend is clear, but exact
  per-quarter percentages are not printed, so panel b values below are approximate reads off the
  y-axis gridlines, marked ≈)

## Visual description

### Panel (a): Study design diagram
- **Components**: A flow diagram with three time-labeled stages: "Randomized 1:1 (N=1736)" →
  76-week "Placebo-controlled period" → 78-week "Long-term extension period."
  - Top row: "Donanemab" box (N=860) in the placebo-controlled period, feeding into "Donanemab"
    (N=157) in the LTE (early-start continuers) and, via a branch labeled with switch points at
    24/52/76 weeks, into a "Blinded placebo infusions based on amyloid reduction" box (N=393),
    which itself continues into an LTE "Blinded placebo infusions" box with further switch labels
    at 102/130 weeks.
  - Bottom row: "Placebo" box (N=876) in the placebo-controlled period, feeding into "Donanemab"
    (N=657) in the LTE (delayed-start), which can branch to "Blinded placebo infusions based on
    amyloid reduction" at 102/130 weeks.
  - A row of brain-icon rows below the flow boxes marks the Amyloid PET and MRI assessment
    schedule across both periods.
  - Curly braces on the right label the top pathway "Early start" and the bottom pathway "Delayed
    start."
- **Connections**: Arrows trace participant flow from randomization through each switch point;
  red arrows specifically highlight the N=157/N=393/N=657 transitions into the LTE.
- **Annotations**: Footnotes a–e (superscripts on box labels) specify: (a) donanemab dose
  (700 mg ×3 then 1400 mg Q4W IV); (b) N = participants receiving ≥1 LTE infusion; (c) continuers
  are those who had not met completion criteria by 76 weeks; (d) switch to placebo Q4W
  (saline infusion) upon meeting completion criteria; (e) delayed-start donanemab begins 78 weeks
  post-randomization on the same titration schedule as placebo-controlled-period donanemab
  recipients.
- **What it conveys**: The complete branching trial structure — randomization, the amyloid-PET-
  triggered placebo switch mechanism (limited-duration dosing), and how early-start vs
  delayed-start LTE cohorts are constructed, with every population size labeled exactly.

### Panel (b): Study dosing over time (two stacked-bar-chart panels)
- **Components**: Two side-by-side stacked bar charts, "Early-start participants" (left) and
  "Delayed-start participants" (right), each with y-axis "Infusions (%)" (0–100) and x-axis "Time
  (years)" (0–3). Red = Donanemab infusions, gray = Placebo infusions, stacked to 100% at each
  time point.
- **Trend (left, early-start)**: 100% donanemab from year 0 to ~0.5 years; drops to ≈80% around
  year 1 (24-week switch cohort); a larger step down to ≈50% around year 1.5 (52-week switch
  cohort, coincident with the placebo-controlled-period boundary at 76 weeks/~1.46 years); further
  step down to ≈28% shortly after year 2 (102-week LTE switch); gradual decline to ≈15–20% by
  year 3 (130-week LTE switch and later completions).
- **Trend (right, delayed-start)**: 100% placebo from year 0 to 1.5 years (the entire
  placebo-controlled period, since delayed-start participants receive no donanemab until LTE
  entry at week 78/~1.5 years); donanemab jumps to 100% at 1.5 years; declines stepwise to ≈80%
  around year 2, then to ≈43–48% by year 3 as participants meet 102/130-week completion criteria
  and switch to blinded placebo.
- **What it conveys**: Visually confirms the "majority of infusions administered in both the
  early- and delayed-start groups were placebo by the end of the LTE" (§3.1, `paper.pdf` p4),
  and that delayed-start participants receive no donanemab at all until LTE entry.

## Data table (panel a — exact counts from diagram labels)

| Pathway | Stage | N |
|---|---|---|
| Randomization | Randomized 1:1 | 1736 |
| Early-start (donanemab arm) | Placebo-controlled period (donanemab) | 860 |
| Early-start | Continued donanemab in LTE | 157 |
| Early-start | Switched to blinded placebo in LTE (met completion criteria) | 393 |
| Delayed-start (placebo arm) | Placebo-controlled period (placebo) | 876 |
| Delayed-start | Started donanemab at LTE entry | 657 |

## Trend summary
Panel (a) establishes the exact branching population structure (1736 → 860/876 → 157+393/657)
underlying `logic/problem.md` O4 and `logic/solution/study_design.md`. Panel (b) is a qualitative,
approximate (≈) read confirming the direction and approximate magnitude of the declining
donanemab-infusion percentage in both groups as treatment course completion criteria are
progressively met — consistent with, but not a source of, any exact numeric claim in
`logic/claims.md` (no claim cites specific panel-b percentages).
