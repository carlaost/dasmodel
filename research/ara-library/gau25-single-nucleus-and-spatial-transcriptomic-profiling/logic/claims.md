# Claims

All numbers are copied exactly from the paper PDF (Gaur, Bryois, Calini et al., *Nature
Communications*, 2025, 16:10395). This is an empirical/observational biology paper (snRNA-seq +
spatial in-situ sequencing, not a training-run paper), so reported statistics carry the `[result]`
tag and are grounded to the Results/Methods/Figure-caption text whose verbatim line was opened and
confirmed, with the printed page number (matching the PDF page footer, 1-17) as the pin. `Status:
supported` is used where the paper presents its own generated result as an established finding of
this study.

## C01: Multiple neuronal subpopulations show altered proportional abundance with Braak stage in gray matter (GM), with a THEMIS+/POSTN+ deep-layer subgroup appearing resistant
- **Statement**: In GM, 2 of 5 total RORB+ glutamatergic subpopulations (both also IL1RAPL2+), a SPARCL1+ glutamatergic subset, COL5A2+ (Layer 4) and GLIS3+ (Layer 3) glutamatergic subpopulations, GNAL+ and TLL1+ glutamatergic subpopulations, PVALB+ GABAergic neurons, and SPARCL1+ GABAergic neurons all show lower proportions at late Braak stages, whereas THEMIS+/POSTN+ deep-layer (L5-6) glutamatergic neurons and a SST+/THSD7B+/TRHDE+ GABAergic subpopulation are overrepresented at Braak stage 5/6.
- **Status**: supported
- **Falsification criteria**: A replication ANCOM-BC trait-association analysis on an independent paired GM/WM temporal-cortex cohort finding no significant proportional depletion of RORB+/IL1RAPL2+, SPARCL1+, COL5A2+, GLIS3+, GNAL+, TLL1+ glutamatergic or PVALB+/SPARCL1+ GABAergic subpopulations at late Braak stage, or no enrichment of THEMIS+/POSTN+ neurons, would refute this claim.
- **Proof**: [E01]
- **Evidence basis**: Fig. 2a-b (differential abundance plot and box plots of neuronal subpopulations, GM/WM samples from n=36 individuals).
- **Interpretation**: The consistent depletion pattern across several unrelated glutamatergic and GABAergic subtypes, contrasted with the resistance of the THEMIS+/POSTN+ subgroup (which co-expresses NR4A2/NTNG2, markers of a separately reported tangle-poor L6 population), nominates THEMIS+/POSTN+ neurons as a candidate AD-resilient excitatory subclass.
- **Sources**:
  - "Out of 5 total RORB+ glutamatergic subpopulations, two were found to be less prevalent in later Braak stages compared to earlier stages; interestingly, both of these RORB+ subpopulations express IL1RAPL2." ← Results §"Neuronal and glial subpopulations with lower prevalence...", p.3 of 17 [result]
  - "we also observed a glutamatergic subset with high levels of SPARCL1 was lower in the GM in donors at advanced Braak stages" ← same section, p.3 of 17 [result]
  - "Other subpopulations with lower proportions at later Braak stages included those marked by COL5A2 (putatively in Layer 4) and GLIS3 (putatively in Layer 3)." ← same section, p.3 of 17 [result]
  - "we also observed lower proportions of GNAL+ and TLL1+ glutamatergic subpopulations at Braak stages 5/6" ← same section, p.3 of 17 [result]
  - "we found that a few glutamatergic neuron populations from the deep layers of the cortex (L5-6) in GM, marked by THEMIS and POSTN, are overrepresented at later Braak stages" ← Results §"Specific neuronal and glial subclusters selectively enriched...", p.3 of 17 [result]
  - "a unique SST+/THSD7B+ GABAergic subpopulation marked by Thyrotropin Releasing Hormone Degrading Enzyme (TRHDE) was also enriched in Braak stage 5/6" ← same section, p.3 of 17 [result]
  - "These included parvalbumin (PVALB) neurons (Fig. 2a), which have been reported to be selectively depleted in the frontal cortex of Alzheimer's disease mouse models. SPARCL1+ GABAergic neurons also showed depleted proportions in GM." ← Results §"Neuronal and glial subpopulations with lower prevalence...", p.3 of 17 [result]
- **Dependencies**: none
- **Tags**: cell-proportion, ANCOM-BC, Braak-stage, gray-matter, neuronal-vulnerability

