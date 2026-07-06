# Figure 4: The ARA directory structure

- **Source**: Figure 4, §2.2 (ARA Architecture); full schema in Appendix A.3
- **Caption**: "The ARA directory structure. Each file's role is annotated inline; layer badges mark the four top-level divisions. Cross-layer forensic bindings link claims in /logic to evidence in /evidence and code in /src. Full schema in Appendix A.3; design rationale in Appendix A."
- **Screenshot**: ara_figure4.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: A file-tree of the ARA package rooted at `my-research-ara/` with `PAPER.md` manifest at top, and four badged layers:
  - **Cognitive Layer** `/logic/`: problem.md, solution/ (architecture.md, algorithm.md, heuristics.md), claims.md, experiments.md, related_work.md, concepts.md
  - **Physical Layer** `/src/`: configs/, execution/ (module stubs), environment.md, prompts/
  - **Exploration Graph** `/trace/`: exploration_tree.yaml
  - **Evidence Layer** `/evidence/`: results/, logs/, tables/, figures/
- **Connections**: Inline annotations note cross-layer forensic bindings (claims in /logic → evidence in /evidence and code in /src).
- **Annotations**: Layer badges color-code the four top-level divisions; each file annotated with its role.
- **What it conveys**: The canonical four-layer file-system ontology that an agent navigates with standard tool calls; mirrored into logic/solution/architecture.md.
