# Study Design — Adult Human Organotypic Slice Platform

> Grounding: abstract-only + verified analysis repository. The design below is reconstructed from
> the abstract, the repo README, and the two released R analysis scripts. Wet-lab protocol details
> (slice preparation, medium, TNFα dose/timing, culture duration) are **Not available from provided
> input (no full text)**.

## Overall design

The work is a **platform-establishment + application** study with two coupled arms:

1. **Platform characterization** — show that adult human organotypic slices from neurosurgical
   resections retain mature multicellular identity/architecture in culture (snRNA-seq cell-type
   annotation across 8 cell types).
2. **Perturbation + crosstalk dissection** — apply defined stressors, define stimulus-specific
   programs (bulk RNA-seq + WGCNA), resolve the cell-type-specific TNFα response (snRNA-seq DE),
   validate externally, and infer coordinated glial crosstalk (MultiNicheNet), then confirm in
   postmortem human brain.

## Inputs / samples

- Adult human brain tissue from neurosurgical resections (tumor-adjacent). Supplementary Table 1
  lists 9 donors (ages 22–69; both sexes; frontal/temporal/parietal areas; tumor types glioma,
  metastatic carcinoma/brain metastasis, meningioma), of which 8 contributed bulk RNA-seq and 4
  contributed snuc-RNA-seq (see `data/dataset.md` and `evidence/tables/supp_table1_samples.md`).

## Perturbation panel (bulk arm)

Five conditions analysed together (`bulk_treatments_plots.R`): **Control, BLM (bleomycin), H₂O₂,
LPS, TNFα**. Analyses:
- **LDA** on treatment labels (Panel A) — treatment separability.
- **WGCNA** program–trait correlation heatmap over Prog.1–Prog.5 × 5 treatments with significance
  stars (Panel B); thresholds `*** <0.001`, `** <0.01`, `* <0.05`.
- **Pathway dotplot** (Panel C) — curated enriched pathways per program (e.g. Prog.1: apoptosis /
  p53 / NF-κB / cytokine signaling; Prog.3: response to LPS / TNF signaling / chemotaxis; Prog.4:
  interferon signaling; per the `selected_pathways` list in the script).

## Cell-type-resolved arm (snRNA-seq)

`sNucRNAseq_plots.R` defines the design:
- **Cell-type annotation** via `Molecular_markers` for 8 cell types: Astrocytes, Endothelial,
  Ex.neurons, In.neurons, Microglia, Oligos, OPCs, Perivascular_cells (Figure 1: UMAP, marker
  dotplot, cell-type proportions).
- **TNFα vs Control** contrast (Figure 2): treatment UMAP, NFKB1 density, shared TNF-response gene
  heatmap (`gene_list`: NAMPT, SOD2, WTAP, IRAK1, NFKB1, PARP14, TNFAIP2, TNIP1), per-glial-type
  volcano plots (microglia, astrocytes, OPCs; sig at adj-p < 0.05, |log2FC| vs 0.2), and per-type
  pathway barplots.

## Validation arm

Slice-derived TNFα signatures tested against external datasets (README): mouse microglia, human
iPSC-derived astrocytes, COVID-19 postmortem human brain, and large AD snRNA-seq cohorts; abstract
highlights validation in **postmortem human brains**.

## Communication arm

**MultiNicheNet** comparison of TNFα-treated vs control slices prioritizes ligand–receptor
interactions (Supplementary Table 5, "TNF signaling analysis"), interpreted as the pro-/anti-
inflammatory loops among microglia, astrocytes, and OPCs.

## Readout logic

Platform validity (C01) → stimulus-specific programs (C02/C05) → cell-type TNFα response (C03) →
external validation (C04) → prioritized crosstalk edges (C06) → biological interpretation as
coordinated multicellular loops (C03).
