# Table 10: Cost of below-reference exploration across 24,008 agent runs

**Source**: Table 10, Appendix E.3 (Exploration Cost Detailed Breakdown)
**Caption**: "Cost of below-reference exploration across 24,008 agent runs (21 frontier models, 228 tasks). The exploration itself is necessary research work; the cost only becomes waste when subsequent agents must re-incur it because the failure record is not preserved in the published artifact."
**Screenshot**: ara_table10.png
**Extraction type**: raw_table

| Metric | Tokens | Cost |
|--------|--------|------|
| Below-reference run rate (overall) | 31.6% | — |
| Below-reference run rate (RE-Bench) | 73.4% | — |
| Cost ratio: below-ref vs. ref (median) | 113× | — |
| Dead-end exploration | 44.8% | — |
| Re-derivation of known solutions | 14.4% | — |
| Total below-reference exploration | 59.2% | 90.2% |

Notes (from §7.4 / Appendix E.3 text): total dollar cost across the corpus is $63,483; mean below-reference token cost is 8.6× a reference-reaching run (2.58M vs. 300K tokens per run); median 113×. At the per-task level, easy tasks reach reference 85.4% of the time, medium 30.7%, hard 15.1%.
