# Experiments (Verification / Analysis Plans)

*Grounding: full-text of a narrative review. This review presents no original experiments; the plans
below are declarative reconstructions of the study designs — reported in the cited primary
literature — that establish each claim. Directional only; exact numbers live in `evidence/`.*

## E01: Characterize APOE4-driven microglial lipid metabolic reprogramming and LD formation
- **Verifies**: C01
- **Setup**:
  - Cells: APOE-targeted-replacement or isogenic-iPSC-derived microglia (APOE4 vs APOE3/APOE2), with and without Aβ stimulation.
  - Assays: lipid-droplet imaging (BODIPY/oil-red-O), triglyceride/free-fatty-acid quantification, ATAC-seq/RNA-seq for enhancer/gene-expression profiling, mitochondrial β-oxidation assays, autophagy/lipophagy flux assays.
- **Procedure**:
  1. Compare LD number/size and triglyceride vs free-fatty-acid ratio between APOE4 and APOE3/2 microglia.
  2. Quantify fatty-acid-synthesis (FAS) gene expression (e.g., ACSL1, PLIN2) vs fatty-acid-oxidation (FAO) gene expression.
  3. Profile enhancer occupancy for PU.1 and NF-κB in LD-rich APOE4 microglia via ATAC-seq/RNA-seq.
  4. Assess mitochondrial structure/function and β-oxidation capacity.
- **Metrics**: LD count/size, triglyceride:FFA ratio, FAS/FAO gene expression fold-change, PU.1/NF-κB enhancer enrichment, β-oxidation rate.
- **Expected outcome**: APOE4 microglia show elevated LD accumulation, upregulated FAS genes, suppressed FAO/lipophagy, and PU.1/NF-κB enrichment at LD-associated enhancers, consistent with an "enhanced synthesis–suppressed degradation" imbalance.
- **Baselines**: APOE3 (and/or APOE2) isogenic microglia; unstimulated (no Aβ) controls.
- **Dependencies**: none

## E02: Test the ER stress–SREBP2 cholesterol pathway and cholesterol-efflux impairment in APOE4 microglia
- **Verifies**: C02
- **Setup**:
  - Cells: APOE4 vs APOE3 microglia (iPSC-derived or targeted-replacement).
  - Assays: ER-Ca2+ imaging, SREBP2 transcriptional-activity reporter, HMGCR/SQLE expression, ABCA1 recycling/cholesterol-efflux assays, Aβ-degradation assays.
- **Procedure**:
  1. Measure ER Ca2+ levels and SREBP2 nuclear translocation/activity in APOE4 vs APOE3 microglia.
  2. Quantify HMGCR and SQLE transcript levels (cholesterol biosynthesis).
  3. Assess ABCA1 membrane recycling and cholesterol efflux capacity.
  4. Measure intracellular cholesterol accumulation and downstream Aβ-degradation capacity (lysosomal Aβ turnover assay).
  5. Test rescue with LXR agonists, ABCA1 overexpression, or TRPV1 activation.
- **Metrics**: ER Ca2+ level, SREBP2 activity, HMGCR/SQLE expression, cholesterol efflux rate, intracellular cholesterol level, Aβ-degradation rate.
- **Expected outcome**: APOE4 microglia show ER stress, SREBP2 activation, elevated HMGCR/SQLE, impaired ABCA1-dependent efflux, cholesterol accumulation, and reduced Aβ-degradation capacity; pharmacological efflux enhancers reverse the phenotype.
- **Baselines**: APOE3 microglia; vehicle-treated APOE4 microglia (for rescue experiments).
- **Dependencies**: E01

## E03: Test direct receptor-mediated and cell-intrinsic inflammatory activation of APOE4 microglia
- **Verifies**: C03
- **Setup**:
  - Cells: APOE4 vs APOE3 microglia; LilrB3 knockdown/knockout lines; Cxorf56 knockdown.
  - Stimuli: recombinant APOE4 (including nAPOE4(1-151) fragment); LPS; IFN-γ.
