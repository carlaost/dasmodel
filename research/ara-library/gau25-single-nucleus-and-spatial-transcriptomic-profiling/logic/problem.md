# Problem Specification

## Observations

### O1: AD research has focused disproportionately on gray matter, leaving white matter (WM) transcriptomic changes under-characterized
- **Statement**: "While the pathogenesis of Alzheimer's disease has been extensively studied, the predominant focus has traditionally been on gray matter alterations, overlooking the essential role that white matter plays in neurological health."
- **Evidence**: Abstract; Introduction, Page 1 of 17.
- **Implication**: Motivates a paired gray-matter (GM) / white-matter (WM) sampling design from the same donors and brain region, rather than GM-only profiling as in most prior AD snRNA-seq studies.

### O2: Prior transcriptomic/epigenomic work established cell-type-level AD signatures (neuronal-function downregulation, innate-immune upregulation) but rarely examined spatial distribution of expression relative to pathology
- **Statement**: "recent transcriptomic and epigenomic analyses have revealed that post-mortem human AD brain tissue exhibits down-regulation of genes associated with neuronal function and upregulation of the genes involved in the innate immune response. However, not many studies have looked systematically at the spatial distribution of gene expression and its relationship to neuropathology."
- **Evidence**: Introduction, Page 1 of 17 (citing refs 4-8).
- **Implication**: Motivates pairing dissociated-nuclei profiling with an in-situ spatial platform (CARTANA) on the same donor tissue.

### O3: The study generated a large paired GM/WM snRNA-seq dataset from the temporal cortex (TC) of 40 individuals
- **Statement**: "we generated 430,271 single-nucleus RNA profiles from both white and gray matter samples, which were collected separately from the midsection of the mid-temporal cortex (mid-TC) in 40 individuals," profiling 80 post-mortem samples (40 individuals x GM+WM) spanning controls and varying Braak stages, with nuclei retained after QC and cluster identification segregated into 8 major cell types (glutamatergic neurons, GABAergic neurons, microglia, astrocytes, oligodendrocytes, OPCs, endothelial cells, pericytes) further subclustered into 20/22/7/5/4/3/3/6 subpopulations respectively.
- **Evidence**: Abstract; Results §"Transcriptional states of CNS cell types...", Page 3 of 17; Fig. 1b-f.
- **Implication**: Provides the statistical base (repeated GM/WM sampling per donor) for cell-subtype-resolved AD trait-association and differential-expression analyses.

### O4: Multiple neuronal and glial subpopulations show differential abundance with Braak stage in GM, with one deep-layer glutamatergic subgroup (THEMIS+/POSTN+) appearing resistant rather than vulnerable
- **Statement**: In GM, RORB+ (2 of 5 subpopulations, both IL1RAPL2+), SPARCL1+ glutamatergic, COL5A2+ (Layer 4), GLIS3+ (Layer 3), GNAL+, and TLL1+ glutamatergic subpopulations, plus PVALB+ and SPARCL1+ GABAergic subpopulations and RPL19+ microglia, show lower proportions at late Braak stages, whereas THEMIS+/POSTN+ deep-layer (L5-6) glutamatergic neurons, a SST+/THSD7B+/TRHDE+ GABAergic subpopulation, HSPA1A+ OPCs, MGP+ pericytes, and TNC+ astrocytes are overrepresented at later Braak stages.
- **Evidence**: Results §"Neuronal and glial subpopulations with lower prevalence...", Pages 3-4 of 17; Fig. 2a-d.
- **Implication**: Identifies both selectively vulnerable and selectively resistant/reactive cell subpopulations as candidate targets, with THEMIS+/POSTN+ neurons nominated as a potentially AD-resistant excitatory subclass.

### O5: WM shows distinct, sometimes opposite, subcluster associations with Braak stage compared to GM
- **Statement**: In WM, RORB+/IL1RAPL2+ glutamatergic neurons show *higher* proportions at intermediate Braak stages 2/4 (opposite to their pattern of being lower in GM at late stage), while TSHZ2+ endothelial cells and HSPA1A+ OPCs are higher, and PVALB+/TMEM132C+, PVALB+/SPARCL1+, LAMP5+/CHST9+ GABAergic subpopulations plus RPL19+ microglia and TAGLN+ pericytes are lower, at advanced Braak stages.
- **Evidence**: Results §"Neuronal and glial subclusters selectively enriched and depleted in white matter...", Pages 4-5 of 17; Fig. 2 legend.
- **Implication**: Indicates that WM pathological association is tissue-specific rather than a simple attenuated echo of the GM signal, motivating cell-type- and tissue-specific (GM vs WM interaction-term) statistical modeling throughout the paper.

