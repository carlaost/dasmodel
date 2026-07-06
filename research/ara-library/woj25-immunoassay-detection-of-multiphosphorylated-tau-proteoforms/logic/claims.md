# Claims

## C01: Two Simoa assays specifically detect doubly phosphorylated tau
- **Statement**: Two sandwich Simoa immunoassays were developed — C231D181 (capture p-tau231 + detect p-tau181) and C231D217 (capture p-tau231 + detect p-tau217) — that require concurrent phosphorylation at two sites (T181&T231 or T217&T231) on a single tau molecule to generate signal, and both passed analytical validation for CSF and plasma.
- **Status**: supported
- **Falsification criteria**: Signal is produced by a mix of single-site phosphorylated peptides (no double phosphorylation), or precision/linearity/sensitivity metrics fall outside acceptable assay ranges.
- **Proof**: [E01]
- **Evidence basis**: A run with a mix of single-site phosphorylated peptides produced a blank-level signal, showing double phosphorylation is required to form the immunocomplex (§Technical validation). Both assays reported LLOQ/ULOQ, intra/inter-assay CV, dilution linearity, and spike-recovery within reported ranges.
- **Interpretation**: The dual-site sandwich geometry is a general, flexible platform for measuring any multiphosphorylated proteoform.
- **Dependencies**: none
- **Tags**: assay-development, specificity, Simoa

## C02: CSF p-tau181&231 and p-tau217&231 discriminate AD continuum from controls with high accuracy
- **Statement**: In both cohorts, CSF p-tau181&231 and p-tau217&231 were significantly elevated in all AD continuum groups vs NDC and yielded high diagnostic accuracy (discovery CSF AUC range 0.986–1.000; validation CSF AUC range 0.927–1.000).
- **Status**: supported
- **Falsification criteria**: CSF p-tau181&231 or p-tau217&231 fails to separate any AD continuum group from NDC, or AUC drops to chance level.
- **Proof**: [E02, E03]
- **Evidence basis**: Figure 2a, Figure 4a show significant elevation (p ≤ 0.0001 markers) with large Cohen's d; text reports discovery CSF AUC range 0.986–1.000 and validation CSF AUC range 0.927–1.000 (Supplementary Table 15).
- **Interpretation**: Multiphosphorylated tau is a viable CSF AD biomarker on par with single-site CSF p-tau.
- **Dependencies**: C01
- **Tags**: CSF, diagnostic-accuracy, AUC

## C03: Plasma p-tau217&231 outperforms single-site plasma p-tau217 and p-tau231
- **Statement**: Plasma p-tau217&231 consistently showed improved diagnostic performance versus single-site plasma p-tau217 or p-tau231, yielding the highest nominal AUC among plasma markers for NDC vs all combined AD continuum (discovery AUC = 0.979, 95% CI 0.945–1.000; validation AUC = 0.968, 95% CI 0.929–1.000), with a statistically significant difference from plasma p-tau217 but not always from plasma p-tau231.
- **Status**: supported
- **Falsification criteria**: Plasma p-tau217&231 AUC is not higher than plasma p-tau217/p-tau231, or the improvement is never statistically significant.
- **Proof**: [E03, E05]
- **Evidence basis**: Figure 3a (discovery AUC 0.979 [0.945–1.000] > p-tau231 0.936 [0.875–0.997] > p-tau217 0.913 [0.837–0.990]); Figure 3b (validation AUC 0.968 [0.929–1.000] > p-tau231 0.910 [0.846–0.975] > p-tau217 0.856 [0.768–0.943]). Text: significant difference vs plasma p-tau217 (NDC vs MCI-AD and NDC vs AD-dem) but not vs p-tau231 (Supplementary Table 16).
- **Interpretation**: Doubly phosphorylated p-tau217&231 may be a superior blood-based AD biomarker to existing single-site plasma p-tau.
- **Dependencies**: C01
- **Tags**: plasma, diagnostic-accuracy, ROC, added-value

