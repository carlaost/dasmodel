# Claims

*Grounding: full-text. This is a narrative review; the claims below are the review's synthesized
assertions. Each is supported by primary studies the review cites (not original experiments by
these authors). `Proof` points to the verification plans in `experiments.md` that describe the
study designs establishing the claim. Numbers are copied verbatim from the review text; each
load-bearing number carries a `**Sources**` entry with the matched line.*

## C01: Microglial APOE4 drives an "enhanced synthesis–suppressed degradation" lipid imbalance that produces the LDAM phenotype
- **Statement**: The APOEε4 genotype disrupts the normal fatty-acid-synthesis/fatty-acid-oxidation equilibrium in microglia, promoting de novo lipogenesis and lipid-droplet (LD) accumulation by upregulating fatty acid synthesis (FAS) while suppressing autophagy-related genes (impairing lipophagy), and inhibiting fatty acid oxidation (FAO) both directly (mitochondrial structural/functional damage reducing β-oxidation capacity) and indirectly (proinflammatory polarization downregulating FAO-gene expression). This "enhanced synthesis–suppressed degradation" imbalance produces the pathological lipid-droplet-accumulating microglia (LDAM) phenotype.
- **Status**: supported
- **Falsification criteria**: Demonstration that APOEε4 microglia do not show elevated FAS/LD accumulation relative to APOEε3 microglia under matched conditions, or that FAO capacity is unaffected by APOE4 genotype.
- **Proof**: [E01]
- **Evidence basis**: §3.2 (refs 72-76); Figure 3 (triglyceride synthesis, ACSL1/PLIN2 upregulation under Aβ stimulation).
- **Interpretation**: This is the review's central mechanistic node — the biochemical description of *how* APOE4 converts microglia from lipid-homeostatic to lipid-pathological, from which downstream cholesterol overload, inflammation, and phagocytic defects are derived.
- **Dependencies**: none
- **Tags**: LDAM, lipid-droplets, FAS, FAO, mitochondrial-dysfunction, autophagy
- **Sources**: "enhanced synthesis–suppressed degradation" ← §3.2 «This "enhanced synthesis-suppressed degradation" imbalance ultimately leads to the formation of pathological LDAM» [input]

## C02: Microglial APOE4 induces cholesterol overload via the ER stress–ER Ca2+–SREBP2 pathway and impairs efflux, reducing Aβ degradation capacity
- **Statement**: Microglial APOE4 induces ER stress, leading to ER Ca2+ depletion and activation of the SREBP2 transcription factor, which promotes transcription of cholesterol-biosynthesis genes HMGCR and SQLE; concurrently, APOE4 impairs ABCA1 recycling, lysosomal function, and cholesterol efflux/metabolism. The resulting intracellular cholesterol accumulation reduces microglial capacity for Aβ degradation, and disrupted cholesterol homeostasis in lipid rafts affects amyloid precursor protein cleavage by α-, β-, and γ-secretases, promoting Aβ plaque formation.
- **Status**: supported
- **Falsification criteria**: Blocking the ER stress–SREBP2 axis (or restoring ABCA1 function) in APOE4 microglia failing to normalize cholesterol levels or Aβ-degradation capacity.
- **Proof**: [E02]
- **Evidence basis**: §4.1.2 (refs 51,96,97); Figure 3 (ER stress–Ca2+–SREBP2–HMGCR/SQLE pathway; reduced cholesterol efflux).
- **Interpretation**: Establishes cholesterol dysregulation — distinct from but coupled to triglyceride/LD accumulation (C01) — as a second, parallel lipid-metabolic lesion contributing to impaired Aβ clearance.
- **Dependencies**: C01
- **Tags**: cholesterol, SREBP2, ER-stress, ABCA1, Aβ-degradation, lipid-rafts