- **Procedure**:
  1. Expose microglia to APOE4; measure LilrB3 binding and downstream interferon-stimulated gene induction (IFITM3, BST2, MX1, ISG15, STAT1) with/without LilrB3 knockdown.
  2. Measure basal NLRP3 inflammasome activation and ROS production in APOE4 vs APOE3 microglia.
  3. Apply LPS/IFN-γ and measure TNF-α, IL-1β, NOS2, MCP1 secretion, stratified by sex.
  4. Test nAPOE4(1-151) fragment effect on Cxorf56 expression and TNF-α induction, with/without Cxorf56 knockdown rescue.
- **Metrics**: ISG expression fold-change, NLRP3/ROS levels, cytokine secretion (TNF-α, IL-1β, NOS2, MCP1), Cxorf56 expression.
- **Expected outcome**: APOE4-LilrB3 binding induces ISGs (blocked by LilrB3 knockdown); APOE4 microglia show elevated basal and LPS/IFN-γ-induced NLRP3/ROS/cytokines (more pronounced in females); nAPOE4(1-151) suppresses Cxorf56, elevating TNF-α (reversed by Cxorf56 restoration).
- **Baselines**: APOE3 microglia; unstimulated controls; LilrB3/Cxorf56 wild-type controls.
- **Dependencies**: none

## E04: Test lipid-metabolic amplification of neuroinflammation
- **Verifies**: C04
- **Setup**:
  - Cells: APOE4 microglia with pharmacological/genetic manipulation of glycolysis (e.g., HK2), TCA cycle, and NF-κB signaling.
  - Assays: metabolic flux analysis (Seahorse-type glycolysis/OXPHOS), lipid mediator quantification (prostaglandins, arachidonic-acid metabolites), NF-κB reporter assay, MHC-II antigen-presentation/T-cell-activation co-culture, 25-HC and IL-1β secretion assay.
- **Procedure**:
  1. Measure glycolytic flux and TCA-cycle activity in APOE4 vs APOE3 microglia.
  2. Quantify proinflammatory lipid mediator release and correlate with NF-κB activation.
  3. Assess MHC-II expression and co-culture with T cells to measure activation.
  4. Measure 25-HC and IL-1β secretion following LPS, with and without exogenous 25-HC.
- **Metrics**: Glycolysis/TCA flux ratio, lipid mediator levels, NF-κB reporter activity, MHC-II expression, T-cell activation markers, 25-HC/IL-1β levels.
- **Expected outcome**: APOE4 microglia show a glycolysis-dominant metabolic shift, elevated lipid mediators and NF-κB activity, enhanced MHC-II-driven T-cell activation, and a 25-HC → IL-1β amplification loop.
- **Baselines**: APOE3 microglia; non-stimulated controls.
- **Dependencies**: E01, E03

## E05: Assess microglial Aβ-phagocytosis capacity under APOE4 and pathway-specific manipulation
- **Verifies**: C05
- **Setup**:
  - Cells/models: APOE4 microglia (in vitro and mouse models); microglia-specific APOE4 ablation; ITGB8-TGFβ pathway blockade; IL-17F/IL-17RA blockade; female vs male AD models/patients.
  - Assays: Aβ-phagocytosis/uptake assay, TREM2 expression, mitochondrial function assay, membrane-fluidity/pseudopod-extension imaging, plaque-burden quantification.
- **Procedure**:
  1. Compare Aβ-uptake rate, TREM2 expression, mitochondrial function, and pseudopod extension between APOE4 and APOE3 microglia.
  2. Selectively ablate microglial APOE4 in vivo; measure phagocytic function and plaque burden.
  3. Block ITGB8-TGFβ signaling; measure Aβ42-specific clearance.
  4. In female APOEε4 carriers, measure neutrophil IL-17F and microglial IL-17RA interaction; block the pathway and measure cognition/Aβ deposition.
