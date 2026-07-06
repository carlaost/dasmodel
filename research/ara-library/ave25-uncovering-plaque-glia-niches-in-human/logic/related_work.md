# Related Work

## RW01: Chen et al., 2020 (bioRxiv preprint; PIG/OLIG gene modules)
- **DOI**: Not specified in paper (bioRxiv, cited as ref [30])
- **Type**: imports
- **Delta**:
  - What changed: Defined the plaque-induced gene (PIG) module and the oligodendrocyte (OLIG) response gene module from spatial and temporal transcriptomics of mouse AD models, and characterized microglia-astroglia crosstalk in the amyloid-β plaque cell niche.
  - Why: Provides multicellular, plaque-proximal gene-module definitions from a mouse spatial dataset that this paper tests for conservation in human ST data via GSEA.
- **Claims affected**: C04
- **Adopted elements**: PIG and OLIG gene sets used directly as GSEA reference genesets (Fig. 3F, 5F); the paper's interpretation that OLIG is high in mild-Aβ domains and decreases in dense-Aβ microenvironments is cited as concordant with this paper's own OLIG enrichment pattern.

## RW02: Keren-Shaul et al., 2017, *Cell* (Disease-associated microglia, DAM) [ref 31]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Defined the DAM microglial state in mouse AD models, characterized as restricting Aβ-pathology development.
  - Why: DAM gene signature used as an external reference geneset to test whether mouse-defined disease-associated microglial programs are enriched in the human ST glial response.
- **Claims affected**: C04
- **Adopted elements**: DAM gene set used directly in GSEA (Fig. 3F, 5F); MG3 human microglial state (this paper, via ref [8]) is explicitly described as "most resembling mouse DAM."

## RW03: Habib et al., 2020, *Nat Neurosci* (Disease-associated astrocytes, DAA) [ref 32]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Defined the DAA astrocyte state associated with AD and aging in mouse models.
  - Why: DAA gene signature used as an external reference geneset analogous to DAM but for astrocytes.
- **Claims affected**: C04
- **Adopted elements**: DAA gene set used directly in GSEA (Fig. 3F, 5F).

## RW04: Sun et al., 2023, *Cell* (Human microglial state dynamics in AD progression) [ref 8]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Defined 12 transcriptionally distinct human microglial states (MG0-MG12, including MG0 homeostatic, MG1 neuronal surveillance, MG3 "ribosome biogenesis"/DAM-like) from snRNA-seq of human postmortem AD brains.
  - Why: Provides the human-derived (rather than mouse-derived) microglial state taxonomy used as the primary GSEA reference for interpreting both the ST glial response and the iMGL in vitro response.
- **Claims affected**: C04, C08, C09
- **Adopted elements**: All 12 MG-state gene sets used directly as GSEA genesets (Fig. 3F, 5F, 7J); the MG3 state is repeatedly identified as the most-enriched state across all Aβ/glia/iMGL contrasts in this paper.

## RW05: Chen et al., 2022, *Acta Neuropathol Commun* (Spatially resolved transcriptomics, human MTG vulnerability) [ref 14]
- **DOI**: Not specified in paper
- **Type**: baseline / bounds
- **Delta**:
  - What changed: A prior human-brain ST study identifying altered co-expression patterns of gene modules near AD pathology, but "only comprised a handful of samples."
  - Why: Directly motivates this paper's rationale (Background) for generating a much larger (78-section, 21-donor), IHC-paired human ST dataset to achieve adequate statistical power.
