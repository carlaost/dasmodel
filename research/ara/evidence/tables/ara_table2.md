# Table 2: Benchmark characteristics (PaperBench vs RE-Bench)

**Source**: Table 2, §7.1 (Datasets and Motivation)
**Caption**: "Benchmark characteristics. PaperBench supplies configuration depth via expert rubrics; RE-Bench supplies trajectory depth via MALT failure traces. These are the two source-side enrichments ARA is built to exploit."
**Screenshot**: ara_table2.png
**Extraction type**: raw_table

| Attribute | PaperBench (Starace et al., 2025) | RE-Bench (Wijk et al., 2025) |
|-----------|-----------------------------------|------------------------------|
| Papers / Tasks | 23 peer-reviewed ML papers across diverse subfields | 7 R&D hill-climbing tasks on well-defined objective functions |
| Scale | 8,921 expert-authored rubric requirements | 24,008 agent runs; 46,303 failure episodes |
| Contents | PDF + companion GitHub repo (15/23 papers); expert rubrics encode hyperparameter values, implementation tricks, and configurations absent from the paper; failure knowledge rarely preserved in published papers | Starter codebase per task; METR MALT transcripts with full real agent successful and failure trajectories retained per run |
| Scoring | Expert hierarchical rubric (yes / partial / no) | Automated continuous objective; no human judgment required |
| Used in | Understanding (§7.2, Cat. A & B); Reproduction (§7.3) | Understanding (§7.2, Cat. C); Extension (§7.4) |
