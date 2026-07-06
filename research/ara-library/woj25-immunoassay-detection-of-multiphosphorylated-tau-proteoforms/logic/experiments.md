# Experiments

## E01: Analytical (technical) validation of the two immunoassays
- **Verifies**: C01
- **Setup**:
  - Assays: C231D181 (capture p-tau231 / detect p-tau181), C231D217 (capture p-tau231 / detect p-tau217)
  - Instrument: Quanterix HD-X (two independent instruments for dilution linearity)
  - Standards: custom synthetic doubly phosphorylated calibrator peptides (Anaspec); 8-point standard curves
  - Controls: a mix of single-site phosphorylated peptides (specificity control)
- **Procedure**:
  1. Establish standard curve range; determine LLOQ and ULOQ.
  2. Estimate intermediate precision (inter-assay reproducibility) and repeatability (intra-assay) via CV of replicates.
  3. Assess dilution linearity on two independent instruments across serial dilutions of a spiked sample.
  4. Perform spike-recovery at low and high spike levels.
  5. Run a mix of single-site phosphorylated peptides and check whether signal is produced.
  6. Fit standard curves with a 4-parameter logistic model (weighting 1/y for C231D181, 1/y² for C231D217).
- **Metrics**: LLOQ/ULOQ (pg/mL); intra- and inter-assay CV (%); dilution-linearity CV (%) per instrument; spike-recovery (%); signal level for the single-site peptide mix.
- **Expected outcome**:
  - Both assays achieve usable dynamic range and acceptable precision/linearity.
  - The single-site peptide mix yields only a blank-level signal (double phosphorylation required for signal).
- **Baselines**: In-house single-site Simoa assays (p-tau181, p-tau231, p-tau217) as reference measurements.
- **Dependencies**: none

## E02: Cross-group comparison of biomarker concentrations
- **Verifies**: C02, C04, C06, C07
- **Setup**:
  - Cohorts: discovery (n=55) and validation (n=118), University of Perugia
  - Groups: NDC, pre-AD (validation only), MCI-AD, AD-dem, FTD (validation only)
  - Markers: CSF & plasma p-tau181, p-tau217, p-tau231, p-tau181&231, p-tau217&231
- **Procedure**:
  1. Measure all five markers in CSF and plasma for each participant.
  2. Test normality (D'Agostino–Pearson omnibus K2).
  3. Compare groups with Kruskal–Wallis test, followed by Dunn's post-hoc test, adjusting p values for multiple comparisons (two-sided).
  4. Compare each AD continuum group and FTD against NDC.
- **Metrics**: median (Q1–Q3) marker concentration per group; adjusted p values for group differences.
- **Expected outcome**:
  - CSF markers and plasma p-tau217/231/217&231 elevated in AD continuum vs NDC; plasma p-tau181&231 not significantly different from NDC.
  - Markers do not separate NDC from FTD.
- **Baselines**: NDC group.
- **Dependencies**: E01

## E03: ROC diagnostic-accuracy analysis
- **Verifies**: C02, C03, C06
- **Setup**: Same cohorts/markers as E02; comparisons NDC vs each AD stage and NDC vs all combined AD continuum.
- **Procedure**:
  1. Compute ROC curves for each marker/matrix for each comparison.
  2. Compute AUC and 95% CI (Wilson/Brown method).
  3. Compare AUC between assays with the DeLong test (pROC R package).
- **Metrics**: AUC, 95% CI; pairwise AUC comparison p values.
- **Expected outcome**:
  - CSF multiphosphorylated markers achieve high AUC across stages.
  - Plasma p-tau217&231 achieves the highest nominal plasma AUC; plasma p-tau181&231 near chance.
- **Baselines**: Single-site p-tau markers.
- **Dependencies**: E02

## E04: CSF–plasma correlation analysis
- **Verifies**: C04, C06
- **Setup**: Discovery (n=55) and validation (n=118) cohorts; all ten CSF/plasma markers.
- **Procedure**:
  1. Compute Spearman correlation coefficient (ρ) between every marker pair.
  2. Render as correlation heatmaps for each cohort.
- **Metrics**: Spearman ρ per marker pair.
- **Expected outcome**:
  - Strong positive within-matrix and cross-matrix correlations for most markers; plasma p-tau181&231 near-zero/negative correlations with all markers including its CSF equivalent.
- **Baselines**: none (descriptive).
- **Dependencies**: E02

## E05: Effect size and median fold-change analysis
- **Verifies**: C03, C04, C05
- **Setup**: Both cohorts; all markers; AD continuum groups vs NDC.
- **Procedure**:
  1. Compute Cohen's d (effsize R package) for each AD group vs NDC per marker/matrix.
  2. Compute median concentration fold change = median(AD group) / median(NDC).
  3. Rank markers by effect size and fold change.
- **Metrics**: Cohen's d (unitless); median fold change (unitless ratio).
- **Expected outcome**:
  - p-tau217&231 shows the largest fold change in both matrices; plasma p-tau181&231 negligible effect.
- **Baselines**: single-site markers.
- **Dependencies**: E02

## E06: ROC by CSF AT profile
- **Verifies**: C08
- **Setup**: Both cohorts; grouping by CSF AT profile — A+ vs A−, and A+T+ vs other.
- **Procedure**:
  1. Reclassify patients by CSF AT profile rather than clinical stage.
  2. Compute ROC/AUC (Wilson/Brown CI) for each plasma marker.
  3. Compare standardized effect sizes.
- **Metrics**: AUC, 95% CI; standardized effect size.
- **Expected outcome**: Plasma p-tau217&231 gives the highest AUC and effect size among plasma markers under AT-profile grouping.
- **Baselines**: other plasma p-tau markers.
- **Dependencies**: E03

## E07: AD-dem vs FTD discrimination
- **Verifies**: C07
- **Setup**: Validation cohort; AD-dem (n=16) vs FTD (n=39); CSF and plasma p-tau markers.
- **Procedure**:
  1. Compute ROC/AUC for AD-dem vs FTD for each marker.
  2. Also test whether markers differ between NDC and FTD.
- **Metrics**: AUC, 95% CI; group-difference p values.
- **Expected outcome**:
  - CSF p-tau217/231/217&231 and plasma p-tau217/231/217&231 discriminate AD-dem from FTD; CSF p-tau181/231/181&231 do not differ between NDC and FTD.
- **Baselines**: NDC, FTD groups.
- **Dependencies**: E02, E03
