# Related Work — Typed Dependency Graph

Full `RW` blocks for works with a specific technical delta (reference atlases used as
baselines/validation, method software imported, the mouse model, KCNIP4 biology). A condensed
footprint of the remaining citations follows. Deposited datasets and software are also recorded as
typed dependencies (per compile instructions).

---

## RW01: Gabitto et al., 2024 — SEA-AD integrated multimodal cell atlas of AD
- **DOI**: 10.1038/s41593-024-01774-5 (Nat. Neurosci. 27, 2366–2383) [ref 23]
- **Type**: baseline / imports
- **Delta**:
  - What changed: SEA-AD DLPFC atlas (~1.4M nuclei, BICCN reference annotations/supertypes) is used as the reference for cosine-distance validation, scANVI/ingest label transfer, and spatialID DNN training.
  - Why: to benchmark this study's 18 Ex / 19 In annotations and to project cell identities onto spatial data.
- **Claims affected**: C10 (Ex5 mapping), and cluster-annotation validity underpinning C01–C05.
- **Adopted elements**: BICCN cell-subclass/supertype nomenclature; SEA-AD as MERFISH/atlas comparator.

## RW02: Jorstad et al., 2023 — transcriptomic cytoarchitecture of human neocortex
- **DOI**: 10.1126/science.adf6812 (Science 382) [ref 3]
- **Type**: baseline / bounds
- **Delta**:
  - What changed: primary-visual-cortex (BA17) reference; Ex5 maps to L4_IT2/3/5/6 supertypes; provides the BA17 excitatory reference in which Ex5 = 34.42%.
  - Why: cross-region validation that Ex5 is a BA17-specialized L4 IT population.
- **Claims affected**: C10.
- **Adopted elements**: WithinArea_clusters; L4 sublayer (4cα/4cβ) correspondence.

## RW03: Mathys et al., 2023 — single-cell atlas of cognition/resilience to AD
- **DOI**: 10.1016/j.cell.2023.08.039 (Cell 186, 4365–4385) [ref 8]
- **Type**: baseline
- **Delta**: prefrontal reference dataset for scANVI prediction (Ex5 = 3% of 112,143). Prior broad resilience/cognition work that this paper narrows to L4.
- **Claims affected**: C10 (and framing of resilience).
- **Adopted elements**: reference annotations for label transfer.

## RW04: Green et al., 2024 — cellular communities / trajectories of brain ageing and AD
- **DOI**: 10.1038/s41586-024-07871-6 (Nature 633, 634–645) [ref 5]
- **Type**: baseline
- **Delta**: prefrontal reference dataset for scANVI prediction (Ex5 = 3.03% of 637,968).
- **Claims affected**: C10.
- **Adopted elements**: reference annotations.

## RW05: Otero-Garcia et al., 2022 — molecular signatures of NFT susceptibility in AD
- **DOI**: 10.1016/j.neuron.2022.06.021 (Neuron 110, 2929–2948) [ref 4]
- **Type**: extends
- **Delta**: prior work (shared author M.O.G.) on tangle-bearing vulnerable neurons; this study complements it by defining the *resilient* counterpart in L4.
- **Claims affected**: C02, C04 (vulnerability context).
- **Adopted elements**: vulnerability framework.

## RW06: Gazestani et al., 2023 — early AD pathology involves transient cell states
- **DOI**: 10.1016/j.cell.2023.08.005 (Cell 186, 4438–4453) [refs 7, 57]
- **Type**: refutes / bounds (contrast)
- **Delta**:
  - What changed: identified a *maladaptive* hyperexcitability signature in vulnerable L2/3 pyramidal neurons (upregulation of APP, PRNP, ATP1A3, SNAP25, SYT1, CDK5); this study contrasts it with a *neuroprotective* resilience signature in L4 IT.
  - Why: distinguishes maladaptive vs compensatory responses to hyperexcitability.
- **Claims affected**: C04, C08 (compensatory vs maladaptive).
- **Adopted elements**: hyperexcitability framing.

