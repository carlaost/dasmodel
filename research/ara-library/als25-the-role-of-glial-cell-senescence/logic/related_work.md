# Related Work — Typed Dependency Graph

*Grounding: full-text. This is a review, so its "related work" is the primary literature it
synthesizes. Full `RW` blocks are given for studies with a specific, load-bearing technical delta
that a claim rests on; the remaining citation footprint is captured more briefly below. The paper's
reference list gives journal/volume/pages but not DOIs for most entries, so DOI fields are marked
accordingly rather than fabricated.*

## RW01: Bussian et al., 2018 — Clearance of senescent glial cells prevents tau pathology
- **DOI**: Nature 562(7728):578–582 (DOI not listed in paper reference)
- **Type**: imports (foundational causal evidence)
- **Delta**:
  - What changed: Genetic clearance of p16INK4A-positive senescent glia (astrocytes + microglia) in a tauopathy mouse model reduced tau phosphorylation, NFT formation, cortical/hippocampal neurodegeneration, and ameliorated memory/cognitive decline; also used INK-ATTAC×PS19 and Navitoclax (ABT-263).
  - Why: Establishes senescent glia as causal drivers of tau pathology, not bystanders.
- **Claims affected**: C01, C05, C07
- **Adopted elements**: Central causal pillar for the senolytic-therapy argument.

## RW02: Zhang et al., 2019 — Senescent OPCs near Aβ plaques; senolytic rescue
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: In APP/PS1, senescent OPCs (p16INK4A+, p21WAF1/CIP1+) accumulate near Aβ plaques; SA-β-gal colocalizes with OPC markers and increases with age; senolytic treatment removed senescent OPCs, reduced Aβ accumulation, and enhanced cognition. Aβ triggers SA-β-gal in OPCs in vitro.
  - Why: Links OPC senescence to amyloid pathology and cognition.
- **Claims affected**: C01, C03, C07
- **Adopted elements**: OPC senescence evidence (Table 2).

## RW03: Gaikwad et al., 2021 — Astrocyte senescence and tau oligomers in AD
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: >75% of GFAP+ astrocytes in AD frontal cortex reactive to both TauO and p16INK4A (vs far fewer in controls); elevated HMGB1 (SASP) and γH2AX in TauO-associated astrocytes.
  - Why: Quantitative human-tissue anchor for astrocyte senescence linked to tau.
- **Claims affected**: C01, C03, C05
- **Adopted elements**: Basis of claim C05; HMGB1 marker (Tables 1, 2).

## RW04: Musi et al., 2018 — Tau-driven senescence; senolytics in tauopathy
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Senescent cells in tauopathy; intermittent D+Q in very-old tauopathy mice reduced NFTs, improved cerebral blood flow, decreased ventricular pathology and brain atrophy.
  - Why: Preclinical senolytic efficacy against tau pathology and neurodegeneration.
- **Claims affected**: C05, C07
- **Adopted elements**: Senolytic evidence (§1.3).

## RW05: Hu et al., 2021 — Microglial replicative senescence in APP/PS1
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Plaque-associated microglia expand, become DAM/senescent (↑ SA-β-gal, telomere shortening, senescence signature); pharmacological inhibition of proliferation prevented DAM, reduced senescence, mitigated Aβ-dependent synaptic damage, improved cognition. Pharmacological prevention of microglial senescence alleviated Aβ pathology.
  - Why: Mechanistic basis for microglial replicative senescence.
- **Claims affected**: C06, C07
- **Adopted elements**: Basis of claim C06 (with Olmos-Alonso 2016).

## RW06: Fancy et al., 2024 — Comprehensive senescent-microglia analysis in AD
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Post-mortem AD cortex shows more senescent microglia (↑ p16INK4A, p21WAF1/CIP1, γH2AX, GLB1) vs controls; single-nuclei RNA-seq shows upregulated DDR/senescence and downregulated phagocytosis genes; plaque-associated microglia (PAM) have higher senescence/DNA-damage/mitochondrial-stress markers.
  - Why: Human single-cell evidence tying microglial senescence to Aβ load and phagocytic decline.
- **Claims affected**: C01, C04, C06
- **Adopted elements**: Microglia markers (Table 2).

## RW07: Karabag et al., 2023 — Tau-induced microglial senescence
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Recombinant human tau increased microglial p16INK4A/p21, induced SASP (IL-1β, IL-6, TNF-α), decreased Lamin B1, increased γH2AX, reduced migration and tau uptake.
  - Why: Demonstrates tau as a direct inducer of microglial senescence and clearance deficit.
- **Claims affected**: C01, C03, C04
- **Adopted elements**: Microglia pathology markers (Table 2).

## RW08: Ungerleider et al., 2022 — Aβ-induced astrocyte senescence
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Oligomeric Aβ in primary human astrocytes increased p53/p21WAF1/p16INK4A and SA-β-gal, decreased Ki-67, increased IL-6, reduced IGF-1/NGF, increased γH2AX/53BP1 foci.
  - Why: Direct in vitro Aβ→astrocyte senescence with functional readouts.