### O6: Key subcluster-Braak associations replicate across independent brain regions, studies, and cohorts, including two much larger external datasets
- **Statement**: THEMIS+/POSTN+ deep-layer glutamatergic neurons were consistently overrepresented in late Braak stages across entorhinal cortex, prefrontal cortex, and superior frontal gyrus integrations, in the SEA-AD middle temporal gyrus (MTG) cohort (84 individuals), and in an independent ROSMAP prefrontal cortex (PFC) cohort (424 individuals); PVALB+/TMEM132C+ GABAergic neurons were lower at advanced Braak stages in all examined regions; TAGLN+ pericytes and RPL19+ microglia were lower, and HSPA1A+ OPCs enriched, in Braak stages 5/6 across multiple cortical regions.
- **Evidence**: Results §"Consistency of subcluster associations with Braak stage across multiple brain regions and studies", Page 5 of 17.
- **Implication**: Cross-cohort/cross-region replication (including in a >10x larger PFC cohort) substantially strengthens confidence that the THEMIS+/POSTN+ resilience signature and the PVALB+/TMEM132C+, TAGLN+, RPL19+ vulnerability signatures are general AD-pathology correlates rather than TC- or cohort-specific artifacts.

### O7: Pseudobulk differential expression reveals a strongly Braak-stage-dependent, highly cell-type-specific transcriptional signature, with far more changes at late than early Braak stages
- **Statement**: Comparing Braak 2-4 vs 0-1 yielded only 17 FDR-significant DEGs (all restricted to GABAergic neurons, oligodendrocytes, and OPCs), while comparing Braak 5-6 vs 0-1 yielded 1230 FDR-significant DEGs, of which ~90% (1102/1230) were specific to a single cell type; 644 genes were additionally affected differentially by late-stage pathology between GM and WM.
- **Evidence**: Results §"Differential expression analysis identifies additional cell type-specific genes...", Pages 5-6 of 17; Fig. 3a.
- **Implication**: Supports a model in which transcriptional dysregulation is concentrated at, and roughly proportional to, the cortical pathology burden expected at late Braak stages, and is predominantly a cell-autonomous (not shared/multi-cell-type) response, with a further tissue-compartment-specific (GM vs WM) layer of specificity.

### O8: Genes upregulated in glutamatergic neurons at late Braak stages are more evolutionarily constrained than non-DE genes
- **Statement**: "upregulated genes in late Braak stages (5-6) in glutamatergic neurons, as well as genes differentially affected between gray and white matter in glutamatergic neurons, were significantly more constrained than non-differentially expressed genes," based on LOEUF score comparison.
- **Evidence**: Results §"Differential expression analysis identifies additional cell type-specific genes...", Page 7 of 17; Fig. 3d.
- **Implication**: Suggests upregulated genes in late-Braak glutamatergic neurons may serve essential/developmentally important functions, consistent with a hypothesized cell-survival response under pathological stress, rather than being incidental bystander transcriptional noise.

### O9: A large-panel (155-gene) CARTANA in-situ sequencing platform, paired with amyloid/tau immunostaining on the same tissue sections, replicates key snRNA-seq cell-type-Braak-stage associations in intact tissue
- **Statement**: In GM, ISH confirmed lower expression of ACTG1/ALDH1A1/TM2D1 (glutamatergic), ACTG1/SCG3/PDCD6 (GABAergic), CD74/P2RY12 (microglia) at late Braak stages, higher GFAP (astrocytes) at late Braak stages, and higher PPP1R1A/CC2D1B (THEMIS+/POSTN+-associated glutamatergic marker combination) at Braak stages 2/4 and 5/6 respectively; in WM, lower PDCD6/ANXA7 (GABAergic) at Braak 5/6.
- **Evidence**: Results §"Validation of snRNA-seq derived associations...", Pages 8-9 of 17; Fig. 4c.
- **Implication**: Provides orthogonal, spatially-resolved (non-dissociation-based) confirmation that at least a subset of the snRNA-seq proportion/expression findings are not artifacts of the tissue-dissociation process.

