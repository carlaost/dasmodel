# Problem Specification

## Observations

### O1: AD neurodegeneration progresses stereotypically from association to primary cortices
- **Statement**: In the AD neocortex, neurodegeneration and tau pathology progress from association cortices (prefrontal BA9, precuneus BA7) to primary cortices (primary visual BA17), with BA17 affected only at the latest Braak stage (VI). L4 in BA17 at Braak VI shows amyloid plaques but minimal tau pathology.
- **Evidence**: Introduction; refs 9–12, 20–22; Fig. 1a (experimental design).
- **Implication**: Comparing early- vs late-affected regions gives a framework to separate cell-intrinsic and microenvironmental factors influencing selective vulnerability/resilience.

### O2: Vulnerable neuronal populations are well characterized; resilient ones are not
- **Statement**: snRNA-seq has identified early-depleted vulnerable populations (L1 NDNF/RELN inhibitory interneurons; L2/3 CUX2/COL5A2 excitatory neurons). Few studies focus on subtypes preserved even in advanced AD.
- **Evidence**: Introduction; refs 2, 7, 8.
- **Implication**: The molecular basis of resilience is a gap; resilient subtypes and their preservation mechanisms could inform therapy.

### O3: Layer 4 cytoarchitecture varies dramatically across neocortical regions
- **Statement**: L4 (internal granular layer) comprises ~38% of the cortical ribbon in BA17 (striate cortex, containing the line of Gennari) but only ~8.6% in BA9. L4 is a major postsynaptic target of thalamic sensory input.
- **Evidence**: Introduction; Fig. 2d–f; refs 3, 6, 16–19.
- **Implication**: L4 has "long been considered a resilient area in AD" due to low tau NFT burden, but its single-cell composition across AD progression was poorly understood.

### O4: Neuronal hyperexcitability is an early feature of AD
- **Statement**: Neuronal hyperexcitability (including subclinical epileptiform activity) is an early and prominent feature of AD pathogenesis, driven by excitatory/inhibitory imbalance; gene-expression changes can be maladaptive or compensatory/neuroprotective.
- **Evidence**: Discussion; refs 52–54, 57.
- **Implication**: Genes that regulate excitability (e.g., potassium-channel-associated) are candidate resilience/neuroprotection factors.

## Gaps

### G1: Whether L4 resilience holds across neocortical regions is unknown
- **Statement**: BA17 and its L4 are considered resilient, but it was unclear whether L4 is resilient across regions (e.g., in association cortex BA9) and which L4 subtypes are involved.
- **Caused by**: O1, O3.
- **Existing attempts**: Prior atlases (SEA-AD, Mathys, Green, Gazestani) broadly defined vulnerability across regions.
- **Why they fail**: They focused on vulnerability and did not resolve region-shared resilient L4 subtypes or their gene signatures.

### G2: The molecular signature and drivers of neuronal resilience are undefined
- **Statement**: No consensus set of genes/pathways distinguishing resilient from vulnerable neurons, nor a validated causal resilience factor.
- **Caused by**: O2, O4.
- **Existing attempts**: Vulnerability signatures (e.g., APP, PRNP, ATP1A3, SNAP25, SYT1, CDK5 in vulnerable L2/3 neurons; ref 57).
- **Why they fail**: A maladaptive/vulnerability signature does not identify what protects resilient cells.

## Key Insight
- **Insight**: Because AD spreads along a spatiotemporal gradient, a resilient region (BA17) at *late* stage should transcriptomically resemble a vulnerable region (BA9) at *early* stage; comparing a prototype resilient subtype (Ex5 L4 IT) against a prototype vulnerable subtype (Ex2 L2/3 IT) across region×stage isolates resilience-associated (upregulated, early, BA17-enriched) genes.
- **Derived from**: O1, O3, O4.
- **Enables**: A conservative multi-method "high-confidence" DGE + co-expression strategy that prioritizes robust resilience genes (e.g., KCNIP4) and a functional proof-of-principle (AAV overexpression).

## Assumptions
- A1: The low/intermediate/high neuropathology grouping (ABC/Braak/CERAD) approximates monotonic disease progression.
- A2: Gene-expression changes in late-stage BA17 are expected to be concordant with early-stage BA9 (progression concordance).
- A3: Relative preservation (increasing proportion) of Ex5 reflects resilience of that population as neighbors degenerate — not merely a technical/compositional artifact (addressed by sensitivity analyses).
- A4: Broad AAV/CaMKIIa overexpression of Kcnip4 in mouse cortex is an acceptable, if imperfect, model of the cell-type-specific upregulation observed in human AD.
- A5: c-Fos and Arc are valid readouts of neuronal activation/hyperexcitability.
