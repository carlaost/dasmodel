# Concepts

## APOE carrier status (E2+ / E4+)
- **Notation**: E2+ (E2/E2, E2/E3); E4+ (E3/E4, E4/E4)
- **Definition**: The study's primary risk axis, grouping donors by presence of the AD-protective E2 allele versus the AD-risk E4 allele at the Apolipoprotein E locus. Encoded as the `APOE_carrier` / `APOE_syn` covariate and contrasted as `APOE_carrierE4+`.
- **Boundary conditions**: E3/E3 homozygotes are not a group here; the cohort was selected for allelic variation (E2/E2, E2/E3, E3/E4, E4/E4). All donors are neurotypical (no clinical AD).
- **Related concepts**: Spatial domain, Fine subcluster, Pseudobulk DGE

## Spatial domain (SpD / Sp9D)
- **Notation**: L~Sp{k}D{d}, e.g. WM.uf~Sp9D7
- **Definition**: A transcriptionally distinct region of ERC tissue identified by spatially-aware BayesSpace clustering of Visium spots at resolution k=9. Named `L~Sp k D d` where L is the layer annotation of domain d at clustering resolution k. Nine SpDs were defined: Vasc~Sp9D8, L1~Sp9D5, L2.3~Sp9D1, LD~Sp9D2, Inhib~Sp9D9, L5~Sp9D3, L6~Sp9D4, WM.uf~Sp9D7, WM~Sp9D6.
- **Boundary conditions**: Defined at k=9 (optimal by BayesSpace qTune negative log-likelihood); ERC lamination is less discrete than DLPFC, so L2–L4 domains did not register cleanly to DLPFC layers.
- **Related concepts**: Spatial registration, Laminar desiccans, Fine subcluster

## Fine subcluster (cell-type subcluster)
- **Notation**: e.g. Oligo.3, Astro.3, OPC.5, Excit.L2
- **Definition**: One of 38 fine-resolution snRNA-seq clusters nested within 8 broad cell types (Astro, Macro, Micro, Oligo, OPC, Vasc, Excit, Inhib), derived by iterative graph-based clustering + subclustering of 122,004 high-quality nuclei.
- **Boundary conditions**: Some subclusters have few cells per donor, limiting DGE power (e.g. ~53 vascular cells/donor).
- **Related concepts**: Broad cell type, Spatial registration, MeanRatio marker

## Non-myelinating oligodendrocyte (Oligo.3)
- **Notation**: Oligo.3
- **Definition**: The oligodendrocyte subcluster identified as the primary locus of APOE E4+ transcriptional change; transcriptionally closest to OPCs (trajectory), low expression of mature myelination markers, proposed to be in a differentiating (E2+) versus immune-reactive/maturation-stalled (E4+) state.
- **Boundary conditions**: Expresses very low APOE, so the APOE effect on it is likely indirect (e.g. via astrocytes).
- **Related concepts**: Fine subcluster, Trajectory analysis, Myelination

## Spatial registration
- **Notation**: —
- **Definition**: A `spatialLIBD` framework that computes pairwise correlations between enrichment t-statistics of two datasets to align domains/clusters (e.g. ERC SpDs vs DLPFC reference layers, or SpDs vs snRNA-seq subclusters). High-confidence matches: cor > 0.5, merge ratio = 0.1 (marked "X"); low-confidence marked "*".
- **Boundary conditions**: Correlational; provides annotation support, not proof of identity.
- **Related concepts**: Spatial domain, Fine subcluster

## Pseudobulk differential gene expression (pseudobulk DGE)
- **Notation**: —
- **Definition**: Aggregating spots/nuclei into per-sample-per-cluster pseudobulk profiles, then modeling with covariate-adjusted linear models (voomLmFit / limma), enabling adjustment for sample-level covariates, batch, heteroscedasticity, and zero inflation. Contrast fit: `~0 + APOE_syn + Sex + Age + Anc_Afr + pseudo_expr_chrM_ratio`.
- **Boundary conditions**: Requires ≥10 cells/spots per pseudobulk sample (min_ncells default) and ≥2 pseudobulk samples per carrier group; underpowered for rare subclusters.
- **Related concepts**: APOE carrier status, Fine subcluster, Spatial domain

## Multi-Omics Factor Analysis (MOFA) / multicellular factor
- **Notation**: MOFA factor (e.g. factor 3), R²
- **Definition**: An unsupervised framework (MOFAcellulaR) that learns latent factors from multiple pseudobulk "views" (SRT SpDs and snRNA-seq subclusters), assigning per-gene weights within each view and one score per donor per factor; donor scores are tested against covariates. Here 7 factors were computed.
- **Boundary conditions**: Enables integration across views even when genes are not shared; associations FDR-corrected with each factor as a test.
- **Related concepts**: Pseudobulk DGE, Spatial domain, Fine subcluster

## Differential proportion analysis (crumblr)
- **Notation**: CLR
- **Definition**: Testing for changes in cell-type / SpD composition across covariates using centered-log-ratio (CLR) transformed proportions modeled with `dream` in variancePartition; used to test SpD and subcluster frequency differences by APOE carrier status, sex, and age.
- **Boundary conditions**: Composition analyses in snRNA-seq can be biased; validation with orthogonal assays recommended.
- **Related concepts**: Fine subcluster, Spatial domain

## Cell-cell communication (CCC) / ligand-receptor (LR) pair
- **Notation**: LR pair; magnitude_rank
- **Definition**: LIANA+ inference of ligand-receptor interactions between subcluster pairs from snRNA-seq, retained when significant (magnitude_rank < 0.05) in ≥20 of 30 samples, with spatial validation via bivariate Moran's-type co-expression scores in Visium.
- **Boundary conditions**: Recurrence threshold (≥20/30 samples) defines "commonly observed"; only Oligo.3 DEGs overlapped commonly observed LR interactions.
- **Related concepts**: Fine subcluster, Non-myelinating oligodendrocyte

## pTau pathology annotation
- **Notation**: t+ / t−
- **Definition**: Presence of phosphorylated-tau (AT8) accumulation in ERC assessed by RNAScope-IF; a section is pTau-positive if ≥3 discrete pTau signals were seen by two blinded experimenters. Used because only 18 donors had Braak staging.
- **Boundary conditions**: Semi-quantitative, visual, adjacent-section based; 9 of 31 samples pTau-positive, 22 pTau-negative.
- **Related concepts**: MOFA factor, APOE carrier status
