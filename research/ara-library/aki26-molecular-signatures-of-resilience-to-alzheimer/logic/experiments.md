# Experiments

Declarative verification/analysis plans. Directional only — exact values live in `evidence/`.

---

## E01: snRNA-seq profiling and neuronal-subtype clustering
- **Verifies**: C02, C10 (and underpins C01)
- **Setup**:
  - Tissue: postmortem human neocortex, 3 regions (BA9, BA7, BA17), 46 donors, Braak 0–VI.
  - Assay: FANS (NeuN+ and all-nuclei) → Drop-seq or 10x Chromium 3' v2/v3 snRNA-seq.
  - Pipeline: kb-python (GRCh38, Ensembl 105) → DropletUtils → DoubletFinder → Scanpy QC → Harmony integration → Leiden clustering.
- **Procedure**:
  1. Enrich neurons by FANS; sequence both nuclear suspensions.
  2. Align, remove empty droplets, filter by gene count and mitochondrial %, remove doublet clusters.
  3. Integrate over assay and region; recluster excitatory and inhibitory subsets.
  4. Annotate clusters by canonical subclass markers + 1–3 top marker genes; select 7–10-gene subtype gene sets.
- **Metrics**: nuclei counts (total/neuronal/per-cluster); silhouette score; WCSS; marker-gene specificity.
- **Expected outcome**: A reproducible taxonomy of excitatory and inhibitory neuronal subtypes distinguishable by small consistent gene sets across regions, with L4 IT resolving into distinct subtypes.
- **Baselines**: Concordance with reference atlases (SEA-AD, BICCN).
- **Dependencies**: none

## E02: Xenium spatial validation of subtype laminar distribution
- **Verifies**: C01, C10
- **Setup**:
  - Platform: 10x Genomics Xenium; 16 sections (8 BA9, 8 BA17), 4 AD + 4 control donors; 266-gene brain panel + custom 100-gene panel; cell-segmentation add-on.
  - Annotation: 4-method ensemble for major cell types; ingest label transfer from snRNA-seq for subtypes.
- **Procedure**:
  1. Segment cells (RNA-based boundary + DAPI expansion).
  2. Annotate major types by ensemble voting; annotate neuronal subtypes by label transfer.
  3. Map excitatory subtypes across layers; compare BA9 vs BA17 (and adjacent BA18).
- **Metrics**: cells per section; layer-resolved subtype abundance; consensus confidence.
- **Expected outcome**: Subtype layer positions match snRNA-seq labels; Ex5 enriched in BA17 L4 (deep, sharp L5 boundary), Ex6/Ex7 enriched in BA9 L4.
- **Baselines**: Independent Visium dataset (different panel) reproduces regional patterns.
- **Dependencies**: E01

## E03: Compositional analysis of subtype proportions across pathology
- **Verifies**: C01, C02
- **Setup**:
  - Data: per-donor per-subtype counts, BA9 and BA17 separately, min 500 genes/cell.
  - Models: scCODA (Bayesian Dirichlet-multinomial) and GLMM (beta regression, logit link) covarying sex, age, APOE, assay.
- **Procedure**:
  1. Build donor×subtype count matrices; compute proportions.
  2. Fit scCODA (automatic reference; credible at PIP>0.95); fit per-subtype GLMM.
  3. Run sensitivity analyses: min-500-gene subclass annotation; 200–300-gene nuclei rescue via scANVI; sign-constrained "loss-only" scCODA stress test.
- **Metrics**: log2-fold change (high vs low), PIP, FDR/p-values per subtype.
- **Expected outcome**: L4 IT (esp. Ex5) relatively increases with pathology (credible in BA9; trend in BA17); vulnerable L2/3 IT and SST interneurons trend downward.
- **Baselines**: two independent methods (scCODA vs GLMM) must agree; annotation-method robustness.
- **Dependencies**: E01

## E04: High-confidence differential gene expression across region × stage
- **Verifies**: C03, C04, C05
- **Setup**:
  - Comparisons: 'early' = low vs intermediate, 'late' = intermediate vs high; per subtype; BA9 and BA17.
  - Methods: zero-inflated mixed model (MAST + lme4), bootstrap (100 iterations, 50% subsampling), pseudobulk pyDESeq2.
- **Procedure**:
  1. Run each DGE method with donor random effect and covariates (cngeneson, assay, age, sex, RIN, total counts).
  2. Define high-confidence DE genes = LMM ∩ (bootstrap or pseudobulk or hdWGCNA top-50).
  3. Intersect across the four region×stage conditions (UpSet); enrich pathways (Enrichr/Metascape/g:profiler).
- **Metrics**: DE-gene counts (up/down), shared-gene intersections, enrichment FDR, average logFC.
- **Expected outcome**: More DE genes in BA9 than BA17 and in late than early; resilient Ex5 shows early upregulation of synaptic/calcium/neuroprotection genes and of KCNIP4.
- **Baselines**: Parallel BINCC-annotated min-500-gene analysis for overlap.
- **Dependencies**: E01

## E05: hdWGCNA co-expression network analysis
- **Verifies**: C09 (supports C04, C05)
- **Setup**:
  - Tool: hdWGCNA (Seurat) on metacells (k=25, min 50 cells), Harmony batch correction; per neuronal subtype × region.
  - Focus: vulnerable Ex2 vs resilient Ex5, BA9 and BA17.
