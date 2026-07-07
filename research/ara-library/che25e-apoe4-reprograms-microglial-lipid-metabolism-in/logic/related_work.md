# Related Work — Typed Dependency Graph

*Grounding: full-text. This is a review, so its "related work" is the primary literature it
synthesizes. Full `RW` blocks are given for studies with a specific, load-bearing technical delta
that a claim rests on; the remaining citation footprint is captured more briefly below. Reference
numbers correspond to the paper's own numbered bibliography.*

## RW01: Haney et al., 2024 (Nature) — APOE4/4 linked to damaging lipid droplets in AD microglia
- **DOI**: Not listed in paper reference (Nature 628:154-161)
- **Type**: imports (foundational causal evidence)
- **Delta**:
  - What changed: Establishes that APOEε4/ε4 genotype is directly linked to pathological, "damaging" lipid droplets in AD microglia — a central empirical anchor for the review's LDAM framework.
  - Why: Provides the human-genotype-to-lipid-droplet-phenotype link underlying the whole microglial lipid narrative.
- **Claims affected**: C01, C09
- **Adopted elements**: Central evidentiary basis for LD-focused microglial mechanism (§3.2, §4.1.1).

## RW02: Marschallinger et al., 2020 (Nat Neurosci, Author Correction) — Discovery of lipid-droplet-accumulating microglia (LDAM)
- **DOI**: Not listed in paper reference
- **Type**: imports (foundational)
- **Delta**:
  - What changed: Original identification of LDAM as a dysfunctional, proinflammatory microglial state in the aging brain.
  - Why: Source of the LDAM concept and terminology used throughout the review.
- **Claims affected**: C01, C09
- **Adopted elements**: LDAM definition and phenotype (impaired phagocytosis, proinflammatory secretion).

## RW03: Zhou et al., 2023 (Cell Res) — LilrB3 as a cell-surface receptor of APOE4
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Identifies LilrB3 as an APOE4-binding receptor on microglia, upregulating type-I-interferon-stimulated genes (IFITM3, BST2, MX1, ISG15, STAT1) and driving a proinflammatory, phagocytosis-impaired state.
  - Why: Establishes the direct receptor-mediated route by which APOE4 activates neuroinflammation, independent of its lipid-metabolic effects.
- **Claims affected**: C03
- **Adopted elements**: LilrB3/ISG pathway (Figure 4A; §4.2).

## RW04: Yin et al., 2023 (Nat Immunol) — APOE4 impairs microglial response via TGFβ-mediated checkpoints
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Shows APOE4 activates ITGB8-TGFβ signaling, upregulates homeostatic checkpoint molecules (e.g., Inpp5d), and inhibits MGnD neuroprotective function; suppresses Aβ42-specific clearance.
  - Why: Mechanistic basis for the ITGB8-TGFβ phagocytosis-suppression node distinct from TREM2/LilrB3.
- **Claims affected**: C05, C09
- **Adopted elements**: ITGB8-TGFβ / Inpp5d / MGnD-suppression mechanism (Figure 2C, Figure 4B).

## RW05: Kaji et al., 2024 (Immunity) — APOE aggregation in microglia seeds β-amyloidosis
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Demonstrates APOE4 increases formation of fibrillar aggregates within microglia that act as nucleation sites for Aβ plaque formation, and that selective ablation of microglial APOE4 restores phagocytic function and reduces plaque burden.
  - Why: Direct causal (ablation) evidence linking microglial APOE4 to both plaque nucleation and phagocytic impairment.
- **Claims affected**: C05
- **Adopted elements**: Microglial-APOE4-ablation rescue evidence (§4.3).

## RW06: Litvinchuk et al., 2024 (Neuron) — LXR agonist ameliorates tau/APOE4-linked glial lipid accumulation
- **DOI**: Not listed in paper reference
- **Type**: imports (therapeutic evidence)
- **Delta**:
  - What changed: An LXR agonist reduces glial lipid accumulation and neurodegeneration linked to tau and APOE4.
  - Why: Preclinical proof-of-concept that pharmacologically restoring cholesterol efflux ameliorates APOE4/tau-linked glial and neurodegenerative pathology.
