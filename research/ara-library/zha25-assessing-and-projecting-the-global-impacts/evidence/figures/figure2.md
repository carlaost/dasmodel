# Figure 2: Projected global burden of age-standardized rates of Alzheimer's disease in 2030, by locations

- **Source**: Figure 2, Results §3.3–3.4, p.6
- **Caption**: "Projected global burden of age-standardized rates of Alzheimer's disease in 2030,
  by locations. (A) ASIR, (B) ASDR, and (C) age-standardized DALY rate. DALY = disability adjusted
  life-year. ASIR = age standardized incidence rate. ASDR = age standardized death rate. ASRs =
  age standardized rates."
- **Screenshot**: figure2.png
- **Figure type**: quantitative_plot
- **Extraction method**: `exact_from_labels` for the location identity of the tallest/shortest bars
  in each panel (cross-referenced against the exact 2030 DALY-ASR figures printed in Results §3.3,
  already transcribed in `logic/claims.md` C04); `digitized_estimate` (≈) for all other bar-height
  readings, since no data labels are printed on the bars themselves (only axis gridlines and error
  whiskers for the 95% UI).
- **Reading confidence**: high for relative ranking/ordering of bars within each panel; medium
  (≈) for absolute bar-height values read off the axis, since values must be interpolated between
  gridlines.

- **Plot kind**: vertical bar chart, one bar per location, three separate panels (A/B/C), each with
  its own Y-axis scale and its own color-gradient legend ("ASRs"); error whiskers on every bar show
  the 95% UI.
- **Axes**:
  - Panel A ("Incidence by Region in Both"): Y = ASRs, gridlines at 0, 2000, 4000; legend swatches
    1000/2000/3000/4000/5000 (darkest green = lowest ASR, palest = highest).
  - Panel B ("Deaths by Region in Both"): Y = ASRs, gridlines at 0, 300, 600, 900; legend swatches
    250/500/750/1000.
  - Panel C ("DALYs (Disability-Adjusted Life Years) by Region in Both"): Y = ASRs, gridlines at 0,
    5000, 10000, 15000, 20000, 25000; legend swatches 5000/10000/15000/20000.
  - X (shared across all three panels, 24 locations): Global, High SDI, High-middle SDI, Middle
    SDI, Low-middle SDI, Low SDI, Andean Latin America, Australasia, Caribbean, Central Asia,
    Central Europe, Central Latin America, Central Sub-Saharan Africa, East Asia, Eastern Europe,
    Eastern Sub-Saharan Africa, High-income Asia Pacific, High-income North America, Oceania,
    Southeast Asia, Southern Latin America, Southern Sub-Saharan Africa, Tropical Latin America,
    Western Europe — this is the same fixed row order as `tables/table1.md` (Global, then 5 SDI
    tiers, then the 18 GBD regions alphabetically), **not** sorted by magnitude (unlike Figure 1,
    which is DALY-EAPC-sorted).
  - Scale: linear in all three panels.
- **Color**: single hue (green) per panel, shaded by ASR magnitude per each panel's own "ASRs"
  legend (darkest = lowest, palest = highest) — a different color-encoding convention from Figure 1
  (which used blue).

## Trend summary
- In all three panels, **Central Sub-Saharan Africa** has the visibly tallest (palest) bar by a
  wide margin, and **Low SDI** is the second-tallest bar — consistent with claim C04's text-sourced
  ranking (Central Sub-Saharan Africa highest 2030 DALY ASR at 22,703.53, ahead of Eastern
  Sub-Saharan Africa, Oceania, and Southern Sub-Saharan Africa, all visibly tall bars here too).
- **Eastern Europe** and **Central Europe** have the visibly shortest bars (near-zero height with
  very wide error whiskers extending far above the bar top) in all three panels — consistent with
  C04's text-sourced minimum (Eastern Europe 2030 DALY ASR 1,404.84, 95% UI 0.05–3,014.43; the wide,
  asymmetric whisker down to the axis is visually striking and matches the near-zero lower UI
  bound).
- **High-income Asia Pacific** and **Western Europe** are also visibly short bars, matching C04's
  text-sourced next-lowest values (4,365.22 and 4,555.77 respectively).
- Exact per-location point values and 95% UIs for these extremes are given in the Results §3.3 text
  (transcribed in `logic/claims.md` C04), not printed as data labels on this figure; this figure's
  incremental content is the visual confirmation of relative bar heights/ranking and the visibly
  wide, asymmetric uncertainty whiskers on the lowest-ASR locations (Eastern Europe, Central
  Europe) — a visual signal of the same degenerate/low-count pattern flagged for country-level data
  in claim C06.
