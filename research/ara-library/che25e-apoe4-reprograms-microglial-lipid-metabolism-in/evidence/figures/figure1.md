# Figure 1: APOE4-mediated dysregulation and neurological implications

- **Source**: Figure 1, p.2, Chen et al. (2025), *BioScience Trends*, Advance Publication, doi:10.5582/bst.2025.01148, §2.1-§2.2
- **Caption**: "Figure 1. APOE4-mediated dysregulation and neurological implications. (A). Chromosomal
  location of the APOE gene and differences in different protein isoforms, the percentage of
  APOEε4 gene carriers, and the association of APOE4 with multiple diseases. (B). In AD, APOE4
  promotes Aβ deposition and impairs Aβ clearance through receptor competition and BBB disruption.
  APOE4 drives astrocytes and microglia toward a pro-inflammatory phenotype and induces
  mitochondrial dysfunction. Importantly, APOE4 disrupts intracellular lipid metabolism, leading to
  pathological lipid droplet accumulation and accelerated AD progression. ABCA1, ATP-binding
  cassette transporters A1; LDLR, low-density lipoprotein receptor; LRP1, LDL receptor-related
  protein 1; AS, atherosclerosis; BBB, blood-brain barrier; CVD, cardiovascular disease; TBI,
  traumatic brain injury; CAA, cerebral amyloid angiopathy."
- **Screenshot**: figure1.png
- **Figure type**: diagram (mixed — a structural/schematic diagram whose panel A carries some exact
  printed percentages, so it also functions as a small data label set)
- **Extraction method**: exact_from_labels (the three carrier percentages are printed directly on
  the diagram)
- **Reading confidence**: high

## Visual description

**Panel A** (APOE gene/isoform structure and epidemiology):
- Two chromosome-19 ideograms labeled "19" on the left.
- A linear protein-domain map: NTD (1-167, with a "receptor binding site" sub-region highlighted in
  orange, spanning approximately residues 112-158 based on the flanking tick marks 112 and 158) —
  connected by a linker — to CTD (207-299, with a "lipid binding site" sub-region highlighted in
  dark blue/purple).
- A 3-row isoform table showing amino-acid identity at positions 112 and 158: APOE2 (Cys112,
  Cys158), APOE3 (Cys112, Arg158), APOE4 (Arg112, Arg158).
- An "APOEε4 carrier" bracket listing three genotype percentages: APOEε4/ε2 = 2.3%, APOEε4/ε3 =
  20.6%, APOEε4/ε4 = 2.1%.
- Below, two schematic diagrams: (left) a lipid/lipoprotein-loading vesicle showing ABCA1
  transporting lipid onto a lipoprotein particle, which then binds LDLR or LRP1 receptors on a
  neuron/cell membrane; (center) a large "APOE4" label with triangular APOE4 icons and two outward
  arrows; (right) two disease-association schematics: a balance-scale icon showing LDL-C↑ vs
  HDL-C↓ leading to "AS↑, CVD risk↑," and a brain icon with a red lesion plus microglia/astrocyte
  icons leading to "TBI, stroke prognosis↓, CAA, AD risk↑."

**Panel B** (Aβ deposition and cell-type effects):
- A microglia cell (labeled "microglia") and an astrocyte cell (labeled "astrocyte"), separated by
  a horizontal "impaired BBB" band of endothelial-cell icons.
- APOE4 triangular icons flow from both cells toward a central "deposition" arrow pointing down to
  an amyloid-fibril aggregate icon, with "Aβ clearance↓" labeled beside a downward red arrow.
- The microglia icon contains lipid (yellow circle) and mitochondria icons and secretes
  inflammatory-cytokine (small purple dot) icons.
- The astrocyte icon contains lipid and mitochondria icons and shows "dysregulated lipid
  homeostasis" text beside it.
- A legend at the bottom-right of panel B defines icons: APOE4 (dark red triangle), inflammatory
  cytokines (purple dots), Aβ fibre (green fibril), Aβ plaque (brown aggregate), lipid (yellow
  circle), mitochondria (purple organelle), LDLR (purple receptor stem).
- **What it conveys**: Panel A grounds the review's genetic/structural premise (isoform sequence
  differences, dose-dependent carrier frequency, multisystem disease associations); Panel B
  previews the cell-type-specific (microglia + astrocyte), lipid-metabolism-centered, BBB-linked
  mechanism that the rest of the review elaborates.

## Data (exact values printed in Panel A)

| Genotype | Carrier percentage |
|---|---|
| APOEε4/ε4 | 2.1% |
| APOEε3/ε4 | 20.6% |
| APOEε2/ε4 | 2.3% |

These three values sum to the review's stated overall APOEε4 carrier rate of "approximately 23.9%"
(2.1 + 20.6 + 2.3 = 25.0% as printed in the figure; see `logic/claims.md` C12 `**Sources**` entry
for the body-text figure of 23.9% and the discrepancy note below).

## Trend summary / consistency note

Panel A's three printed percentages (2.1% + 20.6% + 2.3% = 25.0%) do not sum to exactly the body
text's "approximately 23.9%" (§2.2, ref 32) cited in `logic/claims.md` C12 and `logic/problem.md`
O2 — both are copied verbatim from their respective sources (figure label vs. body text) without
reconciliation, per the "exact numbers, no silent correction" rule. This is a minor internal
inconsistency in the source paper itself, not an ARA transcription error.
