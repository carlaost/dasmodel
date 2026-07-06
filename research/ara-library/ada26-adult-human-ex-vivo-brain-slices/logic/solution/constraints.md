# Constraints, Assumptions & Limitations

> Grounding: abstract-only + verified analysis repository. Constraints stated by the paper's running
> text (explicit limitations sections) are **Not available from provided input (no full text)**;
> those below are grounded in the abstract, the sample table, and the released code, plus honest
> methodological caveats implied by the design.

## Boundary conditions
- **Tissue source**: Adult human brain from **neurosurgical resections** (tumor-adjacent) — not
  healthy donor brain. Sample cohort (Supplementary Table 1) is 9 donors with brain tumors
  (glioma, metastatic carcinoma/brain metastasis, meningioma).
- **Modality split**: 8 donors bulk RNA-seq, 4 donors snuc-RNA-seq (small n, especially for the
  cell-type-resolved TNFα arm).
- **Perturbation panel**: Findings on stimulus specificity are bounded to the five tested arms
  (Control, BLM, H₂O₂, LPS, TNFα).
- **Culture window**: Preservation asserted "over weeks"; exact viable/valid duration Not available
  from provided input.

## Assumptions
- A1: Tumor-adjacent resection tissue reflects glial biology generalizable beyond the tumor
  microenvironment — a caveat given all donors had CNS tumors.
- A2: Ex-vivo culture does not itself induce the transcriptional states attributed to stressors
  (control arm is intended to guard against this).
- A3: Cell-type annotations from canonical markers correctly partition mature identities in cultured
  tissue.
- A4: TNFα signatures validated in postmortem/external datasets are transferable and not
  slice-artifactual (the validation arm exists to support this).

## Known limitations
- **No peer review**: bioRxiv v1 preprint (2026-01-12), not peer reviewed.
- **Full text unavailable to compiler**: quantitative results, exact protocols, statistics, figure
  values, and the complete limitations/discussion are Not available from provided input (bioRxiv PDF
  and JATS behind Cloudflare; Unpaywall does not index the 10.64898 prefix). This ARA therefore
  cannot report effect sizes, sample-level statistics, or the paper's own stated caveats.
- **Data availability**: No public sequencing-data accession (GEO/SRA/EGA/ArrayExpress) was located
  (Europe PMC PPR1228173 `hasData=N`; empty GEO search); likely embargoed for this v1 preprint.
  Independent reanalysis of raw data is therefore not currently possible from public repositories.
- **Small donor n** limits statistical power, especially for the snRNA-seq TNFα comparisons.
- **Tumor-patient cohort**: all tissue is peritumoral; healthy-brain generalization is an open
  question the abstract does not resolve in the available text.
- **Released code is plotting/analysis-only**: the two R scripts regenerate manuscript figures and
  contain hard-coded paths/placeholders (e.g. `f_tnf <- "..."`); the upstream alignment/QC/DE-model
  and WGCNA-construction steps are not fully contained in the repo (only the plotting layer + inputs
  such as `LDA_treatments.csv`, `WGCNA_program_trait_correlations.csv`).
