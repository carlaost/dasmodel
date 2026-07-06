# Experiments (Analysis Plans)

> Grounding: abstract-only. These are directional analysis plans reconstructed from the analyses explicitly named in the abstract. Exact values, protocols, software, and statistical thresholds are not available from provided input, and no exact numerical results are included here.

## E01: Generate and characterize the Stereo-seq PFC atlas
- **Verifies**: C01
- **Setup**:
  - Method: Stereo-seq spatial transcriptomics
  - Tissue: Human prefrontal cortex
  - Cohorts: Male AD cases at varying neuropathological stages and age-matched male controls
  - System: Not available from provided input
- **Procedure**:
  1. Generate a subcellular-resolution spatial transcriptome atlas from human PFC samples.
  2. Organize atlas data by disease/control status and neuropathological stage.
  3. Characterize the atlas sufficiently to support downstream spatial analyses.
- **Metrics**: Atlas coverage, spatial resolution, sample inclusion, and quality-control measures; exact metrics not available from provided input.
- **Expected outcome**:
  - The atlas supports spatial transcriptomic comparison between AD cases and controls.
- **Baselines**: Age-matched male controls
- **Dependencies**: none

## E02: Analyze AD-associated transcriptional and laminar changes across PFC layers
- **Verifies**: C02
- **Setup**:
  - Data: Stereo-seq PFC atlas
  - Groups: AD cases versus age-matched controls
  - Stratification: PFC layers
  - System: Not available from provided input
- **Procedure**:
  1. Assign spatial transcriptomic observations to PFC layers.
  2. Compare transcriptional profiles across layers between AD and controls.
  3. Assess laminar structure for AD-associated disruption.
- **Metrics**: Differential transcriptional alteration and laminar-structure disruption measures; exact metrics not available from provided input.
- **Expected outcome**:
  - AD cases show layer-associated transcriptional alterations and laminar disruption relative to controls.
- **Baselines**: Age-matched male controls
- **Dependencies**: E01

## E03: Infer AD-related layer-to-layer, cell-cell, and stress-response interactions
- **Verifies**: C02, C03
- **Setup**:
  - Data: Stereo-seq PFC atlas with layer and cell-context annotations
  - Focus: Stressed neurons, nearby glial cells, amyloid-beta-clearance-promoting stress-response interactions
  - System: Not available from provided input
- **Procedure**:
  1. Infer layer-to-layer and cell-cell interactions from the spatial transcriptomic atlas.
  2. Identify genes upregulated in stressed neurons and nearby glial cells.
  3. Compare stress-response interactions between AD and controls.
- **Metrics**: Interaction-shift measures, stress-response interaction strength, and gene upregulation evidence; exact metrics not available from provided input.
- **Expected outcome**:
  - AD is associated with shifts in interactions and diminished stress-response interactions that promote amyloid-beta clearance.
- **Baselines**: Age-matched male controls
- **Dependencies**: E01, E02

## E04: Identify AD-progression-linked neuronal co-expression modules and ZNF460 regulation
- **Verifies**: C04
- **Setup**:
  - Data: Cell-type-specific expression profiles from the Stereo-seq PFC atlas
  - Focus: Neuronal co-expression modules and transcription-factor regulation
  - System: Not available from provided input
- **Procedure**:
  1. Perform cell-type-specific co-expression analysis.
  2. Identify neuronal modules linked to neuroprotection, protein dephosphorylation, and amyloid-beta regulation.
  3. Assess module regulation and identify transcription factors associated with module control.
  4. Compare module expression across AD progression.
- **Metrics**: Module-expression trends and transcription-factor regulatory evidence; exact metrics not available from provided input.
- **Expected outcome**:
  - Neuronal modules are downregulated as AD progresses, and ZNF460 is implicated as a regulator.
- **Baselines**: Less advanced AD stages and/or controls; exact baseline structure not available from provided input.
- **Dependencies**: E01
