# Synthesized Mechanistic Model: Microglial APOE4 → Lipid Dysregulation → AD

*Grounding: full-text. This is the review's core "method" — the mechanistic framework it assembles
around microglial APOE4. Structure mirrors Figures 3, 4, and 5 and §4.1-§4.3. No original data; all
steps are attributed to cited primary studies within the review. Cell-type-specific effects in
astrocytes and neurons (Figure 2A/B, §3.1) are detailed separately in `cell_type_effects.md`.*

## Overview

The review's central claim is that microglia bear APOE4's "most pronounced effects" (Abstract),
and builds a self-reinforcing triad — **lipid metabolic dysregulation → neuroinflammation →
phagocytic impairment** — with each arm feeding back on the others (Figure 5). The upstream driver
is APOE4's molten-globule structural instability (§2.1); the downstream output is impaired
clearance of Aβ, p-tau, and synapses, and disrupted neuron-microglia communication, amplifying
neurotoxicity in AD.

## Stage 1 — Upstream structural cause

APOE4 (Arg112/Arg158) is the least stable of the three APOE isoforms, adopting a "molten globule"
folded-intermediate state that enhances binding to lipid-rich particles and Aβ while impairing
lipid transport capacity (§2.1, Figure 1A). This single biophysical property propagates into every
downstream cell-type-specific lesion the review documents.

## Stage 2 — Microglial lipid metabolic reprogramming (core node)

- Under physiological conditions, microglial lipid metabolism balances fatty acid synthesis (FAS)
  and fatty acid oxidation (FAO) to support immune surveillance (§3.2).
- APOE4 disrupts this equilibrium: upregulates FAS and lipid-droplet (LD) formation (via ACSL1,
  PLIN2), suppresses autophagy/lipophagy genes, and inhibits FAO both directly (mitochondrial
  damage reducing β-oxidation) and indirectly (proinflammatory polarization downregulating
  FAO genes) — the **"enhanced synthesis–suppressed degradation"** imbalance (§3.2).
- ATAC-seq/RNA-seq of LD-rich APOE4 microglia show enrichment of **PU.1** (regulates LD-formation
  genes) and **NF-κB** (proinflammatory gene expression) at accessible enhancers (§4.1.1).
- Under fibrillar-Aβ stimulation via TREM2, the PI3K-Akt-mTOR pathway overexpresses LD-related
  genes ACSL1/PLIN2, especially in APOEε4/ε4 AD patients; TREM2-R47H mutant microglia show reduced
  LD accumulation **in vivo** but exacerbated LD accumulation **in vitro** (§4.1.1; Figure 3) — a
  context-dependent finding (claim C10).
- Output: **LDAM** (lipid-droplet-accumulating microglia) — dysfunctional, proinflammatory,
  phagocytosis-impaired (Figure 2C).

## Stage 3 — Cholesterol overload (parallel lipid lesion)

- Microglial APOE4 induces ER stress → ER Ca2+ depletion → SREBP2 activation → transcription of
  HMGCR and SQLE (cholesterol biosynthesis) (§4.1.2, Figure 3).
- APOE4 impairs ABCA1 recycling and lysosomal function, reducing cholesterol efflux; the resulting
  intracellular cholesterol overload reduces Aβ-degradation capacity.
- Cholesterol's uneven membrane distribution promotes lipid-raft formation, involved in α-/β-/
  γ-secretase-mediated APP cleavage and Aβ generation; disrupted cholesterol homeostasis promotes
  abnormal Aβ accumulation/release and plaque formation (§4.1.2).
- Extracellularly, accumulated cholesterol (from impaired microglial reuptake) increases neuronal
  **GIRK3** expression, hyperpolarizing neurons and reducing excitability (§4.1.3, Figure 3) — a
  direct microglia-to-neuron lipid-signaling consequence.

## Stage 4 — Direct and lipid-amplified neuroinflammation

**Direct/receptor-mediated route** (§4.2, Figure 4A):
- APOE4 binds **LilrB3**, upregulating type-I-interferon-stimulated genes (IFITM3, BST2, MX1,
  ISG15, STAT1), driving a proinflammatory state that impairs phagocytosis and promotes Aβ
  deposition.
- Basal APOE4 microglia show elevated **NLRP3 inflammasome** activation and ROS; LPS/IFN-γ
  stimulation further increases TNF-α, IL-1β, NOS2, MCP1 (more pronounced in female mice).
- The microglial nAPOE4(1-151) fragment increases TNF-α by inhibiting **Cxorf56**.

