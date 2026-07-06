# Claims

Numeric values are grounded to the paper text with verbatim «quotes». Tags: `[result]` = a value the
study's analysis produced (reported in Results/Methods). Sources cite the PMC full text section.

## C01: APOE E4+ differential expression converges on a single oligodendrocyte subcluster (Oligo.3)
- **Statement**: In fine-resolution snRNA-seq pseudobulk DGE between APOE E4+ and E2+ carriers, the majority of DEGs fall in oligodendrocyte subcluster Oligo.3, with 679 upregulated and 343 downregulated genes at FDR<0.05.
- **Status**: supported
- **Falsification criteria**: Re-running the covariate-adjusted pseudobulk DGE and finding DEGs are not concentrated in Oligo.3, or that Oligo.3 up/down counts differ materially from 679/343 at FDR<0.05.
- **Proof**: [E01, E04]
- **Evidence basis**: Direct DEG counts for Oligo.3 in the fine-subcluster carrier analysis (Figure 5A, Table S13).
- **Interpretation**: Convergence on one subtype implies a subtype-specific, not diffuse, locus of APOE risk in the ERC.
- **Sources**:
  - 679 up / 343 down in Oligo.3 ← §2.6 «The majority of DEGs were found in oligodendrocyte subcluster Oligo.3 ( Figure 5A , Fig S41 , Table S13 , 679 upregulated and 343 downregulated genes, FDR<0.05)» [result]
- **Dependencies**: none
- **Tags**: oligodendrocyte, DGE, snRNA-seq, APOE

## C02: Oligo.3 downregulated genes are myelination / oligodendrocyte-differentiation genes
- **Statement**: Genes downregulated in Oligo.3 in E4+ carriers include canonical myelination and oligodendrocyte-differentiation genes (PLP1, MAG, MAL, MBP, SOX10, OPALIN; MAPT also downregulated), while upregulated genes (FOS, TLR2, STAT1, STAT4) relate to calcium-ion response and inflammation.
- **Status**: supported
- **Falsification criteria**: These named genes not being significant DEGs in the stated directions in Oligo.3.
- **Proof**: [E04, E05]
- **Evidence basis**: Named DEGs and GO enrichment for Oligo.3 (Figure 5A–B, Table S13/S14).
- **Interpretation**: Suggests stalled maturation and an immune-reactive Oligo.3 state in E4+ carriers.
- **Sources**:
  - Downregulated set ← §2.6 «Downregulated genes in Oligo.3 were implicated in myelination and oligodendrocyte differentiation, such as PLP1 , MAG , MAL , MBP , SOX10 , and OPALIN» [result]
  - Upregulated set ← §2.6 «Upregulated Oligo.3 DEGs included FOS , TLR2 , STAT1 , and STAT4 , which are all involved in response to calcium ion» [result]
- **Dependencies**: C01
- **Tags**: myelination, GO enrichment, inflammation, oligodendrocyte

## C03: In spatial data, APOE-dependent DEGs are highest in vascular (Vasc~Sp9D8) and U-fiber WM (WM.uf~Sp9D7) domains
- **Statement**: In Visium pseudobulk DGE (E4+ vs E2+, adjusting for ancestry and sex), the vascular domain Vasc~Sp9D8 has the most DEGs (22 upregulated, 8 downregulated, FDR<0.05) and the U-fiber white-matter domain WM.uf~Sp9D7 has the second most; downregulated genes across WM/vascular domains are enriched for myelination / axon-ensheathment GO terms.
- **Status**: supported
- **Falsification criteria**: A different SpD carrying the most DEGs, or Vasc~Sp9D8 counts departing from 22/8 at FDR<0.05.
- **Proof**: [E03]
- **Evidence basis**: SpD-level DEG counts and volcano plots (Figure 3A–C), GO dot plot (Figure 3G).
- **Interpretation**: Consistent with WM being an early site of AD-related change and APOE E4+ blood-brain-barrier dysfunction.
- **Sources**:
  - 22 up / 8 down in Vasc~Sp9D8; WM.uf second ← §2.4 «The highest number of differentially expressed genes (DEGs, FDR < 0.05, 22 upregulated and 8 downregulated) was localized to Vasc~Sp 9 D 8» and «the U-fiber WM SpD (WM.uf~Sp 9 D 7 ) had the second most DEGs» [result]
