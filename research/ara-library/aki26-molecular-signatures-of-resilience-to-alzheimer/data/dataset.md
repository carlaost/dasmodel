# Dataset

## Provenance
Postmortem human neocortical brain tissue + AppSAA/WT mouse tissue. Human tissue from Stanford
(Pathology & ADRC), UCLA (Pathology & Easton Center), and the NIH Neurobiobank (Sepulveda
repository; Mt. Sinai Brain Bank).

## Human cohort
- **Donors**: 46 total; region participation 42 BA9, 15 BA7, 24 BA17.
- **Regions**: prefrontal cortex (BA9), precuneus (BA7), primary visual cortex (BA17).
- **Staging**: Braak 0–VI; ABC score (NIA-AA); CERAD neuritic plaque density.
- **Pathology groups (overall)**: low 18 (6F/12M), intermediate 10 (7F/3M), high 18 (12F/6M).
  - Region-specific counts used in composition models (Fig. 4 caption): BA9 low 17 / int 10 / high 15; BA17 low 7 / int 5 / high 12.
- **Mean age** (low/int/high): 70.5±9.2 / 81.9±13.6 / 82.4±10.4 y.
- **RIN**: 5.8±0.7 / 6.2±0.7 / 6.2±0.7. **PMI (h)**: 15.6±8.2 / 12.8±8.2 / 13.8±9.7.
- **APOE**: genotyped (Genewiz/Azenta); modeled as covariate.
- **Exclusions**: large-vessel infarction, hemorrhage, neoplasm, CNS infection, hypoxic-ischemic injury.

## Modalities and scale
| Modality | Samples/sections | Cells/nuclei |
|----------|------------------|--------------|
| snRNA-seq | 243 samples (184 Drop-seq, 59 10x; 37 batches) | 655,407 profiled → **424,528** after QC (362,224 neuronal: 282,930 Ex, 79,294 In; 62,304 non-neuronal) |
| snRNA-seq per region (post-QC) | — | BA9 288,030; BA7 72,088; BA17 64,410 |
| snRNA-seq per disease group | — | Low 136,344; Int 125,814; High 162,370 |
| Non-neuronal | — | astrocytes 14,691; microglia 5,071; OPCs 5,770; oligodendrocytes 36,589; vascular 183 |
| Xenium spatial | 16 (8 BA9, 8 BA17; 4 AD + 4 control) | **765,992** after QC |
| Visium spatial | 16 sections (controls + AD) | 1383-gene panel; median 221 genes / 392 UMI per spot |

## Clusters
18 excitatory (Ex1–Ex18) + 19 inhibitory (In1–In19) neuronal subtypes; 4 astrocyte, 4 microglia, 2 oligodendrocyte states. Full cluster labels in Fig. 1f,g and evidence/figures/figure1.md.

## Mouse tissue
- AppSAA (JAX #034711) and WT C57BL/6J (#000664); male; 12 months for in vivo AAV; P0 pups for primary cortical neurons.

## Deposited datasets / access
| Dataset | Identifier | Repository | Access |
|---------|-----------|------------|--------|
| Raw snRNA-seq + metadata + processed matrices | GSE263468 | NCBI GEO | open |
| Reused samples (8/243) | GSE129308, GSE181715 | NCBI GEO | open |
| Interactive snRNA-seq | collection 0d35c0fd-ef0b-4b70-bce6-645a4660e5fa | CZI CELLxGENE | open |
| Xenium spatial | 10.5281/zenodo.16703438 | Zenodo | open |
| Code + pretrained models | 10.5281/zenodo.18113528 | Zenodo / GitHub | open (CC-BY-4.0) |
| Source data | provided with paper | Nature Communications | open |

## Preprocessing / QC summary
See `logic/solution/methods_pipeline.md` §3 and `src/configs/pipeline_parameters.md`. Alignment
GRCh38/Ensembl 105 (kb-python), unspliced counts; empty-droplet (DropletUtils, FDR<0.05),
gene-count (≥300) and mito (<5%) filters, DoubletFinder, Harmony integration over assay+region.
