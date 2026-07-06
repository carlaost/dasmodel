# Claims

All numbers are copied exactly from the paper PDF (Avey et al., *Molecular Neurodegeneration
Advances*, 2025). This is an empirical/observational + experimental biology paper (not a
training-run paper), so reported statistics carry the `[result]` tag and are grounded to the
Results/Methods section and page-of-23 label whose verbatim text was opened and confirmed.
`Status: supported` is used where the paper presents its own generated result as an established
finding of this study (not an external prior claim being cited).

## C01: Aβ-load-stratified pseudobulk expression yields distinct, largely non-overlapping DEG sets
- **Statement**: Contrasting low-Aβ vs. high-Aβ pseudobulk expression (linear mixed models, FDR<0.05) detected 93, 140, and 159 differentially expressed genes (DEGs) for the combined, glia-low, and glia-high conditions respectively, with only 18 genes overlapping among all three contrasts.
- **Status**: supported
- **Falsification criteria**: A replication pseudobulk LMM analysis on an independent paired ST-IHC human AD cohort yielding materially different DEG counts or negligible contrast-specificity (i.e., near-complete overlap across conditions) would refute the claim that glial context modifies the Aβ transcriptomic response.
- **Proof**: [E01]
- **Evidence basis**: Fig. 3B-D (volcano plot, glia-stratified scatterplot, Venn diagram of DEG overlap).
- **Interpretation**: The low overlap (18/~300 total significant genes) indicates that surrounding glial abundance substantially reshapes which genes respond to Aβ load, rather than the Aβ response being a fixed, glia-independent transcriptional program.
- **Sources**:
  - 93, 140, 159 DEGs ← Results §"Low-Aβ spots show transcriptomic profiles..." p.11 of 23 «we detected 93, 140, and 159 differentially expressed genes (DEGs) for combined, glia-low, and glia-high conditions» [result]
  - 18 genes overlapping ← Results, same section, p.11 of 23 «Many DEGs are unique for a specific contrast, with only 18 genes overlapping among all three contrasts» [result]
- **Dependencies**: none
- **Tags**: differential-expression, pseudobulk, amyloid-beta, glia-stratification

## C02: Low-Aβ (diffuse-plaque-enriched) spots show a more neurotoxic local transcriptomic and histological profile than high-Aβ spots
- **Statement**: GSEA on the low-vs-high-Aβ contrast shows reduced synaptic-function pathways (especially under the glia-high condition) and elevated apoptosis/immune pathways, with lower expression of neuronal/synaptic genes (NEFH, NEFM, SYT13, SYNGR1, SLC17A6, GABRD) and higher apoptosis-gene (CIDEA) expression in low-Aβ spots across glia conditions; independent IHC on FFPE sections from 10 AD individuals confirmed more cleaved-caspase-3 puncta co-localized with NeuN+ nuclei (paired t-test p=0.041) and with total nuclei (p=2.61e-4) near low-Aβ plaques than high-Aβ plaques.
- **Status**: supported
- **Falsification criteria**: An independent IHC/spatial cohort showing equal or greater apoptosis/synaptic loss near high-Aβ (vs. low-Aβ) plaques, or no significant caspase-3 difference by Aβ stratum, would refute the claim.
- **Proof**: [E01, E03]
- **Evidence basis**: Fig. 3E, 3G (GSEA/gene-level boxplots), Fig. 3H-I (IHC images and caspase-3 quantification).
- **Interpretation**: The authors propose this could reflect that vulnerable neurons near high-Aβ (more mature) plaques have already undergone cell death, so damage signatures are more visible earlier, around diffuse/low-Aβ plaques — consistent with imaging/cryo-EM studies suggesting early-stage plaques are richer in toxic oligomers/protofibrils.
- **Sources**:
  - paired t-test p=0.041, p=2.61e-4 ← Fig. 3 caption, p.13 of 23 «Points represent average values from > 100 ROIs for each of 10 AD individuals (paired t-test; *p = 0.041, **p = 2.61e-4)» [result]
  - "more cleaved caspase-3 puncta ... near low Aβ plaques compared to high Aβ plaques" ← Results §"Low-Aβ spots show transcriptomic profiles..." p.13 of 23 «We detected more cleaved caspase-3 puncta co-localized with NeuN + nuclei and total nuclei near low Aβ plaques compared to high Aβ plaques» [result]
