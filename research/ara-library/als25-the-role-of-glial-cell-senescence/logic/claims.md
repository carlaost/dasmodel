# Claims

*Grounding: full-text. This is a narrative review; the claims below are the review's synthesized
assertions. Each is supported by primary studies the review cites (not original experiments by these
authors). `Proof` points to the verification plans in `experiments.md` that describe the study
designs establishing the claim. Numbers are copied verbatim from the review text; each load-bearing
number carries a `**Sources**` entry with the matched line.*

## C01: Glial cells undergo cellular senescence in the aging and AD brain
- **Statement**: Astrocytes, microglia, and oligodendrocytes/OPCs undergo cellular senescence, marked by shared hallmarks — elevated SA-β-gal activity, increased p16INK4A, p21WAF1/CIP1, and p53, γH2AX foci / DNA damage, loss of Lamin B1, and SASP secretion — in both normal aging and AD/pathology-induced contexts.
- **Status**: supported
- **Falsification criteria**: Demonstration that senescence markers in glia are artifacts of activation/quiescence with no bona fide senescence program, or absence of these markers in carefully controlled AD tissue.
- **Proof**: [E01]
- **Evidence basis**: Tables 1 and 2 catalogue these markers by glial cell type in age-related and pathology-induced senescence, each with citations. Senescent cells reported in post-mortem AD brain and mouse models (§1.1).
- **Interpretation**: The review treats the convergence of shared markers across cell types and contexts as strong evidence for a real, cross-glial senescence program in AD.
- **Dependencies**: none
- **Tags**: senescence-markers, astrocytes, microglia, oligodendrocytes, SASP

## C02: Most age-related brain gene-expression change occurs in glia, not neurons
- **Statement**: In a transcriptional analysis of 480 individuals aged 16–106 years across human brain regions, most age-related gene expression differences were observed in glial cells rather than neurons, and dysregulation of astrocyte- and microglia-specific genes was the best predictor of aging.
- **Status**: supported
- **Falsification criteria**: A comparably powered transcriptomic study finding age-related change concentrated in neurons rather than glia.
- **Proof**: [E02]
- **Evidence basis**: §1.2, Soreq et al. 2017.
- **Interpretation**: Motivates the review's glia-centric (vs neuron-centric) framing of brain aging and AD.
- **Dependencies**: none
- **Tags**: transcriptomics, aging, glia, hippocampus, substantia-nigra
- **Sources**: "480 individuals aged 16–106 years" ← §1.2 «conducted on 480 individuals aged 16–106 years, revealed that most age-related gene expression differences were observed in glial cells rather than neurons (Soreq et al. 2017)» [result]

## C03: Aβ and tau directly induce glial senescence
- **Statement**: Amyloid-β oligomers and pathological tau directly induce senescence in glia in vitro and in AD models — inducing p16INK4A, SA-β-gal activity, and SASP factors (e.g., IL-1β, IL-6, TNF-α, CXCL-1), DNA damage (γH2AX), and loss of Lamin B1 — in astrocytes, microglia, and OPCs.
- **Status**: supported
- **Falsification criteria**: Controlled Aβ/tau exposure failing to induce senescence markers across glial cell types.
- **Proof**: [E03]
- **Evidence basis**: Aβ oligomers induce p16INK4A and SA-β-gal in neural stem/progenitor cells via ROS-MAPK (He 2013); oligomeric Aβ raises p53/p21/p16, SA-β-gal, decreases Ki-67 in primary human astrocytes (Ungerleider 2022); recombinant tau raises p16/p21 and IL-1β/IL-6/TNF-α, lowers Lamin B1 in primary microglia (Karabag 2023); Aβ triggers SA-β-gal in OPCs (Zhang 2019). Tables 2.
- **Interpretation**: Establishes AD proteinopathy as an upstream cause (not just consequence) of glial senescence.
- **Dependencies**: C01
- **Tags**: amyloid-beta, tau, senescence-induction, SASP, in-vitro

## C04: Senescent glia lose phagocytic/supportive function and are neurotoxic
- **Statement**: Senescent astrocytes and microglia exhibit reduced phagocytic clearance of Aβ and cellular debris and exert neurotoxicity; senescent astrocytes reduce synaptic vesicle pools, induce glutamate excitotoxicity, and decrease neurotrophic factor (IGF-1, NGF) release, while aged astrocytes reduce Aβ-uptake receptors LRP1 and SR-B1.
- **Status**: supported
- **Falsification criteria**: Senescent glia showing preserved or enhanced phagocytosis and neurotrophic support relative to non-senescent controls.
- **Proof**: [E04]
- **Evidence basis**: Reduced LRP1/SR-B1 in aged astrocytes (Iram 2016); senescent astrocytes reduce synaptic vesicle pool (Kawano 2012) and increase pro-inflammatory / decrease neurotrophic release (Turnquist 2016); glutamate excitotoxicity and neuronal death in co-culture (Limbad 2020); reduced microglial phagocytosis (Fancy 2024; Karabag 2023; Hellwig 2015). Tables 2 ("↓ phagocytosis", "↓ Aβ endocytosis").
- **Interpretation**: Loss of function plus toxic gain of function is the mechanistic bridge from senescence to neurodegeneration.
- **Dependencies**: C01
- **Tags**: phagocytosis, neurotoxicity, glutamate, LRP1, SR-B1, neurotrophic-factors

