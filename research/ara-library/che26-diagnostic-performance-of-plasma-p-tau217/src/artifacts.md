# Artifacts

The deliverables of this work are the review synthesis itself and its registration — there is no
released source code or accessioned primary dataset. The concrete, locatable artifacts are described
below (grounded in sources.yaml, verified).

## PROSPERO systematic review registration
- **File(s) in repo**: not a repo file — registered record CRD420261327845 on PROSPERO
  (https://www.crd.york.ac.uk/prospero/).
- **Nature**: prospective systematic-review protocol registration.
- **What it does / contains**: pre-registered protocol for this PRISMA-DTA network meta-analysis of
  plasma p-tau isoforms across the AD continuum. Access: open (verified).
- **How to use / run**: search the PROSPERO register for identifier CRD420261327845.
- **Claims supported**: methodological grounding for C01-C08 (pre-specified protocol).

## Extracted summary-data (network meta-analysis inputs)
- **File(s) in repo**: not released as an accessioned dataset; per the Data Availability statement the
  extracted contributions are "included in the article/Supplementary material" and available on request
  from the corresponding author. Referenced Supplementary items: Table S1 (QUADAS-2), Table S2 (ratio
  AUC-gain meta-analysis), Figures S1-S4 (subgroup/ranking curves).
- **Nature**: extracted diagnostic-accuracy summary statistics (AUC ± 95% CI, sensitivity, specificity)
  mapped to biomarker+platform nodes.
- **What it does / contains**: the per-study AUCs feeding the NMA; produced by two independent reviewers
  using a standardized extraction form (§2.4).
- **How to use / run**: obtain via the article's Supplementary material
  (https://www.frontiersin.org/articles/10.3389/fnagi.2026.1834591/full#supplementary-material) or the
  corresponding author.
- **Claims supported**: C01-C08 (the pooled estimates in `evidence/`).

## Underlying AD cohorts (secondary data, not released here)
- **File(s) in repo**: none — controlled/by-request access via each cohort's consortium.
- **Nature**: established AD research cohorts reused as the primary data behind the extracted AUCs.
- **What it does / contains**: BioFINDER-1/2, ADNI, TRIAD, WRAP, ALFA+, MCSA, Coimbra, ALZAN, Clarity AD,
  SPIN, plus Han Chinese cohorts Huashan and Greater Bay Area. See `data/dataset.md`.
- **How to use / run**: apply through the respective consortia/data-access committees.
- **Claims supported**: C01-C07 (data provenance).
