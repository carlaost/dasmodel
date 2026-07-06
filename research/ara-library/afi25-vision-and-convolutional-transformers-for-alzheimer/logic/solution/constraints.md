# Constraints, Assumptions, and Limitations

## Scope boundaries (what the review covers)
- **Time window**: studies published 2021–2025 only (search executed 20 Feb 2025).
- **Venues**: peer-reviewed journal articles only — conference papers, preprints, book chapters, patents, surveys, and conference abstracts are excluded (Table 3).
- **Databases**: five — Scopus, Web of Science, ScienceDirect, IEEE Xplore, PubMed. Works outside these are excluded.
- **Language**: English-only.
- **Architectures**: studies must incorporate some form of ViT or CViT; pure CNN/3DCNN/ML-only works are excluded.
- **Tasks**: AD classification and/or MCI-to-AD conversion prediction, using neuroimaging and/or clinical data.

## Methodological assumptions
- A1: Two independent reviewers with consensus adjudication adequately mitigate selection bias.
- A2: Reported performance metrics from primary studies are tabulated at face value (the review runs no experiments of its own) while critically annotating validation weaknesses (data leakage, missing external validation).
- A3: The fusion-level hierarchy (input/intermediate/output, adapted from [47, 174, 175]) and the serial/parallel/hierarchical integration taxonomy are appropriate organizing frameworks.
- A4: The categorization counts (Fig. 15, Tables 4–7) are the authoritative tallies; where the running text and a figure disagree (see the sMRI 14-vs-15 note in claims C02), both are reproduced.

## Stated limitations of the reviewed field (the review's critique, §12.1)
- **L1 — Multimodal fusion underutilized/vague**: many works are single-modal; multimodal ones often default to simple late fusion and omit alignment/normalization details (reproducibility risk).
- **L2 — Preprocessing non-standardization**: heterogeneous skull-stripping, bias-field correction, and normalization choices make cross-study comparison unreliable.
- **L3 — Spatiotemporal/volumetric underuse**: 3D volumes are frequently reduced to 2D slices; the temporal (longitudinal) dimension is rarely modeled.
- **L4 — Dataset homogeneity & bias**: over-reliance on ADNI (demographically White/highly-educated, single-protocol) risks shortcut learning and inequitable performance; external validation is rare.
- **L5 — Accuracy paradox**: >99% accuracies on curated/balanced internal test sets do not reflect clinical utility, especially for MCI conversion.
- **L6 — Uncritical data augmentation**: geometric augmentations may create biologically implausible anatomy; augmentation's effect on generalizability is rarely tested.
- **L7 — Computational cost**: self-attention scales quadratically with sequence length, a deployment bottleneck for 3D neuroimaging in resource-constrained hospital IT.
- **L8 — Trustworthiness gap**: little uncertainty quantification; post-hoc XAI (saliency maps) shows *where* not *why*; models are "knowledge islands" disconnected from biomedical knowledge bases.
- **L9 — Reproducibility crisis**: ~85% of studies do not share code; licensing is neglected; domain-specific pretrained neuroimaging models are scarce.
- **L10 — Clinical-deployment barriers**: integration with PACS/EHR, model lifecycle/maintenance, human-in-the-loop feedback, and ethics/privacy (re-identification from sMRI, vulnerable-population consent) are largely unaddressed.

## Limitations of the review itself (implicit / inferred)
- The review does not re-execute or re-validate any primary study's model; bias categorization is by reported methodology, so no study is definitively labelled biased.
- No PROSPERO registration ID is reported (PRISMA-2020 adherence only) — reproducibility of the search/selection is not independently pre-registered.
- The LVM comparison (Table 8) is explicitly "representative rather than exhaustive," curated to illustrate a narrative rather than sampled systematically.
- The review releases no dataset or code of its own ("No datasets were generated or analysed during the current study").
