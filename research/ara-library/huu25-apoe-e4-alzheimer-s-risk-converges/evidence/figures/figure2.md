# Figure 2: Identification and annotation of fine resolution ERC subclusters in the snRNA-seq data
- **Source**: Figure 2, §2.3
- **Caption**: "A. tSNE plot of 122k nuclei across 38 fine resolution subclusters. B. Hierarchical clustering (method='ward.D2') of fine resolution subclusters. C. Violin plot of APOE log-normalized expression (logcounts) across fine subclusters. D. spatialLIBD spatial registration heatmap showing the correlation between enrichment t-statistics for the ERC SpDs and snRNA-seq subclusters. Inset shows SRT spotplot of SpDs for Br5517. High confidence matches (cor > 0.5, merge ratio = 0.1) marked 'X', low confidence '*'. Related to Figure 1, Fig S15–S29, Fig S43, Table S5."
- **Screenshot**: figure2.png
- **Figure type**: mixed
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Panel A (qualitative_plot, tSNE)**: ~122,004 nuclei in 2D tSNE, colored by 38 fine subclusters; large orange excitatory-neuron mass, distinct glial (Astro green, Oligo/OPC orange-brown, Micro purple) and vascular (pink) islands.
- **Panel B (diagram, dendrogram)**: ward.D2 hierarchical clustering of the 38 subclusters; branches group by broad type — Inhib (Pax6, Chandelier, Pvalb, Sst, Lamp5_Lhx6, Vip), Excit (L2, L6b, L6_CT, L5.1/5.2, L2.3_5.1/5.2, L2), Macro, Micro.1-5, Vasc.PC/Endo/VLMC, Oligo.1-5, Astro.1-5, OPC.1-5. Scale bar to ~1200.
- **Panel C (quantitative_plot, violin)**: APOE logcounts across the 38 subclusters (0–~6 axis). Highest in Astro subclusters (esp. Astro.1), moderate in Micro/Macro/Vasc.PC, low in Oligo/OPC and neurons.
- **Panel D (quantitative_plot, heatmap)**: correlation of 38 subclusters (rows) vs 9 ERC SpDs (columns). "X" matches: Astro subclusters↔L1~Sp9D5; Oligo subclusters↔WM~Sp9D6; Vasc↔Vasc~Sp9D8; Inhib subclusters↔Inhib~Sp9D9; Excit.L5 subclusters↔L5~Sp9D3; Excit.L6↔L6~Sp9D4; Excit.L2_5↔both L2.3 and L5. Weak matches ('*') for Micro/Macro↔Vasc and OPC↔L1.

## Trend summary
38 fine subclusters across 8 broad types; APOE highest in astrocytes (esp. Astro.1); spatial registration cleanly maps subcluster→SpD (all Oligo→WM~Sp9D6, Astro→L1). Grounds concept "Fine subcluster" and claims C01, C04.