- **Claims affected**: (motivates the paper's overall design; not tied to a specific numbered claim)
- **Adopted elements**: None directly reused; cited as the prior state of the art this paper extends in scale and IHC pairing.

## RW06: Zeng et al., 2023, *Nat Neurosci* (Integrative in situ mapping, mouse AD tauopathy model with BayesSpace) [ref 13]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Integrative in situ mapping of single-cell transcriptional states and tissue histopathology in a mouse AD model, and imaging evidence that microglia closely surround plaques while astrocytes are more distant.
  - Why: Cited as corroborating this paper's finding (C08) that microglia, more than astrocytes, mediate the plaque-proximal glial response.
- **Claims affected**: C08
- **Adopted elements**: BayesSpace (the spatial clustering method from this lineage) used as a comparator clustering method (see RW-adjacent method citation, ref [43], below) for validating Louvain-based spot clustering.

## RW07: Bouvier et al., 2016, *Sci Rep* (High-resolution dissection of reactive glial nets in AD) [ref 4]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: High-resolution imaging showing microglia and astrocytes form reactive glial nets around Aβ plaques in postmortem human brain, and that these nets constitute toxic inflammatory microenvironments.
  - Why: Establishes the imaging-based precedent for "plaque-glia niches" as toxic microenvironments, which this paper extends with spatial transcriptomics.
- **Claims affected**: C03
- **Adopted elements**: Conceptual framing (glial nets around plaques); not a computational or gene-set dependency.

## RW08: Mathys et al., 2019, *Nature* (Single-cell transcriptomic analysis of AD) [ref 9]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Published single-nucleus RNA-seq dataset of human DLPFC defining ~44 brain cell (sub)types.
  - Why: Used as the reference for cell2location deconvolution of ST spots.
- **Claims affected**: (supports spot-cluster annotation infrastructure, not a specific numbered claim)
- **Adopted elements**: The 44-cell-type reference (and an 8-major-cell-type collapsed version) used directly as the cell2location deconvolution reference (Fig. 1F).

## RW09: Mostafavi et al., 2018, *Nat Neurosci* (Molecular network of the aging human brain, 478 donors) [ref 11]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Bulk RNA-seq co-expression network from DLPFC of 478 individuals.
  - Why: Used as an independent, much larger bulk dataset against which this paper's ST-derived 23 co-expression modules were tested for preservation (WGCNA modulePreservation, Zsummary statistic).
- **Claims affected**: (data-quality-check infrastructure, not a specific numbered claim)
- **Adopted elements**: Used as the comparison network for module preservation analysis (Supplementary Fig. 4B-C); not a gene-set input to the main Aβ/glia contrasts.

## RW10: Zhou et al., 2020, *Nat Med* (TREM2-dependent/independent responses, human & mouse) [ref 6]; Srinivasan et al., 2020, *Cell Rep* (AD microglia enhanced aging/transcriptional activation) [ref 7]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Established that IBA1 correlates with microglial activation and that human/mouse glial transcriptional responses to AD pathology diverge.
  - Why: Cited to justify (a) using IBA1 intensity as a microglial-activation proxy for glia stratification, and (b) the paper's motivation that mouse-model glial signatures may not directly transfer to human tissue.
- **Claims affected**: (motivates methodology, especially glia stratification and the choice to also test human-derived MG states)
- **Adopted elements**: Conceptual justification only.

## RW11: Korsunsky et al., 2019, *Nat Methods* (Harmony) [ref 17]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provides the Harmony algorithm for fast, sensitive batch integration of single-cell/spatial data.
  - Why: Selected (after benchmarking against 6 alternatives) as this paper's integration method for spot clustering.
- **Claims affected**: (methodological dependency; supports spot-cluster annotation used across all downstream analyses)
- **Adopted elements**: Harmony package (v0.1.0) used directly for batch integration prior to Louvain clustering.

## RW12: Raredon et al., 2023, *Bioinformatics* (NICHES) [ref 33]
- **DOI**: 10.1093/bioinformatics/btac775
- **Type**: imports
- **Delta**:
  - What changed: Provides the NICHES framework for comprehensive visualization/inference of cell-cell interactions in single-cell and spatial transcriptomics.
  - Why: Directly used as this paper's ligand-receptor spatial-signaling inference method.
- **Claims affected**: C06, C07
- **Adopted elements**: NICHES (v1.0.0) used directly with the Omnipath LR database for all ligand-receptor analyses (Fig. 4, 6).

## RW13: Kleshchevnikov et al., 2022, *Nat Biotechnol* (cell2location) [ref 41]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provides a Bayesian model for fine-grained cell-type mapping in spatial transcriptomics.
  - Why: Used to estimate per-spot cell-type abundance from the Mathys et al. snRNA-seq reference.
- **Claims affected**: (supports cell-type annotation infrastructure, Fig. 1F)
- **Adopted elements**: cell2location used directly for spot-level cell-type deconvolution.

## RW14: Fleming et al., 2023, *Nat Methods* (CellBender) [ref 37]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provides unsupervised removal of ambient-RNA background noise from droplet-based scRNA-seq.
  - Why: Applied to correct raw count matrices from the iPSC co-culture scRNA-seq experiment prior to downstream analysis.
- **Claims affected**: C08, C09 (data-quality dependency)
- **Adopted elements**: CellBender (v0.3.0) used directly in the scRNA-seq preprocessing pipeline.

## RW15: Zhao et al., 2021, *Nat Biotechnol* (BayesSpace) [ref 43]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Provides a spatial-clustering method (subspot resolution) explicitly designed to leverage spatial coordinates, unlike expression-only Louvain clustering.
  - Why: Used as a comparator to validate the paper's Louvain-based spot clustering; found more spatially contiguous but unable to identify sporadically distributed clusters (Blood Vessel, Interneuron) that Louvain captured.
- **Claims affected**: (methodological validation, not a numbered claim; supports the decision node in the exploration tree comparing clustering methods)
- **Adopted elements**: Not adopted for final analysis (Louvain retained); used only as a benchmarking comparator, with 99% concordance reported between Louvain- and BayesSpace-labeled gray-matter spots.

## RW16: Mallach et al., 2024, *Cell Rep* (Microglia-astrocyte crosstalk in mouse AD plaque niche via ST) [ref 51]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Mouse ST study showing alterations in GABAergic/glutamatergic signaling corresponding to microglia density in plaque-glia niches.
  - Why: Cited as consistent with this paper's IHC finding of reduced neuronal/synaptic markers near glia-high plaques.
- **Claims affected**: C03
- **Adopted elements**: Conceptual corroboration only (cross-species consistency check), not a shared dataset or gene set.

## RW17: Röhr et al., 2020, *Acta Neuropathol Commun* (label-free vibrational imaging of plaque types) [ref 45]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Demonstrated increasing Aβ content along the ascending plaque-maturity sequence (diffuse → compact → dense core), and that early-stage plaques are richer in toxic oligomers/protofibrils while late-stage plaques are primarily fibrillar.
  - Why: Cited as independent, biochemical corroboration of (a) this paper's Aβ-intensity-to-plaque-type mapping (C05) and (b) the interpretation that low-Aβ/diffuse plaques are more neurotoxic (C02).
- **Claims affected**: C02, C05
- **Adopted elements**: Conceptual corroboration only.

## RW18: Yang et al., 2022, *Science* (Cryo-EM structures of Aβ42 filaments from human brains) [ref 55]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Identified two structurally distinct Aβ42 filament types: Type I predominant in sporadic AD with abundant compact plaques, Type II predominant in familial AD with abundant diffuse plaques.
  - Why: Cited as additional structural biology support for greater neurotoxicity of diffuse (low-Aβ) plaques, given the generally greater pathology severity of familial AD.
- **Claims affected**: C02
- **Adopted elements**: Conceptual corroboration only.

## Additional citations without a specific technical delta (background / corroborating / infrastructure)

- **Walker 2020 [1]** — background review on Aβ plaques and glial recruitment.
- **Deczkowska et al. 2018 [2]; Huang et al. 2021 [3]** — background on microglia/TAM receptors and Aβ engulfment.
- **Serrano-Pozo et al. 2011 [5]** — background: reactive glia parallels neurofibrillary tangle progression.
- **Morabito et al. 2021 [10]** — background: single-nucleus chromatin accessibility/transcriptomics in AD.
- **Hafemeister & Satija 2019 [25] (SCTransform); Robinson et al. 2010 [24] (edgeR); Law et al. 2014 [46] (voom); Langfelder & Horvath 2008 [28] (WGCNA); Gaiteri et al. 2015 [26] (SpeakEasy); Kolberg et al. 2023 [27] (gprofiler); He et al. 2021 [16] (NEBULA); Blondel et al. 2024 [42] (Louvain)** — statistical/computational method infrastructure adopted directly as named R/Bioconductor tools throughout the pipeline.
- **Xu et al. 2021 [18] (scANVI); Haghverdi et al. 2018 [19] (fastMNN); Johnson et al. 2007 [20] (ComBat); Stuart et al. 2019 [21] (Seurat v3 RPCA); Lopez et al. 2018 [22] (scVI); Polański et al. 2020 [23] (BBKNN)** — alternative integration methods included in the benchmarking comparison (not adopted).
- **Maynard et al. 2021 [38]; Kim et al. 2022 [39]; He et al. 2017 [40]** — background: reference transcriptomic characterizations of human cortical layers, used to sanity-check cluster-enriched gene overlap.
- **Lagomarsino et al. 2021 [34]** — source of the BR28 iPSC line used for astrocyte/neuron differentiation.
- **Abud et al. 2017 [35]; McQuade et al. 2018 [36]** — iMGL differentiation protocols adopted (with minor modifications).
- **Peng et al. 2017 [15] (BaSiC)** — imaging background/shading correction tool adopted directly.
- **Kinney et al. 2018 [47]; Hong et al. 2016 [48]; Garcia-Contreras & Thakor 2023 [49]; Zhang et al. 2022 [50]** — background on inflammation, complement, extracellular vesicles, and autophagy in AD pathogenesis, cited to interpret glia-contrast GSEA pathway results.
- **Guha et al. 2022 [56]; Homayouni et al. 1999 [57]; Beffert et al. 2005 [58]; Elsworthy et al. 2022 [59]; Tang 2020 [60]; Rueda-Carrasco et al. 2021 [61]; Warrier et al. 2016 [62]** — background used to interpret specific compensatory gene candidates (ICAM1, DAB1, ADAM10, SFRPs) identified in the DEG analysis.
- **Baik et al. 2016 [63]; Spangenberg et al. 2019 [64]; Venegas et al. 2017 [65]; Liddelow et al. 2017 [66]** — background mechanistic literature on microglial/astrocyte contributions to plaque growth and neurotoxicity, cited in the Discussion to contextualize the glia-high DEG/IHC findings.
- **Chen et al. 2023 [67]; Nguyen et al. 2020 [68]** — background on T-cell infiltration and CD163+ myeloid cells in AD, cited to interpret the unexpected leukocyte-mediated-immunity GSEA enrichment.
- **Dolan et al. 2023 [69]; Gosselin et al. 2017 [71]; Cadiz et al. 2022 [72]** — background on iPSC-microglia disease-state recapitulation and known limitations of cultured microglia, cited to frame the in vitro validation (E10) and its limitations.
- **Rostami et al. 2021 [70]** — background on astrocyte-microglia crosstalk increasing Aβ aggregate degradation, cited in the Discussion.
- **Koffie et al. 2009 [52]; Shankar et al. 2008 [53]** — background establishing oligomeric Aβ as the synaptotoxic species and its association with plaque "halos," motivating the iMGL Aβ-oligomer treatment paradigm (E10).
- **Lee et al. 2022 [54]** — background on intraneuronal Aβ accumulation contributing to extracellular plaque formation, cited to interpret the low-Aβ apoptosis finding (C02).
