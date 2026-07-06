# Concepts

## Multiphosphorylated tau proteoform
- **Notation**: p-tau_i&j (e.g., p-tau181&231)
- **Definition**: A single tau protein molecule carrying phosphorylation simultaneously at two (or more) distinct residues. Distinct from a population in which some molecules are phosphorylated at site i and others at site j; multiphosphorylation requires co-occurrence on the same molecule.
- **Boundary conditions**: In this work restricted to two-site combinations T181&T231 and T217&T231, detected in CSF and plasma.
- **Related concepts**: p-tau181&231, p-tau217&231, sandwich immunoassay, tau PTM.

## p-tau181&231
- **Notation**: p-tau181&231
- **Definition**: Tau phosphorylated concurrently at threonine 181 and threonine 231; measured by the C231D181 assay (capture p-tau231, detect p-tau181).
- **Boundary conditions**: Diagnostic in CSF; non-diagnostic in plasma (does not separate AD groups from NDC).
- **Related concepts**: C231D181 assay, multiphosphorylated tau proteoform, matrix-specific protein processing.

## p-tau217&231
- **Notation**: p-tau217&231
- **Definition**: Tau phosphorylated concurrently at threonine 217 and threonine 231; measured by the C231D217 assay (capture p-tau231, detect p-tau217).
- **Boundary conditions**: Diagnostic in both CSF and plasma; highest fold change and highest nominal plasma AUC.
- **Related concepts**: C231D217 assay, multiphosphorylated tau proteoform.

## Simoa sandwich immunoassay
- **Notation**: —
- **Definition**: Single-molecule array (Simoa®) bead-based sandwich immunoassay: an analyte is captured by an antibody on paramagnetic dye-encoded beads, bound by a biotinylated detector antibody, labelled with streptavidin-β-galactosidase (SBG) enzyme, and resuspended in RGP (β-D-galactopyranoside substrate) to generate a fluorescent signal read on an HD-X instrument. Ultrasensitive (subfemtomolar).
- **Boundary conditions**: Requires both capture and detector epitopes to be present on the analyte for signal.
- **Related concepts**: AEB, SBG, RGP, C231D181 assay, C231D217 assay.

## C231D181 assay
- **Notation**: C231D181
- **Definition**: Simoa assay measuring p-tau181&231. Capture antibody = anti-p-tau231 (ADx253) on beads; detector = biotinylated anti-p-tau181 (AT270). Uses a 2-step protocol.
- **Boundary conditions**: LLOQ 1.25 pg/mL, ULOQ 80 pg/mL; 8-point standard curve (1:2 dilutions).
- **Related concepts**: p-tau181&231, Simoa sandwich immunoassay.

## C231D217 assay
- **Notation**: C231D217
- **Definition**: Simoa assay measuring p-tau217&231. Capture antibody = anti-p-tau231 (ADx253) on beads; detector = biotinylated anti-p-tau217 antibody fragment (confidential, Quanterix). Uses a 3-step protocol.
- **Boundary conditions**: LLOQ 0.05 pg/mL, ULOQ 40 pg/mL; 8-point standard curve (1:3 dilutions).
- **Related concepts**: p-tau217&231, Simoa sandwich immunoassay.

## AD continuum (A/T/N framework)
- **Notation**: A+/T+; A−/T−/N−
- **Definition**: Classification of patients by core CSF AD biomarkers per the NIA-AA research framework: A (amyloid, Aβ42/Aβ40), T (tau phosphorylation, p-tau181), N (neurodegeneration, t-tau). AD continuum patients are defined by an A+/T+ CSF profile; stages: pre-AD (preclinical), MCI-AD, AD-dem. NDC are A−/T−/N−.
- **Boundary conditions**: Cut-offs used: Aβ42/Aβ40 = 0.072 (95% CI 0.07–0.074); p-tau181 = 50 (95% CI 46.2–52.3); t-tau = 393 (95% CI 359–396).
- **Related concepts**: pre-AD, MCI-AD, AD-dem, NDC.

## Standardized effect size (Cohen's d)
- **Notation**: d
- **Definition**: Standardized difference in mean marker concentration between two groups. Interpreted as: large d > 0.8, medium d > 0.5, small d > 0.2, negligible < 0.2 (computed with the effsize R package).
- **Boundary conditions**: Used here for AD group vs NDC comparisons in Figures 2 and 4.
- **Related concepts**: median concentration fold change.

## Median concentration fold change
- **Notation**: —
- **Definition**: Ratio of the median marker concentration in an AD continuum group (pre-AD, MCI-AD, or AD-dem) to the median in the control (NDC) group.
- **Boundary conditions**: Reported per marker/matrix/stage (Supplementary Table 17).
- **Related concepts**: standardized effect size.

## AEB (Average Enzyme per Bead)
- **Notation**: AEB
- **Definition**: The raw Simoa signal unit — average number of enzyme labels per bead — from which analyte concentration is extrapolated via the standard curve (in-house Quanterix software).
- **Boundary conditions**: For clinical samples, raw AEB was assigned calibrator-based concentrations post hoc from the averaged technical-validation standard curve.
- **Related concepts**: Simoa sandwich immunoassay, dilution linearity.

## Matrix-specific protein processing
- **Notation**: —
- **Definition**: The hypothesis that tau is fragmented/truncated and processed differently in CSF versus plasma (e.g., differential loss of peptides spanning residues 221–226), so a given proteoform's epitope survival and diagnostic value differ by matrix.
- **Boundary conditions**: Invoked to explain the CSF-diagnostic / plasma-non-diagnostic split of p-tau181&231; interpretive, not directly measured.
- **Related concepts**: p-tau181&231, tau truncation.

## Dilution linearity & spike-recovery
- **Notation**: —
- **Definition**: Analytical-validation assessments — dilution linearity checks that measured concentration scales proportionally across serial sample dilutions (CV of the recovery across dilutions); spike-recovery checks the fraction of a known spiked analyte recovered by the assay (low-spike and high-spike).
- **Boundary conditions**: Assessed on two independent HD-X instruments; part of intermediate precision / repeatability validation.
- **Related concepts**: LLOQ, ULOQ, Simoa sandwich immunoassay.
