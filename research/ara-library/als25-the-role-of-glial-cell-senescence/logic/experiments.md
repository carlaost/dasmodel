# Experiments (Verification / Analysis Plans)

*Grounding: full-text of a narrative review. This review presents no original experiments; the plans
below are declarative reconstructions of the study designs — reported in the cited primary
literature — that establish each claim. Directional only; exact numbers live in `evidence/`.*

## E01: Detect and quantify senescence markers in glial cells (human tissue + models)
- **Verifies**: C01, C05, C09
- **Setup**:
  - Samples: post-mortem human AD brain vs age-matched non-demented controls; AD mouse models (APP/PS1, 5xFAD, PS19, triple-transgenic); primary/cultured glia.
  - Cell types: astrocytes (GFAP+), microglia, OPCs, oligodendrocytes.
  - Assays: immunostaining / triple-label immunofluorescence, SA-β-gal histochemistry, single-cell / single-nuclei RNA sequencing.
- **Procedure**:
  1. Stain/measure senescence markers (SA-β-gal, p16INK4A, p21WAF1/CIP1, p53, γH2AX, Lamin B1, HMGB1, SASP factors) by glial cell type.
  2. Compare AD vs control tissue and old vs young models.
  3. Co-localize markers with pathology (TauO, Aβ plaques) and cell-type identity.
  4. Quantify fraction of a marker-positive glial population (e.g., GFAP+ astrocytes co-reactive for TauO and p16INK4A).
- **Metrics**: Marker-positive cell counts/percentages; marker intensity; transcript up/down-regulation; spatial co-localization with plaques/tangles.
- **Expected outcome**:
  - Senescence markers are elevated in AD/aged glia versus controls/young, across multiple cell types.
  - Marker presence differs by cell type (non-universal); some markers (HMGB1) restricted to fewer cell types.
- **Baselines**: Age-matched non-demented controls; young animals; non-senescent/quiescent glia.
- **Dependencies**: none

## E02: Transcriptomic mapping of brain aging across cell types and regions
- **Verifies**: C02
- **Setup**:
  - Cohort: large human sample spanning a wide age range across multiple brain regions.
  - Assay: bulk/region-level transcriptional profiling with cell-type deconvolution.
- **Procedure**:
  1. Profile gene expression across brain regions and ages.
  2. Attribute age-related differentially expressed genes to glial vs neuronal identity.
  3. Test which cell-type gene sets best predict chronological age; identify most-affected regions.
- **Metrics**: Number/fraction of age-associated DEGs by cell type; predictive accuracy of cell-type gene panels for age; per-region effect sizes.
- **Expected outcome**: Age-related expression change is concentrated in glia (astrocyte/microglia genes best predict aging); hippocampus and substantia nigra most affected.
- **Baselines**: Neuronal gene sets; younger age strata.
- **Dependencies**: none

## E03: Induce glial senescence with Aβ or tau in vitro / in models
- **Verifies**: C03
- **Setup**:
  - Cells: primary human/rodent astrocytes, primary microglia, OPCs, neural stem/progenitor cells.
  - Stimuli: oligomeric Aβ; recombinant human tau / pathological tau; oxidative and other stressors.
- **Procedure**:
  1. Expose glia to Aβ oligomers or tau.
  2. Measure induction of senescence markers (p16INK4A, p21, p53, SA-β-gal, γH2AX, Lamin B1) and SASP factor secretion (IL-1β, IL-6, TNF-α, CXCL-1).
  3. Assess proliferation (Ki-67) and neurotrophic factor expression (IGF-1, NGF).
  4. Probe signaling (e.g., ROS-MAPK / p38 MAPK) mediating induction.
- **Metrics**: Marker induction (up/down direction), SASP cytokine levels, Ki-67 decrease, DNA-damage foci counts.
- **Expected outcome**: Aβ and tau induce senescence markers and SASP and reduce proliferation/neurotrophic support across glial cell types.
- **Baselines**: Vehicle/untreated glia; scrambled/monomeric protein controls.
- **Dependencies**: E01