### O10: Spatial (CARTANA) analysis reveals cell type-specific gene-expression gradients with distance from amyloid plaques and tau tangles that are not directly observable in dissociated snRNA-seq data
- **Statement**: Cells close to plaques show lower NEFL/NEFM (glutamatergic) and lower RELN (GABAergic) than cells at intermediate/far distance; microglial CD68 is higher at intermediate distance from plaques; astrocytic GFAP and endothelial/pericyte ID3 are higher farther from plaques; for tangles, THEMIS (glutamatergic), GFAP (astrocytes), and PLP1 (oligodendrocytes) are all higher in tangle-distant cells.
- **Evidence**: Results §"Spatial analysis identifies genes with altered expression near pathological inclusions", Pages 9-11 of 17; Fig. 5b-c.
- **Implication**: Because plaques are extracellular and tangles are predominantly intraneuronal, the differing proximal signatures for the two pathologies (e.g., distinct neuronal genes affected) are interpreted as reflecting pathology-specific mechanisms of local cellular stress, information unavailable from dissociated-nuclei approaches alone.

### O11: A counter-intuitive finding — bulk GFAP transcript is higher farther from plaques, apparently conflicting with prior IHC reports of increased GFAP+ astrocyte density near plaques — is reconciled by evidence of a non-unimodal (bimodal-like) GFAP expression distribution specifically in plaque-proximal cells
- **Statement**: Using kernel density estimation and Hartigan's dip statistic, the plaque-proximal distance bin showed the highest median dip statistic (0.124) versus intermediate (0.119) and far (0.121) bins, indicating a stronger deviation from unimodality (i.e., more heterogeneous GFAP-high/GFAP-low subgroup structure) near plaques.
- **Evidence**: Discussion, Page 11-12 of 17; Supplementary Fig. 7d (not included in provided PDF; dip-statistic values are stated directly in the main-text Discussion).
- **Implication**: The authors propose this can be reconciled with prior IHC findings if both GFAP-high and GFAP-low astrocyte subpopulations increase in density near plaques, producing a non-unimodal average that offsets the expected mean elevation seen by IHC.

### O12: An unexpected discordance between two "homeostatic" microglial markers (TMEM119 upregulated vs. P2RY12 downregulated) is observed in the CARTANA data but not in the snRNA-seq data
- **Statement**: "the expression of TMEM119, a presumed homeostatic microglial gene, is unexpectedly upregulated in donors with advanced pathology. This contrasts with P2RY12, another homeostatic microglial gene, which is typically downregulated in similar conditions; this discrepancy is not found in the snRNA-seq data."
- **Evidence**: Results §"Validation of snRNA-seq derived associations...", Page 9 of 17; Discussion, Page 12 of 17 (citing Satoh et al. 2016 and Mercurio et al. 2022 as partial precedent for TMEM119 upregulation in pathology/injury contexts).
- **Implication**: Flags a platform-specific (or dissociation-sensitive) anomaly in a canonical homeostatic-microglia marker pair that the paper explicitly leaves unresolved, cautioning against uncritical use of TMEM119 as a homeostatic-microglia proxy in spatial/ISH data.

## Gaps

### G1: It was unknown which specific neuronal/glial subpopulations in gray AND white matter of the human temporal cortex change in proportion or expression with AD (Braak-stage) pathology, using a design with sufficient paired GM/WM sampling to compare tissue compartments directly
- **Caused by**: O1, O2.
- **Existing attempts**: Single-cell/single-nucleus AD studies in prefrontal cortex (Mathys et al. 2019; Cain et al. 2020; Zhou et al. 2020; Green et al. 2024), entorhinal cortex (Leng et al. 2021; Grubman et al. 2019), superior frontal gyrus (Leng et al. 2021), and deep PFC white matter (Bryois et al. 2022).
- **Why they fail**: These studies each profile a single brain region and largely a single tissue compartment (mostly GM), so no prior single study directly compared GM and WM composition/expression changes within the same donors' temporal cortex at the scale reported here (40 individuals, 430,271 nuclei).

### G2: Dissociated single-nucleus proportion/expression associations with pathology could reflect tissue-dissociation artifacts, and it was unclear whether they hold in intact tissue or specifically near pathological inclusions
- **Caused by**: O2, O4, O5.
- **Existing attempts**: Prior human AD spatial transcriptomic work generally used smaller sample sizes, coarser (non-single-cell) spot resolution, or, unlike this study, did not pair the same in-situ platform's readout with immunostaining for both amyloid and tau on the same sections.
- **Why they fail**: Without a spatial platform validated on the same donor tissue, cluster-proportion changes measured from dissociated nuclei cannot distinguish a true compositional shift from an artifact of differential dissociation susceptibility across cell states, nor can they localize expression changes relative to specific pathological inclusions.

