# Figure 1: Hybridization and de-coding scheme of img-ST

- **Source**: Figure 1, page 3 of 14
- **Caption**: "Fig. 1 Hybridization and de-coding scheme of img-ST. (A) The encoding probes binding
  to target mRNA, signal detection, and decoding method for MERFISH with hemming distance 4
  barcoding system. (B) The encoding probes bind to target mRNA, signal detection, and decoding
  method for seq-FISH with combinations of different fluorophores of readout probes. (C) The
  Padlock encoding probes bind to target mRNA, RCP, and signal detection with 2 to 6 nucleotides per
  cycle"
- **Screenshot**: figure1.png
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high (all panel text, labels, and barcode/color-coding schemes are clearly
  legible in the rendered image)

## Visual description (Panel A — MERFISH)
- **Components**: A schematic mRNA molecule bound to the tissue substrate ("mRNA" bar) is targeted
  by an encoding-probe complex terminating in an orange "readout" circle. To the right, an
  "Adaptors" box shows a single gray adaptor bar, and a "Readouts" box shows three colored circular
  readout probes (orange, red, purple) on gray stalks. A "Hybridization Round" table lists rounds
  1-4, "...", 19, 20 as columns and Gene 1 / Gene 2 / Gene 3 / ... / Gene n as rows, with each
  cell containing a binary value (0 or 1) rendered in a colored box (purple/gray/green/orange
  depending on value and round).
- **Connections**: The mRNA-bound encoding probe connects through adaptors to combinatorial readout
  probes; each gene's identity is encoded as a binary vector across ~20 hybridization rounds (a
  barcode), read out combinatorially.
- **Annotations**: "MERFISH" label; round numbers 1, 2, 3, 4, ..., 19, 20 as column headers; Gene
  1/2/3/n as row labels.
- **What it conveys**: The combinatorial binary-barcoding encoding/decoding logic underlying
  MERFISH, in which a minimum Hamming distance of 4 between per-gene barcodes provides
  error-robust decoding across multiple hybridization rounds (described in `logic/concepts.md`
  under "MERFISH"). This is the mechanistic basis for the "over 2000 mRNA species" and "2,000-6,000
  RNA species" multiplexing capacities cited in `logic/claims.md` C01.

## Visual description (Panel B — seqFISH)
- **Components**: An mRNA-bound probe complex with four labeled arms (I, II, III, IV) terminating
  in a blue circular readout probe. A "Readouts" box shows five colored readout circles (blue,
  orange, green, purple, yellow) on gray stalks. A "Barcoding Round 1" table lists positions I-IV as
  columns and Gene 1/2/3/.../20 as rows, with each cell filled by one of the five readout colors.
- **Connections**: Each gene is assigned a unique ordered combination of fluorophore colors across
  the four positions (I-IV) within a single barcoding round, and this is repeated across multiple
  rounds — generating a combinatorial "pseudocolor" readout.
- **Annotations**: "seq-FISH" label; position labels I/II/III/IV; "Readout Hyb" row-group labels 1,
  2, 3, ..., 20.
- **What it conveys**: The combinatorial-fluorophore encoding logic underlying seqFISH, distinct
  from MERFISH's binary-hybridization-round barcoding — both achieve multiplexing beyond
  traditional FISH's spectral-overlap limit, as described in `logic/concepts.md` under "seqFISH."

## Visual description (Panel C — Padlock/ISS)
- **Components**: An mRNA-bound padlock probe forms a circularized structure ("RCPs" = rolling
  circle products) shown as a spiral of orange/black beads. A "Bridge" box shows a single orange
  bar; a "Readouts" box shows two pairs of colored circles (purple/orange and green/red) on gray
  stalks. A "Cycle Readouts" table lists cycles 1-6 as columns and Gene 1/2/3/n as rows, with each
  cell containing a single DNA base letter (A/C/G/T) in a colored box.
- **Connections**: The padlock probe hybridizes to the target mRNA-derived cDNA, circularizes, and
  undergoes rolling-circle amplification to form a localized rolony; sequencing-by-ligation across
  6 cycles reads out a base-letter barcode (2 nucleotides per cycle position pair) that identifies
  the gene.
- **Annotations**: "Padlock" label; "RCPs" label; cycle numbers 1-6; Gene 1/2/3/n row labels.
- **What it conveys**: The padlock-probe/rolling-circle-amplification/sequencing-by-ligation logic
  underlying in situ sequencing (ISS) methods such as STARmap and Xenium, as described in
  `logic/concepts.md` under "In situ sequencing (ISS) / padlock probes."

## Trend summary
All three panels are pure schematic diagrams illustrating three distinct encoding/decoding
strategies used by img-ST platforms (binary hybridization-round barcoding for MERFISH,
combinatorial-fluorophore barcoding for seqFISH, and base-letter sequencing-by-ligation for
padlock-probe ISS). No quantitative data table is fabricated from this figure; it is foundational
technology-explainer context for `logic/claims.md` C01 and `logic/concepts.md`.
