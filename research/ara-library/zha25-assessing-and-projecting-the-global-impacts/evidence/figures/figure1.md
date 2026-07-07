# Figure 1: Projected EAPC of global burden of Alzheimer's disease from 2022 to 2030, by locations

- **Source**: Figure 1, Results §3.3, p.5
- **Caption**: "Projected EAPC of global burden of Alzheimer's disease from 2022 to 2030, by
  locations. (A) ASIR, (B) ASDR, and (C) age-standardized DALY rate. DALY = disability adjusted
  life-year. ASIR = age standardized incidence rate. ASDR = age standardized death rate. ASRs =
  age standardized rates."
- **Screenshot**: figure1.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels for the underlying EAPC values (all visible bars
  correspond to rows already transcribed exactly in `tables/table1.md`); visual_description for
  the sort order and the color-gradient legend, which carry no separate printed labels.
- **Reading confidence**: high (bar heights and ordering are unambiguous; exact values are
  cross-referenced to Table 1 rather than digitized from pixels)

- **Plot kind**: vertical bar chart, one bar per location, three stacked panels (A/B/C) sharing a
  single X-axis category order (the location labels are printed once, beneath panel C, and apply
  to all three panels above it) — the shared order runs from highest (most positive) to lowest
  (most negative) DALY EAPC.
- **Axes**:
  - Panel A ("Incidence by Region in Both"): Y = EAPC (%), gridlines at 0, −5, −10, −15.
  - Panel B ("Deaths by Region in Both"): Y = EAPC, gridlines at 0, −5, −10, −15, −20.
  - Panel C ("DALYs (Disability-Adjusted Life Years) by Region in Both"): Y = EAPC, gridlines at
    0, −5, −10, −15.
  - X (shared, 24 locations = 5 SDI tiers + 18 regions + Global): Low SDI, Andean Latin America,
    Southern Latin America, Caribbean, Central Latin America, Low-middle SDI, Oceania,
    High-income North America, Eastern Sub-Saharan Africa, Southern Sub-Saharan Africa, Central
    Sub-Saharan Africa, Tropical Latin America, High SDI, Global, Middle SDI, Australasia,
    High-income Asia Pacific, Western Europe, Central Asia, Southeast Asia, East Asia,
    High-middle SDI, Central Europe, Eastern Europe.
  - Scale: linear in all three panels. Because the shared order is sorted by DALY EAPC (panel C),
    panels A and B — whose own EAPCs correlate with but do not exactly match panel C's ranking —
    are visibly non-monotonic under this shared ordering (e.g., in panel B, High-middle SDI's
    death EAPC is more negative than several regions plotted to its right).
- **Color**: single hue (blue), shaded by EAPC magnitude per the "EAPCs" legend (darker = closer to
  0, lightest = most negative, spanning roughly −15 to 0 in the legend swatch).

## Trend summary
- Under the shared (DALY-sorted) ordering, Low SDI, Andean Latin America, Southern Latin America,
  and the Caribbean sit at the positive (rising) end in all three panels, and Central Europe and
  Eastern Europe sit at the far negative (falling) end with visually distinct, much taller
  downward bars than every other location — directly supporting claim C03's magnitude gap between
  the Latin American/low-SDI cluster and the Central/Eastern Europe outliers.
- The shared sort order is fully consistent with the DALYs 2022–2030 column of
  `tables/table1.md` sorted descending.
- Exact per-location EAPC values (for all three measures) are transcribed in
  [../tables/table1.md](../tables/table1.md); this figure's incremental content is the sorted
  visual ranking and the relative-magnitude comparison across all 24 locations at a glance.
