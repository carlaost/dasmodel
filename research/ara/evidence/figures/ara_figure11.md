# Figure 11: Aggregate reproduction success rates by difficulty

- **Source**: Figure 11, §7.3 (Reproduction from ARA)
- **Caption**: "Aggregate reproduction success rates across all 15 papers, stratified by difficulty. The ARA advantage widens monotonically with difficulty (+4.9% easy, +5.6% medium, +8.5% hard), tracking the tiers where reproduction depends most heavily on configuration content the PDF underspecifies."
- **Screenshot**: ara_figure11.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels
- **Reading confidence**: high
- **Plot kind**: grouped bar
- **Axes**: X = difficulty tier (Easy / Medium / Hard), Y = Success Rate (%, linear, 0–100)

| Difficulty | ARA (%) | PDF + GitHub (%) | ARA advantage |
|------------|---------|------------------|---------------|
| Easy | 85.1 | 80.2 | +4.9% |
| Medium | 68.5 | 62.9 | +5.6% |
| Hard | 54.5 | 46.0 | +8.5% |

(Per-tier means match the bottom row of Table 11. Values are printed as data labels.)

## Trend summary
ARA beats PDF+GitHub at every difficulty tier; the gap widens monotonically from +4.9% (easy) to +8.5% (hard), concentrating where reproduction depends on under-specified configuration detail.
