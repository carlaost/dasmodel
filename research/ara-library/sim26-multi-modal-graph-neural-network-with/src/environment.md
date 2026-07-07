# Environment

- **Language/runtime**: Not specified in paper.
- **Framework**: Not specified in paper (no deep-learning framework, e.g. PyTorch/TensorFlow, is
  named).
- **Hardware**: Not specified in paper (no GPU/CPU type, count, or memory is stated).
- **Data sources**: Alzheimer's Disease Neuroimaging Initiative (ADNI) study — T=919 preclinical AD
  subjects. Each subject's brain was partitioned into 148 cortical + 12 sub-cortical = 160 ROIs
  using the Destrieux atlas [3]. Structural brain networks (graph edges) were constructed from
  tractography on diffusion-weighted imaging (DWI), calculating the number of white-matter fibers
  connecting the 160 regions. On the same parcellation, three region-wise imaging features were
  measured: Standard Uptake Value Ratio (SUVR) of metabolic intensity from FDG-PET, β-Amyloid
  protein from Amyloid-PET, and cortical thickness from MRI (§3, Dataset). See `data/dataset.md`
  for full cohort breakdown.
- **Key dependencies**: Not specified in paper (no software library versions given).
- **Protocols**: 5-fold cross-validation used throughout to obtain "unbiased results" (§3, Setup).
  Four separate 3-way classification experiments were run, one per modality combination (Cortical
  Thickness & β-Amyloid; Cortical Thickness & FDG; β-Amyloid & FDG; All Imaging Features). Baselines
  were grouped into three families: (1) convolution-based GNNs (GCN [12], GAT [22]), (2) GNNs with
  graph diffusion (GraphHeat [26], GDC [7], ADC [27], LSAP [18]), and (3) graph transformers
  (NodeFormer [24], DIFFormer [23], SGFormer [25]). The paper states "More details are given in the
  supplementary" (§3, Setup) — no supplementary document was included in this ARA's input, so
  training/optimization details beyond this summary cannot be grounded.
- **Random seeds**: Not specified in paper.
- **Reproducibility note**: No code repository, trained model weights, or a supplementary
  document/appendix accompanies the 10-page main text provided as input to this ARA. All
  hyperparameters referenced in `logic/solution/algorithm.md` and `logic/solution/constraints.md`
  (`Z`, `P`, `C`, `α`, `β`, optimizer, epochs, batch size) are therefore recorded as
  "Not specified in paper."