- **Dependencies**: none
- **Tags**: spatial transcriptomics, white matter, vasculature, DGE

## C04: Oligo.3 is the most OPC-proximal (least mature) oligodendrocyte subcluster
- **Statement**: Trajectory analysis places Oligo.3 closest to oligodendrocyte precursor cells (OPC) and distinct from the most mature myelinating subclusters Oligo.1/Oligo.2, supporting a non-myelinating (candidate pre-myelinating) identity; Oligo.3 marker genes (LINGO2, GPM6A, KCNJ3) are shared with OPC.5.
- **Status**: supported
- **Falsification criteria**: Trajectory / marker analysis placing Oligo.3 among mature myelinating subclusters instead.
- **Proof**: [E06]
- **Evidence basis**: TSCAN trajectory and Oligo marker dot plot (Figure 5D–E).
- **Interpretation**: A maturation-stalled Oligo.3 in E4+ could explain reduced myelinating Oligo.1/Oligo.2 frequency.
- **Sources**:
  - Oligo.3 most OPC-related / immature ← §2.6 «Trajectory analysis revealed that Oligo.3 was most closely related to oligodendrocyte precursor cells (OPC), suggesting Oligo.3 represented a more immature cell state compared with Oligo.1 and Oligo.2, the most mature Oligo subclusters» [result]
- **Dependencies**: C01
- **Tags**: trajectory, maturation, OPC, oligodendrocyte

## C05: APOE-associated DEGs are strongly modified by ancestry
- **Statement**: Ancestry-specific analyses yield largely non-overlapping DEG sets: e.g. in the U-fiber WM domain, AA donors have 15 DEGs vs only 2 downregulated DEGs in EA donors; at broad cell-type level, 98 DEGs are found in astrocytes in AA donors; Oligo.3 shows ancestry-specific DEGs with some genes regulated in opposite directions.
- **Status**: supported
- **Falsification criteria**: AA and EA analyses yielding statistically indistinguishable DEG sets/counts.
- **Proof**: [E03, E04, E07]
- **Evidence basis**: Ancestry-specific DEG counts (Figure 3A, Figure 4A, Fig S37).
- **Interpretation**: Molecular correlate of the epidemiological observation that APOE risk/protection differs by ancestry.
- **Sources**:
  - WM.uf AA 15 vs EA 2 ← §2.4 «we identified 15 DEGs in WM.uf~Sp 9 D 7 for AA, while EA donors only had 2 downregulated DEGs (1 in each WM SpD, Fig S37A )» [result]
  - Astro AA 98 ← §2.5 «Ancestry-specific analysis identified 98 DEGs in Astro in AA donors» [result]
- **Dependencies**: C01, C03
- **Tags**: ancestry, DGE, health disparities

## C06: APOE-associated DEGs are strongly sex-biased (male-dominated)
- **Statement**: Sex-specific DGE detects far more DEGs in males than females: 91 male DEGs vs 1 female DEG (PAX6) in WM domains for Visium; 948 male vs 2 female DEGs at broad cell-type level; and 1,830 male DEGs in Oligo.3, with the imbalance attributed to the uneven sex representation (21/30, 70% male).
- **Status**: supported (interpretation-limited by female sample size)
- **Falsification criteria**: Comparable male and female DEG counts, or the male excess disappearing after correcting for sample size.
- **Proof**: [E03, E04]
- **Evidence basis**: Sex-specific DEG counts (Fig S38); cohort sex ratio (§2.1, §2.4).
- **Interpretation**: Likely driven by low female N; consistent with prior male-specific Oligo AD changes.
- **Sources**:
  - 91 male vs 1 female (PAX6), 70% male ← §2.4 «we identified 91 male DEGs in WM.uf~Sp 9 D 7 , and 1 female DEG, PAX6 , in WM~Sp 9 D 6» and «uneven representation of sexes across the cohort (21/30 male; 70%)» [result]
  - 948 male vs 2 female (broad) ← §2.5 «Sex-specific DEGs were detected mostly in males (948 DEGs)... Only 2 DEGs were detected in females» [result]
  - 1,830 male DEGs in Oligo.3 ← §2.6 «Oligo.3 sex-specific DEGs were only detected in males (1,830 DEGs, Fig S38C )» [result]
