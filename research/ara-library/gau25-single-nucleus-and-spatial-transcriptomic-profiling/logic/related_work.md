# Related Work

## RW01: Miyoshi et al., 2023, bioRxiv (Spatial and single-nucleus transcriptomic analysis of genetic and sporadic AD) [ref 8]
- **DOI**: 10.1101/2023.07.24.550282
- **Type**: baseline / bounds
- **Delta**:
  - What changed: One of the few prior studies to look systematically at the spatial distribution of gene expression and its relationship to neuropathology in AD.
  - Why: Directly motivates this paper's rationale (Introduction) that "not many studies have looked systematically at the spatial distribution of gene expression and its relationship to neuropathology," framing the gap this paper's CARTANA spatial arm addresses.
- **Claims affected**: (motivates overall study design; not tied to a single numbered claim)
- **Adopted elements**: None directly reused; cited as the prior spatial-AD-transcriptomics state of the art this paper extends with a paired GM/WM, immunostaining-co-registered design.

## RW02: Mathys et al., 2019, *Nature* (Single-cell transcriptomic analysis of Alzheimer's disease) [ref 5]
- **DOI**: Not specified in paper
- **Type**: imports / baseline
- **Delta**:
  - What changed: Established a foundational human prefrontal-cortex single-cell AD atlas and cell-type-specific transcriptional signatures of AD pathology.
  - Why: Used as one of the prefrontal-cortex datasets incorporated into this paper's cross-region integration/replication analysis.
- **Claims affected**: C04
- **Adopted elements**: PFC single-nucleus dataset incorporated directly into the Harmony-integrated multi-region trait-association analysis.

## RW03: Leng et al., 2021, *Nat Neurosci* (Molecular characterization of selectively vulnerable neurons in Alzheimer's disease) [ref 10]
- **DOI**: Not specified in paper
- **Type**: imports / baseline
- **Delta**:
  - What changed: Identified RORB as a marker of selectively vulnerable excitatory neurons in the entorhinal cortex and superior frontal gyrus.
  - Why: Provides both an external dataset (entorhinal cortex, superior frontal gyrus) for cross-region integration and the conceptual precedent (RORB vulnerability) that this paper both aligns with and refines (finding that not all RORB+ subpopulations are equally vulnerable at late Braak stages).
- **Claims affected**: C01, C04
- **Adopted elements**: EC and SFG datasets incorporated into the multi-region Harmony integration; RORB-vulnerability framing directly discussed against this paper's own more granular (subcluster-level) finding.

## RW04: Grubman et al., 2019, *Nat Neurosci* (A single-cell atlas of entorhinal cortex from individuals with Alzheimer's disease) [ref 11]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provided a single-cell atlas of entorhinal cortex in AD with cell-type-specific gene expression regulation.
  - Why: Incorporated as an external EC dataset for the multi-region Harmony integration, but later excluded from the trait-association analysis specifically due to demographic-detail variation from the other studies.
- **Claims affected**: (integration infrastructure only; excluded from the specific analysis behind C04)
- **Adopted elements**: EC dataset included in the initial multi-study merge/integration; excluded from the downstream ANCOM-BC trait-association step.

## RW05: Cain et al., 2020, bioRxiv (Multi-cellular communities are perturbed in the aging human brain and Alzheimer's disease) [ref 12]
- **DOI**: 10.1101/2020.12.22.424084
- **Type**: imports
- **Delta**:
  - What changed: Provided a prefrontal-cortex single-nucleus dataset examining multicellular community perturbation with aging/AD.
  - Why: Incorporated as one of the PFC datasets for cross-region integration/replication.
- **Claims affected**: C04
- **Adopted elements**: PFC dataset included directly in the Harmony-integrated multi-region trait-association analysis.

## RW06: Zhou et al., 2020, *Nat Med* (Human and mouse single-nucleus transcriptomics reveal TREM2-dependent and TREM2-independent cellular responses in Alzheimer's disease) [ref 13]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provided human and mouse PFC single-nucleus data characterizing TREM2-dependent/independent AD cellular responses.
  - Why: Incorporated as one of the PFC datasets for cross-region integration/replication.
- **Claims affected**: C04
- **Adopted elements**: PFC dataset included directly in the Harmony-integrated multi-region trait-association analysis.

## RW07: Bryois et al., 2022, *Nat Neurosci* (Cell-type-specific cis-eQTLs in eight human brain cell types identify novel risk genes for psychiatric and neurological disorders) [ref 14]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provided deep white-matter (prefrontal cortex) single-nucleus data and identified FCER1G among other cell-type-specific eQTL-linked AD/psychiatric risk genes.
  - Why: Supplies the deep-WM-from-PFC dataset for cross-region integration, and the prior evidence that FCER1G carries AD genetic risk, cited when interpreting this paper's own FCER1G GM-vs-WM differential-expression finding.
