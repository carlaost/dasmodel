# Figure 6: Transcriptome signatures of resilience in Ex5 L4 IT neurons
- **Source**: Figure 6, §"Genes and pathways associated with resilience in the AD neocortex"
- **Caption**: "a Heatmaps displaying 'high-confidence' DE genes shared across BA9 and BA17 at early and late stages in prototype vulnerable excitatory (Ex2; L2/3 IT) and prototype resilient (Ex5; L4 IT) neuronal subtypes… colored based on log2 fold change values. b Biological function network of the genes represented in (a)… Node size reflects the number of connections… c Co-expression networks for vulnerable (Ex2) and resilient (Ex5) subtypes from BA9 and BA17, identified by hdWGCNA. The top 10 intra-module connected genes, ranked by kME, for each module are represented… d Enrichment network for candidate resilient modules in Ex5 L4 IT neurons. The top 50 highly co-expressed genes from modules M2, M3, and M4 (BA9) and modules M2 and M3 (BA17)… Colors represent contributions from BA9 (moss), BA17 (teal), or both (red)."
- **Screenshot**: figure6.png
- **Figure type**: mixed (heatmaps + biological-function network + hdWGCNA kME dot plots/networks)
- **Extraction method**: exact_from_labels (gene/module labels, kME axes) + visual_description
- **Reading confidence**: medium (dense networks; kME read `≈`)

## Panel a (heatmaps, Ex2 vs Ex5; color = average log2FC)
Ex5 (L4 IT) early-upregulated high-confidence genes incl. KCNIP4, PTPRT, GRIN2A, GRM7, LINGO2, CSMD1, AUTS2, UBE2E2, SLC24A2, TAFA1, ADGRB3, NRG3, FGF14, SLC8A1, DLG2, TENM2, NRXN1, SYN3, NCAM2. Ex2 (L2/3 IT) panel shows contrasting/downregulated pattern. Color scale ~ −0.75 to +1.25 average log2FC.

## Panel b (biological-function network)
Function nodes contributed by Ex2 (vulnerable) and Ex5 (resilient): cell-cell adhesion via plasma-membrane adhesion molecules; anterograde trans-synaptic signaling; chemical synaptic transmission; response to amyloid-beta; regulation of monoatomic cation transmembrane transport; calcium ion transmembrane transport/import; regulation of sodium ion transport; transport along microtubule; cellular response to hypoxia; protein localization to membrane. Genes mapped onto these (TENM2, SDK1, KIRREL3, PTPRT, NRXN1, SYT1, RORA, KCND2, GRM7, DLG2, CHRM3, MAGI2, SLC8A1, IGF1R, NALF1, CACNA1C, KCNIP4, CACNA1B, DPP6/10, SLC24A2, UTRN, DMD, PRKCE, FGF14, LRRC4C, CDH12, IL1RAPL1, GRIN2A).

## Panel c (hdWGCNA modules — top-10 hub genes by kME)
- **Ex5 BA17-M2**: CUX1, TENM2, FGF14, NEGR1, NALF1, NRXN1, ADGRB3, NRG3, CADM2, KCNIP4
- **Ex5 BA17-M3**: RIMS2, SNTG1, IQCJ-SCHIP1, RALYL, NLGN1, ANKS1B, RORA, CNTN5, LRRC4C, PTPRD
- **Ex5 BA9-M2**: MYT1L, CACNA1C, ERC2, MAPK10, KAZN, CACNA1B, AGBL4, DOCK3, CACNA2D3, DLGAP2
- **Ex5 BA9-M4**: NRXN1, NRG3, ADGRB3, CADM2, MAGI2, CNTNAP2, RBFOX1, CSMD1, PTPRD, KCNIP4
- (Ex2 modules M1–M9 also shown; e.g. Ex2-BA9-M4 contains GRIN2A, AUTS2, IL1RAPL1, KCNIP4.)
- Enrichment dot plots per region (BA9 M1–M9; BA17 M1–M5/M1–M3): terms incl. trans-synaptic signaling, chemical synaptic transmission, calcium ion import/transport, regulation of membrane potential, glutamate receptor activity, synapse organization, learning/memory.

## Panel d (candidate resilience-module enrichment network, Ex5 BA9-M2/M3/M4 + BA17-M2/M3)
Function groups: gated channel activity, trans-synaptic signaling, channel regulator activity, calcium ion transmembrane transporter activity, glutamate receptor activity, netrin-activated signaling, calcium ion import across plasma membrane. Relevant genes: GRIN2A, GRM5, GRM7, CACNA1B, CACNA1C, CACNG5, KCNIP4, NALF1, NRXN1, NLGN1, NRG3, PTPRD, FGF14.

## Trend summary
Resilient Ex5 modules (up early) converge on trans-synaptic signaling, calcium homeostasis, and
neuronal excitability, with KCNIP4 recurring as a hub. Supports C04, C05, C09.
