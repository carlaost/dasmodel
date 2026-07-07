# Figure 2: The correlation between the socio-demographic index with age-standardized incidence, death, and DALY rates of Alzheimer's disease and other dementias, in 204 countries or territories, 2021, by sex

- **Source**: Figure 2, Results (p.9 of paper.pdf)
- **Caption**: "The correlation between the socio-demographic index with age-standardized incidence, death, and DALY rates of Alzheimer's disease and other dementias, in 204 countries or territories, 2021, by sex. (where circle size represents the number of incident cases, death cases, and DALYs of ADOD in 2021; the blue line and grey shadows represent the overall trends and 95%CIs in ADOD age-standardized rates associated with SDI, and the dashed lines represent quantile regression results for each quantile/95th,75th,50th, 25th, and 5th percentiles)"
- **Screenshot**: figure2.png
- **Figure type**: quantitative_plot
- **Extraction method**: digitized_estimate (no data labels printed on the scatter/regression curves; readings below are visual trend estimates, not exact source values)
- **Reading confidence**: medium

## Plot description
A 3×3 grid of scatter plots. Rows = ASIR, ASDR, ASR-DALYs (Y axis, per 100,000, linear scale, panel-specific range). Columns = Both sexes, Male, Female. X axis in every panel = SDI (linear scale, range ≈0.1-0.95). Each point is one of 204 countries/territories in 2021; point size encodes the country's incident/death/DALY count (legend gives 2-3 reference sizes per panel, e.g. "Incidents×10³: 500/1000/1500" for the Both-sexes ASIR panel). A solid blue trend line with grey 95% CI shading shows the overall (mean) association between SDI and the age-standardized rate; five dashed lines (colors per legend, not separately labeled in-panel beyond a general "quantile regression" note) show quantile-regression fits at the 5th, 25th, 50th, 75th, and 95th percentiles.

- **Axes**: X = SDI (unitless index, 0-1 scale), linear. Y = age-standardized rate per 100,000 (ASIR / ASDR / ASR-DALYs), linear; ranges: ASIR Both-sexes ≈60-135, Male ≈55-120, Female ≈80-150ish; ASDR Both-sexes ≈15-35, Male ≈15-27, Female ≈15-40ish; ASR-DALYs Both-sexes ≈350-500ish, Male ≈250-450, Female ≈350-550ish (axis gridline labels read approximately from the low-resolution render).

## Approximate/qualitative reading (no data table — points are 204 individual countries, not resolvable to exact values from this render)

| Row | Both sexes trend | Male trend | Female trend |
|---|---|---|---|
| ASIR vs SDI | Rising, mildly nonlinear: shallow at low SDI (≈0.1-0.4), steepening around SDI≈0.4-0.7, flattening again above ≈0.7-0.8 | Similar rising shape; the text notes ASIR for males rises rapidly at low SDI, then slows / slightly declines beyond SDI≈0.6 | Rising trend; flatter/slightly declining at low SDI, then accelerating once SDI passes a threshold (per text) |
| ASDR vs SDI | Declines from low to mid SDI (≈0.1-0.6), reaches a trough around SDI≈0.6-0.7, then rises again toward SDI≈0.9 (a shallow U/valley shape) | Broadly flat-to-rising across the SDI range, less pronounced trough than "both sexes" | Declines then plateaus/rises slightly; trough visible around SDI≈0.5-0.7 |
| ASR-DALYs vs SDI | Similar shallow U/valley shape to ASDR: mild decline then a slight rise at high SDI | Rising trend across the SDI range | Declines then plateaus, valley near SDI≈0.6-0.7 |

The dashed quantile-regression lines fan out from the solid mean-trend line at both ends of the SDI range in every panel — i.e., the spread between the 5th and 95th percentile fitted lines is visibly wider at low and high SDI than in the middle, indicating the SDI-ASR relationship's variability across countries differs by quantile (consistent with the paper's stated rationale for using quantile regression alongside the mean-trend spline).

## Trend summary
Across all three burden measures, the country-level scatterplots show a materially nonlinear (not straight-line) relationship between SDI and age-standardized rates, differing by measure: ASIR trends upward with SDI (steeper in the mid-SDI range); ASDR and ASR-DALYs show a shallow valley — declining from low to mid SDI, then rising again at the highest SDI levels — broadly consistent with the paper's text: "the incidence of ADOD increased more rapidly as SDI increased in areas that have historically shown lower incidence... in regions with higher mortality or DALYs burden, these indicators decreased relatively faster as SDI increased" (Abstract). Because this is a 204-point scatter with no printed axis data labels, exact per-country or per-SDI values cannot be recovered from the image; the reading above is directional only (reading confidence: medium).
