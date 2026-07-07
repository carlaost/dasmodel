# Claims

> Grounding: full-text PDF (14 pages) plus visually extracted figures. This is a narrative review;
> claims are the review's synthesized findings from cited primary literature, not new primary results
> of Zhou & Glass. Every load-bearing number is grounded to a verbatim quote from `paper.pdf`, cited by
> page number (the PDF carries no line numbers). `[result]` tags mark values the review reports as an
> empirical finding from a cited study; `[input]` tags mark values that describe a fixed technology
> spec (e.g., a platform's resolution).

## C01: img-ST and seq-ST platforms trade off resolution, throughput, and gene-panel flexibility
- **Statement**: Imaging-based spatial transcriptomics (img-ST: MERFISH, seqFISH, STARmap/ISS) achieves sub-cellular to single-molecule resolution but requires a pre-selected gene panel, whereas sequencing-based spatial transcriptomics (seq-ST: Visium ~50 μm, Slide-seq ~10 μm, Visium HD ~2 μm, Stereo-seq ~220 nm) captures the whole transcriptome at a range of spot resolutions from tens of micrometers down to sub-micrometer scale.
- **Status**: supported
- **Falsification criteria**: The primary img-ST/seq-ST platform papers report gene-panel-free whole-transcriptome imaging at single-molecule resolution, or report seq-ST spot sizes that do not fall in the 50 μm–220 nm range cited.
- **Proof**: [E01]
- **Evidence basis**: Platform resolution and panel-size values are stated directly in the technology-overview section and in Fig. 2's grid overlay.
- **Interpretation**: No single current ST platform simultaneously achieves whole-transcriptome coverage and sub-micrometer resolution; platform choice for AD spatial-niche studies is a resolution/coverage trade-off.
- **Sources**:
  - "resolution of about 50 μm" (Visium) ← paper.pdf p.3 «ture with a resolution of about 50 μm (Fig. 2B and D)» [input]
  - "resolution of about 10 µm" (Slide-seq) ← paper.pdf p.5 «with the resolution of about 10 µm [44] (Fig. 2C)» [input]
  - "approximately 220 nm" (Stereo-seq) ← paper.pdf p.5 «imaging spots down to approximately 220 nm [46]» [input]
  - "minimum Hamming distance of 4" (MERFISH) ← paper.pdf p.2 «Hamming distance of 4 between barcodes, thereby providing robust error correction across several rounds of hybridization [35]» [input]
  - "2,000 and 6,000 RNA species" (CosMx) ← paper.pdf p.2 «similar systems like CosMx developed by NanoString may resolve between 2,000 and 6,000 RNA species» [input]
  - "over 2000 mRNA species" (MERFISH platforms) ← paper.pdf p.2 «platforms using MERFISH method have demonstrated the imaging of over 2000 mRNA species imaging» [input]
  - FISSEQ "100–200 nm" resolution / "100–200 transcripts per cell" ← paper.pdf p.5 «FISSEQ can achieve subcellular resolution (around 100–200  nm), though its sensitivity is limited to detecting approximately 100–200 transcripts per cell under standard experimental conditions [47]» [input]
- **Dependencies**: none
- **Tags**: spatial transcriptomics, img-ST, seq-ST, resolution, platform comparison

## C02: Microglia are broadly distributed but regionally heterogeneous in density
- **Statement**: Microglia constitute approximately 4–10% of central nervous system cells and are more widely distributed than region-restricted neurons, yet exhibit a brain-wide density gradient: similar density in cortex, striatum, and hippocampus; roughly half that density in thalamus and midbrain; and lower density still in cerebellum.
- **Status**: supported
- **Falsification criteria**: Cited regional dissection/scRNAseq studies show uniform microglial density across brain regions, or report a different rostral-caudal/density gradient.
- **Proof**: [E02]
- **Evidence basis**: The 4–10% figure and the regional density comparison are both stated directly in the "Microglia regional and functional heterogeneity" section.
- **Interpretation**: Microglial regional heterogeneity is a baseline structural fact the review uses to motivate why spatial (not just dissociated) profiling of microglia is necessary.
- **Sources**:
  - "approximately 4–10%" ← paper.pdf p.5 «microglia are widely distributed throughout the brain, constituting approximately 4–10% of central nervous system cells [48]» [result]
  - regional density gradient ← paper.pdf p.5 «Similar densities of microglia are found in the cortex, striatum, and hippocampus, whereas the thalamus and midbrain exhibit nearly half the density, and the cerebellum even lower.» [result]
- **Dependencies**: none
- **Tags**: microglia, regional heterogeneity, density

## C03: DAM, ARM, and MGnD are convergent, overlapping microglial activation states
- **Statement**: Disease-associated microglia (DAM, identified in 5xFAD/APP-PS1 mice), activated response microglia (ARM, identified in AD mouse models), and the microglial neurodegenerative phenotype (MGnD, identified in ALS/MS/neurodegeneration models) were each discovered independently but "share many similar signatures," with DAM markers including Clec7a, B2m, Apoe, Trem2, Tyrobp, Cst7, and Lpl.
- **Status**: supported
- **Falsification criteria**: The cited primary scRNAseq studies for DAM/ARM/MGnD report non-overlapping gene signatures, or the states are shown to be model/context-specific with no shared core program.
- **Proof**: [E03]
- **Evidence basis**: Direct statement in the microglia heterogeneity section, with named marker genes.
- **Interpretation**: A convergent disease-associated activation program appears across multiple neurodegeneration models rather than being AD-specific, suggesting a general microglial injury-response module later co-opted by the amyloid plaque niche.
- **Sources**:
  - DAM marker genes ← paper.pdf p.5 «Following activation, microglia upregulate a suite of genes that define DAMs, such as Clec7a, B2m, Apoe, Trem2, and its adaptor Tyrobp, as well as genes involved in phagocytosis and lipid metabolism like Cst7 and Lpl» [result]
  - shared signatures statement ← paper.pdf p.5 «Notably, ARMs and MGnDs share many similar signatures with DAMs.» [result]
- **Dependencies**: C02
- **Tags**: DAM, ARM, MGnD, microglia activation, gene signature

## C04: Plaque-induced genes (PIGs) define a 57-gene multicellular co-expression network around amyloid plaques
- **Statement**: The first ST study in AD, using a seq-ST method with a 100 μm spot imaging size in the AppNL−G−F mouse model and a 50 μm plaque-niche mask around Aβ staining, identified 57 plaque-induced genes (PIGs) that are strongly associated with DAMs and inflammatory astrocytes; while PIG expression is primarily microglia-driven, several PIGs are expressed across multiple cell types.
- **Status**: supported
- **Falsification criteria**: The founding PIG study (ref. 43/Chen WT et al., Cell 2020) reports a different PIG count, a different masking distance, or shows PIGs are exclusively microglia-restricted with no cross-cell-type expression.
- **Proof**: [E04]
- **Evidence basis**: Exact PIG count, spot size, and masking distance stated directly; cross-cell-type PIG expression is separately confirmed by an img-ST in situ sequencing follow-up study.
- **Interpretation**: PIGs represent the first spatially defined, quantitatively bounded molecular signature of the amyloid plaque niche, establishing microglia as the dominant but not exclusive driver of the local transcriptional response.
- **Sources**:
  - "57 different PIGs" / "100 μm" spot / "50 μm masking area" ← paper.pdf p.6 «The plaque cellular niche was defined by expanding a 50 μm masking area of the Ab staining boundary. Using a seq-ST method of a spot imaging size of 100 μm in the AppNL−G−F mouse model, with adjacent brain tissue staining with Aß, 57 different PIGs were identified [43]» [result]
  - cross-cell-type PIG examples (Cyba, Cd9, H2-K1, Ly86, Mpeg1, Lgmn, Ctsa) ← paper.pdf p.6–7 «Cyba is present in both microglia and oligodendrocytes, and Cd9 is expressed in astrocytes, microglia, and oligodendrocytes. Some inflammatory molecules (e.g., H2-K1, Ly86, and Mpeg1) and lysosomal enzymes (e.g., Lgmn and Ctsa) are detected in both microglia and neurons.» [result]
- **Dependencies**: C03
- **Tags**: PIGs, amyloid plaque niche, AppNL-G-F, seq-ST

## C05: Microglia are the most plaque-proximal cell type, with other glia peaking at greater distances
- **Statement**: In an img-ST (STARmap Plus) study of the TauPS2APP mouse model that simultaneously profiled 2,766 RNA species across 13 major cell types, microglia were the most enriched population within the first 10 μm and 10–20 μm regions surrounding amyloid plaques, whereas astrocytes, oligodendrocytes, OPCs, and endothelial cells peaked in a 10–30 μm zone; oligodendrocyte clusters were specifically enriched at 20–40 μm and OPCs at 10–30 μm in late AD stages.
- **Status**: supported
- **Falsification criteria**: The cited STARmap Plus study (ref. 81/Zeng H et al., Nat Neurosci 2023) shows a different cell type as the closest-plaque-proximal population, or reports overlapping (non-graded) distance enrichment across cell types.
- **Proof**: [E05]
- **Evidence basis**: Distance bands and RNA-species/cell-type counts are stated directly.
- **Interpretation**: The amyloid plaque niche is spatially graded by cell type — microglia dominate the innermost shell, other glia occupy progressively outer shells — consistent with a sequential or role-differentiated cellular response to plaque pathology.
- **Sources**:
  - "2,766 RNA species" / "13 major cell types" ← paper.pdf p.7 «simultaneously profiled 2,766 RNA species alongside antibody staining for amyloid and phosphorated-tau [81]. Among the 13 major cell types, microglia, astrocytes, oligodendrocytes, oligodendrocyte precursor cells (OPC) and endothelial cells showed relative enrichment in the vicinity of plaques.» [result]
  - "10 μm and 10–20 μm" microglia / "10–30 μm" other glia ← paper.pdf p.7 «Microglia were the most enriched population within the first 10 μm and 10–20 μm regions surrounding plaques, whereas other glia populations peaked in a 10–30 μm zone.» [result]
  - "20–40 μm" oligodendrocytes / "10–30 μm" OPCs ← paper.pdf p.7 «distinct oligodendrocyte clusters are enriched 20–40 μm distance from plaques, and OPCs are notably enriched within 10–30 μm from plaques in late AD stages» [result]
- **Dependencies**: C04
- **Tags**: STARmap Plus, TauPS2APP, plaque distance gradient, microglia, oligodendrocytes, OPC

## C06: Disease-associated astrocytes (DAA) are ~14% of the astrocyte population and enriched at an intermediate distance from plaques
- **Statement**: In the cortex and hippocampus of TauPS2APP mice, DAA-like cells account for about 14% of all astrocyte populations, are enriched at an intermediate distance (10–40 μm) from amyloid plaques, and are marked by Gfab, Vim, and Ctsb expression.
- **Status**: supported
- **Falsification criteria**: The cited study (ref. 81) reports a substantially different DAA-like fraction of the astrocyte population, or shows DAA-like cells enriched immediately adjacent to (not at intermediate distance from) plaques.
- **Proof**: [E05]
- **Evidence basis**: Percentage, distance band, and marker genes stated directly.
- **Interpretation**: Astrocyte reactivity around plaques is spatially offset from the microglial response, consistent with a sequential or paracrine-relay model of glial activation.
- **Sources**:
  - "about 14% of all astrocyte populations" / "10–40 μm" / Gfab, Vim, Ctsb ← paper.pdf p.7 «DAA-like cells account for about 14% of all astrocyte populations, they are enriched around plaques at an intermediate distance (10–40 μm), and are marked by expression of Gfab, Vim and Ctsb genes [81]» [result]
- **Dependencies**: C05
- **Tags**: DAA, astrocytes, TauPS2APP, plaque distance

## C07: Microglia-astrocyte receptor-ligand crosstalk strengthens with proximity to plaques
- **Statement**: Receptor-ligand (RL) interaction analysis of img-ST/seq-ST data (CosMx and Stereo-seq) identified 130 candidate microglia-astrocyte RL pairs, of which 11 are PIGs; the strength of these interactions — including microglia-to-microglia signals (Csf1-Csf1r, Cd44-Tyrobp) and astrocyte-to-microglia crosstalk (astrocytic Cd44/Clu/Apoe with microglial Tyrobp/Trem2) — increases as cells approach the plaque.
- **Status**: supported
- **Falsification criteria**: The cited study (ref. 84/Mallach A et al., Cell Rep 2024) reports a different candidate-pair count, or shows RL interaction strength is invariant with (or decreases with) distance from plaque.
- **Proof**: [E06]
- **Evidence basis**: Pair counts and named ligand-receptor genes stated directly.
- **Interpretation**: Microglia-astrocyte signaling is not merely co-localized but graded in strength by physical proximity to the amyloid lesion, supporting a model where the plaque acts as a diffusible or contact-dependent signaling source.
- **Sources**:
  - "130 candidate pairs" / "11 of them are PIGs" ← paper.pdf p.7 «analysis of receptor-ligand (RL) interactions identified 130 candidate pairs between microglia and astrocytes, and 11 of them are PIGs» [result]
  - distance-dependent strength / named RL pairs ← paper.pdf p.7 «The strength of these interactions, including microglia-to-microglia signals (e.g., Csf1 to Csf1r and Cd44 to Tyrobp) and astrocyte-to-microglia crosstalk (e.g., astrocytic Cd44, Clu, Apoe with microglial Tyrobp and Trem2), increases as cells approaching plaques [84]» [result]
- **Dependencies**: C04, C06
- **Tags**: receptor-ligand interactions, microglia-astrocyte crosstalk, CosMx, Stereo-seq

## C08: Interferon-I (IFN-I) signaling mediates microglia-neuron crosstalk and bidirectionally controls synapse loss and plaque accumulation
- **Statement**: About half of Clec7a+ DAMs are interferon-responsive in 5xFAD mice; microglial Ifnar1 deletion near plaques reduces post-synaptic terminal loss by mitigating selective synaptic engulfment, whereas neural Ifnar1 deletion restores pre-synaptic terminals and decreases plaque accumulation.
- **Status**: supported
- **Falsification criteria**: The cited study (ref. 88/Roy ER et al., Immunity 2022) reports no interferon-responsive subset among DAMs, or shows cell-type-specific Ifnar1 deletion has no differential effect on pre-/post-synaptic terminal loss or plaque burden.
- **Proof**: [E07]
- **Evidence basis**: The interferon-responsive DAM fraction and the cell-type-specific Ifnar1 knockout phenotypes are stated directly.
- **Interpretation**: IFN-I signaling is a bidirectional, cell-type-specific node in the microglia-neuron interaction network: it drives detrimental synaptic engulfment when acting in microglia, but restrains plaque accumulation when acting in neurons — making it "a critical module within the neuroinflammatory network of AD" (paper.pdf p.7).
- **Sources**:
  - "half of the Clec7a + DAMs are Interferon responsive" ← paper.pdf p.7 «This study showed that half of the Clec7a + DAMs are Interferon responsive in 5xFAD mice.» [result]
  - Ifnar1 cell-type-specific effects ← paper.pdf p.7 «Deletion of microglial Ifnar1 near plaques reduces post-synaptic terminal loss by mitigating selective engulfment, whereas neural Ifnar1 deletion restored pre-synaptic terminals and decreased plaque accumulation.» [result]
- **Dependencies**: C04
- **Tags**: interferon signaling, Ifnar1, synaptic loss, microglia-neuron crosstalk

## C09: p-tau-proximal neuronal identity shifts from cortical to hippocampal excitatory neurons between 8 and 13 months in the TauPS2APP model
- **Statement**: Using STAR-MAP to jointly visualize phosphorylated tau (p-tau) and microglia in TauPS2APP mice, the majority of p-tau+ neurons at 8 months were CTX-Ex2 excitatory neurons, while by 13 months the majority were CA1 excitatory neurons of the hippocampus; inhibitory neurons accounted for less than 20% of p-tau+ neurons at both time points (mostly Pvalb neurons at 8 months, mostly Sst neurons at 13 months), and oligodendrocytes were the most substantially enriched cell type near high p-tau signal in the corpus callosum and hippocampus.
- **Status**: supported
- **Falsification criteria**: The cited STAR-MAP study reports a stable (non-shifting) p-tau+ neuronal subtype composition across the 8-to-13-month window, or shows inhibitory neurons exceeding 20% of the p-tau+ population.
- **Proof**: [E08]
- **Evidence basis**: Time-point-specific cell-type compositions are stated directly for both excitatory and inhibitory p-tau+ neuron populations.
- **Interpretation**: The identity of tau-vulnerable neurons is not fixed but progresses spatially and temporally with disease stage, tracking the spread of pathology from cortex to hippocampus.
- **Sources**:
  - 8-month vs. 13-month excitatory neuron identity ← paper.pdf p.8 «At 8 months, the majority of p-tau + neurons were CTX-Ex2 excit­atory neurons, whereas at 13 months, the majority of p-tau + neurons were the CA1 excitatory neurons of the hippocampus.» [result]
  - "< 20% of p-tau + neurons" inhibitory / Pvalb vs. Sst shift ← paper.pdf p.8 «Inhibitory neurons account for < 20% of p-tau + neurons, most of them were Pvalb neurons at 8 months, whereas at 13 months, most of them came from the Sst population.» [result]
- **Dependencies**: none
- **Tags**: p-tau, STAR-MAP, TauPS2APP, vulnerable neurons, disease progression

## C10: A curated 11-gene microglia / 8-gene astrocyte panel defines a spatial "activation score" that tracks aging and correlates with adjacent oligodendrocyte inflammation
- **Statement**: Using a 421-gene MERFISH panel in the aging mouse frontal cortex and striatum, an "activation score" computed from 11 microglia genes (B2m, Trem2, Ccl2, Apoe, Axl, Itgax, Cd9, C1qa, C1qc, Lyz2, Ctss) and 8 astrocyte genes (C4b, C3, Serpina3n, Cxcl10, Gfap, Vim, Il18, Hif3a) showed that astrocytic and microglial clusters enriched in aged animals correlated with the inflammation level of adjacent oligodendrocytes.
- **Status**: supported
- **Falsification criteria**: The cited study (ref. 116/Allen WE et al., Cell 2023) reports the activation score is uncorrelated with age or with oligodendrocyte inflammation state.
- **Proof**: [E09]
- **Evidence basis**: The exact gene panel size and gene lists are stated directly, along with the correlation finding.
- **Interpretation**: Glial activation in the aging brain is a spatially coupled, multicellular phenomenon rather than an independent, cell-autonomous process in each glial type.
- **Sources**:
  - "421 genes" MERFISH panel ← paper.pdf p.9 «One study using a panel of MERFISH probes targeting 421 genes calculated an 'activation score' in the mouse frontal cortex and stratum of aging brains [116].» [result]
  - gene lists (microglia and astrocyte) ← paper.pdf p.9 «The activation scores were calculated based on selected gene expressions of microglia (B2m, Trem2, Ccl2, Apoe, Axl, Itgax, Cd9, C1qa, C1qc, Lyz2, Ctss) and Astrocytes (C4b, C3, Serpina3n, Cxcl10, Gfap, Vim, Il18, and Hif3a).» [result]
  - correlation with oligodendrocyte inflammation ← paper.pdf p.9 «The data revealed that astrocytic and microglial clusters that are enriched in aged animals correlated with the inflammation level of adjacent oligodendrocytes.» [result]
- **Dependencies**: none
- **Tags**: aging, activation score, MERFISH, microglia, astrocytes, oligodendrocytes

## C11: A 300-gene "Spatial Ageing Clock" shows microglia accelerate neighbor cell aging while neural stem cells (NSCs) exert a rejuvenating proximity effect
- **Statement**: A 300-gene MERFISH panel used to build a per-cell "Spatial Ageing Clock" across the mouse lifespan predicts that microglia accelerate the aging of nearby cells; applying this clock to published ST datasets showed microglia, astrocytes, and oligodendrocytes exhibit accelerated aging in response to LPS and in AD (with DAM enrichment), while neural stem cells (NSCs) — localized to the lateral ventricles and declining with age — exert a pro-rejuvenating proximity effect on neighboring cells, evidenced by increased expression of the exocytosis marker Cd9 in NSC-adjacent cells (confirmed by immunostaining).
- **Status**: supported
- **Falsification criteria**: The cited study (ref. 118/Sun ED et al., Nature 2024) reports no directional proximity effect of microglia or NSCs on neighboring cell aging, or shows the clock's predictions do not replicate in independent LPS/AD/demyelination datasets.
- **Proof**: [E10]
- **Evidence basis**: The panel size, the microglia pro-aging effect, the NSC pro-rejuvenating effect, and the Cd9 immunostaining confirmation are all stated directly.
- **Interpretation**: Cell-intrinsic aging state is not purely autonomous; specific cell types (microglia, NSCs) actively modulate the aging trajectory of their spatial neighborhood in opposite directions, and this proximity effect generalizes across independent perturbation models (LPS, EAE, localized demyelination injury, AD).
- **Sources**:
  - "300 gene panel" / "Spatial Ageing Clock" ← paper.pdf p.9 «Another study using a 300 gene panel of MERFISH probes identified the 'Spatial Ageing Clock' of each cell in the brains of mice across the whole lifespan [118].» [result]
  - microglia accelerate neighbor aging ← paper.pdf p.9 «The 'Spatial Age­ing Clock' predicts that microglia accelerate the aging of nearby cells.» [result]
  - NSC pro-rejuvenating effect / Cd9 marker ← paper.pdf p.9 «Conversely, NSCs have a strong pro-rejuvenating proximity effect on neigh­boring cells. ... The neighboring cells of NSCs dis­played increased expression of the 'exocytosis' marker as Cd9, which was confirmed by immunostaining.» [result]
- **Dependencies**: C10
- **Tags**: spatial aging clock, microglia, NSC, proximity effect, MERFISH

## C12: Foamy microglia in remyelination lesions co-express DAM and lipid/cholesterol metabolism genes and localize near interferon-responsive microglia
- **Statement**: Combined MERFISH and electron microscopy in an LPC-induced white matter injury model identified "foamy" microglia at the center of remyelination lesions, expressing both DAM signature genes and lipid/cholesterol metabolism genes (Plin2, Soat1, Abca1, Abcg1); these foamy microglia are found in close proximity to interferon-responsive microglia (marked by Stat1, Ifit1, Usp18, Rsad2), oligodendrocytes, astrocytes, and CD8+ T cells.
- **Status**: supported
- **Falsification criteria**: The cited study (ref. 115/Androvic P et al., Nat Commun 2023) reports foamy microglia lack lipid-metabolism gene upregulation, or shows no spatial proximity between foamy and interferon-responsive microglia subsets.
- **Proof**: [E11]
- **Evidence basis**: Named genes for both the foamy and interferon-responsive microglia subsets, and their spatial co-localization, are stated directly.
- **Interpretation**: White-matter injury/remyelination produces at least two spatially adjacent, molecularly distinct microglial substates (lipid-handling "foamy" and interferon-responsive), suggesting functional specialization within the same lesion microenvironment.
- **Sources**:
  - foamy microglia genes ← paper.pdf p.8–9 «The foamy microglia, laden with lipid droplets, expressed not only DAM signatures but also genes involved in lipid and cholesterol metabo­lism (e.g., Plin2, Soat1, Abca1, and Abcg1).» [result]
  - spatial proximity to IFN-responsive microglia and other cell types ← paper.pdf p.8–9 «In the lesions, foamy microglia are found in close proximity with interferon-responsive microglia (enriched with Stat1, Ifit1, Usp18, and Rsad2), oligodendrocytes, astrocytes and CD8 + T-cells» [result]
- **Dependencies**: none
- **Tags**: foamy microglia, demyelination, remyelination, MERFISH, electron microscopy, DAM

## C13: Spatial proteomics platforms multiplex 30–60 protein targets at subcellular resolution, complementing spatial transcriptomics findings
- **Statement**: Imaging-based spatial proteomics platforms have advanced to multiplex the detection of 30–60 protein targets at subcellular resolution, and multiple such platforms have independently identified plaque-associated microglial subsets, reinforcing spatial transcriptomics findings.
- **Status**: supported
- **Falsification criteria**: The cited spatial proteomics platform papers report protein target counts outside the 30–60 range, or fail to replicate plaque-associated microglial subset findings from ST studies.
- **Proof**: [E12]
- **Evidence basis**: The protein-target multiplexing range is stated directly, along with the claim of convergent microglial-subset findings.
- **Interpretation**: Spatial proteomics is presented as a maturing, complementary modality that can independently corroborate ST-derived microglial state findings and partially address the mRNA-protein dissociation problem the review raises for AD microglia.
- **Sources**:
  - "30–60 protein targets" ← paper.pdf p.10 «particularly imaging-based protein-inclusive methods that multiplex the detection of 30–60 protein targets at subcellular resolution [154–158]» [input]
  - convergent microglial subset finding ← paper.pdf p.10 «multiple platforms have demonstrated microglial heterogeneity and identi­fied plaque-associated microglial subsets, reinforcing the findings from spatial transcriptomics studies [154, 157]» [result]
- **Dependencies**: none
- **Tags**: spatial proteomics, microglia, future directions

## C14: Elevated pro-inflammatory microglial mRNA does not necessarily track with corresponding protein abundance
- **Statement**: Following innate immune challenge, elevated levels of certain pro-inflammatory mRNAs do not necessarily correlate with their corresponding protein abundance, indicating a dissociation between microglial mRNA and protein networks likely driven by post-transcriptional and translational regulation.
- **Status**: supported
- **Falsification criteria**: The cited study shows pro-inflammatory mRNA and protein levels are tightly correlated following innate immune challenge.
- **Proof**: [E12]
- **Evidence basis**: Stated directly in the Conclusions/Future directions section.
- **Interpretation**: This is presented as a caveat that limits how far transcriptomic (including spatial transcriptomic) findings alone can be extrapolated to functional/protein-level microglial states, motivating the review's call for complementary spatial proteomics.
- **Sources**:
  - mRNA-protein dissociation ← paper.pdf p.10 «studies have shown that following innate immune challenge, elevated levels of certain pro-inflam­matory mRNAs do not necessarily correlate with their corresponding protein abundance, highlighting a disso­ciation between microglial mRNA and protein networks that is likely driven by post-transcriptional and transla­tional regulation [150]» [result]
- **Dependencies**: none
- **Tags**: mRNA-protein dissociation, translational regulation, limitations
