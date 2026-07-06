# Table 3: Understanding evaluation — accuracy and per-question token usage

**Source**: Table 3, §7.2 (Knowledge Extraction from ARA)
**Caption**: "Understanding evaluation: accuracy and per-question token usage across 450 paired outcomes. ARA wins at every category and every benchmark; the per-category mechanism is unpacked in Appendix E.4."
**Screenshot**: ara_table3.png
**Extraction type**: raw_table

Columns: Accuracy (%) for ARA and Baseline (BL); Tokens (K/Q = thousands per question) for ARA and BL. n = number of paired outcomes.

| Category | n | Accuracy ARA | Accuracy BL | Tokens ARA (K/Q) | Tokens BL (K/Q) |
|----------|---|--------------|-------------|------------------|-----------------|
| A: Fidelity | 300 | 95.6 | 80.8 | 84.6 | 88.5 |
| — PaperBench | 230 | 96.7 | 89.8 | 86.3 | 97.7 |
| — RE-Bench | 70 | 92.1 | 51.4 | 79.0 | 58.2 |
| B: Detail (PaperBench) | 115 | 92.6 | 67.8 | 183.0 | 178.3 |
| C: Failure (RE-Bench) | 35 | 81.4 | 15.7 | 139.3 | 58.0 |
| Overall | 450 | 93.7 | 72.4 | 114.0 | 109.1 |