- **Dependencies**: C01
- **Tags**: apoptosis, synaptic-degeneration, amyloid-beta, IHC-validation

## C03: Glia-high plaque niches show elevated inflammatory/apoptotic signaling and reduced neuronal/synaptic markers relative to glia-low niches
- **Statement**: Contrasting glia-high vs. glia-low pseudobulk expression (FDR<0.05) detected 230, 241, and 63 DEGs for the combined, low-Aβ, and high-Aβ conditions respectively; glia-high spots show higher glial-marker expression (SPARC, CD44, HLA-DRA) and lower excitatory/inhibitory neuronal, synaptic, ion-channel, and neurofilament marker expression (RORB, PVALB, SYT2, SLC6A17, GRM7, GABBR2, SCN1B, NEFH/M/L); IHC on FFPE sections from 10 AD individuals confirmed reduced synaptophysin (SYP) and NeuN staining and greater CD68 abundance surrounding glia-high vs. glia-low plaques (paired t-test, most comparisons p<0.005 to p<1e-10).
- **Status**: supported
- **Falsification criteria**: A replication showing no significant difference in neuronal/synaptic marker expression or IHC staining between glia-high and glia-low niches would refute the claim that glial abundance itself (independent of Aβ load) associates with local neurodegeneration.
- **Proof**: [E05, E07]
- **Evidence basis**: Fig. 5B-D (DEG counts, volcano/scatter), Fig. 5G (gene boxplots), Fig. 5H (IHC images/quantification).
- **Interpretation**: Supports a model in which plaque-surrounding reactive glia actively contribute to (rather than merely respond to) local neuronal/synaptic loss, converging with mouse-model evidence that microglial elimination halts plaque-associated transcriptomic change.
- **Sources**:
  - 230, 241, 63 DEGs ← Results §"Plaques with surrounding glia display transcriptomic differences..." p.13 of 23 «We detected 230, 241, and 63 DEGs for combined, low Aβ and high Aβ conditions (FDR adjusted p < 0.05; Fig. 5B-D; Supplementary Table 8), respectively» [result]
  - IHC paired t-test significance bands ← Fig. 5 caption, p.16 of 23 «Points represent average values from each of 10 AD individuals quantified in the area surrounding plaques (scale bar = 25 µm; paired t-test; **p < 0.005, ***p < 1e-10, n.s. not significant)» [result]
- **Dependencies**: none
- **Tags**: glia-abundance, differential-expression, neurodegeneration, IHC-validation

## C04: Spatial glial responses converge on established mouse/human glial-activation gene modules, with the human MG3 (DAM-like) state most consistently enriched
- **Statement**: GSEA against mouse-model gene modules (PIG, OLIG, DAM, DAA) and 12 human AD-brain microglial states (MG0-MG12) shows positive enrichment of PIG, OLIG, DAM, and DAA under both low-Aβ and high-Aβ as well as both glia-low and glia-high conditions, and enrichment of nearly all human MG states except MG0 (homeostatic) and MG1 (neuronal surveillance); the MG3 state ("ribosome biogenesis," reported to most resemble mouse DAM) shows the strongest enrichment across all Aβ and glia contrasts tested.
- **Status**: supported
- **Falsification criteria**: A replication in which MG3 (or a DAM-like signature) fails to be the top-enriched microglial state across independent Aβ/glia contrasts, or in which PIG/OLIG/DAM/DAA modules show no enrichment in human spatial data, would refute the claim of cross-species/cross-modality convergence.
- **Proof**: [E02, E06]
- **Evidence basis**: Fig. 3F, Fig. 5F (GSEA heatmaps for gene modules and MG0-12 states).
- **Interpretation**: The convergence across independently derived module sets (mouse single-cell modules and human microglial states derived from a separate snRNA-seq cohort) is interpreted as evidence for a partially conserved, plaque-proximal glial activation program, with MG3 nominated as a potential therapeutic cell-state target.
- **Sources**:
  - MG3 "ribosome biogenesis" resembles mouse DAM, strongest under all glia conditions ← Results §"ST spot stratification..." p.11-12 of 23 «MG3 microglia were reported as "ribosome biogenesis" MG state, which most resembles mouse DAM» [result]
  - enrichment for almost all MG states except MG0/MG1 ← Results §"Plaques with surrounding glia..." p.14-15 of 23 «we detected enrichment for almost all MG states except for MG0 (homeostatic) and MG1 (neuronal surveillance)» [result]
  - MG3 strongest enrichment under all Aβ conditions ← Results, same section, p.15 of 23 «The MG3 DAM (ribosome biogenesis) state showed the strongest enrichment under all Aβ conditions» [result]