## E04: Assess functional consequences of glial senescence (phagocytosis, neurotoxicity)
- **Verifies**: C04
- **Setup**:
  - Cells: senescent vs non-senescent astrocytes/microglia; co-cultures with hippocampal neurons.
  - Assays: Aβ/debris phagocytosis or endocytosis assays; co-culture neuronal viability; glutamate/vesicle assays; receptor expression (LRP1, SR-B1); irradiation-induced senescence models.
- **Procedure**:
  1. Compare phagocytic/endocytic clearance of Aβ and debris by senescent vs control glia.
  2. Co-culture senescent glia with neurons; measure neuronal survival, synaptic vesicle pool, glutamate handling.
  3. Quantify pro-inflammatory vs neurotrophic factor release and Aβ-uptake receptor levels.
- **Metrics**: Phagocytosis rate, neuronal death, synaptic vesicle count, glutamate uptake/excitotoxicity, LRP1/SR-B1 expression, cytokine vs neurotrophin levels.
- **Expected outcome**: Senescent glia clear less Aβ/debris, support neurons less, and are neurotoxic (excitotoxicity, reduced neurotrophins) relative to non-senescent controls.
- **Baselines**: Non-senescent glia; neuron-only cultures.
- **Dependencies**: E01, E03

## E05: Test senescent-cell clearance / senotherapeutics (models and humans)
- **Verifies**: C07, C08
- **Setup**:
  - Preclinical: AD/tauopathy mouse models (APP/PS1, PS19, INK-ATTAC×PS19, very-old tauopathy, TBI model); genetic (INK-ATTAC/AP20187) or pharmacological senolytics (D+Q, ABT-263/Navitoclax, Fisetin) and senomorphics (rapamycin/PQR530, resveratrol, apigenin, adalimumab, SGB121).
  - Clinical: phase I trial (Hickson 2019); symptomatic early-AD older adults (Gonzales 2023).
- **Procedure**:
  1. Administer senolytic/genetic clearance or senomorphic treatment.
  2. Measure senescent-cell burden (p16INK4A+ cells, SA-β-gal), SASP factors, Aβ and tau pathology, neuroinflammation, neurodegeneration/atrophy.
  3. Assess cognition/behavior (Y-maze, water maze) in animals; cognition, structural MRI, and CSF/plasma biomarkers in humans.
  4. In humans, test BBB penetration (plasma vs CSF drug levels).
- **Metrics**: Senescent-cell counts, SASP cytokine/chemokine levels (e.g., MMP-12, IL-6, MMP-9), Aβ/tau load, cognitive scores, MRI measures, drug CSF/plasma levels.
- **Expected outcome**:
  - Animals: clearance reduces Aβ/tau pathology, neuroinflammation, and neurodegeneration and improves cognition.
  - Humans: D+Q lowers SASP factors and reaches CSF (target engagement), but does not yet improve cognition/structural MRI in short trials.
- **Baselines**: Vehicle-treated models; pre-treatment/placebo human measures.
- **Dependencies**: E01, E03, E04

## E06: Block microglial proliferation to test replicative-senescence mechanism
- **Verifies**: C06
- **Setup**:
  - Model: APP/PS1 mice with pharmacological inhibition of microglial proliferation; single-cell transcriptomics of microglia in old vs young mice.
- **Procedure**:
  1. Pharmacologically inhibit microglial proliferation after Aβ-plaque onset.
  2. Measure DAM appearance, microglial senescence markers (SA-β-gal, telomere length, senescence signature genes), Aβ-dependent synaptic damage, and cognition.
  3. Compare DAM/senescence enrichment in old vs young mice via single-cell transcriptomics.
- **Metrics**: DAM cluster presence, senescence marker levels, telomere length, synaptic-damage measures, cognitive scores.
- **Expected outcome**: Inhibiting proliferation prevents DAM, reduces microglial senescence, mitigates synaptic damage, and improves cognition — supporting a replicative-senescence mechanism.
- **Baselines**: Untreated APP/PS1 mice; young mice.
- **Dependencies**: E01
