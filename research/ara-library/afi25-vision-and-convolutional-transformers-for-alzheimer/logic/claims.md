# Claims

All numbers below are the review's own synthesized findings over the 68 reviewed studies; they are
tagged `[result]` and cited to the paper's text/figures/tables. Per-study performance values are not
promoted into claim Statements (they live in `evidence/tables/`).

## C01: Hybrid CViTs have overtaken pure ViTs as the dominant transformer paradigm
- **Statement**: Of the 68 reviewed studies, 46 use CViT (hybrid CNN+transformer) architectures and 22 use standalone ViTs, making CViT the dominant and most-adopted paradigm for AD diagnosis.
- **Status**: supported
- **Falsification criteria**: Show that a correct re-tally of the 68 studies yields more ViT than CViT studies, or that the ViT/CViT split is not 22/46.
- **Proof**: [E02]
- **Evidence basis**: Fig. 15 categorization tree labels "ViT Studies (22)" and "CViT Studies (46)"; §8 states "systematically analyzes 46 such studies"; §7 states "reviews 22 studies".
- **Interpretation**: The paper frames this as a "decisive architectural shift" toward hybrids that synergize CNN local features with transformer global context; the count itself only shows prevalence, not superiority.
- **Sources**:
  - 46 ← Fig. 15 / §8 «This section systematically analyzes 46 such studies» [result]
  - 22 ← §7 «The subsequent discussion reviews 22 studies» [result]
  - 68 ← Abstract/§3 «ultimately selecting 68 studies» [result]
- **Dependencies**: none
- **Tags**: architecture, CViT, ViT, trend

## C02: sMRI is the predominant input modality
- **Statement**: Across single-modality studies the modality distribution is sMRI 31, fMRI 7, PET 3; within ViT single-modality studies sMRI=15, PET=2, fMRI=4 (Fig. 17) and within CViT single-modality studies sMRI=16, PET=1, fMRI=3 (Fig. 25).
- **Status**: supported
- **Falsification criteria**: Re-tally of modality usage contradicts sMRI being the most-used single modality, or the figure bar labels differ from these values.
- **Proof**: [E03]
- **Evidence basis**: Fig. 16b bar labels (sMRI 31, PET 3, fMRI 7); Fig. 17 bar labels (15/2/4); Fig. 25 bar labels (16/1/3); §8.3.2 "sMRI was the preponderant choice, utilized in 16 studies (approximately 80% of single-modality CViT applications)".
- **Interpretation**: sMRI's dominance is attributed to availability, low cost, and non-invasiveness; the paper flags it as a factor in dataset homogeneity/bias.
- **Note (source inconsistency)**: §7.3.2 states sMRI is "approximately 70% (14 out of 20)" of single-modality ViT applications, but the Fig. 17 bar label reads 15. Reproduced verbatim; the 14-vs-15 discrepancy is the paper's own.
- **Sources**:
  - 31 ← Fig. 16b bar label «sMRI ... 31» [result]
  - 15 (ViT sMRI) ← Fig. 17 bar label «15» [result]
  - 16 (CViT sMRI) ← Fig. 25 bar label «16»; §8.3.2 «utilized in 16 studies (approximately 80% of single-modality CViT applications)» [result]
- **Dependencies**: none
- **Tags**: modality, sMRI, data-utilization

## C03: The field is over-reliant on the ADNI dataset
- **Statement**: ADNI appears in roughly 73% (16/22) of ViT studies and ~72% (33/46) of CViT studies, making it the central resource and a source of dataset-homogeneity/bias risk.
- **Status**: supported
- **Falsification criteria**: A correct count shows ADNI usage well below the reported ~72–73%, or Table 7's ADNI study list does not dominate.
- **Proof**: [E04]
- **Evidence basis**: §7.3.2 "roughly 73% (16 out of 22) of all examined ViT studies"; §8.3.3 "approximately 33 of the 46 studies (~72%)"; Table 7 lists ADNI as used by the largest set of studies.
- **Interpretation**: The paper argues ADNI's demographic (predominantly White, highly educated) and technical homogeneity inflates internal metrics and threatens generalizability/equity.
- **Sources**:
  - 16/22 (~73%) ← §7.3.2 «roughly 73% (16 out of 22) of all examined ViT studies» [result]
  - 33/46 (~72%) ← §8.3.3 «approximately 33 of the 46 studies (~72%)» [result]
- **Dependencies**: C02
- **Tags**: dataset, ADNI, bias, generalizability

## C04: MCI-to-AD progression prediction is underexplored relative to AD classification
- **Statement**: The majority of the 68 studies target AD-stage classification; only a small number address MCI-to-AD conversion (pMCI vs sMCI), leaving prognosis underdeveloped.
- **Status**: supported
- **Falsification criteria**: A tally shows progression-prediction studies are as numerous as classification studies.
- **Proof**: [E05]
- **Evidence basis**: §7.3.3 "Only two studies focused solely on this using single-modality data"; §8.3.4 "Prediction of MCI progression was the sole focus in fewer instances"; Conclusion "the clinically vital task of predicting MCI-to-AD progression remaining relatively underexplored"; Fig. 15 category leaves.
- **Interpretation**: The paper treats this as a critical clinical gap because progression prediction enables early intervention.
- **Sources**:
  - "Only two studies focused solely on this" (single-modality ViT MCI prediction) ← §7.3.3 «Only two studies focused solely on this using single-modality data» [result]
