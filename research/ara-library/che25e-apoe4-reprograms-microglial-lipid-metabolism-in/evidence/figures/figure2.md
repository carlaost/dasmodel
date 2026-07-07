# Figure 2: APOE4-mediated dysfunction of cellular lipid metabolism

- **Source**: Figure 2, p.4, Chen et al. (2025), *BioScience Trends*, Advance Publication, doi:10.5582/bst.2025.01148, §3.1-§3.2
- **Caption**: "Figure 2. APOE4-mediated dysfunction of cellular lipid metabolism. (A). APOE4
  astrocytes exhibit dysregulated lipid metabolism, characterized by SREBP2 activation, de novo
  cholesterol synthesis, and PPARγ suppression. Pathological cholesterol accumulation impairs
  mitophagy, leading to mitochondrial dysfunction. Additionally, APOE4 astrocytes specifically
  upregulates GPC-4, enhancing LRP1-mediated tau propagation. (B). APOE4 is hydrolyzed by
  neuron-specific proteases, producing neurotoxic fragments that exacerbate tau pathology and
  activate microglia. Metabolically, FAs are increased in APOE4 neurons, and hyperbinding of APOE4
  to LDLR further increases lipid uptake in neurons, leading to lipid metabolism disorders,
  triggering lysosomal dysfunction, lipofuscin accumulation, and impaired autophagy-mediated tau
  protein aggregation. C. APOE4 microglia exhibit diverse phenotypic features, including LDAM, DAM,
  phagocytosis and pro-inflammatory phenotype, MGnD and TIM. SREBP2, sterol regulatory
  element-binding protein 2; GPC-4, glypican-4; FAs, fatty acids; LDAM, lipid-droplet-accumulating
  microglia; DAM, disease-associated microglia; MGnD, neurodegenerative microglia; TIM, terminally
  inflammatory microglia."
- **Screenshot**: figure2.png
- **Figure type**: diagram (schematic mechanism diagram, three panels; no plotted data points)
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description

**Panel A — "APOE4 astrocytes"**: A membrane-embedded receptor (GPC-4) connects to LRP1, labeled
"p-tau spread" across the membrane. Inside the cell, *APOE DNA* is transcribed via two parallel
arms: (1) CEBP → mRNA → APOE4 protein (helical ribbon icon), which is exported and feeds back to
up-regulate GPC-4 (closing an autocrine loop, arrow from "APOE4" back up to "GPC-4"); (2) SREBP2 +
PPARγ (shown as a suppressed/dimmed pairing) → "synthesis of cholesterol" (hexagon icons) → a
lysosome-like vesicle. A "mitophagy" icon (double-membrane vesicle with DNA) sits below the
cholesterol-synthesis output with an inhibitory (⊣) connector from cholesterol synthesis to
mitophagy. Free lipid-droplet (yellow circle) icons are scattered in the cytoplasm.

**Panel B — "APOE4 neurons"**: A neuronal soma/axon-terminal icon shows two enlarged
vesicle/organelle structures inside the terminal: one containing scattered small dots/fragments
labeled via a dashed connector to "lysosomal autophagy disorder," and one containing dark
red/brown granules. Outside the terminal, "fatty acids" (yellow circle icons) point in via an
arrow. "APOE4 fragments," labeled with a bullet list "p-tau / lipofuscin / APOE4 fragments ↑" and
an upward red arrow, are shown budding from the terminal alongside dark-red fibrillar icons. A
separate "LDLR → APOE4" downward arrow on the left indicates receptor-mediated APOE4 uptake into
the neuron. An "activated microglia" icon (distinct purple/lavender branched cell) sits at
lower-right, receiving the released fragments/tau.

**Panel C — "APOE4 microglia" (subtype taxonomy)**: A central microglia icon (with APOE4 triangle
icons inside) sends five branching arrows to five labeled subtype outcomes, each with a
gene/marker-expression box and a resulting cell icon:
1. Box "Plin2, ACSL1↑ / Clec7a, CD74↓" → cell icon "LDAM" (filled with yellow lipid droplets) →
   downstream arrow to "tau pathology / neuron toxicity."
2. Box "Iba1, Tmem119↓ / ApoE, Trem2↑" → cell icon "DAM" (orange) → below it: "aerobic glycolysis↑
   / HIF-1α↑" → arrow to "Aβ clearance↓."
3. Box "Trem1, Trem2, Tyrobp↑" → cell icon labeled "enriched in phagocytosis and proinflammatory
   genes" (pink, containing brown aggregate icons).
4. Box "Tgfβ1, Inpp5d, P2ry12, Tmem119↓ / ApoE, Clec7a↑" (connected via an "ITGB8-TGFβ" labeled
   arrow from the central microglia) → cell icon "MGnD" (tan, with brown granular inclusions).
5. Box "S100a8/9, Fos, Jun↑ / Smad4, Irf5/7/9, Stat1/2↓" → cell icon "TIM" → downstream arrow to
   "Aβ clearance↓" (with a brown aggregate icon).

A shared legend (bottom of panel C) defines: APOE4 (dark red triangle), Aβ (brown aggregate),
cholesterol (yellow hexagon), autophagosome (blue-ringed circle), LDs (yellow circle cluster),
lysosome (pink-ringed circle), tau protein tangle (dark-red fibril), lipofuscin (brown granule
cluster).

**What it conveys**: The figure is the review's cell-type comparison centerpiece — Panel A
(astrocyte) and Panel B (neuron) establish parallel but distinct lipid-handling lesions, while
Panel C establishes that "microglial dysfunction" under APOE4 is not one state but five
transcriptionally distinct subtypes (LDAM, DAM, a phagocytic/proinflammatory-enriched cluster,
MGnD, TIM), each with a characteristic marker signature and functional consequence — directly
grounding `logic/solution/cell_type_effects.md`'s subtype table and claim C09.
