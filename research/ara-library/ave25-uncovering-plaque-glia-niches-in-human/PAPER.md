---
title: "Uncovering plaque-glia niches in human Alzheimer's disease brains using spatial transcriptomics"
authors: ["Denis R. Avey", "Bernard Ng", "Ricardo A. Vialle", "Nicola A. Kearns", "Katia de Paiva Lopes", "Artemis Iatrou", "Sashini De Tissera", "Himanshu Vyas", "Devin M. Saunders", "Daniel J. Flood", "Jishu Xu", "Shinya Tasaki", "Chris Gaiteri", "David A. Bennett", "Yanling Wang"]
year: 2025
venue: "Molecular Neurodegeneration Advances"
doi: "10.1186/s44477-025-00002-z"
ara_version: "1.0"
domain: "Alzheimer's disease neuropathology / spatial transcriptomics / neuroimmunology"
keywords: ["spatial transcriptomics", "amyloid-beta", "glia", "microglia", "astrocytes", "Alzheimer's disease", "plaque-glia niche", "disease-associated microglia", "iPSC", "ligand-receptor signaling"]
claims_summary:
  - "Aβ-load-stratified pseudobulk expression yields distinct, largely non-overlapping DEG sets depending on glial context (C01)"
  - "Low-Aβ (diffuse-plaque-enriched) spots show a more neurotoxic transcriptomic and histological profile than high-Aβ spots (C02)"
  - "Glia-high plaque niches show elevated inflammatory/apoptotic signaling and reduced neuronal/synaptic markers relative to glia-low niches (C03)"
  - "Spatial glial responses converge on established mouse/human glial-activation gene modules, with the human MG3 (DAM-like) state most consistently enriched (C04)"
  - "Aβ-intensity spot stratification tracks classical plaque maturity and replicates across two independent tissue cohorts (C05)"
  - "Aβ load reshapes inferred intercellular ligand-receptor signaling, with the largest, most synapse/neuron-relevant changes in low-Aβ spots (C06)"
  - "Glial abundance reshapes inferred ligand-receptor signaling toward reduced synaptic and (in high-Aβ) increased immune/TREM2 signaling (C07)"
  - "Aβ-oligomer-treated iPSC-derived microglia (iMGL), but not astrocytes or neurons, recapitulate the spatial glia-high-vs-glia-low transcriptomic response (C08)"
  - "Aβ-treated iMGL subclusters differentially resemble specific human AD microglial states, with iMGL1 most closely resembling MG3 (C09)"
abstract: "Background Amyloid-beta (Aβ) plaques and their associated glial responses are hallmark features of Alzheimer's disease (AD), yet their interactions within the human brain remain poorly defined. Methods We applied spatial transcriptomics (ST) and immunohistochemistry (IHC) to 78 postmortem brain sections from 21 individuals in the Religious Orders Study and Memory and Aging Project (ROSMAP). We paired ST with histological data and stratified spots into major categories of plaque-glia niches based on Aβ, GFAP, and IBA1 intensity. Leveraging published ROSMAP single-nucleus RNA-seq data, we examined differences in gene expression, cellular composition, and intercellular communication across these niches. Neuronal and glial changes were validated by IHC and quantitative analyses. We further characterized glial responses using gene set enrichment analysis (GSEA) with known mouse glial signatures and human AD-associated microglial states. Finally, we used iPSC-derived multicellular cultures and single-cell RNA sequencing (scRNA-seq) to identify cell types that, upon short-term Aβ exposure, recapitulate the glial responses observed in the human spatial data. Results Low-Aβ regions, enriched for diffuse plaques, exhibited transcriptomic profiles consistent with greater neuronal loss than high-Aβ regions. High-glia regions showed increased expression of inflammatory and neurodegenerative pathways. Spatial glial responses aligned with established gene modules, including plaque-induced genes (PIGs), oligodendrocyte (OLIG) responses, disease-associated microglia (DAM), disease-associated astrocytes (DAA), and human AD-associated microglial states, indicating that diverse glial phenotypes emerge around plaques and shape the local immune environment. IHC confirmed elevated neuronal apoptosis near low-Aβ plaques and greater CD68 abundance and synaptic loss near glia-high plaques. In vitro, iPSC-derived microglia—but not astrocytes—exposed to Aβ displayed transcriptomic changes that closely mirrored the glial states identified in our ST dataset. Conclusions Our study provides a comprehensive spatial transcriptomic dataset from human AD brain tissue and bridges spatial gene expression with traditional neuropathology. By integrating ST, snRNA-seq, and human multicellular models, we map cellular states and molecular events within plaque-glia niches. This work offers a spatially resolved framework for dissecting plaque-glia interactions and reveals new insights into the cellular and molecular heterogeneity underlying neurodegenerative pathology."
---