- **Dependencies**: none
- **Tags**: MCI, prognosis, gap

## C05: A pervasive reproducibility gap — only ~15% of studies share code
- **Statement**: Only ten of the 68 reviewed studies provided publicly accessible source code (one requiring direct author correspondence), i.e. ~15% code availability vs 85% unavailable.
- **Status**: supported
- **Falsification criteria**: Table 6 code-availability column yields substantially more than 10 studies with public code, or Fig. 42b percentages differ from 15%/85%.
- **Proof**: [E07]
- **Evidence basis**: §9 "only ten of the 68 reviewed studies provided publicly accessible source code, with one requiring direct author correspondence"; §9.1 "a mere 15% of the 68 reviewed studies provided publicly accessible code"; Fig. 42b pie (15% available / 85% not available); Table 6 code column.
- **Interpretation**: Framed as a "reproducibility crisis" impeding verification, wasting resources, and blocking clinical translation.
- **Sources**:
  - 10/68 ← §9 «only ten of the 68 reviewed studies provided publicly accessible source code, with one requiring direct author correspondence» [result]
  - 15% ← §9.1 «a mere 15% of the 68 reviewed studies provided publicly accessible code»; Fig. 42b label «15%» [result]
  - 85% ← Fig. 42b label «85%» [result]
- **Dependencies**: none
- **Tags**: reproducibility, open-source, code-availability

## C06: PyTorch is the most-used implementation framework
- **Statement**: Among the reviewed studies, PyTorch was used in 35, TensorFlow in 13, Keras in 2, MATLAB in 2, Theano in 2, AWS SageMaker in 1, and 19 did not report a framework.
- **Status**: supported
- **Falsification criteria**: Fig. 42a / Table 6 framework tallies differ from these bar-label values.
- **Proof**: [E07]
- **Evidence basis**: §9 "PyTorch was utilized in 35 of the reviewed studies … TensorFlow was employed in 13 studies … Keras, used in two studies"; Fig. 42a bar labels (PyTorch 35, Not reported 19, TensorFlow 13, Keras 2, MATLAB 2, Theano 2, AWS SageMaker 1).
- **Interpretation**: PyTorch's dynamic graph favors research prototyping of bespoke transformer architectures.
- **Sources**:
  - 35 (PyTorch) ← §9 «PyTorch was utilized in 35 of the reviewed studies»; Fig. 42a label «35» [result]
  - 13 (TensorFlow) ← §9 «TensorFlow was employed in 13 studies»; Fig. 42a label «13» [result]
  - 19 (Not reported) ← Fig. 42a bar label «19» [result]
- **Dependencies**: none
- **Tags**: frameworks, PyTorch, tooling

## C07: Multimodal fusion is far more prevalent in CViT than ViT studies
- **Statement**: Explicit multimodal integration appears in only 2 of 22 ViT studies (~9%) but in 26 of 46 CViT studies (~57%).
- **Status**: supported
- **Falsification criteria**: Correct counts show comparable multimodal prevalence in ViT and CViT groups.
- **Proof**: [E06]
- **Evidence basis**: §7.3.4 "explicit multimodal data integration was infrequent, observed in only two studies (approximately 9%)"; §8.3.2 "the majority of CViT research (26 out of 46 studies, ~57%) employed multimodal approaches"; Fig. 15 (ViT Multi-modality 2, CViT Multi-modality 26).
- **Interpretation**: CViTs' inductive-bias and architectural flexibility make them better suited to fusing heterogeneous data.
- **Sources**:
  - 2/22 (~9%) ← §7.3.4 «observed in only two studies (approximately 9%)» [result]
  - 26/46 (~57%) ← §8.3.2 «26 out of 46 studies, ~57%) employed multimodal approaches» [result]
- **Dependencies**: C01
- **Tags**: multimodal, fusion, CViT

