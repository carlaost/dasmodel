# Problem Specification

## Observations

### O1: Glia cluster around Aβ plaques but their human in-situ transcriptional interplay is undefined
- **Statement**: Microglia and astrocytes are known to cluster around amyloid-beta (Aβ) plaques and form "reactive glial nets," and glial responses continue to evolve after Aβ accumulation plateaus, but how glial cells interact with Aβ plaques within "plaque-glia niches" (local microenvironments containing both Aβ and reactive glia) to shape local cellular composition and gene expression in the human brain remained undefined prior to this study.
- **Evidence**: Background section, citing prior imaging/transcriptomic studies [refs 1-8]; Page 2 of 23.
- **Implication**: Establishes the central unresolved question the paper addresses — whether/how plaque-associated glia shape the local transcriptome in human tissue.

### O2: Prior spatial transcriptomics (ST) of AD pathology was almost entirely restricted to mouse models or tiny human samples
- **Statement**: Spatial profiling technologies had been applied in AD research primarily in mouse models; a recent human-brain ST study identifying altered gene-module co-expression near AD pathology "only comprised a handful of samples."
- **Evidence**: Background section, citing ref [14] (Chen et al. 2022); Page 2 of 23.
- **Implication**: Motivates generating a large, paired ST + IHC human dataset to obtain statistical power that prior human work lacked.

### O3: The study generated a large paired ST-IHC human AD dataset
- **Statement**: The authors profiled 258,987 Visium ST spots (average 3,505 genes and 9,908 transcripts/UMIs per spot) across 78 postmortem DLPFC sections from 21 ROSMAP participants (13 AD, 8 no-cognitive-impairment controls), each ST section paired with two IHC-stained adjacent sections (Aβ, GFAP, IBA1).
- **Evidence**: Results §"Spatial transcriptomics on postmortem DLPFC of 21 ROSMAP participants", Page 10 of 23; Methods "Tissue collection..."; Fig. 1A.
- **Implication**: Provides the statistical power (repeated-measures pseudobulk contrasts across dozens of sections/donors) needed to resolve niche-specific transcriptomic effects that smaller studies could not detect.

### O4: Low-Aβ (diffuse-plaque-enriched) spots show more transcriptomic signs of neurotoxicity than high-Aβ spots
- **Statement**: Contrasting low- vs. high-Aβ pseudobulk expression detected 93, 140, and 159 FDR-significant DEGs for the combined, glia-low, and glia-high conditions respectively (only 18 genes shared across all three contrasts), with GSEA showing reduced synaptic-function pathways and elevated apoptosis/immune genes (e.g., CIDEA) in low-Aβ spots, and IHC confirming more cleaved-caspase-3 near low-Aβ plaques than high-Aβ plaques.
- **Evidence**: Results §"Low-Aβ spots show transcriptomic profiles indicative of a more neurotoxic local environment", Page 11 of 23; Fig. 3B-I.
- **Implication**: Suggests neuronal damage may occur earlier in plaque development (around diffuse, low-Aβ plaques) rather than after plaques mature, because vulnerable neurons near high-Aβ plaques may have already died.

### O5: Higher local glia abundance is associated with a more neurotoxic, more inflamed niche
- **Statement**: Contrasting glia-high vs. glia-low spots detected 230, 241, and 63 FDR-significant DEGs for combined, low-Aβ, and high-Aβ conditions respectively, with glial markers (SPARC, CD44, HLA-DRA) up and neuronal/synaptic markers (RORB, PVALB, SYT2, SLC6A17, GABBR2, NEFH/M/L) down in glia-high spots; IHC confirmed reduced SYP/NeuN and elevated CD68 near glia-high plaques versus glia-low plaques.
- **Evidence**: Results §"Plaques with surrounding glia display transcriptomic differences indicative of elevated neuronal toxicity", Page 13-16 of 23; Fig. 5B-H.
- **Implication**: Glial reactivity, not just Aβ load per se, is an independent driver of local neurodegeneration.