### G3: It was unclear whether AD-associated cell subpopulation signatures generalize beyond a single cohort/brain region, given known heterogeneity in AD presentation
- **Caused by**: O4, O5.
- **Existing attempts**: Individual published snRNA-seq AD studies of PFC, EC, and SFG existed but had not been harmonized against this study's TC-derived subcluster taxonomy.
- **Why they fail**: Absent a common subcluster label transfer (via Harmony integration and the Cell Type Mapper algorithm) across studies/regions, apparent subcluster-Braak associations could not be tested for cross-region/cross-cohort consistency.

### G4: The directionality and cell-type specificity of transcriptional dysregulation across early vs. late AD pathology stages, and across GM vs. WM, was not established for the temporal cortex
- **Caused by**: O7.
- **Existing attempts**: Prior single-region pseudobulk/cell-type DE analyses in AD (e.g., Mathys et al. 2019; Zhou et al. 2020) established cell-type-specific DE signatures but did not test a Braak-stage x tissue (GM/WM) interaction term within the same donor's paired samples.
- **Why they fail**: Without paired same-donor GM/WM sampling and an explicit interaction term in the statistical model, tissue-compartment-specific components of the AD transcriptional response (e.g., the 644 genes found here to be differentially affected between GM and WM at late Braak stage) cannot be isolated from the overall Braak-stage effect.

## Key Insight
- **Insight**: Because the RNA-preserving dissociation protocol used for snRNA-seq cannot preserve spatial/pathological context, and cluster-proportion-based dissociated-nuclei analyses cannot distinguish true compositional change from dissociation-susceptibility artifacts, pairing large-scale paired-GM/WM snRNA-seq (430,271 nuclei, 40 individuals) with a targeted (155-gene) in-situ sequencing platform (CARTANA) applied to the *same* donor tissue sections that are *also* immunostained for amyloid and tau enables (1) direct validation of dissociated-nuclei-derived proportion/expression associations in intact tissue, and (2) discovery of cell type-specific gene-expression changes as a function of literal spatial proximity to pathological inclusions — a class of finding invisible to dissociation-based methods altogether.
- **Derived from**: O1, O2, O3, O9, O10.
- **Enables**: A multimodal framework linking cell-subtype composition, cell-type-specific differential expression, cross-region/cross-cohort replication, and spatially-resolved (proximity- and density-based) gene expression analysis to Braak-stage AD pathology in both gray and white matter of the human temporal cortex.

## Assumptions
- A1: Braak stage (tau/neurofibrillary-tangle spread) is an adequate single proxy variable for overall AD pathological progression, chosen over amyloid-beta pathology because "the spread of tangles in the brain is more stereotyped" and "global post-mortem tau is more strongly correlated with cognitive impairment than post-mortem amyloid-beta" (ref 16).
- A2: Categorizing continuous Braak stage into three discrete bins (0-1, 2-4, 5-6) for both trait-association (ANCOM-BC) and differential-expression (glmmTMB) models adequately captures disease-stage-dependent effects without losing critical information from finer-grained staging.
- A3: Cell-subcluster labels derived from the TC dataset (via Harmony integration, Louvain clustering at resolution 0.8, and Random Forest-based refinement) transfer validly onto external datasets (EC, PFC, SFG, WM-PFC, SEA-AD MTG, ROSMAP PFC) via the Cell Type Mapper algorithm, enabling valid cross-region/cross-cohort trait-association comparison.
- A4: Alternative CARTANA marker genes selected in place of "optimal" snRNA-seq-derived markers (necessitated by probe-design constraints) still adequately discriminate the corresponding snRNA-seq-derived subclusters, despite not being the top differentially expressed genes for those subclusters.
- A5: Distance cutoffs for the plaque-proximity (<70 µm / 70-154 µm / >154 µm) and tangle-proximity (<98 µm / 98-262 µm / >262 µm) categorization, "calculated empirically based on the overall distribution," adequately capture biologically meaningful near/intermediate/far pathology microenvironments.
- A6: The 100x100 pixel (1056 µm²) tile size used for the tile-based (plaque-density) differential expression analysis is an appropriate spatial unit for detecting microenvironment-level (as opposed to single-plaque-proximity) transcriptional effects.
