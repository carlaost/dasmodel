# Figure 8: The ARA Seal — three-level verification credential (+ human stage)

- **Source**: Figure 8, §5.2 (The ARA Seal); implementation in Appendix H.1
- **Caption**: "The ARA Seal is a three-level verification credential. Each level tests a progressively stronger property of the artifact, escalating in cost and breadth: structural integrity (seconds, deterministic), argumentative rigor (minutes, rubric-anchored agent), and execution reproducibility (hours to days, sandboxed coding agent). Passing the applicable levels issues a Seal Certificate that downstream agents check before investing compute."
- **Screenshot**: ara_figure8.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: Four escalating cards, each with VERIFIES/JUDGES items, a RUNTIME cost, and an issued certificate:
  - **Level 1 — Structural Integrity** — VERIFIES: schema conformance; cross-layer references resolve; mandatory files & fields present; minimum node counts. RUNTIME: seconds, fully deterministic. → **L1 Certificate** (Artifact ID + schema hash).
  - **Level 2 — Argumentative Rigor** — VERIFIES: evidence relevance (claim ↔ experiment); falsifiability quality; methodological rigor; scope coherence, exploration integrity. RUNTIME: minutes, rubric-anchored 1–5 scoring. → **L2 Certificate** (rubric scores + audit report).
  - **Level 3 — Execution Reproducibility** — VERIFIES: central claims reproduce empirically; directional checks on top-ranked claims; code kernel actually runs. RUNTIME: hours–days, scaled-down, budget-bounded. → **L3 Certificate** (per-claim outcomes + env hash).
  - **Level 4 — Human Review** (JUDGES, not a Seal level): significance & novelty; problem framing; ethical implications; adjudicates disputed findings. RUNTIME: days–weeks, domain expert review. → **L4 Certificate** (review decision + expert sign-off).
- **Connections**: Cards chained left→right with "passes" gates; each level must pass before the next is attempted.
- **What it conveys**: The Seal is a gated credential separating cheap deterministic checks from expensive reproduction, reserving human judgment for the final stage. (Note: text calls L1–L3 the three Seal levels; L4 in the figure is the human-judgment stage of the review pipeline.)
