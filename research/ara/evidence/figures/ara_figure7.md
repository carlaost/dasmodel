# Figure 7: The ARA Compiler — four-stage top-down compilation

- **Source**: Figure 7, §4 (The ARA Compiler)
- **Caption**: "The ARA Compiler accepts any combination of research sources and guides a coding agent through four stages of top-down artifact compilation, iterating 2–3× with in-loop ARA Seal Level 1 validation until the output conforms to the protocol."
- **Screenshot**: ara_figure7.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: Left "Sources" (PDF, Code Repo, Rubrics, Trajectories) feed into a "Compiler Skill" box containing four ordered stages: (1) Semantic Deconstruction, (2) Cognitive Mapping, (3) Physical Grounding, (4) Exploration Graph Extraction. Output is the "ARA Artifact" (Cognitive / Physical / Exploration / Evidence layers).
- **Connections**: Many-to-one inputs → compiler; the four stages run top-down (each informs the next); an in-loop arrow shows generate → validate (ARA Seal Level 1) → fix iterating 2–3×.
- **Annotations**: "ARA Seal Level 1" validation gate inside the loop.
- **What it conveys**: The Compiler is a single agent skill that decompresses heterogeneous legacy sources into a schema-conformant ARA via iterative Level-1-gated top-down generation.
