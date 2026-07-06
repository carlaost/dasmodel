# Experiments (Analysis Plans)

> Grounding: abstract-only and directional only. These are reconstructed analysis plans from the abstract. Exact sample sizes, effect sizes, platforms, statistical thresholds, and brain-region lists are not available from provided input.

## E01: Spatial transcriptomic comparison of actively immunized AD, nonimmunized AD, and healthy control brains
- **Verifies**: C01
- **Setup**:
  - Design: Comparative human brain spatial transcriptomics study.
  - Groups: Actively immunized patients with AD; nonimmunized patients with AD; neurologically healthy controls.
  - Tissue: AD brain and control brain; exact regions not available from provided input.
  - Platform: Spatial transcriptomics; exact platform not available from provided input.
- **Procedure**:
  1. Profile brain tissue from the three comparison groups using spatial transcriptomics.
  2. Identify microglial transcriptional states.
  3. Associate microglial states with Aβ clearance.
- **Metrics**: Microglial-state identity, spatial localization, and association with Aβ clearance; exact quantitative metrics not available from provided input.
- **Expected outcome**:
  - Distinct microglial states are associated with Aβ clearance.
- **Baselines**: Nonimmunized AD and neurologically healthy controls.
- **Dependencies**: none

## E02: High-resolution spatial transcriptomics with single-cell RNA sequencing after lecanemab treatment
- **Verifies**: C02
- **Setup**:
  - Design: Post-lecanemab transcriptomic pathway analysis.
  - Data modalities: High-resolution spatial transcriptomics and single-cell RNA sequencing.
  - Treatment context: Lecanemab treatment.
  - Samples and regions: Not available from provided input.
- **Procedure**:
  1. Generate or analyze high-resolution spatial transcriptomic data after lecanemab treatment.
  2. Integrate or compare with single-cell RNA sequencing to resolve cell-type pathways.
  3. Identify transcriptional pathways involved in Aβ removal.
- **Metrics**: Pathway activation/enrichment and cell-type localization; exact metrics not available from provided input.
- **Expected outcome**:
  - Transcriptional pathways involved in Aβ removal after lecanemab treatment are identified.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E03: Cross-immunization analysis of microglial TREM2/APOE and clearance-related correlations
- **Verifies**: C03, C05
- **Setup**:
  - Design: Cross-approach molecular association analysis.
  - Immunization approaches: Active and passive Aβ immunization.
  - Molecules: TREM2 and APOE in microglia.
  - Outcomes: Antibody responses and Aβ removal.
- **Procedure**:
  1. Measure or infer microglial TREM2 and APOE expression across immunization approaches.
  2. Relate expression patterns to antibody response.
  3. Relate expression patterns to Aβ removal.
- **Metrics**: Direction of expression change and correlation with antibody response/Aβ removal; exact values not available from provided input.
- **Expected outcome**:
  - TREM2 and APOE are upregulated in microglia and positively associated with antibody response and Aβ removal.
- **Baselines**: Nonimmunized AD and/or controls where available; exact baseline structure not available from provided input.
- **Dependencies**: E01, E02

## E04: Brain myeloid-cell complement signaling analysis after immunization
- **Verifies**: C04, C05
- **Setup**:
  - Design: Cell-type/pathway analysis of complement signaling.
  - Cell type: Brain myeloid cells.
  - Context: Aβ clearance after immunization.
  - Exact complement pathway definition: Not available from provided input.
- **Procedure**:
  1. Identify complement signaling activity in brain myeloid cells after immunization.
  2. Link complement signaling to Aβ clearance.
  3. Assess whether the evidence supports contribution to clearance.
- **Metrics**: Complement signaling activity and relationship to Aβ clearance; exact metrics not available from provided input.
- **Expected outcome**:
  - Complement signaling in brain myeloid cells contributes to Aβ clearance after immunization.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01, E02
