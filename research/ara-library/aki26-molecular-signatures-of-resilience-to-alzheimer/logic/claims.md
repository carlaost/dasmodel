# Claims

Numbers in `Statement`/`Evidence basis` are copied verbatim from the paper (full-text PDF). Each
load-bearing value carries a `**Sources**` entry citing the PDF location and the matched line.
Exact per-comparison p-values live in the paper's Source Data file (not reproduced here).

---

## C01: Resilient L4 IT population Ex5 increases in relative proportion with AD pathology
- **Statement**: A resilient excitatory population in layer 4 (cluster Ex5, co-expressing RORB, CUX2, EYA4, LAMA3), enriched in primary visual cortex (BA17), shows a significant relative increase in high- vs low-pathology cases in both BA9 (scCODA log2-fold change = 1.75) and BA17 (log2-fold change = 0.46); GLMM confirmed a significant increase in BA9 (FDR = 0.008) and a non-significant increasing trend in BA17 (p-value = 0.06).
- **Status**: supported
- **Falsification criteria**: If independent compositional analysis (or a bias-controlled model) showed Ex5 proportion unchanged or decreasing with pathology in BA9, or if the increase were fully explained by platform/QC artifact.
- **Proof**: [E03]
- **Evidence basis**: Fig. 4a (scCODA boxplots, credible effects PIP>0.95) and Fig. 4b (GLMM volcano). Sensitivity analyses (min 500 genes; 200–300-gene rescue) preserved the effect.
- **Interpretation**: The population is "resilient and becomes more prominent as other neuronal subtypes are lost" — relative, not absolute, increase.
- **Sources**:
  - 1.75 ← paper.pdf p6 «increase in the proportion of Ex5 neurons in high compared to low pathology cases in both BA9 (log2-fold change = 1.75) and BA17 (log2-fold change = 0.46)» [result]
  - FDR = 0.008 ← paper.pdf p7 Fig.4 caption «Ex5 neurons showed increased relative abundance in advanced AD in BA9 (FDR = 0.008)» [result]
  - p = 0.06 ← paper.pdf p7 Fig.4 caption «In BA17, Ex5 neurons showed a non-significant trend of increase (p-value = 0.06)» [result]
- **Dependencies**: C02, C10
- **Tags**: resilience, Ex5, L4 IT, compositional analysis, scCODA, GLMM

## C02: L4 IT excitatory neurons are relatively preserved during AD progression across regions
- **Statement**: The L4 IT excitatory neuron population is relatively preserved during AD progression in both BA9 and BA17; on a QC-filtered dataset (min 500 genes/cell, subclass-level annotation) the total L4 IT population remained relatively increased in high-pathology cases in both BA9 (log₂-fold change = 0.21) and BA17 (log₂-fold change = 0.33).
- **Status**: supported
- **Falsification criteria**: L4 IT showing robust depletion (like L2/3 IT / SST interneurons) across analyses would refute preservation.
- **Proof**: [E03]
- **Evidence basis**: Fig. 4a; Supplementary Fig. 7 (filtered dataset). Summary text: "our data consistently show that the L4 IT excitatory neuron population is relatively preserved during AD progression in BA9 and BA17."
- **Interpretation**: Preservation generalizes beyond BA17 to association-cortex L4 IT, though BA17 changes may carry platform bias (Drop-seq).
- **Sources**:
  - BA9 log₂FC = 0.21, BA17 = 0.33 ← paper.pdf p6 «total L4 IT population remained relatively increased in high-pathology cases in both BA9 (log₂-fold change = 0.21) and BA17 (log₂-fold change = 0.33) (Supplementary Fig. 7)» [result]
- **Dependencies**: C01
- **Tags**: resilience, L4 IT, preservation, sensitivity analysis

