# Figure 9: Three-stage ARA-native review pipeline

- **Source**: Figure 9, §5.3 (Three-Stage Review Pipeline)
- **Caption**: "Three-stage ARA-native review pipeline. Stages 1–2 invoke the ARA Seal levels of Figure 8 to resolve mechanical and rigor issues before human reviewers engage, redirecting expert attention to novelty and significance."
- **Screenshot**: ara_figure9.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components** (three gated stages, CI/CD-style):
  - **Stage 1: Conceptual Verification (Minutes)** — runs Seal Level 1 (structural) + Level 2 (Rigor Auditor); outputs a CI Report + Level 2 rigor report; advisory diagnostics.
  - **Stage 2: Empirical Verification (Hours–Days)** — runs Seal Level 3 (scaled-down directional reproduction under compute budget, evidence-layer isolated); outputs an Empirical Review Report.
  - **Stage 3: Human Review (Days–Weeks)** — reviewers receive both reports; judge significance, novelty, formulation, ethics; adjudicate contested findings; write structured typed reviews.
- **Connections**: Each stage gates the next; only Seal checks are pass/fail; diagnostics inform but do not gate.
- **What it conveys**: Mechanical/rigor verification is automated upstream so human attention is reserved for judgment.
