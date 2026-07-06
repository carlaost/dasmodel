# Claims

> Grounding: abstract-only. Every claim is supported by the abstract in `metadata.md` / `metadata.json`. No exact quantitative result values are available beyond bibliographic metadata, so claims avoid invented numbers and cite verbatim abstract phrases.

## C01: Distinct microglial states are associated with Aβ clearance after immunization
- **Statement**: Spatial transcriptomics identifies distinct microglial states associated with Aβ clearance when actively immunized AD brains are compared with nonimmunized AD brains and neurologically healthy controls.
- **Status**: supported
- **Falsification criteria**: Full-text methods or data showing no distinct microglial states associated with Aβ clearance, or showing that the comparison groups described in the abstract were not used.
- **Proof**: [E01]
- **Evidence basis**: The abstract states that the authors compare actively immunized AD, nonimmunized AD, and neurologically healthy controls and identify distinct microglial states associated with Aβ clearance.
- **Interpretation**: The result supports a microglia-centered mechanism for immune-mediated amyloid clearance, but effect sizes, state definitions, and brain-region distributions are not available from provided input.
- **Sources**:
  - microglial states associated with Aβ clearance ← metadata.md:13 «We compare actively immunized patients with AD with nonimmunized patients with AD and neurologically healthy controls, identifying distinct microglial states associated with Aβ clearance.» [result]
- **Dependencies**: none
- **Tags**: microglia, spatial-transcriptomics, amyloid-clearance, active-immunization

## C02: High-resolution spatial transcriptomics and single-cell RNA sequencing identify pathways involved in Aβ removal after lecanemab treatment
- **Statement**: High-resolution spatial transcriptomics alongside single-cell RNA sequencing is used to investigate transcriptional pathways involved in Aβ removal after lecanemab treatment.
- **Status**: supported
- **Falsification criteria**: Full-text methods showing that lecanemab-treated samples were not analyzed with high-resolution spatial transcriptomics and single-cell RNA sequencing, or that no transcriptional pathways linked to Aβ removal were investigated.
- **Proof**: [E02]
- **Evidence basis**: The abstract reports high-resolution spatial transcriptomics with single-cell RNA sequencing to delve into transcriptional pathways involved in Aβ removal after lecanemab treatment.
- **Interpretation**: This claim identifies the analysis modality and target process; the abstract does not provide exact pathway lists beyond TREM2/APOE and complement signaling.
- **Sources**:
  - lecanemab transcriptional pathway analysis ← metadata.md:13 «Using high-resolution spatial transcriptomics alongside single-cell RNA sequencing, we delve deeper into the transcriptional pathways involved in Aβ removal after lecanemab treatment.» [result]
- **Dependencies**: C01
- **Tags**: lecanemab, single-cell-RNA-sequencing, spatial-transcriptomics, transcriptional-pathways

## C03: TREM2 and APOE are upregulated in microglia across immunization approaches and correlate with antibody response and Aβ removal
- **Statement**: TREM2 and APOE are upregulated in microglia across Aβ immunization approaches and correlate positively with antibody responses and Aβ removal.
- **Status**: supported
- **Falsification criteria**: Full-text data showing no microglial TREM2/APOE upregulation across immunization approaches, or no positive correlation with antibody responses and Aβ removal.
- **Proof**: [E03]
- **Evidence basis**: The abstract states this molecular finding directly.
- **Interpretation**: TREM2/APOE are candidate molecular mechanisms and potential therapeutic target space, but the abstract does not provide correlation coefficients, adjusted models, or causal perturbation evidence.
- **Sources**:
  - TREM2/APOE upregulation and positive correlation ← metadata.md:13 «Our analysis reveals upregulation of the triggering receptor expressed on myeloid cells 2 (TREM2) and apolipoprotein E (APOE) in microglia across immunization approaches, which correlate positively with antibody responses and Aβ removal.» [result]
- **Dependencies**: C01, C02
- **Tags**: TREM2, APOE, microglia, antibody-response, amyloid-removal

## C04: Complement signaling in brain myeloid cells contributes to Aβ clearance after immunization
- **Statement**: Complement signaling in brain myeloid cells contributes to Aβ clearance after immunization.
- **Status**: supported
- **Falsification criteria**: Full-text results showing complement signaling is not changed, not localized to brain myeloid cells, or not linked to Aβ clearance after immunization.
- **Proof**: [E04]
- **Evidence basis**: The abstract says that complement signaling in brain myeloid cells contributes to Aβ clearance after immunization.
- **Interpretation**: The authors present complement signaling as part of the mechanism of immune-mediated clearance; the abstract does not reveal whether this is supported by association, perturbation, pathway enrichment, or another analysis.
- **Sources**:
  - complement signaling contribution ← metadata.md:13 «Furthermore, we show that complement signaling in brain myeloid cells contributes to Aβ clearance after immunization.» [result]
- **Dependencies**: C01, C02
- **Tags**: complement-signaling, brain-myeloid-cells, immunization, amyloid-clearance

## C05: Reported microglial mechanisms suggest potential targets for enhancing Aβ-targeted immunotherapies
- **Statement**: The reported transcriptional mechanisms of Aβ removal uncover potential molecular targets that could enhance Aβ-targeted immunotherapies.
- **Status**: hypothesis
- **Falsification criteria**: Follow-up mechanistic or therapeutic studies showing that the reported pathways do not modulate Aβ-targeted immunotherapy response or cannot be targeted to improve Aβ clearance.
- **Proof**: [E03, E04]
- **Evidence basis**: The abstract frames the reported mechanisms as providing new insight and uncovering potential molecular targets for improving Aβ-targeted immunotherapies.
- **Interpretation**: This is a forward-looking therapeutic implication rather than a demonstrated intervention effect in the provided abstract.
- **Sources**:
  - potential molecular targets ← metadata.md:13 «Importantly, our work uncovers potential molecular targets that could enhance Aβ-targeted immunotherapies, offering new avenues for developing more effective therapeutic strategies to combat AD.» [result]
- **Dependencies**: C03, C04
- **Tags**: molecular-targets, immunotherapy-enhancement, therapeutic-strategy, Alzheimer-disease