## C04: Plasma p-tau181&231 fails to differentiate AD continuum from controls
- **Statement**: Plasma p-tau181&231 levels did not significantly differ between NDC and any AD continuum group (negligible standardized effect, Cohen's d < 0.2), and plasma p-tau181&231 did not correlate with CSF/plasma p-tau181, p-tau231, nor with its own CSF equivalent (CSF p-tau181&231).
- **Status**: supported
- **Falsification criteria**: Plasma p-tau181&231 separates any AD group from NDC, or correlates strongly (ρ high) with its CSF equivalent.
- **Proof**: [E02, E04, E05]
- **Evidence basis**: Figure 2b (Plasma p-tau181&231 Cohen's d MCI-AD/NDC = 0.00, AD-dem/NDC = 0.17; no significance markers); text ROC discovery NDC vs MCI-AD AUC = 0.514 (0.320–0.709), NDC vs AD-dem AUC = 0.579 (0.383–0.775). Figure 1a: plasma p-tau181&231 correlations are near zero/negative with all markers (e.g., −0.06 with plasma p-tau217&231; −0.13 with CSF p-tau181&231).
- **Interpretation**: The p-tau181&231 proteoform behaves matrix-dependently — diagnostic in CSF, uninformative in plasma.
- **Dependencies**: C01, C02
- **Tags**: plasma, negative-result, p-tau181&231

## C05: p-tau217&231 shows the highest median fold change across the AD continuum
- **Statement**: p-tau217&231 (C231D217 assay) showed the highest median concentration fold change (AD continuum groups vs NDC) among all measured markers in both CSF and plasma (e.g., plasma p-tau217&231 discovery AD-dem/NDC = 13.63, validation AD-dem/NDC = 20.6; CSF p-tau217&231 discovery AD-dem/NDC = 18.13), with large standardized effect size for all comparisons.
- **Status**: supported
- **Falsification criteria**: Another marker shows a larger AD-dem/NDC median fold change than p-tau217&231 in both matrices.
- **Proof**: [E05]
- **Evidence basis**: Text (§Diagnostic performance, both cohorts) reporting fold changes from Supplementary Table 17; Figure 2 & Figure 4 Cohen's d tables (p-tau217&231 large effect throughout).
- **Interpretation**: The p-tau217&231 proteoform has the widest dynamic range across disease stages, supporting its use as a staging/early marker.
- **Dependencies**: C01
- **Tags**: fold-change, effect-size, p-tau217&231

## C06: CSF vs plasma divergence for p-tau181&231 indicates matrix-specific tau processing
- **Statement**: The diagnostic performance of p-tau181&231 significantly differs between CSF (diagnostic) and plasma (non-diagnostic), and plasma p-tau181&231 does not correlate with CSF p-tau181&231, consistent with matrix-specific protein processing / differential tau fragmentation between compartments.
- **Status**: supported
- **Falsification criteria**: Plasma and CSF p-tau181&231 show equivalent diagnostic behavior and strong cross-matrix correlation.
- **Proof**: [E02, E03, E04]
- **Evidence basis**: Contrast between C02 (CSF diagnostic) and C04 (plasma non-diagnostic); Figure 1a cross-matrix correlations for p-tau181&231 near zero/negative; Discussion attributes this to matrix-specific processing and known differential truncation (residues 221–226) between compartments (refs 16, 35–37, 39).
- **Interpretation**: Tau fragmentation/truncation differs between CSF and plasma, altering which doubly phosphorylated epitopes survive in each matrix — a mechanistic hypothesis requiring further study (interpretive, not directly measured here).
- **Dependencies**: C02, C04
- **Tags**: matrix-effect, mechanism-hypothesis

## C07: Single-site and multiphosphorylated p-tau markers are elevated across the AD continuum but do not distinguish AD from FTD relative to controls
- **Statement**: CSF and plasma p-tau181, p-tau217, p-tau231 and p-tau217&231, and CSF (but not plasma) p-tau181&231, were significantly elevated across AD continuum groups vs NDC; CSF p-tau181/p-tau231/p-tau181&231 did NOT differ between NDC and FTD, while CSF p-tau217/p-tau231/p-tau217&231 discriminated AD-dem vs FTD (validation AUC range 0.934–0.978) and plasma p-tau217/p-tau231/p-tau217&231 discriminated AD-dem vs FTD (AUC range 0.803–0.904).
- **Status**: supported
- **Falsification criteria**: p-tau markers separate NDC from FTD, or fail to separate AD-dem from FTD where reported.
- **Proof**: [E02, E07]
- **Evidence basis**: Figure 2, Figure 4 (elevation vs NDC); text: CSF p-tau181/231/181&231 did not differ NDC vs FTD; AD-dem vs FTD AUC ranges (CSF 0.934–0.978; plasma 0.803–0.904) from Supplementary Table 15.
- **Interpretation**: These markers reflect AD-specific tau pathology, not generic neurodegeneration.
- **Dependencies**: C02
- **Tags**: FTD, specificity, differential-diagnosis

## C08: Highest AUC also under CSF AT-profile-based grouping
- **Statement**: In ROC analysis by patients' CSF AT profile, plasma p-tau217&231 yielded the highest nominal AUC and standardized effect size among plasma markers (discovery A+ vs A− AUC = 0.979, 95% CI 0.945–1.000; A+T+ vs other AUC = 0.973, 95% CI 0.934–1.000; validation A+ vs A− AUC = 0.914, 95% CI 0.855–0.973; A+T+ vs other AUC = 0.894, 95% CI 0.831–0.957).
- **Status**: supported
- **Falsification criteria**: Another plasma marker exceeds plasma p-tau217&231 AUC under AT-profile grouping.
- **Proof**: [E06]
- **Evidence basis**: Text (§Diagnostic performance, both cohorts) citing Supplementary Fig. 1 values.
- **Interpretation**: The superiority of plasma p-tau217&231 is robust to how the AD continuum is defined (clinical stage vs biomarker profile).
- **Dependencies**: C03
- **Tags**: plasma, AT-profile, robustness
