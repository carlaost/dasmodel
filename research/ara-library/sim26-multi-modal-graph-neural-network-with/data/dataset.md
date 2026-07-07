# Dataset

## Cohort
- **Source**: Alzheimer's Disease Neuroimaging Initiative (ADNI) study.
- **Size**: T = 919 preclinical AD subjects (§3, Dataset).
- **Group labels** (3-way classification target):
  - Control (CN): T = 333
  - Significant Memory Concern (SMC): T = 172
  - Early Mild Cognitive Impairment (EMCI): T = 414
  - (333 + 172 + 414 = 919, consistent with the total T stated.)
- **Licensing / consent / IRB**: Not specified in paper (standard ADNI data-use terms are not
  restated here; this ARA does not independently verify ADNI's access/consent framework).

## Graph Construction
- **Parcellation**: Destrieux atlas [3] — 148 cortical regions + 12 sub-cortical regions = 160 ROIs
  per subject, used as graph nodes.
- **Edges**: Tractography on diffusion-weighted imaging (DWI) was applied to calculate the number
  of white-matter fibers connecting the 160 brain regions, constructing the per-subject brain
  network (graph).

## Modalities (Nodal Features)
Three region-wise imaging features are measured on the same 160-ROI parcellation:
1. **Cortical thickness** — from MRI.
2. **FDG** — Standard Uptake Value Ratio (SUVR) [20] of metabolic intensity from FDG-PET.
3. **β-Amyloid** — β-Amyloid protein burden from Amyloid-PET.

## Experimental Modality Combinations (Table 1)
Four 3-way classification experiments, each using a different subset of the three modalities as
nodal features:
1. Cortical Thickness & β-Amyloid
2. Cortical Thickness & FDG
3. β-Amyloid & FDG
4. All Imaging Features (all three modalities)

## Evaluation Protocol
- 5-fold cross-validation, reporting mean ± standard deviation of accuracy, precision, and recall
  (§3, Setup).
- Not specified in paper: train/val/test split ratios within each fold, whether folds are
  subject-stratified by diagnostic group, or any subject exclusion criteria beyond group
  assignment.

## Provenance Notes
- No preprocessing pipeline beyond atlas parcellation, DWI tractography, and SUVR computation is
  described; no additional normalization/harmonization steps (e.g., across scanners or sites) are
  mentioned in the main text.
- The paper does not report ADNI phase (ADNI-1/GO/2/3), scanner field strength, or acquisition
  protocol details — these are "Not specified in paper."
