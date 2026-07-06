# Evidence Index

This paper's main text contains **7 numbered figures (Figure 1-7) and no numbered main-text
tables**. All quantitative "Table" references in the paper (e.g., "Supplementary Table 1" through
"Supplementary Table 12") refer to external supplementary XLSX/CSV/DOCX files that were **not
included** in the `paper.pdf` provided as input to this ARA compilation (see "Not filed" section
below) — they are not main-text tables and could not be rendered from the provided PDF. This was
verified by an exhaustive text sweep of the PDF (`grep -n "Table"` across the full extracted text)
confirming every "Table" mention is prefixed "Supplementary".

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1.md](figures/figure1.md) | Figure 1, Page 5 of 23 | (context/methods; supports C01-C09 indirectly) | ST experimental workflow; UMAP spot clustering, layer annotation, cluster-enriched genes, cell2location cell-type enrichment by cluster |
| [figures/figure2.md](figures/figure2.md) | Figure 2, Page 8 of 23 | C05 | Plaque-glia niche stratification by adjacent-section IHC intensity; plaque-type proportions by Aβ stratum; glia stratification scatterplots |
| [figures/figure3.md](figures/figure3.md) | Figure 3, Page 12 of 23 | C01, C02, C04, C06 | Aβ-load DEG/GSEA analysis; IHC caspase-3 apoptosis validation |
| [figures/figure4.md](figures/figure4.md) | Figure 4, Page 14 of 23 | C06 | NICHES ligand-receptor analysis of Aβ-load contrasts |
| [figures/figure5.md](figures/figure5.md) | Figure 5, Page 15 of 23 | C03, C04, C07 | Glia-abundance DEG/GSEA analysis; IHC synaptic/neuronal loss validation |
| [figures/figure6.md](figures/figure6.md) | Figure 6, Page 17 of 23 | C07 | NICHES ligand-receptor analysis of glia-abundance contrasts |
| [figures/figure7.md](figures/figure7.md) | Figure 7, Page 18 of 23 | C08, C09 | iPSC co-culture Aβ-oligomer treatment, scRNA-seq, cross-GSEA validation of ST glial signature |

## Tables

No numbered main-text tables exist in the source PDF (see note above).

## Not filed (accounted for, not silently omitted)

- **Supplementary Tables 1-12** (external XLSX/CSV files: donor clinicopathological data, spot
  cluster marker genes, cell2location output, co-expression module gene lists, manual plaque
  annotations, Aβ-contrast DEGs, Aβ-contrast LR DEGs, glia-contrast DEGs, 6-way stratification
  DEGs, iMGL/astrocyte/neuron Aβ DEGs, iMGL-subcluster-vs-ST-signature DEGs, iMGL-subcluster-vs-MG-state
  DEGs) — referenced throughout the Results/Methods but distributed as separate Supplementary
  Information files (Supplementary files 1-13, XLSX/CSV), not embedded in `paper.pdf`. Not
  available from the provided input; their existence and content-type are captured in
  `data/dataset.md` without fabricating their contents.
- **Supplementary Figures 1-10** (S1: ST QC metrics/elbow plots; S2: integration-method
  benchmarking; S3: BayesSpace comparison; S4: co-expression module preservation; S5: GFAP
  RNA-protein correlation, per-individual Aβ-stratum enrichment; S6: FFPE plaque-type validation
  (722 plaques); S7: glia-high/low manual cell counts; S8: additional Aβ-contrast gene boxplots; S9:
  additional glia-contrast gene boxplots, CD68 quantification; S10: scRNA-seq QC/clustering
  diagnostics) — referenced throughout but not embedded as separate renderable figures in
  `paper.pdf` (likely bundled within Supplementary file 14, a 6.62 MB DOCX, not provided as input).
  Numeric results **stated in the main text** that cite these supplementary figures (e.g., the
  OR=14.98/p=4.89e-38 FFPE replication statistic, nominally "Supplementary Fig. 6C") are still
  captured in `logic/claims.md` (C05) with the verbatim main-text quote as the source, since that
  statistic is reported directly in the body text, not only in the inaccessible supplementary
  figure itself.

## Screenshot note

Each `figureN.png` is a full-page render (200 dpi, via PyMuPDF) of the PDF page containing that
figure's panels and caption; every figure in this paper is laid out within a single PDF page
(Figures 1-7 each occupy one full page alongside their caption, with body text resuming after the
caption on the same page in most cases). No cropping of sub-panels was performed; the full
rendered page is retained as the "screenshot" to preserve original layout and any panel-adjacent
annotations.