- **Metrics**: Aβ-uptake rate, TREM2 expression, mitochondrial function, plaque burden, Aβ42 clearance rate, cognitive-task performance.
- **Expected outcome**: APOE4 microglia show reduced Aβ uptake, TREM2, and mitochondrial function; microglial APOE4 ablation and ITGB8-TGFβ/IL-17F-IL-17RA blockade restore phagocytosis and reduce plaque burden/cognitive deficits.
- **Baselines**: APOE3 microglia; non-ablated/non-blocked APOE4 controls; male comparator groups (for sex-dependent effects).
- **Dependencies**: E01, E03

## E06: Assess tau/synapse clearance and propagation under APOE4-driven lysosomal dysfunction
- **Verifies**: C06
- **Setup**:
  - Cells/tissue: APOE4 microglia (in vitro, mouse models, and post-mortem AD tissue from APOEε4 carriers vs non-carriers).
  - Assays: lysosomal function assay, intracellular p-tau quantification, exosome isolation/tau content assay, synaptic-phagocytosis imaging (near vs distant from Aβ plaques).
- **Procedure**:
  1. Measure endosomal-lysosomal function and intracellular p-tau accumulation in APOE4 vs APOE3 microglia.
  2. Isolate exosomes and quantify tau content/release rate.
  3. Quantify microglial synaptic phagocytosis in APOEε4-carrier vs non-carrier AD tissue, stratified by plaque proximity.
- **Metrics**: Lysosomal function score, intracellular p-tau level, exosomal tau content, synaptic-phagocytosis rate.
- **Expected outcome**: APOE4 microglia show lysosomal dysfunction, p-tau accumulation, increased exosomal tau release, and increased plaque-proximal synaptic phagocytosis correlating with cognitive decline.
- **Baselines**: APOE3 microglia/tissue; non-carrier AD tissue; plaque-distant regions.
- **Dependencies**: E01, E05

## E07: Characterize APOE4 astrocyte lipid dysregulation and GPC-4/LRP1-mediated tau propagation
- **Verifies**: C07
- **Setup**:
  - Cells: APOE4 vs APOE3 iPSC-derived or isogenic astrocytes.
  - Assays: SREBP2/PPARγ expression, cholesterol synthesis/accumulation assay, mitophagy assay, lipid-droplet composition analysis, GPC-4/LRP1 expression, tau-propagation/hyperphosphorylation assay, miRNA-transfer assay to co-cultured neurons.
- **Procedure**:
  1. Measure SREBP2 activity, PPARγ expression, and de novo cholesterol synthesis in APOE4 vs APOE3 astrocytes.
  2. Assess lysosome-dependent mitophagy and mitochondrial function.
  3. Characterize LD size/composition and lipoprotein lipidation status secreted to neurons.
  4. Measure GPC-4 and LRP1 membrane trafficking, and downstream tau hyperphosphorylation in co-cultured neurons.
  5. Assess APOE4-mediated miRNA transfer efficiency to neurons.
- **Metrics**: SREBP2/PPARγ expression, cholesterol level, mitophagy flux, LD size, lipoprotein lipidation, GPC-4/LRP1 expression, tau phosphorylation level, miRNA transfer efficiency.
- **Expected outcome**: APOE4 astrocytes show SREBP2 activation, PPARγ suppression, cholesterol accumulation, impaired mitophagy, enlarged oxidation-prone LDs, poorly lipidated lipoprotein secretion, elevated GPC-4/LRP1 driving neuronal tau hyperphosphorylation, and impaired miRNA transfer.
- **Baselines**: APOE3 astrocytes; non-co-cultured neurons.
- **Dependencies**: none

