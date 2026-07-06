---
title: "Molecular signatures of resilience to Alzheimer's disease in neocortical layer 4 neurons"
authors: ["S. Akila Parvathy Dharshini", "Jorge Sanz-Ros", "Jie Pan", "Weijing Tang", "Kristen Vallejo", "Yu Chen Liu", "Marcos Otero-Garcia", "Inma Cobos"]
year: 2026
venue: "Nature Communications 17:2223"
doi: "10.1038/s41467-026-68920-4"
ara_version: "1.0"
domain: "Neuroscience — single-nucleus & spatial transcriptomics of Alzheimer's disease; selective neuronal vulnerability/resilience"
keywords: ["Alzheimer's disease", "selective neuronal vulnerability", "resilience", "layer 4 excitatory neurons", "single-nucleus RNA-seq", "spatial transcriptomics", "Xenium", "KCNIP4", "neuronal hyperexcitability", "AppSAA mouse", "hdWGCNA", "RORB/CUX2/EYA4"]
grounding: full-text
claims_summary:
  - "A resilient L4 IT excitatory population (Ex5: RORB/CUX2/EYA4/LAMA3) enriched in primary visual cortex (BA17) increases in relative proportion with AD pathology (scCODA high-vs-low log2FC: BA9 1.75, BA17 0.46; GLMM BA9 FDR=0.008)."
  - "L4 IT excitatory neurons are relatively preserved during AD progression across association (BA9) and primary (BA17) neocortex."
  - "Integrated multi-method DGE yielded 986 high-confidence DE genes; 54 shared across all four region×stage conditions; DE-gene counts are higher in BA9 than BA17 and higher in 'late' than 'early' stages."
  - "Early-stage resilient neurons upregulate synapse-maintenance, plasticity, calcium-homeostasis, and neuroprotection genes (GRIN2A, RORA, NRXN1, NLGN1, NCAM2, FGF14, NRG3, NEGR1, CSMD1)."
  - "KCNIP4 (Kv-channel-interacting protein) is consistently upregulated in resilient Ex5 L4 neurons at early AD stages in both BA9 and BA17, and downregulated in vulnerable Ex2 L2/3 neurons."
  - "KCNIP4 protein is significantly higher in L4 EYA4+ neurons at intermediate stage vs control, and lower in L2/3 neurons at intermediate/high stages."
  - "AAV-mediated Kcnip4 overexpression reduces neuronal hyperactivity in vitro (lower Ca2+ transient frequency), even under Aβ1–42 oligomer exposure."
  - "AAV Kcnip4 overexpression in AppSAA mice reduces activity-dependent markers c-Fos and Arc in transduced (GFP+) neurons and reduces IBA1 (microgliosis), without altering amyloid burden or GFAP."
  - "hdWGCNA identifies candidate resilience modules (BA17: M2, M3; BA9: M2, M3, M4) with KCNIP4 among hub genes, enriched for trans-synaptic signaling, calcium homeostasis, and neuronal excitability."
  - "Three molecular L4 IT subtypes (Ex5, Ex6, Ex7) exist across neocortex; Ex5 is BA17-enriched (34.42% of excitatory cells in the BA17 reference vs 0.33% in SEA-AD DLPFC)."
abstract: "Selective neuronal vulnerability is a hallmark of Alzheimer's disease (AD), yet the molecular basis of resilience remains poorly understood. Using single-nucleus and spatial transcriptomics to compare neocortical regions affected early (prefrontal cortex, precuneus) or late (primary visual cortex) in AD, we identified a resilient excitatory population in layer 4 of the primary visual cortex expressing RORB, CUX2, and EYA4. Layer 4 neurons in association neocortex shared molecular signatures of resilience. Early-stage resilient neurons upregulated genes associated with synapse maintenance, synaptic plasticity, calcium homeostasis, and neuroprotection (GRIN2A, RORA, NRXN1, NLGN1, NCAM2, FGF14, NRG3, NEGR1, CSMD1). We identified KCNIP4, which encodes a voltage-gated potassium channel-interacting protein, as a key resilience factor consistently upregulated during early stages of AD pathology. AAV-mediated overexpression of Kcnip4 in male AppSAA mice reduced the expression of activity-dependent genes Arc and c-Fos, suggesting compensatory mechanisms against neuronal hyperexcitability. Our dataset provides a resource for investigating mechanisms underlying resilience to neurodegeneration."
---

# Molecular signatures of resilience to Alzheimer's disease in neocortical layer 4 neurons

## Overview

