# Environment

This is an experimental clinical-neurochemistry (immunoassay development + biomarker) study. There
is **no computational code repository** associated with the paper (verified: no Code availability
section; no GitHub/GitLab/Zenodo/OSF repo found). Reproducibility rests on wet-lab instruments,
reagents, and statistical software.

- **Language/runtime**: Statistical analysis — R 4.2.2 (R Core Team 2019) and GraphPad Prism 9.5.0
  (USA). No released code.
- **Framework / R packages**: `pROC` (ROC AUC comparison, DeLong test); `effsize` (Cohen's d).
  In-house Quanterix Corp. software for Simoa standard-curve fitting and concentration extrapolation
  from raw AEB signal.
- **Instruments (hardware)**: Quanterix Simoa **HD-X** analyzers (Quanterix Corp., Billerica, MA,
  USA), at the Quanterix Assay Development laboratory (two independent HD-X instruments used for
  dilution-linearity assessment). Core CSF biomarkers on **Lumipulse G600II** (Fujirebio, Japan).
- **Key reagents / kits**:
  - Capture bead antibody: anti-p-tau231 (ADx253, ADx NeuroSciences, Belgium).
  - Detector C231D181: biotinylated anti-p-tau181 (AT270; 90007, Fujirebio, Japan).
  - Detector C231D217: biotinylated anti-p-tau217 antibody fragment (confidential, Quanterix).
  - Commercial reference: p-tau181 Advantage V2 Kit (item 103714), p-tau231 Advantage Kit (item
    102292), prototype non-commercialized p-tau217 assay (all Quanterix).
  - Calibrators: custom synthetic doubly phosphorylated peptides (Anaspec, USA) — sequences in
    `logic/solution/method.md`.
  - Diluent: N4PE CSF Sample Diluent (Quanterix); SBG enzyme; RGP (β-D-galactopyranoside) substrate.
  - Storage tubes: 0.5 mL tubes 72.730.007 (Sarstedt, Germany).

## Data sources

| Source | Content | Access | Verified |
|--------|---------|--------|----------|
| Source Data file / Supplementary Information (MOESM files), Nature Communications article `s41467-024-54878-8` | Raw assay measurements underlying all figures and tables; Supplementary Tables 1–17, Supplementary Figs 1–2 | **Open** (released with the paper; sources.yaml) | Yes (sources.yaml, verified) |
| Discovery + validation patient cohorts (matched CSF & plasma; AD continuum + FTD; discovery n=55, validation n=118) | Patient-level biomarker + clinical data | **On request** from corresponding authors (University of Perugia / Amsterdam UMC); subject to EU data-protection review | Yes (sources.yaml, verified) |

- No external dataset accessions (no GEO/SRA/PRIDE/ProteomeXchange/EGA/Dryad/figshare/Zenodo).
  Cohorts are in-house, not public (not ADNI/BioFINDER).
- Article identifiers: DOI 10.1038/s41467-024-54878-8; PMID 39747866; PMC11696609. Gold OA,
  CC BY-NC-ND 4.0.

## Protocols
- Assay protocols (2-step C231D181, 3-step C231D217): `logic/solution/method.md`.
- Sample collection/handling SOP and statistical analysis plan: `logic/solution/study_design.md`.
- Analytical validation (precision, dilution linearity, LLOQ/ULOQ, spike-recovery): experiment E01;
  parameter values in `src/configs/assay_parameters.md`.

## Random seeds
- Not applicable (no stochastic computation / model training). Not specified in paper.

## Ethics / consent
- Declaration of Helsinki + ICH GCP; informed written consent; Ethics Committee approval Comitato
  Etico Aziende Sanitarie Regione Umbria 19369/AV and 20942/21/OV.

## Funding
- Parkinson's Foundation (PF-PRF-934916); EU Horizon 2020 Framework Programme grant 860197
  (MIRIADE consortium).
