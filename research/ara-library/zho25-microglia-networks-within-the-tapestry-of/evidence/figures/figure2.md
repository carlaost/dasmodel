# Figure 2: Resolution of representative img-ST and seq-ST technologies

- **Source**: Figure 2, page 4 of 14 (panels), legend on page 5 of 14
- **Caption**: "Fig. 2 Resolution of representative img-ST and seq-ST technologies. A. Example
  image of unpublished img-ST MERFISH (~ 120 genes panel) data in human AD brain at single molecule
  level with anti-Aß (4G8) antibody staining and spatial mapping of neuronal and non-neuronal cells
  in the right panel. B-D. Grids mapped onto the image in (A) represent the resolution provided by
  Visium, Slide-seq, and Visium HD platforms, with the right panels indicating cells and molecules
  from single-molecule imaging in (A). E. Grid size of 0.5 μm on the left panel, and single box
  region in the right panel representing the 220 nm resolution of Stereo-seq spot size"
- **Screenshot**: figure2.png
- **Figure type**: mixed (panel A = qualitative sample / real micrograph; panels B-E = diagram —
  grid overlays on the same micrograph representing platform spot sizes)
- **Extraction method**: exact_from_labels (all resolution/scale-bar values are printed directly on
  the figure); visual_description (for image content and layout)
- **Reading confidence**: high (all panel labels, resolution values, and scale bars are clearly
  legible in the rendered image)

## Visual description (Panel A — qualitative sample)
- **Components**: A real fluorescence micrograph of human AD brain tissue, single-molecule MERFISH
  data with anti-Aβ (4G8) antibody staining (red channel, labeled "Plaque" with a dashed pink
  circle outline) plus four gene-color-coded channels: AQP4 (green, labeled "Astro"), CSF1R
  (yellow, labeled "Microglia"), FLT1 (purple), and NRGN (blue, labeled "ExN" = excitatory neurons).
  Colored arrows point to representative astrocyte, microglia, and excitatory-neuron signal within
  the field. A 20 μm scale bar is shown. A separate right-hand panel shows a cortical-layer
  schematic ("Layer II" to "Layer VI") with non-neuronal cells (top, pink/green dots) and excitory
  [excitatory] neurons (bottom, orange/purple/white dots) mapped by layer depth.
- **What it conveys**: Ground-truth single-molecule-resolution spatial localization of individual
  transcripts (astrocyte, microglia, and excitatory neuron marker genes) directly around an
  amyloid plaque in human AD tissue, establishing the reference image onto which panels B-E overlay
  coarser-resolution platform grids for visual comparison.

## Visual description (Panels B-E — diagrammatic grid overlays / platform resolution comparison)
- **Panel B (Visium, ~50 μm spot size)**: A coarse 2x2-ish grid of large squares overlaid on the
  Panel-A micrograph; a zoomed inset (dashed white box) shows the fluorescence detail within one
  such spot, with a 10 μm scale bar in the inset.
- **Panel C (Slide-seq, ~10 μm spot size)**: A denser grid (~4x4 visible squares) overlaid on the
  same micrograph region; zoomed inset with a 5 μm scale bar.
- **Panel D (Visium HD, ~2 μm spot size)**: A much finer grid (~7x7+ visible squares) overlaid on
  the same region; zoomed inset with a 2 μm scale bar.
- **Panel E (Stereo-seq, ~220 nm spot size)**: An extremely fine grid (sub-micron spacing, visually
  near-continuous) overlaid on the full micrograph; zoomed inset with a 0.5 μm grid size on the
  left sub-panel and the caption stating the single-box region in the right panel represents 220 nm
  resolution.
- **What it conveys**: A direct, visual, same-tissue comparison of native spot/pixel resolution
  across four representative seq-ST platforms, spanning roughly two and a half orders of magnitude
  (50 μm down to 220 nm) on identical underlying single-molecule ground truth. This is the primary
  visual evidence underlying the resolution values cited in `logic/claims.md` C01 and
  `logic/concepts.md` (Visium, Slide-seq, Stereo-seq, Visium HD entries).

## Data table (resolution values transcribed from figure labels)
| Panel | Platform | Spot/pixel size (as printed on figure) |
|---|---|---|
| B | Visium | ~50 μm |
| C | Slide-seq | ~10 μm |
| D | Visium HD | ~2 μm |
| E | Stereo-seq | ~220 nm |

## Trend summary
Panel A anchors the comparison in real single-molecule-resolution ground truth from human AD
brain tissue around a plaque. Panels B-E show that as seq-ST platform spot size decreases (Visium
→ Slide-seq → Visium HD → Stereo-seq), the overlaid grid increasingly approaches the density of
individual detected transcripts seen in Panel A — visually demonstrating the resolution/coverage
trade-off discussed in `logic/solution/constraints.md` and grounding the platform-resolution
values in `logic/claims.md` C01.
