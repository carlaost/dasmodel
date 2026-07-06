# Methods Pipeline

End-to-end computational + experimental workflow. Steps grounded in Methods and mirrored by the
released code (`src/execution/`). Exact parameters are consolidated in `src/configs/analysis.md`.

## 1. Nuclei isolation and FANS
- ~100 mg cortical gray matter, Dounce homogenization in Tris/MgCl2/KCl/sucrose/DTT/protease+RNase inhibitor/0.1% Triton X-100; 40-µm strain.
- Iodixanol gradient (50%→29% layering; spin 13,500×g 20 min) to remove myelin.
- Anti-NeuN (MAB377) + Hoechst 34580; FANS (BD FACSAria II or Sony SH800) → two suspensions per sample: all nuclei (Hoechst+) and neuronal (Hoechst+/NeuN+).

## 2. snRNA-seq library prep and sequencing
- Drop-seq (modified; 200 nuclei/µl, 165 beads/µl, ~5% occupancy/doublet; 1% sarkosyl lysis + 72 °C 5 min heat) OR 10x Chromium 3' v2/v3 (~12,500 nuclei loaded, ~5000 captured).
- Illumina NextSeq 500 / NovaSeq 6000; 243 samples, 37 batches, ~75,000 reads/nucleus.

## 3. snRNA-seq preprocessing, QC, integration → clustering
- Alignment: kb-python 0.26.0 (GRCh38, Ensembl 105), Lamanno spliced/unspliced; unspliced counts used downstream.
- Empty-droplet removal: DropletUtils (FDR<0.05) → 665,407 nuclei; <200-gene filter → 549,074.
- Doublets: DoubletFinder 4.2 (v2 2.85%, v3 1.74%, Drop-seq 0.003%); doublet clusters (17,442 nuclei) excluded.
- Scanpy (Python 3.9.1): HVG (dispersion 0.5), 50 PCs, 15-neighbor graph, Leiden (correlation distance).
- Integration: Harmony v1.2.2769 over assay (Drop-seq/10x v2/10x v3) and region (BA9/BA7/BA17); silhouette ≥0.8.
- Final gene cutoff 300 (tested 200–500); mito>5% (1778 nuclei) removed → **424,528** high-quality nuclei.
- Recluster excitatory (282,930) and inhibitory (79,294) subsets: 30 PCs, resolution 1.0 → 18 Ex + 19 In clusters. Cluster naming: canonical subclass markers (CUX2/RORB/THEMIS/FEZF2; LHX6/ADARB2) + 1–3 top markers; plus 7–10-gene subtype gene sets.
- Glia reclustered (10 PCs, res 0.1–0.3): 4 astrocyte, 4 microglia, 2 oligodendrocyte states.

## 4. Cross-dataset annotation
- scANVI 1.0 model (2000 HVGs + top-200 markers/cluster + gene sets; 3 layers, 50 latent, ≤200 epochs; linear_classifier=True; n_samples_per_label=1000; assignment threshold 0.99).
- Cosine-distance matrix vs SEA-AD DLPFC (top-10 markers/cluster, 3000 HVGs).
- Applied to SEA-AD DLPFC/MTG, Mathys 2023, Green 2024, Jorstad 2023.

## 5. Spatial transcriptomics
- **Xenium**: Xenium Ranger 3.1 + squidpy 1.2.3; multimodal segmentation (ribosomal-RNA boundary + 5 µm DAPI expansion). Major-cell-type annotation = ensemble of (1) manual kNN/Leiden + canonical markers, (2) heuristic highest-transcript Python script, (3) spatialID 1.0.0 DNN (trained on SEA-AD DLPFC), (4) ingest label transfer of SEA-AD DLPFC; consensus confidence >0.5 retained. Subtype annotation = ingest label transfer from snRNA-seq (neurons >50 transcripts; top-15 PCs, k=20 kNN).
- **Visium**: Space Ranger; Stereoscope deconvolution (snRNA-seq reference VAE, 200 epochs; spatial model ≤2000 epochs).

## 6. Neuronal-subtype composition analysis
- Per-donor per-subtype counts (min 500 genes/cell), BA9 and BA17 separately.
- **scCODA 0.1.9**: `cell type counts ~ Disease group + Sex + APOE genotype + Assay + Age` (automatic reference; credible at PIP>0.95). Stress test: sign-constrained β≤0 (HalfNormal prior) "loss-only" model.
- **GLMM (glmmTMB 1.1.11, R)**: per-subtype beta regression of donor proportion (logit link), fixed effects assay/age/sex/APOE, donor random intercept; subtypes in <3 donors excluded.

## 7. Differential gene expression (high-confidence consensus)
- 'early' = low vs intermediate; 'late' = intermediate vs high; per subtype × region.
- **MAST 1.24.1 + lme4 1.1-34** zero-inflated mixed model: `Zlm(~condition + (1|donor) + cngeneson + Assay + Age + Sex + RIN + total_counts, method='glmer')`; thresholds expression>20% in ≥1 condition, |logFC|>0.1, FDR<0.05.
- **Bootstrap**: 100 iterations, 50% nuclei subsampled; retain genes DE (same direction) in ≥20/100 iterations.
- **Pseudobulk pyDESeq2 0.3.5**: per-donor aggregated counts; genes in ≥20 nuclei; Benjamini–Hochberg padj<0.05.
- **High-confidence** = mixed model ∩ (bootstrap OR pseudobulk OR hdWGCNA top-50-by-kME).

## 8. Co-expression network analysis
- hdWGCNA 0.2.23 (Seurat) on metacells (`group.by=Author_Annotation`, k=25, min 50 cells, Harmony reduction); soft-power selection; module detection by hierarchical clustering; module reliability by 5000-iteration bootstrap; top-50 genes/module by kME; hub-gene/module-network plots; differential module eigengenes (FindDMEs) early/late.

## 9. Functional enrichment
- Enrichr (GSEApy 1.0.6; GTEx + SynGO backgrounds), Metascape (min overlap 5, p<0.01, min enrichment 2.5), g:profiler (GO MF/BP, term size 10–1000, padj<0.05); networks via Cytoscape.

## 10. Histology / imaging analysis
- RNAscope ISH (EYA4/MME/GABRG1/SLC17A7); immunofluorescence KCNIP4/EYA4/NeuN; VGLUT2 DAB IHC; confocal (Zeiss LSM980). CellProfiler custom pipelines for NeuN segmentation, EYA4+ classification, KCNIP4 intensity (human) and GFP+/GFP− segmentation + c-Fos/Arc quantification (mouse).

## 11. Functional validation of KCNIP4
- **AAV vector**: PHP.eB-CaMKIIa-Kcnip4-P2A-EGFP (mouse Kcnip4 isoform 1, NP_001186171.1); control PHP.eB-CaMKIIa-EGFP; jRGECO1a AAV for calcium imaging (Vector Biolabs / Addgene).
- **In vitro**: P0 cortical neurons, transduce DIV7 (MOI 5000 vg/cell), 200 nM Aβ1–42 oligomers DIV12, calcium imaging DIV14 (jRGECO1a, 5 Hz, 100 s), transient detection >0.2 ΔF/F0 (Python 3.11.12); TUNEL assay control.
- **In vivo**: 12-mo male AppSAA + WT; retro-orbital 1×10¹¹ vg (dose test 5×10¹⁰ vs 1×10¹¹, WB, n=3); sacrifice 30 d; c-Fos/Arc/amyloid-β/GFAP/IBA1 IHC in SSC; stats in Prism 10 (t-test / one-way ANOVA + Tukey).
