# Related Work & Typed Dependencies

> Grounding: abstract-only. The paper's full References list is **not available from provided input
> (no full text)**, so per-citation technical deltas cannot be reconstructed. The typed dependencies
> below are the ones grounded in the abstract + the verified analysis repository: the external
> validation datasets the authors reuse and the methods/tools they build on. Precise citations
> (authors, years, DOIs) for these are Not available from provided input; identifiers are given
> where the repo/README names them.

## Methodological dependencies (tools the analysis builds on)

### RW01: WGCNA — Weighted Gene Co-expression Network Analysis
- **DOI**: Not available from provided input (standard: Langfelder & Horvath, 2008, BMC Bioinformatics, 10.1186/1471-2105-9-559)
- **Type**: imports
- **Delta**:
  - What changed: Applied to bulk RNA-seq across five slice-culture stressors to define shared and
    stimulus-specific gene programs (Prog.1–Prog.5).
  - Why: To reduce the bulk response to interpretable, treatment-associated programs.
- **Claims affected**: C02, C05
- **Adopted elements**: Module detection + module-trait correlation framework.

### RW02: MultiNicheNet — differential cell-cell communication inference
- **DOI**: Not available from provided input (tool: Browaeys et al., MultiNicheNet)
- **Type**: imports
- **Delta**:
  - What changed: Applied to snRNA-seq to compare TNFα-treated vs control slices and prioritize
    ligand–receptor interactions linking glial cell types.
  - Why: To move from per-cell-type DE to coordinated multicellular crosstalk (pro-/anti-
    inflammatory loops).
- **Claims affected**: C03, C06
- **Adopted elements**: Ligand–receptor prioritization across conditions.

### RW03: Seurat — single-cell/-nucleus RNA-seq analysis toolkit
- **DOI**: Not available from provided input (standard: Seurat, Satija/Hao et al.)
- **Type**: imports
- **Delta**:
  - What changed: Used for snRNA-seq clustering, cell-type annotation, UMAP, marker dotplots,
    average expression, and DE visualization (`DimPlot`, `DotPlot`, `AverageExpression`).
  - Why: Standard pipeline for nucleus-resolved profiling of the cultured slices.
- **Claims affected**: C01, C03
- **Adopted elements**: Object model + plotting/DE utilities.

## External validation datasets (reused public data — typed as `bounds`/validation)

### RW04: Mouse microglia dataset
- **DOI**: Not available from provided input
- **Type**: bounds (cross-species validation)
- **Delta**:
  - What changed: Used to test whether slice-derived microglial TNFα signatures generalize to mouse
    microglia.
  - Why: Cross-species reproducibility of the microglial response.
- **Claims affected**: C04
- **Adopted elements**: External expression data for signature enrichment.

### RW05: Human iPSC-derived astrocytes dataset
- **DOI**: Not available from provided input
- **Type**: bounds (orthogonal-model validation)
- **Delta**:
  - What changed: Used to validate slice-derived astrocyte TNFα signatures in an independent human
    in-vitro astrocyte model.
  - Why: Reproducibility across human astrocyte model systems.
- **Claims affected**: C04
- **Adopted elements**: External astrocyte expression data.

### RW06: COVID-19 postmortem human brain dataset
- **DOI**: Not available from provided input
- **Type**: bounds (in-vivo human validation)
- **Delta**:
  - What changed: Used to test the TNFα/inflammatory glial signature in a neuroinflammatory human
    postmortem context.
  - Why: Disease-relevant human in-vivo validation.
- **Claims affected**: C04
- **Adopted elements**: Postmortem snRNA-seq/transcriptomic data.

### RW07: Large Alzheimer's disease (AD) snRNA-seq cohorts
- **DOI**: Not available from provided input
- **Type**: bounds (disease-cohort validation)
- **Delta**:
  - What changed: Used to test whether slice-derived glial TNFα signatures appear in AD human brain.
  - Why: Relevance of the ex-vivo response to a chronic neurodegenerative/neuroinflammatory disease.
- **Claims affected**: C04
- **Adopted elements**: Large-cohort snRNA-seq reference data.

## Broader citation footprint
- The paper's full reference list (background on glial biology, aging/disease, prior slice-culture
  and neuroinflammation literature, and the primary citations for each tool and external dataset
  above) is **not available from provided input (no full text)** and could not be enumerated
  without the PDF. This is a coverage gap imposed by the abstract-only grounding, not an omission of
  available content.
