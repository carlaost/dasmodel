# Figure 5: Fine subcluster differential expression shows interruption of Oligo maturation
- **Source**: Figure 5, §2.6
- **Caption**: "A. Volcano plots of Oligo.3, genes with FDR<0.05 or absolute logFC>1 color highlighted. B. clusterProfiler dotplot of GO term enrichment for Oligo.3 and Astro.3. C. Volcano plot of Astro.3. D. tSNE plot of OPC and Oligo subclusters with trajectory analysis. E. Centered and scaled log-normalized expression scDotPlot of Oligo subcluster marker genes. F. Proposed model for oligodendrocyte subcluster classification and maturation trajectory in APOE E2+ and E4+ carriers. Created in BioRender. Related to Fig S29, S37, S38, S41, S43, S46, S47, Table S13, S14."
- **Screenshot**: figure5.png
- **Figure type**: mixed
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **A (volcano, Oligo.3)**: log(FC) (x) vs −log10 p (y). Many colored points (purple = FDR<0.05, red = |logFC|>1). Labeled up genes (right/top): FOS, ZFY9, GOLIM4, COL18A1, etc.; labeled down genes (left): PLP1, MAG, MAL-related. Reflects 679 up / 343 down (per C01).
- **B (GO dot plot, Oligo.3 & Astro.3)**: down-DEG terms (Oligo.3_down, Astro.3_down): myelination, ensheathment of neurons, axon ensheathment, myelin assembly, substantia nigra development, oligodendrocyte development/differentiation; up-DEG terms (Oligo.3_up): modulation of chemical synaptic transmission, regulation of trans-synaptic signaling, metal/monoatomic/calcium ion transport. Dot size = GeneRatio, color = p.adjust.
- **C (volcano, Astro.3)**: shares many downregulated DEGs with Oligo.3 (e.g. OPALIN most significant down); labeled genes incl. OPALIN, PLP1, CARNS1, CD22.
- **D (quantitative_plot, tSNE + trajectory)**: OPC (OPC.1-5) and Oligo (Oligo.1-5) subclusters in tSNE space with a fitted trajectory (MST/pseudotime). Path: OPC.1-4 → OPC.5 → Oligo.3 → Oligo.4/Oligo.5 → Oligo.1/Oligo.2. Oligo.3 sits nearest OPCs; Oligo.1/Oligo.2 are the far (mature) endpoints.
- **E (dot plot, Oligo markers)**: columns = OPC.5, Oligo.3, Oligo.5, Oligo.2, Oligo.1, Oligo.4 (clustered); rows = marker genes (ATP10A, ABCG2, PRKCH, ADGRF5, LRIG3, BIN1, TSC22D3, LAMA2, KCTD1, NTRK3, LINGO2, KCND2, KCNJ3, GPM6A, LINC00609, MTX2, ITGAV, ANK3, OPALIN, EMC10, GOLGA7, ERBB4). Oligo.1/Oligo.2 high for mature markers (OPALIN, MOG); Oligo.3 shares markers (LINGO2, GPM6A, KCNJ3) with OPC.5. Dot size = percent of cells, color = scaled expression.
- **F (diagram, proposed model)**: OPC.5 → Non-myelinating Oligo.3. In E2+: Astro.3 gives "correct oligo maturation signal (OPALIN, PLP1)" → Oligo.3 in differentiating state → matures into myelinating Oligo (Oligo.1+2). In E4+: Astro.3 gives "reduced oligo maturation signal" → Oligo.3 in immune-reactive state (FOS, TLR2, STAT1, STAT4) → reduced maturation into myelinating Oligo.

## Trend summary
DEGs converge on Oligo.3; down-DEGs = myelination/differentiation, up-DEGs = calcium/synaptic/inflammatory; trajectory + markers place Oligo.3 as the least-mature, OPC-proximal (non-myelinating) subcluster whose maturation is modeled as stalled in E4+. Supports C01, C02, C04.
