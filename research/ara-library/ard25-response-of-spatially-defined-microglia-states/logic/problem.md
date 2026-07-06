# Problem Specification

## Observations

### O1: Microglia are functionally engaged in virtually all CNS disorders and expand via microgliosis
- **Statement**: Adult microglia are self-maintained, originate from prenatal yolk-sac macrophage progenitors, and undergo reactive expansion (microgliosis) in neuroinflammatory, neurodegenerative, neuropsychiatric and neuro-oncological disease.
- **Evidence**: Introduction, refs 1–7.
- **Implication**: Microglial reactivity/expansion is a general disease feature whose cellular sources and heterogeneity need to be resolved.

### O2: Distinct microglial states (DAM / MgnD) exist in AD but their kinetics and spatial relationships are undefined
- **Statement**: Single-cell studies defined disease-associated microglia (DAM) and a MgnD state with high Itgax, Clec7a, Trem2, Apoe, Lpl, Cst7; Trem2 signaling is essential for plaque-associated clustering and limiting AD pathology.
- **Evidence**: Introduction, refs 8–20.
- **Implication**: State definitions exist transcriptionally, but neither cellular kinetics nor spatial relationship to non-plaque microglia were addressed.

### O3: 5xFAD+ microglia show a bimodal spatial distribution (PAM vs non-PAM)
- **Statement**: In frontal cortices of 44-week-old female 5xFAD+ mice, Pu.1+Iba-1+ microglia exist either as PAM (contacting Methoxy-X04+ amyloid, cell bodies within a 30-µm radius) or non-PAM (ramified, distant, no plaque contact); PAM numbers are expanded while non-PAM numbers resemble 5xFAD- controls.
- **Evidence**: Fig 1a,b.
- **Implication**: Spatial position, not just transcriptional identity, defines microglial states in amyloid pathology.

### O4: Both PAM and non-PAM proliferate in 5xFAD+ mice
- **Statement**: BrdU incorporation reveals high proliferative capacity of both PAM and non-PAM in 5xFAD+ mice, whereas 5xFAD- microglia incorporate BrdU to a lesser extent.
- **Evidence**: Fig 1c.
- **Implication**: Proliferation is a shared response, so the two states must be distinguished by other properties (clonality, markers, chromatin, dynamics).

### O5: Environmental factors modify microglial behavior during amyloid pathology
- **Statement**: Gut microbiota, infection and age modify microglial behavior in amyloid models; chronic inflammation increases AD risk in patients; LPS increases plaque load and reduces Aβ uptake.
- **Evidence**: Introduction/Discussion, refs 23,24,36,37.
- **Implication**: Microglial states may be differentially modulated by peripheral stimuli — a candidate lever for therapy.

### O6: CSF1R ligands are dysregulated in human AD
- **Statement**: In patients with AD, CSF1 expression is increased in hippocampal regions while IL34 expression is downregulated; CSF1R is essential for microglial differentiation and survival.
- **Evidence**: Discussion, ref 43; refs 40–42.
- **Implication**: CSF1R and its two ligands (Csf1, IL-34) are candidate, differentially regulated therapeutic targets.

## Gaps

### G1: The cellular source and kinetics of PAM are unknown
- **Statement**: It is unknown whether PAM arise from local clonal expansion, from adjacent non-PAM, or from other sources, and how PAM clones grow over time.
- **Caused by**: O2, O3.
- **Existing attempts**: Single-color fate mapping documented microglial recruitment/accumulation at deposits (ref 2) but did not resolve non-PAM dynamics.
- **Why they fail**: Single-color labeling cannot establish clonal relationships or trace individual non-PAM→PAM conversion.

### G2: The functional role of non-PAM has been largely neglected
- **Statement**: DAM/PAM were considered the only pathophysiologically relevant microglia in neurodegeneration; the contribution of non-PAM (as the potential origin of PAM) was not explored.
- **Caused by**: O2.
- **Existing attempts**: Targeting PAM molecules (TREM2, APOE) gave conflicting disease outcomes.
- **Why they fail**: They did not consider the non-PAM compartment or the transition between states.

### G3: No reliable markers cleanly separate PAM from non-PAM beyond location
- **Statement**: Whether canonical DAM/homeostatic markers discriminate the two spatial states was untested.
- **Caused by**: O2, O3.
- **Existing attempts**: DAM markers (CD11c/Itgax, Apoe, Axl, Clec7a) and homeostatic markers (Tmem119, P2ry12) used broadly.
- **Why they fail**: Several markers (Clec7a, Apoe, Axl, P2RY12) do not separate PAM from non-PAM in this setting (Fig 2a).

### G4: It is unclear whether spatial states can be therapeutically targeted distinctly
- **Statement**: Whether PAM and non-PAM can be selectively engaged, and whether targeting the transition ameliorates amyloid pathology, was unknown.
- **Caused by**: G1, G2, and the differing transcriptomic/epigenomic landscapes of the two states.
- **Existing attempts**: Global CSF1R inhibition/depletion modulates microglia but depletes microglia in unaffected regions and other macrophages.
- **Why they fail**: Non-selective depletion risks losing homeostatic functions; ligand-specific engagement had not been tested on spatial states.

## Key Insight
- **Insight**: Spatial position defines two interconnected microglial states, and **individual non-PAM are the dynamic, environmentally responsive source of clonally expanding PAM**. Because non-PAM retain a homeostatic, more accessible Csf1r locus, engaging CSF1R with peripheral Csf1 (not IL-34) reshapes the non-PAM→PAM transition toward an amyloid-competent, phagocytic PAM phenotype and reduces amyloid burden.
- **Derived from**: O3, O4, O5, O6 combined with fate-mapping, epigenetic and single-cell evidence.
- **Enables**: A microglia-subset-specific therapeutic window during early amyloid pathology that modulates state transitions rather than depleting microglia.

## Assumptions
- A1: Cells within a 30-µm radius of and in direct contact with Methoxy-X04+ amyloid are PAM; ramified cells distant with no contact are non-PAM (operational spatial definition).
- A2: Same-colored Confetti+ cells in a local neighborhood, above a Monte Carlo random baseline, represent a clone derived by local proliferation.
- A3: CD11c (PAM) and Tmem119 (non-PAM) reliably report the two states for sorting and fate mapping.
- A4: Findings are established in **female** mice only; sex generalization is not assumed.
- A5: scRNA-seq and ATAC-seq were run as single (non-replicated) experiments; IHC/quantification experiments were replicated at least twice unless otherwise stated.