## C03: Integrated multi-method DGE yields 986 high-confidence DE genes with region/stage structure
- **Statement**: Combining a linear mixed model with bootstrap, pseudobulk (DESeq2), and hdWGCNA, 986 genes were categorized as 'high-confidence' DE genes; 54 were common across all four region×stage conditions (BA9-Early, BA9-Late, BA17-Early, BA17-Late). The number of DE genes was higher in BA9 than BA17 and higher in 'late' than 'early' groups; a parallel BINCC-annotated analysis on a min-500-gene dataset gave 962 high-confidence DE genes (460 overlapping; 35 shared across all four conditions).
- **Status**: supported
- **Falsification criteria**: Re-analysis producing a materially different high-confidence set, or no region/stage gradient in DE-gene counts.
- **Proof**: [E04]
- **Evidence basis**: Fig. 5b–e; Supplementary Data 7; Supplementary Fig. 10.
- **Sources**:
  - 986 high-confidence DE genes ← paper.pdf p8 «A total of 986 genes were categorized as 'high-conﬁdence' DE genes.» [result]
  - 54 shared across all four ← paper.pdf p9 «We identiﬁed 54 high-conﬁdence DE genes common across all four conditions.» [result]
  - 962 / 460 / 35 ← paper.pdf p9 «we identiﬁed a total of 962 'high-conﬁdence' DE genes, with 460 overlapping between both approaches. Of these 962 genes, 35 were shared across all four conditions» [result]
- **Dependencies**: none
- **Tags**: differential expression, high-confidence genes, region, stage

## C04: Early resilient neurons upregulate synapse/plasticity/calcium/neuroprotection genes
- **Statement**: Early-stage resilient L4 IT neurons upregulate genes associated with synapse maintenance, synaptic plasticity, calcium homeostasis, and neuroprotection, including GRIN2A, RORA, NRXN1, NLGN1, NCAM2, FGF14, NRG3, NEGR1, and CSMD1; several high-confidence DE genes are known AD genetic risk factors (CSMD1, NRG3, SYN3, NRXN1, SLC24A2, DLG2, KCNIP4).
- **Status**: supported
- **Falsification criteria**: Absence of coordinated upregulation of these genes/pathways in resilient (Ex5, BA17-Early) neurons, or their enrichment being non-synaptic/non-neuroprotective.
- **Proof**: [E04, E05]
- **Evidence basis**: Fig. 5f,g (pathway enrichment), Fig. 6a,b,d; Discussion gene list; Supplementary Data 8, 9.
- **Sources**:
  - gene list GRIN2A, RORA, NRXN1, NLGN1, NCAM2, FGF14, NRG3, NEGR1, CSMD1 ← paper.pdf p14 «upregulation of key genes including GRIN2A, RORA, NRXN1, NLGN1, NCAM2, FGF14, NRG3, NEGR1, and CSMD1» [result]
  - AD risk factors ← paper.pdf p9 «several high-conﬁdence DE genes have previously been identiﬁed as genetic risk factors for AD, including CSMD1, NRG3, SYN3, NRXN1, SLC24A2, DLG2, and KCNIP4» [result]
- **Dependencies**: C03, C09
- **Tags**: neuroprotection, synaptic genes, calcium homeostasis, pathway enrichment

## C05: KCNIP4 is upregulated in resilient Ex5 (early) and downregulated in vulnerable Ex2
- **Statement**: KCNIP4 is a high-confidence gene upregulated in resilient Ex5 (L4 IT) neurons at early disease stages in both BA9 and BA17, and consistently increases in Ex5 as disease progresses (MAST linear mixed model, adjusting for assay, sex, RIN, total counts, donor); in vulnerable Ex2 (L2/3 IT) neurons KCNIP4 is downregulated during stages of cell death, with an overall decline in late-stage disease.
- **Status**: supported
- **Falsification criteria**: KCNIP4 not upregulated in Ex5 early, or not divergently regulated between Ex5 and Ex2.
- **Proof**: [E04, E06]
- **Evidence basis**: Fig. 6a; Fig. 7a,b (violin plots across disease groups); Discussion.
- **Sources**:
  - Ex5 early up, both regions ← paper.pdf p9-10 «KCNIP4, a gene speciﬁcally upregulated in resilient Ex5 neurons at early disease stages in both BA17 and BA9» [result]
  - Ex2 down / late decline ← paper.pdf p14 «KCNIP4 was downregulated in vulner-able Ex2 L2/3 IT neurons during stages of cell death, with an overall decline observed in late-stage disease.» [result]
