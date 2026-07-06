# Figure 5: Design of the immunoassays

- **Source**: Figure 5, Methods §Assay development and biomarker measurement
- **Caption**: "Design of the immunoassays. a C231D181, b C231D217 assay. T181: tau phosphorylation at threonine 181, T231: tau phosphorylation at threonine 231, T217 tau phosphorylation at threonine 217, SBG: streptavidin β-galactosidase, RGP: β-D-galactopyranoside. 2-step protocol workflow (C231D181 assay): 1) Sample incubation with a mixture of bead-conjugated capture antibody and biotinylated detector antibody, 2) Incubation with SBG; 3-step protocol workflow (C231D217 assay): 1) Sample incubation with bead-conjugated capture antibody, 2) Incubation with biotinylated detector antibody, 3) Incubation with SBG. Subsequently, immunocomplexes are resuspended in RGP (SBG substrate), resulting in generation of the fluorescent signal."
- **Screenshot**: figure5.png
- **Figure type**: diagram (schematic of the sandwich-assay geometry)
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description

### Panel a — C231D181 (detect tau phosphorylated at T181 & T231)
- **Components**:
  - Bead-conjugated **p-tau231 capture antibody** (blue bead with radiating antibody arms).
  - Central analyte: **multiphosphorylated tau** shown as a linear chain with two phospho-marks —
    **T231** (blue) near one end and **T181** (pink) further along.
  - **Biotinylated p-tau181 detector antibody** (magenta "Y"), carrying **SBG enzyme** which acts on
    the **RGP substrate** to emit a fluorescent signal (star).
- **Connections**: capture bead (binds T231) + tau (T181 & T231) + detector (binds T181) →
  sandwich immunocomplex → SBG + RGP → fluorescent signal. Two "+" symbols denote the assembly of
  the three components.
- **Annotations**: T181 colored pink, T231 colored blue; color coding matches assay name components.
- **What it conveys**: signal requires the same tau molecule to carry BOTH T181 and T231
  phosphorylation, because capture and detector each recognize a different phospho-site.

### Panel b — C231D217 (detect tau phosphorylated at T217 & T231)
- **Components**: identical layout, but the detector is the **biotinylated p-tau217 detector
  antibody** (green "Y"), and the analyte's second phospho-mark is **T217** (green) rather than T181.
  Capture antibody is again bead-conjugated **p-tau231**.
- **Connections**: capture (T231) + tau (T217 & T231) + detector (T217) → immunocomplex → SBG + RGP
  → fluorescent signal.
- **Annotations**: T217 colored green, T231 colored blue.
- **What it conveys**: same dual-site sandwich principle, measuring the p-tau217&231 proteoform.

The diagram's structure (capture-site ≠ detector-site → double-phosphorylation-dependent signal)
is the backbone of the method captured in `logic/solution/method.md` and supports C01.