## RW07: Xia et al., 2022 — AppSAA App knock-in mouse model
- **DOI**: 10.1186/s13024-022-00547-7 (Mol. Neurodegener. 17, 41) [ref 24]
- **Type**: imports (model system)
- **Delta**: provides the humanized App knock-in (AppSAA) model exhibiting amyloid plaques, microgliosis, plaque-associated dystrophic neurites; used for in vivo Kcnip4 overexpression.
- **Claims affected**: C08.
- **Adopted elements**: mouse model, reported sex-difference caveat.

## RW08: Morohashi et al., 2002 — cloning of CALP/KChIP4 (KCNIP4)
- **DOI**: 10.1074/jbc.M200897200 (J. Biol. Chem. 277, 14965–14975) [ref 45]
- **Type**: imports (mechanism)
- **Delta**: defines KChIP4 as an EF-hand protein interacting with presenilin 2 and Kv4; grounds the KCNIP4-presenilin/APP link and calcium-binding classification.
- **Claims affected**: C05, C07, C08 (KCNIP4 mechanism).
- **Adopted elements**: KChIP4 biology.

## RW09: An et al., 2000 — KChIPs modulate A-type potassium channels
- **DOI**: 10.1038/35000592 (Nature 403, 553–556) [ref 48]
- **Type**: imports (mechanism)
- **Delta**: establishes that KChIPs control A-type outward K+ currents via Kv4, the biophysical basis for KCNIP4's proposed excitability-lowering role.
- **Claims affected**: C07, C08.
- **Adopted elements**: Kv4/A-current mechanism.

## RW10: Morabito et al., 2023 — hdWGCNA
- **DOI**: 10.1016/j.crmeth.2023.100498 (Cell Rep. Methods 3, 100498) [ref 56]
- **Type**: imports (method)
- **Delta**: co-expression network method used to derive candidate resilience modules and hub genes; the paper notes its inability to natively include covariates as a limitation.
- **Claims affected**: C09.
- **Adopted elements**: hdWGCNA R package (v0.2.23).

## RW11: Büttner et al., 2021 — scCODA compositional model
- **DOI**: 10.1038/s41467-021-27150-6 (Nat. Commun. 12, 6876) [ref 34]
- **Type**: imports (method)
- **Delta**: Bayesian compositional analysis used (with a custom sign-constrained stress test) to call resilient/vulnerable proportion changes.
- **Claims affected**: C01, C02.
- **Adopted elements**: scCODA v0.1.9.

## RW12: Finak et al., 2015 — MAST
- **DOI**: 10.1186/s13059-015-0844-5 (Genome Biol. 16, 278) [ref 47]
- **Type**: imports (method)
- **Delta**: zero-inflated mixed-model framework (with lme4) is the backbone of the high-confidence DGE and the KCNIP4 stage analysis.
- **Claims affected**: C03, C04, C05.
- **Adopted elements**: MAST v1.24.1.

## Condensed citation footprint (remaining references)

**Single-cell AD/brain atlases & methods (background/baseline):** Mathys 2024 multiregion (ref 1); Cain 2023 multicellular communities (ref 2); Siletti 2023 adult-brain diversity (ref 6); Liu 2025 multiregion epigenomics/cognitive resilience (ref 55); Consens 2022 IT/SST neurons in AD (ref 35).

**Neocortex organization / L4 cytoarchitecture:** Harris & Shepherd 2015 (13); Palomero-Gallagher & Zilles 2019 (14); Zeng & Sanes 2017 (15); Wei 2022 visual-cortex cell types (16); von Economo & Koskinas 1929 (17); Tasic 2018 (18); Cadwell 2019 (19); Lake 2018 (26); Zeng 2012 (27); Yao 2021 mouse taxonomy (28); Di Bella 2021 (59); Rockland & Pandya 1981 (30); Garcia-Cabezas 2020 (31); Balaram 2014 V1/V2 (32,33).