- **Dependencies**: C03, C04
- **Tags**: KCNIP4, resilience factor, Ex5, Ex2, MAST

## C06: KCNIP4 protein is elevated in L4 EYA4+ neurons at intermediate stage
- **Statement**: By immunofluorescence (n = 6 donors per pathology group), the mean KCNIP4 intensity in neuronal somas was significantly higher in L4 EYA4+ neurons at intermediate disease stages compared to controls, and lower in supragranular (L2/3) neurons at intermediate and high stages compared to controls, in BA17.
- **Status**: supported
- **Falsification criteria**: No stage-dependent divergence of KCNIP4 protein between L4 EYA4+ and L2/3 neurons.
- **Proof**: [E07]
- **Evidence basis**: Fig. 7c,d (immunostaining + quantification; one-way ANOVA + two-sided Tukey).
- **Sources**:
  - direction/stage ← paper.pdf p11 «mean intensity of KCNIP4 in neuronal somas was signiﬁcantly higher in L4 EYA4+ neurons at intermediate disease stages compared to controls, and lower in supragranular (L2/3) neurons at intermediate and high stages compared to controls» [result]
  - n=6 per group ← paper.pdf p11 Fig.7 caption «(n = 6 donors per disease group)» [input]
- **Dependencies**: C05
- **Tags**: KCNIP4, immunohistochemistry, protein, EYA4

## C07: AAV Kcnip4 overexpression reduces neuronal hyperactivity in vitro
- **Statement**: In primary mouse cortical neurons, AAV (PHP.eB-CaMKIIa-Kcnip4-P2A-EGFP) transduction significantly reduced spontaneous activity (decreased Ca2+ transient event frequency at DIV14) both under basal conditions and following 200 nM Aβ1–42 oligomer treatment, compared to GFP-only control neurons; no TUNEL+ neurons were detected, excluding AAV toxicity.
- **Status**: supported
- **Falsification criteria**: No difference in Ca2+ transient frequency between Kcnip4 and control neurons, or effect attributable to toxicity.
- **Proof**: [E08]
- **Evidence basis**: Fig. 8a–c (calcium imaging; 4 wells/condition, 2 fields/well, 3 GFP+ neurons/field); Supplementary Fig. 11a (TUNEL).
- **Sources**:
  - reduction basal + Aβ ← paper.pdf p10 «neurons transduced with Kcnip4 exhibited a signiﬁcant reduction in spontaneous activity, as evidenced by decreased Ca2+ transient events frequency, both under basal conditions and following Aβ1–42 oligomers treatment, compared to control neurons expressing GFP alone» [result]
  - 200 nM Aβ1–42 ← paper.pdf p10 «treated with 200 nM amyloid-β 1–42 (Aβ1–42) oligomers» [input]
- **Dependencies**: C05
- **Tags**: KCNIP4, AAV, calcium imaging, hyperexcitability, in vitro

## C08: AAV Kcnip4 in AppSAA mice reduces c-Fos and Arc and reduces microgliosis
- **Statement**: In 12-month-old humanized App knock-in (AppSAA) mice injected retro-orbitally with 1×10¹¹ vg Kcnip4 AAV, transduced (GFP+) neurons showed reduced c-Fos+ proportion and reduced Arc staining intensity vs GFP− neurons, and elevated c-Fos/Arc in AppSAA vs WT was reversed by Kcnip4 AAV; a small but significant decrease in IBA1 staining (reduced microgliosis) was observed, whereas amyloid plaque burden (anti-human Aβ) and GFAP (astrogliosis) were unchanged.
- **Status**: supported
- **Falsification criteria**: No reduction of c-Fos/Arc in GFP+ vs GFP− AppSAA neurons; or Kcnip4 significantly altering amyloid burden.
- **Proof**: [E09]
- **Evidence basis**: Fig. 8e–u (WB, transduction, amyloid/GFAP/IBA1, c-Fos, Arc; 5–7 mice/group; two-sided t-test / one-way ANOVA + Tukey).
- **Sources**:
  - c-Fos/Arc reduction ← paper.pdf p13 «Kcnip4 AAV-mediated delivery in 12-month-old AppSAA mice reduced the proportion of c-Fos+ neurons in the GFP+ compared to GFP- populations» [result]
  - amyloid ns, GFAP ns, IBA1 down ← paper.pdf p12 «no signiﬁcant differences were found in amyloid plaques ... Reactive astrogliosis ... remained unchanged ... small but signiﬁcant decrease in IBA1 staining, suggesting reduced microgliosis» [result]
  - 1×10¹¹ vg ← paper.pdf p11 «with either Kcnip4 AAV or control AAV (1 × 10^11 vg, retroorbitally)» [input]
