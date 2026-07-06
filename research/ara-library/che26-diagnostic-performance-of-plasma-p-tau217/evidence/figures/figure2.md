# Figure 2 - Evidence network for comparative diagnostic accuracy
- **Source**: Figure 2, Section 3.2 / 3.4, page 5
- **Caption**: "Evidence network for comparative diagnostic accuracy. (A) Network plot for Amyloid-β positivity detection; (B) Network plot for Tau-PET positivity recognition. The size of the nodes is proportional to the total number of participants, and the thickness of the edges represents the number of direct head-to-head comparisons."
- **Screenshot**: figure2.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Panel A — Amyloid-β positivity detection network (8 nodes)**:
  - Nodes: p217_ALZpath, p217_IA, p181_IA, p217_Lilly, p231_UGOT, p217_Lumi, p217_Ratio, p217_MS.
  - Edges: many direct head-to-head connections; edge labels show integer comparison counts (values such as 1 and 2 are printed on edges). p181_IA and p217_MS are hub nodes with the most connections; node sizes vary with participant totals.
  - p181_IA is the reference comparator around which the network is anchored.
- **Panel B — Tau-PET positivity recognition network (6 nodes)**:
  - Nodes: p217_IA, p181_IA, p217_Lilly, p217_Ratio, p217_Lumi, p217_MS.
  - Edges: sparser than panel A, most edge labels = 1 (single head-to-head comparison per link).
- **Connections**: undirected edges = existence of direct comparisons; thickness ∝ number of comparisons.
- **Annotations**: node size ∝ total participants; edge thickness/labels ∝ number of direct head-to-head comparisons.
- **What it conveys**: the two outcome networks are connected (enabling combined direct + indirect NMA evidence); the Abeta network is denser (8 nodes) than the Tau-PET network (6 nodes), reflecting more available comparisons for amyloid detection. Structure mirrored in `logic/solution/study_design.md` (network geometry).

**Note**: This is a network-geometry diagram, not a quantitative plot — no per-node numeric values are
read here. Node rankings/effect sizes are in `evidence/tables/table2.md` and `evidence/figures/figure3.md`.
