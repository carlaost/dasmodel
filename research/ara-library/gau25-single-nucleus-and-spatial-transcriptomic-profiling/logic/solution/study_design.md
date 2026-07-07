# Study Design

## Cohort and tissue

- **Source**: Netherlands Brain Bank (NBB, Amsterdam), approved by the local medical ethics
  committee of VUmc (registration 2009.148); donors provided informed consent for autopsy, tissue
  storage, and use of anonymized clinical/neuropathological data.
- **Primary TC cohort**: 40 individuals, comprising healthy controls and individuals across varying
  Braak stages (1-6), sampled from the middle third of the mid-temporal gyrus of the right
  hemisphere.
- **Paired GM/WM sampling**: Each donor contributed two 10 µm cryosections — one from the temporal
  cortex gray matter (GM) and one from the associated subcortical white matter (WM), separated with
  a razor blade after cryosectioning — yielding 80 total samples (40 individuals x 2 tissue
  compartments).
- **QC exclusions**: Two samples from one individual were excluded from the TC snRNA-seq dataset
  for low quality; samples AD001 and AD002 were separately excluded from all trait-association and
  differential-expression analyses for not meeting QC criteria; all non-AD-dementia samples were
  removed specifically from the proportion-change (trait-association) analysis of AD pathology.
- **Statistical-analysis sample counts** (varying slightly per analysis due to per-analysis QC/
  metadata-completeness filtering): trait association Fig. 2a-d used GM+WM samples from n=36
  individuals; pseudobulk differential expression (Fig. 3d, f-h) used GM+WM samples from n=39
  individuals; CARTANA validation (Fig. 4c) used GM+WM samples from n=11 individuals; the CARTANA
  in-situ sequencing arm overall covered 13 tissue samples.

## Cross-region / cross-cohort integration cohorts

- **Multi-region integration**: 6 previously published studies (entorhinal cortex, prefrontal
  cortex x3, superior frontal gyrus, deep PFC white matter) totaling 888,784 nuclei after doublet
  removal from an initial 959,237-nuclei merge; a further metadata-completeness filter (removing
  cells lacking PMI/age/sex/Braak-stage data, and excluding the Grubman et al. study for
  demographic-detail variation) yielded 835,413 nuclei from 216 samples for the multi-region
  trait-association analysis.
- **SEA-AD MTG replication cohort**: 84 individuals, middle temporal gyrus, Seattle Alzheimer's
  Disease Brain Cell Atlas consortium (Gabitto et al. 2024).
- **ROSMAP PFC replication cohort**: 424 individuals, prefrontal cortex (Green et al. 2024).

## CARTANA spatial validation cohort

- **Samples**: 13 tissue sections from among the study's own NBB donors, spanning control through
  Braak stage 6, selected to represent differing degrees of tau pathology.
- **Panel**: 155 genes, selected to identify all 8 major cell classes plus a combinatorial marker
  set for the snRNA-seq-derived subclusters (with probe-design-constrained substitutions for
  several subclusters).
- **Co-registered pathology**: The same tissue sections were subsequently immunostained (after ISS
  probe removal) for β-amyloid (MOAB-2) and phosphorylated tau (Ser202/Thr205), enabling joint
  spatial localization of gene expression and pathology within a single section.

## Statistical framework

- **Cluster-proportion (trait association)**: ANCOM-BC (log-linear model), two-sided Z-tests,
  Benjamini-Hochberg-adjusted p-values; Braak stage (or diagnosis) as the primary covariate of
  interest, sex/age-of-death/PMI regressed out.
- **Pseudobulk differential expression**: glmmTMB negative-binomial mixed models per cell type,
  with an explicit Braak-stage x tissue (GM/WM) interaction term; two-sided Wald tests,
  Benjamini-Hochberg-adjusted p-values; log-TMM-normalized library size as model offset.
- **Gene constraint**: two-sided Wilcoxon rank-sum tests (uncorrected) comparing LOEUF scores
  between DE and non-DE gene sets.
- **Pathway enrichment**: MAGMA gene-level GWAS association + fgsea gene-set enrichment testing,
  Benjamini-Hochberg-adjusted, reported at 10-20% FDR depending on panel.
- **CARTANA marker validation and spatial-proximity models**: lmerTest linear mixed-effects models
  (gene expression ~ Braak-stage-category or distance-bin + (1|individual)); two-sided tests, no
  multiple-testing correction applied at the individual-gene level within a cell type/tissue.
- **Global/tile-based CARTANA signatures**: Wilcoxon rank-sum tests (Braak-stage and low/high-
  pathology comparisons; paired for the tile-based plaque-vs-no-plaque comparison),
  Benjamini-Hochberg-adjusted.
- **Distribution-shape diagnostic**: Hartigan's dip statistic (with prior kernel-density-estimation-
  based threshold identification) applied specifically to the GFAP plaque-distance-binned
  expression distribution.

## Braak-stage categorization (used throughout)

- Braak stage 0-1 ("early/none"), 2-4 ("intermediate"), 5-6 ("late/advanced") — three discrete bins
  derived from the continuous 1-6 Braak staging scale, used consistently across the ANCOM-BC,
  glmmTMB, and lmerTest models.
