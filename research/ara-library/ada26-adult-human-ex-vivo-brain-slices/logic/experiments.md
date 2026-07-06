# Experiments

> Grounding: abstract-only + verified analysis repository. These are **directional** verification
> plans reconstructed from the abstract and the released analysis scripts. NO exact numerical
> results appear here (none are available without the full text; any filable numbers would go to
> `evidence/`). Precise wet-lab protocols (slicing thickness, culture medium, dosing, timepoints)
> are Not available from provided input (no full text).

## E01: Establish and characterize the organotypic slice platform
- **Verifies**: C01
- **Setup**:
  - Model system: Adult human brain slices from neurosurgical resections (tumor-adjacent tissue)
  - Assay: single-nucleus RNA-seq of cultured slices; cell-type annotation via canonical markers
  - Cell types: astrocytes, endothelial, excitatory neurons, inhibitory neurons, microglia,
    oligodendrocytes, OPCs, perivascular cells (8 marker sets in `Molecular_markers`)
  - Culture window: "weeks" (exact duration not available from input)
- **Procedure**:
  1. Prepare organotypic slices from resection tissue and maintain in culture.
  2. Profile by snRNA-seq; cluster and annotate cell types with canonical marker genes.
  3. Quantify cell-type proportions per sample; visualize on UMAP and marker dotplots.
  4. Assess whether mature cell identities and tissue composition are retained over the window.
- **Metrics**: Presence/abundance of each mature cell type; marker-gene specificity; stability of
  proportions across samples/time.
- **Expected outcome**:
  - Cultured slices retain the full mature CNS cell-type repertoire with canonical marker
    expression, supporting preserved architecture and identity.
- **Baselines**: Freshly resected (uncultured) tissue and/or postmortem reference (comparison
  design not fully specified in input).
- **Dependencies**: none

## E02: Define stimulus-specific gene programs across stressors (bulk RNA-seq + WGCNA)
- **Verifies**: C02, C05
- **Setup**:
  - Assay: bulk RNA-seq of slices under five conditions — Control, BLM, H₂O₂, LPS, TNFα
  - Analysis: LDA on treatment; WGCNA modules (Prog.1–Prog.5); module–trait correlation; pathway
    over-representation per program
- **Procedure**:
  1. Sequence bulk RNA from slices across the five treatment arms.
  2. Run LDA to test treatment separability in low-dimensional space.
  3. Run WGCNA; correlate each program's activity with each treatment; mark significance.
  4. Functionally annotate programs by pathway enrichment.
- **Metrics**: Treatment separability (LDA); program–treatment correlation and significance;
  enriched pathways per program.
- **Expected outcome**:
  - Treatments separate in transcriptional space and programs show treatment-specific correlation,
    with distinct pathway signatures (e.g. NF-κB / TNF signaling for the inflammatory programs).
- **Baselines**: Control (untreated) slices.
- **Dependencies**: E01

## E03: Resolve the cell-type-specific TNFα response (snRNA-seq DE)
- **Verifies**: C03
- **Setup**:
  - Assay: snRNA-seq of TNFα-treated vs control slices
  - Analysis: per-cell-type differential expression for microglia, astrocytes, OPCs; volcano and
    pathway enrichment; shared TNF-response gene heatmap across cell types
- **Procedure**:
  1. Split TNFα vs control nuclei by annotated cell type.
  2. Compute DE (avg_log2FC, adjusted p) within each glial type.
  3. Identify shared vs cell-type-specific responses; enrich pathways.
- **Metrics**: Per-cell-type up/down-regulated gene sets; enriched pathways; overlap of shared
  response genes.
- **Expected outcome**:
  - Each glial type mounts a TNFα response with both shared inflammatory genes and cell-type-
    specific components.
- **Baselines**: Control slices.
- **Dependencies**: E01

## E04: Validate slice-derived TNFα signatures in postmortem and external datasets
- **Verifies**: C04
- **Setup**:
  - Reference datasets: postmortem human brain; external datasets — mouse microglia, human
    iPSC-derived astrocytes, COVID-19 postmortem brains, large AD snRNA-seq cohorts (per repo)
  - Analysis: signature concordance / enrichment of slice-derived TNFα signatures in each dataset
- **Procedure**:
  1. Derive per-cell-type TNFα signatures from the slice snRNA-seq (E03).
  2. Test their expression/enrichment in postmortem human brain and each external dataset.
- **Metrics**: Signature concordance / enrichment statistics across datasets.
- **Expected outcome**:
  - Slice-derived TNFα signatures are recapitulated in postmortem human brain and reproduced across
    the external datasets.
- **Baselines**: Matched control/non-inflamed conditions within each external dataset.
- **Dependencies**: E03

## E05: Test stimulus-specificity by cross-stressor comparison
- **Verifies**: C02
- **Setup**:
  - Assay: the same bulk RNA-seq panel across Control, BLM, H₂O₂, LPS, TNFα
  - Analysis: compare program activation and DE across stressors to establish specificity vs shared
    stress response
- **Procedure**:
  1. Contrast each stressor's program/DE profile against the others.
  2. Separate stimulus-specific programs from a shared stress response.
- **Metrics**: Between-stressor divergence of program activity; specificity of top pathways.
- **Expected outcome**:
  - Distinct stressors activate partially distinct programs, demonstrating stimulus specificity
    beyond a generic stress response.
- **Baselines**: Control slices.
- **Dependencies**: E02

## E06: Infer coordinated glial crosstalk via cell-cell communication (MultiNicheNet)
- **Verifies**: C03, C06
- **Setup**:
  - Assay: snRNA-seq of TNFα-treated vs control slices
  - Analysis: MultiNicheNet ligand–receptor inference and prioritization comparing conditions
- **Procedure**:
  1. Build sender→receiver signaling networks among glial (and other) cell types for each condition.
  2. Prioritize ligand–receptor interactions that change with TNFα.
  3. Interpret prioritized edges as pro-/anti-inflammatory loops among microglia, astrocytes, OPCs.
- **Metrics**: Prioritization score / differential activity of ligand–receptor pairs between TNFα
  and control.
- **Expected outcome**:
  - TNFα reshapes intercellular signaling, prioritizing ligand–receptor interactions that link the
    glial cell types into coordinated pro-/anti-inflammatory loops.
- **Baselines**: Control slices.
- **Dependencies**: E03