- **Claims affected**: C02, C13
- **Adopted elements**: LXR-agonist therapeutic rationale (Table 1; §4.1.2, §5).

## RW07: Lu et al., 2024 (Transl Neurodegener) — TRPV1 alleviates APOE4-dependent microglial antigen presentation
- **DOI**: Not listed in paper reference
- **Type**: imports (therapeutic evidence)
- **Delta**:
  - What changed: TRPV1 activation reduces APOE4-driven MHC-II-dependent antigen presentation and T-cell infiltration.
  - Why: Links the lipid-inflammation axis (MHC-II/T-cell hyperactivation) to a specific druggable target (TRPV1).
- **Claims affected**: C04, C13
- **Adopted elements**: TRPV1/capsaicin therapeutic strategy (Table 1).

## RW08: Wang et al., 2023 (Exp Mol Med) — TRPV1 regulates APOE4-disrupted lipid homeostasis and synaptic phagocytosis
- **DOI**: Not listed in paper reference
- **Type**: imports (therapeutic evidence)
- **Delta**:
  - What changed: TRPV1 reactivation ameliorates cerebral lipid metabolic dysregulation, reduces LD accumulation, and attenuates microglial synaptic pruning, improving tau pathology and memory.
  - Why: Extends TRPV1's therapeutic relevance from inflammation (RW07) to lipid metabolism and synaptic phagocytosis specifically.
- **Claims affected**: C01, C06, C13
- **Adopted elements**: TRPV1 mechanism spanning lipid + phagocytosis axes (§4.3, §5).

## RW09: Leng et al., 2022 (Nat Metab) — Microglial HK2 deficiency increases ATP generation via lipid metabolism, promoting Aβ clearance
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Pharmacological/genetic HK2 inhibition in microglia activates lipoprotein lipase, redirecting metabolism toward lipid utilization to sustain ATP and promote Aβ clearance; effect reported as microglia-specific.
  - Why: Identifies a distinctive protective/compensatory glycolysis-lipid coupling, contrasting with the otherwise pathological glycolytic shift described elsewhere (Lee et al. 2023, RW10).
- **Claims affected**: C11
- **Adopted elements**: HK2-lipoprotein-lipase-ATP-Aβ-clearance mechanism (§3.2).

## RW10: Lee et al., 2023 (Cell Rep) — APOE modulates microglial immunometabolism in response to age/amyloid/inflammation
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Characterizes the glycolysis-up/TCA-down metabolic rewiring of APOE-genotype-dependent microglial immunometabolism under amyloid and inflammatory challenge.
  - Why: Source of the metabolic-reprogramming data underlying the lipid-inflammation amplification claim (C04).
- **Claims affected**: C04
- **Adopted elements**: Glycolysis/TCA metabolic shift data (§4.2).

## RW11: Victor et al., 2022 (Cell Stem Cell) — Lipid accumulation induced by APOE4 impairs microglial surveillance of neuronal-network activity
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Shows APOE4-driven microglial lipid accumulation reduces microglial surveillance of neuronal network activity; extracellular cholesterol accumulation from impaired lipid reuptake increases GIRK3 and hyperpolarizes neurons, reducing excitability.
  - Why: Establishes the specific neuron-microglia communication defect (GIRK3/excitability) downstream of microglial lipid dysregulation.
- **Claims affected**: C01 (context), problem.md O4
- **Adopted elements**: GIRK3/neuronal-excitability mechanism (Figure 3; §4.1.3).

## RW12: Claes et al., 2021 (Mol Neurodegener) — Plaque-associated human microglia accumulate lipid droplets in a chimeric AD model
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: In a chimeric human-microglia AD mouse model, LD accumulation depends on microglial reactivity and plaque proximity; TREM2-R47H reduces in vivo LD accumulation, plaque reactivity, and plaque-associated APOE secretion.
  - Why: Source of the in vivo half of the TREM2-R47H context-dependency finding.