**Lipid-metabolically amplified route** (§4.2):
- Metabolic reprogramming (glycolysis up, TCA cycle down, carbon flux to lipid synthesis) increases
  proinflammatory lipid mediators (prostaglandins, arachidonic-acid metabolites).
- Accumulated lipid peroxides and cholesterol activate **NF-κB**, forming a self-reinforcing cycle
  of cytokine production and metabolic dysfunction.
- Accumulated lipids enhance **MHC-II**-dependent antigen presentation, hyperactivating T cells.
- APOE4 microglia secrete more **25-hydroxycholesterol (25-HC)** and IL-1β after LPS; 25-HC further
  amplifies IL-1β secretion.

Together these establish a bidirectional "metabolism–inflammation" crosstalk (§4.2): lipid
dysregulation is not merely upstream of inflammation but is actively amplified by it in return.

## Stage 5 — Phagocytic impairment (Aβ, tau, synapses)

**Aβ clearance** (§4.3, Figure 4B):
- APOE4 induces mitochondrial dysfunction and compromises pseudopod extension (altered membrane
  fluidity from lipid accumulation), coupled with downregulated **TREM2** — collectively impairing
  phagocytic capacity.
- APOE4 increases fibrillar-aggregate nucleation within microglia (seeding plaque formation) and
  specifically suppresses Aβ42 clearance via **ITGB8–TGFβ** disruption; selective ablation of
  microglial APOE4 restores phagocytic function and reduces plaque burden.
- In female APOEε4 carriers, neutrophil **IL-17F** interacting with microglial **IL-17RA** disrupts
  Aβ clearance; interrupting this signaling ameliorates cognitive deficits and reduces Aβ
  deposition.

**Tau/synapse clearance** (§4.3):
- LD accumulation compromises membrane integrity and endosomal-lysosomal function, attenuating
  tau-protein processing and causing intracellular p-tau accumulation; accumulated p-tau is
  released via exosomes, propagating intercellularly.
- Increased microglial phagocytosis of pathological synapses is observed in APOEε4-carrier AD
  brains, particularly near Aβ plaques, correlating with cognitive decline.

## Stage 6 — Feedback loops (self-reinforcement, Figure 5)

- **Lipid dysregulation ⇄ neuroinflammation**: metabolic reprogramming produces inflammatory lipid
  mediators and NF-κB activation (Stage 4), while inflammation (cytokines, ROS) further disrupts
  lipid handling.
- **Impaired phagocytosis ⇄ pathology accumulation**: phagocytosis-impaired APOE4 microglia release
  proinflammatory cytokines and ROS that promote neuronal lipogenesis and lipid translocation to
  microglia, "creating a vicious cycle" (§4.1.3, Figure 3 legend).
- **Neuroinflammation ⇄ functional impairment**: "activation of neuroinflammation further
  aggravates abnormal lipid metabolism and affects the immune function of microglia" (§6).
- Net output (§6): the pathogenic triad — **lipid dysregulation, sustained neuroinflammation, and
  impaired phagocytosis** — forms a self-perpetuating cycle that exacerbates AD progression via
  three convergent effects: (1) proinflammatory cytokine secretion activating microglia; (2)
  impaired phagocytic function via energy metabolism, membrane fluidity, and lysosomal deficits;
  and (3) disrupted neuron-microglia crosstalk through lipid-mediated signaling.

## Stage 7 — Neuron-microglia communication disruption (§4.1.3)

- APOE4 induces pronounced microglial LD accumulation, impairing lipid-uptake efficiency and
  enhancing proinflammatory signaling, attenuating microglial surveillance of neuronal-network
  activity.
- APOE4 shifts microglial energy metabolism from oxidative phosphorylation toward glycolysis,
  further exacerbating intracellular lipid accumulation.
- Impaired lipid reuptake causes extracellular cholesterol accumulation → neuronal hyperpolarization
  via GIRK3 upregulation → reduced neuronal excitability.
- Bidirectionally, neurons actively regulate microglial lipid metabolism via **AMPK**-mediated
  suppression of lipogenesis and activation of lipophagy — a reciprocal regulatory mechanism.

## Method status

This is a **synthesized narrative model**, not a formally specified algorithm or quantitative
pathway model. It is supported by convergent evidence from iPSC-derived human glia, APOE-targeted-
replacement/chimeric mouse models, and post-mortem human tissue, but retains unresolved gaps (see
`constraints.md` and `problem.md` G1-G4) — notably the lack of an integrated quantitative model
across its five-plus semi-independent molecular arms, and the unexplained context-dependence of
TREM2-R47H.
