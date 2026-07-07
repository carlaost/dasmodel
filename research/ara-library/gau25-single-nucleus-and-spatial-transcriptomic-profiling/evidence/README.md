# Evidence Index

Source: Gaur, Bryois, Calini et al. (2025), "Single-nucleus and spatial transcriptomic profiling of
human temporal cortex and white matter reveals key associations with AD pathology." *Nature
Communications* 16:10395, doi:10.1038/s41467-025-65350-6. Grounding: full-text (Open Access, CC
BY-NC-ND 4.0), 17-page PDF as provided in `research/data/lib/gau25-single-nucleus-and-spatial-transcriptomic-profiling/paper.pdf`.

## Tables

**None.** A systematic sweep of the full-text PDF (main body, pages 1-17) for the string "Table"
(case-insensitive) found **zero** occurrences of a numbered `Table N` anywhere in the paper — all
structured data in this paper is presented as figures (Fig. 1-5, plus Supplementary Figs. 1-9, not
included in the provided PDF), not tables. This was confirmed programmatically via PyMuPDF text
search across all 17 pages.

## Figures (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Figure 1 | [figures/figure1.md](figures/figure1.md) | Experimental scheme (BioRender diagram) + UMAP/dot-plot molecular map of 430,271 TC nuclei, 8 major cell types, exact per-subcluster nucleus counts | O3, C01, C02, C09 (subcluster identity/sizing) | `figures/figure1.png` |
| Figure 2 | [figures/figure2.md](figures/figure2.md) | ANCOM-BC trait association (beta-value dot plots + box plots) for neuronal/glial subclusters in GM/WM across Braak stage, plus sex-association panel | C01, C02, C03 | `figures/figure2.png` |
| Figure 3 | [figures/figure3.md](figures/figure3.md) | Pseudobulk differential expression: DEG counts per cell type/contrast (exact), largest-fold-change heatmap, LOEUF constraint (exact p-values), pathway enrichment, gene-level box plots (exact adjusted p-values) | C05, C06, C07, C08 | `figures/figure3.png` |
| Figure 4 | [figures/figure4.md](figures/figure4.md) | Spatial plaque/tangle tissue maps (7 + 6 donor sections) and CARTANA marker-gene Braak-stage validation box plots (exact p-values quoted in caption) | O9, C09 | `figures/figure4.png` |
| Figure 5 | [figures/figure5.md](figures/figure5.md) | Distance-from-plaque and distance-from-tangle heatmaps (exact Delta log-expression values, GM only) | C12, C13 | `figures/figure5.png` |

## Accounted-for omissions

- **No numbered tables exist in this paper** (verified above) — all quantitative summaries are
  reported inline in Results-section prose (transcribed with exact values and page-pinned sources in
  `logic/claims.md`) or in figures.
- **Supplementary Figures 1-9** (referenced extensively in-text, e.g. Supplementary Fig. 1a-d, 2a-h,
  3a-j, 4a-b, 5a-e, 6a, 7a-d, 8, 9) are **not included in the provided `paper.pdf`** (a main-text-only
  journal PDF) and are therefore not filed here. Every claim in `logic/claims.md` whose primary
  supporting evidence is a Supplementary Figure states this explicitly in its **Evidence basis**
  field (e.g. C04, C10, C11, C13, C14) rather than silently citing an unavailable object.
  Corresponding narrative statements from the main text (which do carry exact reported statistics,
  e.g. the 29-gene/31-gene nominal-enrichment counts in C10, the 0.124/0.119/0.121 dip-statistic
  values in C13) are grounded directly to Results/Discussion text instead.
- **Supplementary Data files 1-24** (referenced throughout, e.g. Supplementary Data 1-24) are
  external data tables not included in the provided PDF and are not filed here.
- A **Source Data file** (referenced in every main-figure caption, "Source data are provided as a
  Source Data file") is a separate Nature Communications supplementary deliverable, not included in
  the provided `paper.pdf`.

## Screenshot rendering notes

- All screenshots were rendered directly from `paper.pdf` using PyMuPDF (`fitz`), as full journal
  pages (each figure occupies essentially its full printed page, including the printed caption on
  the following or same page as applicable) — sufficient resolution (1654x2197 px) to read every
  panel label, axis, and printed numeric value at full zoom.
- Figure captions are reproduced verbatim (with special characters normalized, e.g. "β" is unaffected
  but hyphenation/ligature artifacts from PDF text extraction — e.g. "Delta" for "Δ", "beta" for
  "β" in prose where the raw extraction produced non-ASCII glyphs — are spelled out) in each
  `evidence/figures/figureN.md` file's **Caption** field.

## Self-consistency notes

- Figure 3 panel a's printed per-cell-type DEG counts sum to 1229 (Braak 5-6 main effect) and 643
  (Braak5-6 x Temporal-Cortex interaction) — both within 1 gene of the paper's stated totals of 1230
  and 644 (`logic/claims.md` C05, C06), attributable to one unlabeled small bar in each sub-panel too
  small to print a number. See `evidence/figures/figure3.md` Trend summary for the full arithmetic.
