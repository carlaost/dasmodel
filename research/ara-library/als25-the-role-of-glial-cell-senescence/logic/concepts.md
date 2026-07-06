# Concepts

*Grounding: full-text. Definitions are the review's usage of each term, with source sections.*

## Cellular senescence
- **Notation**: —
- **Definition**: A protective physiological response of irreversible (permanent) cell-cycle arrest in aged or damaged cells that limits proliferation of dysfunctional cells; accompanied by metabolic changes, altered apoptosis sensitivity (resistance to apoptosis), and secretion of pro-inflammatory molecules (SASP). Triggered by mitochondrial dysfunction, telomere shortening, oncogene activation, DNA damage, and oxidative stress.
- **Boundary conditions**: Beneficial in wound healing and tumor suppression; deleterious when senescent cells accumulate with age, contributing to aging and age-related disease. Traditionally associated with proliferating cells, but post-mitotic cells may enter a "senescence-like" state.
- **Related concepts**: SASP, DNA damage response, replicative senescence, inflammaging, p16INK4A, p21WAF1/CIP1

## Senescence-associated secretory phenotype (SASP)
- **Notation**: SASP
- **Definition**: The mix of interleukins, chemokines, growth factors, and proteases released by senescent cells (e.g., IL-1α, IL-1β, IL-6, IL-8, TNF-α, TGF-β, MMPs, HMGB1, PAI-1, NOS2, RAGE-related factors) that propagates senescence to neighboring cells and drives chronic inflammation and tissue damage.
- **Boundary conditions**: Composition varies by cell type and stimulus; sustained SASP produces "inflammaging" and self-reinforcing senescence loops.
- **Related concepts**: Cellular senescence, inflammaging, NF-κB, GATA4, neuroinflammation

## DNA damage response (DDR)
- **Notation**: DDR
- **Definition**: The signaling cascade activated by DNA damage that promotes cell-cycle arrest via p53 → p21WAF1/CIP1, or alternatively via upregulation of p16INK4A. When DNA damage is severe, persistent, or irreparable, chronic DDR enforces permanent arrest (senescence).
- **Boundary conditions**: Triggered by telomere erosion, replicative stress, oxidative stress, radiation, and genotoxic chemicals; upstream regulators include ATM and ATR kinases.
- **Related concepts**: γH2AX, p53, p21WAF1/CIP1, p16INK4A, ATM/ATR, cellular senescence

## p16INK4A (CDKN2A)
- **Notation**: p16INK4A
- **Definition**: Cyclin-dependent kinase inhibitor 2A; a CDK inhibitor whose upregulation mediates cell-cycle arrest independent of the p53/p21 axis. A principal senescence marker used throughout the review; elevated in senescent astrocytes, microglia, OPCs, and oligodendrocytes, and in tau-tangle-bearing neurons/neuritic plaques in AD cortex.
- **Boundary conditions**: Expression is non-universal — higher in microglia and OPCs than astrocytes in mouse models; used as a target for genetic clearance (INK-ATTAC, AP20187).
- **Related concepts**: p21WAF1/CIP1, p53, cell-cycle arrest, senolytics, DAM

## p21WAF1/CIP1 (CDKN1A)
- **Notation**: p21WAF1/CIP1
- **Definition**: Cyclin-dependent kinase inhibitor 1; downstream effector of p53 in the DDR that enforces cell-cycle arrest. A senescence marker elevated across glial types in aging and AD.
- **Boundary conditions**: Upregulated in vitro but not ex vivo in some microglial contexts (Stojiljkovic 2019).
- **Related concepts**: p53, p16INK4A, DDR, GADD45a

## Replicative senescence
- **Notation**: —
- **Definition**: Senescence triggered by progressive telomere shortening during repeated cell division in proliferating cells. In AD, invoked for microglia that senesce after pathology-driven excessive proliferation around Aβ plaques.
- **Boundary conditions**: Applies to proliferation-competent glia (microglia, astrocytes, OPCs); mature oligodendrocytes and neurons are post-mitotic and must senesce via division-independent mechanisms.
- **Related concepts**: Telomere erosion, DAM, microglia, stress-induced senescence

