# Figure 4: Relative preservation of Ex5 neurons in advanced AD
- **Source**: Figure 4, §"Relative preservation of layer 4 excitatory neurons during AD progression"
- **Caption**: "a Boxplots showing neuronal cell composition estimated with scCODA across pathology disease groups in BA9 and BA17. Individual donor proportions are overlaid as open circles. Data are presented as median (center line) and interquartile range (IQR; box limits); whiskers extend to the most extreme values within 1.5×IQR… Sample sizes for BA9: low 17, intermediate 10, high 15 donors; BA17: low 7, intermediate 5, high 12 donors. Credible differences between high and low pathology groups (red asterisks) and between intermediate and low groups (black asterisks)… for clusters with a magnitude of change (log2-fold change) greater than 0.1… Credible effects were defined at those with a posterior inclusion probability (PIP) > 0.95. The lower plots show the credible effects (orange) along with the fold changes… b Differential cell proportion analysis… using GLMM in BA9 and BA17. Ex5 neurons showed increased relative abundance in advanced AD in BA9 (FDR = 0.008). In BA17, Ex5 neurons showed a non-significant trend of increase (p-value = 0.06), while reductions were observed in deeper-layer excitatory populations, including Ex8 (L5 IT; p-value = 0.02), Ex11 (L5 IT; p-value = 0.01), Ex12 (L6 IT; p-value = 0.01), and Ex13 (L6 IT Car3; p-value = 0.05)…"
- **Screenshot**: figure4.png
- **Figure type**: quantitative_plot (scCODA boxplots + log2FC bars; GLMM volcano scatter)
- **Extraction method**: exact_from_labels (text/caption-stated values) — plot points not individually labeled
- **Reading confidence**: high (for stated values); medium (per-donor points)

## Panel a — scCODA (boxplots of proportion + log2FC bars, high vs low)
- **Axes**: proportion (0–0.30 BA9; 0–0.6 BA17); lower bars = log2FC (High vs Low), −0.5 to 2.0; error bars = SEM. Credible = orange.

| Cluster | Region | log2FC (High vs Low) | Note |
|---------|--------|----------------------|------|
| Ex5 | BA9 | 1.75 | credible increase (largest positive bar) |
| Ex5 | BA17 | 0.46 | credible increase |
| Ex3 (SV2C deep-L3) | BA9 | negative (≈ −0.4) | credible decrease (vulnerable) |
| Ex7 | BA9 | negative (≈ −0.2) | credible decrease |
| In4 (SST) | BA9 | negative | credible (less robust) |
| In6 (SST) | BA17 | negative | credible (less robust) |

(log2FC values other than Ex5's 1.75 / 0.46 are read approximately from the bar plot: `≈`.)

## Panel b — GLMM (volcano: −log10 p-value vs Z score)
| Cluster | Region | p-value | direction |
|---------|--------|---------|-----------|
| Ex5 | BA9 | FDR = 0.008 | increase (credible) |
| Ex5 | BA17 | p = 0.06 | increase (trend, ns) |
| Ex8 (L5 IT) | BA17 | p = 0.02 | reduction |
| Ex11 (L5 IT) | BA17 | p = 0.01 | reduction |
| Ex12 (L6 IT) | BA17 | p = 0.01 | reduction |
| Ex13 (L6 IT Car3) | BA17 | p = 0.05 | reduction |

## Trend summary
Ex5 is the standout population whose relative proportion increases with pathology (credible in BA9,
trend in BA17), consistent with resilience as neighbors are lost; deeper-layer excitatory subtypes
(Ex8/Ex11/Ex12/Ex13) trend down in BA17. Directly supports C01; with sensitivity analyses, C02.