## C03: Microglial APOE4 directly activates inflammatory pathways through receptor-mediated and cell-intrinsic mechanisms
- **Statement**: APOE4 binds to LilrB3 on the microglial surface, upregulating type-I-interferon-stimulated genes (IFITM3, BST2, MX1, ISG15, STAT1), driving microglia into a proinflammatory state that hinders phagocytic function and contributes to Aβ deposition (Zhou et al.). Independently, in the basal state APOE4-expressing microglia show increased NLRP3 inflammasome activation and excessive ROS production, an effect further exacerbated by LPS/IFN-γ stimulation (increased TNF-α, IL-1β, NOS2, MCP1, especially in female mice); microglial nAPOE4(1-151) fragment increases TNF-α expression by inhibiting Cxorf56.
- **Status**: supported
- **Falsification criteria**: LilrB3 knockdown/knockout in APOE4 microglia failing to reduce interferon-stimulated-gene expression, or absence of elevated NLRP3/ROS in APOE4 vs APOE3 microglia under matched basal conditions.
- **Proof**: [E03]
- **Evidence basis**: §4.2 (refs 75, 112-114); Figure 4A.
- **Interpretation**: Establishes that microglial APOE4 activates neuroinflammation through mechanisms independent of, and in addition to, its lipid-metabolic effects (contrast with C04) — i.e., a direct receptor/intrinsic inflammatory arm.
- **Dependencies**: none
- **Tags**: LilrB3, interferon-stimulated-genes, NLRP3, ROS, Cxorf56, TNF-α, sex-differences

## C04: APOE4-induced lipid metabolic reprogramming further amplifies neuroinflammation
- **Statement**: Metabolic reprogramming of APOE4-expressing microglia (enhanced glycolysis, inhibited tricarboxylic acid cycle, carbon flux redirected to lipid synthesis) increases release of proinflammatory lipid mediators (prostaglandins, arachidonic-acid metabolites) and activates neuroinflammatory pathways; accumulated lipid peroxides and cholesterol activate NF-κB signaling, creating a self-reinforcing cycle of cytokine production and metabolic dysfunction; accumulated lipids also enhance MHC-II-dependent antigen presentation, hyperactivating T cells. APOE4 microglia secrete more oxysterol 25-hydroxycholesterol (25-HC) and IL-1β following LPS treatment, and 25-HC further increases IL-1β secretion.
- **Status**: supported
- **Falsification criteria**: Blocking the glycolytic shift or NF-κB activation in APOE4 microglia failing to reduce proinflammatory lipid mediator release or cytokine secretion.
- **Proof**: [E04]
- **Evidence basis**: §4.2 (refs 78, 73, 100, 111); Figure 4A.
- **Interpretation**: Completes the bidirectional "metabolism–inflammation" crosstalk the review names explicitly — lipid dysregulation (C01, C02) is not merely a consequence but an active amplifier of neuroinflammation (C03), forming a self-reinforcing loop.
- **Dependencies**: C01, C03
- **Tags**: glycolysis, TCA-cycle, NF-κB, MHC-II, 25-hydroxycholesterol, prostaglandins

## C05: APOE4 impairs microglial phagocytic clearance of Aβ through multiple convergent mechanisms
- **Statement**: APOE4 induces mitochondrial dysfunction and compromises pseudopod extension (via altered membrane fluidity from lipid accumulation) coupled with downregulated TREM2 expression, collectively impairing phagocytic capacity. APOE4 also increases formation of fibrillar aggregates within microglia that nucleate Aβ plaque formation, and specifically suppresses Aβ42 clearance by disrupting ITGB8–TGFβ signaling (selective ablation of microglial APOE4 restores phagocytic function and reduces plaque burden). In female APOEε4-carrying AD patients, APOE4-expressing neutrophils upregulate IL-17F, which interacts with microglial IL-17RA to disrupt Aβ clearance; interrupting IL-17F/IL-17RA signaling ameliorates cognitive deficits and reduces Aβ deposition.
- **Status**: supported
- **Falsification criteria**: Genetic ablation of microglial APOE4, or blockade of ITGB8–TGFβ or IL-17F/IL-17RA signaling, failing to restore phagocytic function or reduce plaque burden.
- **Proof**: [E05]
- **Evidence basis**: §4.3 (refs 74,118,42,85,119); Figure 4B.
- **Interpretation**: Consolidates several independently reported receptor/signaling axes (TREM2, ITGB8-TGFβ, IL-17F/IL-17RA) into a single "phagocytosis-impairment" node downstream of the lipid (C01,C02) and inflammatory (C03,C04) lesions.
- **Dependencies**: C01, C03
- **Tags**: TREM2, ITGB8-TGFβ, IL-17F, IL-17RA, phagocytosis, sex-differences, Aβ42