## C02: Glial subpopulations show altered proportional abundance with Braak stage in gray matter, with RPL19+ microglia depleted and MGP+ pericytes/TNC+ astrocytes/HSPA1A+ OPCs enriched at late stage
- **Statement**: In GM, RPL19+ microglia are "significantly lower in intermediate and late Braak stages" (the strongest glial signal reported), while HSPA1A+ ("heat shock protein specific") OPCs, MGP+ pericytes, and TNC+ astrocytes all show higher proportions in individuals at later Braak stages.
- **Status**: supported
- **Falsification criteria**: A replication finding no significant depletion of RPL19+ microglia or no enrichment of TNC+ astrocytes/MGP+ pericytes/HSPA1A+ OPCs with Braak stage in GM would refute this claim.
- **Proof**: [E01]
- **Evidence basis**: Fig. 2c-d (differential abundance plot and box plots of glial subpopulations, GM/WM samples from n=36 individuals).
- **Interpretation**: Because this is a cross-sectional study, the authors explicitly note it "does not provide information as to whether these signatures are protective, reactionary, or pathological" — the TNC+ astrocyte enrichment is interpreted (via prior mouse-lesion and human EC/SFG literature) as a candidate marker of astrocytic reactivity to neuronal damage rather than a causal driver.
- **Sources**:
  - "we found associations between microglial subsignatures with later Braak stages. The strongest signal was in RPL19+ microglia, which were significantly lower in intermediate and late Braak stages in GM, possibly reflecting the loss of a protective type of microglia (Fig. 2c, d)." ← Results §"Neuronal and glial subpopulations with lower prevalence...", p.3 of 17 [result]
  - "Among glial cells, OPCs specific to heat shock protein were higher in GM in individuals with more advanced AD pathology. A similar pattern was observed in MGP+ pericytes and TNC+ astrocytes, whose proportions were higher in individuals at later Braak stages" ← Results §"Specific neuronal and glial subclusters selectively enriched...", p.3 of 17 [result]
- **Dependencies**: none
- **Tags**: cell-proportion, ANCOM-BC, Braak-stage, gray-matter, glial-reactivity

## C03: White matter shows distinct, and in one case opposite, subcluster-Braak-stage associations compared to gray matter
- **Statement**: In WM, TSHZ2+ endothelial cells and HSPA1A+ OPCs show higher proportions at advanced Braak stages (the latter resembling the GM finding), while RPL19+ microglia and TAGLN+ pericytes are lower at intermediate and advanced Braak stages respectively; PVALB+/TMEM132C+ and PVALB+/SPARCL1+ GABAergic subpopulations are lower in WM at advanced Braak stages (paralleling GM), but RORB+/IL1RAPL2+ glutamatergic neurons show a different, opposite-direction pattern in WM — higher proportions at intermediate Braak stages 2/4 (vs. lower proportions in GM at late stage) — and LAMP5+/CHST9+ GABAergic neurons show lower prevalence in WM at Braak stages 5-6.
- **Status**: supported
- **Falsification criteria**: A replication finding the RORB+/IL1RAPL2+ WM pattern is concordant (not opposite in direction) with the GM pattern, or finding no WM-specific TSHZ2+/HSPA1A+ enrichment, would refute the claim that WM has a tissue-compartment-specific (not merely attenuated GM-mirroring) Braak-stage association profile.
- **Proof**: [E01]
- **Evidence basis**: Fig. 2 legend and body text (WM-restricted panels within Fig. 2a-d).
- **Interpretation**: The opposite-direction RORB+/IL1RAPL2+ pattern is interpreted as potentially reflecting either mislocalization of these neurons from GM to WM in disease, or region-specific differences in selective vulnerability between GM and WM.
- **Sources**:
  - "Endothelial cells marked by TSHZ2 were present at higher proportions in donors at advanced Braak stages (Fig. 2c), as were OPCs with high expression of heat-shock proteins; this latter finding resembles the same finding in GM." ← Results §"Neuronal and glial subclusters selectively enriched and depleted in white matter...", p.4 of 17 [result]
  - "Finally, RPL19+ microglia and TAGLN+ pericytes were lower in individuals at intermediate and advanced Braak stages, respectively; RPL19+ microglia were one of the cell signatures showing the same trend in WM and GM" ← same section, p.4 of 17 [result]
  - "Similar to our findings in GM, PVALB+/TMEM132C+ and PVALB+/SPARCL1+ subpopulations were lower in WM in donors at advanced Braak stages (Fig. 2a, b and Supplementary Data 5). By contrast, RORB+/IL1RAPL2+ glutamatergic subpopulations showed a different pattern in WM, exhibiting higher proportions at intermediate Braak stages 2/4" ← Results, p.5 of 17 [result]
  - "GABAergic neurons expressing LAMP5 ... and CHST9 ... showed lower prevalence in WM in late Braak stages (5-6)" ← Results, p.5 of 17 [result]
- **Dependencies**: none
- **Tags**: cell-proportion, ANCOM-BC, Braak-stage, white-matter, tissue-specificity

