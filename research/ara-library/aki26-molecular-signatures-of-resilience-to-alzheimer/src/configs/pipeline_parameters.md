# Pipeline Parameters

Key parameters and thresholds by stage. All values from Methods.

## QC / integration
### Empty-droplet FDR
- **Value**: < 0.05 (DropletUtils) → 665,407 nuclei
- **Rationale**: distinguish cells from ambient RNA via knee/inflection points.
- **Source**: Methods, Preprocessing/QC.

### Minimum genes per nucleus (initial → final)
- **Value**: initial filter <200 genes removed (→549,074); final cutoff **300** genes (tested 200–500)
- **Rationale**: Ex5 has low gene counts; 300 balances retention vs quality; separate rescue of 200–300-gene nuclei (62,498; 48,849 kept at 99% scANVI probability).
- **Sensitivity**: high (drove a dedicated sensitivity analysis).
- **Source**: Methods; Supplementary Fig. 8.

### Mitochondrial content
- **Value**: >5% mito → discarded (1778 nuclei) → 424,528 final
- **Source**: Methods.

### Harmony integration variables
- **Value**: assay (Drop-seq / 10x v2 / 10x v3) + region (BA9/BA7/BA17); silhouette ≥ 0.8
- **Source**: Methods.

### Clustering (neuronal subsets)
- **Value**: 30 PCs, Leiden resolution 1.0; UMAP min_dist 0.6, spread 1.4 → 18 Ex + 19 In clusters
- **Source**: Methods.

### Top-marker thresholds
- **Value**: pts>0.2; pts_rest<0.1; pts/pts_rest>3; logFC>1.5; padj<0.05 (relaxed for Ex1/Ex2/Ex5: pts_rest<0.2, ratio>2)
- **Source**: Methods.

## scANVI
### Assignment probability threshold
- **Value**: 0.99 — **Rationale**: minimize false positives. **Source**: Methods.
### Model config
- **Value**: 2000 HVGs + top-200 markers/cluster + gene sets; 3 layers; 50 latent; ≤200 epochs; linear_classifier=True; n_samples_per_label=1000
- **Source**: Methods.

## Composition (scCODA / GLMM)
### scCODA credible effect
- **Value**: PIP > 0.95; formula `counts ~ Disease group + Sex + APOE genotype + Assay + Age`; automatic reference; min 500 genes/cell
- **Stress test**: sign-constrained β≤0 (HalfNormal prior), loss-only.
- **Source**: Methods; Fig. 4 caption.
### GLMM
- **Value**: beta regression, logit link; fixed effects assay/age/sex/APOE; donor random intercept; subtypes in <3 donors excluded
- **Source**: Methods.

## Differential gene expression
### Mixed-model DE filter
- **Value**: expression>20% in ≥1 condition; |logFC|>0.1; FDR<0.05 — **Source**: Methods.
### Bootstrap
- **Value**: 100 iterations, 50% nuclei subsampled; retain genes DE (same direction) in ≥20/100 — **Source**: Methods.
### Pseudobulk (pyDESeq2)
- **Value**: genes expressed in ≥20 nuclei; Benjamini–Hochberg padj<0.05 — **Source**: Methods.
### High-confidence definition
- **Value**: mixed model ∩ (bootstrap OR pseudobulk OR hdWGCNA top-50-by-kME) — **Source**: Methods.

## hdWGCNA
- **Value**: metacells (Methods: k=25, min 50 cells; repo script: k=20, max_shared=15, min_cells=50), group.by Author_Annotation; module reliability bootstrap 5000 iterations; top-50 genes/module by kME; `set.seed(12345)`
- **Note (source discrepancy):** Methods state metacell k=25; the released `hdwgcna_network.r` uses k=20 with max_shared=15. Both reproduced verbatim; not silently reconciled.
- **Source**: Methods; `execution/hdwgcna_network.r`.

## Functional enrichment
- **Value**: Enrichr padj<0.05, ≥3 genes (GTEx + SynGO backgrounds); Metascape min overlap 5, p<0.01, min enrichment 2.5; g:profiler GO MF/BP term size 10–1000, padj<0.05; top 50 pathways plotted
- **Source**: Methods.

## Functional validation
### AAV / calcium imaging
- **Value**: AAV MOI 5000 vg/cell (DIV7); 200 nM Aβ1–42 oligomers (DIV12); imaging DIV14 at 5 Hz, 100 s/field; Ca2+ transient threshold 0.2 ΔF/F0; 4 wells/condition (biological replicate), 2 fields/well, 3 GFP+ neurons/field
- **Source**: Methods.
### In vivo dosing
- **Value**: 12-month male mice; retro-orbital 1×10¹¹ vg (main); WB dose test 5×10¹⁰ vs 1×10¹¹ vg (n=3); sacrifice 30 days post-injection; analysis in SSC
- **Source**: Methods; Fig. 8.
### Statistics (mouse/in vitro)
- **Value**: Shapiro-Wilk normality; ROUT (Q=1%) outlier screen (none excluded); two-sided t-test / one-way ANOVA + Tukey; significance p<0.05; Prism 10
- **Source**: Statistics & Reproducibility.
