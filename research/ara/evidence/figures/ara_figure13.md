# Figure 13: Per-paper ARA − baseline reproduction delta (heatmap)

- **Source**: Figure 13, Appendix F.2 (Per-Paper Reproduction Analysis)
- **Caption**: "Per-paper ARA − baseline delta (percentage points) on each difficulty stratum, sorted by mean advantage. Green indicates ARA wins, red indicates baseline wins. Gains concentrate in the medium and hard columns across most papers; the few baseline wins are confined to a small set, most prominently self-expansion and ftrl."
- **Screenshot**: ara_figure13.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels
- **Reading confidence**: high
- **Plot kind**: heatmap (cell-annotated)
- **Axes**: X = difficulty (Easy / Medium / Hard); Y = paper (sorted by mean advantage); color = ARA − Baseline (percentage points), green positive / red negative.

| Paper | Easy | Medium | Hard |
|-------|------|--------|------|
| mech.-und. | +3.2 | +51.6 | +12.1 |
| pinn | +17.4 | +18.8 | +23.9 |
| seq.-neural | +25.9 | +14.8 | +11.9 |
| fre | +17.1 | +12.8 | +22.3 |
| all-in-one | −0.9 | +4.5 | +19.1 |
| self-comp.-pol. | −5.8 | +10.5 | +15.1 |
| bbox | −4.5 | +6.8 | +14.3 |
| stoch.-interp. | +2.2 | 0.0 | +1.7 |
| sample-masks | 0.0 | −5.9 | +5.4 |
| adaptive-pruning | +1.1 | −3.0 | −3.3 |
| test-time-adapt. | −6.6 | −6.5 | +3.9 |
| bam | −2.9 | +2.0 | −11.9 |
| self-expansion | +13.9 | −27.5 | −8.0 |
| ftrl | −11.2 | −16.4 | +2.0 |

## Trend summary
ARA gains concentrate in the medium/hard columns; the largest single cell is mechanistic-understanding medium (+51.6). Baseline wins are confined to a few papers (most prominently self-expansion medium −27.5, ftrl medium −16.4, bam hard −11.9). Deltas are consistent with the per-paper weighted columns of Table 11.
