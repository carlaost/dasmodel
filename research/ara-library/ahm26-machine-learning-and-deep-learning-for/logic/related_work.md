# Related Work (Typed Dependency Graph)

This is a survey, so its "dependencies" are the studies it reviews. The eight named primary studies
and the principal supporting review get full `RW` blocks; the remaining citations (largely the author
group's own methodology papers in adjacent domains) are captured briefly to preserve the paper's full
citation footprint. DOIs are transcribed from the References list (PDF p.648-649).

## RW01: Islam & Zhang, 2018 — Ensemble CNN for MRI-based AD diagnosis
- **DOI**: 10.1186/s40708-018-0080-3
- **Type**: baseline
- **Delta**:
  - What changed: Ensemble of deep CNNs classifying AD stages directly from MRI, reducing dependence
    on handcrafted feature extraction.
  - Why: Establish end-to-end deep convolutional diagnosis as a serious direction.
- **Claims affected**: C02
- **Adopted elements**: Cited as the representative early CNN milestone (single-modality; earlier-
  generation benchmark).

## RW02: Lu et al., 2018 — Multimodal multiscale DNN (MRI + FDG-PET)
- **DOI**: 10.1038/s41598-018-22871-z
- **Type**: extends
- **Delta**:
  - What changed: Combined structural MRI and FDG-PET in a multimodal, multiscale deep network,
    including progression-related (MCI-to-AD conversion) prediction.
  - Why: Show multimodal fusion improves diagnosis, especially in clinically challenging settings.
- **Claims affected**: C01
- **Adopted elements**: Bridges single-modality DL to multimodal fusion; strong dependence on curated
  benchmark data noted as its main limitation.

## RW03: Golovanevsky et al., 2022 — Attention-based multimodal DL
- **DOI**: 10.1093/jamia/ocac168
- **Type**: extends
- **Delta**:
  - What changed: Cross-modal attention over imaging + genetic + clinical inputs, moving beyond simple
    feature concatenation.
  - Why: Adaptively weight modalities since not all contribute equally per case.
- **Claims affected**: C01
- **Adopted elements**: Exemplar of attention-based fusion; noted as architecturally complex and less
  deployment-oriented.

## RW04: Qiu et al., 2022 — Successive-step multimodal DL for dementia assessment
- **DOI**: 10.1038/s41467-022-31037-5
- **Type**: extends
- **Delta**:
  - What changed: Multimodal framework identifying CN, MCI, AD, and non-Alzheimer dementias via
    successive diagnostic steps, with external validation across multiple cohorts and interpretability
    analysis.
  - Why: Move beyond binary classification toward clinical decision support.
- **Claims affected**: C01, C04, C06
- **Adopted elements**: Held up as the strongest example of translational ambition (external
  validation); limitation: high complexity and demanding multimodal pipeline.

## RW05: Zhang et al., 2023 — Multi-modal GNN (sMRI + PET + phenotypic)
- **DOI**: 10.1016/j.compbiomed.2023.107328
- **Type**: extends
- **Delta**:
  - What changed: Multi-modal GNN with per-modality GNN branches fused at multiple levels; integrates
    brain-network and phenotypic relational information.
  - Why: CNN multimodal pipelines do not naturally incorporate image-derived + phenotypic relational
    structure; GNNs suit non-Euclidean data.
- **Claims affected**: C03
- **Adopted elements**: Exemplar of relational/graph diagnosis; limitation: graph-construction choices
  affect reproducibility.

## RW06: Castellano et al., 2024 — Uni-/multimodal CNNs (2D/3D MRI + amyloid PET)
- **DOI**: 10.1038/s41598-024-56001-9
- **Type**: baseline
- **Delta**:
  - What changed: Direct comparison of 2D vs 3D MRI and uni-modal vs multimodal (with amyloid PET);
    used the OASIS-3 cohort.
  - Why: Test representational choices; broaden beyond ADNI.
- **Claims affected**: C01
- **Adopted elements**: Supports "3D > 2D" and "multimodal > single-modality" conclusions; limitation:
  mainly centered on one cohort.

## RW07: Hu et al., 2024 — Self-explainable GNN for ADRD risk prediction
- **DOI**: 10.2196/54748
- **Type**: extends
- **Delta**:
  - What changed: Self-explainable GNN emphasizing relation importance as part of the prediction
    process (architecture-level interpretability), using claims/relational health data.
  - Why: Move from post hoc saliency to model-intrinsic explainability.
- **Claims affected**: C05
- **Adopted elements**: Exemplar of self-explainable/architecture-level XAI; limitation: not a pure
  neuroimaging diagnosis system.

## RW08: Zhao et al., 2024 — Vision-transformer-equipped CNN (3D MRI)
- **DOI**: 10.3389/fneur.2024.1490829
- **Type**: extends
- **Delta**:
  - What changed: Hybrid transformer-equipped CNN combining local CNN feature extraction with global
    attention-based context modeling on 3D MRI.
  - Why: Capture long-range dependencies of distributed AD pathology.
- **Claims affected**: C03
- **Adopted elements**: Exemplar of hybrid local-global learning; limitation: transformer benefit
  still requires broader validation.

## RW09: Alsubaie, Luo & Shaukat, 2024 — Systematic review of DL on neuroimaging for AD
- **DOI**: 10.3390/make6010024
- **Type**: imports
- **Delta**:
  - What changed: Supporting systematic review used to substantiate broad observations about datasets,
    modality trends, evaluation practices, reproducibility, and unresolved limitations.
  - Why: Ground the survey's claims about benchmark dependence and weak standardization.
- **Claims affected**: C02, C04, C06
- **Adopted elements**: Cited repeatedly as evidence for field-level challenges (standardization,
  reproducibility, benchmark overreliance).

## Additional citations (brief — background / adjacent-domain methodology, no specific AD-diagnosis delta)
These are largely the author group's own machine-learning methodology papers in other clinical/data
domains, cited to reinforce general points about robust, generalizable modeling. Captured for citation
completeness (References [10]-[14], PDF p.648-649):

- **RW10 — Abubakkar et al., 2025** (DOI 10.63125/13dazp67): prognostic modeling for hepatic disorders;
  cited (p.641) for the general importance of balanced, generalized, robust healthcare ML. Type: imports.
- **RW11 — Ghosh et al., 2024** (DOI 10.32996/jcsts.2024.6.3.2): chronic kidney disease prediction,
  ML algorithms + hybrid model; cited (p.647, Conclusion) as background. Type: imports.
- **RW12 — Reja Sweet et al., 2024** (DOI 10.62527/comien.1.3.21): credit-risk assessment with
  statistical/ML methods; cited (p.647) as background on ML methodology. Type: imports.
- **RW13 — Rakin et al., 2024** (DOI 10.1109/APWiMob64015.2024.10792967): ML/DL framework for cervical
  cancer prediction; cited (p.647) as background. Type: imports.
- **RW14 — Sharif et al., 2025** (DOI 10.1109/ICMCTC62214.2025.11196541): ML framework for DNA sequence
  / splice-junction classification; cited (p.648) as background. Type: imports.
