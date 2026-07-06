# Constraints, Assumptions, and Limitations

> Grounding: abstract-only. This file emphasizes unavailable details to prevent downstream agents from treating abstract-level claims as full protocol knowledge.

## Boundary Conditions

- Study domain: Alzheimer’s disease brain tissue and Aβ immunization.
- Immunization modes: Active and passive Aβ immunization are both mentioned in the abstract.
- Comparison groups explicitly named: actively immunized AD patients, nonimmunized AD patients, and neurologically healthy controls.
- Passive treatment explicitly named: lecanemab.
- Data modalities explicitly named: spatial transcriptomics, high-resolution spatial transcriptomics, and single-cell RNA sequencing.
- Cell/process focus explicitly named: microglia, brain myeloid cells, TREM2, APOE, complement signaling, antibody responses, and Aβ removal/clearance.

## Assumptions

- The abstract is assumed to summarize the paper’s central claims accurately.
- Positive correlation language is interpreted as association unless the full text supplies causal or perturbational evidence.
- "Contributes to Aβ clearance" is retained as the authors' wording, but the provided input does not reveal whether contribution is inferred from association, enrichment, perturbation, or another design.

## Known Limitations

- Sample sizes: Not available from provided input.
- Brain regions profiled: Not available from provided input.
- Tissue source, pathology scoring, and inclusion/exclusion criteria: Not available from provided input.
- Sequencing/spatial platforms and preprocessing: Not available from provided input.
- Statistical models, covariates, multiple-testing correction, and thresholds: Not available from provided input.
- Exact microglial-state definitions and marker panels beyond TREM2/APOE: Not available from provided input.
- Complement genes/pathway components: Not available from provided input.
- Figures, tables, appendices, and supplementary data: Not available from provided input.
- Code, configs, and data-access instructions: Not available from provided input.

## Practical Use Bounds

- This ARA can support high-level paper discovery, claim indexing, and abstract-grounded reasoning.
- This ARA cannot support reproduction, numerical meta-analysis, protocol replication, or figure/table extraction without the full paper and supplementary materials.