- **Claims affected**: C10
- **Adopted elements**: In vivo TREM2-R47H LD-reduction data (§4.1.1).

## RW13: Andreone et al., 2020 (Nat Neurosci) — PLCγ2 required for TREM2 function and inflammatory response
- **DOI**: Not listed in paper reference
- **Type**: baseline
- **Delta**:
  - What changed: TREM2-R47H exacerbates LD accumulation in vitro — opposite direction from the in vivo chimeric-model finding (RW12).
  - Why: Source of the in vitro half of the TREM2-R47H context-dependency contrast.
- **Claims affected**: C10
- **Adopted elements**: In vitro TREM2-R47H LD-increase data (§4.1.1).

## RW14: Rosenzweig et al., 2024 (Nat Med) — Sex-dependent APOE4 neutrophil-microglia interactions drive cognitive impairment
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: In female APOEε4-carrying AD patients, APOE4-expressing neutrophils upregulate IL-17F, interacting with microglial IL-17RA to disrupt Aβ clearance; interrupting this signaling ameliorates cognitive deficits and reduces Aβ deposition.
  - Why: Identifies a sex-specific, neutrophil-microglia signaling axis contributing to phagocytic impairment, distinct from cell-intrinsic microglial mechanisms.
- **Claims affected**: C05
- **Adopted elements**: IL-17F/IL-17RA sex-dependent mechanism (Figure 4B; §4.3).

## RW15: Tcw et al., 2022 (Cell) — Cholesterol and matrisome pathways dysregulated in astrocytes and microglia
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Characterizes SREBP2-driven cholesterol dysregulation shared across APOE4 astrocytes and microglia, alongside matrisome pathway alterations.
  - Why: Cross-cell-type evidence for the SREBP2/cholesterol lesion generalizing beyond microglia alone.
- **Claims affected**: C02, C07
- **Adopted elements**: SREBP2/cholesterol dysregulation data (§3.1, §4.1.2).

## RW16: Saroja et al., 2022 (PNAS) — Astrocyte-secreted glypican-4 drives APOE4-dependent tau hyperphosphorylation
- **DOI**: Not listed in paper reference
- **Type**: imports
- **Delta**:
  - What changed: Identifies GPC-4 secretion by APOE4 astrocytes as a driver of LRP1-mediated tau hyperphosphorylation in neurons.
  - Why: Establishes the astrocyte-specific GPC-4/LRP1 tau-propagation mechanism.
- **Claims affected**: C07
- **Adopted elements**: GPC-4/LRP1 mechanism (Figure 2A; §3.1).

## Broader citation footprint (brief entries)

Grouped by role; these support background, individual mechanisms, or single points without a
claim-defining delta of their own:

- **APOE4 structure/biophysics**: Hatters et al. 2006; Morrow et al. 2002 (molten globule); Chetty et al. 2017; Rawat et al. 2019; Zannis et al. 1984; Wahrle et al. 2004; Fitz et al. 2019; Herz & Bock 2002.
- **APOE4 epidemiology / genetic risk modifiers**: Farrer et al. 1997 (dose-risk meta-analysis); Wang et al. 2021 (carrier-rate pooled analysis, 389,000 community-dwellers); Fortea et al. 2024 (APOE4 homozygosity as distinct genetic AD form); Belloy et al. 2023 (age/sex/ancestry risk); Payami et al. 1996 (sex difference); Dubal & Yokoyama 2020, Le Guen et al. 2022, Belloy et al. 2020 (Klotho-VS, R251G risk modifiers); Huq et al. 2019 (genetic resilience in ε4 homozygotes); Haan et al. 1999 (comorbidity interactions).
- **Amyloid-pathway mechanisms**: Kanekiyo et al. 2014; Chen et al. 2021; Baligács et al. 2024; Bell et al. 2012; Jackson et al. 2022 (BBB disruption).
- **Astrocyte APOE biology**: Xia et al. 2021 (C/EBPβ); Wynne et al. 2023; de Leeuw et al. 2022; Chung et al. 2016; Staurenghi et al. 2022; Zhao et al. 2017; Qi et al. 2021; Windham et al. 2024; Li et al. 2021; Zalocusky et al. 2021; Koutsodendris et al. 2023.
- **Neuronal APOE4 biology**: Guo et al. 2025; Wang et al. 2025 (senescence/ABCA1); Mahley 2016 (proteolytic fragments); Wang et al. 2018 (structure corrector); Rao et al. 2025 (microglia depletion rescues neuronal pathology).
- **Microglial subtype / transcriptomic biology**: Bassal et al. 2025; Mauerer et al. 2009; Wang et al. 2022 (immunometabolism review); Liu et al. 2015 (glial lipid droplets/ROS); Liu et al. 2023 (cell-autonomous APOE4 restricting microglial response); Muth et al. 2019; Serrano-Pozo et al. 2021 (glial transcriptome); Krasemann et al. 2017 (TREM2-APOE-MGnD pathway); Millet et al. 2024 (exhausted TIM population).
- **Cholesterol/lipid raft biology**: Zhang & Liu 2015; Li et al. 2024 (senescence/cholesterol susceptibility); Komatsu & Komatsu 2023; Lee et al. 2012 (APOE-modulated cholesterol trafficking); Egawa et al. 2016; Rudajev & Novotny 2023.
- **Neuroinflammation background**: Leng & Edison 2021; Zhang et al. 2024 (bibliometric); Goel et al. 2022; Amelimojarad et al. 2024; Wong et al. 2020 (25-HC/IL-1β); Pollock et al. 2019 (Cxorf56); Mhatre-Winters et al. 2022 (sex/APOE inflammatory states); Liu et al. 2024 (APOE-NLRP3 axis).
- **Phagocytosis / tau-propagation biology**: Fitz et al. 2021; Bogie et al. 2013; Park et al. 2024; Vogels et al. 2019; Wu et al. 2025; Asai et al. 2015; Ferrari-Souza et al. 2023; Nelson et al. 2023 (APOE-R136S); Tzioras et al. 2023 (×2, synaptic degeneration/MFG-E8); Huynh et al. 2019.
- **Companion / integrative reviews**: Hu et al. 2024 (companion Biosci Trends piece); Chen et al. 2025 (Cell Death Discov, multifaceted APOE4 roles); Jung et al. 2025 (microglial immunometabolism); Blumenfeld et al. 2024 (Nat Rev Neurosci, cell-type-specific APOE4 roles).
- **Therapeutics — lipid metabolism**: Valencia-Olvera et al. 2023; Boehm-Cagan & Michaelson 2014 (bexarotene); Boehm-Cagan et al. 2016 (ABCA1 agonist); Prakash et al. 2025 (DGAT2); Loix et al. 2022 (PLIN2).
- **Therapeutics — neuroinflammation**: Sangineto et al. 2023 (dimethyl malonate); Yin et al. 2018, Feng et al. 2018, Park et al. 2019, Lonnemann et al. 2020 (NLRP3 inhibitors); Ndoja et al. 2020 (COP1); Feng & Zhang 2019, Abozaid et al. 2022 (resveratrol); Qiao et al. 2020 (curcumin); Huynh et al. 2024 (ACAT inhibitor).
- **Therapeutics — phagocytosis**: Lu et al. 2021 (desloratadine); Pan et al. 2019 (sodium rutin); Lv et al. 2020 (DW14006); Wang et al. 2020, AL002 trial registrations (NCT03635047, NCT04592874).
- **Therapeutics — APOE4-targeting**: Kuszczyk et al. 2013, Krishnamurthy et al. 2020, Liu et al. 2014 (Aβ-mimetics/CN-105); Gratuze et al. 2022, Xiong et al. 2021 (HAE-4 antibody); Zhao et al. 2016, Rosenberg et al. 2018 (AAV-APOEε2); LX1001 trial registrations (NCT03634007, NCT05400330); Li et al. 2023 (CRISPR-Cas9 review).