- **Dependencies**: C01, C03
- **Tags**: GSEA, microglia-states, DAM, gene-modules, cross-species

## C05: Aβ-intensity spot stratification (no/low/high) tracks classical plaque maturity (diffuse vs. compact/dense-core) and replicates across two independent tissue cohorts
- **Statement**: High-Aβ IHC-intensity ST spots are enriched for compact/dense-core plaques and low-Aβ spots for diffuse plaques in the primary frozen-tissue cohort (781 manually annotated plaques; odds ratio OR=3.02, p=3.21e-9), and this pattern replicates in an independent FFPE validation cohort of 9 AD ROSMAP participants (722 manually annotated plaques; OR=14.98, p=4.89e-38).
- **Status**: supported
- **Falsification criteria**: Failure to replicate the diffuse/low-Aβ vs. compact-dense-core/high-Aβ association (e.g., a non-significant or inverted odds ratio) in an independent annotated cohort would refute the validity of the IHC-intensity-based stratification as a plaque-maturity proxy.
- **Proof**: [E09]
- **Evidence basis**: Fig. 2C (frozen-section plaque-type proportions by Aβ stratum with OR/p); Supplementary Fig. 6 (FFPE replication; figure not included in provided PDF, cited from text only).
- **Interpretation**: Validates using continuous IHC intensity (rather than manual diffuse/compact/dense-core scoring, which the frozen ST sections' freezing artifacts precluded doing reliably at scale) as the basis for the no/low/high Aβ spot stratification used throughout the study.
- **Sources**:
  - OR=3.02, p=3.21e-9 (frozen, n=781 plaques) ← Results §"ST spot stratification by Aβ and glial staining" p.11 of 23 «the high Aβ spots are more enriched for compact and dense core plaques and the low Aβ spots are more enriched for diffuse plaques (OR = 3.02, p = 3.21e-9, Fig. 2C)» [result]
  - OR=14.98, p=4.89e-38 (FFPE, n=722 plaques, 9 individuals) ← Results, same section, p.11 of 23 «we found that low-Aβ areas are enriched for diffuse plaques, while high-Aβ areas are enriched for compact and dense core plaques (OR = 14.98, p = 4.89e-38, Supplementary Fig. 6 C)» [result]
- **Dependencies**: none
- **Tags**: plaque-typing, validation, IHC, cross-cohort

## C06: Aβ load reshapes inferred intercellular ligand-receptor (LR) signaling, with the largest, most synapse/neuron-relevant changes in low-Aβ spots
- **Statement**: NICHES-inferred LR differential-expression analysis of low-Aβ-vs-no-Aβ and low-Aβ-vs-high-Aβ contrasts shows a positive correlation (R=0.85) between the two contrasts, with many shared dysregulated LR pairs related to synapses, neuron differentiation, and ECM pathways; low-Aβ spots additionally show higher expression of vesicle-transport-related LRs (APP-DCC, APP-VLDLR, APOE-LDLR) and immune/MAPK-cascade-related LRs (C1QA-CD93, CD99-PILRA) relative to no-Aβ and high-Aβ spots.
- **Status**: supported
- **Falsification criteria**: Absence of correlation between the low-vs-no and low-vs-high LR contrasts, or failure to detect synapse/neuron-relevant LR pairs among the top differentially expressed pairs in an independent dataset, would refute the claim that Aβ load coherently reshapes the inferred local signaling microenvironment.
- **Proof**: [E04]
- **Evidence basis**: Fig. 4A-C (LR scatterplot with R value, GO enrichment heatmap, representative spatial LR expression).
- **Interpretation**: The authors interpret the vesicle-transport LR upregulation (APP-DCC/VLDLR, APOE-LDLR) as a possible compensatory Aβ-clearance mechanism, and the MAPK/immune LR enrichment as supporting combined immune-modulation + MAPK-inhibition as a candidate therapeutic strategy for early AD, particularly given that low-Aβ spots show the more pronounced synaptic/neuronal-degeneration-related LR signal.
- **Sources**:
  - R=0.85 correlation between contrasts ← Results §"Inferred intercellular communication suggests neurodegeneration in low Aβ spots" p.13 of 23 «We noticed a positive association (R = 0.85) between these contrasts» [result]
- **Dependencies**: C02
- **Tags**: ligand-receptor, NICHES, intercellular-communication, amyloid-beta

## C07: Glial abundance reshapes inferred ligand-receptor signaling toward reduced synaptic and (in high-Aβ) increased immune/TREM2 signaling
- **Statement**: NICHES LR analysis of glia-high-vs-glia-low contrasts under low-Aβ and high-Aβ conditions shows a positive correlation (R=0.41) between the two conditions; synaptic-pathway LR pairs (RPH3A-NRXN1, DSCAM-DCC, GNB3-GABBR2, RIMS1-SLC17A7, CXCR16-GRM7) are downregulated in glia-high spots across all Aβ conditions, while under the high-Aβ condition specifically, immune-related LRs (CLU-TREM2, PLXNA1-TREM2, APOE4-LDLR, GFAP-APLNR) and ECM/vesicle-transport LRs (SPARC-ENG, APP-TSPAN15) are upregulated and TGF-β1 signaling (TGFB1-ITGAV) is downregulated in glia-high spots.
- **Status**: supported
- **Falsification criteria**: Absence of the reported correlation between low-Aβ and high-Aβ glia-contrast LR signatures, or failure to replicate downregulation of the identified synaptic LR pairs in glia-high niches, would refute the claim.
- **Proof**: [E08]
- **Evidence basis**: Fig. 6A-D (LR scatterplot with R value, representative spatial/boxplot expression, GO enrichment heatmap).
- **Interpretation**: The more substantial LR differences under the high-Aβ condition (increased autophagy, reduced cell adhesion/myelination per GSEA) are interpreted as possibly reflecting a culmination of progressive plaque development, glial activation, and neurodegeneration.
- **Sources**:
  - R=0.41 correlation ← Results §"Inferred intercellular communication suggests synaptic degeneration in glia-high plaque spots" p.16 of 23 «We observed a positive correlation (R = 0.41) between the low Aβ and high Aβ conditions» [result]
- **Dependencies**: C03
- **Tags**: ligand-receptor, NICHES, intercellular-communication, glia-abundance

## C08: Aβ-oligomer-treated iPSC-derived microglia (iMGL), but not co-cultured astrocytes or neurons, recapitulate the spatial glia-high-vs-glia-low transcriptomic response
- **Statement**: In an iPSC-derived multicellular co-culture (iMGL + astrocyte/neuron) treated with Aβ oligomers for 24 h and profiled by scRNA-seq (13,740 cells total), differential expression analysis identified 199, 58, and 271 Aβ-induced DEGs in neurons, astrocytes, and iMGLs respectively; GSEA using these Aβ-induced DEGs as genesets against the ST-derived glia-high-vs-glia-low signature showed positive enrichment only in iMGLs, with no enrichment detected in astrocytes or neurons.
- **Status**: supported
- **Falsification criteria**: A replication showing enrichment of the ST glial signature in astrocyte or neuron Aβ-response genes (rather than iMGL-specific), or no enrichment in iMGLs, would refute the claim that microglia are the principal cell type mediating the spatially observed glial response.
- **Proof**: [E10]
- **Evidence basis**: Fig. 7C-F (cell-type UMAP/marker dotplot, GSEA enrichment by cell type, iMGL DEG boxplots).
- **Interpretation**: Supports a model in which microglia play a primary (though not necessarily exclusive) role in mediating the tissue-level glial response to Aβ, consistent with imaging studies showing microglia (more than astrocytes) closely surround plaques; the authors note that the short (24 h) treatment window may under-detect slower astrocyte/neuron responses.
- **Sources**:
  - 13,740 cells ← Results §"ST glial response to Aβ plaques recapitulated..." p.16 of 23 «We acquired scRNA-seq data from 13,740 cells under the Aβ untreated and treated conditions» [result]
  - 199, 58, 271 Aβ DEGs (neurons, astrocytes, iMGLs) ← Results, same section, p.16 of 23 «we analyzed differential gene expression for neurons, astrocytes, and iMGLs, and identified 199, 58, and 271 Aβ DEGs, respectively» [result]
  - positive enrichment in iMGLs only ← Results, same section, p.16 of 23 «We detected a positive enrichment of the ST glial response in iMGLs. However, no enrichment was observed in astrocytes and neurons» [result]
- **Dependencies**: C03, C04
- **Tags**: iPSC, microglia, in-vitro-validation, scRNA-seq

## C09: Aβ-treated iMGL subclusters differentially resemble specific human AD microglial states, with iMGL1 most closely resembling MG3
- **Statement**: Sub-clustering Aβ-treated iMGLs into four subclusters (iMGL1-4) and running GSEA of each subcluster's marker genes against the ST glia-high-vs-glia-low signature showed iMGL1 enriched under both Aβ-low and Aβ-high conditions while iMGL2 and iMGL3 were enriched primarily under the Aβ-low condition; cross-referencing each subcluster's DEGs against the 12 human MG-state genesets showed iMGL1 positively enriched for the MG3 (DAM, "ribosome biogenesis") state — the state most enriched in the in vivo ST glial response — while iMGL2 was enriched for MG4 (lipid processing), MG5 (phagocytic), MG7 (glycolytic), and MG10 (inflammatory III).
- **Status**: supported
- **Falsification criteria**: A replication failing to reproduce iMGL1's specific enrichment for the MG3/DAM signature, or showing a different iMGL subcluster as the dominant MG3-resembling population, would refute the claim of a specific correspondence between iMGL1 and the in vivo MG3 state.
- **Proof**: [E10]
- **Evidence basis**: Fig. 7G-J (iMGL subcluster UMAP, marker heatmap, GSEA enrichment for ST signature and for MG0-12 states).
- **Interpretation**: Supports using Aβ-treated iMGL1 as an in vitro proxy for the MG3/DAM-like state implicated as the dominant in vivo glial response, enabling mechanistic dissection of this state outside the tissue context.
- **Sources**:
  - iMGL1 enriched under both Aβ-high and Aβ-low; iMGL2/3 primarily Aβ-low ← Results §"ST glial response to Aβ plaques recapitulated..." p.18 of 23 «iMGL1 demonstrated enrichment under both Aβ-high and Aβ-low conditions, whereas iMGL2 and iMGL3 showed enrichment primarily in the Aβ-low condition» [result]
  - iMGL1 positively enriched for MG3 ← Results p.19 of 23 «iMGL1 is positively enriched for the MG3 DAM state, which is the most enriched state in the ST glial response» [result]
  - iMGL2 enriched for MG4, MG5, MG7, MG10 ← Results p.19 of 23 «iMGL2 is enriched for MG4 (lipid processing), MG5 (phagocytic), MG7 (glycolytic), and MG10 (inflammatory III)» [result]
- **Dependencies**: C08
- **Tags**: iPSC, microglia-states, DAM, in-vitro-validation