**AD neuropathology / staging:** Braak & Braak 1991 (9); Hyman 2012 NIA-AA (10); Du 2007 (11); Ossenkoppele 2019 (12); Serrano-Pozo 2011 (20); Duyckaerts 2009 (21); Braak 2006 (22); Mirra 1991 CERAD (69); Crary 2014 PART (70); Hof 1990 vulnerable pyramidal neurons (58); Leuba & Kraftsik 1994 visual cortex in AD (51); Hawrylycz 2012 Allen Human Brain Atlas (29).

**AD genetic risk / KCNIP:** Zhang 2023 (38); Prokopenko 2022 DTNB/DLG2 (39); Park 2021 (40); Wang 2014 NRG3 (41); Werren 2024 CSMD1 (42); Athanasiu 2017 CSMD1/CSMD2 (43); Baum 2024 CSMD1/complement (44); Shulman 2013 (46); Kitazawa 2014 Kv4/KChIP stoichiometry (60); Buxbaum 1998 calsenilin/presenilin (61); Polans 1995 recoverin (62).

**Hyperexcitability / therapeutics:** Palop 2007 (50); Palop & Mucke 2016 (52); Vossel 2017 (53); Targa Dias Anastacio 2022 (54); Mattson & Arumugam 2018 (63); Slutsky 2024 (64); Li 2022 arousal circuits (65); Vossel 2021 levetiracetam RCT (66); Sanchez 2012 levetiracetam (67); Shigihara 2020 non-pharmacological (68); Simon 2024 opto-seq IEGs (49).

**Software / statistical methods (imports):** Macosko 2015 Drop-seq (71); Melsted 2021 kb-python (72); Lun 2019 DropletUtils/EmptyDrops (73); McGinnis 2019 DoubletFinder (74); Wolf 2018 Scanpy (75); Korsunsky 2019 Harmony (76); Xu 2021 scANVI (77); Mollie 2017 glmmTMB (78); Andersson 2020 Stereoscope (79); Palla 2022 squidpy (80); Shen 2022 spatialID (81); Luke 2017 lme4 significance (82); Muzellec 2023 pyDESeq2 (83); Fang 2023 GSEApy (84); Zhou 2019 Metascape (85); Kolberg 2023 g:profiler (86); GTEx Consortium 2013 (87); Koopmans 2019 SynGO (88); Shannon 2003 Cytoscape (89); Beaudoin 2012 primary neuron culture (90); Gerrits 2021 microglia profiles (25); Squair 2021 false discoveries in scRNA DE (36); Junttila 2022 DE benchmarking (37).

**Self-archive:** Dharshini et al. 2026 — Zenodo code archive (ref 91), DOI 10.5281/zenodo.18113528.

## Deposited datasets (typed dependency: data sources)
| Dataset | Identifier | Repository | Access | Role |
|---------|-----------|------------|--------|------|
| Raw snRNA-seq + metadata + processed matrices (new) | GSE263468 | NCBI GEO | open | Primary data (C01–C06, C09, C10) |
| Reused snRNA-seq samples (8 of 243) | GSE129308; GSE181715 | NCBI GEO | open | Subset of cohort |
| Interactive snRNA-seq exploration | collection 0d35c0fd-ef0b-4b70-bce6-645a4660e5fa | CZI CELLxGENE | open | Browsable resource |
| Xenium spatial dataset (16 sections, BA9+BA17, 4 AD + 4 control) | 10.5281/zenodo.16703438 | Zenodo | open | Spatial validation (C01, C10) |
| Code + pretrained models | 10.5281/zenodo.18113528 (GitHub AkilaRanjith/…) | Zenodo / GitHub | open (CC-BY-4.0) | Reproducibility (all) |

## Clinical trials
None. This is a basic/translational study (human postmortem tissue + AppSAA mouse AAV overexpression); no trial registration. Levetiracetam trials (refs 66,67) are cited as therapeutic background, not run here.
