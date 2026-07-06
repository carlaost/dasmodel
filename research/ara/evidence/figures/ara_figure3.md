# Figure 3: The reproduction information gap across 8,921 PaperBench requirements

- **Source**: Figure 3, §1 / §7.1 (also detailed in Appendix E.2)
- **Caption**: "The reproduction information gap across 8,921 PaperBench requirements. (a) PDFs systematically under-specify code development tasks. (b) The three largest gap types are precisely the categories ARA's structured layers address."
- **Screenshot**: ara_figure3.png
- **Figure type**: mixed (quantitative_plot panel (a) stacked bar; quantitative_plot panel (b) pie)
- **Extraction method**: exact_from_labels
- **Reading confidence**: high

## Panel (a): Information sufficiency by task category — stacked bar
- **Plot kind**: stacked bar (Sufficient / Partial / Absent, summing to 100%)
- **Axes**: X = task category (with requirement count), Y = Percentage of requirements (%, linear, 0–100)

| Task category (n) | Sufficient | Partial | Absent |
|-------------------|-----------|---------|--------|
| Code Development (3,942) | 37.3% | 54.9% | 7.8% |
| Code Execution (4,355) | 50.5% | 47.9% | 1.6% |
| Result Analysis (624) | 60.6% | 36.9% | 2.6% |
| Overall (8,921) | 45.4% | 50.2% | 4.4% |

(Mirrors Table 8. Partial+Absent = 54.6% overall.)

## Panel (b): Gap type distribution — pie
| Gap type | % |
|----------|---|
| Missing hyperparameter | 26.2% |
| Vague description | 21.9% |
| Cross-reference only | 13.4% |
| Missing code detail | 10.9% |
| Missing baseline detail | 10.8% |
| Missing URL | 5.5% |
| Figure only | 5.1% |
| Ambiguous specification | 4.1% |
| Implicit assumption | 1.5% |

(Mirrors Table 9.)

## Trend summary
Only 45.4% of requirements are fully specified in source PDFs; code development is the most under-specified category (37.3% sufficient). Missing hyperparameters + vague descriptions + cross-references account for >60% of all gaps.
