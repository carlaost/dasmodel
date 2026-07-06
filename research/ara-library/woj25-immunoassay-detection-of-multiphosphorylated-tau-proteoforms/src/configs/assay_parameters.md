# Assay Parameters

Concrete parameter values for the two Simoa assays. Values are transcribed from Methods
§"Assay development and biomarker measurement" and §"Technical validation" (Results). Raw
per-replicate data live in Supplementary Tables 2–14 (Source Data / MOESM — not provided as
separate files here).

## Bead & detector concentrations

### Capture beads (both assays)
- **Value**: antibody-bound bead concentration 7.2 × 10⁶/mL (647 nm, dye-encoded); helper beads
  12.8 × 10⁶/mL (488 nm)
- **Rationale**: Not specified in paper
- **Sensitivity**: Not specified in paper
- **Source**: Methods §Assay development

### SBG enzyme concentration (both assays)
- **Value**: 150 pM
- **Rationale**: Not specified in paper
- **Source**: Methods §Assay development

### Detector antibody concentration (both assays)
- **Value**: 1 µg/mL
- **Source**: Methods §Assay development

### Sample dilution (both assays)
- **Value**: 4-fold in N4PE CSF Sample Diluent (default for CSF and plasma)
- **Source**: Methods §Assay development

### RGP incubation (both assays)
- **Value**: 35 °C, 30 min, 800 rpm; RGP volume 50 µl
- **Source**: Methods §Assay development

## C231D181 (p-tau181&231) assay

### Protocol
- **Value**: 2-step protocol
- **Source**: Methods §Assay development; Figure 5 caption

### Standard curve
- **Value**: 8-point curve, peptide standard dilutions 1:2, range 80 pg/mL → 1.25 pg/mL + blank
- **Source**: §Technical validation (Supplementary Table 2)

### LLOQ / ULOQ
- **Value**: LLOQ = 1.25 pg/mL; ULOQ = 80 pg/mL
- **Source**: §Technical validation (Supplementary Table 3)

### Precision (CV%)
- **Value**: intra-assay 10%; inter-assay 3%
- **Source**: §Technical validation (Supplementary Tables 4, 5)

### Dilution linearity (CV%)
- **Value**: instrument 1 = 11%; instrument 2 = 6% (dilutions tested: 1×, 2×, 4×, 8×, 16×, 32×)
- **Source**: §Technical validation (Supplementary Table 6)

### Spike-recovery
- **Value**: 69% (low spike); 87% (high spike)
- **Source**: §Technical validation (Supplementary Table 7)

### Specificity control
- **Value**: a run with a mix of single-site phosphorylated peptides produced a blank-level signal
  (double phosphorylation required to form immunocomplex and produce signal)
- **Source**: §Technical validation (Supplementary Table 8)

### Curve-fit weighting
- **Value**: 4-parameter logistic (4PL) with 1/y weighting
- **Source**: Methods §Assay development

## C231D217 (p-tau217&231) assay

### Protocol
- **Value**: 3-step protocol
- **Source**: Methods §Assay development; Figure 5 caption

### Standard curve
- **Value**: 8-point curve, peptide standard dilutions 1:3, range 40 pg/mL → 0.05 pg/mL + blank
- **Source**: §Technical validation (Supplementary Table 9)

### LLOQ / ULOQ
- **Value**: LLOQ = 0.05 pg/mL; ULOQ = 40 pg/mL
- **Source**: §Technical validation (Supplementary Table 10)

### Precision (CV%)
- **Value**: inter-assay 7%; intra-assay 4%
- **Source**: §Technical validation (Supplementary Tables 11, 12)

### Dilution linearity (CV%)
- **Value**: instrument 1 = 2%; instrument 2 = 3% (dilutions tested: 2×, 4×, 8×, 16×, 32×)
- **Source**: §Technical validation (Supplementary Table 13)

### Spike-recovery
- **Value**: 72% (low spike); 84% (high spike)
- **Source**: §Technical validation (Supplementary Table 14)

### Curve-fit weighting
- **Value**: 4-parameter logistic (4PL) with 1/y² weighting
- **Source**: Methods §Assay development
