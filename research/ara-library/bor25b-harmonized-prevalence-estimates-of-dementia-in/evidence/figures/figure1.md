# Figure 1: Association between the probability of being demented and frequent comorbidities of dementia

- **Source**: Figure 1, paper.pdf p.7 (Results)
- **Caption**: "Association between the probability of being demented and frequent comorbidities of dementia. The blue dots show the percentage by which the presence of a comorbidity decreases/increases the probability of being demented. The error bands denote 95% confidence intervals. For example, having had a diagnose of a stroke increases the probability of being demented by 7.2% which is statistically significant, while high blood pressure does not have a statistically significant association with dementia conditional on the other co-morbidities. All associations are conditional on age, sex and education."
- **Screenshot**: figure1.png
- **Figure type**: quantitative_plot
- **Extraction method**: digitized_estimate (three rows — stroke, diabetes, depression — additionally confirmed by exact values stated in body text; the remaining six rows are read off the plotted point/whisker positions only)
- **Reading confidence**: medium (axis has only four labeled gridlines: −.05, 0, .05, .1; point positions estimated visually relative to these ticks)

- **Plot kind**: coefficient/dot-and-whisker plot (Stata-style), horizontal
- **Axes**: X = percentage-point change in probability of being demented (linear scale, range shown −.05 to .1), Y = comorbidity/lifestyle factor (categorical, 9 rows)

| Factor | Point estimate (pp change in P(demented)) | 95% CI (approx.) | Crosses zero? | Statistically significant per text |
|---|---|---|---|---|
| self-rated health | ≈ +0.018 | ≈ +0.008 to +0.028 | No | Yes (implied — CI does not cross 0) |
| depression (EURO-D > 4) | +0.040 (exact, stated in text) | ≈ +0.030 to +0.048 | No | Yes |
| stroke | +0.072 (exact, stated in text) | ≈ +0.060 to +0.084 | No | Yes |
| diabetes | +0.008 (exact, stated in text) | ≈ +0.002 to +0.016 | No | Yes |
| high blood cholesterol | ≈ −0.006 | ≈ −0.013 to +0.002 | Yes | No |
| high blood pressure | ≈ −0.004 | ≈ −0.011 to +0.003 | Yes | No |
| some physical activity | ≈ −0.032 | ≈ −0.039 to −0.024 | No | Yes (reduces risk) |
| smoking | ≈ +0.013 | ≈ +0.006 to +0.021 | No | Yes |
| excessive alcohol | ≈ −0.003 | ≈ −0.019 to +0.013 | Yes (wide CI) | No |

## Trend summary
All nine associations are estimated from a single multivariate regression linking the probability of being demented to a self-reported doctor's diagnosis of each condition across SHARE Waves 1–9, conditional on age, sex and education. Three factors have point estimates confirmed exactly by the body text: stroke (+7.2 percentage points, the largest positive/risk-increasing association shown), depression via EURO-D>4 (+4.0 points), and diabetes (+0.8 points, smallest significant risk factor). Physical activity is the only protective (risk-reducing) factor with a CI clearly excluding zero (≈ −3.2 points). Smoking and self-rated health show smaller positive (risk-increasing) associations with CIs excluding zero. High blood cholesterol, high blood pressure, and excessive alcohol all have CIs crossing zero and are described in the text as not statistically significant conditional on the other comorbidities (excessive alcohol has the widest CI of the nine factors).