## C04: Key subcluster-Braak-stage associations (THEMIS+/POSTN+ resilience; PVALB+/TMEM132C+, TAGLN+, RPL19+ vulnerability) replicate across independent brain regions, studies, and two much larger external cohorts (SEA-AD MTG n=84; ROSMAP PFC n=424)
- **Statement**: After integrating the TC dataset with entorhinal cortex, prefrontal cortex, superior frontal gyrus, and PFC-white-matter studies via Harmony, THEMIS+/POSTN+ deep-layer glutamatergic neurons were "consistently overrepresented in late Braak stages" across brain regions; PVALB+/TMEM132C+ GABAergic neurons were "lower at advanced Braak stages in all brain regions we examined"; TAGLN+ pericytes and RPL19+ microglia were lower, and HSPA1A+ OPCs enriched, in Braak stages 5/6 across multiple cortical regions. Using Cell Type Mapper to transfer TC subcluster labels, trait-association analysis in the SEA-AD MTG cohort (84 individuals) again found THEMIS+/POSTN+ neurons consistently overrepresented at late Braak stage, and analysis of an independent ROSMAP PFC cohort (424 individuals) again found THEMIS+/POSTN+ neurons enriched in advanced AD pathology and TAGLN+ pericytes lower at advanced Braak stages.
- **Status**: supported
- **Falsification criteria**: Failure of the THEMIS+/POSTN+ enrichment or PVALB+/TMEM132C+ depletion to replicate in either the SEA-AD MTG (n=84) or ROSMAP PFC (n=424) cohort after label transfer would refute the claim of cross-region/cross-cohort generalizability.
- **Proof**: [E02]
- **Evidence basis**: Results text citing Supplementary Fig. 3 (not included in the provided PDF) and Supplementary Data 6-10 (external files, not provided).
- **Interpretation**: Replication in two independently collected, substantially larger cohorts (MTG n=84, PFC n=424) than the primary 40-individual TC cohort meaningfully increases confidence that these are general cortical AD-pathology correlates rather than idiosyncratic to the TC cohort.
- **Sources**:
  - "We found that THEMIS+/POSTN+ deep layer glutamatergic neurons were consistently overrepresented in late Braak stages, suggesting that these deep layer neurons may be generally resistant to AD pathology across the cortex" ← Results §"Consistency of subcluster associations...", p.5 of 17 [result]
  - "Conversely, PVALB+/TMEM132C+ GABAergic neurons were lower at advanced Braak stages in all brain regions we examined." ← same section, p.5 of 17 [result]
  - "we performed trait association analyses in the middle temporal gyrus (MTG) from 84 individuals in Seattle Alzheimer's Disease Brain Cell Atlas (SEA-AD) consortium" and "found that the potentially resilient THEMIS+/POSTN+ glutamatergic neurons were consistently overrepresented in late Braak stages of AD in the MTG as well" ← same section, p.5 of 17 [result]
  - "we included an additional study of the prefrontal cortex (PFC) from the ROSMAP cohort (424 individuals)" and "again found that THEMIS+/POSTN+ glutamatergic neurons were enriched in advanced AD pathology ... Along with this, TAGLN+ pericytes were also lower in advanced Braak stages" ← same section, p.5 of 17 [result]
- **Dependencies**: C01, C02, C03
- **Tags**: cross-region-replication, cross-cohort-replication, Harmony-integration, cell-type-mapper

## C05: Pseudobulk differential expression is minimal at early Braak stage but extensive and highly cell-type-specific at late Braak stage
- **Statement**: Braak 2-4 vs. Braak 0-1 (early stage) yielded only 17 FDR-adjusted-significant (p<0.05) DEGs, all restricted to GABAergic neurons, oligodendrocytes, and OPCs, with only 10 genes differentially affected between GM and WM at this early stage; Braak 5-6 vs. Braak 0-1 (late stage) yielded 1230 FDR-significant DEGs, of which ~90% (1102/1230) were specific to a single cell type.
- **Status**: supported
- **Falsification criteria**: A replication finding a comparably large number of early-Braak-stage DEGs (i.e., not a sharp early/late asymmetry), or finding the majority of late-Braak DEGs shared across multiple cell types (not ~90% cell-type-specific), would refute the claim of a late-stage-concentrated, predominantly cell-autonomous transcriptional response.
- **Proof**: [E03]
- **Evidence basis**: Fig. 3a (number of DEGs per cell type and per GM/WM-interaction contrast, by Braak-stage comparison).
- **Interpretation**: The cell-type specificity is interpreted by the authors as consistent with either genes being exclusively expressed in a particular cell type, or with a cell-type-specific transcriptional response to AD pathology; the sharp early/late asymmetry is interpreted as expected given that "cortical pathologies in the TC are only observed at later Braak stages in AD."
- **Sources**:
  - "We found a few expression changes in the early stages of AD (Braak 2-4 vs Braak 0-1), with only 17 genes differentially expressed (FDR-adjusted p-value < 0.05), and all of these were in GABAergic neurons, oligodendrocytes, and OPCs" ← Results §"Differential expression analysis identifies additional cell type-specific genes...", p.5 of 17 [result]
  - "We found only a few genes that were affected at early Braak stage differentially between GM and WM (10 genes, FDR-adjusted p-value < 0.05, Supplementary Data 11)." ← same section, p.5-6 of 17 [result]
  - "we found a large number of differentially expressed genes (1230 at FDR-adjusted p-value < 0.05) in late Braak stages (Braak 5-6 vs Braak 0-1)" ← same section, p.6 of 17 [result]
  - "Interestingly, the majority of differentially expressed genes were specific to individual cell types (~90%, 1102/1230)." ← same section, p.6 of 17 [result]
