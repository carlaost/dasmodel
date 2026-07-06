# Figure 2: Stratification of tissue microdomains by adjacent-section IHC intensities
- **Source**: Figure 2, Page 8 of 23
- **Caption**: "Stratification of tissue microdomains by adjacent-section IHC intensities. A
  Representative images of different plaque types from two ST-adjacent sections. Six spots (1-6;
  including all major plaque types) are shown with a 55-µm spot area superimposed to scale. B We
  stratified all ST spots by Aβ intensity into no (white; log2(avg Aβ intensity + 1) between 2.5
  and 4), low (yellow; log2(avg Aβ intensity + 1) between 4 and 6.5), or high (blue; log2(avg Aβ
  intensity + 1) > 6.5) groups. The distribution of Aβ IF intensity is shown for each group. C A
  subset of 781 spots from ST-adjacent sections were selected for manual plaque-type annotation
  (Supplementary Table 5). The proportion of plaque types is shown, stratified by low or high
  intensity of Aβ [odds ratio (OR) and p-value based on Fisher's Exact test indicated]. D Spots
  were further stratified by the abundance of glia (GFAP: x-axis, IBA1: y-axis). Scatterplots show
  the average GFAP and IBA1 intensities for each ST spot among Low Aβ (left) and High Aβ (right)
  groups (red: glia-low, blue: glia-high). Gray-colored spots had intermediate GFAP/IBA1 intensity
  and were not sorted into a group"
- **Screenshot**: figure2.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (panel B group sizes and panel C OR/p are printed data
  labels; panel A/D are qualitative/quantitative images without a discrete data table)
- **Reading confidence**: high

## Data table (Panel B - Aβ intensity stratification group sizes, quantitative_plot / violin)
- **Plot kind**: violin (distribution of log2(avg Aβ intensity+1) per group)
- **Axes**: X = Aβ stratification group (categorical: no Aβ, low Aβ, high Aβ), Y =
  log2(avg Aβ intensity + 1), scale: linear (range shown ~0-12.5)

| Group | n (spots) | Approx. Y range (log2 avg Aβ intensity+1) |
|-------|-----------|------|
| no Aβ | 23,072 | ~2.5-4 (per stratification definition) |
| low Aβ | 93,947 | ~4-6.5 |
| high Aβ | 34,215 | ~6.5-12.5 (observed distribution extends higher) |

## Trend summary (Panel B)
Group sizes (n=23,072 / 93,947 / 34,215 for no/low/high Aβ) are printed directly on the violin
plot as data labels; total = 151,234 spots shown in this panel (a gray-matter/tissue-covered
subset of the full 258,987-spot dataset — the paper elsewhere states 258,986/258,987 total spots
across no/low/high strata combined with additional excluded/ungrouped spots). The high-Aβ group's
distribution extends to visibly higher log2 intensity values than the low-Aβ group, consistent
with the stratification definition.

## Data table (Panel C - plaque-type proportion by Aβ stratum)
- **Plot kind**: stacked horizontal bar (proportions)
- **Axes**: X = proportion of plaque type (0 to 1, linear), Y = Aβ stratum (low Aβ, high Aβ)

| Aβ stratum | Diffuse (≈proportion) | Compact (≈proportion) | Dense core (≈proportion) | OR (vs. other stratum) | p-value |
|---|---|---|---|---|---|
| low Aβ | ≈0.72 | ≈0.28 | ≈0.00 (negligible) | 3.02 | 3.21e-9 |
| high Aβ | ≈0.28 | ≈0.65 | ≈0.07 | 3.02 | 3.21e-9 |

Proportions for compact/diffuse/dense-core are read off the stacked-bar boundaries (digitized
estimate, marked ≈); the OR=3.02 and p=3.21e-9 values are exact, printed/stated values (also
confirmed in main text, Page 11 of 23).

## Trend summary (Panel C)
Low-Aβ spots are enriched for diffuse plaques; high-Aβ spots are enriched for compact and dense-core
plaques (OR=3.02, p=3.21e-9), supporting claim C05's mapping of the Aβ-intensity stratification onto
classical plaque maturity typing, based on n=781 manually annotated spots (Supplementary Table 5,
not included in provided PDF).

## Visual description (Panel A - qualitative_sample)
- **Shows**: Six representative ST-adjacent-section IHC spots (55-µm spot area outlined), each
  imaged for DAPI/Aβ/IBA1/GFAP plus a merge channel, spanning the three defined types: low-Aβ
  diffuse plaques (spots 1, 4), high-Aβ compact plaques (spots 2, 5), and high-Aβ dense-core
  plaques (spots 3, 6), from two different ST-adjacent sections (11_D top, 20_B bottom).
- **Demonstrates**: Visually distinguishable staining morphology (diffuse fuzzy Aβ signal vs. dense
  compact/core Aβ signal) underlying the manual plaque-type annotation used to validate the
  intensity-based stratification.
- **Supports**: C05.

## Data table / visual description (Panel D - glia stratification scatterplots, quantitative_plot)
- **Plot kind**: scatter (two panels: Low Aβ spots, High Aβ spots)
- **Axes**: X = log2(avg GFAP intensity+1), linear scale (~0-12); Y = log2(avg IBA1 intensity+1),
  linear scale (~0-12)
- Individual point coordinates are not extractable at this resolution (thousands of overlapping
  points per panel); no numeric table is transcribed. Points are colored red (glia-low: IBA1<6.2
  and GFAP<6.5) or blue (glia-high: IBA1>6.8 and/or GFAP>7.2); intermediate/gray points are
  unclassified.

## Trend summary (Panel D)
Both Low-Aβ and High-Aβ spot populations show a continuous, positively associated GFAP-IBA1
intensity cloud, with a clear separable subpopulation of high-GFAP/high-IBA1 points (blue,
glia-high) distinct from the low-intensity cluster (red, glia-low) in both panels, visually
validating that the glia-high/glia-low intensity thresholds separate a distinguishable
subpopulation of spots rather than arbitrarily bisecting a unimodal distribution.
