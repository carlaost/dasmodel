# Figure 3: APOE carrier status interacts with ancestry to impact gene expression in distinct SpDs
- **Source**: Figure 3, §2.4
- **Caption**: "A. Number of DEGs (FDR<0.05), up or downregulated in APOE E4+ relative to E2+ for the full dataset (carrier) and ancestry-specific analyses (carrier_AA, carrier_EA). B-C. Volcano plots for carrier DE analysis for Vasc~Sp9D8 (B) and WM.uf~Sp9D7 (C). D. logFC heatmap for up to top 5 DEGs in each SpD. E. cleanY log-normalized expression boxplots for KLK6 comparing E2+ and E4+ in Vasc~Sp9D8 and WM.uf~Sp9D7. F. cleanY expression boxplot of PEX14 in WM.uf~Sp9D7 comparing E2+/E4+ over ancestry groups. G. clusterProfiler dot plot of top biological-process GO terms for E4+ vs E2+ DEGs. Related to Fig S35, S37, S38, Table S9, S10."
- **Screenshot**: figure3.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (Panel A count labels) + visual_description
- **Reading confidence**: medium

## Panel A — DEG counts by SpD (carrier model, E4+ vs E2+, FDR<0.05)
Bar-label counts read from the figure; up/down direction assigned per §2.4 text. Only labeled bars shown.

| SpD | Visible count labels | Text-confirmed |
|-----|----------------------|----------------|
| Vasc~Sp9D8 | 8 and 22 | 22 upregulated, 8 downregulated (most DEGs) |
| WM.uf~Sp9D7 | 10, 2, 19 (carrier / carrier_AA has 15 per text) | 2nd most DEGs; AA-specific = 15 |
| carrier_AA WM.uf | 7 (up), 8 (down) region | AA WM.uf = 15 DEGs total |
| Other GM SpDs (L2.3, LD, Inhib, L5, L6) | few / near zero | 21 total across Inhib~Sp9D9, L5~Sp9D3, L6~Sp9D4 (per §3) |

Note: exact per-bar up/down attribution beyond Vasc (22/8) is not unambiguous from the plot alone; authoritative counts are in `logic/claims.md` (C03, C05) with verbatim text sources.

## Visual description (other panels)
- **B (volcano, Vasc~Sp9D8)** and **C (volcano, WM.uf~Sp9D7)**: log2FC (x) vs −log10 p (y); colored points = FDR<0.05 and/or |logFC|>1. Labeled genes incl. CNTN2, MAL, KLK6, NPTX2 (Vasc); MAP2, GPM6A (WM.uf).
- **D (heatmap, logFC)**: rows = 9 SpDs, columns = top DEGs (GAD1, KLK6, CNDP1, UGT8, HHIP, TMEM144, CDR2L, TTYH2, JAZF1, INPP1, MAP2, CPNE8, CDYL2, FAM155CP, ALDH3B1, NVE2, NPTX2). Shared DEGs visible: NPTX2 up in Vasc & L5; KLK6 down in WM.uf & Vasc. Stars denote FDR<0.05/<0.01/<0.001.
- **E (boxplots, KLK6)**: cleanY expression higher in E2+ than E4+ in both Vasc~Sp9D8 and WM.uf~Sp9D7 (downregulated in E4+).
- **F (boxplot, PEX14 in WM.uf~Sp9D7)**: split by ancestry (carrier_AA vs carrier_EA); EA shows E4+ downregulation, AA does not.
- **G (GO dot plot)**: BP terms across DE_class groups (L5~Sp9D3_up, L6~Sp9D4_down, Vasc~Sp9D8_down, WM.uf~Sp9D7_down/_up). Myelination, axon ensheathment, oligodendrocyte differentiation, learning/memory terms; dot size = gene ratio, color = p.adjust.

## Trend summary
APOE E4+ DEGs concentrate in vascular and U-fiber WM domains; downregulated genes are myelination-related; changes differ by ancestry (AA-heavy in WM.uf; PEX14 EA-specific). Supports C03, C05.
