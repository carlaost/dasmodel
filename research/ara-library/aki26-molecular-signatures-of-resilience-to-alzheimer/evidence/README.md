# Evidence Index

**Grounding**: full-text (publisher OA PDF). Figures were read visually from rendered pages
(170 dpi, PyMuPDF); each `.png` is the rendered page region containing that figure + caption.

**Tables**: The main text contains **no numbered tables** (Table 1, Table 2, …). All quantitative
content is delivered through the 8 main figures plus Supplementary Data 1–10 and Supplementary
Figs 1–11 (supplementary files are not part of the provided main PDF and are therefore not filed
as evidence objects; they are cited in-line where relevant). Evidence-completeness for tables: N/A
(none exist in the main text).

**Numbers policy**: Where the paper prints an exact value in text/caption (e.g., log2FC 1.75,
FDR 0.008, 986 DE genes, cell percentages), it is filed as `exact_from_labels` (text-stated). The
plots themselves rarely carry per-point data labels; any value read off an axis is marked `≈`
(`digitized_estimate`). Diagrams and qualitative micrographs carry visual descriptions, not tables.

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1.md](figures/figure1.md) | Fig. 1, §Results-1 | C10, C02 | Cohort/experimental design + snRNA-seq cell-type composition, 18 Ex/19 In clusters, cosine-distance validation, glial states (mixed) |
| [figures/figure2.md](figures/figure2.md) | Fig. 2, §Results-2 | C01, C10 | Xenium spatial design + layer-specific localization of excitatory subtypes in BA9 vs BA17 (mixed: diagram + spatial maps + bar) |
| [figures/figure3.md](figures/figure3.md) | Fig. 3, §Results-3 | C10, C01 | L4 markers across regions: UMAPs, mouse conservation, Xenium spatial, EYA4/KCNH8/VGLUT2 ISH (mixed) |
| [figures/figure4.md](figures/figure4.md) | Fig. 4, §Results-4 | C01, C02 | scCODA boxplots + GLMM volcano: relative preservation/increase of Ex5 (quantitative_plot) |
| [figures/figure5.md](figures/figure5.md) | Fig. 5, §Results-5 | C03, C04 | Transcriptome signatures of AD progression: DE-gene bar plots, heatmaps, UpSet plots, pathway enrichment (mixed) |
| [figures/figure6.md](figures/figure6.md) | Fig. 6, §Results-6 | C04, C05, C09 | Resilience signatures in Ex5: DE heatmaps, biological-function network, hdWGCNA modules/hub genes (mixed) |
| [figures/figure7.md](figures/figure7.md) | Fig. 7, §Results-7 | C05, C06 | KCNIP4 upregulation: violin plots by cell type/stage + KCNIP4/EYA4/NeuN IHC quantification (mixed) |
| [figures/figure8.md](figures/figure8.md) | Fig. 8, §Results-8 | C07, C08 | AAV Kcnip4 functional validation: vector schematics, Ca2+ traces, WB, c-Fos/Arc/amyloid/GFAP/IBA1 quantification (mixed) |

All eight numbered main figures are filed (markdown + PNG). No numbered figure is omitted.
