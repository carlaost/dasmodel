# Figure 1 — Continuous biomarker z-scores and HR of transition across cognitive stages

**Source**: `paper.pdf` p.3 (main text, full page), rendered at 5x scale (cropped to the figure region, excluding running header/footer) to `figure1.png`. Visually inspected in three row-bands at higher magnification (Aβ42/40+p-tau181; p-tau217+t-tau; NfL+GFAP) to confirm axis labels, curve shapes, and shaded-band extents before transcribing.

**Caption (verbatim)**: "Fig. 1 | Continuous values of blood biomarkers of Alzheimer's disease (AD) and hazard ratio (HR) of progression from normal cognition (NC) to mild cognitive impairment (MCI), reversion from MCI to NC, and progression from MCI to all-cause dementia. Hazard Ratios (HR) with 95% Confidence Intervals (CI) are derived from multistate Markov models, using age as time scale and adjusted for sex and education. AD blood biomarkers were converted into z-scores and modeled using restricted cubic splines with 3 prespecified knots at 25th, 50th, and 75th percentiles. The median value was chosen as reference for all the z-scored biomarkers. Aß42/40 amyloid beta 42/40, MCI mild cognitive impairment, NC normal cognition, p-tau181 phosphorylated tau 181, p-tau217 phosphorylated tau 217, t-tau total tau, NfL neurofilament light chain, GFAP glial fibrillary acidic protein. Color schemes: Aß42/40: yellow; p-tau181: red; p-tau217: purple; t-tau: blue; NfL: green; GFAP: turquoise."

## Figure type
`quantitative_plot` — an 18-panel grid (6 biomarker rows × 3 transition columns) of HR curves with shaded 95% CI bands, on log-scale y-axes.

## Extraction method and reading confidence
- **Extraction method**: `visual_description` for curve shapes/trends; `digitized_estimate` (≈) for specific HR values read off the log-scale axis at the panel extremes (no data labels are printed on this figure — unlike Fig. 2, no exact numeric HR values are given for Fig. 1; all values here are visually estimated).
- **Reading confidence**: medium. The y-axis gridlines (0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0 — log scale) and x-axis gridlines (z-score −1, 0, 1, 2) are clearly legible at the rendered resolution; curve endpoints were read against these gridlines. Because no data labels exist, all specific numbers below are approximate (≈) and should not be treated as source-verbatim exact values (those come from Table 2 / body text for the dichotomized analysis instead).

## Panel-by-panel description (each cell: HR curve, solid black line, with a colored 95% CI shaded band; dashed horizontal line at HR=1)

**Row: Aβ42/40 (yellow band)**
- NC→MCI: flat, HR≈1 across z ∈ [−1, 2]; band widens at the extremes (z=2 upper ≈2.5).
- MCI→NC: flat/slightly rising, HR≈1 at z=0 to ≈1.2 at z=2; wide band.
- MCI→all-cause dementia: HR≈1.5-2 at z=−1, dips to ≈1 near z=0, rises slightly to ≈1.1-1.2 at z=2 — a shallow U-shape rather than monotonic, consistent with this biomarker's weak/non-monotonic association (Table 2 shows only a modest dichotomized HR of 1.30).

**Row: p-tau181 (red band)**
- NC→MCI: flat, HR≈1 across the range.
- MCI→NC: HR≈1.2 at z=−1 declining to ≈0.6-0.7 at z=2 (declining trend, consistent with Table 2's HR 0.50 basic-model reversion association).
- MCI→all-cause dementia: HR≈1 at z=−1 rising to ≈2.0-2.2 at z=2 (rising, monotonic).

**Row: p-tau217 (purple band)**
- NC→MCI: HR≈1 at z=−1 rising slightly to ≈1.3-1.4 at z=2.
- MCI→NC: HR≈1.2 at z=−1 declining to ≈0.4 at z=2 (declining).
- MCI→all-cause dementia: HR≈0.8 at z=−1 rising steeply and monotonically to ≈2.2 at z=2 — one of the steepest curves in the grid, consistent with p-tau217 being one of the two strongest biomarkers (Table 2 HR 1.74).

**Row: t-tau (blue band)**
- NC→MCI: flat, HR≈1 across the range.
- MCI→NC: flat, HR≈1 across the range (wide band).
- MCI→all-cause dementia: HR≈1 at z=−1 rising to ≈2.2 at z=2 (rising, monotonic).

**Row: NfL (green band)**
- NC→MCI: HR≈0.6-0.7 at z=−1, rising to ≈1 near z=0, roughly flat thereafter to z=2.
- MCI→NC: HR≈1.3 at z=−1 declining to ≈0.9 at z=2 (mild decline).
- MCI→all-cause dementia: HR≈0.4 at z=−1 rising steeply to ≈2 near z=0.5 and continuing to ≈4.5-5 at z=2 — the steepest, highest-reaching curve in the entire grid, consistent with NfL being the single strongest biomarker for this transition (Table 2 HR 1.84 dichotomized; text reports HR 2.34 for AD dementia specifically).

**Row: GFAP (turquoise band)**
- NC→MCI: HR≈0.7 at z=−1 rising to ≈1 near z=0, roughly flat to slightly declining thereafter (≈0.8 at z=2).
- MCI→NC: HR≈1 at z=−1 declining steadily to ≈0.2 at z=2 (strong decline — the steepest downward reversion curve in the grid, consistent with GFAP's significant basic + fully-adjusted reversion HRs in Table 2).
- MCI→all-cause dementia: HR≈0.5 at z=−1 rising to ≈1.4 near z=0, continuing to ≈1.8-1.9 at z=2 (rising, monotonic, though less steep than NfL or p-tau217).

## Cross-cutting visual pattern
Across all six rows, the "NC→MCI" column is visually flat (HR hugging 1) while the "MCI→all-cause dementia" column shows the steepest, most consistently rising curves — the figure's core visual argument for claim C02 and the null result C05.
