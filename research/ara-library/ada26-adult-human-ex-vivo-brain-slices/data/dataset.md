# Datasets

> Grounding: verified repository (Supplementary Table 1 + README) and `sources.yaml`. Consent/IRB
> details and exact sequencing depths/platforms are **Not available from provided input (no full
> text)**.

## Primary data (generated in this study)

- **Content**: Bulk RNA-seq and single-nucleus RNA-seq of adult human organotypic brain slice
  cultures under a five-arm perturbation panel (Control, BLM, H₂O₂, LPS, TNFα for bulk; TNFα vs
  Control for snRNA-seq).
- **Provenance**: Living adult human brain tissue from **neurosurgical resections** (tumor-adjacent).
- **Cohort (Supplementary Table 1)**: 9 donors. Ages 22–69; sexes M and F; brain areas Frontal,
  Temporal, Parietal; tumor types Glioma, Metastatic Carcinoma / Brain Metastasis, Meningioma.
  Assay assignment: 8 donors → Bulk RNA-seq; 4 donors → snuc-RNA-seq (one donor is snuc-only). Full
  per-row transcription: `evidence/tables/supp_table1_samples.md`.
- **Accession / access**: **None located.** No GEO/SRA/EGA/ArrayExpress accession in the repo or
  Europe PMC (record PPR1228173, `hasData=N`); GEO search empty. Access type: **unknown / likely
  embargoed** for this v1 preprint. Recorded as `null` rather than fabricated (`sources.yaml`).
- **Consent/IRB/ethics**: Not available from provided input (no full text).
- **Licensing**: Preprint license `cc_no` (per metadata). Data license not stated.

## Bundled supplementary tables (open, in repo)

Supplementary Tables 1–5 (`.xlsx`) are redistributed under `data/` in the repo — see
`src/artifacts.md`. These are the openly available processed outputs (cohort, WGCNA, bulk/snRNA-seq
DE and pathways, MultiNicheNet signaling), not the raw sequencing reads.

## Precomputed analysis inputs referenced by scripts

The released R scripts consume intermediate files not all shipped in the repo: `LDA_treatments.csv`,
`WGCNA_program_trait_correlations.csv`, `WGCNA_program_trait_p_values.csv`, per-program pathway
`*.csv`, `TNF.rds` (Seurat object), and a DE-results folder. Their absence limits end-to-end
reproducibility from the repo alone.

## External validation datasets (reused public data)

Per README, slice-derived TNFα signatures were validated in: mouse microglia; human iPSC-derived
astrocytes; COVID-19 postmortem human brain; and large Alzheimer's disease snRNA-seq cohorts.
Specific accessions/citations: Not available from provided input (see `logic/related_work.md`
RW04–RW07).