- **Procedure**:
  1. Build metacells; construct co-expression network; identify modules by hierarchical clustering; bootstrap module reliability (5000 iterations).
  2. Rank genes by kME; retain top 50 per module; identify hub genes.
  3. Test differential module eigengenes early/late; enrich module functions.
- **Metrics**: kME, module membership, hub-gene identity, enrichment terms.
- **Expected outcome**: Ex5 candidate resilience modules (BA17 M2/M3, BA9 M2/M3/M4) upregulated early, containing KCNIP4 as hub, enriched for trans-synaptic signaling, calcium homeostasis, excitability.
- **Baselines**: contrast against Ex2 modules.
- **Dependencies**: E01

## E06: KCNIP4 expression across disease stages (targeted LMM)
- **Verifies**: C05
- **Setup**: MAST linear mixed model of KCNIP4 across low/intermediate/high groups in Ex2 and Ex5, BA9 and BA17; fixed covariates assay, sex, RIN, total counts; random effect donor.
- **Procedure**: Estimate KCNIP4 expression per group per subtype/region; visualize (violin plots).
- **Metrics**: log-normalized / estimated mean KCNIP4 expression per group.
- **Expected outcome**: KCNIP4 increases with disease in resilient Ex5; diverges from vulnerable Ex2.
- **Baselines**: cell-type distribution of KCNIP4 (predominant in excitatory neurons and OPCs).
- **Dependencies**: E01, E04

## E07: KCNIP4 protein quantification by immunohistochemistry
- **Verifies**: C06
- **Setup**: Immunofluorescence for KCNIP4/EYA4/NeuN on BA17 cryosections, low/intermediate/high (n=6 donors/group); CellProfiler segmentation; one-way ANOVA + two-sided Tukey.
- **Procedure**: Segment NeuN+ neurons; classify L4 EYA4+, L4 EYA4−, L2/3; measure mean KCNIP4 soma intensity; compare across stages.
- **Metrics**: mean KCNIP4 intensity per neuronal class per stage.
- **Expected outcome**: Higher KCNIP4 in L4 EYA4+ at intermediate stage; lower in L2/3 at intermediate/high.
- **Baselines**: L4 EYA4− neurons as within-layer control.
- **Dependencies**: E06

## E08: In vitro calcium imaging of Kcnip4 overexpression
- **Verifies**: C07
- **Setup**: Primary P0 mouse cortical neurons; AAV-PHP.eB-CaMKIIa-Kcnip4-P2A-EGFP vs control EGFP AAV (MOI 5000 vg/cell), co-transduced with jRGECO1a AAV; 200 nM Aβ1–42 oligomers or vehicle at DIV12; imaging at DIV14 (5 Hz, 100 s/field); TUNEL control.
- **Procedure**: Extract ΔF/F0 traces from GFP+ somas; detect Ca2+ transients (>0.2 ΔF/F0); average event frequency per well (biological replicate: 4 wells/condition).
- **Metrics**: Ca2+ transient event frequency (events/min); TUNEL+ count.
- **Expected outcome**: Kcnip4 lowers transient frequency vs control, basally and under Aβ; no TUNEL+ neurons (no toxicity).
- **Baselines**: GFP-only AAV; vehicle vs Aβ.
- **Dependencies**: none (functional validation of C05)

## E09: In vivo AAV Kcnip4 in AppSAA mice — activity markers and pathology
- **Verifies**: C08
- **Setup**: 12-month-old male AppSAA and WT mice; retro-orbital 1×10¹¹ vg Kcnip4 or control AAV; tissue at 30 days; WB dose test (5×10¹⁰ vs 1×10¹¹ vg, n=3); IHC for c-Fos, Arc, amyloid-β, GFAP, IBA1 in SSC; CellProfiler quantification; t-test / one-way ANOVA + Tukey.
- **Procedure**: Confirm KCNIP4 protein increase (WB); quantify transduction (%GFP+); compare c-Fos+ proportion and Arc intensity in GFP+ vs GFP− and across groups; quantify amyloid/GFAP/IBA1 stained area.
- **Metrics**: KCNIP4 WB signal; %GFP+; %c-Fos+ neurons; mean Arc intensity; stained-area % (amyloid/GFAP/IBA1).
- **Expected outcome**: Kcnip4 reduces c-Fos/Arc in transduced AppSAA neurons and reverses AppSAA elevation; reduces IBA1; no change in amyloid or GFAP.
- **Baselines**: control AAV; WT vs AppSAA; GFP− neurons.
- **Dependencies**: E08

## E10: Cross-dataset cell-identity prediction (scANVI)
- **Verifies**: C10
- **Setup**: scANVI model trained on the authors' 18 Ex / 19 In clusters (2000 HVGs + top-200 markers/cluster + gene sets; batch key = assay×region); applied to reference datasets (SEA-AD DLPFC & MTG, Mathys 2023, Green 2024, Jorstad 2023); assignment probability threshold 0.99.
- **Procedure**: Predict cluster identity of external excitatory cells; quantify Ex5 fraction per dataset/region; compare cosine distance and marker expression.
- **Metrics**: predicted Ex5 counts and fractions; sensitivity/specificity vs author annotations.
- **Expected outcome**: Ex5 enriched in the BA17-origin reference and rare in prefrontal references, confirming BA17-specialization.
- **Baselines**: author-annotated vs predicted labels.
- **Dependencies**: E01
