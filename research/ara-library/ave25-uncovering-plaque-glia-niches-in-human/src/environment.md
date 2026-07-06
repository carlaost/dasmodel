# Environment

- **Language/runtime**: R (Seurat v4.2.0 pipeline); no version of R itself is stated in the paper.
- **Framework / key software packages** (with stated versions where given):
  - Space Ranger (10x Genomics) — FASTQ generation, barcode mapping, count matrices
  - Seurat v4.2.0 (R) — object management, SCTransform normalization, clustering, marker
    identification (`FindMarkers`, Wilcoxon rank-sum + Bonferroni)
  - Harmony v0.1.0 — batch integration for spot clustering
  - spatialLIBD v7.5 — cortical-layer cluster annotation reference
  - BayesSpace — comparator spatial-clustering method (version not specified in paper)
  - cell2location — cell-type deconvolution (version not specified in paper)
  - edgeR v3.36.0 — TMM normalization
  - limma v3.50.1 / v3.50.3 — voom transform, `removeBatchEffect`, `duplicateCorrelation`
  - WGCNA v1.70-3 — `modulePreservation` (Zsummary statistic)
  - SpeakEasy (SE) v1.0 — consensus co-expression clustering
  - gprofiler2 v0.2.1 — GO/pathway enrichment (g:GOSt, g:SCS correction)
  - GSEA (Subramanian et al. 2005 method) — gene set enrichment testing (implementation/version not
    specified in paper)
  - NEBULA — negative binomial mixed model for IHC count outcomes (version not specified in paper)
  - NICHES v1.0.0 with Omnipath v3.2.8 — ligand-receptor spatial signaling inference
  - CellRanger v6.0.1 — scRNA-seq FASTQ processing
  - CellBender v0.3.0 — ambient RNA correction
  - ImageJ (with BaSiC plugin, "Landmark Correspondences" plugin) — IHC image stitching, shading
    correction, and cross-section registration
  - Adobe Photoshop 23.4.2 — H&E image stitching
  - NIS-Elements AR 5.11.01 (64-bit) — brightfield image acquisition software
- **Hardware**:
  - Illumina NovaSeq (ST sequencing, 3 batches, minimum 50,000 raw reads/spot target)
  - NovaSeq 6000 (scRNA-seq, ~50,000 reads/cell target)
  - Nikon Ti2 microscope with NIS-Elements AR (H&E brightfield imaging)
  - ThermoFisher CellInsight CX7 LZR High Content Analysis (HCA) platform (IHC/IF imaging, 20x)
  - SpectraMax M3 plate reader (Qubit 1x dsDNA HS library quantification)
  - Agilent Fragment Analyzer (library size distribution)
  - Countess II (Invitrogen) — cell counting (trypan blue)
  - GPU/CPU compute specifications: Not specified in paper
- **Data sources**:
  - ROSMAP (Religious Orders Study and Memory and Aging Project) cohort — 21 donors for the primary
    ST-IHC dataset (13 AD, 8 NCI, all female, DLPFC); 9 additional AD ROSMAP participants for FFPE
    plaque-typing validation; 10 additional AD individuals for FFPE functional-validation IHC.
  - Published ROSMAP DLPFC single-nucleus RNA-seq dataset (Mathys et al. 2019) — used as
    cell2location reference (44 cell types / 8 major types).
  - Published bulk RNA-seq network from 478 ROSMAP/aging-brain donors (Mostafavi et al. 2018) —
    used for co-expression module preservation testing.
  - Human microglial state gene sets (Sun et al. 2023, 12 states MG0-MG12) — external GSEA
    reference.
  - Mouse AD-model gene modules: PIG/OLIG (Chen et al. 2020), DAM (Keren-Shaul et al. 2017), DAA
    (Habib et al. 2020) — external GSEA reference.
  - iPSC lines: AICS-0090-391 (Coriell Institute) for iMGL differentiation; BR28 (obtained from Dr.
    Tracy Young-Pearse) for astrocyte/neuron differentiation.
  - Raw and normalized ST + paired IHC image data deposited at Synapse, accession **syn53141470**.
  - Differentially expressed genes, differentially expressed LRs, gene modules, and ST/scRNA-seq
    cluster marker genes are provided as Supplementary Information (Supplementary files 1-14,
    XLSX/CSV/DOCX; not included in the PDF provided as input to this ARA — see
    `evidence/README.md`).
- **Key dependencies**: See package list above; no `requirements.txt`/`environment.yml`/container
  definition is provided in the paper.
- **Protocols**:
  - Spatial transcriptomics: 10x Genomics Visium Spatial Gene Expression User Guide (CG000239).
  - iMGL differentiation: Abud et al. 2017 and McQuade et al. 2018 protocols (with minor
    modifications).
  - Astrocyte/neuron differentiation: STEMCELL Technologies astrocyte differentiation/maturation
    protocol (kits 100-0013, 100-0016).
  - Aβ1-42 oligomer preparation: Fujifilm/Cellular Dynamics Labeling Amyloid Beta protocol
    (rPeptide amyloid-beta aggregation kit).
  - Ethics: ROS and MAP each separately approved by a Rush University Medical Center IRB; written
    informed consent and Anatomic Gift Act signed by all participants for brain donation and data
    use.
- **Random seeds**: Not specified in paper.
- **Analytical vs. computational nature**: This is a wet-lab-generated, computationally analyzed
  dataset (not a purely analytical/theoretical work); no released code repository is cited in the
  paper, so `src/` in this ARA captures environment/configuration facts only (see
  `src/configs/analysis_parameters.md`) — no code stub is fabricated (see Rule 14 in the compiler
  skill: a prose-only method description is not re-encoded as code).
