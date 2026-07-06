# Study Design

## Overview

An observational, multi-modal (spatial transcriptomics + immunohistochemistry + snRNA-seq
deconvolution + iPSC in vitro validation) case-control study of human dorsolateral prefrontal
cortex (DLPFC), designed to link Aβ-plaque and glial-reactivity neuropathology to spatially
resolved gene expression, then causally test cell-type contributions in vitro.

## Cohort and tissue

- **Source**: ROSMAP (Religious Orders Study and Memory and Aging Project) cohort, Rush
  Alzheimer's Disease Center, Rush University Medical Center.
- **Selection**: 21 individuals — 13 clinically diagnosed AD with high pathology, 8 controls with
  no cognitive impairment (NCI) and no/minimal pathology. All female (insufficient age-matched
  males meeting RIN>5 / minimal-freezing-artifact criteria), age-matched.
- **Tissue**: ~1 cm³ fresh-frozen right-hemisphere DLPFC blocks, cryosectioned at 10 µm (Leica
  CM1950, −17°C). Per individual, up to 4 sets of 3 sections were cut (10-50 µm spacing between
  sets): the middle section for Visium ST + H&E, and the two flanking sections for adjacent IHC.
- **Yield**: 78 ST sections total across 21 donors.

## Two independent IHC validation cohorts (distinct from the 21-donor ST cohort)

- **FFPE plaque-typing cohort**: 9 AD ROSMAP participants, 722 manually annotated plaques
  (diffuse/compact/dense-core), used to replicate the Aβ-intensity-to-plaque-type association
  (C05) found in the primary frozen cohort.
- **FFPE functional-validation cohort**: 10 AD individuals, stained across several marker panels
  (Aβ/GFAP/IBA1/cleaved-caspase-3/NeuN; Aβ/GFAP/IBA1/SYP/NeuN; Aβ/GFAP/IBA1/CD68) to validate
  apoptosis (C02), synaptic/neuronal loss, and neuroinflammation (C03) findings from the ST data.

## Plaque-glia niche stratification design

1. **Aβ stratification** (no/low/high) from adjacent-section 4G8/Aβ IHC intensity, thresholds
   calibrated on 781 manually scored plaques (see `logic/concepts.md` "Aβ intensity
   stratification").
2. **Glia stratification** (glia-high/glia-low) from adjacent-section GFAP/IBA1 intensity,
   thresholds calibrated by manual cell counting (glia-high ≈ >4 glial cells per spot; glia-low ≈
   0-4).
3. **Combined stratification**: Aβ × glia strata analyzed both independently (combined Aβ contrast
   regardless of glia; combined glia contrast regardless of Aβ) and jointly (Aβ contrast within
   each glia stratum; glia contrast within each Aβ stratum), plus an attempted finer 6-way
   (GFAP×IBA1×Aβ intensity level) stratification that proved underpowered except for one contrast
   (LHL vs. LLL).

## Analysis arms

1. **Spot clustering / cell-type mapping** — establishes tissue architecture (cortical layers,
   white matter, meninges, vasculature) and cell-type abundance per spot (cell2location), as
   context for niche analyses (not itself hypothesis-testing about plaque-glia niches).
2. **Aβ-load contrast arm** (pseudobulk DEG + GSEA + NICHES LR + IHC apoptosis validation) — tests
   whether/how Aβ load shapes the local transcriptome and signaling environment (C01, C02, C05,
   C06).
3. **Glia-abundance contrast arm** (pseudobulk DEG + GSEA + NICHES LR + IHC synaptic/CD68
   validation) — tests whether/how surrounding glial abundance shapes the local transcriptome and
   signaling environment (C03, C04, C07).
4. **In vitro causal-validation arm** (iPSC co-culture + Aβ-oligomer treatment + scRNA-seq +
   cross-GSEA) — tests which cell type(s) recapitulate the in vivo glial signature and which
   specific microglial substates are involved (C08, C09).

## Statistical framework

All niche-contrast differential-expression testing uses section-level pseudobulk aggregation
(summing spot UMI counts within a niche type per section) followed by TMM-voom normalization and
linear mixed models with donor as a random effect (to account for up to 4 sections per donor) and
age/RIN/batch/AD-status as fixed-effect covariates, with BH-FDR correction across genes and
contrasts (α=0.05). IHC validation experiments use NEBULA (count outcomes, e.g., caspase-3 or NeuN
counts, with a nuclei-count or area offset) or linear mixed models (continuous intensity outcomes,
e.g., SYP/CD68 average intensity), again with subject-level random effects for repeated ROIs, and
paired t-tests on per-individual condition averages for the summary comparisons shown in figures.

## Key design decisions (see `trace/exploration_tree.yaml` for full detail)

- IHC performed on two sections **adjacent** to (not the same as) the sequenced ST section, after
  same-section IHC on the RNA-preserving fixation protocol proved inadequate.
- Harmony selected as the data-integration method for spot clustering after benchmarking against 6
  alternatives (scANVI, fastMNN, ComBat, Seurat v3 RPCA, scVI, BBKNN) on a 16-section subsample;
  used **only** for clustering — all differential-expression, cell-proportion, and LR analyses use
  pre-integration (non-batch-corrected) counts.
- Louvain (not BayesSpace) retained for spot clustering despite BayesSpace's greater spatial
  contiguity, because BayesSpace failed to recover sporadically distributed clusters (Blood
  Vessel, Interneuron) that Louvain captured (99% concordance on gray-matter labels between the
  two methods).
- Glia-intensity thresholds kept at the reported values rather than stricter/single-positive-only
  criteria, because stricter thresholds reduced the number of sections usable for pseudobulk
  analysis and thus reduced DEG-detection power.
