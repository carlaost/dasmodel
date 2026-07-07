# Concepts

## Spatial transcriptomics (ST)
A method to simultaneously measure transcripts at single-cell or near-single-cell resolution in a multiplexed manner, in situ, while preserving spatial tissue context. "Spatially resolved transcriptomic technology (ST) has emerged as a method to simultaneously measure transcripts at single-cell or near single-cell resolution in a multiplexed manner" (paper.pdf p.2). Broadly divided into imaging-based (img-ST) and sequencing-based (seq-ST) approaches.

## Imaging-based spatial transcriptomics (img-ST)
ST built on fluorescence in situ hybridization (FISH), using combinatorial barcoding and multiple imaging rounds to overcome the spectral-overlap multiplexing limit of traditional FISH. Provides sub-cellular resolution but requires a pre-selected gene panel (paper.pdf p.2–3). Includes MERFISH, seqFISH, and in situ sequencing (ISS) methods (STARmap, Xenium).

## Sequencing-based spatial transcriptomics (seq-ST)
ST that uses spatially barcoded oligonucleotide capture arrays or beads on mounted tissue sections to capture the entire transcriptome, trading sub-cellular resolution for whole-transcriptome coverage (paper.pdf p.3). Includes Visium, Slide-seq, Visium HD, Stereo-seq, DBiT-seq, and FISSEQ.

## MERFISH (Multiplexed Error-Robust FISH)
An img-ST method that assigns a unique combinatorial barcode to each mRNA species, designed with a minimum Hamming distance of 4 between barcodes for robust error correction across multiple hybridization rounds; commercialized as MERSCOPE by Vizgen (paper.pdf p.2, Fig. 1A).

## seqFISH
An img-ST method achieving multiplexing via combinatorial encoding barcodes plus multiple readout probes detected by different fluorophores across successive imaging rounds, generating a "pseudocolor" readout that identifies thousands of transcripts (paper.pdf p.2, Fig. 1B).

## In situ sequencing (ISS) / padlock probes
An img-ST approach in which padlock probes hybridize to cDNA by reverse transcription, circularize, and undergo rolling-circle amplification (RCA) to generate localized amplified products ("rolonies"); barcode sequences are then decoded by sequencing-by-ligation chemistry (paper.pdf p.2, Fig. 1C). STARmap and 10x Genomics Xenium are advanced/commercialized ISS platforms.

## STARmap / STARmap Plus
An ISS-based img-ST method (Spatially Resolved Transcript Amplicon Readout Mapping) that maps thousands of mRNAs in tissue sections up to 150 μm thick; STARmap Plus extends this to simultaneous profiling of RNA alongside antibody staining for amyloid and phosphorylated tau (paper.pdf p.2, p.7).

## Visium / Visium HD
A seq-ST platform using pre-defined capture spots on slides to collect mRNA while preserving tissue architecture, at a resolution of about 50 μm (Visium) down to about 2 μm (Visium HD) (paper.pdf p.3, Fig. 2B).

## Slide-seq
A seq-ST method using densely packed, DNA-barcoded beads deposited on a surface to capture transcripts from overlying tissue, achieving roughly 10 μm resolution (paper.pdf p.3, Fig. 2C).

## Stereo-seq
A seq-ST platform (BGI) using nanoball-DNA for mRNA detection, resolving imaging spots down to approximately 220 nm (paper.pdf p.3, Fig. 2E).

## DBiT-seq (Deterministic Barcoding in Tissue)
A seq-ST method that uses microfluidic channels to deliver barcodes directly onto tissue sections, enabling simultaneous profiling of multiple molecular layers at high spatial resolution (paper.pdf p.3).

## FISSEQ (Fluorescent In Situ Sequencing)
A method using RCA to generate localized amplicons subsequently sequenced by ligation or synthesis chemistry, achieving subcellular resolution (~100–200 nm) but limited in throughput (~100–200 transcripts per cell under standard conditions) (paper.pdf p.3).

## Disease-associated microglia (DAM)
A microglial activation state first identified by scRNAseq of sorted microglia in 5xFAD and APP/PS1 mice, marked by upregulation of genes including Clec7a, B2m, Apoe, Trem2, Tyrobp, Cst7, and Lpl, involved in phagocytosis and lipid metabolism (paper.pdf p.5).

## Activated response microglia (ARM)
A microglial state characterized in AD pathology mouse models that shares many signature genes with DAMs (paper.pdf p.5).

## Microglial neurodegenerative phenotype (MGnD)
A microglial state associated with neuritic dystrophy, observed across multiple neurodegeneration models (including ALS and multiple sclerosis) and sharing signatures with DAM/ARM (paper.pdf p.5).

## Plaque-induced genes (PIGs)
Multi-cellular co-expressed gene networks associated with amyloid plaques, first identified in the founding AD ST study; PIGs are primarily microglia-driven but some are expressed across multiple cell types (paper.pdf p.6–7).

## Disease-associated astrocytes (DAA)
A reactive astrocyte state with a characteristic gene signature (e.g., Gfap, Vim, Ctsb) found in AD patients and mouse models, implicated in a major transcriptional response to microglia (paper.pdf p.7).

## Amyloid plaque niche
The spatial microenvironment surrounding an amyloid plaque, operationalized in the literature as a distance-graded zone (e.g., 10/20/30/40 μm bands from the plaque boundary) within which glial and neuronal responses are measured (paper.pdf p.6–7, Fig. 3A).

## Receptor-ligand (RL) interaction analysis
A computational approach (applied to ST data) that identifies candidate ligand-receptor gene pairs between spatially co-located cell types and quantifies the distance-dependent strength of the inferred signaling interaction (paper.pdf p.7).

## Type I interferon (IFN-I) signaling module
A conserved microglial and neuronal transcriptional response (marked by genes such as Ifit3, Oasl2, Irf7, Stat1, Ifit1, Usp18, Rsad2) implicated as a mechanistic link between microglia-neuron crosstalk, synaptic loss, and memory impairment near plaques (paper.pdf p.5, p.7, p.9).

## Foamy microglia
A lipid-droplet-laden microglial morphological/transcriptional state located at the center of remyelination lesions, expressing DAM signatures plus lipid/cholesterol metabolism genes (Plin2, Soat1, Abca1, Abcg1), identified using combined MERFISH + electron microscopy (paper.pdf p.8–9).

## Activation score (aging)
A quantitative per-cell score computed from a curated panel of microglia genes (B2m, Trem2, Ccl2, Apoe, Axl, Itgax, Cd9, C1qa, C1qc, Lyz2, Ctss) and astrocyte genes (C4b, C3, Serpina3n, Cxcl10, Gfap, Vim, Il18, Hif3a), derived from a 421-gene MERFISH panel applied to aging mouse frontal cortex and striatum (paper.pdf p.9).

## Spatial Ageing Clock
A per-cell computational aging-prediction model built from a 300-gene MERFISH panel across the mouse lifespan, used to detect "proximity effects" — i.e., that a cell's predicted age is influenced by the identity of its spatial neighbors (paper.pdf p.9).

## Cell proximity effect
The phenomenon, identified via spatial aging clocks and related spatial analyses, whereby a cell's molecular/aging phenotype is measurably shaped by the identity and state of its spatially adjacent neighbor cells (e.g., microglia accelerate neighbor aging; neural stem cells (NSCs) exert a rejuvenating effect on neighbors) (paper.pdf p.9).