- **Claims affected**: C04, C06
- **Adopted elements**: Deep-WM-PFC dataset included in the Harmony-integrated multi-region analysis; FCER1G AD-genetic-risk annotation adopted directly in the Results interpretation.

## RW08: Gabitto et al., 2024, *Nat Neurosci* (Integrated multimodal cell atlas of Alzheimer's disease; SEA-AD) [ref 28]
- **DOI**: Not specified in paper
- **Type**: imports / baseline
- **Delta**:
  - What changed: Provided the Seattle Alzheimer's Disease Brain Cell Atlas (SEA-AD), a middle temporal gyrus (MTG) single-nucleus dataset from 84 individuals.
  - Why: Used as one of the two large external cohorts onto which this paper transferred its TC subcluster labels (via Cell Type Mapper) to test cross-cohort replication of the THEMIS+/POSTN+ and PVALB+/TMEM132C+ associations.
- **Claims affected**: C04
- **Adopted elements**: SEA-AD MTG dataset (84 individuals) and its associated Braak-stage/demographic metadata used directly as the query dataset for label transfer and replication trait-association analysis.

## RW09: Green et al., 2024, *Nature* (Cellular communities reveal trajectories of brain ageing and Alzheimer's disease) [ref 30]
- **DOI**: Not specified in paper
- **Type**: imports / baseline
- **Delta**:
  - What changed: Provided a large (424-individual) ROSMAP prefrontal-cortex single-nucleus dataset and its own subcluster taxonomy.
  - Why: Used as the second large external cohort (via Cell Type Mapper label transfer) for cross-cohort replication of this paper's subcluster-Braak-stage findings; also cited as an example of cohort sizes exceeding this paper's own (40-individual) cohort, contextualizing a stated limitation.
- **Claims affected**: C04
- **Adopted elements**: ROSMAP PFC dataset (424 individuals) used directly as the query dataset for label transfer and replication trait-association analysis.

## RW10: AllenInstitute, cell_type_mapper (GitHub) [ref 29]
- **DOI**: Not specified in paper (software repository)
- **Type**: imports
- **Delta**:
  - What changed: Provides the Cell Type Mapper algorithm for reference-to-query cell-type/subcluster label transfer between single-cell datasets.
  - Why: Directly used to transfer this paper's TC-derived subcluster taxonomy onto the SEA-AD MTG and ROSMAP PFC datasets.
- **Claims affected**: C04
- **Adopted elements**: `cell_type_mapper.cli.precompute_stats_scrattch` and `cell_type_mapper.cli.map_to_on_the_fly_markers` commands used directly, with default parameters, for label transfer.

## RW11: Korsunsky et al., 2019, *Nat Methods* (Harmony) [ref 52]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provides the Harmony algorithm for fast batch integration of single-cell data.
  - Why: Used directly for both (a) integrating the 80 TC samples across sequencing batches for subclustering, and (b) integrating the TC dataset with six external multi-region studies.
- **Claims affected**: C01, C02, C03, C04 (integration infrastructure underlying all subcluster-level findings)
- **Adopted elements**: Harmony (version 0.1.0), 30 principal components, resolution 0.8, used directly via the Seurat `RunHarmony` function.

## RW12: Lin & Peddada, 2020, *Nat Commun* (ANCOM-BC) [ref 58]; Lin & Peddada, 2024, *Nat Methods* (multigroup ANCOM-BC2) [ref 60]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provide the ANCOM-BC log-linear compositional differential-abundance framework (and its multigroup/covariate-adjusted extension).
  - Why: ANCOM-BC (v1.0.5) is the paper's primary trait-association method for TC-region proportion analysis; the multigroup ANCOM-BC2 (v2.0.2) extension is used for the cross-region/cross-cohort replication analyses with additional covariates.
- **Claims affected**: C01, C02, C03, C04
- **Adopted elements**: `ancombc` function used directly, with Braak stage as the covariate of interest and sex/age/PMI regressed out.

## RW13: Brooks et al., 2017, *R Journal* (glmmTMB) [ref 62]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provides a flexible, fast-fitting generalized/zero-inflated mixed-model R package.
  - Why: Used directly to fit the negative-binomial (family=nbinom2) mixed model for all pseudobulk differential-expression contrasts.
