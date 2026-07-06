# Figure 4: Associations between VeraBIND Tau semi-quantitative measure and cognition/tau-PET/plasma biomarkers

- **Source**: Figure 4, "Tables and Figures" section, PDF p.47 (caption continues onto PDF p.48)
- **Caption**: "Fig. 4. Associations between VeraBIND Tau semi-quantitative measure and: A. Mini-Mental State Examination score (MMSE), B. Episodic memory composite score (z-score), C. Entorhinal tau burden, as measured using [18F]MK6240 tau-PET Standard Uptake Value ratio (SUVr), D. Inferior temporal tau burden (SUVr), E. Plasma concentration of pTau217 (pg/mL), F. Plasma concentration of pTau181 (pg/mL). VeraBIND Tau semi-quantitative scores were plotted on a logarithmic scale. rs = Spearman's rho."
- **Screenshot**: figure4.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels (correlation coefficients are printed data labels on each panel); digitized_estimate (individual scatter positions)
- **Reading confidence**: high (for printed rs/p values); medium (for the scatter-cloud shape)

- **Plot kind**: scatter with fitted regression line and shaded 95% CI band, 6 panels (A–F)
- **Axes**: Y = VeraBIND Tau Score (RLU ratio), **log scale**, all 6 panels (gridlines at 0.6, 1.0, 1.6, 2.7, per the caption's explicit statement that the score was plotted logarithmically). X-axes are linear and panel-specific: A = MMSE (/30), B = Episodic memory z-score, C = Entorhinal tau-PET SUVr, D = Inferior temporal tau-PET SUVr, E = Plasma pTau217 concentration (pg/mL), F = Plasma pTau181 concentration (pg/mL). Points colored/shaped by A/T group: A−T− (blue circle), A−T+ (red circle), A+T− (blue asterisk), A+T+ (red asterisk).

| Panel | X variable | Age-adjusted Spearman's rho | p-value |
|---|---|---|---|
| A | MMSE (/30) | rs = -0.42 | p<0.001 |
| B | Episodic memory z-score | rs = -0.53 | p<0.001 |
| C | Entorhinal tau-PET SUVr | rs = 0.71 | p<0.001 |
| D | Inferior temporal tau-PET SUVr | rs = 0.62 | p<0.001 |
| E | Plasma pTau217 concentration (pg/mL) | rs = 0.60 | p<0.001 |
| F | Plasma pTau181 concentration (pg/mL) | rs = 0.44 | p<0.001 |

## Trend summary
All six panels show a clear monotonic association in the expected direction: VeraBIND Tau score decreases with better cognition (panels A, B — negative slope) and increases with greater tau-PET burden and higher pTau217/pTau181 concentration (panels C–F — positive slope). The strongest association by far is with entorhinal tau-PET SUVr (panel C, rs=0.71), visually the tightest scatter around the fitted line; the weakest of the six is with MMSE (panel A, rs=-0.42), consistent with MMSE's known ceiling effect in largely-preclinical samples. In every panel, A+T+ points (red asterisks, mostly CI participants) cluster at higher VeraBIND Tau scores and worse-direction X values, while A−T− points (blue circles, mostly CU) cluster at lower VeraBIND Tau scores; one clear high-leverage outlier point (VeraBIND Tau score ≈2.8, an A−T+ case) appears near the top of every panel. This figure is the visual basis for Claim C08.
