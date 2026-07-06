# Concepts

## Plaque-glia niche
- **Notation**: —
- **Definition**: A local microenvironment containing both amyloid-beta (Aβ) deposition and reactive glia (astrocytes/microglia); the paper's central unit of analysis, operationalized as an ST spot (or set of spots) classified jointly by Aβ intensity (no/low/high) and glial intensity (glia-high/glia-low).
- **Boundary conditions**: Defined at the resolution of a Visium ST spot (~55 µm diameter), which typically contains multiple cells of mixed type; the paper notes this resolution is insufficient to separate astrocyte-specific from microglia-specific contributions within a "glia-high" spot.
- **Related concepts**: Aβ intensity stratification, Glia intensity stratification, Spatial transcriptomics.

## Spatial transcriptomics (ST) via 10x Genomics Visium
- **Notation**: —
- **Definition**: A spot-barcoded, spatially resolved RNA-sequencing platform (10x Genomics Visium Spatial Gene Expression, protocol CG000239) that captures whole-transcriptome gene expression while preserving each transcript's spatial (spot) coordinate within a tissue section; used here on 78 fresh-frozen DLPFC sections from 21 ROSMAP donors, yielding 258,987 spots.
- **Boundary conditions**: Each spot is ~55 µm in diameter and captures pooled transcripts from multiple cells; RNA-preserving fixation (methanol) precludes the antigen retrieval and extended immunostaining protocols needed for high-quality same-section IHC.
- **Related concepts**: Plaque-glia niche, IHC-ST alignment, Pseudobulk aggregation.

## IHC-ST adjacent-section alignment
- **Notation**: —
- **Definition**: The study's method for obtaining per-spot immunohistochemistry (IHC) intensity without compromising ST RNA quality: two sections immediately adjacent to (flanking) the sequenced ST section are separately fixed (PFA) and immunostained for Aβ (4G8), GFAP, and IBA1, then computationally registered to the ST section's H&E image via 7-12 manually placed landmark correspondences (ImageJ "Landmark Correspondences" plugin), after which per-spot average fluorescence intensity is computed for each stain.
- **Boundary conditions**: Requires that pathology in the adjacent (10-50 µm offset) sections is representative of the sequenced section; the paper attempted same-section IHC first and found it inadequate due to the RNA-preserving fixation protocol.
- **Related concepts**: Plaque-glia niche, Spatial transcriptomics.

## Aβ intensity stratification (no/low/high)
- **Notation**: log2(avg Aβ IHC intensity + 1)
- **Definition**: Classification of each ST spot into "no Aβ" (log2(avg intensity+1) in [2.5, 4), background fluorescence, primarily tissue-uncovered regions), "low Aβ" ([4, 6.5), diffuse-plaque-enriched), or "high Aβ" (>6.5, compact/dense-core-plaque-enriched), with cutoffs selected from manual scoring of 781 plaques such that the 6.5 threshold maximized the distinction between diffuse and compact/dense-core plaque types.
- **Boundary conditions**: Values below 2.5 were observed only in tissue-uncovered regions and excluded; thresholds were derived on frozen ST-adjacent sections and separately re-validated (top-25%/bottom-75% split) on an independent FFPE cohort.
- **Related concepts**: Plaque-glia niche, Glia intensity stratification, IHC-ST adjacent-section alignment.

## Glia intensity stratification (glia-high/glia-low)
- **Notation**: log2(avg IBA1 or GFAP IHC intensity + 1)
- **Definition**: Classification of ST spots as "glia-high" when log2(avg intensity+1) for IBA1 >6.8 and/or GFAP >7.2, and "glia-low" when both IBA1 <6.2 and GFAP <6.5; manual assessment indicated glia-high spots typically contain >4 glial cells (astrocytes and/or microglia) while glia-low spots contain ~0-4.
- **Boundary conditions**: Spots with intermediate GFAP/IBA1 intensity fall into neither category and are excluded from glia-stratified contrasts; stricter thresholds or single-positive-only stratification (e.g., GFAP+/IBA1- only) were tested but reduced the number of usable sections and thus statistical power, so were not adopted.
- **Related concepts**: Aβ intensity stratification, Plaque-glia niche.

