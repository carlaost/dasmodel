# Table 6: Taxonomy of reproduction-critical information in PaperBench rubrics

**Source**: Table 6, Appendix A.1 (Taxonomy of reproduction-critical information)
**Caption**: "Taxonomy of reproduction-critical information in PaperBench rubrics. Frequency is computed across 3,050 leaf requirements from five papers. The 'PDF Difficulty' column characterizes the primary challenge of extracting this information from a narrative PDF. The 'ARA Layer' column identifies which ARA component directly addresses each category."
**Screenshot**: ara_table6.png
**Extraction type**: raw_table

| Category | % | PDF Difficulty | ARA Layer |
|----------|---|----------------|-----------|
| Combinatorial experiment matrix | 24.1 | Implicit in prose | experiments.md |
| Evaluation protocol | 18.5 | Scattered across §, appendix | experiments.md |
| Hyperparameters | 17.2 | Buried in appendix tables | configs/training.md |
| Metric logging | 10.4 | Rarely specified | experiments.md |
| Result interpretation | 8.6 | Mixed with discussion | claims.md, evidence/ |
| Architecture specification | 5.8 | Split across text, figures, appendix | architecture.md |
| Mathematical formulation | 4.5 | Equation references break across sections | algorithm.md |
| Implementation tricks | 4.2 | Footnotes, appendix asides | heuristics.md |
| Data pipeline | 3.8 | Preprocessing details omitted | configs/, environment.md |
| Environment / infrastructure | 2.9 | Assumed known | environment.md |