## C06: APOE4 impairs tau clearance and promotes pathological tau/synapse propagation
- **Statement**: APOE4-driven LD accumulation compromises plasma membrane integrity and impairs endosomal–lysosomal system functionality, attenuating tau-protein processing/degradation and causing abnormal intracellular p-tau accumulation; accumulated p-tau is subsequently released via exosomes, facilitating intercellular propagation. Increased microglial phagocytosis of pathological synapses was observed in AD patients carrying APOEε4, particularly pronounced near Aβ plaques.
- **Status**: supported
- **Falsification criteria**: Restoring lysosomal function in APOE4 microglia failing to reduce intracellular p-tau accumulation or exosomal tau release; absence of elevated synaptic phagocytosis in APOEε4 carriers versus non-carriers.
- **Proof**: [E06]
- **Evidence basis**: §4.3 (refs 51,68,121,122,125,126); Figure 4B.
- **Interpretation**: Extends the phagocytosis-impairment node (C05) from Aβ specifically to tau and synapses, and reframes microglia as active propagators (not just passive failed-clearers) of tau pathology via exosome release and pathological synaptic pruning.
- **Dependencies**: C01, C05
- **Tags**: tau, p-tau, exosomes, lysosomal-dysfunction, synaptic-phagocytosis, cognitive-decline

## C07: APOE4 astrocytes exhibit SREBP2/PPARγ-driven lipid dysregulation and GPC-4/LRP1-mediated tau propagation
- **Statement**: APOE4 astrocytes exhibit aberrant SREBP2 activation, increasing de novo cholesterol synthesis despite lysosomal-dysfunction-induced accumulation, involving upregulated lipid-metabolism genes but downregulated transport genes, potentially mediated by reduced PPARγ expression; this pathological cholesterol accumulation disrupts lysosome-dependent mitophagy, causing mitochondrial dysfunction and early AD energy deficits. APOE4 astrocytes also accumulate enlarged, oxidation-prone lipid droplets enriched with unsaturated triglycerides while secreting poorly lipidated lipoproteins that inefficiently support neuronal lipid demands. Additionally, APOE4 astrocytes upregulate glypican-4 (GPC-4), increasing LRP1 membrane trafficking to promote tau propagation and hyperphosphorylation, and impair APOE4-mediated miRNA transfer to neurons.
- **Status**: supported
- **Falsification criteria**: APOE4 astrocytes failing to show elevated SREBP2 activity, cholesterol accumulation, or GPC-4/LRP1 upregulation relative to APOE3 astrocytes under matched conditions.
- **Proof**: [E07]
- **Evidence basis**: §3.1 (refs 58,59,52,60-64); Figure 2A.
- **Interpretation**: Establishes that the microglia-centric mechanism (C01-C06) is not the sole cell-type affected — a parallel, partially independent astrocytic lipid-tau pathway also contributes to AD progression, motivating the review's comparative cell-type framing.
- **Dependencies**: none
- **Tags**: astrocytes, SREBP2, PPARγ, mitophagy, GPC-4, LRP1, tau-propagation

## C08: APOE4 neurons show lysosomal dysfunction, lipofuscin accumulation, and lipotoxicity driving tau aggregation
- **Statement**: Excessive binding of APOE4 to LDLR increases neuronal lipid uptake, causing lysosomal dysfunction, lipofuscin accumulation, and impaired autophagy, which subsequently triggers tau protein aggregation and brain cell death. APOE4-expressing neurons exhibit deficient fatty-acid storage in lipid droplets, leading to pathological accumulation of free fatty acids and increased lipotoxicity risk; neighboring astrocytes' lipid transport/oxidation capacity is impaired by APOE4, particularly in the hippocampus. APOE4 also promotes ABCA1 degradation, reduces cholesterol efflux, and activates mTORC1-mediated senescence pathways, impairing synaptic plasticity; APOE4 undergoes neuron-specific proteolysis generating neurotoxic fragments that destabilize the cytoskeleton and exacerbate tau pathology.
- **Status**: supported
- **Falsification criteria**: Blocking APOE4-LDLR binding failing to reduce lysosomal dysfunction/lipofuscin accumulation, or absence of elevated free-fatty-acid accumulation in APOE4 vs APOE3 neurons.
- **Proof**: [E08]
- **Evidence basis**: §3.1 (refs 65-71); Figure 2B.
- **Interpretation**: Completes the cell-type-specific survey (with C07) that the review uses to argue microglia bear the most pronounced APOE4 burden (O4) — by contrast to the narrower, largely cell-autonomous neuronal and astrocytic lesions.
- **Dependencies**: none
- **Tags**: neurons, LDLR, lipofuscin, autophagy, lipotoxicity, mTORC1, senescence, proteolytic-fragments

