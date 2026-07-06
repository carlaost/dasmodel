# Claims

> Grounding: abstract/metadata only. Every load-bearing number in a claim statement is copied verbatim from `metadata.md` and bound to a `Sources` entry. No full-text tables, figures, sample sizes, statistical tests, or effect sizes were available.

## C01: The model is a vascularized neuroimmune hPSC organoid containing AD-relevant human cell types
- **Statement**: The paper reports a complex human pluripotent stem cell-based vascularized neuroimmune organoid model containing human neurons, microglia, astrocytes, and blood vessels.
- **Status**: supported
- **Falsification criteria**: Full-text methods or independent replication showing that the model lacks one or more of the reported cell-type components, or that the reported components are not human hPSC-derived where claimed.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly states that the authors developed this organoid model and lists its cell-type components.
- **Interpretation**: The model is positioned as a multicellular human platform for AD modeling; the abstract does not provide construction protocols, marker panels, validation statistics, or vascularization criteria.
- **Sources**:
  - model composition ← `metadata.md` Abstract «we developed a complex human pluripotent stem cell (hPSC)-based vascularized neuroimmune organoid model, which contains multiple cell types affected in human AD brains, including human neurons, microglia, astrocytes, and blood vessels» [result]
- **Dependencies**: none
- **Tags**: hPSC, vascularized-organoid, neuroimmune, model-system

## C02: Sporadic AD brain extracts induce multiple AD-like pathologies in the organoids after four weeks
- **Statement**: The paper reports that brain extracts from individuals with sporadic AD induce multiple AD pathologies in organoids four weeks post-exposure, including amyloid beta (Aβ) plaque-like aggregates, tau tangle-like aggregates, neuroinflammation, elevated microglial synaptic pruning, synapse/neuronal loss, impaired neural network activity, and disrupted AD-related proteomic pathways.
- **Status**: supported
- **Falsification criteria**: Full-text data or independent replication showing that sporadic AD brain extracts do not induce the listed pathology classes under the reported exposure conditions, or that the observed effects are indistinguishable from appropriate control extracts.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly reports multiple pathology classes after exposure and reports disrupted AD-related pathways by proteomics.
- **Interpretation**: The result supports use of patient-brain-extract exposure as an abstract-level disease induction paradigm for sAD-like pathology, but exact assays, controls, sample sizes, and effect sizes are not available from provided input.
- **Sources**:
  - four weeks post-exposure and pathology list ← `metadata.md` Abstract «brain extracts from individuals with sAD can effectively induce multiple AD pathologies in organoids four weeks post-exposure, including amyloid beta (Aβ) plaque-like aggregates, tau tangle-like aggregates, neuroinflammation, elevated microglial synaptic pruning, synapse/neuronal loss, and impaired neural network activity» [result]
  - proteomic pathway disruption ← `metadata.md` Abstract «Proteomics analysis also revealed disrupted AD-related pathways in our vascularized AD neuroimmune organoids.» [result]
- **Dependencies**: C01
- **Tags**: sporadic-AD, brain-extracts, Aβ, tau, neuroinflammation, proteomics

## C03: Lecanemab reduces amyloid burden while elevating vascular inflammation response in exposed organoids
- **Statement**: The paper reports that Lecanemab treatment of AD brain-extract-exposed organoids produces a significant reduction of amyloid burden along with an elevated vascular inflammation response.
- **Status**: supported
- **Falsification criteria**: Full-text data or independent replication showing no amyloid-burden reduction after Lecanemab treatment in this model, or no associated elevation in vascular inflammation response under comparable conditions.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly states the Lecanemab treatment outcome and identifies the drug as targeting Aβ.
- **Interpretation**: The result suggests the model can report both intended amyloid-directed pharmacodynamic effects and vascular inflammatory responses relevant to immunotherapy evaluation. The abstract does not provide dose, timing, statistical test, or magnitude of either effect.
- **Sources**:
  - Lecanemab response ← `metadata.md` Abstract «after treatment with Lecanemab, an FDA-approved antibody drug targeting Aβ, AD brain extracts exposed organoids showed a significant reduction of amyloid burden, along with an elevated vascular inflammation response» [result]
- **Dependencies**: C01, C02
- **Tags**: Lecanemab, immunotherapy, amyloid-burden, vascular-inflammation