- **Claims affected**: C05, C06, C07
- **Adopted elements**: glmmTMB used directly for all cell-type-specific pseudobulk DE models, including the Braak-stage x tissue interaction term.

## RW14: de Leeuw et al., 2015, *PLOS Comput. Biol.* (MAGMA); Wightman et al., 2021, *Nat Genet.* (AD GWAS, 1,126,563 individuals) [refs 64, 65]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: MAGMA provides gene-level genetic-association testing from GWAS summary statistics; Wightman et al. provide the specific large-scale AD GWAS summary statistics used as input.
  - Why: Used together to identify AD-genetically-associated pathways, which are then tested (via fgsea) for enrichment among this paper's cell-type-specific DEGs.
- **Claims affected**: C08
- **Adopted elements**: MAGMA run directly on the Wightman et al. AD GWAS summary statistics (gene window 35 kb upstream to 10 kb downstream) to define AD-genetically-associated pathways from GO_BP/CC/MF, Hallmark, KEGG, and REACTOME.

## RW15: Karczewski et al., 2020, *Nature* (gnomAD mutational constraint spectrum / LOEUF) [ref 34]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Quantified genome-wide loss-of-function mutational constraint (LOEUF) from 141,456 humans (gnomAD).
  - Why: LOEUF scores used directly as the gene-constraint metric compared between late-Braak-stage DEGs and non-DE genes in glutamatergic neurons.
- **Claims affected**: C07
- **Adopted elements**: LOEUF scores used directly, without re-derivation, as input to the Wilcoxon rank-sum constraint comparison.

## RW16: Kuznetsova et al., 2017, *J. Stat. Softw.* (lmerTest) [ref 67]
- **DOI**: Not specified in paper
- **Type**: imports
- **Delta**:
  - What changed: Provides significance-testing extensions (Satterthwaite approximation) for linear mixed-effects models fit with lme4.
  - Why: Used directly for both the CARTANA cell-type-marker Braak-stage validation model and the distance-based (plaque/tangle proximity) spatial expression models.
- **Claims affected**: C09, C12, C13
- **Adopted elements**: lmerTest used directly to fit all CARTANA-based linear mixed-effects models (two-sided tests, uncorrected for multiple comparisons at the per-gene level).

## RW17: Bennett et al., 2012, *Ann. Neurol.* (Relation of neuropathology to cognition in persons without cognitive impairment) [ref 16]
- **DOI**: Not specified in paper
- **Type**: bounds
- **Delta**:
  - What changed: Established that post-mortem tau pathology correlates more strongly with cognitive impairment than post-mortem amyloid-beta pathology.
  - Why: Directly cited as the rationale for selecting Braak stage (tau) rather than amyloid pathology as this paper's primary AD-progression proxy variable.
