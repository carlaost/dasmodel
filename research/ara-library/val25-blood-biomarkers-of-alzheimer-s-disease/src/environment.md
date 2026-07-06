# Environment

This is an original epidemiological cohort study, not a software/model-training project. `src/` therefore holds only the analytical environment and data/code availability facts stated in the paper; no runnable code was provided as input (only `paper.pdf` was supplied to this compilation), so no code stub is fabricated (compiler Rule 14).

## Software
- **Language/runtime**: R version 4.3.1 (The R Foundation for Statistical Computing) — p.7, Methods, Statistical analysis: "Statistical analyses were conducted using R version 4.3.1 (The R Foundation for Statistical Computing)." [input]
- **Key package**: `msm` — multi-state models for panel data (Jackson, ref. 56) — p.7: "To ﬁt multistate models we used the msm56 package." [input]

## Laboratory / assay platform
- **Instrument**: Quanterix Simoa (Single molecule array) platform, Affinity Proteomics Stockholm Unit, SciLifeLab.
- **Kits**: Simoa Neuro 3-plex A Kit (Aβ40, Aβ42, t-tau); Simoa pTau-181 Advantage V2 Kit; Simoa ALZpath p-Tau-217 Advantage PLUS Kit; Simoa Neuro 2-plex B Kit (NfL, GFAP) — p.6, Methods.
- **Curve-fitting**: Quanterix SR-X software, 4-parameter logistic (4PL) fit, from AEB (average enzyme per bead) values.

## Data availability
- SNAC-K data are sensitive/restricted; de-identified raw and analyzed data can be requested by qualified researchers via https://www.snac-k.se/, subject to review and a signed data-sharing agreement — p.7: "SNAC-K data are sensitive data; thus, they cannot be shared publicly, but raw and analyzed de-identiﬁed data can be requested by qualiﬁed researchers at https://www.snac-k.se/." [input]
- "Source data are provided with this paper" per the paper's Data availability statement (source-data file not included in the compiled input) — p.7. [input]

## Code availability
- The paper states: "Analysis codes for this study are available at https://github.com/ARCbiostat/biomdemstages/tree/main." (p.7, Code availability) [input]
- **This ARA does not fetch or transcribe that repository.** The compiled input for this artifact was the paper PDF only; per the compiler's input-fidelity rule, external resources not actually provided are not captured as if verified, and no code stub is fabricated from the method prose. The repository URL is recorded here as a pointer only, for a future compilation pass that is explicitly given the repository as input.

## Hardware / compute
- Not specified in paper (a standard statistical-analysis workflow; no GPU/HPC or specialized compute infrastructure is described).
