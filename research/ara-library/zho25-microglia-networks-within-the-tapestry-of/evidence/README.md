# Evidence Ledger

This paper contains **3 numbered figures** and **0 numbered tables**. All figures are filed below,
each with a markdown transcription/description and a saved PNG screenshot. No table objects exist
in the source (verified by full-text sweep — the string "Table" does not appear as a numbered
object anywhere in the main text or appendix; this is a narrative review with no data tables).

## Figures

| Object | Type | Pages | File |
|---|---|---|---|
| Figure 1 | diagram | p.3 | [figures/figure1.md](figures/figure1.md) / [figures/figure1.png](figures/figure1.png) |
| Figure 2 | mixed (qualitative micrographs + diagrammatic grid overlays) | p.4-5 | [figures/figure2.md](figures/figure2.md) / [figures/figure2.png](figures/figure2.png) |
| Figure 3 | diagram | p.6 | [figures/figure3.md](figures/figure3.md) / [figures/figure3.png](figures/figure3.png) |

## Tables

None. The paper is a 14-page narrative review with no numbered data tables; all quantitative
findings are reported in prose (with exact numbers grounded per-claim in `logic/claims.md`) rather
than in tabular form.

## Extraction method notes

- All three figures were rendered from `paper.pdf` at 250 DPI using PyMuPDF (`fitz`), cropped to the
  figure panel region (excluding running header/footer), and read visually panel-by-panel.
- Figure 1 and Figure 3 are pure diagrams (schematic illustrations of molecular encoding/decoding
  schemes and cell-cell communication networks, respectively) — no data table is fabricated from
  either; both are captured as structured visual descriptions.
- Figure 2 is a mixed figure: panel A is a real fluorescence micrograph (qualitative sample) with
  overlaid cell-type/gene labels, and panels B-E are the same micrograph with diagrammatic grid
  overlays representing each seq-ST platform's native spot size (quantitative labels: 50 μm, 10 μm,
  2 μm, 220 nm — these are platform specification values printed directly on the figure, not
  digitized estimates).
- No figure required digitization of unlabeled plot axes; all numeric values appearing in the
  figures (scale bars, spot sizes) are printed directly on the image and are transcribed exactly as
  shown (`extraction_method: exact_from_labels` for those values; `visual_description` for the
  diagrammatic/schematic content).
