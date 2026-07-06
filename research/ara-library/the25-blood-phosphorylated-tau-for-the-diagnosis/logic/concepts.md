# Concepts

> Grounding: abstract-only. Definitions reflect the standard meaning of terms as used in the abstract; where the paper's own precise usage would require the full text, that is noted.

## Plasma phosphorylated tau (p-tau)
- **Notation**: p-tau (site-specific variants: p-tau181, p-tau205, p-tau212, p-tau217, p-tau231)
- **Definition**: Tau protein phosphorylated at specific residues, measured in blood plasma as a biomarker of Alzheimer's disease pathology. The number denotes the phosphorylated amino-acid position.
- **Boundary conditions**: Measured in plasma (blood), distinct from cerebrospinal fluid (CSF) p-tau. This review evaluates its use to identify biologically defined AD.
- **Related concepts**: Biologically defined Alzheimer's disease, Biological reference standard, Diagnostic odds ratio.

## p-tau217
- **Notation**: p-tau217
- **Definition**: Plasma tau phosphorylated at threonine 217; identified in this meta-analysis as the highest-performing individual p-tau assay for biologically defined AD.
- **Boundary conditions**: Performance figures (C01) are pooled across heterogeneous primary studies and reference standards.
- **Related concepts**: Plasma p-tau, AUROC, Diagnostic odds ratio.

## Biologically defined Alzheimer's disease
- **Notation**: —
- **Definition**: Alzheimer's disease defined by the presence of AD pathology as established by a biological reference standard (amyloid-PET, tau-PET, CSF biomarkers, or neuropathology), rather than by clinical syndrome alone.
- **Boundary conditions**: The target condition of the diagnostic-accuracy analysis; the specific case definitions per reference standard require the full text (Not available from provided input).
- **Related concepts**: Biological reference standard, Amyloid-PET, Tau-PET.

## Biological reference standard
- **Notation**: —
- **Definition**: The gold-standard test used to confirm the presence/absence of AD pathology against which the index blood biomarker is compared; here amyloid-PET, tau-PET, CSF, and neuropathological standards.
- **Boundary conditions**: Studies lacking an appropriate biological reference standard were excluded.
- **Related concepts**: Amyloid-PET, Tau-PET, Biologically defined Alzheimer's disease.

## Bivariate random-effects meta-analysis
- **Notation**: —
- **Definition**: A meta-analytic model that jointly pools paired sensitivity and specificity across studies while accounting for their correlation and between-study heterogeneity via random effects; used here to derive pooled sensitivity, specificity, DOR, and AUROC.
- **Boundary conditions**: Requires paired 2×2 diagnostic-accuracy data from each included study.
- **Related concepts**: Sensitivity/specificity, Diagnostic odds ratio, AUROC.

## AUROC (area under the ROC curve)
- **Notation**: AUROC
- **Definition**: Area under the receiver operating characteristic curve; a threshold-independent summary of discriminative accuracy ranging 0.5 (chance) to 1.0 (perfect). Reported as a percentage in this study.
- **Boundary conditions**: Summary AUROC from the bivariate model, not a single-study estimate.
- **Related concepts**: Bivariate random-effects meta-analysis, Diagnostic odds ratio.

## Diagnostic odds ratio (DOR)
- **Notation**: DOR
- **Definition**: The ratio of the odds of a positive test result in diseased versus non-diseased individuals; a single global measure of test discrimination where higher values indicate better performance.
- **Boundary conditions**: Sensitive to threshold and prevalence assumptions embedded in the source studies.
- **Related concepts**: Sensitivity/specificity, AUROC.

## QUADAS-2
- **Notation**: QUADAS-2
- **Definition**: Quality Assessment of Diagnostic Accuracy Studies, version 2 — a standardised tool for assessing risk of bias and applicability in diagnostic-accuracy studies across patient-selection, index-test, reference-standard, and flow-and-timing domains.
- **Boundary conditions**: Used to rate the 113 included studies; ~90% were high risk of bias for threshold derivation (C06).
- **Related concepts**: Risk of bias, GRADE, PRISMA-DTA.

## GRADE
- **Notation**: GRADE
- **Definition**: Grading of Recommendations, Assessment, Development and Evaluations — a system for rating the certainty (quality) of a body of evidence, here reported as "low" or "moderate" certainty per assay.
- **Boundary conditions**: Applied to pooled diagnostic-accuracy outcomes.
- **Related concepts**: QUADAS-2, Bivariate random-effects meta-analysis.
