# Figure 6: Common gene expression signature across oligodendrocytes and white matter associated with APOE carrier status and tau pathology
- **Source**: Figure 6, §2.8
- **Caption**: "A. MOFA (MOFAcellulaR) heatmap. Input gene expression views (SRT SpDs and snRNA-seq subclusters) in top orange rows, colors = variance explained (R2) by donor-level MOFA factor scores (columns). Purple heatmap = p-values for association between donor factor scores and covariates (rows). Bottom heatmap = 30 donors and their factor scores with covariate annotations. B. Boxplot of MOFA factor 3 donor scores over APOE carrier status, presence of pTau pathology, and sex. C. Boxplot of factor 3 scores over APOE carrier status combined with pTau (t−/t+). D. Heatmap of factor-3 gene-level weights for top 5 signature genes across select views. E. Heatmap of APOE carrier DE logFC for the top MOFA factor 3 signature genes shown in D. Related to Table S17."
- **Screenshot**: figure6.png
- **Figure type**: mixed
- **Extraction method**: exact_from_labels (association p/FDR from text) + visual_description
- **Reading confidence**: medium

## Panel A/B — factor 3 associations (from §2.8 text)
| Association | Value |
|-------------|-------|
| Number of MOFA factors | 7 |
| Views with high factor-3 R² | WM~Sp9D6 (SRT); Oligo.3, Oligo.4, Oligo.5, Excit.L5.2 (snRNA-seq) |
| Factor 3 vs E4+ vs E2+ | p = 0.014, FDR = 0.095 (nominal) |
| Factor 3 vs sex (F vs M) | p = 0.056, FDR = 0.395 |
| Factor 3 vs pTau | significant negative association, FDR < 0.05 |

## Visual description
- **A (heatmap)**: top orange block = R² per view (rows: 38 subclusters + 9 SpDs) × 7 factors (columns); factor 3 column shows high R² concentrated in WM~Sp9D6 and Oligo.3-5. Middle purple block = covariate association p-values (APOE_carrier, Ancestry, taupathy, Sex, Age, Braak, CERAD) × factors; factor 3 shows signal for APOE_carrier and taupathy. Bottom block = 30 donors × factors with APOE/ancestry/tau/age/sex annotation bars.
- **B (boxplots)**: three facets — APOE_carrier (E4+ higher than E2+, FDR=9.52e-02); taupathy (t− higher than t+, FDR=2.16e-02); Sex (F vs M, FDR=3.95e-01). Points = donors.
- **C (boxplot)**: factor-3 scores across combined APOE × pTau categories (E2+ t−, E2+ t+, E4+ t−, E4+ t+); highest for E4+ / t− (E4+ with no pTau).
- **D (heatmap, gene weights)**: top/bottom factor-3 signature genes (CNTN6, GPC6, CABLES1, GRIP1, SLC4A4, ADGRL2, NEBL, PTPRG, UTRN, GRIK1, KCNQ5, SNTG1, BX3GLCT, CRTAP, CAMK2A, TDRD7, CPNE4, HES5, SYNPO, MGAT5B, and negatives CDH19, NKX6-2, RNASE1, SELENOP, LINC01792, NBPF12, OARD1, DPYSL5, ENPP6, LRRG33, PLS1, TGFBRAP1, WSB1, CDH12, GJC2, LRP2, ST18, TRIM59) × views (Multi, Oligo.3, Oligo.4, Oligo.5, Excit.L5.2, WM~Sp9D6). positive_weight annotation shown.
- **E (heatmap, logFC)**: same gene rows, APOE carrier DE logFC per view; stars mark E2+/E4+ DEGs. Top signature genes overlap Oligo.3 upregulated E4+ DEGs; some WM~Sp9D6-only genes (SYNPO, HES5, MGAT5B) not in Oligo.3-5.

## Trend summary
An integrative MOFA factor (factor 3) spanning non-myelinating oligodendrocytes (Oligo.3-5) and WM~Sp9D6 associates with APOE carrier status (nominal, p=0.014) and pTau pathology (FDR<0.05), independently corroborating the DGE convergence and adding WM-specific genes. Supports C07.
