# Experiments (Analysis / Verification Plans)

For a systematic review, "experiments" are the review's analysis procedures and the verification
procedures a reader would run to check its claims. Directional only — exact counts/values live in
`evidence/`.

## E01: PRISMA search, screening, and corpus reconstruction
- **Verifies**: C11
- **Setup**:
  - Sources: five databases — Scopus, Web of Science, ScienceDirect, IEEE Xplore, PubMed.
  - Search date: 20 February 2025.
  - Query: four Boolean-combined concept domains (disease/cohort × core technology/architecture × task × data/methodology).
  - Screeners: two independent reviewers with consensus adjudication.
- **Procedure**:
  1. Execute the search string per database (Table 2).
  2. Remove duplicate records.
  3. Screen titles/abstracts against scope.
  4. Full-text eligibility assessment against inclusion/exclusion criteria (Table 3), screening for data leakage.
  5. Tally the final corpus and compare scope columns to prior reviews (Table 1).
- **Metrics**: counts at each PRISMA stage (identified, deduplicated, screened, excluded, included); per-database found/selected.
- **Expected outcome**:
  - A funnel from a large initial pool down to a much smaller included set, dominated by ScienceDirect/Scopus contributions.
  - The review's scope-coverage exceeds every prior review in Table 1.
- **Baselines**: the 8 prior reviews in Table 1.
- **Dependencies**: none

## E02: Architecture-taxonomy classification (ViT vs CViT, integration pattern)
- **Verifies**: C01, C10
- **Setup**: The included corpus; taxonomy of standalone ViT vs hybrid CViT and (for CViT) serial/parallel/hierarchical integration.
- **Procedure**:
  1. Assign each study to ViT or CViT.
  2. For CViT, classify architectural-integration pattern and attention-integration type.
  3. Populate the categorization tree (Fig. 15) and summary tables (Tables 4, 5).
- **Metrics**: count of ViT vs CViT studies; distribution of integration patterns.
- **Expected outcome**: CViT studies substantially outnumber ViT studies; serial integration is the most common CViT pattern.
- **Baselines**: none
- **Dependencies**: E01

## E03: Modality-utilization analysis
- **Verifies**: C02
- **Setup**: The included corpus; modality tags (sMRI, PET, fMRI, DTI, CSF, genetic, clinical).
- **Procedure**:
  1. Tag each study's modality configuration (single vs multi) and specific modalities.
  2. Aggregate single-modality counts overall (Fig. 16b) and per ViT (Fig. 17) / CViT (Fig. 25).
  3. Aggregate multimodal data-type combinations (Fig. 16a).
- **Metrics**: per-modality study counts and shares.
- **Expected outcome**: sMRI dominates single-modality usage in both ViT and CViT groups; multimodal combinations are led by sMRI+PET and sMRI+clinical.
- **Baselines**: none
- **Dependencies**: E01

## E04: Dataset-dependency analysis
- **Verifies**: C03
- **Setup**: The included corpus; dataset tags (ADNI, OASIS, AIBL, Kaggle, NACC, UK Biobank, AANLIB, HUASHAN-MCI, Dong-A).
- **Procedure**:
  1. Record which dataset(s) each study used (Tables 4, 5, 7).
  2. Compute ADNI share within ViT and CViT groups.
  3. Note external/multi-dataset validation usage.
- **Metrics**: dataset-usage counts/shares; number of studies using multiple/external datasets.
- **Expected outcome**: ADNI appears in a large majority of studies in both groups; external validation is more common among CViT works than ViT works.
- **Baselines**: none
- **Dependencies**: E01

## E05: Diagnostic-focus tally (classification vs MCI progression)
- **Verifies**: C04
- **Setup**: The included corpus; objective tags (AD classification, MCI progression, both).
- **Procedure**:
  1. Tag each study's diagnostic objective(s).
  2. Aggregate counts per ViT/CViT and per single/multimodal (Fig. 15 leaves).
- **Metrics**: counts of classification-only vs progression-only vs both.
- **Expected outcome**: Classification-focused studies greatly outnumber progression-focused studies.
- **Baselines**: none
- **Dependencies**: E01

## E06: Multimodal-fusion prevalence and strategy analysis
- **Verifies**: C07
- **Setup**: The included corpus; fusion-level tags (input/intermediate/output/hybrid/knowledge-based).
- **Procedure**:
  1. Identify multimodal studies within ViT and CViT groups.
  2. Classify each multimodal study's fusion strategy.
  3. Compare multimodal prevalence between groups.
- **Metrics**: multimodal share in ViT vs CViT; distribution over fusion levels.
- **Expected outcome**: Multimodal fusion is far more prevalent in CViT than ViT studies; intermediate (feature-level) fusion dominates.
- **Baselines**: none
- **Dependencies**: E02

## E07: Reproducibility and framework audit
- **Verifies**: C05, C06
- **Setup**: The included corpus; per-study framework and code-availability annotation (Table 6, Fig. 42).
- **Procedure**:
  1. Record the DL framework reported by each study.
  2. Record whether public code is available (and whether by-request only).
  3. Aggregate framework counts (Fig. 42a) and code-availability share (Fig. 42b).
- **Metrics**: framework usage counts; fraction of studies with public code.
- **Expected outcome**: PyTorch is the most-used framework; a small minority of studies share code.
- **Baselines**: comparison to a radiology meta-study code-sharing rate cited by the paper.
- **Dependencies**: E01

## E08: Dataset-bias categorization / external-validation audit
- **Verifies**: C08
- **Setup**: The included corpus; bias-category assignment (Category 1 high / 2 moderate / 3 lower).
- **Procedure**:
  1. Classify each study by validation rigor and dataset diversity.
  2. Contrast reported internal accuracies against externally-validated accuracies for Category-3 exemplars.
- **Metrics**: distribution over bias categories; internal vs external accuracy gap.
- **Expected outcome**: Most studies fall in high/moderate-risk categories with optimistic internal metrics; externally-validated models report lower, more realistic performance.
- **Baselines**: Category-3 externally-validated studies as the reference standard.
- **Dependencies**: E04

## E09: Reviewed ViT-vs-CNN head-to-head comparison synthesis
- **Verifies**: C09
- **Setup**: Subset of reviewed studies reporting direct transformer-vs-CNN benchmarks (e.g. [158], [30], [159], [162]).
- **Procedure**:
  1. Extract head-to-head accuracy comparisons from those studies.
  2. Summarize the direction of the transformer-vs-CNN ordering, noting counter-examples.
- **Metrics**: relative ordering (transformer vs CNN) per task; note tasks where CNN wins.
- **Expected outcome**: Transformers generally match/outperform CNNs on binary AD classification, with at least one counter-example on a harder multi-class PET task.
- **Baselines**: modern CNNs (ResNet, DenseNet, EfficientNet, VGG19).
- **Dependencies**: E01