- **Claims affected**: (motivates the paper's core design choice, underlying all Braak-stage-based claims C01-C09, C12)
- **Adopted elements**: Conceptual justification only, not a shared dataset or method.

## RW18: Serrano-Pozo et al., 2013, *J. Neuropathol. Exp. Neurol.* (Differential relationships of reactive astrocytes and microglia to fibrillar amyloid deposits in Alzheimer disease) [ref 46]
- **DOI**: Not specified in paper
- **Type**: baseline / bounds
- **Delta**:
  - What changed: Reported (via IHC) increased GFAP+ astrocyte density near plaques in the temporal neocortex.
  - Why: Creates the apparent contradiction with this paper's own finding (higher bulk GFAP transcript farther from plaques), which the paper explicitly attempts to reconcile via the GFAP-bimodality/Hartigan's-dip-statistic analysis.
- **Claims affected**: C13
- **Adopted elements**: Not adopted computationally; cited as the prior finding this paper's own spatial transcriptomic result appears to contradict and then reconciles.

## RW19: Satoh et al., 2015/2016, *Neuropathology* (TMEM119 marks a subset of microglia in the human brain) [ref 47]; Mercurio et al., 2022, *Front. Cell. Neurosci.* (Tmem119 protein expression changes in a mouse TBI model) [ref 48]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Satoh et al. reported elevated TMEM119 mRNA in AD frontal cortex; Mercurio et al. reported Tmem119 protein changes in a mouse traumatic-brain-injury model coinciding with microglial activation.
  - Why: Cited as partial precedent for this paper's own unexpected finding of TMEM119 upregulation (rather than the typically-reported downregulation) in CARTANA data at advanced pathology, discordant with co-measured P2RY12.
- **Claims affected**: C11
- **Adopted elements**: Conceptual corroboration only, not a shared dataset or gene set; the paper explicitly leaves the discrepancy's cause unresolved despite this partial precedent.

## RW20: Otero-Garcia et al., 2022, *Neuron* (Molecular signatures underlying neurofibrillary tangle susceptibility in Alzheimer's disease) [ref 39]
- **DOI**: Not specified in paper
- **Type**: baseline
- **Delta**:
  - What changed: Identified an NR4A2+/NTNG2+ deep-layer (L6) glutamatergic neuronal type harboring the lowest neurofibrillary tangle burden in AD, nominally tangle-resistant.
  - Why: Cited as independent precedent supporting this paper's own THEMIS+/POSTN+ subcluster (which the authors note also expresses high NR4A2 and NTNG2) as a resilient excitatory neuronal subclass.
- **Claims affected**: C01, C04
- **Adopted elements**: Conceptual corroboration only; no shared dataset or gene set directly reused.

## Additional citations without a specific technical delta (background / corroborating / infrastructure)

- **Mucke 2009 [1]; Dolgin 2018 [2]; Mostafavi et al. 2018 [3]** — background on AD pathological hallmarks, diagnosis, and a prior molecular-network study of the aging human brain.
- **Williams, Cao & Yan 2021 [4]; Heneka et al. 2015 [6]; Obulesu & Jhansilakshmi 2013 [7]; Luquez et al. 2022 [9]** — background on synaptic-gene downregulation and innate-immune upregulation in AD transcriptomics.
- **Muratore et al. 2017 [17]** — background on cell-type-dependent selective neuronal vulnerability in AD.
- **Kong et al. 2009 [18]; Squillario & Barla 2011 [19]; Cruchaga et al. 2013 [20]** — background microarray/GWAS studies supporting COL5A2 and GLIS3 as AD-associated genes.
- **Lai, Esiri & Tan 2014 [21]; Jeong et al. 2015 [22]** — background on GNAL alternative splicing and TLL1/Aβ-processing gene associations in AD.
- **Ali et al. 2019 [23]** — background on PVALB neuron loss in AD-model mouse frontal cortex.
- **Yin et al. 2009 [24]; Richens et al. 2014 [25]** — background CSF biomarker literature cited to interpret SPARCL1/NPTX findings.
- **Deng et al. 2022 [26]; Cacabelos et al. 2014 [27]** — background on LAMP5 interneuron loss and CHST9 drug-metabolism association in AD.
- **Libiger et al. 2020 [31]** — background establishing NPTX2 as a CSF prognostic AD biomarker.
- **Namba et al. 1991 [32]; Steinberg et al. 2015 [33]** — background on APOE immunoreactivity in amyloid/tangle pathology and ABCA7 loss-of-function AD risk.
- **Yu et al. 2008 [35]; Deutsch, Rosse & Deutsch 2006 [36]** — background on FOXJ1 (ciliogenesis) and RELN (tau-phosphorylation inhibition) gene function, cited to interpret specific DEGs.
- **Mathys et al. 2023 [37]; Kocherhans et al. 2010 [38]** — background on cognitive-resilience single-cell atlases and reelin's effect on plaque/tau pathology in transgenic mice.
- **Horiuchi et al. 1999 [40]; Shih et al. 2014 [41]; Shimamura et al. 2012 [42]; Matsunaga et al. 2015 [43]** — background on periostin (POSTN) biology (neurite outgrowth, neuroprotection), cited to interpret the THEMIS+/POSTN+ resilience signature.
- **De Jager et al. 2012 [44]** — background GWAS of age-related cognitive decline, cited for THSD7B.
- **Laywell et al. 1992 [45]** — background on Tenascin (TNC) upregulation after adult brain injury, cited to interpret the TNC+ astrocyte enrichment.
- **Ruan & Elyaman 2022 [49]** — commentary contextualizing the Mercurio et al. TMEM119 findings.
- **Zheng et al. 2017 [50] (10x Chromium method); Germain et al. 2021 [51] (scDblFinder); Amezquita et al. 2019 [53] (Bioconductor/SingleCellExperiment); Stuart et al. 2019 [54] (Seurat v3); McInnes et al. 2018 [55] (UMAP); dittoSeq [56]; Lun, McCarthy & Marioni 2016 [57] (scran workflow); Gelman 2007 [59] (covariate scaling); Robinson, McCarthy & Smyth 2009 [61] (edgeR); Robinson & Oshlack 2010 [63] (TMM normalization); Korotkevich et al. 2016 [66] (fgsea); Wickham et al. [68] (dplyr)** — statistical/computational method infrastructure adopted directly as named R/Bioconductor tools and platforms throughout the pipeline.
