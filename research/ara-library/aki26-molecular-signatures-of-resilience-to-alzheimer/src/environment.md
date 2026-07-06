# Environment

Reproducibility record. Values grounded in Methods; software versions are those stated in the paper.

- **Language/runtime**: Python (Scanpy pipeline reported at Python 3.9.1; calcium-imaging analysis at Python 3.11.12); R (glmmTMB, hdWGCNA, Seurat, dplyr, tidyr).
- **Frameworks / key libraries (with versions where stated)**:
  - Alignment/QC: kb-python 0.26.0; DropletUtils; DoubletFinder 4.2; Scanpy; Harmony v1.2.2769.
  - Annotation/prediction: scANVI 1.0; spatialID 1.0.0.
  - Composition: scCODA 0.1.9; glmmTMB 1.1.11 (R).
  - DGE: MAST 1.24.1; lme4 1.1-34; pyDESeq2 0.3.5; bootstrap (100 iterations, in-house).
  - Networks: hdWGCNA 0.2.23 (Seurat / WGCNA / harmony / igraph).
  - Spatial: Xenium Ranger 3.1; squidpy 1.2.3; Space Ranger; Stereoscope.
  - Enrichment: GSEApy (Enrichr) 1.0.6; Metascape; g:profiler; Cytoscape.
  - Imaging/stats: CellProfiler (custom pipelines); ImageJ; GraphPad Prism 10; matplotlib; seaborn.
- **Hardware**: Not specified in paper (no GPU/CPU spec given). Wet-lab instruments: BD FACSAria II / Sony SH800 (FANS); Illumina NextSeq 500 / NovaSeq 6000 (sequencing); Zeiss LSM980 confocal; Zeiss Axio Imager M2/2; 10x Chromium; FlowJEM microfluidics (Drop-seq); Xenium Analyzer.
- **Random seeds**: hdWGCNA R script sets `set.seed(12345)`. Other seeds not specified in paper.
- **Protocols**: See `logic/solution/methods_pipeline.md`. Reporting per Nature Portfolio Reporting Summary (linked to article).

## Data sources
| Source | Identifier | Repository | Access | Notes |
|--------|-----------|------------|--------|-------|
| Raw snRNA-seq + metadata + processed digital expression matrices (newly generated) | **GSE263468** | NCBI GEO | open | Primary dataset |
| Reused snRNA-seq samples (8 of 243) | **GSE129308**, **GSE181715** | NCBI GEO | open | Prior-study samples |
| Interactive snRNA-seq exploration | CELLxGENE collection **0d35c0fd-ef0b-4b70-bce6-645a4660e5fa** | CZI CELLxGENE | open | cellxgene.cziscience.com |
| Xenium spatial dataset (16 sections; BA9+BA17; 4 AD + 4 control) | **10.5281/zenodo.16703438** | Zenodo | open | Spatial transcriptomics |
| Code + pretrained cell-type models | **10.5281/zenodo.18113528** (GitHub AkilaRanjith/Molecular-Signatures-of-Resilience-…) | Zenodo / GitHub | open, CC-BY-4.0 | ref 91 |
| Human reference genome | GRCh38, Ensembl 105 | Ensembl | open | Alignment index |
| External reference atlases | SEA-AD DLPFC/MTG; BICCN; Jorstad 2023; Mathys 2023; Green 2024 | see related_work.md | open | Annotation validation |
| Allen Human Brain Atlas ISH | experiments 80510718, 78937929 | human.brain-map.org | open | EYA4/KCNH8 histology (Fig. 3g,h) |

## Model organisms / key reagents
- Mice: AppSAA (B6.Cg-Apptm1.1Dnli/J, JAX #034711) and WT C57BL/6J (#000664); male only; 12 months for in vivo.
- AAV: PHP.eB-CaMKIIa-Kcnip4-P2A-EGFP (mouse Kcnip4 isoform 1, NCBI NP_001186171.1); control PHP.eB-CaMKIIa-EGFP (Addgene #50469-PHPeB); PHP.eB-Syn.NES-jRGECO1a.WPRE.SV40 (Addgene #100854-PHPeB).
- Key antibodies: anti-NeuN (Millipore MAB377; Sigma ABN90), anti-KCNIP4 (Proteintech 60133-1-Ig), anti-EYA4 (Thermo PA552113), anti-c-Fos (Synaptic Systems 226 308), anti-Arc (Synaptic Systems 156 111), anti-GFP (Invitrogen A11122), anti-VGLUT2 (Millipore MAB5504), anti-human amyloid-β (IBL 18584), anti-GFAP (Dako Z0334), anti-Iba1 (FujiFilm 019-19741).

## Ethics
Human tissue deidentified; NHSR determination. IRBs: UCLA/Easton, NIH Neurobiobank (Sepulveda PCC# 2015-060672 / VA #0002; Mt. Sinai HAR-13-059), Stanford IRB-33727. Animal: Stanford APLAC protocol ID 33824.
