---
title: "Response of spatially defined microglia states with distinct chromatin accessibility in a mouse model of Alzheimer's disease"
authors: ["Alberto Ardura-Fabregat", "Lance Fredrick Pahutan Bosch", "Emile Wogram", "Omar Mossad", "Roman Sankowski", "Philipp Aktories", "Lina Kieger", "James Cook", "Dilara Hasavci", "Hatice Ulupinar", "Daniel Brock", "Fang Wang", "Nicola Iovino", "Samuel Wald", "Sebastian Preissl", "Bahtiyar Yilmaz", "Daniel Schnepf", "Andrew J. Macpherson", "Thomas Blank", "Katrin Kierdorf", "Marco Prinz"]
year: 2025
venue: "Nature Neuroscience (Volume 28, August 2025, 1688–1703)"
doi: "10.1038/s41593-025-02006-0"
ara_version: "1.0"
grounding: full-text
domain: "Neuroimmunology / microglia biology / Alzheimer's disease (preclinical mouse model)"
keywords: ["microglia", "plaque-associated microglia", "PAM", "non-PAM", "5xFAD", "amyloid-beta", "Confetti fate mapping", "clonal expansion", "chromatin accessibility (ATAC-seq)", "scRNA-seq", "CSF1R", "Csf1", "IL-34", "disease-associated microglia (DAM)"]
claims_summary:
  - "In 5xFAD+ mice, cortical microglia partition into two spatially defined states — plaque-associated microglia (PAM, within 30 µm of / contacting amyloid) and non-plaque-associated microglia (non-PAM) — with PAM numbers expanded while non-PAM numbers resemble controls."
  - "PAM clonally expand at plaque sites (non-random by Monte Carlo simulation); clone size correlates with adjacent plaque volume up to ~1,000 µm3."
  - "CD11c specifically marks PAM and Tmem119 preferentially marks non-PAM, enabling marker-based discrimination."
  - "Fate mapping (Tmem119CreERT2) shows non-PAM give rise to adjacent same-colored PAM clones, which grow between 2 and 8 weeks after labeling."
  - "Peripheral LPS increases and antibiotic (ABX) microbiota depletion slightly reduces PAM clonal expansion at early disease stage; effects are absent at late stage (age/stage dependence)."
  - "Only non-PAM (not PAM) show transcriptional plasticity to LPS/ABX at early stage, with treatment-specific scRNA-seq clusters appearing only in non-PAM."
  - "Chromatin accessibility separates PAM from non-PAM; non-PAM resemble homeostatic 5xFAD- microglia. PAM vs non-PAM: 5,661 DARs (4,360 more accessible/PAM-up, 1,301 less/PAM-down)."
  - "Csf1r shows higher transcript level and more open chromatin in non-PAM than PAM, nominating CSF1R as a non-PAM-directed target."
  - "Peripheral Csf1 (but not IL-34) reduces PAM clonal expansion and overall microglial number, increases PAM phagocytic (CD68+) compartment, and lowers soluble and insoluble Aβ40/Aβ42."
  - "Csf1 treatment reduces inflammatory gene programs and raises oxidative-phosphorylation/autophagy programs in PAM (and non-PAM) without changing their core homeostatic/activation signatures — generating amyloid-competent PAM."
abstract: "Microglial spatial heterogeneity remains a crucial yet not fully answered question in the context of potential cell-directed therapies for Alzheimer's disease (AD). There is an unclear understanding of the dynamics of distinct microglia states adjacent to or far from amyloid-beta (Aβ) plaques and their contributions to neurodegenerative diseases. Here we combine multicolor fluorescence cell fate mapping, single-cell transcriptional analysis, epigenetic profiling, immunohistochemistry and computational modeling to comprehensively characterize the relation of plaque-associated microglia (PAM) and non-plaque-associated microglia (non-PAM) in a mouse model of AD. We show that non-PAM are a distinct and highly dynamic microglial state, transitioning to PAM after Aβ plaque deposition in female mice. Non-PAM modulate the cell population expansion in response to amyloid deposition and rapidly respond to environmental cues. Indeed, Csf1 signaling modulates non-PAM-to-PAM transition during disease progression. Our data suggest that microglia states and their dynamics between each other can have distinct contributions to disease, and they may be targeted for the treatment of AD."
---

# Response of spatially defined microglia states with distinct chromatin accessibility in a mouse model of Alzheimer's disease

## Overview

Using the 5xFAD amyloid mouse model, the authors dissect microglia into two spatially defined
states — plaque-associated microglia (PAM), whose processes contact Methoxy-X04+ amyloid and whose
cell bodies lie within a 30-µm radius of a plaque, and non-plaque-associated microglia (non-PAM),
ramified cells distant from amyloid. Combining multicolor Confetti fate mapping with Monte Carlo
clonality testing, Voronoi-grid spatial analysis, single-cell RNA-seq, ATAC-seq chromatin
profiling, immunohistochemistry, ELISA/western blot and peripheral pharmacology, they show that
individual non-PAM are the dynamic source of clonally expanding PAM and are the transcriptionally
plastic, environmentally responsive compartment. Non-PAM retain a homeostatic, more accessible
Csf1r locus, and peripheral Csf1 (but not IL-34) engages CSF1R to restrict PAM clonal expansion,
boost PAM phagocytosis and reduce amyloid burden — nominating the non-PAM→PAM transition as a
therapeutic window in early amyloid pathology. Study is exclusively in **female** mice.

This ARA is a **full-text** compilation (PDF: 30 pp incl. Methods, Extended Data and Reporting
Summary). All numerical values are transcribed exactly from the source; figures were read visually.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight → assumptions |
| [claims.md](logic/claims.md) | 13 falsifiable claims (C01–C13) |
| [concepts.md](logic/concepts.md) | 12 key technical terms defined |
| [experiments.md](logic/experiments.md) | 11 verification/analysis plans (E01–E11) |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's citation footprint |
| [solution/constraints.md](logic/solution/constraints.md) | Assumptions, boundary conditions, limitations |
| [solution/study_design.md](logic/solution/study_design.md) | Mouse models, treatment paradigms, experimental logic |
| [solution/computational_methods.md](logic/solution/computational_methods.md) | Monte Carlo clonality test, Voronoi gridding, scRNA-seq & ATAC-seq pipelines |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [environment.md](src/environment.md) | Software/hardware, data sources (GEO), tool versions, protocols | all |
| [configs/analysis_parameters.md](src/configs/analysis_parameters.md) | scRNA-seq (Seurat) and ATAC-seq analysis parameters | C07–C09, C13 |
| [artifacts.md](src/artifacts.md) | GEO datasets, brain-immunity.de portal, KNIME/iRoCS image-analysis pipeline, Monte Carlo script | C01–C13 |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | Research DAG reconstructing the paper's trajectory |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 12 filed figures (Fig 1–7 + Extended Data Fig 1–5) |

No numbered main-text Tables exist in the source; embedded tabular panels (Fig 5d motif table,
Extended Data Fig 4b TSS scores) are transcribed inside their parent figure files. See
`evidence/README.md` for the full ledger and accounting of Supplementary Table 1.