## E08: Characterize APOE4 neuronal lipid dysregulation, lysosomal dysfunction, and tau aggregation
- **Verifies**: C08
- **Setup**:
  - Cells: APOE4 vs APOE3 iPSC-derived or isogenic neurons; co-cultured astrocytes.
  - Assays: LDLR-binding/lipid-uptake assay, lysosomal function assay, lipofuscin quantification, autophagy flux, free-fatty-acid quantification, ABCA1 expression, mTORC1 activity, senescence markers, tau-aggregation assay, proteolytic-fragment detection.
- **Procedure**:
  1. Measure APOE4-LDLR binding and neuronal lipid uptake.
  2. Assess lysosomal function, lipofuscin accumulation, and autophagy flux.
  3. Quantify free-fatty-acid accumulation from deficient LD storage; assess neighboring-astrocyte lipid transport/oxidation (hippocampus-focused).
  4. Measure ABCA1 degradation, cholesterol efflux, mTORC1 activity, and senescence markers.
  5. Detect neuron-specific APOE4 proteolytic fragments and downstream tau aggregation/cell death.
- **Metrics**: Lipid uptake rate, lysosomal function score, lipofuscin level, free-fatty-acid level, ABCA1 expression, mTORC1 activity, senescence-marker expression, tau-aggregate level, proteolytic-fragment abundance.
- **Expected outcome**: APOE4 neurons show excess lipid uptake, lysosomal dysfunction, lipofuscin/lipotoxic FFA accumulation, reduced ABCA1/cholesterol efflux, mTORC1-driven senescence, and proteolysis-linked tau aggregation and cell death.
- **Baselines**: APOE3 neurons; APOE4-R136S mutant comparator (partial protection).
- **Dependencies**: none

## E09: Single-cell/transcriptomic profiling of APOE4-associated microglial subtypes
- **Verifies**: C09
- **Setup**:
  - Tissue/models: single-cell/single-nucleus RNA-seq of microglia from APOE4 AD mouse models and human post-mortem AD tissue.
  - Assays: clustering/subtype classification (LDAM, DAM, MGnD, TIM), APOE-TREM2-TYROBP and ITGB8-TGFβ pathway activity, Aβ-uptake/glycolysis functional assays per subtype.
- **Procedure**:
  1. Cluster microglia transcriptionally and annotate subtypes by marker genes.
  2. Correlate subtype abundance with APOE genotype (APOE4 vs APOE3) and plaque proximity.
  3. Measure per-subtype functional readouts (glycolysis, Hif1a expression, Aβ uptake, apoptotic-neuron clearance for MGnD).
  4. Test ITGB8-TGFβ pathway activation and its effect on MGnD-function suppression.
- **Metrics**: Subtype proportion, marker-gene expression, glycolysis/Hif1a level, Aβ-uptake rate, apoptotic-neuron clearance rate.
- **Expected outcome**: APOE4 genotype is associated with increased LDAM/DAM/TIM proportions and altered MGnD function via ITGB8-TGFβ, each subtype showing the functional signature described (impaired phagocytosis for LDAM/TIM, glycolytic/impaired-Aβ-uptake for DAM, suppressed neuroprotection for MGnD).
- **Baselines**: APOE3 tissue/models; plaque-distant microglia.
- **Dependencies**: E01

## E10: Compare TREM2-R47H microglial lipid-droplet phenotype in vivo vs in vitro
- **Verifies**: C10
- **Setup**:
  - Models: chimeric AD mouse model with human iPSC-derived microglia (TREM2-R47H vs wild-type), in vivo; parallel isolated in vitro TREM2-R47H microglial cultures.
- **Procedure**:
  1. Measure LD accumulation, plaque reactivity, and plaque-associated APOE secretion in TREM2-R47H vs wild-type microglia in the chimeric in vivo model.
  2. Measure the same endpoints in isolated in vitro TREM2-R47H microglial cultures under matched Aβ exposure.
  3. Compare directionality of the TREM2-R47H effect between contexts.
