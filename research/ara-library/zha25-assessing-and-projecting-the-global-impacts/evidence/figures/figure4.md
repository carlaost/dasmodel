# Figure 4: Projected global burden of rate percentages of Alzheimer's disease in 2030, by sexes and locations

- **Source**: Figure 4, Results §3.5 (end) / §4 Discussion transition, p.8
- **Caption**: "Projected global burden of rate percentages of Alzheimer's disease in 2030, by sexes
  and locations. (A) ASIR, (B) ASDR, and (C) age-standardized DALY rate. DALY = disability adjusted
  life-year. ASIR = age standardized incidence rate. ASDR = age standardized death rate. ASRs = age
  standardized rates."
- **Screenshot**: figure4.png
- **Figure type**: quantitative_plot
- **Extraction method**: `visual_description` — the two-color split within each bar has no printed
  numeric labels and no color-key legend (see Note below), so exact percentage splits are read
  approximately (≈) off the shared 0–100 axis; the total-bar-length dimension carries no
  information (every bar spans the full 0–100% by construction of a 100%-stacked bar).
- **Reading confidence**: medium for the approximate percentage split per location (axis gridlines
  at every 20 units allow reasonably precise interpolation); **the assignment of colors to sexes is
  unverifiable** (see Note).

- **Plot kind**: three horizontal 100%-stacked bar charts (A/B/C), one bar per location, two
  segments per bar (green, red).
- **Axes**:
  - Panel A ("Sex Percentage for Incidence in 2030"): X = Percentage, gridlines at 0, 20, 40, 60,
    80, 100.
  - Panel B ("Sex Percentage for Deaths in 2030"): same X-axis convention.
  - Panel C ("Sex Percentage for DALYs (Disability-Adjusted Life Years) in 2030"): same X-axis
    convention.
  - Y (shared, all three panels; 24 locations, listed top-to-bottom): Western Europe, Tropical
    Latin America, Southern Sub-Saharan Africa, Southern Latin America, Southeast Asia, Oceania,
    Middle SDI, Low-middle SDI, Low SDI, High-middle SDI, High-income North America, High-income
    Asia Pacific, High SDI, Global, Eastern Sub-Saharan Africa, Eastern Europe, East Asia, Central
    Sub-Saharan Africa, Central Latin America, Central Europe, Central Asia, Caribbean, Australasia,
    Andean Latin America — the same 24-location set as `tables/table1.md`, listed in reverse order
    (Andean Latin America at the bottom, Western Europe at the top).
  - Scale: linear, 0–100%.
- **Color**: two-color 100%-stacked split, green + red, per bar. **No legend is printed identifying
  which color corresponds to male vs. female** in any of the three panels (unlike Figures 1 and 2,
  which do carry legends) — see `logic/solution/constraints.md` C-g. The sex assignment of each
  color cannot be determined from the provided PDF.

## Trend summary
- Most location bars split roughly 40–60% green/red (i.e., close to an even sex split), consistent
  with the paper's own 2030 sex-specific point estimates for the Global row (claim C02: male vs.
  female 2030 ASRs for death, DALY, and incidence rate are all within roughly 5% of each other).
- A few locations show a visibly more lopsided split: **High-income Asia Pacific** and
  **Australasia** show the green segment extending to roughly 65–70% of the bar in all three
  panels (the most one-sided split among locations with a visible two-color division).
- **Eastern Europe is a striking outlier**: in Panels A (Incidence) and B (Deaths), the Eastern
  Europe bar is **entirely green with no visible red segment at all** (100%–0% split) — the only
  location in either panel with no visible second color. In Panel C (DALYs), however, the Eastern
  Europe bar shows a small red segment starting at roughly 80–85% (i.e., approximately 80–85%
  green / 15–20% red) — visibly different from its own all-green appearance in Panels A and B. This
  panel-to-panel inconsistency for the same location is not discussed by the authors and is
  reproduced here as a factual visual observation, not corrected (Rule 10); it is consistent in
  spirit with the other Eastern-Europe-specific data-quality signals already noted for this paper
  (the near-zero-width 2030 DALY-ASR uncertainty interval and outsized EAPC magnitudes in
  `tables/table1.md` and `evidence/figures/figure2.md`).
- Because the color-to-sex mapping is unverifiable (no legend, per the Note above), this figure
  cannot be used to determine numerically *which* sex is over- or under-represented at any
  location; it is filed as visual evidence of the relative split magnitude and the Eastern Europe
  anomaly only, not as a source for any claim's `Statement`.