## C08: High benchmark accuracies reflect methodological bias risk, not clinical readiness ("accuracy paradox")
- **Statement**: The vast majority of the 68 studies (bias Categories 1 and 2) rely on single-dataset internal validation without external validation, so reported near-perfect accuracies (often >99%) likely overstate real-world performance; only a small Category-3 group performing rigorous external validation reports lower, more believable metrics (e.g. ~90–93% and ~77%).
- **Status**: supported
- **Falsification criteria**: Demonstrate that most reviewed studies did perform rigorous external validation, or that externally-validated models match the >99% internal accuracies.
- **Proof**: [E08]
- **Evidence basis**: §10.1 categorizes the 68 studies into high/moderate/lower bias risk; "the vast majority of the 68 papers reviewed … exhibit a high methodological risk of bias"; §12.1.3 "the reporting of exceptionally high performance metrics, often accuracies exceeding 99% … risk creating an illusion of clinical readiness"; Category-3 examples (Xin et al. [31] ~90–93%, Gao et al. [172] ~77%).
- **Interpretation**: The paper calls for a shift from accuracy toward AUC on imbalanced classes, external-cohort performance, and calibration.
- **Sources**:
  - ">99%" accuracies ← §12.1.3 «the reporting of exceptionally high performance metrics, often accuracies exceeding 99%» [result]
  - "90-93% and 77%" (external-validation range) ← §10.1 «accuracy scores (in the 90-93% and 77% ranges, respectively)» [result]
- **Dependencies**: C03
- **Tags**: bias, external-validation, accuracy-paradox, clinical-readiness

## C09: In reviewed head-to-head comparisons, transformer models outperform CNN baselines
- **Statement**: Multiple reviewed benchmarks report transformer architectures matching or significantly outperforming modern CNNs on AD classification (e.g. DeiT "significantly outperformed all tested CNN models" per Carcagni et al. [158]; CViTs from Khatri & Kwon [30] and Hosny et al. [159] beat CNN baselines).
- **Status**: supported (as a reported trend, not a re-run comparison)
- **Falsification criteria**: The cited reviewed studies do not actually report transformer > CNN, or a systematic re-analysis reverses the ordering.
- **Proof**: [E09]
- **Evidence basis**: §4.4.2 "Carcagn et al. [158] revealed that a ViT could 'significantly outperform' several modern CNN architectures"; Table 4 (Carcagni: DeiT 77% ADNI2 / ~74% OASIS1).
- **Interpretation**: The advantage is presented as often statistically significant but coming at the cost of ViTs being data-hungry, motivating CViTs; a counter-example exists (Shin et al. [162]: ViT underperformed VGG19 on the ternary PET task, 56.7% vs 66.7%).
- **Sources**:
  - "significantly outperform" ← §4.4.2 «a ViT could "significantly outperform" several modern CNN architectures» [result]
  - counter-example 56.7% vs 66.7% ← §8.1.1 (Shin et al.) «it underperformed in the more challenging ternary classification (56.7% vs. 66.7%)» [result]
- **Dependencies**: C01
- **Tags**: ViT-vs-CNN, benchmark, performance

## C10: The review contributes four novel organizing taxonomies
- **Statement**: The review introduces taxonomies categorizing works by (a) CViT architectural-integration pattern (serial / parallel / hierarchical; plus attention integration), (b) fusion level (input / intermediate / output, plus knowledge-based and hybrid), (c) data modality (single vs multimodal), and (d) diagnostic objective (AD classification vs MCI progression vs both).
- **Status**: supported (contribution claim)
- **Falsification criteria**: These categorization schemes are absent from the paper, or are shown to be directly reproduced from a single prior source without adaptation.
- **Proof**: [E02]
- **Evidence basis**: Abstract "We introduce novel taxonomies to systematically categorize these works by model architecture, data modality, fusion strategy, and diagnostic objective"; Fig. 12 (CViT categorization), Fig. 13 (CViT types), Fig. 14 (fusion levels), Fig. 15 (study categorization).
- **Interpretation**: These taxonomies are the review's primary conceptual scaffolding; some borrow foundational fusion-level concepts (from [47, 174, 175]) but are adapted to the ViT/CViT AD setting.
- **Sources**:
  - "novel taxonomies … model architecture, data modality, fusion strategy, and diagnostic objective" ← Abstract «We introduce novel taxonomies to systematically categorize these works by model architecture, data modality, fusion strategy, and diagnostic objective» [result]
- **Dependencies**: none
- **Tags**: taxonomy, contribution, framework

## C11: This review has broader scope than prior AD-AI reviews
- **Statement**: Compared with 8 prior reviews (Table 1), this is the only one covering all of: AD classification, MCI prediction, ViTs, CViTs, single-modal, multimodal (neuroimaging), multimodal (neuroimaging+clinical), fusion strategies, algorithm reproducibility, and frameworks — across 68 studies (2021–2025).
- **Status**: supported
- **Falsification criteria**: Table 1 shows a prior review with equal-or-greater column coverage, or "Our" row does not span all listed dimensions.
- **Proof**: [E01]
- **Evidence basis**: Table 1 "Our 2025 (2021–2025) 68" row carries checkmarks across all comparison columns while each prior review carries only a subset.
- **Interpretation**: Establishes the review's positioning/novelty relative to [16, 40, 42, 43, 44, 45, 57, 58].
- **Sources**:
  - 68 studies, 2021–2025, full-column coverage ← Table 1 «Our 2025 (2021–2025) 68 ✓✓✓✓✓✓✓✓✓✓» [result]
- **Dependencies**: C01
- **Tags**: scope, novelty, related-work