### O6: Spatial glial transcriptomic responses converge on a common, DAM-like human microglial state (MG3)
- **Statement**: GSEA against mouse plaque-induced gene modules (PIG, OLIG, DAM, DAA) and 12 human AD microglial states (MG0-MG12, from Sun et al. 2023) showed enrichment across most states except homeostatic MG0/MG1, with the MG3 ("ribosome biogenesis," DAM-like) state showing the strongest, most consistent enrichment across all Aβ and glia contrasts.
- **Evidence**: Results, Page 12-16 of 23; Fig. 3F, Fig. 5F.
- **Implication**: Identifies a candidate cellular target (MG3-like microglia) for niche-specific immunomodulatory therapy.

### O7: An iPSC-derived microglia-only (not astrocyte, not neuron) in vitro system recapitulates the spatial glial signature
- **Statement**: In an iPSC-derived co-culture of microglia-like cells (iMGL), astrocytes and neurons treated with Aβ oligomers for 24 h, scRNA-seq identified 199, 58, and 271 Aβ-induced DEGs in neurons, astrocytes, and iMGLs respectively; GSEA showed the ST-derived glia-high-vs-glia-low signature was positively enriched only in the iMGL Aβ-response genes, with no enrichment in astrocytes or neurons.
- **Evidence**: Results §"ST glial response to Aβ plaques recapitulated by co-cultured microglia-like cells...", Page 16 of 23; Fig. 7C-J.
- **Implication**: Points to microglia (versus astrocytes) as the primary cell type driving the spatially observed glial transcriptional response to Aβ, and provides a tractable in vitro model for mechanistic follow-up.

### O8: Aβ intensity-based spot stratification tracks plaque maturation stage across two independent tissue cohorts
- **Statement**: High-Aβ IHC-intensity spots were enriched for compact/dense-core plaques and low-Aβ spots for diffuse plaques both in the frozen ST-adjacent sections (781 manually annotated plaques; OR = 3.02, p = 3.21e-9) and in an independent FFPE validation cohort (722 manually annotated plaques from 9 AD ROSMAP participants; OR = 14.98, p = 4.89e-38).
- **Evidence**: Results §"ST spot stratification by Aβ and glial staining", Page 10-11 of 23; Fig. 2C; Supplementary Fig. 6.
- **Implication**: Validates that the paper's IHC-intensity-based Aβ stratification (no/low/high) is a reasonable, reproducible proxy for classical neuropathological plaque typing (diffuse/compact/dense-core), which could not be scored directly on frozen ST sections due to freezing artifacts.

## Gaps

### G1: No large, spatially resolved, IHC-paired transcriptomic dataset of human AD plaque-glia niches existed
- **Statement**: Without a large paired ST + IHC dataset, it was not possible to statistically resolve which genes/pathways differ specifically as a function of local Aβ load and local glial abundance in human brain tissue (as opposed to bulk tissue or animal models).
- **Caused by**: O1, O2.
- **Existing attempts**: Mouse ST studies of plaque niches (e.g., Chen et al. 2020 PIG/OLIG modules; Zeng et al. 2023); a small (few-sample) human ST study (Chen et al. 2022).
- **Why they fail**: Mouse glia show transcriptional signatures distinct from human glia (refs 6-8), so mouse-derived niche modules cannot be assumed to transfer; the one prior human ST study lacked the sample size for statistically robust niche-level contrasts.

### G2: It was unknown which of the several proposed glial-activation frameworks (mouse DAM/DAA/PIG/OLIG modules vs. human-brain-derived MG0-12 microglial states) actually characterize the glial response around plaques in situ in the human cortex, and whether that response is separable into a specific glial-cell contribution.
- **Caused by**: O1, O6.
- **Existing attempts**: snRNA-seq characterizations of human AD microglial states in bulk/dissociated tissue (Sun et al. 2023); mouse-model DAM/DAA/PIG/OLIG gene-module definitions.
- **Why they fail**: snRNA-seq loses spatial context (cannot say which state arises specifically near plaques vs. elsewhere), and the mouse gene modules had unconfirmed applicability to human spatial data before this study's GSEA cross-referencing.

