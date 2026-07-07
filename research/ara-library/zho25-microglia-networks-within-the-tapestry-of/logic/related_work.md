# Related Work

> This review's citation footprint spans 162 references. Full typed blocks (`RW`) are given for the
> works that carry a specific, load-bearing technical delta used in the claims above; the remainder
> of the footprint (platform-origin papers, disease-model papers, and background/context citations)
> is captured in the summary tables that follow, grouped by role.

## RW01: Chen WT et al. — Spatial Transcriptomics and In Situ Sequencing to Study Alzheimer's Disease (Cell, 2020) [ref. 79/43 in text]
- **Relationship**: imports (foundational finding — defines PIGs, directly underlies C04, C05 context, and is a same-first-author companion analysis to the plaque-niche masking protocol described in the text)
- **Delta this paper takes**: The 57-PIG gene set, the 50 μm plaque-mask protocol, and the finding that oligodendrocyte gene modules are upregulated early (e.g., 3 months in AppNL−G−F mice) but decrease within the immediate plaque niche as plaque load increases (paper.pdf p.7: "while oligodendrocyte modules are upregulated early (e.g., at 3 months in AppNL−G−F mice), they decrease within the immediate plaque niche").
- **Used for claims**: C04

## RW02: Zeng H et al. — Integrative in situ mapping of single-cell transcriptional states and tissue histopathology in a mouse model of Alzheimer's disease (Nat Neurosci, 2023) [ref. 81]
- **Relationship**: imports (STARmap Plus distance-graded cell-type enrichment findings around plaques; also imports the DAA-like astrocyte characterization; also cited as evidence for accelerated aging in AD via DAM enrichment, per Sun ED et al.'s cross-dataset application)
- **Delta this paper takes**: The 2,766-RNA-species panel, 13-major-cell-type classification, distance-binned enrichment (microglia at 10/10–20 μm; other glia at 10–30 μm; oligodendrocytes at 20–40 μm; OPCs at 10–30 μm in late AD), and the 14% DAA-like astrocyte fraction with 10–40 μm intermediate-distance enrichment.
- **Used for claims**: C05, C06

## RW03: Mallach A et al. — Microglia-astrocyte crosstalk in the amyloid plaque niche of an Alzheimer's disease mouse model, as revealed by spatial transcriptomics (Cell Rep, 2024) [ref. 84]
- **Relationship**: imports (receptor-ligand interaction quantification method and findings)
- **Delta this paper takes**: The 130-candidate-pair RL interaction set (11 overlapping with PIGs), the distance-dependent interaction-strength finding, and the region-specific astrocytic response (hippocampal astrocytes: Itm2b/Cpe/C1qa; cortical astrocytes: Atp1a1/Ckb/Kcnip4) plus the GABA/glutamate-signaling shift between astrocytes and CA1–CA3/dentate gyrus neurons.
- **Used for claims**: C07

## RW04: Roy ER et al. — Concerted type I interferon signaling in microglia and neural cells promotes memory impairment associated with amyloid beta plaques (Immunity, 2022) [ref. 88]
- **Relationship**: imports (cell-type-specific Ifnar1 knockout phenotypes and the interferon-responsive DAM fraction)
- **Delta this paper takes**: The "half of Clec7a+ DAMs are interferon-responsive" finding and the divergent microglial-vs-neuronal Ifnar1 deletion phenotypes on synaptic terminals and plaque burden.
- **Used for claims**: C08

## RW05: Allen WE, Blosser TR, Sullivan ZA, Dulac C, Zhuang X — Molecular and spatial signatures of mouse brain aging at single-cell resolution (Cell, 2023) [ref. 116]
- **Relationship**: imports (activation-score methodology and gene panel)
- **Delta this paper takes**: The 421-gene MERFISH panel, the 11-gene microglia / 8-gene astrocyte activation-score gene sets, and the finding that aged-animal-enriched glial clusters correlate with adjacent oligodendrocyte inflammation.
- **Used for claims**: C10

## RW06: Sun ED et al. — Spatial transcriptomic clocks reveal cell proximity effects in brain ageing (Nature, 2024) [ref. 118]
- **Relationship**: imports (Spatial Ageing Clock method and cross-dataset proximity-effect findings)
- **Delta this paper takes**: The 300-gene MERFISH panel-based aging clock, the microglia-accelerates-neighbor-aging finding (replicated across LPS, EAE, localized-injury, and AD datasets), and the NSC-rejuvenates-neighbors finding with Cd9 immunostaining validation.
- **Used for claims**: C11

## RW07: Androvic P et al. — Spatial transcriptomics-correlated electron microscopy maps transcriptional and ultrastructural responses to brain injury (Nat Commun, 2023) [ref. 115]
- **Relationship**: imports (combined MERFISH + EM method and foamy-microglia characterization)
- **Delta this paper takes**: The "foamy" microglia morphological/molecular definition (DAM signature + Plin2/Soat1/Abca1/Abcg1 lipid-metabolism genes) and its spatial proximity to interferon-responsive microglia, oligodendrocytes, astrocytes, and CD8+ T cells in LPC-induced remyelination lesions.
- **Used for claims**: C12

## RW08: Keren-Shaul H et al. — A Unique Microglia Type Associated with Restricting Development of Alzheimer's Disease (Cell, 2017) [ref. 69]
- **Relationship**: imports (defines DAM state and marker genes used throughout the review)
- **Delta this paper takes**: The DAM gene signature (Clec7a, B2m, Apoe, Trem2, Tyrobp, Cst7, Lpl) used as the reference activation program against which ARM, MGnD, and PIG findings are compared.
- **Used for claims**: C03, C04

## RW09: Krasemann S et al. — The TREM2-APOE Pathway Drives the Transcriptional Phenotype of Dysfunctional Microglia in Neurodegenerative Diseases (Immunity, 2017) [ref. 63]
- **Relationship**: imports (defines MGnD state)
- **Delta this paper takes**: The MGnD phenotype and its association with neuritic dystrophy across multiple neurodegeneration models (AD, ALS, MS).
- **Used for claims**: C03

## RW10: Sala Frigerio C et al. — The major risk factors for Alzheimer's disease: age, sex, and genes modulate the microglia response to Abeta plaques (Cell Rep, 2019) [ref. 62]
- **Relationship**: imports (defines ARM state)
- **Delta this paper takes**: The ARM phenotype in AD pathology mouse models, contributing to the DAM/ARM/MGnD convergence argument in C03.
- **Used for claims**: C03

## RW11: Safaiyan S et al. — White matter aging drives microglial diversity (Neuron, 2021) [ref. 114]
- **Relationship**: imports
- **Delta this paper takes**: The white-matter-microglia transcriptomic signature (DAM/MHC-II-related genes, 3–5-cell clustering morphology) that motivates the aging-brain section's white-matter focus.
- **Used for claims**: C10 (context), logic/problem.md

## RW12: Masuda T et al. — Spatial and temporal heterogeneity of mouse and human microglia at single-cell resolution (Nature, 2019) [ref. 59]
- **Relationship**: imports
- **Delta this paper takes**: Demyelination-associated microglia gene signature (Fam20c, Cst7, Ccl6, Fn1, Ank, Psat1, Spp1) and its conservation across mouse and human/MS tissue; contributes to the regional/functional heterogeneity baseline in C02–C03.
- **Used for claims**: C02, C03

## RW13: De Biase LM et al. — Local Cues Establish and Maintain Region-Specific Phenotypes of Basal Ganglia Microglia (Neuron, 2017) [ref. 57]
- **Relationship**: imports
- **Delta this paper takes**: Basal-ganglia-specific microglial anatomical features and their correlation with local astrocyte abundance, supporting the regional heterogeneity claim (C02).
- **Used for claims**: C02

## RW14: Ayata P et al. — Epigenetic regulation of brain region-specific microglia clearance activity (Nat Neurosci, 2018) [ref. 58]
- **Relationship**: imports
- **Delta this paper takes**: Cerebellum-specific elevated basal clearance activity correlated with cerebellar neuronal attrition, a second regional-heterogeneity data point for C02.
- **Used for claims**: C02

## Platform/technology-origin papers (brief entries — imports, technology basis for C01)
- **Stahl PL et al.** — Visualization and analysis of gene expression in tissue sections by spatial transcriptomics (Science, 2016) [ref. 43]: introduced the founding seq-ST concept of immobilized capture oligonucleotides on a chip, ancestor of 10x Visium.
- **Rodriques SG et al.** — Slide-seq (Science, 2019) [ref. 44]: DNA-barcoded bead-based seq-ST, ~10 μm resolution.
- **Liu Y et al.** — DBiT-seq (Cell, 2020) [ref. 45]: microfluidic-channel barcoding for multi-omic spatial profiling.
- **Chen A et al.** — Stereo-seq (Cell, 2022) [ref. 46]: DNA-nanoball-based seq-ST, ~220 nm resolution.
- **Lee JH et al.** — FISSEQ (Science, 2014) [ref. 47]: RCA-based in situ sequencing, ~100–200 nm resolution, ~100–200 transcripts/cell.
- **Chen KH et al.** — MERFISH (Science, 2015) [ref. 35]: combinatorial-barcode img-ST with Hamming-distance-4 error correction.
- **Shah S, Lubeck E, Zhou W, Cai L** — seqFISH (Neuron, 2016) [ref. 36]: pseudocolor combinatorial-fluorophore img-ST.
- **Eng CL et al.** — seqFISH transcriptome-scale (Nature, 2019) [ref. 37]: extended seqFISH multiplexing.
- **Wang X et al.** — STARmap (Science, 2018) [ref. 42]: in situ sequencing with 150 μm tissue-thickness capability.

## Baseline/disease-model papers cited for microglial state nomenclature (bounds — define the terms C03 depends on distinguishing)
- **Masuda T et al. (2019)** [ref. 59] and **Paolicelli RC et al.** — Microglia states and nomenclature: a field at its crossroads (Neuron, 2022) [ref. 60]: frames the DAM/ARM/MGnD naming inconsistency the review's C03 synthesis addresses.

## Human-AD extension papers (baseline/comparison — support the human-vs-mouse-model gap in logic/problem.md)
- **Miyoshi E et al.** — Spatial and single-nucleus transcriptomic analysis of genetic and sporadic forms of Alzheimer's disease (Nat Genet, 2024) [ref. 138]
- **Gong Y et al.** — Stereo-seq of the prefrontal cortex in aging and Alzheimer's disease (Nat Commun, 2025) [ref. 139]
- **van Olst L et al.** — Microglial mechanisms drive amyloid-beta clearance in immunized patients with Alzheimer's disease (Nat Med, 2025) [ref. 140]
- **Maynard KR et al.** — Transcriptome-scale spatial gene expression in the human dorsolateral prefrontal cortex (Nat Neurosci, 2021) [ref. 135]
- **Chen S et al.** — Spatially resolved transcriptomics reveals genes associated with the vulnerability of middle temporal gyrus in Alzheimer's disease (Acta Neuropathol Commun, 2022) [ref. 136]

## Future-directions / complementary-modality papers (baseline — motivate C13/C14 and the review's Conclusions)
- **Fang R et al.** and **Gandin V et al.** — 3D/deep-tissue single-cell transcriptome imaging (Elife 2024 [ref. 141]; Science 2025 [ref. 142]): proposed next step for 3D spatial cellular network mapping.
- **Li Y et al.** — Microglial lipid droplet accumulation in tauopathy brain regulated by neuronal AMPK (Cell Metab, 2024) [ref. 143]: motivates Raman-scattering metabolic imaging as a future direction.
- **Bintu B et al.; Lu T et al.; Deng Y et al.; Zhang D et al.; Su JH et al.** [refs. 145–149]: spatial epigenomics methods proposed as the necessary parallel development to spatial transcriptomics.
- **Boutej H et al.** — Diverging mRNA and protein networks in activated microglia (Cell Rep, 2017) [ref. 150]: source of the mRNA-protein dissociation finding in C14.
- **Mrdjen D et al.; Gholampour M et al.; Kumar P et al.; Vijayaragavan K et al.; Walker JM et al.** [refs. 154, 157, 155, 156, 158]: spatial-proteomics platforms cited in C13 as corroborating ST-derived microglial subsets.
