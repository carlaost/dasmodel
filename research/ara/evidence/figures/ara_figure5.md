# Figure 5: Cross-layer structure of a real ARA

- **Source**: Figure 5, §2.2 (ARA Architecture)
- **Caption**: "Cross-layer structure of a real ARA. Claims in /logic link to code in /src and evidence in /evidence via forensic bindings. The Exploration Graph (bottom center) captures the research DAG with dead-end nodes (marked ×) that preserve failure modes and lessons."
- **Screenshot**: ara_figure5.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components** (four horizontal layer bands):
  - Cognitive Layer: claims.md (e.g., "C03: Method outperforms EOS"), experiments.md ("E05: Main comparison"), heuristics.md ("H02: Warmup schedule"), related_work.md ("RW: Prior work bounds")
  - Physical Layer: model.py (core algorithm implementation), train.yaml (lr: 3e-4, warmup: 1000), environment.md (PyTorch 2.1, CUDA 12.1)
  - Exploration Graph: a small DAG Question → Decision → Experiment, with a Dead-end node marked ×
  - Evidence Layer: results.csv (Method: 87.3, Baseline: 82.1), convergence.json (raw training curves)
- **Connections**: "proof" arrow claims→experiments; "code_ref / implements" arrows claims→model.py; "evidence" arrows claims→results; "refuted" arrow from a dead-end branch back to a claim; trace edges Question→Decision→Experiment.
- **Annotations**: Green ✓ on a successful experiment node, red × on dead-end node.
- **What it conveys**: Forensic cross-layer bindings make each claim traceable downstream to code/evidence and upstream to its hypothesis; the exploration DAG retains dead ends.