- **Dependencies**: C01, C03
- **Tags**: sex differences, DGE, power

## C07: A MOFA multicellular factor (factor 3) links non-myelinating oligodendrocytes and white matter to APOE status and pTau
- **Statement**: Of 7 MOFA factors computed jointly from snRNA-seq subclusters and SRT SpDs, factor 3 explains high variance in WM~Sp9D6 and Oligo.3-5; higher factor-3 donor scores are nominally associated with E4+ vs E2+ (p=0.014, FDR=0.095) and significantly (negatively) associated with pTau pathology (FDR<0.05).
- **Status**: supported (APOE association nominal; pTau association FDR<0.05)
- **Falsification criteria**: Factor 3 not associating with APOE/pTau, or the reported p/FDR values not reproducing.
- **Proof**: [E08]
- **Evidence basis**: MOFA association heatmap and factor-3 boxplots (Figure 6A–C, Table S17).
- **Interpretation**: An independent, integrative signal corroborating the DGE convergence on oligodendrocytes/WM and tying it to pathology.
- **Sources**:
  - 7 factors ← §2.8 «We calculated 7 MOFA factors from both snRNA-seq subclusters and SRT SPDs» [result]
  - E4+ p=0.014, FDR=0.095 ← §2.8 «Higher factor 3 scores were nominally associated with E4+ vs. E2+ (p = 0.014, FDR = 0.095, Figure 6B )» [result]
  - pTau negative association FDR<0.05 ← §2.8 «MOFA factor 3 donor-level scores also had a significant negative association (FDR< 0.05) with pTau scores in adjacent ERC tissue sections» [result]
- **Dependencies**: C01, C03
- **Tags**: MOFA, multi-omics integration, pTau, oligodendrocyte

## C08: Oligo.3 E4+ signatures replicate myelination-gene downregulation seen in published AD datasets
- **Statement**: Gene-set enrichment against two published AD snRNA-seq datasets shows significant (FDR<0.05) overlap between Oligo.3 E4+ downregulated DEGs and AD-downregulated oligodendrocyte genes, including shared PLP1 and OPALIN, in both Grubman et al. (ERC; 6 AD + 6 controls) and Blanchard et al. (PFC; 20 AD + 12 controls).
- **Status**: supported
- **Falsification criteria**: No significant enrichment between Oligo.3 downregulated DEGs and the published AD Oligo downregulated sets.
- **Proof**: [E07]
- **Evidence basis**: Fisher-test enrichment (Fig S46, Table S15).
- **Interpretation**: Neurotypical E4+ risk changes partially prefigure disease-state oligodendrocyte changes.
- **Sources**:
  - Grubman 6+6 ← §2.7 «cell type DEGs from Grubman et al., which included 6 AD donors and 6 controls» [result]
  - Blanchard 20+12 (PFC) ← §2.7 «cell type DEGs from Blanchard et al., which analyzed gene expression differences... in the prefrontal cortex (PFC) of 20 AD and 12 control donors» [result]
  - Shared PLP1/OPALIN downregulation ← §2.7 «significant overlap (FDR < 0.05) between downregulated Oligo DEGs in AD donors and downregulated Oligo.3 DEGs in APOE E4+ carriers, including a shared decrease in PLP1 and OPALIN» [result]
- **Dependencies**: C01, C02
- **Tags**: replication, cross-dataset enrichment, myelination
