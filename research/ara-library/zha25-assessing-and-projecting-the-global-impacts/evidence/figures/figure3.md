# Figure 3: Projected Trends of global burden of age-standardized rates of Alzheimer's disease from 1990 to 2030, by SDI regions

- **Source**: Figure 3, Results §3.5, p.7
- **Caption**: "Projected Trends of global burden of age-standardized rates of Alzheimer's disease
  from 1990 to 2030, by SDI regions. (A) ASIR, (B) ASDR, and (C) age-standardized DALY rate. DALY =
  disability adjusted life-year. ASIR = age standardized incidence rate. ASDR = age standardized
  death rate. ASRs = age standardized rates."
- **Screenshot**: figure3.png
- **Figure type**: quantitative_plot
- **Extraction method**: `exact_from_labels` for each line's start (1990) / historical-window and
  projected-window direction, cross-referenced to the exact EAPC values already transcribed in
  `tables/table1.md` for Global + the 5 SDI tiers; `visual_description` for the trajectory shape
  (the historical decline and, for some strata, the projected-window reversal) since no data labels
  are printed on the lines themselves and the yearly X-axis tick labels are too small to resolve
  individual annual values.
- **Reading confidence**: high for line identity (color-coded, legend below each panel) and for the
  qualitative shape of each trajectory (monotonic decline vs. decline-then-reversal); low for
  reading exact intermediate-year ASR values off the lines (no gridline-level precision possible
  for individual years).

- **Plot kind**: three side-by-side line charts (A/B/C) sharing the same six-line legend; each line
  is a stratum's annual ASR from 1990 to 2030, with a shaded confidence/uncertainty band that
  widens over the 2022–2030 projected segment (visually distinguishing observed 1990–2021 GBD
  estimates from GAM-projected 2022–2030 values, though no vertical divider or the year "2021"/"
  2022" is explicitly marked).
- **Axes**:
  - Panel A ("Trend of Incidence"): Y = ASR, gridlines at 1000, 2000, 3000, 4000, 5000.
  - Panel B ("Trend of Deaths"): Y = ASR, gridlines at 0, 250, 500, 750.
  - Panel C ("Trend of DALYs (Disability-Adjusted Life Years)"): Y = ASR, gridlines at 5000, 10000,
    15000, 20000.
  - X (shared, all three panels): Year, annual ticks 1990–2030 (rotated, individually small but
    continuous).
  - Scale: linear in all three panels.
- **Color/series** (identical legend under each panel): Global = navy, High-middle SDI = green,
  Low-middle SDI = purple, High SDI = red, Low SDI = teal/cyan, Middle SDI = peach/orange.

## Trend summary
- **Low SDI (teal)** is the standout trajectory in all three panels: it declines from the highest
  or near-highest 1990 starting value through roughly the mid-2010s, reaches a visible trough, and
  then **reverses upward** through 2030, ending as the single highest line in each panel by 2030 —
  directly consistent with Low SDI's positive 2022–2030 EAPC in `tables/table1.md` (DALYs 1.4387,
  Deaths 1.7575, Incidence 1.1660 — the only SDI tier besides Low-middle SDI with a positive
  projected EAPC on all three measures).
- **High-middle SDI (green)** declines steadily and its shaded uncertainty band visibly widens
  toward 2030, ending among the lowest lines with the widest band of any stratum — consistent with
  High-middle SDI's strongly negative 2022–2030 EAPC (DALYs −3.5088, Deaths −4.4899, Incidence
  −2.5446 — the most negative of the five SDI tiers in Table 1).
- **Low-middle SDI (purple)** flattens and turns slightly upward after roughly the mid-2010s,
  ending essentially flat by 2030 — consistent with its small positive 2022–2030 EAPC (DALYs 0.3827,
  Deaths 0.6081, Incidence 0.0898).
- **Middle SDI (peach)** and **High SDI (red)** both continue a visually steady decline through
  2030, with High SDI ending as the lowest or near-lowest line — consistent with their negative
  2022–2030 EAPCs in Table 1 (Middle SDI: −1.5541/−1.7881/−1.4431; High SDI: −1.3768/−1.2757/
  −1.5120).
- **Global (navy)** declines throughout, sitting between the High-SDI/Middle-SDI cluster and the
  Low-SDI/Low-middle-SDI cluster for most of the series — consistent with its own negative EAPC in
  both windows (claim C01).
- This figure's incremental content beyond Table 1's endpoint EAPC values is the **visual shape** of
  each trajectory across the full 1990–2030 span — in particular, the Low SDI reversal (trough
  around the early-to-mid 2010s, then a sustained projected rise) and the widening uncertainty band
  for High-middle SDI, neither of which is quantified anywhere else in the main text.
