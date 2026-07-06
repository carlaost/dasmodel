# Preprocessing

See `logic/solution/method.md` for the full staged computational pipeline. Summary of the
preprocessing / QC / normalization steps specifically (as distinct from downstream statistical
testing):

## Spatial transcriptomics (ST)
1. Space Ranger maps barcodes to Gencode 27 human genome reference; generates per-section FASTQ
   and count matrix.
2. Sections merged into a single Seurat v4.2.0 object.
3. Per-spot QC: spots with fewer than 500 measured genes removed.
4. `Seurat::SCTransform` normalization (regularized negative binomial regression) for clustering
   purposes only.
5. PCA on top 3,000 variable genes; Harmony integration (top 10 embeddings used) correcting for
   age, RIN, library batch, donor — used only to derive spot clusters (brain-region/layer labels),
   not for downstream quantitative comparisons.
6. All downstream differential-expression, cell-proportion, and ligand-receptor analyses use the
   pre-integration (non-SCTransform, non-Harmony-corrected) raw/pseudobulk count data.

## IHC image preprocessing
1. H&E images: 20x tiled (9x9, 10% overlap) acquisition, stitched in Adobe Photoshop.
2. IHC/IF images: 20x tiled (10x10, 16-bit) acquisition; background/shading correction via ImageJ
   BaSiC plugin; stitching (1% overlap) via ImageJ stitching plugin.
3. Cross-modality registration: adjacent IHC sections aligned to the middle/ST H&E section using
   7-12 manually placed landmark correspondences (ImageJ "Landmark Correspondences" plugin).
4. Artifact correction: grayscale morphological opening/closing (structural element sized above
   plaque/glial scale) to estimate and regress out large bright artifacts and local background
   inhomogeneity; border spots overlapping remaining bright artifacts excluded from analysis.
5. Per-spot average pixel intensity computed per channel (Aβ, GFAP, IBA1) within each spot's
   55-µm-diameter footprint.

## Pseudobulk construction for niche-contrast differential expression
1. Assign each gray-matter ST spot to a plaque-glia niche type via the Aβ/glia intensity
   stratification (see `src/configs/parameters.md`).
2. Sum UMI counts of all spots in a given niche type, per section, to build one pseudobulk sample
   per section per niche type.
3. Retain genes with CPM > 1 in ≥80% of sections; TMM-normalize (edgeR) and voom-transform (limma)
   the resulting pseudobulk matrix.
4. Exclude any section/niche-type combination with fewer than 50 contributing spots from that
   contrast.

## scRNA-seq (iPSC co-culture) preprocessing
1. CellRanger v6.0.1 generates raw count matrices from FASTQ.
2. CellBender v0.3.0 corrects for ambient RNA.
3. Seurat v4.2.0: cells with <2,000 or >9,000 genes and/or >7.5% mitochondrial reads removed;
   manual doublet removal (mixed cluster signatures) — 13,740 cells retained.
4. Data scaled and log-normalized; PCA on top 2,000 variable genes; UMAP on top 15 PCs;
   Louvain clustering (SNN neighbors=20, resolution=0.3).
5. For the Aβ-treated-iMGL-only subset (3,875 cells), steps 4 above are repeated independently on
   the subsetted data to derive iMGL1-4 subclusters.

## Co-expression network preprocessing (data-quality check, not a primary contrast)
1. Pseudobulk per donor (summed UMIs across all spots); genes filtered to ≥1 CPM in all samples;
   TMM-voom normalized.
2. `removeBatchEffect` (limma) adjusts for library batch, RIN, age, PMI prior to SpeakEasy
   consensus clustering.
