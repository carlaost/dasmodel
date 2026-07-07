# Cell-Type-Specific Effects of APOE4 on Lipid Metabolism

*Grounding: full-text §3.1 (astrocytes and neurons), §3.2 (microglial subtypes). This file captures
the comparative cell-type survey the review uses to justify its microglia-centric focus (Abstract,
problem.md O4). The microglial mechanistic deep-dive itself is in `mechanisms.md`; this file covers
astrocytes, neurons, and the taxonomy of microglial subtypes (Figure 2).*

## Astrocytes (§3.1, Figure 2A)

Astrocytes are the primary CNS source of APOE, with expression modulated by C/EBPβ and
mitochondrial function. Physiologically, astrocyte-derived APOE maintains lipid homeostasis,
supports synaptic pruning, and preserves BBB integrity.

**APOE4 astrocyte dysregulation**:
- Aberrant **SREBP2** activation increases de novo cholesterol synthesis despite lysosomal-
  dysfunction-induced accumulation; upregulated lipid-metabolism genes but downregulated transport
  genes, potentially mediated by reduced **PPARγ** expression.
- Pathological cholesterol accumulation disrupts lysosome-dependent **mitophagy**, causing
  mitochondrial dysfunction and early AD energy deficits.
- Accumulation of enlarged, oxidation-prone lipid droplets enriched with unsaturated triglycerides;
  secretion of poorly lipidated lipoproteins that inefficiently support neuronal lipid demands,
  impairing synaptogenesis and neuronal viability.
- Upregulation of **glypican-4 (GPC-4)**, increasing **LRP1** membrane trafficking to promote tau
  propagation and hyperphosphorylation; impaired APOE4-mediated miRNA transfer to neurons,
  disrupting neuronal metabolic/epigenetic regulation.
- Net effect: synaptic dysfunction and memory deficits via multiple synergistic pathways.

## Neurons (§3.1, Figure 2B)

Neuronal APOE expression increases during stress and aging, with early detrimental effects on
synaptic function and neurodevelopment.

**APOE4 neuron dysregulation**:
- Excessive APOE4-**LDLR** binding increases neuronal lipid uptake → lysosomal dysfunction,
  lipofuscin accumulation, impaired autophagy → tau protein aggregation and brain cell death.
- Deficient fatty-acid (FA) storage in lipid droplets → pathological accumulation of free FAs →
  increased lipotoxicity risk; neighboring astrocytes take up these lipids but APOE4 impairs their
  transport/oxidation capacity, particularly in the hippocampus.
- APOE4 promotes **ABCA1** degradation, reduces cholesterol efflux, and activates **mTORC1**-
  mediated senescence pathways, impairing synaptic plasticity.
- APOE4 undergoes neuron-specific proteolysis, generating neurotoxic fragments that destabilize the
  cytoskeleton and exacerbate tau pathology.
- APOE4 selectively depletes GABAergic neurons (potentially disrupting neural network balance) and
  activates microglia via cell-nonautonomous mechanisms, amplifying neuroinflammation.

## Microglial subtype taxonomy (§3.2, Figure 2C)

Single-cell sequencing reveals microglial subtypes mediated by cellular metabolic reprogramming
during development, growth, and disease:

| Subtype | Signature | APOE4-driven functional consequence |
|---|---|---|
| **LDAM** (lipid-droplet-accumulating microglia) | Plin2, ACSL1 ↑; Clec7a, CD74 ↓ | Canonical APOE4 pathological subtype: dysregulated lipid metabolism, proinflammatory, impaired phagocytosis → tau pathology, neuron toxicity |
| **DAM** (disease-associated microglia) | Iba1, Tmem119 ↓; ApoE, Trem2 ↑; Trem1, Trem2, Tyrobp ↑ | Aerobic glycolysis ↑, HIF-1α ↑, Aβ clearance ↓; APOE4 microglia show DAM-consistent features with impaired Aβ uptake |
| Phagocytosis/proinflammatory-enriched subset | (clusters near plaques) | Drives conversion via APOE-TREM2-TYROBP axis |
| **MGnD** (neurodegenerative microglia) | Tgfβ1, Inpp5d, P2ry12, Tmem119 ↓; ApoE, Clec7a ↑ | Normally neuroprotective (clears apoptotic neurons) via TREM2-APOE pathway; APOE4 exacerbates neurodegeneration by activating ITGB8-TGFβ signaling and inhibiting MGnD function |
| **TIM** (terminally inflammatory microglia) | S100a8/9, Fos, Jun ↑; Smad4, Irf5/7/9, Stat1/2 ↓ | Exhausted, APOE4-associated subtype; profound Aβ-clearance deficits in AD patients and mouse models |

This taxonomy is the phenotypic vocabulary underlying the mechanistic claims in `mechanisms.md` —
"microglial dysfunction" in this review is not a single state but a family of transcriptionally
distinct, APOE4-enriched pathological subtypes.

## Comparative framing

The review's explicit rationale (Abstract; §3 intro) for focusing on microglia despite documenting
real astrocyte and neuron lesions: microglia show the review's most extensively characterized,
most functionally consequential (energy-metabolism deficits, LDAM formation), and most therapeutically
tractable (Table 1 majority of agents target microglia specifically) APOE4 effects — astrocyte and
neuron lesions are real but comparatively narrower in the cited literature's scope.