- **Dependencies**: none
- **Tags**: differential-expression, pseudobulk, glmmTMB, Braak-stage, cell-type-specificity

## C06: Late-stage AD pathology affects gene expression differently between gray and white matter for a specific gene subset (644 genes), including FCER1G, APOE, and ABCA7
- **Statement**: 644 genes (FDR-adjusted p<0.05) were affected differently by late-stage (Braak 5-6) pathology in GM vs. WM; FCER1G (an AD genetic-risk-associated gene) was lower in GM but higher in WM at late Braak stage; APOE was differentially expressed in endothelial cells between GM and WM, downregulated in both tissues but with a greater magnitude of decrease in GM than WM; ABCA7 was significantly higher in GM microglia than in WM microglia.
- **Status**: supported
- **Falsification criteria**: A replication finding no significant GM-vs-WM interaction DEGs at late Braak stage, or finding FCER1G/APOE/ABCA7 patterns reversed or absent, would refute the claim of tissue-compartment-specific transcriptional dysregulation.
- **Proof**: [E03]
- **Evidence basis**: Fig. 3a (644-gene count), Fig. 3g (FCER1G boxplot, adjusted p=4.5e-07), Fig. 3h (APOE boxplot, adjusted p=0.04).
- **Interpretation**: The APOE finding is interpreted as suggesting "compartment (gray and white matter)-specific alterations in the vasculature in AD" despite APOE's more typical association with microglia/astrocytes; collectively the tissue-interaction DEGs are read as evidence that "cross-tissue differential expression analysis at the cell type level will be necessary to fully capture the transcriptional changes associated with AD."
- **Sources**:
  - "We also found that 644 genes (FDR adjusted p-value < 0.05) were affected differently by late stage pathology in gray vs white matter (Fig. 3a)." ← Results §"Differential expression analysis identifies additional cell type-specific genes...", p.6 of 17 [result]
  - "FCER1G, a gene associated with AD genetic risk was affected differentially in late Braak stages in gray (lower) vs white matter (higher) (Fig. 3g), suggesting that transcriptional changes in AD can differ between different brain tissue types." ← same section, p.6 of 17 [result]
  - "APOE, a well-known AD risk gene belonging to pathways related to amyloid formation, is differentially expressed in endothelial cells between gray and white matter cells (Fig. 3h). ... the difference between controls and cases was more pronounced in the GM compared to the WM, though APOE levels were downregulated in both GM and WM. Specifically, the magnitude of the decrease was greater in the GM than in the WM." ← same section, p.6 of 17 [result]
  - "ABCA7, another AD risk gene, was significantly higher in GM microglia than in WM microglia (Supplementary Data 11)." ← same section, p.6 of 17 [result]
  - adjusted P-value = 4.5e-07 (FCER1G-Microglia) ← Fig. 3g panel label, p.6 of 17 [result]
  - adjusted P-value = 0.04 (APOE-Endothelial) ← Fig. 3h panel label, p.6 of 17 [result]
- **Dependencies**: C05
- **Tags**: differential-expression, tissue-interaction, gray-white-matter, APOE, FCER1G, ABCA7

## C07: Genes upregulated in glutamatergic neurons at late Braak stage, and those differentially affected between GM and WM in glutamatergic neurons, are significantly more evolutionarily constrained (lower LOEUF) than non-differentially-expressed genes
- **Statement**: Comparing LOEUF (loss-of-function observed/expected upper bound fraction) scores by two-sided Wilcoxon rank-sum test (no multiple-testing correction), genes upregulated ("Up") in glutamatergic neurons at Braak 5-6 vs. FDR≥5% (non-DE) genes differ at p=3.5e-09, and genes differentially affected by the Braak5-6 x Temporal-Cortex tissue interaction ("Up") vs. FDR≥5% genes differ at p=1.8e-05; the corresponding "Down"-gene comparisons are p=0.95 (Braak 5-6, not significant) and p=0.0083 (Braak5-6 x Temporal Cortex).
- **Status**: supported
- **Falsification criteria**: A replication finding no significant LOEUF difference between late-Braak-upregulated glutamatergic-neuron genes and non-DE genes would refute the claim that these genes are under stronger evolutionary constraint.
- **Proof**: [E04]
- **Evidence basis**: Fig. 3d (LOEUF violin/dot plots with p-values for Up/Down vs. FDR≥5% genes, Braak 5-6 and Braak5-6*Temporal-Cortex comparisons; GM/WM samples from n=39 individuals).
- **Interpretation**: The authors interpret greater constraint among late-Braak-upregulated glutamatergic genes as consistent with these genes serving "essential functions" and possibly playing "an important developmental role," speculating this reflects glutamatergic neurons upregulating survival-relevant genes under pathological stress.
- **Sources**:
  - "upregulated genes in late Braak stages (5-6) in glutamatergic neurons, as well as genes differentially affected between gray and white matter in glutamatergic neurons, were significantly more constrained than non-differentially expressed genes (Fig. 3d)" ← Results §"Differential expression analysis identifies additional cell type-specific genes...", p.7 of 17 [result]
  - p=3.5e-09 (Braak5-6, Up vs. FDR≥5%); p=0.95 (Braak5-6, Down vs. FDR≥5%) ← Fig. 3d panel labels, p.6 of 17 [result]
  - p=1.8e-05 (Braak5-6*Temporal Cortex, Up vs. FDR≥5%); p=0.0083 (Braak5-6*Temporal Cortex, Down vs. FDR≥5%) ← Fig. 3d panel labels, p.6 of 17 [result]