## Disease-associated microglia (DAM)
- **Notation**: DAM
- **Definition**: A microglial activation state (also plaque-associated microglia, PAM) identified transcriptionally; in aged mice the DAM cluster appears enriched for p16INK4A, indicating the majority of DAM are senescent.
- **Boundary conditions**: DAM-related cluster identified only in old mice; PAM near Aβ plaques express higher senescence and DNA-damage/mitochondrial-stress markers than plaque-distant microglia.
- **Related concepts**: Microglia, replicative senescence, PAM, p16INK4A, phagocytosis

## Senescence-associated β-galactosidase (SA-β-gal)
- **Notation**: SA-β-gal
- **Definition**: Lysosomal β-galactosidase activity detectable at pH 6, the most widely used histochemical marker of senescent cells; encoded in part by GLB1. Elevated across senescent astrocytes, microglia, OPCs, and oligodendrocytes.
- **Boundary conditions**: Nonspecific/low-sensitivity; cannot alone distinguish senescent from quiescent/terminally differentiated cells (a stated limitation).
- **Related concepts**: GLB1, cellular senescence, senescence markers

## Senolytics
- **Notation**: —
- **Definition**: Small molecules designed to selectively eliminate senescent cells by inducing their apoptosis. Examples surveyed: dasatinib + quercetin (D+Q), AP20187 (clears highly p16INK4A-expressing cells), Navitoclax/ABT-263 (BCL-2/BCL-xL inhibitor), Fisetin.
- **Boundary conditions**: Effects are cell-type- and context-specific (dasatinib vs quercetin target different senescent cell types); systemic administration risks off-target toxicity; intermittent "hit-and-run" dosing proposed to limit harm.
- **Related concepts**: Senomorphics, D+Q, BCL-2/BCL-xL, p16INK4A, apoptosis

## Senomorphics
- **Notation**: —
- **Definition**: Small molecules that suppress the SASP (rather than killing senescent cells) by inhibiting SASP-driving signaling pathways (p38MAPK, mTOR, JAK/STAT) or transcription factors (NF-κB, STAT3). Examples: rapamycin/PQR530 (mTOR), resveratrol and apigenin (NF-κB), adalimumab (anti-TNF-α), Ginsenoside F1/SGB121.
- **Boundary conditions**: Require continuous treatment to maintain SASP suppression (unlike senolytics, which eliminate cells).
- **Related concepts**: SASP, senolytics, NF-κB, mTOR, JAK/STAT

## GATA4
- **Notation**: —
- **Definition**: A transcription factor identified as a mediator of senescence in astrocytes, oligodendrocytes, and pyramidal neurons; accumulates in aged human prefrontal cortex, spatially correlates with p16INK4A, and regulates NF-κB and SASP components (IL-6, IL-1α, Cxcl1). Activated downstream of ATR/ATM but independently of p53 and p16INK4A signaling.
- **Boundary conditions**: A senescence/SASP inducer that operates in a p53/p16-independent DDR branch.
- **Related concepts**: SASP, NF-κB, ATM/ATR, DDR

## Inflammaging
- **Notation**: —
- **Definition**: The chronic, low-grade inflammation of advanced age driven in part by SASP release and oxidative stress from senescent cells; promotes senescence in neighboring cells, creating a self-perpetuating loop.
- **Boundary conditions**: A systemic aging phenomenon manifesting in the brain as chronic neuroinflammation.
- **Related concepts**: SASP, neuroinflammation, cellular senescence, feedback loop

## Glial cells (astrocytes, microglia, oligodendrocytes/OPCs)
- **Notation**: —
- **Definition**: Non-neuronal CNS cells (~50% of brain cells) maintaining homeostasis: astrocytes (~20% of brain cells; BBB, ion/glutamate balance, tripartite synapse), microglia (~5%–10%; resident immune cells, phagocytosis, synaptic surveillance), oligodendrocytes (myelination) and their precursors OPCs (highest proliferation rate; remyelination).
- **Boundary conditions**: Retain proliferative capacity (unlike neurons) and can therefore undergo replicative and stress-induced senescence.
- **Related concepts**: Replicative senescence, myelination, tripartite synapse, DAM
