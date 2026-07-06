# Concepts

> Grounding: abstract-only + verified analysis repository. Definitions are standard field
> definitions anchored to how the paper/repo uses each term; paper-specific parameterizations that
> would need the full text are marked as such.

## Adult human organotypic brain slice culture
- **Notation**: —
- **Definition**: An ex vivo culture in which a thin slice of living adult human brain tissue —
  obtained from neurosurgical resection — is maintained so that its native three-dimensional tissue
  architecture and multiple resident cell types remain intact ("organotypic"), enabling controlled
  perturbation and readout while approximating the in-tissue context.
- **Boundary conditions**: Tissue is resection-derived (here, tumor-adjacent; see constraints.md);
  fidelity is asserted "over weeks" — exact viable window Not available from provided input.
- **Related concepts**: Ex vivo platform, glial cells, mature cell identity.

## Glial cells (microglia, astrocytes, OPCs, oligodendrocytes)
- **Notation**: —
- **Definition**: Non-neuronal CNS cells that modulate brain function. The study focuses on the
  glial compartment — microglia (immune sentinels), astrocytes (homeostatic/metabolic support),
  oligodendrocyte precursor cells (OPCs), and oligodendrocytes — as the responders to stress and
  the participants in multicellular crosstalk.
- **Boundary conditions**: The coordinated TNFα response is analysed specifically for microglia,
  astrocytes, and OPCs.
- **Related concepts**: Multicellular communication, TNFα response, cell-type-specific DE.

## Stimulus-specific transcriptional program
- **Notation**: Prog.1 … Prog.5 (WGCNA programs)
- **Definition**: A coordinated set of co-expressed genes whose activation pattern is characteristic
  of a particular stressor, distinguishing one perturbation's response from another's. Here derived
  by WGCNA over bulk RNA-seq across Control, BLM, H₂O₂, LPS, and TNFα.
- **Boundary conditions**: Defined across the five-treatment panel; program count shown in released
  code is five.
- **Related concepts**: WGCNA, LDA, pathway enrichment.

## WGCNA (Weighted Gene Co-expression Network Analysis)
- **Notation**: —
- **Definition**: An unsupervised method that groups genes into modules ("programs") by co-expression
  similarity, then relates module eigengene activity to sample traits (here, treatment condition)
  via correlation and significance testing, and annotates modules by pathway enrichment.
- **Boundary conditions**: Applied to bulk RNA-seq; module-trait correlations are visualized as a
  Prog×Treatment heatmap with significance stars (p<0.05 *, <0.01 **, <0.001 ***).
- **Related concepts**: Stimulus-specific program, pathway enrichment, gene-module membership.

## TNFα (Tumor Necrosis Factor alpha) stimulation
- **Notation**: TNF / TNFα
- **Definition**: A pro-inflammatory cytokine used as the primary defined stressor applied to the
  slice cultures to elicit and dissect a coordinated glial inflammatory response.
- **Boundary conditions**: One of five treatment arms; the focus of the snRNA-seq DE, external
  validation, and cell-cell communication analyses.
- **Related concepts**: Pro-/anti-inflammatory loop, NF-κB signaling, glial cells.

## Cell-type-specific differential expression (snRNA-seq)
- **Notation**: TNF vs Control DE, `avg_log2FC`, `p_val_adj`
- **Definition**: Identification, within each nucleus-resolved cell type, of genes changing between
  TNFα-treated and control slices — thresholded (in released code) at adjusted p < 0.05 and
  |log2FC| relative to 0.2 for volcano classification — to define per-cell-type response signatures.
- **Boundary conditions**: Computed for microglia, astrocytes, and OPCs (glial focus); thresholds
  are those in the plotting script, not necessarily the primary statistical model.
- **Related concepts**: snRNA-seq, glial cells, pathway enrichment.

## MultiNicheNet cell-cell communication analysis
- **Notation**: —
- **Definition**: A computational framework that infers and prioritizes ligand–receptor–mediated
  intercellular signaling between cell types across conditions; used here to compare TNFα-treated vs
  control slices and prioritize the ligand–receptor interactions linking the glial cell types.
- **Boundary conditions**: Comparison is TNFα vs control; outputs are in Supplementary Table 5.
- **Related concepts**: Pro-/anti-inflammatory loop, ligand-receptor interaction, glial crosstalk.

## Pro-/anti-inflammatory loop (multicellular crosstalk)
- **Notation**: —
- **Definition**: Reciprocal signaling circuits among microglia, astrocytes, and OPCs in which some
  interactions amplify (pro-inflammatory) and others restrain (anti-inflammatory) the TNFα response,
  constituting the "coordinated" multicellular behavior the platform resolves.
- **Boundary conditions**: Asserted in the abstract as the interpretation of the TNFα response;
  the constituent edges rest on the MultiNicheNet analysis (C06). Full mechanistic detail Not
  available from provided input.
- **Related concepts**: MultiNicheNet, glial cells, TNFα stimulation.
