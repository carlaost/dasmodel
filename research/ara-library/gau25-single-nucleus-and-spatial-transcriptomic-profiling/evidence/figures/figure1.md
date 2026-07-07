# Figure 1: Experimental scheme and molecular map of the human TC in 40 individuals

- **Source**: Fig. 1, Gaur et al. (2025), *Nature Communications* 16:10395, doi:10.1038/s41467-025-65350-6, page 2 of 17.
- **Caption**: "Fig. 1 | Experimental scheme and molecular map of the human TC in 40 individuals (controls and AD). a Overview of the experimental scheme (created in BioRender. Gaur, P. (2025)). b UMAP embedding of 430,271 single-nucleus RNA profiles from the TC brain region of 40 individuals; colored by cell type. c Dot plot of the canonical markers distinguishing 8 major cell types with different levels of expression (color) and percentage of expressing nuclei (dot size) across 430,271 TC nuclei. d UMAP embedding of 430,271 single-nucleus RNA profiles from the TC brain region colored by different subclusters. e Dot plot of differentially expressed (DE) genes distinguishing neuronal cell subgroups, showing different levels of expression and percentage of expressing nuclei across different subclusters, with numbers of nuclei (n) shown in the right. f Dot plot of DE genes distinguishing glial cell subgroups, showing different levels of expression and percentage of expressing nuclei across different subclusters, with numbers of nuclei (n) shown in the right. Source data are provided as a Source Data file."
- **Screenshot**: figure1.png (full journal page 2, all 6 panels a-f plus caption)
- **Figure type**: mixed (panel a = diagram; panels b, d = UMAP embeddings, i.e. qualitative_sample/diagram; panels c, e, f = quantitative dot plots with printed exact per-subcluster nucleus counts)
- **Extraction method**: exact_from_labels (subcluster nucleus counts in e/f are printed directly; panel a is a workflow diagram, not data; b/d UMAPs are qualitative cluster-separation visualizations without axis-readable coordinates)
- **Reading confidence**: high (panel a workflow and e/f printed n-values); medium (color/dot-size intensity in c/e/f, read qualitatively, not digitized to exact expression values)

## Visual description

- **Panel a (diagram)**: A workflow schematic starting from "Temporal cortex region (n=40)" (brain
  icon), branching into three parallel arms: (1) **snRNA-Seq**: "80 Samples" (Gray & white matter
  icon) → "snRNA Sequencing" → "TC subcellular architecture" → "Associating subcellular changes with
  AD pathology"; (2) **Spatial transcriptomics** (n=13): "CARTANA in-situ sequencing" (microscope
  icon) → "CARTANA data analysis & snRNA validation"; (3) **Integration**: six external-study names
  (Zhou et al., Grubman et al., Bryois et al., Leng et al., Cain et al., Mathys et al.) feeding into
  "Multi-Regions snRNA-Seq" → "Integrated data analysis." This is a pure process diagram (BioRender);
  no numeric data is encoded in it beyond the "n=40" and "n=13" sample-size labels and "80 Samples."
- **Panel b (UMAP, qualitative_sample)**: A 2-D UMAP embedding of 430,271 nuclei, colored by 8 major
  cell types (legend: Glutamatergic=blue, GABAergic=red, Astrocytes=orange, Oligodendrocytes=purple,
  OPCs=magenta, Microglia=green, Endothelial=salmon, Pericytes=pink). Shows large, well-separated
  clusters, with the Oligodendrocyte cluster visibly the largest (consistent with WM dominance by
  oligodendrocytes noted in the text) and Microglia/Endothelial/Pericytes forming small, distinct
  islands.
- **Panel c (quantitative dot plot)**: Canonical marker genes (x-axis: SLC17A6, SLC17A7 [Glutamatergic];
  GAD2, SLC32A1 [GABAergic]; AQP4 [Astrocytes]; FGFR3, ALDH1L1 [Oligodendrocytes lineage]; MOG
  [Oligodendrocytes]; PDGFRA [OPCs]; AIF1, C1QA [Microglia]; CLDN5 [Endothelial]; RGS5 [Pericytes])
  against the 8 major cell types (y-axis, right-side colored bar groups). Dot color = average
  expression (yellow→teal scale, 0-2+); dot size = percent nuclei expressing (0/25/50/75/100% legend).
  Each canonical marker shows a clean, near-exclusive high-expression/large-dot pattern in its
  expected cell type, confirming clean 8-way cell-type separation.
- **Panel d (UMAP, qualitative_sample)**: Same 430,271-nuclei UMAP embedding as panel b, recolored by
  finer subcluster identity (dozens of distinct colors), showing substructure within each of the
  8 major-cell-type islands from panel b.
