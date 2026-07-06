# Claims

> Grounding: abstract-only. Claims below use only statements present in `metadata.json` and `metadata.md`. No full text, tables, figures, or supplementary evidence were provided. Exact numerical claims are limited to numbers explicitly present in the abstract.

## C01: The study generated a subcellular-resolution Stereo-seq atlas of human PFC in AD and aging controls
- **Statement**: The study presents a subcellular-resolution spatial transcriptome atlas of the human prefrontal cortex generated with Stereo-seq from six male AD cases at varying neuropathological stages and six age-matched male controls.
- **Status**: supported
- **Falsification criteria**: The claim would be falsified if the paper did not use Stereo-seq, did not analyze human PFC, or did not include the stated six male AD cases and six age-matched male controls.
- **Proof**: [E01]
- **Evidence basis**: The abstract states the atlas type, anatomical region, method, and case/control sample counts.
- **Interpretation**: The atlas is positioned as a spatial transcriptomic resource for studying molecular mechanisms of AD in the PFC.
- **Sources**:
  - six male AD cases and six age-matched male controls ← metadata.md (Abstract) «generated with Stereo-seq from six male AD cases at varying neuropathological stages and six age-matched male controls» [result]
- **Dependencies**: none
- **Tags**: Stereo-seq, spatial-transcriptomics, prefrontal-cortex, atlas

## C02: AD is associated with transcriptional, laminar, and interaction changes across PFC layers
- **Statement**: The abstract reports distinct transcriptional alterations across PFC layers, disruptions in laminar structure, and AD-related shifts in layer-to-layer and cell-cell interactions.
- **Status**: supported
- **Falsification criteria**: The claim would be falsified if layer-wise transcriptomic analysis, laminar-structure analysis, or interaction analysis failed to show AD-associated differences.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly states these three analysis outcomes.
- **Interpretation**: The study frames AD in the PFC as a spatially organized molecular and cellular-network disruption, not only a global expression difference.
- **Sources**:
  - no load-bearing number in statement; qualitative result ← metadata.md (Abstract) «Our analyses revealed distinct transcriptional alterations across PFC layers, highlighted disruptions in laminar structure, and exposed AD-related shifts in layer-to-layer and cell-cell interactions.» [result]
- **Dependencies**: C01
- **Tags**: laminar-structure, cortical-layers, cell-cell-interactions, AD

## C03: AD diminishes stress-response interactions linked to amyloid-beta clearance
- **Statement**: The abstract reports highly upregulated genes in stressed neurons and nearby glial cells, and states that AD diminished stress-response interactions that promote amyloid-beta clearance.
- **Status**: supported
- **Falsification criteria**: The claim would be falsified if stressed neurons and nearby glia did not show the reported upregulated genes, or if the stress-response interaction analysis did not indicate diminished amyloid-beta-clearance-promoting interactions in AD.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly links stressed neurons, nearby glial cells, AD-diminished stress-response interactions, and amyloid-beta clearance.
- **Interpretation**: The result suggests that local neuron-glia stress-response circuits may be impaired in AD, but the abstract does not provide mechanistic validation details.
- **Sources**:
  - no load-bearing number in statement; qualitative result ← metadata.md (Abstract) «we identified genes highly upregulated in stressed neurons and nearby glial cells, where AD diminished stress-response interactions that promote Aβ clearance» [result]
- **Dependencies**: C01, C02
- **Tags**: stressed-neurons, glia, amyloid-beta-clearance, interaction-analysis

## C04: Three neuronal co-expression modules are downregulated with AD progression and are regulated by ZNF460
- **Statement**: Cell-type-specific co-expression analysis highlighted three neuronal modules linked to neuroprotection, protein dephosphorylation, and amyloid-beta regulation; all three modules were downregulated as AD progresses, and ZNF460 was identified as a transcription factor regulating these modules.
- **Status**: supported
- **Falsification criteria**: The claim would be falsified if the co-expression analysis did not identify three neuronal modules with the stated functional links, if the modules were not downregulated with AD progression, or if ZNF460 was not implicated as a regulator.
- **Proof**: [E04]
- **Evidence basis**: The abstract states the number of modules, functional associations, direction across AD progression, and ZNF460 regulatory interpretation.
- **Interpretation**: ZNF460 is presented as a potential therapeutic target, but the abstract does not provide validation experiments or effect sizes.
- **Sources**:
  - three neuronal modules ← metadata.md (Abstract) «cell-type-specific co-expression analysis highlighted three neuronal modules linked to neuroprotection, protein dephosphorylation, and Aβ regulation, with all modules downregulated as AD progresses» [result]
  - ZNF460 ← metadata.md (Abstract) «We identified ZNF460 as a transcription factor regulating these modules, offering a potential therapeutic target.» [result]
- **Dependencies**: C01
- **Tags**: co-expression, neuronal-modules, ZNF460, therapeutic-target
