# Method — Assay Design and Wet-Lab Protocols

Source: Methods §"Assay development and biomarker measurement"; Figure 5 (assay design diagrams).

## Core design principle (Figure 5)

Each assay is a **Simoa® sandwich immunoassay** whose capture and detector antibodies target
**two different phosphorylation sites**. Signal is generated only when a single tau molecule is
phosphorylated at *both* sites simultaneously, so the readout is specific to a doubly
phosphorylated proteoform.

- **C231D181** (Figure 5a): capture = bead-conjugated **anti-p-tau231**; analyte = tau
  phosphorylated at **T181 & T231**; detector = biotinylated **anti-p-tau181**. → measures
  **p-tau181&231**.
- **C231D217** (Figure 5b): capture = bead-conjugated **anti-p-tau231**; analyte = tau
  phosphorylated at **T217 & T231**; detector = biotinylated **anti-p-tau217**. → measures
  **p-tau217&231**.

Both use SBG enzyme + RGP substrate to generate the fluorescent signal after immunocomplex
formation.

## Reagents (verbatim from Methods)

- **Beads**: paramagnetic, fluorescent dye-encoded beads (647 nm), antibody-bound bead
  concentration 7.2 × 10⁶/mL, conjugated with a mouse monoclonal antibody against human p-tau231
  (**ADx253, ADx NeuroSciences, Belgium**), mixed with unconjugated helper beads (488 nm,
  concentration 12.8 × 10⁶/mL).
- **C231D181 detector**: biotinylated mouse monoclonal antibody against human p-tau181
  (**AT270; 90007, Fujirebio, Japan**), SBG-labelled (SBG concentration 150 pM, detector
  concentration 1 µg/mL).
- **C231D217 detector**: SBG-labelled biotinylated mouse monoclonal antibody **fragment** against
  human p-tau217 (**confidential, Quanterix Corp., USA**), SBG concentration 150 pM, detector
  concentration 1 µg/mL.
- **Antibody provenance**: capture (p-tau231) antibody = the capture antibody in the p-tau231
  Advantage Kit (item 102292, Quanterix). C231D181 detector (p-tau181) = the capture antibody in the
  p-tau181 Advantage V2 Kit (item 103714, Quanterix). C231D217 detector (p-tau217) = the capture
  antibody in a prototype, non-commercialized p-tau217 assay (Quanterix).
- **Sample dilution**: 4-fold dilution in N4PE CSF Sample Diluent (Quanterix), default for CSF and
  plasma in both assays.
- **RGP**: incubated on shaker at 35 °C for 30 min (800 rpm) before each run; RGP volume 50 µl in
  both protocols.

## Calibrator peptides (custom synthetic, Anaspec, USA)

- **C231D181 calibrator** — doubly phosphorylated at T181 and T231 (N-term → C-term):
  `IPAKTPPAPKT (PO₃H₂) PSSGEPPK-REPKKVAVVRT (PO₃H₂) PPKSPSSAK`
- **C231D217 calibrator** — doubly phosphorylated at T217 and T231 (N-term → C-term):
  `SRSRTPSLPT (PO₃H₂) PPTREPKKVAVVRT (PO₃H₂) PPKSPSSAK`
- All standard dilutions prepared with N4PE CSF Sample Diluent.

## Protocol workflows (Figure 5 caption)

- **C231D181 — 2-step protocol**: (1) sample incubation with a mixture of bead-conjugated capture
  antibody + biotinylated detector antibody; (2) incubation with SBG.
- **C231D217 — 3-step protocol**: (1) sample incubation with bead-conjugated capture antibody;
  (2) incubation with biotinylated detector antibody; (3) incubation with SBG.
- After either protocol, immunocomplexes are resuspended in RGP (SBG substrate) → fluorescent
  signal. All measurements run on HD-X instruments (Quanterix Corp., Billerica, MA, USA) at the
  Quanterix Assay Development laboratory.

## Standard curves & curve fitting

- **C231D181**: 8-point standard curve, peptide standard dilutions **1:2** ranging 80 pg/mL →
  1.25 pg/mL + a blank void of peptide standard. Curve fit: 4-parameter logistic (4PL) with **1/y**
  weighting.
- **C231D217**: 8-point standard curve, peptide standard dilutions **1:3** ranging 40 pg/mL →
  0.05 pg/mL + a blank void of peptide standard. Curve fit: 4PL with **1/y²** weighting.
- Concentrations extrapolated from raw AEB (Average Enzyme per Bead) signal via in-house Quanterix
  software. For clinical samples, raw AEB values were assigned calibrator-based concentrations post
  hoc from an averaged standard curve obtained across technical-validation runs.

## Reference (single-site) assays

CSF and plasma p-tau181, p-tau231, p-tau217 were measured with in-house manufactured Simoa assays
using the same antibodies/standards/buffers as commercial Quanterix kits: p-tau181 Advantage V2 Kit
(item 103714), p-tau231 Advantage Kit (item 102292; at the time commercially launched for CSF), and
a prototype non-commercialized p-tau217 assay. These are standard-format assays employing a
phosphorylation-site-specific capture antibody (T181/T231/T217) and a detector antibody targeting
unphosphorylated tau.

## Numeric analytical-validation results

Exact validation numbers (LLOQ/ULOQ, CVs, dilution linearity, spike-recovery) are recorded in
`src/configs/assay_parameters.md` and grounded in the Technical-validation text; the raw values live
in Supplementary Tables 2–14 (not provided as separate files in the input — Source Data / MOESM).