## Pseudobulk aggregation and linear mixed model (LMM) contrast
- **Notation**: log2 CPM (TMM-voom normalized)
- **Definition**: For each brain section, UMI counts of all spots belonging to a given plaque-glia niche type are summed to form a pseudobulk expression estimate per gene; pseudobulk estimates across sections are normalized (TMM via edgeR, voom-limma), then contrasted between niche types using linear mixed models with niche type as a binary fixed effect, age/RIN/batch/AD-status as covariate fixed effects, and donor modeled as a random effect to account for within-subject correlation across the up-to-four sections per donor; significance declared at FDR<0.05.
- **Boundary conditions**: Applied only to gray-matter spots for niche contrasts involving glia stratification; brain sections with fewer than 50 spots in a given niche type were excluded from that contrast.
- **Related concepts**: Plaque-glia niche, GSEA.

## Gene set enrichment analysis (GSEA) with mouse/human glial gene modules
- **Notation**: normalized enrichment score (NES); signed −log10(p)
- **Definition**: GSEA (Subramanian et al. 2005) applied with per-gene t-values from niche-contrast LMMs as the ranking score and GO terms, canonical pathways, or curated glial gene sets (PIG, OLIG, DAM, DAA, and 12 human MG states MG0-MG12) as genesets, to test whether niche contrasts are enriched for pre-defined glial-activation programs.
- **Boundary conditions**: Mouse-derived modules (PIG/OLIG/DAM/DAA) and human-brain-derived microglial states (MG0-12) were both used as external reference genesets without re-derivation in this dataset; enrichment reflects concordance with, not independent discovery of, these programs.
- **Related concepts**: Plaque-induced genes (PIG), Disease-associated microglia (DAM), Disease-associated astrocytes (DAA), Human AD microglial states (MG0-MG12).

## Plaque-induced genes (PIG) / OLIG gene modules
- **Notation**: —
- **Definition**: Multicellular gene expression modules originally defined by spatial and temporal transcriptomics in mouse AD models (Chen et al. 2020): PIG (plaque-induced genes, reflecting astrocyte-microglia intercellular crosstalk near plaques) and OLIG (an oligodendrocyte-response gene module reported to be highly expressed in mild-Aβ domains but to decrease in dense-Aβ microenvironments).
- **Boundary conditions**: Defined in mouse tissue; used here as an external reference geneset for human ST GSEA, not re-derived.
- **Related concepts**: GSEA, Disease-associated microglia (DAM), Disease-associated astrocytes (DAA).

## Disease-associated microglia (DAM) / disease-associated astrocytes (DAA)
- **Notation**: —
- **Definition**: Transcriptionally distinct, disease-associated glial states originally defined in mouse AD models: DAM (Keren-Shaul et al. 2017), a microglial state restricting AD-pathology development; DAA (Habib et al. 2020), an astrocyte state associated with AD and aging.
- **Boundary conditions**: Mouse-derived reference gene sets; used here purely as GSEA genesets against human ST contrasts.
- **Related concepts**: Human AD microglial states (MG0-MG12), Plaque-induced genes (PIG).

## Human AD microglial states (MG0-MG12)
- **Notation**: MG0 (homeostatic), MG1 (neuronal surveillance), MG2-MG12 (various, including MG3 = "ribosome biogenesis"/DAM-like)
- **Definition**: Twelve transcriptionally defined microglial states identified from single-nucleus RNA-seq of human postmortem AD brains (Sun et al. 2023), used in this study as GSEA reference genesets to interpret both the in vivo ST glial response and the in vitro iMGL Aβ-response signature.
- **Boundary conditions**: Defined from dissociated snRNA-seq (no spatial information at their point of origin); this paper's contribution is testing which of these states are enriched in a spatially defined plaque-glia contrast and in an iPSC model, not redefining the states themselves.
- **Related concepts**: GSEA, Disease-associated microglia (DAM), iPSC-derived microglia-like cells (iMGL).