- **Dependencies**: C05
- **Tags**: LOEUF, gene-constraint, glutamatergic-neurons, Wilcoxon

## C08: Late-stage differentially expressed genes show cell-type-specific enrichment for distinct, AD-relevant biological pathways
- **Statement**: Among Braak5-6-vs-0-1 DEGs, genes involved in "negative regulation of amyloid fibril formation" are lower at late Braak stage in inhibitory (GABAergic) neurons; "phospholipid binding" and "cellular response to lipids" pathway genes are higher at late Braak stage in microglia and OPCs respectively; genes with higher GM-astrocyte expression at late stage are enriched in endocytosis and kinase-binding processes; the analogous genes in GM glutamatergic neurons are enriched in regulation of vesicle transport; genes with higher expression specifically in WM (not GM) microglia at late Braak stage are enriched in cellular response to lipoprotein particle stimuli; the analogous WM-oligodendrocyte genes are enriched for regulation of amyloid-beta formation.
- **Status**: supported
- **Falsification criteria**: A replication finding no cell-type-specific segregation of these pathway enrichments (e.g., amyloid-fibril-formation genes not preferentially altered in inhibitory neurons, or lipid-response genes not preferentially altered in microglia/OPCs) would refute the claim of pathway-level cell-type specificity.
- **Proof**: [E05]
- **Evidence basis**: Fig. 3c (pathway enrichment dot plot, 20% FDR), Fig. 3e (pathway enrichment dot plot, 10% FDR of DEGs in pathways associated with AD genes).
- **Interpretation**: The cell-type-segregated pathway pattern (amyloid-clearance genes affected in neurons, lipid/lipoprotein-response genes affected in microglia/OPCs, vesicle-transport/endocytosis genes affected in glutamatergic neurons/astrocytes, WM-specific amyloid-beta-formation regulation in oligodendrocytes) is presented as evidence that AD-pathology-associated transcriptional programs are routed through distinct cell-type-specific and tissue-specific biological processes rather than a single shared response.
- **Sources**:
  - "genes involved in the negative regulation of amyloid fibril formation were lower at late Braak stages in inhibitory neurons, while 'phospholipid binding' and 'cellular response to lipids' were higher at late Braak stages in microglia and OPCs, respectively (Fig. 3c)." ← Results §"Differential expression analysis identifies additional cell type-specific genes...", p.7 of 17 [result]
  - "The genes with higher expression GM astrocytes in late stage pathology were enriched in endocytosis and kinase binding processes (Fig. 3e), while the analogous genes in GM glutamatergic neurons were enriched in the regulation of vesicle transport." ← same section, p.7 of 17 [result]
  - "Genes with higher expression in WM microglia (but not GM microglia) at later Braak stages were enriched in cellular response to lipoprotein particle stimuli, while the analogous genes in WM oligodendrocytes showed enrichment for the regulation of amyloid-beta formation." ← same section, p.7 of 17 [result]
- **Dependencies**: C05, C06
- **Tags**: pathway-enrichment, MAGMA, fgsea, cell-type-specificity, AD-genes