- **Claims affected**: C01, C03, C04
- **Adopted elements**: Astrocyte pathology markers (Table 2).

## RW09: Hickson et al., 2019 — First-in-human senolytic (D+Q) phase I
- **DOI**: EBioMedicine (DOI not listed in paper reference)
- **Type**: baseline (clinical target-engagement benchmark)
- **Delta**:
  - What changed: Oral D+Q in humans decreased SA-β-Gal activity, reduced p16INK4A, decreased circulating SASP factor MMP-12.
  - Why: First human demonstration of senolytic target engagement.
- **Claims affected**: C07, C08
- **Adopted elements**: Human evidence for senolytic feasibility.

## RW10: Gonzales et al., 2023 — D+Q in early symptomatic AD
- **DOI**: (DOI not listed in paper reference)
- **Type**: baseline (human clinical result)
- **Delta**:
  - What changed: In early-AD older adults, D+Q decreased SASP cytokines/chemokines (IL-17, IL-21, IL-10, IL-6, MMP-9); dasatinib crossed into CSF; no effect on cognition or structural MRI in the short study period.
  - Why: Establishes human target engagement but null clinical efficacy so far.
- **Claims affected**: C08
- **Adopted elements**: Basis for cautious efficacy framing.

## RW11: Kang et al., 2015 — GATA4 as senescence/SASP mediator
- **DOI**: Science (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: GATA4 mediates senescence in astrocytes, oligodendrocytes, and pyramidal neurons; accumulates in aged human prefrontal cortex; regulates NF-κB and SASP (IL-6, IL-1α, Cxcl1); activated via ATR/ATM independently of p53/p16.
  - Why: Introduces a p53/p16-independent senescence branch.
- **Claims affected**: C01
- **Adopted elements**: GATA4 inflammation marker (Tables 1).

## RW12: Soreq et al., 2017 — Brain aging transcriptomics concentrated in glia
- **DOI**: Cell Reports (DOI not listed in paper reference)
- **Type**: imports (motivating datum)
- **Delta**:
  - What changed: Across 480 individuals aged 16–106, most age-related gene expression change is in glia not neurons; astrocyte/microglia gene dysregulation best predicts aging; hippocampus and substantia nigra most affected.
  - Why: Empirical justification for glia-centric framing.
- **Claims affected**: C02
- **Adopted elements**: Basis of claim C02.

## RW13: Ogrodnik et al., 2021 — Cross-glial senescence markers; AP20187
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Documents p16INK4A/p21 across microglia, OPCs, oligodendrocytes (higher in microglia/OPCs than astrocytes); AP20187 in aged INK-ATTAC mice reduced microglial activation and SASP and improved cognition.
  - Why: Comparative marker levels (basis of C09) plus genetic senolytic evidence.
- **Claims affected**: C07, C09
- **Adopted elements**: Marker comparison (Tables 1); AP20187 evidence.

## RW14: Matsudaira et al., 2023 — Single-cell microglial senescence; DAM
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Single-cell transcriptomics shows microglia senesce in brain/spinal cord during aging (↑ p16INK4A, Il1b, Cxcl10, γH2AX in white matter); DAM cluster only in old mice and enriched for p16INK4A (most DAM senescent).
  - Why: Links DAM state to senescence.
- **Claims affected**: C01, C06
- **Adopted elements**: Microglia markers (Table 1).

## RW15: Wang et al., 2020 — OPC differentiation loss drives age-dependent myelin loss
- **DOI**: (DOI not listed in paper reference)
- **Type**: imports
- **Delta**:
  - What changed: Age-dependent myelin loss is mostly due to loss of OPC proliferation/differentiation; preventing OPC differentiation caused memory deficits in young mice, promoting it rescued synaptic loss/memory in old mice.
  - Why: Causal link OPC dysfunction → myelin → cognition.
- **Claims affected**: C01, C04
- **Adopted elements**: Oligodendrocyte/OPC senescence narrative (§1.2.3).

## RW16: Lopez-Otin et al., 2023 — Hallmarks of aging
- **DOI**: Cell (DOI not listed in paper reference)
- **Type**: imports (conceptual framework)
- **Delta**:
  - What changed: Framework of aging hallmarks (mitochondrial/oxidative/metabolic decline, DNA damage) used to frame senescence triggers.
  - Why: Conceptual scaffold for the Introduction.
- **Claims affected**: (background)
- **Adopted elements**: Trigger taxonomy (Figure 1).

## Broader citation footprint (brief entries)

Grouped by role; these support background, individual markers, or single mechanistic points without
a claim-defining delta:

- **Senescence biology / triggers**: McHugh & Gil 2018; Wiley & Campisi 2021; de Magalhaes 2024; Baker & Petersen 2018; d'Adda di Fagagna 2008; Roger et al. 2021; Satyanarayana et al. 2003; Sapieha & Mallette 2018; Schafer et al. 2020; Millner & Atilla-Gokcumen 2020; Al-Azab et al. 2022; Going et al. 2002; Hudgins et al. 2018; Tian et al. 2022; Crescenzi et al. 2023.
- **Senescence DNA-damage/chromatin markers**: Siddiqui et al. 2015 (γH2AX); Freund et al. 2012 (Lamin B1); Sofiadis et al. 2021 (HMGB1); Davalos et al. 2013; Gaikwad et al. 2024.
- **p16/p21/p53 in aging and removal-rescue**: Chin et al. 1999; Baker et al. 2008; Janzen et al. 2006; Sato et al. 2015.
- **AD pathology / senescence in AD brain**: Trejo-Lopez et al. 2022; Leng & Edison 2021; Pini et al. 2016; McShea et al. 1997; Bhat et al. 2012; Wei et al. 2016; de la Monte et al. 1997; Frost et al. 2014/2016; Panossian et al. 2003; Thomas et al. 2008; Franco et al. 2006; Flanary et al. 2007; Forero et al. 2016; Arendt et al. 1996/1998; Islam et al. 2022; Luth et al. 2000; Ohyagi et al. 2005; Welch et al. 2022; He et al. 2013; Hussong et al. 2023.
- **Glial biology / proliferation**: von Bartheld et al. 2016; Salas et al. 2020; Sikora et al. 2021; Lee et al. 2000; Ardaya et al. 2020; Joya & Martin 2021; Faulkner et al. 2004; Colodner et al. 2005; Askew et al. 2017; Rodriguez et al. 2022; Sierra et al. 2007/2014; Young et al. 2013; Verkhratsky & Nedergaard 2018.
- **Astrocyte function/senescence**: Perea et al. 2009; Ahmad et al. 2019; Farina et al. 2007; Verkhratsky et al. 2010; Kawano et al. 2012; Salminen et al. 2011; Porchet et al. 2003; Simard et al. 2003; Simpson et al. 2011; Lee et al. 2022; Chen et al. 2020; Gildea & Liddelow 2025; Pertusa et al. 2007; Ojo et al. 2015; Bitto et al. 2010; Evans et al. 2003; Matias et al. 2022; Cohen & Torres 2019; Dai et al. 2020; Yu et al. 2017; Turnquist et al. 2016; Limbad et al. 2020; Frost & Li 2017; Iram et al. 2016; Soni et al. 2024; Garcia-Agudo et al. 2024; Zhao et al. 2011; Chinta et al. 2018; Parhizkar et al. 2019.
- **Microglia function/senescence**: Mittelbronn et al. 2001; Pont-Lezica et al. 2014; Zhan et al. 2014; Nimmerjahn et al. 2005; Streit et al. 2004/2009; Stojiljkovic et al. 2019; Xu et al. 2008; Damani et al. 2011; Safaiyan et al. 2016; Ritzel et al. 2015; Henry et al. 2009; Olmos-Alonso et al. 2016; Hellwig et al. 2015; Henningfield et al. 2024; Yao et al. 2024.
- **Oligodendrocyte/OPC/myelin**: Bradl & Lassmann 2010; Sutor et al. 2000; Haines et al. 2011; Kirkpatrick et al. 2001; Edgar et al. 2004; Pan et al. 2020; Steadman et al. 2020; Luan et al. 2021; Kujuro et al. 2010; Gomez et al. 2024; Neumann et al. 2019; Windener et al. 2024; Al-Mashhadi et al. 2015; Schlett et al. 2023; Tepavcevic 2021; Thorburne & Juurlink 1996; Nasrabady et al. 2018; Huang et al. 2024; Kolind et al. 2013; Dean 3rd et al. 2016; Bourbon-Teles et al. 2019; Ota et al. 2019; McAleese et al. 2015; Dong et al. 2018; Qiu et al. 2023; Depp et al. 2023; Jantaratnotai et al. 2003; Xie et al. 2021; Rouillard et al. 2022; Li et al. 2024.
- **AD risk factors / neuroinflammation**: Raulin et al. 2022; Mendsaikhan et al. 2019; Li et al. 2023; Heneka et al. 2013; Hou et al. 2019; Wang & Michaelis 2010; Flores-Ponce & Velasco 2024; Kreisman et al. 2000; Mueller et al. 2007; Scheff et al. 2007; West et al. 2004.
- **Therapeutics / senotherapeutics**: Wang et al. 2023; Drake et al. 2024; Hickson et al. 2019; Yousefzadeh et al. 2018; Xu et al. 2018; Mikawa et al. 2024; Dorling et al. 2020; Zhu et al. 2015; Van Skike et al. 2021; Lin et al. 2013; Morawe et al. 2022; Capiralla et al. 2012; Tosatti et al. 2022; Balez et al. 2016; Park et al. 2019; Hou et al. 2022; Longo & Massa 2023.
- **Proteostasis / mitochondria (Conclusions)**: Cozachenco et al. 2023; Barmaki et al. 2023; Kreher et al. 2021; Tajbakhsh et al. 2021; Wang et al. 2009; Bhatti et al. 2017; Miwa et al. 2022.
