# Artifacts

The concrete deliverables of this work are **two wet-lab immunoassays** and their reagent/calibrator
specifications — not software. No code, binaries, or public datasets were released. The raw
measurement data are released as a Source Data file (see `src/environment.md` → Data sources).

## C231D181 immunoassay (p-tau181&231)
- **File(s) in repo**: none (physical assay; specification in Methods and Figure 5a)
- **Nature**: Simoa® sandwich immunoassay (wet-lab method), 2-step protocol
- **What it does / contains**: Measures tau doubly phosphorylated at T181 & T231 in CSF and plasma.
  Capture = bead-conjugated anti-p-tau231 (ADx253, ADx NeuroSciences); detector = biotinylated
  anti-p-tau181 (AT270; 90007, Fujirebio); SBG-labelled. Calibrator = custom synthetic peptide
  `IPAKTPPAPKT(PO₃H₂)PSSGEPPK-REPKKVAVVRT(PO₃H₂)PPKSPSSAK` (Anaspec). 8-point curve, 1:2 dilutions,
  80→1.25 pg/mL; LLOQ 1.25 / ULOQ 80 pg/mL.
- **How to use / run**: On a Quanterix HD-X analyzer; 4-fold sample dilution in N4PE CSF Sample
  Diluent; 4PL curve fit with 1/y weighting. Full protocol in `logic/solution/method.md`; parameter
  values in `src/configs/assay_parameters.md`.
- **Claims supported**: C01, C02, C04, C06

## C231D217 immunoassay (p-tau217&231)
- **File(s) in repo**: none (physical assay; specification in Methods and Figure 5b)
- **Nature**: Simoa® sandwich immunoassay (wet-lab method), 3-step protocol
- **What it does / contains**: Measures tau doubly phosphorylated at T217 & T231 in CSF and plasma.
  Capture = bead-conjugated anti-p-tau231 (ADx253); detector = biotinylated anti-p-tau217 antibody
  fragment (confidential, Quanterix); SBG-labelled. Calibrator = custom synthetic peptide
  `SRSRTPSLPT(PO₃H₂)PPTREPKKVAVVRT(PO₃H₂)PPKSPSSAK` (Anaspec). 8-point curve, 1:3 dilutions,
  40→0.05 pg/mL; LLOQ 0.05 / ULOQ 40 pg/mL.
- **How to use / run**: On a Quanterix HD-X analyzer; 4-fold sample dilution in N4PE CSF Sample
  Diluent; 4PL curve fit with 1/y² weighting. Full protocol in `logic/solution/method.md`; parameter
  values in `src/configs/assay_parameters.md`.
- **Claims supported**: C01, C02, C03, C05, C06, C08

## Source Data / Supplementary Information
- **File(s) in repo**: Nature Communications article MOESM files for `s41467-024-54878-8`
- **Nature**: Dataset (raw assay measurements) + Supplementary Tables 1–17 + Supplementary Figs 1–2
- **What it does / contains**: Underlying data for all main and supplementary figures/tables.
- **How to use / run**: Downloadable from the article's Supplementary Information (open access).
- **Claims supported**: all (C01–C08)