## C09: CARTANA in-situ sequencing validates specific cell-type-marker-gene associations with Braak stage in intact tissue, in both gray and white matter
- **Statement**: Linear mixed-effects modeling (lmerTest) of 155-gene CARTANA expression against Braak stage (0-1/2-4/5-6, n=11 individuals) confirmed, in GM: lower expression of ACTG1 (p=0.02), CC2D1B (p=0.001), PPP1R1A (p=0.02), ALDH1A1 (p=0.011), TM2D1 (p=0.02) in glutamatergic neurons and ACTG1 (p=0.006), SCG3 (p=0.016, 0.002), PDCD6 (p=0.013) in GABAergic neurons at late Braak stages, alongside higher CC2D1B/PPP1R1A at Braak stages 5/6 and 2/4 respectively (consistent with THEMIS+/POSTN+ resilience); lower CD74 (p=0.012) and P2RY12 (p=0.001) in microglia; higher GFAP (p=0.0001) in astrocytes; and in WM: lower PDCD6 (p=0.03) and ANXA7 (p=0.012) in GABAergic neurons.
- **Status**: supported
- **Falsification criteria**: A replication CARTANA (or comparable in-situ) experiment finding no significant association between these marker genes and Braak stage in the corresponding cell class would refute the claim that the snRNA-seq-derived proportion/expression associations validate in intact tissue.
- **Proof**: [E06]
- **Evidence basis**: Fig. 4c (boxplots of genes with significant Braak-stage associations in GM/WM tissue, with per-gene p-values in the figure caption).
- **Interpretation**: Because CARTANA measures gene expression directly on intact tissue sections (not dissociated nuclei), concordant directionality with the snRNA-seq findings is interpreted as evidence that the dissociated-nuclei proportion/expression signatures are not artifacts of the dissociation process.
- **Sources**:
  - "we found that the expression of ACTG1, ALDH1A1, and TM2D1 within glutamatergic neurons was statistically significantly lower in GM tissue from donors at late Braak stages." ← Results §"Validation of snRNA-seq derived associations...", p.8-9 of 17 [result]
  - "Within GABAergic neurons, we found lower expression of ACTG1 and SCG3 ... In addition to this, we found relatively lower expression of PDCD6 in Braak stages 5/6" ← same section, p.9 of 17 [result]
  - "we found higher expression of PPP1R1A and CC2D1B within glutamatergic neurons at Braak stages 2/4 and 5/6, respectively" ← same section, p.9 of 17 [result]
  - "the ISH data recapitulated lower proportions of the RPL19+ microglial subcluster, as evidenced by lower expression of CD74 and P2RY12 in microglia in intact tissue" ← same section, p.9 of 17 [result]
  - "higher expression of GFAP at advanced Braak stages was consistent with our snRNA-seq findings" ← same section, p.9 of 17 [result]
  - "we identified lower expression of PDCD6 and ANXA7 in PVALB+ GABAergic neurons in Braak stage 5/6" (WM) ← same section, p.9 of 17 [result]
  - Specific p-values GM: "ACTG1_Glut- 0.02, CC2D1B_Glut- 0.001, PPP1R1A_Glut- 0.02, ALDH1A1_Glut-0.011, TM2D1_Glut-0.02, ACTG1_GABA- 0.006, SCG3_GABA- 0.016, 0.002, PDCD6_GABA- 0.013, CD74_Microg- 0.012, P2RY12_Microg- 0.001, GFAP_Astro- 0.0001." Specific p-values WM: "PDCD6_GABA- 0.03, ANXA7_GABA- 0.012." ← Fig. 4 caption, p.9 of 17 [result]
- **Dependencies**: C01, C02, C03
- **Tags**: CARTANA, in-situ-sequencing, spatial-validation, lmerTest

## C10: Global (all-cell-class) CARTANA expression signature shows nominal enrichment above the null expectation with Braak stage and with binarized pathology, but no genes survive multiple-testing correction
- **Statement**: At the global (all-cell) level, no genes were statistically significant after multiple-testing correction for Braak-stage comparisons, but 29 genes reached nominal significance (a two-fold enrichment relative to the null expectation); grouping donors into low/high pathology instead of individual Braak stage yielded 31 genes at nominal p<0.05, a ~4-fold enrichment relative to the null expectation of ~8 genes (155 tests x 0.05).
- **Status**: supported
- **Falsification criteria**: A replication finding no nominal enrichment above the null (i.e., approximately 8/155 genes nominally significant by chance) at either the Braak-stage or low/high-pathology global-signature level would refute the claim of a detectable, if statistically underpowered, global transcriptional signal.
- **Proof**: [E07]
- **Evidence basis**: Supplementary Fig. 7a-b (not included in the provided PDF; the 29-gene and 31-gene nominal-enrichment statistics are stated directly in the main-text Results).
- **Interpretation**: The authors read this as confirmation, "at both the global and broad cell class level," that "the strongest signals from our dissociated single nucleus RNA-seq proportion and gene expression analyses" are recapitulated with at least nominal statistical signal in the spatial data, while acknowledging the global (non-cell-type-resolved) analysis lacks power for formal significance after correction.
- **Sources**:
  - "At the global level, we did not find any statistically significant genes after multiple testing corrections. However, we found 29 genes with nominal significance, which is a two-fold enrichment with respect to the null." ← Results §"Validation of snRNA-seq derived associations...", p.9 of 17 [result]
  - "when we grouped donors into low and high pathology (instead of by individual Braak stage), we identified 31 genes with a nominal p-value below 0.05, which is a ~4-fold enrichment compared to what would be expected under the null (i.e., 155 tests*0.05 = 8 genes)" ← same section, p.9 of 17 [result]
- **Dependencies**: none
- **Tags**: CARTANA, global-signature, nominal-significance, Wilcoxon

