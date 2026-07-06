# Claims

> Grounding: abstract-only. Claims use only `metadata.md` and `metadata.json`. The only load-bearing number in a claim is the review's stated two-part structure, grounded verbatim below. No full-text evidence, figures, or tables were available.

## C01: Neurovascular and clearance dysregulation is implicated in Alzheimer pathophysiology
- **Statement**: Clinical and preclinical evidence implicates brain microcirculation, cerebral hypoperfusion, blood-brain barrier dysfunction, and reduced amyloid clearance in Alzheimer pathophysiology.
- **Status**: supported
- **Falsification criteria**: A comprehensive review of the clinical and preclinical evidence showing no material link between these systems and Alzheimer pathophysiology.
- **Proof**: [E01]
- **Evidence basis**: The abstract states this implication directly.
- **Interpretation**: The paper treats vascular, barrier, perfusion, and clearance biology as core Alzheimer disease mechanisms rather than secondary context.
- **Sources**:
  - neurovascular and clearance implication <- metadata.md Abstract «Evidence from clinical and preclinical studies implicates brain microcirculation, cerebral hypoperfusion, blood–brain barrier dysfunction, and reduced amyloid clearance in Alzheimer pathophysiology.» [result]
- **Dependencies**: none
- **Tags**: Alzheimer disease, microcirculation, hypoperfusion, blood-brain barrier, amyloid clearance

## C02: The review uses a two-part physiology-to-disease structure
- **Statement**: The review has 2 parts: one describing cerebral microcirculation, cerebral blood flow, extracellular fluid drainage, and neurovascular-unit components with emphasis on the blood-brain barrier, and one summarizing how each aspect is altered in Alzheimer disease.
- **Status**: supported
- **Falsification criteria**: Full-text inspection showing that the paper is not organized around these two parts or does not cover the listed systems.
- **Proof**: [E02]
- **Evidence basis**: The abstract explicitly states the review's two-part structure.
- **Interpretation**: This design supports a component-wise comparison between healthy neurovascular physiology and Alzheimer disease dysregulation.
- **Sources**:
  - 2 parts <- metadata.md Abstract «This review has 2 parts: part 1 describes the cerebral microcirculation, cerebral blood flow, extracellular fluid drainage, and the neurovascular unit components with an emphasis on the blood-brain barrier, and part 2 summarizes how each aspect is altered in AD.» [result]
- **Dependencies**: C01
- **Tags**: review design, neurovascular unit, blood-brain barrier, extracellular fluid drainage

## C03: Aberrant pericytes are framed as early and central contributors in Alzheimer disease
- **Statement**: Discussing neurovascular-unit structures separately allows the authors to conclude that aberrant pericytes are an early contributor and central to understanding Alzheimer disease pathophysiology.
- **Status**: supported
- **Falsification criteria**: Full-text inspection showing that pericytes are not treated as early contributors or central explanatory actors.
- **Proof**: [E02, E03]
- **Evidence basis**: The abstract states this conclusion directly.
- **Interpretation**: The paper's central synthesis is pericyte-centered rather than merely listing pericytes as one neurovascular component among many.
- **Sources**:
  - pericyte centrality <- metadata.md Abstract «Discussing the neurovascular unit structures separately allows us to conclude that aberrant pericytes are an early contributor and central to understanding AD pathophysiology.» [result]
- **Dependencies**: C01, C02
- **Tags**: pericytes, Alzheimer pathophysiology, neurovascular unit

## C04: Pericytes connect barrier integrity, capillary dynamics, coupling, drainage, and protein clearance
- **Statement**: Pericytes are described as having functions in blood-brain barrier integrity, capillary blood flow, capillary stalling, neurovascular coupling, intramural periarterial drainage, glymphatic drainage, and consequently amyloid and tau clearance.
- **Status**: supported
- **Falsification criteria**: Full-text inspection showing that the paper does not attribute these functions to pericytes.
- **Proof**: [E03]
- **Evidence basis**: The abstract lists these functions directly.
- **Interpretation**: Pericyte dysfunction is positioned as a multi-pathway mechanism, capable of linking perfusion abnormalities to impaired molecular clearance.
- **Sources**:
  - pericyte functions <- metadata.md Abstract «Pericytes have multiple functions including maintenance of blood-brain barrier integrity and the control of capillary blood flow, capillary stalling, neurovascular coupling, intramural periarterial drainage, glia-lymphatic (glymphatic) drainage, and consequently amyloid and tau clearance.» [result]
- **Dependencies**: C03
- **Tags**: pericytes, barrier integrity, capillary flow, glymphatic drainage, amyloid clearance, tau clearance

## C05: Pericyte dysfunction is linked to hypoperfusion and PDGBB-PDGFRbeta signaling failure
- **Statement**: Hypoperfusion in Alzheimer disease is linked to a pericyte-mediated response, and deficient endothelial cell-pericyte PDGBB-PDGFRbeta signaling loops cause pericyte dysfunction that contributes to and can initiate Alzheimer degeneration.
- **Status**: supported
- **Falsification criteria**: Evidence showing that the review does not link Alzheimer hypoperfusion to pericyte-mediated responses or does not describe deficient PDGBB-PDGFRbeta signaling as causative for pericyte dysfunction.
- **Proof**: [E03]
- **Evidence basis**: The abstract states both mechanistic links directly.
- **Interpretation**: The abstract treats pericytes not only as markers of pathology but as possible causal participants in degenerative progression.
- **Sources**:
  - hypoperfusion link <- metadata.md Abstract «Hypoperfusion in AD is linked to a pericyte-mediated response.» [result]
  - signaling-loop dysfunction <- metadata.md Abstract «Deficient endothelial cell–pericyte (PDGBB-PDGFRβ) signaling loops cause pericyte dysfunction, which contributes and even initiates AD degeneration.» [result]
- **Dependencies**: C03, C04
- **Tags**: hypoperfusion, PDGBB-PDGFRbeta, endothelial cell-pericyte signaling, degeneration

## C06: Pericytes are proposed as therapeutic and regenerative-therapy targets
- **Statement**: The authors conclude that pericytes are central to Alzheimer disease pathophysiology, an interesting therapeutic target in Alzheimer disease, and have an emerging role in regenerative therapy.
- **Status**: supported
- **Falsification criteria**: Full-text inspection showing that the review does not make a therapeutic-target or regenerative-therapy argument about pericytes.
- **Proof**: [E04]
- **Evidence basis**: The abstract conclusion states the therapeutic and regenerative-therapy framing directly.
- **Interpretation**: The paper's translational implication is that pericyte biology may guide drug-target identification and treatment development.
- **Sources**:
  - therapeutic target <- metadata.md Abstract «We conclude that pericytes are central to understanding AD pathophysiology, are an interesting therapeutic target in AD, and have an emerging role in regenerative therapy.» [result]
- **Dependencies**: C03, C04, C05
- **Tags**: therapeutic target, regenerative therapy, pericytes, translational relevance