# Uncovering plaque-glia niches in human Alzheimer's disease brains using spatial transcriptomics

## Overview

This paper applies paired spatial transcriptomics (10x Visium) and immunohistochemistry (Aβ,
GFAP, IBA1) to 78 postmortem DLPFC sections from 21 ROSMAP donors (13 AD, 8 no-cognitive-impairment
controls), stratifying the resulting 258,987 ST spots into "plaque-glia niches" by local Aβ
intensity (no/low/high) and glial abundance (glia-high/glia-low). Pseudobulk linear-mixed-model
contrasts, gene set enrichment analysis (against mouse DAM/DAA/PIG/OLIG modules and 12 human
AD-brain microglial states), cell-type deconvolution (cell2location), and ligand-receptor spatial
signaling inference (NICHES) reveal that low-Aβ (diffuse-plaque) niches and glia-high niches are
each independently associated with more neurotoxic transcriptomic and histological signatures than
high-Aβ or glia-low niches respectively, and that a DAM-like human microglial state (MG3) is the
most consistently enriched glial program across contrasts. An iPSC-derived multicellular
co-culture (microglia + astrocyte + neuron) exposed to Aβ oligomers shows that only the
microglia-like cells (iMGL), not astrocytes or neurons, recapitulate this in vivo glial
transcriptional signature, with one iMGL subcluster (iMGL1) specifically resembling the MG3 state.
The work contributes a large, publicly deposited (Synapse syn53141470) human paired ST-IHC dataset
and a spatially resolved framework linking classical AD neuropathology to plaque-proximal
transcriptomics.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | 8 observations, 4 gaps, key insight (adjacent-section IHC pairing enabling powered niche contrasts), 5 assumptions |
| [claims.md](logic/claims.md) | 9 falsifiable claims (C01-C09) covering Aβ-load DEGs, glia-abundance DEGs, gene-module/MG-state convergence, plaque-type validation, LR signaling, and iPSC cross-validation |
| [concepts.md](logic/concepts.md) | 14 genuine technical terms/methods (plaque-glia niche, ST, IHC-ST alignment, stratification schemes, pseudobulk LMM, GSEA + gene modules, cell2location, NICHES, iMGL co-culture, integration benchmarking) |
| [experiments.md](logic/experiments.md) | 10 declarative verification/analysis plans (E01-E10), directional only |
| [related_work.md](logic/related_work.md) | 18 full RW blocks (typed: imports/baseline/bounds) plus a briefer catalog of ~40 additional background/infrastructure citations |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions, assumptions, and the paper's own stated limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Cohort, tissue, validation-cohort, and statistical-framework design |
| [solution/method.md](logic/solution/method.md) | 10-stage computational analysis pipeline (ST QC through iPSC scRNA-seq cross-validation) |

### Physical Layer (`/src`, `/data`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Software/hardware/data-source/protocol inventory; no code repository released (prose-only method — no fabricated code stub, per Rule 14) | all |
| [configs/parameters.md](src/configs/parameters.md) | 16 explicitly stated quantitative pipeline parameters (QC thresholds, clustering resolution, stratification cutoffs, significance thresholds, sequencing depth targets) | C01-C09 |
| [data/dataset.md](data/dataset.md) | Primary ST-IHC cohort + 2 independent IHC validation cohorts + iPSC scRNA-seq dataset + external reference datasets; notes on unincluded supplementary files | C01-C09 |
| [data/preprocessing.md](data/preprocessing.md) | ST/IHC/scRNA-seq QC and normalization steps, and pseudobulk construction procedure | C01-C09 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG: 1 question, 1 pivot (same-section→adjacent-section IHC), 3 decisions (integration method, clustering method, glia-threshold stringency), 2 dead ends (threshold stringency, underpowered 6-way stratification), 7 experiments |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 7 figures (no numbered main-text tables in this paper); notes on unincluded supplementary tables/figures |
| figures/figure1.md + .png | ST workflow, spot clustering/layer annotation, cell2location cell-type enrichment |
| figures/figure2.md + .png | Plaque-glia niche IHC stratification and plaque-type validation |
| figures/figure3.md + .png | Aβ-load DEG/GSEA analysis + IHC apoptosis validation |
| figures/figure4.md + .png | NICHES ligand-receptor analysis of Aβ-load contrasts |
| figures/figure5.md + .png | Glia-abundance DEG/GSEA analysis + IHC synaptic/neuronal-loss validation |
| figures/figure6.md + .png | NICHES ligand-receptor analysis of glia-abundance contrasts |
| figures/figure7.md + .png | iPSC co-culture Aβ-oligomer treatment, scRNA-seq, cross-GSEA validation |