### G3: Directionality of Aβ-plaque-stage vs. neurotoxicity was unresolved
- **Statement**: It was unclear whether neurotoxicity (synaptic/neuronal loss, apoptosis) tracks with increasing Aβ load (compact/dense-core, "high-Aβ" plaques) or is instead more pronounced earlier, around diffuse ("low-Aβ") plaques.
- **Caused by**: O1.
- **Existing attempts**: Label-free vibrational imaging (Röhr et al. 2020) and cryo-EM filament-typing (Yang et al. 2022) studies suggesting early-stage plaques are richer in toxic oligomers/protofibrils.
- **Why they fail**: These studies characterize plaque biochemistry but do not directly measure the local transcriptomic/neuronal consequence, leaving the transcriptomic evidence for early- vs. late-stage plaque toxicity untested until this paper's Aβ-stratified DEG/IHC analysis (O4).

### G4: No experimental system existed to test, in a controlled and manipulable way, which brain cell type drives the ST-observed glial response to Aβ
- **Caused by**: O1, O6.
- **Existing attempts**: Single-cell-type iPSC-microglia studies exposed to AD-related stimuli (refs 8, 69) established that iMGLs can adopt disease states, but had not been cross-validated against a matched in vivo human ST plaque-niche signature in a multicellular (microglia+astrocyte+neuron) co-culture.
- **Why they fail**: Prior iMGL work did not have a spatial, tissue-derived reference signature to test enrichment against, and cultured microglia are known to diverge transcriptionally from in vivo microglia absent brain-specific cues (refs 71, 72), so cross-validation against the human ST signature was needed to establish relevance.

## Key Insight
- **Insight**: Because same-section IHC on the RNA-preserving (methanol-fixed, non-antigen-retrieved) Visium section gave inadequate staining quality, pairing each ST section with two flanking, independently and optimally fixed IHC sections (aligned back to the ST section via landmark registration) allows spot-level Aβ/GFAP/IBA1 intensity to be assigned to every ST spot without compromising RNA quality. This enables stratifying spots into a defined "plaque-glia niche" taxonomy (no/low/high Aβ crossed with glia-high/glia-low) and testing niche contrasts with adequately powered, donor-repeated-measures pseudobulk linear mixed models — revealing that low-Aβ (diffuse-plaque) and glia-high niches are the most neurotoxic, and that this in vivo signature is substantially recapitulated by Aβ-oligomer-treated iPSC-derived microglia alone.
- **Derived from**: O1, O3, O4, O5, O7.
- **Enables**: A spatially resolved, statistically powered framework linking classical neuropathology (plaque type, glial IHC) to spot-level transcriptomics, cell-type deconvolution, intercellular ligand-receptor inference, and an in vitro (iPSC) causal follow-up system — generalizable to other spatial pathology-transcriptomics questions in neurodegeneration.

## Assumptions
- A1: Aβ/GFAP/IBA1 IHC intensity measured on the two sections immediately adjacent to (above/below) the sequenced ST section faithfully represents the pathology present within each 55-µm ST spot of the middle section, after landmark-based image alignment (partially validated by a reported GFAP-gene-expression vs. GFAP-protein-intensity correlation, Supplementary Fig. 5A-B; validation figure not included in the provided PDF).
- A2: The manually derived intensity cutoffs (log2(avg Aβ intensity+1): no Aβ 2.5-4, low Aβ 4-6.5, high Aβ >6.5; glia-high: IBA1 >6.8 and/or GFAP >7.2; glia-low: IBA1 <6.2 and GFAP <6.5), calibrated on a manually annotated subset of 781 plaques, generalize across all 78 sections/21 donors.
- A3: Section-level pseudobulk aggregation (summing UMI counts of all spots of a given niche type per section) adequately represents niche-specific expression for linear-mixed-model contrasts, despite discarding spot-level heterogeneity within a niche/section.
- A4: Gene modules defined in mouse AD models (PIG, OLIG, DAM, DAA) and human-brain-derived microglial states (MG0-MG12, defined from dissociated snRNA-seq, not spatial data) are valid reference genesets for interpreting human ST niche-level differential expression via GSEA.
- A5: A 24-hour Aβ-oligomer exposure of a two-cell-type (iMGL + astrocyte/neuron) iPSC co-culture is sufficient to elicit a transcriptional response comparable to the chronic, multicellular in vivo plaque-glia niche.