## C11: TMEM119 is unexpectedly upregulated (rather than the typically-reported downregulated) in CARTANA data at advanced pathology, discordant with co-measured homeostatic marker P2RY12, and this discrepancy is absent from the snRNA-seq data
- **Statement**: "the expression of TMEM119, a presumed homeostatic microglial gene, is unexpectedly upregulated in donors with advanced pathology. This contrasts with P2RY12, another homeostatic microglial gene, which is typically downregulated in similar conditions; this discrepancy is not found in the snRNA-seq data."
- **Status**: supported
- **Falsification criteria**: A replication CARTANA/ISH dataset in which TMEM119 is downregulated (concordant with P2RY12) at advanced pathology, or in which the same TMEM119-upregulation pattern is also present in snRNA-seq data, would refute the claim that this is a platform-specific discordance.
- **Proof**: [E07]
- **Evidence basis**: Results text and Discussion (no dedicated main-text figure panel; referenced qualitatively in the Fig. 4/global-ISH-signature discussion).
- **Interpretation**: The authors note partial precedent for TMEM119 upregulation in pathology/injury contexts in the literature (Satoh et al. 2016, elevated TMEM119 mRNA in AD frontal cortex; Mercurio et al. 2022, Tmem119 changes in a mouse TBI model) but explicitly leave the underlying cause of the TMEM119-vs-P2RY12 discordance unresolved.
- **Sources**:
  - "Notably, the expression of TMEM119, a presumed homeostatic microglial gene, is unexpectedly upregulated in donors with advanced pathology. This contrasts with P2RY12, another homeostatic microglial gene, which is typically downregulated in similar conditions; this discrepancy is not found in the snRNA-seq data." ← Results §"Validation of snRNA-seq derived associations...", p.9 of 17 [result]
  - "While the underlying cause of this unusual pattern remains unclear, we reference some studies that have reported a similar expression trend for TMEM119." ← Discussion, p.12 of 17 [result]
- **Dependencies**: C10
- **Tags**: TMEM119, P2RY12, microglia, unresolved-discrepancy, CARTANA

## C12: Cell type-specific gene expression varies with spatial proximity to amyloid plaques and tau tangles, revealing pathology-specific proximal signatures not observable from dissociated nuclei
- **Statement**: In the distance-based mixed-effects model (close/intermediate/far bins), glutamatergic NEFL and NEFM are lower, and ALDH5A1 higher, at intermediate/far distance from plaques (i.e., higher near plaques); GABAergic RELN is lower proximal to plaques; microglial CD68 is higher at intermediate distance from plaques; astrocytic GFAP and endothelial/pericyte ID3 are higher in plaque-distant cells. For tangles, THEMIS (glutamatergic), GFAP (astrocytes), and PLP1 (oligodendrocytes) are all higher in tangle-distant cells. In the plaque x tangle interaction model, glutamatergic ACTG1 is lower at intermediate distance from plaques and far from tangles, DYNC2LI1 is lower in cells farthest from both pathologies, and inhibitory-cell KIT is reduced at intermediate distance from both.
- **Status**: supported
- **Falsification criteria**: A replication finding no significant gene-expression gradient with plaque/tangle distance for these genes/cell types (e.g., no NEFL/NEFM elevation near plaques in glutamatergic neurons) would refute the claim of pathology-proximity-dependent, cell-type-specific expression gradients.
- **Proof**: [E08]
- **Evidence basis**: Fig. 5b (distance-from-plaques heatmap: GFAP, ID3, RELN, ALDH5A1, NEFL, NEFM, CD68, with Δ log-expression values and significance stars), Fig. 5c (distance-from-tangles heatmap: GFAP, THEMIS, PLP1).
- **Interpretation**: Because plaques are extracellular and tangles are predominantly intraneuronal, the paper interprets the differing proximal gene sets for the two pathologies as reflecting distinct local cellular-stress mechanisms; the elevated neurofilament (NEFL/NEFM) expression specifically near plaques is interpreted as a candidate marker of plaque-related neuronal stress.
- **Sources**:
  - "In glutamatergic cells, there was higher expression of ALDH5A1 in cells at intermediate distance and far from plaques, whereas NEFL and NEFM showed lower expression in these groups" ← Results §"Spatial analysis identifies genes with altered expression near pathological inclusions", p.9 of 17 [result]
  - "In GABAergic cells, RELN had lower expression in the proximal cells (higher expression in the plaque-intermediate and distant group)" ← same section, p.9 of 17 [result]
  - "In microglia, expression of CD68 was higher in cells at intermediate distance from plaques, while astrocytic GFAP expression was higher in plaque-distant cells" ← same section, p.9 of 17 [result]
  - "in endothelial and pericytes, ID3 showed higher expression in plaque-distant cells" ← same section, p.9 of 17 [result]
  - "we found that THEMIS expression was higher in glutamatergic neurons far from tangles, as was GFAP expression in astrocytes and PLP1 expression in oligodendrocytes" ← same section, p.9 of 17 [result]
  - "in glutamatergic neurons, the expression of ACTG1 was lower at an intermediate distance from plaques and when located far from tangles, and DYNC2LI1 expression was lower in cells furthest from both pathologies. Among inhibitory cells, only KIT expression varied in the interaction model, with reduced abundance at an intermediate distance from both tangles and plaques." ← Results §"Spatial analysis...", p.11 of 17 [result]