- **Panel e (quantitative dot plot, exact nucleus counts)**: DE genes (x-axis) distinguishing
  neuronal (glutamatergic + GABAergic) subclusters (y-axis rows, ~40+ named subclusters e.g.
  `Gaba_VIP_ZBTB20`, `L5-6_Gluta_THEMIS_POSTN`, `L5_Gluta_RORB_IL1RAPL2`), with printed nucleus
  counts (n) at right for every row, e.g.: L6_Gluta_THEMIS_AC005885.1 n=8552; L5-6_Gluta_THEMIS_RGS12
  n=3978; **L5-6_Gluta_THEMIS_POSTN n=173**; L5_Gluta_TLL1 n=121; L5_Gluta_RORB_TSHZ2 n=7535;
  **L5_Gluta_RORB_IL1RAPL2_LINC02196 n=2055**; **L5_Gluta_RORB_IL1RAPL2 n=4944**; L5_Gluta_CTGF
  n=4049; L5_Gluta_ADRA1A n=292; L5_Gluta_ADAMTSL1_SEMA3E n=6031; L4-6_Gluta_SPARCL1 n=33173;
  L4-6_Gluta_RORB_AC008415.1 n=11028; L4_Gluta_RORB_PLCH1 n=2144; **L4_Gluta_COL5A2 n=2970**;
  **L3_Gluta_CUX2_GLIS3_COL5A2 n=3773**; **L3_Gluta_CUX2_GLIS3 n=5582**; **L3_Gluta_CUX2_CBLN2_GNAL
  n=18564**; L3_Gluta_CUX2_CBLN2 n=1161; **L2-4_Gluta_TLL1 n=2245**; and GABAergic rows including
  Gaba_VIP_ZBTB20 n=1491, Gaba_VIP_NELL1 n=1838, **Gaba_PVALB_TRPM3 n=1568**,
  **Gaba_SST_TRHDE_THSD7B n=944**, Gaba_SST_NPY n=299, Gaba_VIP_RYR3 n=2207, Gaba_PVALB_TRPS1 n=874,
  **Gaba_PVALB_TMEM132C n=3266**, Gaba_SST_PCDH15 n=2402, Gaba_LAMP5_KIT n=2392, Gaba_LAMP5_SOX1
  n=63, **Gaba_LAMP5_CHST9 n=1764**, Gaba_SST_TRHDE_PCDH15 n=1701, **GABA_PVALB_SPARCL1 n=2377**,
  Gaba_SST_CDH12 n=2071, Gaba_LAMP5_CADPS2 n=1085, Gaba_VIP_THSD7B n=709,
  Gaba_LAMP5_RELN_IL1RAPL2 n=553, Gaba_LAMP5_RELN n=639, Gaba_VIP_OLFM3 n=2558,
  Gaba_ADARB2_FAM19A1 n=1107, Gaba_VIP_CNR1 n=559 (bold = subclusters directly named in
  `logic/claims.md` C01/C03/C04/C09).
- **Panel f (quantitative dot plot, exact nucleus counts)**: Same format as panel e, for glial
  subclusters, e.g.: Peri_TAGLN n=218; Peri_SNTG2 n=115; Peri_RGS5_GJC1 n=291; Peri_RGS5 n=1125;
  **Peri_MGP n=48**; Peri_C11orf96 n=602; **Endo_TSHZ2 n=537**; Endo_EMP1 n=198; Endo_CLDN5 n=3496;
  Micro_RIPOR2 n=98; **Micro_P2RY12 n=7992**; Micro_DIAPH3 n=238; Micro_CD83 n=735;
  Micro_CD163 n=13707; **Micro_AIF1_RPL19 n=3389**; Micro_AC068992.1 n=1067; OPCs_SEZ6L n=15011;
  **OPCs_HSPA1A n=474**; OPCs_EGR1 n=291; Oligo_MOG_MID1 n=15104; Oligo_MOG_LINC01099 n=13810;
  Oligo_MOG n=163458; Oligo_HSPA1A n=2791; Astro_TPST1 n=4495; **Astro_TNC n=4675**; Astro_IFI44L
  n=493; Astro_CABLES1 n=19891; Astro_APLNR n=1893 (bold = subclusters directly named in
  `logic/claims.md` C01/C02/C09).

## Data table (subcluster nucleus counts referenced by claims — exact, printed in panels e/f)

| Subcluster | Broad cell type | n (nuclei) |
|---|---|---|
| L5-6_Gluta_THEMIS_POSTN | Glutamatergic | 173 |
| L5_Gluta_RORB_IL1RAPL2_LINC02196 | Glutamatergic | 2055 |
| L5_Gluta_RORB_IL1RAPL2 | Glutamatergic | 4944 |
| L4_Gluta_COL5A2 | Glutamatergic | 2970 |
| L3_Gluta_CUX2_GLIS3 | Glutamatergic | 5582 |
| L3_Gluta_CUX2_CBLN2_GNAL | Glutamatergic | 18564 |
| L2-4_Gluta_TLL1 | Glutamatergic | 2245 |
| Gaba_PVALB_TMEM132C | GABAergic | 3266 |
| Gaba_SST_TRHDE_THSD7B | GABAergic | 944 |
| GABA_PVALB_SPARCL1 | GABAergic | 2377 |
| Gaba_LAMP5_CHST9 | GABAergic | 1764 |
| Micro_AIF1_RPL19 | Microglia | 3389 |
| OPCs_HSPA1A | OPCs | 474 |
| Peri_MGP | Pericytes | 48 |
| Endo_TSHZ2 | Endothelial | 537 |
| Astro_TNC | Astrocytes | 4675 |

## Trend summary
Panels b-d establish clean UMAP separation of 430,271 nuclei into 8 major cell types (with
oligodendrocytes forming the largest cluster, consistent with WM dominance) and their subclusters.
Panels e-f give the exact per-subcluster nucleus counts that ground the subcluster names invoked
throughout `logic/claims.md` (e.g. the 173-nucleus THEMIS+/POSTN+ resilience population is a
comparatively small but robust subcluster relative to the 33,173-nucleus SPARCL1+ L4-6 population).
