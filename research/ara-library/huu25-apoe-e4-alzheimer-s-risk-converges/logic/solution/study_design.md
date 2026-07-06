# Study Design

## Cohort
- **Donors**: 31 postmortem human ERC donors initially dissected; final analyzed cohort = 30 donors after dropping one sample (see Data QC below). All neurotypical (no clinical AD diagnosis, minimal-to-no AD pathology).
- **Risk stratification (final n=30)**:
  - APOE carrier status: E2+ (E2/E2, E2/E3) n=14; E4+ (E3/E4, E4/E4) n=16.
  - Ancestry: African ancestry (AA, sub-Saharan) n=14; European ancestry (EA) n=16.
  - Sex: 21 male, 9 female (70% male).
  - Age at death: 30–68 years.
- **Cross-tab (Figure 1A)**: EA/E2+ = 8 (m7,f1); EA/E4+ = 6 (m6,f0); AA/E2+ = 6 (m3,f3); AA/E4+ = 10 (m5,f5).
- **Consent/ethics**: Maryland Dept. of Health IRB #12-24; County of Santa Clara Medical Examiner (WCG #20111080); NIMH IRP NIH #90-M-0142.

## Assays (paired, per donor)
- **snRNA-seq**: 10x Chromium 3' v3.1; nuclei isolated (dounce + EZ lysis), PI-stained, FANS-sorted (14,000 PI+ nuclei/donor, target ~9,000 recovered); sequenced on NovaSeq 6000, min 50,000 reads/nucleus. n=31 samples.
- **SRT (Visium)**: 10x Visium Spatial Gene Expression; one 10 μm section per donor, H&E imaged (Leica CS2), 18-min permeabilization; NovaSeq 6000, min 60,000 reads/spot. 31 samples.
- **Anatomical validation**: multiplexed smFISH (RNAScope) for RELN (L1), FREM3 (L3), TRABD2A (L5), MBP (WM) to confirm ERC inclusion.
- **pTau**: RNAScope-IF (AT8 anti-pTau + MBP + SNAP25), one section/donor; pTau-positive if ≥3 discrete signals by two blinded raters.
- **Genotyping/ancestry**: Illumina BeadChip; Plink QC; TOPMed imputation (GRCh38); FLARE local/global ancestry using 1000 Genomes YRI/CHB/CEU references.

## Analysis pipeline (high level)
1. **Visium**: VistoSeg slide split → SpaceRanger align/count → spatialLIBD QC + SpotSweeper outlier removal → nnSVG SVGs + DLPFC layer markers → PCA (scater) → harmony → BayesSpace clustering (k=9) → SpD annotation via spatial registration to DLPFC and ERC references + MeanRatio markers.
2. **snRNA-seq**: CellRanger → DropletUtils emptyDrops → scDblFinder doublet removal → adaptive-MAD QC → GLM-PCA (scry) → harmony → graph clustering (scran/igraph walktrap) → iterative subclustering → ScType + registration annotation → 38 fine subclusters in 8 broad cell types.
3. **Integration**: RCTD spot deconvolution; spatial registration between SpDs and subclusters.
4. **Differential expression**: pseudobulk (registration_pseudobulk, min_ncells=10) → edgeR filtering → voomLmFit + limma, carrier / ancestry / sex models.
5. **Composition**: crumblr (CLR + dream) differential proportion.
6. **Functional**: clusterProfiler GO overrepresentation + rrvgo parent terms.
7. **Trajectory**: TSCAN on OPC+Oligo subset.
8. **Cross-dataset**: Fisher-exact gene-set enrichment vs Grubman et al. and Blanchard et al.
9. **Cell-cell communication**: LIANA+ (snRNA-seq LR pairs + Visium spatial bivariate validation).
10. **Multi-omic integration**: MOFAcellulaR (7 factors) across SpD + subcluster pseudobulk views; factor–covariate association.

## Statistical models
- Carrier DGE: `~0 + APOE_syn + Sex + Age + Anc_Afr + pseudo_expr_chrM_ratio` (block: exp_round for snRNA-seq, Visium_slide for Visium).
- Ancestry-specific: `~0 + carrier_Anc + Sex + Age + pseudo_expr_chrM_ratio`.
- Sex-specific: `~0 + carrier_Sex + Sex + Age + pseudo_expr_chrM_ratio` (X/Y genes excluded, ancestry not modeled).
- Differential proportion: `dream(~ APOE_carrier + Sex + Anc_Afr + Age + [Visium_slide|exp_round])`, coef = `APOE_carrierE4+`.

## Design rationale
- Balanced AA/EA (14/16) gives power for ancestry-interaction discovery — a distinguishing feature vs prior AD studies.
- Neurotypical middle-aged donors isolate *risk* biology from established disease.
- Paired modalities let SRT localize changes spatially and snRNA-seq resolve them to fine subtypes, with MOFA reconciling both.