This study leverages the stereotyped spatiotemporal progression of Alzheimer's disease (AD) — from association cortices to primary cortices — to identify neurons and genes associated with *resilience* rather than vulnerability. The authors profiled 655,407 nuclei (424,528 after QC; 362,224 neuronal) by single-nucleus RNA-seq (snRNA-seq) from three neocortical regions (prefrontal BA9, precuneus BA7, primary visual BA17) across 46 donors spanning Braak stages 0–VI, and complemented this with single-cell spatial transcriptomics (10x Genomics Xenium; 765,992 cells across 16 sections) and Visium. They defined 18 excitatory (Ex1–Ex18) and 19 inhibitory (In1–In19) clusters, and identified a resilient L4 intratelencephalic (IT) excitatory subtype, **Ex5** (RORB/CUX2/EYA4/LAMA3), enriched in BA17, whose relative proportion *increases* with pathology. Integrated differential gene expression (linear mixed model + bootstrap + pseudobulk DESeq2 + hdWGCNA) yielded high-confidence resilience-associated genes centered on synaptic function, calcium homeostasis, and excitability regulation. As proof of principle, **KCNIP4** (a Kv4-channel-interacting, EF-hand calcium-binding protein) was validated: it is upregulated in resilient Ex5 neurons early in disease, and AAV-mediated Kcnip4 overexpression reduced neuronal hyperactivity in vitro and reduced activity-dependent markers c-Fos/Arc in a humanized AppSAA AD mouse model, supporting a neuroprotective role against hyperexcitability.

This is primarily a computational + wet-lab neuroscience resource paper. Its concrete artifacts (a full computational workflow of Jupyter notebooks, an R hdWGCNA script, CellProfiler segmentation pipelines, and pretrained cell-type-prediction models) are released on GitHub and archived on Zenodo; datasets are on GEO, CELLxGENE, and Zenodo.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 10 falsifiable claims (C01–C10) |
| [concepts.md](logic/concepts.md) | 12 technical concepts (Ex5, KCNIP4, resilience, hdWGCNA module, scCODA, …) |
| [experiments.md](logic/experiments.md) | 10 declarative verification plans (E01–E10) |
| [related_work.md](logic/related_work.md) | Typed dependency graph + full 91-reference footprint + datasets/software |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, region comparison, and analytical strategy |
| [solution/methods_pipeline.md](logic/solution/methods_pipeline.md) | snRNA-seq / spatial / DGE / hdWGCNA / functional-assay pipeline |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, limitations, confounders |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Software versions, data sources, cohort, hardware/reagents | all |
| [execution/alignment_qc_preprocessing.py](src/execution/alignment_qc_preprocessing.py) | kb-python alignment, QC, integration, clustering | C01, C02, C10 |
| [execution/scanvi_excitatory_celltype_prediction.py](src/execution/scanvi_excitatory_celltype_prediction.py) | scANVI cross-dataset label prediction | C10 |
| [execution/deg_lmm_bootstrap_pseudobulk.py](src/execution/deg_lmm_bootstrap_pseudobulk.py) | High-confidence DGE (MAST/lme4, bootstrap, pyDESeq2) | C03, C04, C05 |
| [execution/cellcounts_stats_sccoda.py](src/execution/cellcounts_stats_sccoda.py) | scCODA + GLMM compositional analysis | C01, C02 |
| [execution/hdwgcna_network.r](src/execution/hdwgcna_network.r) | hdWGCNA co-expression networks per subtype | C09 |
| [execution/stereoscope_visium_spatial.py](src/execution/stereoscope_visium_spatial.py) | Stereoscope Visium deconvolution | C02 |
| [execution/xenium_segmentation_analysis.py](src/execution/xenium_segmentation_analysis.py) | Xenium segmentation + subtype annotation | C01, C10 |
| [execution/pretrained_model.py](src/execution/pretrained_model.py) | Loading/applying pretrained cell-type models | C10 |
| [configs/analysis.md](src/configs/analysis.md) | Key parameters/thresholds across the pipeline | C01–C10 |
| [artifacts.md](src/artifacts.md) | CellProfiler pipelines, pretrained models, AAV vectors | C06, C07, C08 |

### Data Layer (`/data`)
| File | Description |
|------|-------------|
| [dataset.md](data/dataset.md) | Cohort, tissue, ethics/IRB, deposited datasets, accessions |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 20-node research DAG |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 8 main figures (0 numbered tables in main text) |
| figures/figure1.md … figure8.md | One markdown + one PNG screenshot per main figure |