- **Dependencies**: C05, C07
- **Tags**: KCNIP4, AppSAA, c-Fos, Arc, IBA1, in vivo, immediate-early genes

## C09: hdWGCNA identifies KCNIP4-containing candidate resilience modules
- **Statement**: hdWGCNA co-expression analysis of Ex5 (L4 IT) neurons identified candidate resilience modules — M2 and M3 in BA17, and M2, M3, M4 in BA9 — whose network genes were predominantly upregulated at early stages; KCNIP4 is among the top-10 hub genes (Ex5 BA17-M2: KCNIP4, CADM2, NRG3, ADGRB3, NRXN1, NALF1, NEGR1, FGF14, TENM2, CUX1). The integrated module network is enriched for trans-synaptic signaling, calcium homeostasis, and neuronal excitability.
- **Status**: supported
- **Falsification criteria**: KCNIP4 absent from resilient-module hub genes, or modules not enriched for synaptic/calcium/excitability functions.
- **Proof**: [E05]
- **Evidence basis**: Fig. 6c,d; Supplementary Data 10.
- **Sources**:
  - BA17 M2/M3, BA9 M2/M3/M4; hub genes ← paper.pdf p9 «two candidate resilient modules, M2 and M3 ... top 10 hub genes ... KCNIP4, CADM2, NRG3, ADGRB3, NRXN1, NALF1, NEGR1, FGF14, TENM2, and CUX1 (for M2) ... For Ex5 neurons from BA9, we identiﬁed three candidate resilient modules: M2, M3, and M4» [result]
- **Dependencies**: C04, C05
- **Tags**: hdWGCNA, co-expression module, hub gene, KCNIP4

## C10: Three L4 IT subtypes exist; Ex5 is BA17-enriched and cross-dataset validated
- **Statement**: Three molecular L4 IT excitatory subtypes were defined across neocortex — Ex5 (CUX2/RORB/EYA4/LAMA3), Ex6 (RORB/MME), Ex7 (RORB/GABRG1). scANVI prediction across reference datasets showed Ex5 is BA17-enriched: 63,870 cells (34.42%) of 185,565 excitatory cells in the BA17 reference (Jorstad et al. 2023), vs 2,152 (0.33%) of 660,751 in SEA-AD DLPFC, 19,360 (3.03%) of 637,968 in Green et al., 3,361 (3%) of 112,143 in Mathys et al., and 7,943 (4.36%) of 182,140 in the authors' BA9 dataset.
- **Status**: supported
- **Falsification criteria**: Ex5 not preferentially mapping to BA17-derived reference clusters, or L4 IT not resolving into these three subtypes.
- **Proof**: [E01, E02, E10]
- **Evidence basis**: Fig. 1j (cosine distance), Fig. 3 (markers + Xenium spatial + ISH), Fig. 3l; Supplementary Fig. 6.
- **Sources**:
  - 63,870 (34.42%)/185,565; 2152 (0.33%)/660,751; 19,360 (3.03%)/637,968; 3361 (3%)/112,143; 7943 (4.36%)/182,140 ← paper.pdf p5 «the number of Ex5 cells predicted in the BA17 reference dataset was high: 63,870 cells (34.42%) out of 185,565 excitatory cells. In contrast, it was low in the prefrontal cortex reference datasets: 2152 cells (0.33%) out of 660,751 ... 19,360 cells (3.03%) out of 637,968 in Green et al.; 3,361 cells (3%) out of 112,143 in Mathys et al., compared with 7943 cells (4.36%) out of 182,140 in our BA9 dataset» [result]
- **Dependencies**: none
- **Tags**: L4 IT subtypes, Ex5, Ex6, Ex7, scANVI, cross-dataset validation