## C09: APOE4 microglia diversify into distinct pathological transcriptional subtypes (LDAM, DAM, MGnD, TIM)
- **Statement**: Single-cell sequencing reveals that microglia exhibit distinct subtypes mediated by cellular-metabolism reprogramming. LDAM is the canonical APOE4-driven pathological subtype (dysregulated lipid metabolism, proinflammatory state, impaired phagocytic function). Disease-associated microglia (DAM) show elevated lipid-metabolism/phagocytosis genes; APOE4 microglia show DAM-like features (increased aerobic glycolysis and Hif1a expression, impaired Aβ uptake). A phagocytic/proinflammatory-gene-enriched subset clusters around neuroinflammatory plaques, driving conversion via the APOE-TREM2-TYROBP axis. The TREM2-APOE pathway also mediates transition to neurodegenerative microglia (MGnD), which are neuroprotective via elimination of apoptotic neurons, but APOE4 exacerbates neurodegeneration by activating ITGB8-TGFβ signaling and inhibiting MGnD function. Terminally inflammatory microglia (TIMs), another APOE4-associated exhausted subtype, display profound Aβ clearance deficits in AD patients and mouse models.
- **Status**: supported
- **Falsification criteria**: Single-cell profiling failing to distinguish LDAM/DAM/MGnD/TIM as transcriptionally distinct populations, or failing to find APOE4-genotype association with these subtypes.
- **Proof**: [E09]
- **Evidence basis**: §3.2 (refs 72,73,81,83-86); Figure 2C.
- **Interpretation**: Provides the taxonomic/phenotypic vocabulary underlying claims C01-C06 — the "microglial dysfunction" described mechanistically corresponds to specific, independently characterized transcriptional states.
- **Dependencies**: C01
- **Tags**: LDAM, DAM, MGnD, TIM, single-cell-sequencing, TREM2-TYROBP, ITGB8-TGFβ

## C10: TREM2-R47H's effect on microglial lipid-droplet accumulation is microenvironment-dependent (in vivo vs in vitro)
- **Statement**: In AD model mice, human-iPSC-derived microglial lipid-droplet accumulation largely depends on microglial reactivity and plaque proximity, and is impaired by the TREM2-R47H mutation: TREM2-R47H-mutant microglia showed reduced LD accumulation in vivo, decreased plaque reactivity, and decreased plaque-associated APOE secretion — whereas the same mutation exacerbated LD accumulation in vitro.
- **Status**: supported
- **Falsification criteria**: Direct side-by-side in vivo/in vitro comparison of TREM2-R47H microglia failing to show opposite-direction LD-accumulation effects.
- **Proof**: [E10]
- **Evidence basis**: §4.1.1 (refs 91,92); Figure 3 legend note on TREM2-R47H.
- **Interpretation**: A genuinely nuanced, non-monotonic finding the review does not smooth over — it explicitly frames this as evidence for "the critical regulatory role of the environmental context in microglial function," a caution against overgeneralizing genotype-phenotype relationships from single-context models.
- **Dependencies**: C01
- **Tags**: TREM2-R47H, context-dependence, chimeric-model, in-vivo-vs-in-vitro

## C11: A microglia-specific glycolysis–lipid metabolic compensatory coupling exists via HK2 inhibition
- **Statement**: In the context of AD, expression of the glycolytic enzyme hexokinase 2 (HK2) is upregulated in microglia; pharmacological inhibition of HK2 activates lipoprotein lipase, increasing lipid metabolism, thereby sustaining ATP production and promoting Aβ clearance. This glycolytic-lipid metabolic coupling appears to be microglia-specific, as it has not been observed in other brain cells.
- **Status**: supported
- **Falsification criteria**: HK2 inhibition in other CNS cell types (astrocytes, neurons) producing the same lipoprotein-lipase activation and Aβ-clearance enhancement, or failure to replicate the effect in microglia.
- **Proof**: [E11]
- **Evidence basis**: §3.2 (ref 80).
- **Interpretation**: A rare *protective*/compensatory finding within an otherwise pathological narrative — the review flags it as a distinctive, cell-type-restricted metabolic flexibility that could inform a therapeutic angle distinct from simply blocking lipid synthesis.
- **Dependencies**: none
- **Tags**: HK2, lipoprotein-lipase, ATP, Aβ-clearance, cell-type-specificity
- **Sources**: "has not been observed in other brain cells" ← §3.2 «This glycolytic-lipid metabolic coupling appears to be microglia specific, as it has not been observed in other brain cells (80)» [input]