- **Dependencies**: C09
- **Tags**: spatial-transcriptomics, distance-based-model, plaque-proximity, tangle-proximity, CARTANA

## C13: Bulk GFAP transcript is elevated distal to plaques, but plaque-proximal cells show a non-unimodal (bimodal-like) GFAP expression distribution, reconciling this with prior IHC reports of increased GFAP+ density near plaques
- **Statement**: Whereas panel-average GFAP transcript levels are higher in plaque-distant cells (C12), Hartigan's dip statistic for the GFAP expression distribution is highest in the plaque-proximal ("close") distance bin (median dip = 0.124) compared to the intermediate (0.119) and far (0.121) bins, indicating a stronger deviation from unimodality (consistent with co-occurring GFAP-high and GFAP-low astrocyte subpopulations) specifically near plaques.
- **Status**: supported
- **Falsification criteria**: A replication finding no elevated dip statistic (i.e., a unimodal GFAP distribution) in the plaque-proximal bin relative to intermediate/far bins would refute the bimodality-based reconciliation of the GFAP finding with prior IHC literature.
- **Proof**: [E08]
- **Evidence basis**: Discussion text; Supplementary Fig. 7d (not included in the provided PDF; the dip-statistic values are stated directly in the main-text Discussion).
- **Interpretation**: The authors propose this pattern "can be reconciled if both GFAP-high and GFAP-low astrocyte densities increase near plaques, resulting in a non-unimodal expression pattern" — i.e., an increase in the total number of astrocytes of both reactive and non-reactive character near plaques, rather than a simple uniform upregulation, would produce exactly the counterintuitive average-expression pattern observed in C12 while remaining consistent with prior IHC reports of increased astrocyte density near plaques.
- **Sources**:
  - "This can be reconciled if both GFAP-high and GFAP-low astrocyte densities increase near plaques, resulting in a non-unimodal expression pattern. To test this, we used kernel density estimation to identify local minima in the expression distribution and defined density-based thresholds to classify GFAP into ordered expression groups." ← Discussion, p.11-12 of 17 [result]
  - "Plaque proximal (close) bin exhibited the highest median dip value (0.124), indicating a stronger deviation from unimodality... In contrast, intermediate and far bins showed lower median dip values (0.119 and 0.121, respectively) than the proximal group." ← Discussion, p.12 of 17 [result]
- **Dependencies**: C12
- **Tags**: GFAP, bimodality, Hartigan-dip-statistic, astrocyte-heterogeneity

## C14: Tile-based (plaque-density) analysis identifies a distinct, nominally-significant set of plaque-microenvironment genes, including reduced SERPINE1 specifically in low-pathology individuals
- **Statement**: Comparing paired plaque-containing vs. plaque-free 1056 µm² tiles (Wilcoxon rank-sum, no significant genes after multiple-testing correction), 15 genes reached nominal significance (p<0.05), a 2-fold enrichment relative to the null; this analysis detected lower NEFM in glutamatergic neurons in plaque-free tiles (consistent with the distance-based finding), higher BIN1 (an AD-risk gene) in microglia in plaque-containing tiles, and reduced SERPINE1 (a vascular/microglial gene that inhibits the amyloid-beta-degrading enzyme plasmin) in plaque-containing tiles specifically in individuals with low pathology.
- **Status**: supported
- **Falsification criteria**: A replication finding no nominal enrichment of genes distinguishing plaque-containing vs. plaque-free tiles, or no low-pathology-specific SERPINE1 reduction in plaque-containing tiles, would refute this claim.
- **Proof**: [E09]
- **Evidence basis**: Supplementary Fig. 7c (not included in the provided PDF; gene-level findings and nominal-enrichment statistic are stated directly in the main-text Results).
- **Interpretation**: The authors interpret the low-pathology-specific SERPINE1 reduction near plaques as suggesting that "activation and amyloid-beta degradation may be greater in these individuals in earlier stages of the disease," i.e., a candidate compensatory clearance mechanism operative preferentially in early, not late, pathological stages.
- **Sources**:
  - "this analysis did not yield any significant genes after multiple testing correction, 15 genes were nominally significant (p < 0.05), corresponding to a 2-fold enrichment with respect to the null hypothesis" ← Results §"Spatial analysis identifies genes with altered expression near pathological inclusions", p.11 of 17 [result]
  - "this approach also detected lower NEFM expression in glutamatergic neurons in tiles with no plaques. In microglia, we observed an increase of BIN1, a well-known AD risk gene, in plaque-containing tiles. Finally, we found a reduction of SERPINE1, a vascular and microglial specific gene involved in the inhibition of plasmin (which degrades amyloid-beta plaques), in plaque-containing tiles only in individuals with low pathology" ← same section, p.11 of 17 [result]
- **Dependencies**: C12
- **Tags**: tile-based-model, plaque-density, SERPINE1, BIN1, CARTANA
