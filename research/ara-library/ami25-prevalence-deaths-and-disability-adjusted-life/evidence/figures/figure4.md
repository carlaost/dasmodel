# Figure 4: Age-standardised DALY rate vs Socio-demographic Index by country, MENA 2021

- **Source**: Figure 4, Results (§"Relationship with the SDI"), p.8
- **Caption**: "Age-standardised DALY rates of AD and other types of dementia for 21 countries and territories in 2021, by SDI; expected values based on the SDI and disease rates in all locations are shown as the black line. Each point shows the observed age-standardised DALY rate for each country in 2021 (generated from data available from http://ghdx.healthdata.org/gbd-results-tool)."
- **Screenshot**: figure4.png
- **Figure type**: quantitative_plot
- **Extraction method**: visual_description (no printed data labels; a dense multi-country trajectory scatter)
- **Reading confidence**: medium

- **Plot kind**: scatter with a fitted smoothing-spline line ("Smooth", black)
- **Axes**: X = Socio-demographic Index, scale: linear, 0.2–0.9; Y = Age-standardised DALY rate per 100,000 population, scale: linear, ≈420–600.
- **Series**: one marker style/colour per country (legend lists North Africa and Middle East [black filled dots], Afghanistan, Algeria, Bahrain, Egypt, Iran, Iraq, Jordan, Kuwait, Lebanon, Libya, Morocco, Oman, Palestine, Qatar, Saudi Arabia, Sudan, Syrian Arab Republic, Tunisia, Turkey, United Arab Emirates, Yemen) plus the black "Smooth" expected-value line. Each country appears as a trajectory of points (its year-by-year 1990→2021 track across SDI values).

## Trend summary (per text §"Relationship with the SDI", p.5, 8)
- The black smoothing-spline (expected DALY rate given SDI across all GBD locations) DECREASES as SDI
  rises from ≈0.2 to ≈0.4, then shows a slight rise up to SDI ≈0.47, then generally decreases for
  higher SDIs, with a minor increase in the 0.6–0.65 range. (verbatim structure from text)
- Observed country trajectories: burden was HIGHER than SDI-expected in Afghanistan, Libya, Turkey,
  Tunisia, Algeria, and Bahrain; and LOWER than expected in Sudan, the Syrian Arab Republic, Jordan,
  and Egypt. Supports C08.
- Visually, high-DALY tracks (Afghanistan red triangles ≈575–605 at low SDI; Turkey purple squares
  and Tunisia purple triangles ≈500–550 at mid SDI) sit above the smooth line; lower tracks (Sudan
  blue asterisks ≈440–480; Yemen magenta open circles) sit below.
- No monotonic dose–response is evident; the paper concludes "no clear trends in changes in dementia
  burden relative to SDI in MENA countries."

Exact per-country 2021 DALY ASRs are in [tables/table1.md](../tables/table1.md); this figure adds the
SDI positioning and the expected-vs-observed comparison, which carry no printed numeric labels.