## C12: APOEε4 confers large, dose-dependent AD risk and is common in the population
- **Statement**: A single APOEε4 allele confers an approximately 3- to 4-fold greater risk of developing AD than non-carriers, while two APOEε4 alleles confer a 9- to 15-fold greater risk. The APOEε4 carrier rate in the general population is approximately 23.9% (2.1% ε4/ε4, 20.6% ε3/ε4, 2.3% ε2/ε4), and nearly all APOEε4 homozygotes display AD-related pathologic features.
- **Status**: supported
- **Falsification criteria**: Large, adequately powered epidemiological studies failing to replicate a dose-dependent APOEε4-AD risk gradient of this magnitude.
- **Proof**: [E12]
- **Evidence basis**: §1 (ref 7); §2.2 (ref 32, Figure 1A; ref 33).
- **Interpretation**: Provides the epidemiological/genetic-risk foundation motivating the entire mechanistic review; establishes APOEε4 as a high-penetrance, high-prevalence risk factor rather than a rare-variant curiosity.
- **Dependencies**: none
- **Tags**: epidemiology, genetic-risk, allele-dose, carrier-frequency
- **Sources**: "3- to 4-fold ... 9- to 15-fold" ← §1 «individuals with a single APOEε4 allele face an approximately 3- to 4-fold greater risk of developing AD than noncarriers do, while those with two APOEε4 alleles have a 9- to 15-fold greater risk (7)» [input]; "23.9%, with 2.1% APOEε4/ε4, 20.6% APOEε3/ε4, and 2.3% APOEε2/ε4" ← §2.2 «The carrier rate of APOEε4 in the general population is approximately 23.9%, with 2.1% APOEε4/ε4, 20.6% APOEε3/ε4, and 2.3% APOEε2/ε4 (32) (Figure 1A)» [input]

## C13: No drug currently exists that specifically corrects APOE4-driven microglial lipid abnormalities, despite a broad candidate pipeline
- **Statement**: The review catalogues 14 therapeutic strategies (Table 1) across four target pathways — lipid metabolism (TRPV1/capsaicin; LXR agonist GW3965/CS-6253; bexarotene), neuro-inflammation (NLRP3 inhibitors JC-124/dihydromyricetin/DAPPD/dapansutrile; ubiquitin ligase COP1 modulators; resveratrol/curcumin; dimethyl malonate), phagocytosis (sodium rutin/desloratadine; DW14006; AL002c), and APOE4 itself (Aβ12-28p/CN-105; HAE-4 antibody; LX1001 AAV gene therapy; CRISPR-Cas9) — several of which have reached phase I/II clinical trials (bexarotene: NCT01782742; AL002c: NCT03635047, NCT04592874; LX1001: NCT03634007, NCT05400330). Despite this, "no effective drugs currently exist to specifically correct APOE4-driven lipid metabolic abnormalities in microglia," and translating animal/cellular findings into effective human therapies "remains challenging."
- **Status**: supported (as a gap/limitation claim)
- **Falsification criteria**: Approval or late-phase trial success of an agent specifically validated to correct APOE4-driven microglial lipid metabolism (as opposed to broader neuroinflammation, phagocytosis, or APOE4-lowering effects).
- **Proof**: [E13]
- **Evidence basis**: §5 (Table 1; refs 96,100,129-158).
- **Interpretation**: The review's concluding, self-aware limitation: mechanistic understanding (C01-C11) has outpaced translational therapeutic precision; most agents act on adjacent nodes (general microglial function, APOE4 genotype broadly) rather than the microglial-lipid axis specifically.
- **Dependencies**: C01, C02, C05
- **Tags**: therapeutics, clinical-trials, translational-gap, TRPV1, LXR, bexarotene, NLRP3, AL002c, LX1001, CRISPR
- **Sources**: "no effective drugs currently exist to specifically correct APOE4-driven lipid metabolic abnormalities in microglia" ← §5 «Despite growing interest in microglial dysfunction and APOE4 as therapeutic targets for AD, no effective drugs currently exist to specifically correct APOE4-driven lipid metabolic abnormalities in microglia» [input]; "translating these findings into effective therapies in humans remains challenging" ← §5 «Although some progress has been made in the study of microglial dysfunction as a therapeutic target for AD in animal models and at the cellular level, translating these findings into effective therapies in humans remains challenging» [input]