## Cell2location cell-type deconvolution
- **Notation**: normalized enrichment score (NES) per cell type per spot
- **Definition**: A Bayesian spatial cell-type deconvolution method (Kleshchevnikov et al. 2022) used to estimate the abundance of each of 8 (or, for finer annotation, 44) reference cell types (derived from a published ROSMAP DLPFC snRNA-seq dataset) within each ST spot, with enrichment of predicted abundance across spot clusters assessed via GSEA.
- **Boundary conditions**: Deconvolution estimates are reference-dependent (accuracy bounded by the quality/completeness of the snRNA-seq reference) and provide relative, not absolute, cell counts per spot.
- **Related concepts**: Spatial transcriptomics, Plaque-glia niche.

## NICHES ligand-receptor (LR) spatial signaling inference
- **Notation**: t-statistic per LR pair (from LMM contrasts)
- **Definition**: NICHES (Niche Interactions and Communication Heterogeneity in Extracellular Signaling; Raredon et al. 2023) infers local intercellular signaling by constructing, for each ST spot, a "niche matrix" summing ligand-receptor co-expression signal from Euclidean-neighboring spots (k=4 nearest neighbors), using the Omnipath LR reference database; per-spot LR values are averaged by section/stratification group and contrasted with mixed linear models.
- **Boundary conditions**: NICHES does not restrict to biochemically validated ligand-receptor pairs; it treats spatially co-expressed gene pairs between neighboring spots as *proxies* for potential (not confirmed) intercellular signaling. Only gray-matter spots from sections/strata with ≥50 spots were analyzed.
- **Related concepts**: Plaque-glia niche, Pseudobulk aggregation.

## iPSC-derived microglia-like cells (iMGL) and multicellular co-culture
- **Notation**: —
- **Definition**: Microglia-like cells differentiated from iPSCs (via hematopoietic progenitor intermediates, following Abud et al. 2017 / McQuade et al. 2018 protocols with minor modifications) and co-cultured with iPSC-derived astrocyte/neuron cultures (from a second iPSC line, BR28) for 72 h prior to a 24-h Aβ-oligomer (or vehicle) treatment, then profiled by scRNA-seq to identify cell-type-specific Aβ-responsive genes and cross-referenced by GSEA against the in vivo ST glial response.
- **Boundary conditions**: A simplified, two-iPSC-line, short-exposure (24 h) in vitro system; the paper notes cultured microglia are known to diverge transcriptionally from in vivo microglia absent brain-specific environmental cues (Gosselin et al. 2017; Cadiz et al. 2022).
- **Related concepts**: Human AD microglial states (MG0-MG12), GSEA.

## Batch/data-integration benchmarking (Harmony vs. alternatives)
- **Notation**: —
- **Definition**: A benchmarking procedure (scib snakemake pipeline) comparing 7 single-cell/spatial data-integration methods (Harmony, scANVI, fastMNN, ComBat, Seurat v3 RPCA, scVI, BBKNN), with and without highly-variable-gene selection and data scaling, on 16 representative sections from 4 individuals, scored on batch-correction metrics (PCR batch, graph iLISI, graph connectivity, kBET) and biological-conservation metrics (isolated-label F1, isolated-label silhouette, graph cLISI) combined in a 40/60 weighted mean.
- **Boundary conditions**: Benchmarking was performed on a 16-section subsample (not the full 78-section dataset) for computational tractability; Harmony was selected for downstream spot clustering only — all downstream differential-expression, cell-proportion, and ligand-receptor analyses used pre-integration (non-batch-corrected) count data.
- **Related concepts**: Spatial transcriptomics, Plaque-glia niche.
