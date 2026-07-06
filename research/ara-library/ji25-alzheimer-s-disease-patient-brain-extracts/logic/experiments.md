# Experiments (Abstract-Level Verification Plans)

> Grounding: abstract/metadata only. These are directional reconstructions of the analyses reported in the abstract. Exact numerical results are intentionally omitted here and appear only in claims/problem where the abstract directly supports them.

## E01: Build and characterize the vascularized neuroimmune organoid model
- **Verifies**: C01
- **Setup**:
  - Model system: human pluripotent stem cell-based vascularized neuroimmune organoids.
  - Intended cellular components: human neurons, microglia, astrocytes, and blood vessels.
  - Protocol details: Not available from provided input.
- **Procedure**:
  1. Generate the hPSC-based organoid model.
  2. Assess whether the organoids contain the reported neuronal, immune, astrocytic, and vascular components.
  3. Establish the model as the platform for subsequent disease-induction and drug-treatment tests.
- **Metrics**: Presence and characterization of the reported cell-type components; exact marker panels and quantification methods are not available from provided input.
- **Expected outcome**:
  - The organoids contain the reported human cell types relevant to AD brains.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Expose organoids to sporadic AD patient brain extracts and assess AD-like pathology
- **Verifies**: C02
- **Setup**:
  - Model system: vascularized neuroimmune organoids from E01.
  - Perturbation: brain extracts from individuals with sporadic AD.
  - Controls: Not available from provided input.
- **Procedure**:
  1. Expose organoids to sAD patient brain extracts.
  2. Assess protein-aggregate, inflammatory, synaptic, neuronal, network-activity, and proteomic pathway readouts.
  3. Compare exposed organoids against appropriate controls if available in the full paper.
- **Metrics**: Presence or increase of AD-like pathology classes; proteomic pathway disruption; exact assay definitions and effect sizes are not available from provided input.
- **Expected outcome**:
  - Exposed organoids show multiple AD-like pathology classes and disrupted AD-related pathways.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E03: Treat AD brain-extract-exposed organoids with Lecanemab
- **Verifies**: C03
- **Setup**:
  - Model system: AD brain-extract-exposed vascularized neuroimmune organoids.
  - Treatment: Lecanemab, described in the abstract as an FDA-approved antibody drug targeting Aβ.
  - Dose and timing: Not available from provided input.
- **Procedure**:
  1. Treat exposed organoids with Lecanemab.
  2. Measure amyloid burden after treatment.
  3. Measure vascular inflammation response after treatment.
  4. Compare against untreated or vehicle-treated exposed organoids if available in the full paper.
- **Metrics**: Direction of amyloid-burden change and vascular inflammation response; exact assays, statistics, and magnitudes are not available from provided input.
- **Expected outcome**:
  - Treatment reduces amyloid burden while increasing vascular inflammation response.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E02
