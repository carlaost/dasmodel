# Concepts

## Selective neuronal vulnerability
- **Notation**: —
- **Definition**: The phenomenon whereby specific neuronal subtypes degenerate early and preferentially in a neurodegenerative disease while others are spared, despite residing in similar microenvironments. A hallmark of AD.
- **Boundary conditions**: Defined here at the level of transcriptomic clusters (Ex/In subtypes) within neocortical regions across Braak stages 0–VI.
- **Related concepts**: Resilience, Ex2 (vulnerable prototype), spatiotemporal AD progression.

## Resilience (neuronal)
- **Notation**: —
- **Definition**: The relative preservation of a neuronal population even in advanced disease. Operationalized here as a neuronal subtype whose *relative* proportion is maintained or increases with pathology (as neighbors are lost) and which upregulates putatively protective genes at early stages.
- **Boundary conditions**: Relative (compositional), not absolute cell-number preservation; inferred from cross-sectional postmortem cohorts, hence hypothesis-generating.
- **Related concepts**: Ex5, L4 IT, KCNIP4, compensatory response.

## Ex5 (resilient L4 IT excitatory subtype)
- **Notation**: Ex5 — full label "Ex5:RORB-CUX2-EYA4-LAMA3"
- **Definition**: An excitatory intratelencephalic (IT) neuron cluster of layer 4, co-expressing RORB, CUX2, EYA4, and LAMA3 (top markers also KCNH8, VAV3, KCNIP1, TRPC3), overrepresented in BA17 and rare in BA9. Identified as the prototype resilient population. Maps to Jorstad L4 IT_2/3/5/6 supertypes.
- **Boundary conditions**: BA17-enriched; deep layer 4c (matches VGLUT2+ thalamocortical terminals); likely comprises several finer molecular subtypes.
- **Related concepts**: Ex6 (RORB/MME), Ex7 (RORB/GABRG1), L4 IT, resilience.

## Ex2 (vulnerable L2/3 IT prototype)
- **Notation**: Ex2 — "Ex2:CUX2-RORB-GLIS3-LRRC2"
- **Definition**: An L2/3 IT excitatory cluster used as the prototype *vulnerable* neuron for contrastive DGE/hdWGCNA against resilient Ex5. L2/3 IT neurons are reported vulnerable in AD.
- **Boundary conditions**: Vulnerability trends were less robust in this cohort than in prior high-quality association-cortex datasets.
- **Related concepts**: Ex5, selective vulnerability, Ex3 (SV2C deep-L3, vulnerable).

## KCNIP4 (KChIP4 / CALP)
- **Notation**: KCNIP4 (gene); KChIP4/CALP (protein)
- **Definition**: A voltage-gated potassium-channel-interacting protein; an integral component of Kv4 channel complexes and a member of the recoverin branch of the EF-hand superfamily (four EF-hand calcium-binding motifs). Increased KChIP4 binding enhances Kv4.2 recovery from inactivation, exerting an inhibitory effect on neuronal excitability; also interacts with presenilins (modulating APP processing/Aβ).
- **Boundary conditions**: Regulates A-type outward potassium currents; effect depends on relative expression/stoichiometry with Kv4 subunits.
- **Related concepts**: Neuronal hyperexcitability, calcium homeostasis, resilience factor, KCNIP1-3.

## High-confidence DE gene
- **Notation**: —
- **Definition**: A differentially expressed gene identified by at least two methods — the linear mixed model (MAST/lme4) plus either bootstrap resampling, pseudobulk (pyDESeq2), or the top-50-by-kME genes from hdWGCNA co-expression network analysis. Designed to prioritize robust, reproducible signals over subtler donor-restricted changes.
- **Boundary conditions**: Conservative; biases toward higher-baseline-expression, larger-effect, more stable genes. Thresholds: |logFC|>0.1, FDR<0.05, expression>20% in ≥1 condition (LMM).
- **Related concepts**: MAST, bootstrap, pseudobulk, hdWGCNA module.

## hdWGCNA co-expression module
- **Notation**: M1, M2, … (per subtype/region), module eigengene kME
- **Definition**: A cluster of interconnected co-expressed genes computed by high-dimensional weighted gene co-expression network analysis on metacells, ranked internally by kME (module eigengene connectivity). "Candidate resilience modules" are those upregulated at early stages in resilient Ex5.
- **Boundary conditions**: Correlation-based; does not natively adjust for covariates (age, sex, APOE), so residual confounding may affect module/hub-gene composition.
- **Related concepts**: kME, hub gene, high-confidence DE gene.

## Braak / ABC neuropathological staging
- **Notation**: Braak 0–VI; ABC score; CERAD C0–C3
- **Definition**: Standardized neuropathological grading of AD change: Braak stages tau NFT distribution; the ABC score (NIA-AA framework) integrates amyloid (A), Braak (B), and CERAD neuritic-plaque (C) scores. Used to bin donors into low, intermediate, and high pathology groups.
- **Boundary conditions**: Low group includes PART (primary age-related tauopathy, Braak I–III, no amyloid); intermediate = Braak III–IV + diffuse/sparse (C1) plaques; high = Braak V–VI + moderate/abundant (C2/C3) plaques.
- **Related concepts**: Disease group (low/int/high), spatiotemporal AD progression.

## Spatiotemporal AD progression
- **Notation**: —
- **Definition**: The stereotyped anatomical spread of AD tau pathology/neurodegeneration from association cortices (BA9, BA7) to primary cortices (BA17), enabling a region×stage design where late resilient-region changes should mirror early vulnerable-region changes.
- **Boundary conditions**: Region cohorts only partially overlap (residual confounding); BA17 predominantly Drop-seq (platform bias).
- **Related concepts**: Braak staging, early/late DE comparison.

## FANS (fluorescence-activated nuclear sorting)
- **Notation**: NeuN+ / all-nuclei
- **Definition**: Flow-cytometric sorting of DAPI/Hoechst+ nuclei with anti-NeuN immunolabeling to enrich neuronal (NeuN+) nuclei prior to snRNA-seq; two suspensions collected per sample (all nuclei; NeuN+).
- **Boundary conditions**: Requires intact NeuN immunostaining; gating tuned with unstained/single-stained controls.
- **Related concepts**: snRNA-seq, Drop-seq, 10x Genomics.

## scCODA compositional analysis
- **Notation**: PIP (posterior inclusion probability); credible effect (PIP>0.95)
- **Definition**: A Bayesian Dirichlet-multinomial framework for compositional single-cell count data, run in automatic reference mode, modeling `cell type counts ~ Disease group + Sex + APOE genotype + Assay + Age`; effects called "credible" at PIP>0.95. A sign-constrained (β≤0) "loss-only" variant is used as a conservative stress test.
- **Boundary conditions**: Compositional (proportions sum to 1); reference cell type assumed invariant.
- **Related concepts**: GLMM (beta regression), relative abundance, resilience.

## Neuronal hyperexcitability
- **Notation**: —
- **Definition**: Excessive neuronal activity (up to subclinical epileptiform activity) that is an early feature of AD, reflecting excitatory/inhibitory imbalance; read out here via Ca2+ transient frequency (in vitro) and immediate-early genes c-Fos and Arc (in vivo).
- **Boundary conditions**: Can reflect maladaptive vulnerability or compensatory/neuroprotective adaptation depending on context.
- **Related concepts**: KCNIP4, c-Fos, Arc, Kv4 channels, excitotoxicity.