- **Metrics**: LD count/size, plaque-reactivity score, plaque-associated APOE secretion level.
- **Expected outcome**: TREM2-R47H reduces LD accumulation, plaque reactivity, and APOE secretion in vivo, but increases LD accumulation in vitro — an opposite-direction, context-dependent effect.
- **Baselines**: Wild-type TREM2 microglia in each context (in vivo and in vitro).
- **Dependencies**: E01

## E11: Test HK2 inhibition as a microglia-specific glycolysis–lipid metabolic compensatory mechanism
- **Verifies**: C11
- **Setup**:
  - Cells: APOE4 microglia vs other CNS cell types (astrocytes, neurons) in AD models; pharmacological HK2 inhibitor.
- **Procedure**:
  1. Measure HK2 expression in microglia vs other brain cell types in AD models.
  2. Pharmacologically inhibit HK2 in microglia; measure lipoprotein lipase activation, lipid metabolism, ATP production, and Aβ clearance.
  3. Repeat HK2 inhibition in astrocytes/neurons to test cell-type specificity.
- **Metrics**: HK2 expression, lipoprotein lipase activity, ATP level, Aβ-clearance rate, per-cell-type comparison.
- **Expected outcome**: HK2 is upregulated in AD microglia; its pharmacological inhibition activates lipoprotein lipase, increases lipid metabolism, sustains ATP production, and promotes Aβ clearance specifically in microglia, with no equivalent coupling observed in other brain cell types.
- **Baselines**: Untreated microglia; astrocytes/neurons under the same HK2 inhibition protocol.
- **Dependencies**: none

## E12: Epidemiological/genetic association of APOEε4 dose with AD risk and population carrier frequency
- **Verifies**: C12
- **Setup**:
  - Cohorts: large population-based and case-control genetic-epidemiology studies of APOE genotype and AD diagnosis, stratified by allele dose (0, 1, or 2 ε4 alleles).
- **Procedure**:
  1. Genotype APOE in AD cases and controls (or population-representative cohorts).
  2. Compute AD risk (odds ratio/relative risk) by APOEε4 allele dose.
  3. Compute population carrier frequency for each APOE genotype combination.
- **Metrics**: Odds ratio/relative risk by allele dose, genotype carrier frequency.
- **Expected outcome**: A dose-dependent risk gradient (heterozygotes ~3-4× risk; homozygotes ~9-15× risk) and a population carrier rate around 23.9% for any ε4 allele.
- **Baselines**: APOEε3/ε3 non-carriers.
- **Dependencies**: none

## E13: Evaluate preclinical and clinical efficacy of APOE4-microglial-pathway-targeted therapeutics
- **Verifies**: C13
- **Setup**:
  - Models/trials: mouse AD models and cell-based assays for each of the 14 agents in Table 1 (lipid metabolism, neuro-inflammation, phagocytosis, and APOE4-targeting classes); phase I/II clinical trials for bexarotene (NCT01782742), AL002c (NCT03635047, NCT04592874), and LX1001 (NCT03634007, NCT05400330).
- **Procedure**:
  1. For each preclinical agent, measure target-pathway engagement (e.g., cholesterol efflux, NLRP3 activity, phagocytic receptor expression, APOE-Aβ interaction) and downstream pathology/cognition readouts.
  2. For clinical-trial agents, assess safety, target engagement/biomarker change, and (where reported) cognitive or imaging endpoints.
  3. Assess whether any agent specifically corrects the microglial-lipid-metabolism axis (versus broader neuroinflammation, phagocytosis, or general APOE4 reduction).
- **Metrics**: Target-pathway engagement magnitude, Aβ/tau pathology change, cognitive-task performance, clinical biomarker/safety/efficacy endpoints.
- **Expected outcome**: Multiple agents show preclinical pathway engagement and pathology/cognitive improvement; early-phase human trials show safety and target engagement/biomarker change, but no agent yet demonstrates disease-modifying efficacy specifically attributable to correcting microglial APOE4-driven lipid metabolism.
- **Baselines**: Vehicle-treated/placebo controls in each model or trial.
- **Dependencies**: E01, E02, E05