## C05: More than 75% of GFAP-positive astrocytes in AD are TauO- and p16INK4A-reactive
- **Statement**: In triple-label immunostaining of AD frontal cortex, more than 75% of GFAP-positive astrocytes exhibited reactivity to both tau oligomers (TauO) and p16INK4A, with significantly fewer TauO- and p16INK4A-positive astrocytes in age-matched non-demented controls; TauO-associated astrocytes in AD also showed elevated HMGB1 and increased γH2AX foci.
- **Status**: supported
- **Falsification criteria**: Independent quantification finding no enrichment of p16INK4A/TauO co-reactivity in AD astrocytes versus controls.
- **Proof**: [E01]
- **Evidence basis**: §1.2.1, Gaikwad et al. 2021.
- **Interpretation**: Provides a quantitative human-tissue anchor linking astrocyte senescence to tau pathology.
- **Dependencies**: C01, C03
- **Tags**: astrocytes, tau-oligomers, p16INK4A, HMGB1, human-tissue
- **Sources**: "more than 75% of GFAP-positive astrocytes" ← §1.2.1 «it was found that more than 75% of GFAP-positive astrocytes in ad exhibited reactivity to both tau oligomers (TauO) and p16INK4A» [result]

## C06: Microglia undergo replicative senescence secondary to pathology-driven proliferation
- **Statement**: In AD, rapid microglial proliferation following Aβ plaque appearance leads to replicative senescence (increased SA-β-gal, telomere shortening, senescence signature genes, DAM markers); pharmacological inhibition of microglial proliferation prevents DAM appearance, reduces microglial senescence, mitigates Aβ-dependent synaptic damage, and improves cognitive deficits in APP/PS1 mice.
- **Status**: supported
- **Falsification criteria**: Blocking microglial proliferation failing to reduce senescence/DAM or failing to improve pathology, or evidence that plaque-associated microglial senescence is proliferation-independent.
- **Proof**: [E06]
- **Evidence basis**: §1.2.2 (Hu 2021; Olmos-Alonso 2016; Matsudaira 2023 — DAM cluster only in old mice, majority of DAM senescent).
- **Interpretation**: Frames a specific mechanism (replicative senescence after excessive proliferation) distinguishing microglia from post-mitotic glia.
- **Dependencies**: C01, C03
- **Tags**: microglia, replicative-senescence, DAM, proliferation, APP/PS1

## C07: Clearing senescent glia reduces AD pathology and improves cognition in mouse models
- **Statement**: Genetic or pharmacological (senolytic) clearance of p16INK4A-positive senescent glia in AD/tauopathy mouse models reduces tau phosphorylation, NFT formation, Aβ accumulation, cortical/hippocampal neurodegeneration, and neuroinflammation, and improves memory and cognitive performance.
- **Status**: supported
- **Falsification criteria**: Senolytic/genetic clearance of senescent glia failing to alter Aβ/tau pathology or cognition in AD models.
- **Proof**: [E05]
- **Evidence basis**: §1.1, §1.2, §1.3 — Bussian 2018 (clearance reduced tau phosphorylation, NFT, neurodegeneration, cognitive decline); Zhang 2019 (senolytic removed senescent OPCs, reduced Aβ, enhanced cognition); Musi 2018; Yao 2024 (D+Q reduced p16 microglia, tau hyperphosphorylation, improved cognition); AP20187 and ABT-263 (Navitoclax) reduced IL-6/IL-1β and tau pathology.
- **Interpretation**: Strongest causal evidence that glial senescence is a driver, not a bystander, and that it is therapeutically addressable.
- **Dependencies**: C01, C03, C04
- **Tags**: senolytics, clearance, tau, amyloid, cognition, mouse-models

## C08: Early-phase human senolytic (D+Q) trials reduce SASP factors but show no cognitive/MRI benefit yet
- **Statement**: In a phase I clinical trial, oral D+Q decreased SA-β-gal activity, reduced p16INK4A expression, and decreased circulating SASP factor MMP-12 (Hickson 2019); in symptomatic early-AD older adults, D+Q decreased SASP-associated cytokines/chemokines (IL-17, IL-21, IL-10, IL-6, MMP-9), with dasatinib detected in CSF (BBB crossing), but the treatment showed no effect on cognition or structural MRI measures over the short study period (Gonzales 2023).
- **Status**: supported
- **Falsification criteria**: Human trials showing D+Q does not lower SASP factors, or (conversely) demonstrating robust cognitive/structural benefit contradicting the reported null.
- **Proof**: [E05]
- **Evidence basis**: §1.3 (Hickson et al. 2019; Gonzales et al. 2023; Longo and Massa 2023).
- **Interpretation**: Target engagement (SASP reduction, CSF penetration) is demonstrated in humans, but clinical efficacy in AD remains unproven; motivates larger randomized controlled trials.
- **Dependencies**: C07
- **Tags**: clinical-trial, dasatinib, quercetin, SASP, MMP-12, target-engagement

## C09: Senescence markers are non-universal across glial cell types and often nonspecific
- **Statement**: Senescence markers vary by cell type, brain region, and pathological context; SA-β-gal, p16INK4A, and p21WAF1/CIP1 are broadly observed but HMGB1 has so far been linked to a single cell type, and mouse models show higher p16INK4A/p21WAF1/CIP1 in microglia and OPCs than in astrocytes; markers are often nonspecific/low-sensitivity, making senescent cells hard to distinguish from quiescent or terminally differentiated cells.
- **Status**: supported
- **Falsification criteria**: Identification of a single marker that is both specific and universally expressed across all senescent glial subtypes and contexts.
- **Proof**: [E01]
- **Evidence basis**: §2 Conclusions (Ogrodnik 2021); Tables 1 and 2 (marker presence differs across columns/cell types).
- **Interpretation**: A core limitation flagged by the authors; drives the call for more sensitive, context-specific markers.
- **Dependencies**: C01
- **Tags**: markers, specificity, heterogeneity, limitation, HMGB1
