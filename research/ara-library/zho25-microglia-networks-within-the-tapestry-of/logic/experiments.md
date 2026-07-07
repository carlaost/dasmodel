# Experiments

> This is a review paper; "experiments" here are the analysis/verification approaches used by the
> primary studies the review synthesizes (as described in the review's narrative), not experiments
> run by Zhou & Glass themselves. Directional only — exact numeric outcomes live in `evidence/` and
> in the `Sources` entries of `logic/claims.md`.

## E01: Comparative benchmarking of img-ST vs. seq-ST platform resolution and gene-panel coverage
- **Verifies**: C01
- **Setup**: Apply MERFISH, seqFISH, and ISS-based img-ST platforms (with pre-selected gene panels) and Visium/Slide-seq/Visium HD/Stereo-seq seq-ST platforms (whole-transcriptome capture) to comparable tissue sections (e.g., the same AD brain region), imaged/sequenced at each platform's native spot or molecule resolution.
- **Procedure**: Overlay each platform's characteristic spot/pixel grid on a shared reference image (e.g., single-molecule MERFISH data with anti-Aβ antibody staining) to visually and quantitatively compare achievable resolution against transcriptome coverage and gene-panel size.
- **Expected outcome**: img-ST platforms show finer (sub-cellular to single-molecule) resolution but restrict analysis to a pre-selected gene set; seq-ST platforms show a resolution/coverage trade-off curve, with newer platforms (Stereo-seq, Visium HD) pushing seq-ST resolution toward the img-ST range while retaining whole-transcriptome capture.

## E02: Regional dissection and scRNAseq profiling of microglia across brain regions
- **Verifies**: C02
- **Setup**: Isolate microglia by fluorescence-activated cell sorting (FACS) from anatomically distinct brain regions (cortex, striatum, hippocampus, thalamus, midbrain, cerebellum, basal ganglia).
- **Procedure**: Perform scRNAseq on sorted microglia per region; quantify regional cell density (e.g., via imaging/stereology) and compare transcriptomic cluster composition across regions and across developmental stages (juvenile vs. adult).
- **Expected outcome**: Microglial density and transcriptomic state distribution vary systematically by brain region, with responses to local environmental cues becoming more pronounced with age.

## E03: Cross-model comparison of microglial activation gene signatures
- **Verifies**: C03
- **Setup**: Perform scRNAseq of sorted microglia across independent neurodegeneration mouse models (5xFAD/APP-PS1 for DAM; AD pathology models for ARM; ALS/MS/demyelination models for MGnD).
- **Procedure**: Identify the differentially expressed gene program defining each named microglial state within its originating model; compare gene lists across models to assess overlap.
- **Expected outcome**: A core disease/injury-associated activation gene module (including phagocytosis and lipid-metabolism genes) recurs across DAM, ARM, and MGnD nomenclatures despite independent discovery in different disease contexts.

## E04: Spatial definition and cross-cell-type validation of plaque-induced genes (PIGs)
- **Verifies**: C04
- **Setup**: Apply a seq-ST method to a mouse amyloid model (AppNL−G−F) with adjacent-section Aβ immunostaining; define a plaque-proximal mask by expanding a fixed distance around the Aβ-positive boundary.
- **Procedure**: Perform spatial differential expression analysis comparing plaque-masked vs. non-plaque spots to identify a co-expressed multicellular gene network (PIGs); cross-validate cell-type origin of individual PIGs using an independent img-ST in situ sequencing method with single-cell resolution.
- **Expected outcome**: A defined PIG gene set emerges that is strongly associated with DAM and inflammatory-astrocyte signatures; while most PIG expression is microglia-driven, a subset of PIGs is detectable in multiple cell types (astrocytes, oligodendrocytes, neurons).

## E05: Distance-binned cell-type enrichment analysis around amyloid plaques
- **Verifies**: C05, C06
- **Setup**: Apply an img-ST method (STARmap Plus) simultaneously profiling a large RNA panel plus antibody co-staining for amyloid and phosphorylated tau in a combined amyloid/tau mouse model (TauPS2APP).
- **Procedure**: Classify all profiled cells into major cell types; bin cells by distance from the nearest plaque boundary (e.g., in 10 μm increments) and compute per-bin cell-type enrichment relative to background; separately quantify the fraction of astrocytes matching a disease-associated astrocyte (DAA) signature per distance bin.
- **Expected outcome**: Distinct cell types show distinct peak-enrichment distances from the plaque (a distance-graded cellular response), with microglia enriched closest to plaques and other glia (astrocytes, oligodendrocytes, OPCs) enriched at progressively greater distances; a defined minority fraction of astrocytes adopts the DAA-like state at an intermediate distance band.

## E06: Receptor-ligand interaction inference from spatial transcriptomics data as a function of plaque distance
- **Verifies**: C07
- **Setup**: Apply img-ST (CosMx) and seq-ST (Stereo-seq) methods to amyloid-plaque-bearing mouse brain tissue with co-registered plaque location.
- **Procedure**: Run receptor-ligand (RL) interaction inference between spatially co-located microglia and astrocytes across the tissue; stratify inferred interaction strength by binned distance from the nearest plaque; cross-reference candidate RL genes against the established PIG gene list.
- **Expected outcome**: A defined set of candidate microglia-astrocyte RL pairs emerges, a subset of which overlap with PIGs; interaction strength for key pairs increases monotonically as spatial distance to the plaque decreases.

## E07: Cell-type-specific genetic deletion of Ifnar1 combined with spatial/synaptic phenotyping near plaques
- **Verifies**: C08
- **Setup**: Cross conditional Ifnar1 knockout alleles (microglia-specific and neuron-specific) onto an amyloid mouse model (5xFAD); identify the interferon-responsive fraction of Clec7a+ DAMs by scRNAseq/ST.
- **Procedure**: Quantify pre- and post-synaptic terminal density near plaques (e.g., by immunostaining for synaptic markers) and plaque burden in microglia-specific vs. neuron-specific Ifnar1 knockouts, relative to controls.
- **Expected outcome**: Microglial Ifnar1 deletion reduces post-synaptic terminal loss near plaques (via reduced selective engulfment); neuronal Ifnar1 deletion instead restores pre-synaptic terminals and reduces plaque accumulation — establishing IFN-I as a bidirectional, cell-type-specific node linking microglia-neuron crosstalk to synaptic and amyloid outcomes.

## E08: Joint STAR-MAP imaging of phosphorylated tau and microglia across disease time points
- **Verifies**: C09
- **Setup**: Apply STAR-MAP to TauPS2APP mouse brain sections at multiple ages (e.g., 8 and 13 months), co-visualizing p-tau signal, microglia, and cell-type-defining transcripts.
- **Procedure**: Grid the tissue into fixed-size squares around p-tau-positive regions; quantify the covariation of cell-type composition with local p-tau density per grid square at each age; classify p-tau+ neurons by excitatory/inhibitory subtype at each time point; separately quantify p-tau enrichment within a fixed radius of amyloid plaques.
- **Expected outcome**: The dominant p-tau+ excitatory neuron subtype and the dominant p-tau+ inhibitory neuron subtype shift between the earlier and later time point, tracking spread of pathology from cortex toward hippocampus; oligodendrocytes show the strongest cell-type enrichment near high p-tau signal in white-matter-adjacent regions; p-tau is also enriched near plaques, attributable to dystrophic neurites rather than intact neuronal cell bodies.

## E09: Panel-based MERFISH activation scoring across aging mouse brain regions
- **Verifies**: C10
- **Setup**: Apply a curated MERFISH gene panel to mouse frontal cortex and striatum tissue sections spanning a range of ages.
- **Procedure**: Compute a per-cell "activation score" from a fixed subset of microglia genes and a fixed subset of astrocyte genes; correlate cluster-level activation score with age and with the inflammatory gene expression level of spatially adjacent oligodendrocyte clusters.
- **Expected outcome**: Microglial and astrocytic activation scores increase with age and co-vary spatially with oligodendrocyte inflammatory state, indicating coordinated (not independently regulated) glial aging responses within local tissue neighborhoods.

## E10: Construction and cross-dataset application of a spatial cell-aging clock
- **Verifies**: C11
- **Setup**: Apply a curated MERFISH gene panel across the full mouse lifespan to train a per-cell age-prediction model ("Spatial Ageing Clock"); apply the trained clock to independent published spatial transcriptomics datasets representing perturbation models (LPS challenge, EAE demyelination, localized demyelination injury, AD).
- **Procedure**: For each dataset, compute predicted cellular age as a function of the identity of spatially neighboring cell types (in particular, proximity to microglia vs. proximity to neural stem cells); validate a specific proximity-driven marker gene (Cd9) by immunostaining in NSC-adjacent tissue.
- **Expected outcome**: Cells near microglia show accelerated predicted aging across multiple independent perturbation datasets; cells near NSCs show a rejuvenating (decelerated aging) proximity effect, with an independently confirmed marker-gene signature.

## E11: Combined MERFISH and electron microscopy characterization of microglial substates in demyelination lesions
- **Verifies**: C12
- **Setup**: Induce localized white-matter demyelination (e.g., LPC injection) in mouse brain; apply MERFISH spatial transcriptomics and correlative electron microscopy to the same lesion tissue.
- **Procedure**: Identify microglia by lipid-droplet-laden ("foamy") morphology via EM; cross-reference the transcriptomic profile of foamy microglia against DAM and lipid/cholesterol metabolism gene sets; map the spatial position of foamy microglia relative to interferon-responsive microglia and other lesion cell types (oligodendrocytes, astrocytes, CD8+ T cells).
- **Expected outcome**: Foamy microglia co-express DAM and lipid-metabolism genes and are spatially restricted to the lesion center, in close proximity to a molecularly distinct interferon-responsive microglial subset and other glial/immune cell types — indicating spatially organized functional specialization within a single demyelination lesion.

## E12: Cross-platform corroboration via spatial proteomics and mRNA-protein correlation analysis
- **Verifies**: C13, C14
- **Setup**: Apply imaging-based spatial proteomics platforms (multiplexed antibody panels) to AD or innate-immune-challenge brain tissue; separately quantify mRNA and corresponding protein abundance for pro-inflammatory microglial genes following innate immune challenge.
- **Procedure**: Compare protein-based microglial subset/state calls against ST-derived microglial state calls in matched or comparable tissue; compute the correlation between mRNA fold-change and protein fold-change for the same pro-inflammatory gene set.
- **Expected outcome**: Spatial proteomics independently recovers plaque-associated microglial subsets consistent with ST findings, while mRNA and protein levels for at least some pro-inflammatory genes show incomplete correlation, indicating a post-transcriptional/translational regulatory layer not captured by transcriptomics alone.
