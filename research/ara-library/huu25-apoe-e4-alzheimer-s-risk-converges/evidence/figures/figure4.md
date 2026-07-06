# Figure 4: APOE carrier status impacts cell type gene expression predominantly in oligodendrocytes
- **Source**: Figure 4, §2.5
- **Caption**: "A. Bar plot of number of FDR<0.05 DE genes, up or downregulated in APOE E4+ relative to E2+ for the full dataset (carrier) and ancestry-specific analyses (carrier_AA, carrier_EA). B. Volcano plot for carrier DE analysis for astrocytes (Astro), oligodendrocytes (Oligo), excitatory (Excit), and inhibitory (Inhib) neurons. C. logFC heatmap for up to top 5 DEGs per broad cell type. D. clusterProfiler dot plot of top BP GO terms for carrier model DEGs. E-F. cleanY boxplots for C1QL3 in Oligo (E) and RIPK2 in Vasc / JUP in Astro over carrier and ancestry (F). Related to Fig S37, S38, S39, Table S11, S12."
- **Screenshot**: figure4.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (Panel A) + visual_description
- **Reading confidence**: medium

## Panel A — DEG counts by broad cell type (carrier, E4+ vs E2+, FDR<0.05)
Direction/ranking per §2.5: "Oligo had the most DEGs, followed by Astro, Excit and Inhib neurons... very few DEGs in other broad cell types, including microglia."

| Broad cell type | Relative DEG count |
|-----------------|--------------------|
| Oligo | highest (largest bar) |
| Astro | 2nd |
| Excit | 3rd |
| Inhib | 4th |
| Micro / Macro / OPC / Vasc | very few |

Ancestry-specific: Astro AA = 98 DEGs (per §2.5, C05). Exact per-bar values are not all printed; authoritative counts in `logic/claims.md`.

## Visual description (other panels)
- **B (volcanos)**: Astro, Oligo, Excit, Inhib. Oligo panel is densest (many colored FDR<0.05 points), consistent with Oligo having the most DEGs. NPTXR labeled as upregulated across Astro/Oligo/Excit.
- **C (heatmap, logFC)**: rows = broad cell types (Astro, Macro, Micro, Oligo, OPC, Vasc, Excit, Inhib); columns = top DEGs (LINC01608, COL4A5, CEDORA, ABCA9, ST18, HSPE1, LDB3, LPAR1, DAB2, PLCE1, RGN, GAN13, RAPGEF4, ELL2, STEAP2, ATP1B3, LY75, FGL2, PLPPR4, CACNB9, AKAP5, NPTXR, DACH1, SRARP, DACH1, C1QL3). Cell-type-specific patterns; NPTXR shared up.
- **D (GO dot plot)**: BP terms per DE_class (Astro_down/up, Oligo_up, Micro_down, Oligo_up). Astro up: synaptic membrane/trans-synaptic terms; Oligo up: substrate-adhesion / extracellular-matrix terms; incl. chaperone-mediated folding, cis-Golgi terms.
- **E (boxplot, C1QL3 in Oligo)**: higher in E4+ than E2+ (upregulated); p<3.65e-02, logFC ≈0.57 shown.
- **F (boxplots)**: RIPK2 in Vasc — downregulated in EA E4+ (carrier_EA FDR<0.05, logFC≈−2.27), not AA; JUP in Astro — upregulated in E4+ with large AA vs EA difference.

## Trend summary
At broad resolution APOE E4+ DEGs are most abundant in oligodendrocytes; ancestry strongly modifies cell-type DEGs (Astro AA 98; RIPK2 EA-specific; JUP AA/EA divergent). Supports C01, C05.
