# Claims

All numbers are transcribed exactly from the source PDF. `**Sources**` entries carry a verbatim
«quote» from the paper (main text, Methods, or figure caption/panel) with an `[input]`
(design/defined value) or `[result]` (measured/analysed value) tag. Statistics are as reported; the
paper reports significance as exact P values or thresholds, generally with mean ± s.e.m.

---

## C01: 5xFAD+ cortex contains two spatially defined microglial states, PAM and non-PAM, with PAM expanded
- **Statement**: In frontal cortices of 44-week-old female 5xFAD+ mice, Pu.1+Iba-1+ microglia partition into PAM (in direct contact with Methoxy-X04+ amyloid, cell bodies within a 30-µm radius) and non-PAM (ramified, distant, no contact); PAM are expanded in number in 5xFAD+ vs 5xFAD- controls, whereas non-PAM numbers are similar to controls. Both PAM and non-PAM show high proliferative (BrdU+) capacity in 5xFAD+ mice.
- **Status**: supported
- **Falsification criteria**: If quantification showed no expansion of PAM in 5xFAD+ vs 5xFAD-, or if non-PAM numbers differed strongly from controls, or if the 30-µm/contact criterion did not separate two populations, the claim fails.
- **Proof**: [E01, E02]
- **Evidence basis**: Fig 1a (representative images, 30-µm ring), Fig 1b (Pu.1+ cells mm⁻³, PAM red / non-PAM blue), Fig 1c (BrdU+Pu.1+ cells mm⁻²).
- **Interpretation**: Spatial position is a defining axis of microglial state in amyloid pathology, beyond transcriptomic identity.
- **Sources**:
  - 30-µm radius ← Fig 1a / Methods «their cell bodies within a 30-µm radius of said deposits» [input]
  - 44-week-old female ← Results §"Non-PAM develop..." «we analyzed the distribution of Pu.1+ microglia in the frontal cortices of 44-week-old female 5×FAD+ animals» [input]
  - PAM expansion, non-PAM unchanged ← Results «Quantification of Pu.1+ PAM and non-PAM showed a clear PAM expansion in 5×FAD+ animals but similar numbers of non-PAM compared to controls (Fig. 1b)» [result]
  - high proliferation of both ← Results «revealed a high proliferative capacity of PAM and non-PAM in 5×FAD+ mice, whereas microglia in 5×FAD− mice incorporated BrdU to a lesser extent (Fig. 1c)» [result]
- **Dependencies**: none
- **Tags**: PAM, non-PAM, spatial state, proliferation, 5xFAD

## C02: PAM clonally expand at plaque sites, whereas non-PAM show random (non-clonal) expansion
- **Statement**: By multicolor Confetti labeling and Monte Carlo (MC) simulation of same-colored-cell proximities, PAM cluster same-colored cells above the randomized baseline at short ring distances (clonal expansion at the plaque site), whereas non-PAM densities do not exceed the random baseline (non-clonal).
- **Status**: supported
- **Falsification criteria**: If the experimental same-color density confidence interval overlapped the MC-randomized interval at all ring distances for PAM, clonality would be rejected.
- **Proof**: [E03]
- **Evidence basis**: Fig 1f (MC simulation densities of non-PAM (top) and PAM (bottom) vs randomized datasets, mean and 98% CI). NOTE — the main text sentence reporting this reads verbatim: "Whereas PAM showed non-clonal random expansion, PAM clonally expand at the plaque site (Fig. 1g)." The first "PAM" is an apparent source typographical error for "non-PAM"; Fig 1f densities and the surrounding argument make the intended meaning (non-PAM random, PAM clonal) unambiguous. Reproduced here verbatim per no-silent-fix policy.
- **Interpretation**: PAM arise by local clonal proliferation at deposits; non-PAM are distributed non-clonally.
- **Sources**:
  - clonality statement (verbatim, incl. typo) ← Results «Whereas PAM showed non-clonal random expansion, PAM clonally expand at the plaque site (Fig. 1g)» [result]
  - MC baseline / significance ← Methods (MC simulation) «After 10,000 shuffling simulations ... The 98% confidence interval was calculated ... the null hypothesis ... is rejected with a significance of P < 0.02» [input]
- **Dependencies**: C01
- **Tags**: clonal expansion, Monte Carlo, Confetti, PAM

## C03: PAM clone size correlates with adjacent plaque volume up to ~1,000 µm3, then saturates
- **Statement**: The number of Confetti+ cells per PAM clone correlates positively with adjacent Methoxy-X04+ plaque volume overall (R = 0.28, P = 0.00028) and for plaques <1,000 µm3 (R = 0.27, P = 0.0091), but not for plaques >1,000 µm3 (R = 0.17, P = 0.17, NS); progressive amyloid deposition thus outcompetes clonal growth of PAM at large plaques.
- **Status**: supported
- **Falsification criteria**: If the >1,000-µm3 correlation were significant, or the overall/small-plaque correlations were non-significant, the saturation interpretation fails.
- **Proof**: [E04]
- **Evidence basis**: Fig 1h (three linear-regression scatterplots with R and P).
- **Interpretation**: Clone size scales with plaque size only while plaques are small; beyond ~1,000 µm3 amyloid growth exceeds PAM clonal growth.
- **Sources**:
  - R = 0.28, P = 0.00028 (all plaques) ← Fig 1h caption «Left: correlation for all Methoxy-X04+ plaque sizes (R = 0.28, ***P = 0.00028)» [result]
  - R = 0.27, P = 0.0091 (<1,000 µm3) ← Fig 1h caption «Middle: correlation for <1,000-µm3-sized Methoxy-X04+ plaques (R = 0.27, **P = 0.0091)» [result]
  - R = 0.17, P = 0.17 (>1,000 µm3) ← Fig 1h caption «Right: correlation for Methoxy-X04+ plaques >1,000 µm3 (R = 0.17, NS P = 0.17)» [result]
  - saturation at >1,000 µm3 ← Results «amyloid plaques of greater than 1,000 µm3 showed no further correlation to the Confetti+Pu.1+ PAM clone size, indicating that progressive amyloid deposition outcompetes clonal growth of PAM» [result]
- **Dependencies**: C02
- **Tags**: clone size, plaque volume, Voronoi, linear regression

## C04: CD11c specifically marks PAM and Tmem119 preferentially marks non-PAM
- **Statement**: Among tested markers, CLEC7A, APOE, AXL and P2RY12 do not separate PAM from non-PAM; CD11c expression is highly restricted to PAM and virtually absent in non-PAM; Tmem119 strongly labels non-PAM with only minor expression in PAM (Tmem119+ % significantly higher in non-PAM than PAM, P < 0.0001).
- **Status**: supported
- **Falsification criteria**: If CD11c were detected in non-PAM, or Tmem119 equally expressed in PAM and non-PAM, marker-based discrimination fails.
- **Proof**: [E05]
- **Evidence basis**: Fig 2a (APOE/CLEC7A/P2RY12), Fig 2b (CD11c restricted to PAM), Fig 2c–e (Tmem119 non-PAM vs PAM; Fig 2e quantification), Extended Data Fig 1.
- **Interpretation**: CD11c and Tmem119 provide an operational sorting/fate-mapping handle for the two spatial states.
- **Sources**:
  - CLEC7A/APOE/AXL/P2RY12 no separation ← Results «For CLEC7A, APOE, AXL AND P2RY12, we found no clear separation between PAM and non-PAM (Fig. 2a and Extended Data Fig. 1a)» [result]
  - CD11c restricted to PAM ← Results «CD11c expression was highly restricted to PAM and virtually absent in non-PAM (Fig. 2b), representing a reliable marker for PAM» [result]
  - Tmem119 non-PAM ← Results «Tmem119 revealed a strong labeling of non-PAM, whereas PAM showed only a minor expression of Tmem119 (Fig. 2c–e)» [result]
  - P < 0.0001 ← Fig 2e caption «***P < 0.0001» [result]
- **Dependencies**: C01
- **Tags**: markers, CD11c, Tmem119, immunohistochemistry

## C05: Individual non-PAM give rise to adjacent same-colored PAM clones that grow over time
- **Statement**: In Tmem119CreERT2R26Confetti5xFAD+ mice (recombination induced at 36 weeks), Confetti+ label appears in both Tmem119+ non-PAM and Tmem119− PAM, indicating initially-labeled non-PAM give rise to PAM; single Confetti+ non-PAM are always located adjacent to same-colored PAM clones, and Confetti+ PAMs per clone increase from 2 to 8 weeks after tamoxifen (P = 0.0021). The fraction of PAM clones associated with a same-colored non-PAM remains stable (81.37% at 2 weeks vs 88.28% at 8 weeks associated).
- **Status**: supported
- **Falsification criteria**: If Confetti+ PAM clones lacked adjacent same-colored non-PAM, or PAM-per-clone did not increase over time, the non-PAM→PAM origin model fails.
- **Proof**: [E06]
- **Evidence basis**: Fig 2f–l (fate-mapping scheme, images, Fig 2k quantification, Fig 2l pie charts).
- **Interpretation**: The PAM compartment is continuously fed by conversion of individual neighboring non-PAM.
- **Sources**:
  - recombination at 36 weeks ← Results «We induced recombination in 36-week-old Tmem119CreERT2R26Confetti5×FAD+ animals» [input]
  - non-PAM give rise to PAM ← Results «we detected Confetti+ microglia in both Tmem119+Iba-1+ non-PAM and Tmem119−Iba-1+ PAM, suggesting that initially labeled non-PAM gave rise to PAM at adjacent amyloid plaques» [result]
  - clone growth 2→8 weeks ← Results «the cell number per clone increased from 2 weeks to 8 weeks after TAM injection (Fig. 2j ...)» [result]
  - P = 0.0021 ← Fig 2k caption «Symbols represent individual clones from biological replicates (n = 2). P = 0.0021» [result]
  - 81.37% (2 wk associated) / 88.28% (8 wk associated) ← Fig 2l panel «81.37% ... 2 weeks after TAM» and «88.28% ... 8 weeks after TAM» (dark-red = without same-colored non-PAM: 16.63% at 2 wk, 11.72% at 8 wk) [result]
- **Dependencies**: C01, C04
- **Tags**: fate mapping, Tmem119CreERT2, non-PAM to PAM, clone dynamics

## C06: Peripheral LPS increases and ABX slightly reduces PAM clonal expansion at early disease stage; effects vanish at late stage
- **Statement**: In Cx3cr1CreERT2R26Confetti5xFAD+ mice, clonal accumulation of Confetti+ PAM at early stage is slightly reduced by antibiotics (ABX) and increased by low-dose LPS; PAM clone size, number of associated plaques and clone territory are enhanced by LPS (not by microbiota loss) at early stage. At late stage, clone size is not altered by either treatment. PAM clone expansion is overall more prominent in young than aged mice.
- **Status**: supported
- **Falsification criteria**: If LPS did not increase and ABX did not reduce early-stage clonal accumulation, or if late-stage clone sizes changed with treatment, the stage-dependence fails.
- **Proof**: [E07]
- **Evidence basis**: Fig 3a–i (MC densities early/late; Fig 3c,e Confetti+ at 30-µm ring with P values; Fig 3g clone size, Fig 3h plaques/clone, Fig 3i clone volume). Early-stage 30-µm ring: 5xFAD- vs untreated P < 0.0001; untreated vs LPS P = 0.0958; volume/clone untreated vs LPS P = 0.0014.
- **Interpretation**: The kinetics of PAM clonality depend on disease duration/age and are tuned by peripheral inflammatory and microbiota signals, chiefly via the non-PAM compartment.
- **Sources**:
  - ABX reduces / LPS increases early ← Results «clonal accumulation of Confetti+ PAM in transgenic mice at early stage was slightly reduced upon ABX treatment, whereas LPS application increased the expansion (Fig. 3b,c)» [result]
  - LPS enhances clone metrics early only ← Results «PAM clone sizes, number of clone-associated plaques as well as clone territory were enhanced upon LPS challenge, but not in the absence of microbiota, at the early stage of disease (Fig. 3f–i)» [result]
  - late stage no change ← Results «During the late stage of disease, no alteration of clone size was observed across the different treatment groups (Fig. 3f–i)» [result]
  - young > aged expansion ← Results «PAM clone expansion was more prominent in young than aged 5×FAD+ mice» [result]
  - clone volume early untreated vs LPS P = 0.0014 ← Fig 3i panel «0.0014» (early-stage untreated vs LPS) [result]
- **Dependencies**: C02
- **Tags**: LPS, antibiotics, microbiota, disease stage, clonality

## C07: Only non-PAM show transcriptional plasticity to LPS/ABX at early stage
- **Statement**: scRNA-seq of index-sorted PAM (CD45+/lowCD11b+CD11c+) and non-PAM (CD45+/lowCD11b+CD11c−) from early-stage mice (1,095 cells) yields five clusters C0–C4 (C0/C1 PAM-enriched, activation signature; C2–C4 non-PAM-enriched, homeostatic signature). ABX and LPS induce prominent transcriptional changes and treatment-specific clusters only in non-PAM (ABX→C3, LPS→C4); no treatment-associated clusters appear in PAM. LPS induces inflammatory gene sets in non-PAM (HALLMARK_INFLAMMATORY_RESPONSE NES = 2, P = 0.0, FDR q = 0.0; TNFA_SIGNALING_VIA_NFKB NES = 2.66; INTERFERON_GAMMA_RESPONSE NES = 1.62) while ABX downregulates innate-immune/macrophage-activation gene sets (NES = −1.51 and −1.34). Late-stage treatment produced only minor changes with no treatment clusters.
- **Status**: supported
- **Falsification criteria**: If treatment-specific clusters had appeared in PAM, or non-PAM showed no differential gene-set enrichment, the non-PAM-specific plasticity fails.
- **Proof**: [E08]
- **Evidence basis**: Fig 4a–g (UMAP, clusters, composition, DE heatmap, volcano plots, GSEA), Fig 4h–j (UCell modules), Extended Data Fig 3.
- **Interpretation**: Non-PAM are the modular, environmentally responsive compartment; PAM are transcriptionally comparatively "locked."
- **Sources**:
  - 1,095 cells / five clusters ← Fig 4a,b caption «Each dot represents one cell (N = 1,095)» and Results «Unsupervised clustering subdivided all annotated microglia to five clusters (C0–C4)» [result]
  - sorting definition ← Methods «non-PAM were defined by CD45+/lowCD11b+CD11c− and PAM by CD45+/lowCD11b+CD11c+ expression» [input]
  - treatment clusters only in non-PAM ← Results «non-PAM exhibited a clear enrichment of cells in distinct clusters after ABX (C3) and LPS (C4) ... In contrast, no treatment-associated microglial clusters were found in PAM» [result]
  - GSEA NES LPS ← Fig 4f caption «HALLMARK_INFLAMMATORY_RESPONSE: normalized enrichment score (NES) = 2, P = 0.0, false discover rate (FDR) q-value = 0.0 ... HALLMARK_INTERFERON_GAMMA_RESPONSE: NES = 1.62 ... HALLMARK_TNFA_SIGNALING_VIA_NFKB: NES = 2.66» [result]
  - GSEA NES ABX ← Fig 4g caption «GOBP_REGULATION_OF_INNATE_IMMUNE_RESPONSE: NES = −1.51, P = 0.002, FDR q = 0.13. GOBP_REGULATION_OF_MACROPHAGE_ACTIVATION: NES = −1.34, P = 0.1, FDR q = 0.15» [result]
- **Dependencies**: C01, C06
- **Tags**: scRNA-seq, GSEA, non-PAM plasticity, LPS, ABX

## C08: Chromatin accessibility separates PAM from non-PAM; non-PAM resemble homeostatic 5xFAD- microglia
- **Statement**: ATAC-seq shows PAM adopt distinct chromatin accessibility, while non-PAM cluster with 5xFAD- microglia (PCA). PAM vs non-PAM: 5,661 differentially accessible regions (DARs) — 4,360 more accessible (PAM-up) and 1,301 less accessible (PAM-down). PAM vs 5xFAD-: 7,637 DARs (5,848 increased, 1,789 decreased) (FDR < 0.05, |log2FC| ≥ 0.584). PAM-up regions include DAM genes (Csf1, Apoe, Spp1, Clec7a, Itgax); non-PAM/5xFAD- show higher accessibility at homeostatic genes (Tmem119, Csf1r).
- **Status**: supported
- **Falsification criteria**: If PAM and non-PAM did not separate in PCA/heatmaps, or DAR counts/directions contradicted, the epigenetic-separation claim fails.
- **Proof**: [E09]
- **Evidence basis**: Fig 5a (accessibility at 22,929 primed/active enhancers), Fig 5b (volcano), Fig 5c (DAR heatmap with counts), Fig 5d (motifs), Fig 5e (IGV tracks), Extended Data Fig 4 (QC, 59,293 consensus peaks, PCA PC1 91%).
- **Interpretation**: PAM acquire a distinct epigenetic state at plaques; non-PAM are epigenetically close to homeostatic microglia.
- **Sources**:
  - 4,360 up / 1,301 down (PAM vs non-PAM) ← Results «we identified differentially accessible regions (DARs) and found 4,360 regions with higher accessibility (PAM-up) and 1,301 regions with lower accessibility (PAM-down) in PAM compared to non-PAM» [result]
  - 5,661 total DARs ← Fig 5c caption «Comparison between PAM and non-PAM revealed 5,661 DARs with 4,360 regions showing a higher accessibility and 1,301 regions with decreased accessibility» [result]
  - 7,637 / 5,848 / 1,789 (PAM vs 5xFAD-) ← Fig 5c caption «In the comparison of PAM versus 5×FAD−, out of a total of 7,637 DARs, 5,848 showed increased accessibility, and 1,789 showed decreased accessibility (FDR < 0.05, log2FC ≥ 0.584 or log2FC ≤ −0.584)» [result]
  - 22,929 enhancer regions ← Fig 5a caption «at 22,929 previously defined primed and active microglial enhancer regions» [result]
  - 59,293 consensus peaks ← Extended Data Fig 4a caption «consensus ATAC-Seq peak set (59,293 total peaks) across all samples» [result]
  - non-PAM clusters with 5xFAD- ← Results «PCA demonstrated that non-PAM and microglia from non-transgenic mice clustered together and separated from PAM (Extended Data Fig. 4c)» [result]
- **Dependencies**: C01
- **Tags**: ATAC-seq, DARs, chromatin accessibility, DESeq2, PCA

## C09: Csf1r shows higher transcript and more open chromatin in non-PAM than PAM, nominating CSF1R as a non-PAM-directed target
- **Statement**: Both scRNA-seq (Fig 4e) and ATAC-seq (Fig 5e) reveal higher Csf1r transcript levels and a more open Csf1r chromatin region in non-PAM compared to PAM; conversely Csf1 accessibility is increased in PAM. This makes CSF1R a candidate molecular target enriched in the non-PAM population.
- **Status**: supported
- **Falsification criteria**: If Csf1r were equally or more accessible/expressed in PAM, the non-PAM-directed targeting rationale fails.
- **Proof**: [E08, E09]
- **Evidence basis**: Fig 4e (Csf1r among genes higher in non-PAM), Fig 5e (Csf1r IGV track higher in non-PAM/5xFAD-; Csf1 higher in PAM).
- **Interpretation**: The homeostatic, Csf1r-retaining non-PAM are the population most amenable to CSF1R-ligand engagement.
- **Sources**:
  - higher Csf1r in non-PAM (both assays) ← Results «In both the scRNA-seq data (Fig. 4e) and the ATAC–seq analysis (Fig. 5e), we revealed higher transcript levels and an open chromatin region for Csf1r in non-PAM compared to PAM, making CSF1R a potential molecular target in this population» [result]
  - Csf1 up / Csf1r homeostatic in non-PAM ← Results «Chromatin accessibility in PAM was increased at DARs assigned to DAM signature genes, such as Csf1, Apoe, Spp1, Clec7a and Itgax ... non-PAM and microglia from 5×FAD− mice showed higher chromatin accessibility at DARs associated with homeostatic microglia signature genes such as Tmem119 but also Csf1r» [result]
- **Dependencies**: C07, C08
- **Tags**: Csf1r, CSF1R target, non-PAM, epigenetics

## C10: Peripheral Csf1 (not IL-34) reduces PAM clonal expansion and overall microglia, boosts PAM phagocytosis, and lowers Aβ
- **Statement**: In early-stage Cx3cr1CreERT2R26Confetti5xFAD+ mice, peripheral Csf1 diminishes Confetti+Pu.1+ PAM clonal expansion (without altering non-PAM), reduces overall Pu.1+ microglial number in 5xFAD+ (P = 0.0164) while slightly elevating it in 5xFAD- (P = 0.0352), reduces the percentage of plaques associated with CD11c+ PAM (P = 0.0037), enlarges the PAM CD68+ lysosomal compartment (PAM P = 0.0159), and strongly reduces soluble and insoluble Aβ1–40 and Aβ1–42 (insoluble Aβ42 P = 0.0114; soluble Aβ42 P = 0.0159; insoluble Aβ40 P = 0.0030; soluble Aβ40 P = 0.0094), without affecting APP processing. Csf1 also reduces plaque number (P = 0.0083) and individual plaque volume (P = 0.0344).
- **Status**: supported
- **Falsification criteria**: If Csf1 did not reduce PAM clonality/plaque-associated PAM/Aβ, or altered APP processing, the therapeutic-effect claim fails.
- **Proof**: [E10]
- **Evidence basis**: Fig 6a–n (MC densities, quantifications, CD68, ELISA, western blot, Voronoi, plaque counts/volumes).
- **Interpretation**: Csf1-CSF1R engagement restricts PAM expansion while enhancing their amyloid-restrictive phagocytic function.
- **Sources**:
  - dosing ← Methods «intraperitoneally injected twice per week with 40 μg kg−1 recombinant murine Csf1 (PeproTech, 315-02) in PBS and 100 μg kg−1 IL-34 (BioLegend, 577602) in PBS or PBS alone for 8 weeks» [input]
  - PAM clonal expansion diminished ← Results «After Csf1 treatment, clonal expansion of Confetti+Pu.1+ PAM was diminished (Fig. 6a,b), but no alterations in the expansion of non-PAM were induced» [result]
  - Pu.1 number 5xFAD+ P = 0.0164 / 5xFAD- P = 0.0352 ← Fig 6c panel «0.0164 ... 0.0352» [result]
  - plaques with PAM P = 0.0037 ← Fig 6d panel «0.0037» [result]
  - CD68 PAM P = 0.0159 ← Fig 6f panel «0.0159» (non-PAM P = 0.2857) [result]
  - Aβ reductions ← Fig 6g panels «Insoluble Aβ42 0.0114; Soluble Aβ42 0.0159; Insoluble Aβ40 0.0030; Soluble Aβ40 0.0094» [result]
  - APP processing unaffected ← Results «Analysis of soluble and insoluble Aβ1–40 and Aβ1–42 levels revealed a strong reduction upon Csf1 treatment (Fig. 6g), whereas amyloid precursor protein (APP) processing itself was not affected (Fig. 6h)» [result]
  - plaques P = 0.0083 / volume P = 0.0344 ← Fig 6k panel «0.0083» and Fig 6l panel «0.0344» [result]
- **Dependencies**: C09
- **Tags**: Csf1, CSF1R, phagocytosis, CD68, amyloid reduction, therapy

## C11: Csf1 restores the clone-size / large-plaque correlation
- **Statement**: After Csf1 treatment, PAM clone size correlates with adjacent plaque volume overall (R = 0.36, P = 4.7 × 10⁻⁷) and, unlike untreated mice, for plaques >1,000 µm3 (R = 0.33, P = 0.016); for plaques <1,000 µm3 there is no correlation (R = 0.084 (reported also as −0.084), P = 0.35). Csf1 thus makes previously "outcompeting" large deposits again correlate with (and be restricted by) PAM clones.
- **Status**: supported
- **Falsification criteria**: If the >1,000-µm3 correlation remained non-significant after Csf1, the restored-restriction interpretation fails.
- **Proof**: [E04, E10]
- **Evidence basis**: Fig 6n (three linear regressions), Fig 6m (plaques with contact to multiple clones, P = 0.3700).
- **Interpretation**: Csf1 re-couples PAM clonal growth to large-plaque restriction (contrast with C03, where large plaques outcompeted clones).
- **Sources**:
  - R = 0.36, P = 4.7 × 10⁻⁷ (all) ← Fig 6n caption «Left: correlation for all Methoxy-X04+ plaque sizes (R = 0.36, ***P = 4.7 × 10−7)» [result]
  - R = −0.084, P = 0.35 (<1,000) ← Fig 6n caption «Middle: correlation for <1,000-µm3-sized Methoxy-X04+ plaques (R = −0.084, NS P = 0.35)» [result]
  - R = 0.33, P = 0.016 (>1,000) ← Fig 6n caption «Right: correlation for Methoxy-X04+ plaques >1,000 µm3 (R = 0.33, *P = 0.016)» [result]
  - large deposits now correlative ← Results «Large amyloid deposits (>1,000 µm3), which outcompeted PAM clones before, became now highly correlative with PAM clone size» [result]
- **Dependencies**: C03, C10
- **Tags**: Voronoi, correlation, plaque restriction, Csf1

## C12: IL-34 (the other CSF1R ligand) has no effect on clonal expansion or amyloid pathology
- **Statement**: In contrast to Csf1, IL-34 treatment does not influence clonal expansion of Confetti+ PAM or non-PAM (PAM 30-µm ring P = 0.2652; non-PAM P = 0.9143), microglial cell number (P = 0.0885 5xFAD+), decoration of plaques with PAM (P = 0.7986), or plaque number/volume (plaques P = 0.1088; volume P = 0.2712), relative to PBS controls.
- **Status**: supported
- **Falsification criteria**: If IL-34 significantly altered any of these measures, the ligand-specificity of the Csf1 effect fails.
- **Proof**: [E10]
- **Evidence basis**: Extended Data Fig 5b–f (MC densities, quantifications, plaque metrics).
- **Interpretation**: The CSF1R therapeutic effect is ligand-specific to Csf1, not shared by IL-34, in this early-stage paradigm.
- **Sources**:
  - IL-34 no effect on expansion ← Results «the other CSF1R ligand, IL-34, did not influence clonal expansion of Confetti-labeled PAM or non-PAM compared to PBS-treated controls (Extended Data Fig. 5b,c)» [result]
  - PAM ring P = 0.2652 / non-PAM P = 0.9143 ← Extended Data Fig 5c panel «0.2652 ... 0.9143» [result]
  - plaques P = 0.1088 / volume P = 0.2712 ← Extended Data Fig 5f panel «0.1088 ... 0.2712» [result]
- **Dependencies**: C10
- **Tags**: IL-34, CSF1R ligand specificity, negative control

## C13: Csf1 reduces inflammatory programs and raises oxidative-phosphorylation/autophagy in PAM without changing core state signatures
- **Statement**: scRNA-seq after 4 weeks of Csf1 (2,686 cells, clusters C0–C7) identifies two Csf1-induced PAM (CD11c+) clusters (C1, C7) but no Csf1-induced non-PAM cluster in 5xFAD+ (one Csf1-induced non-PAM cluster C5 appears in 5xFAD- controls). Both PAM and non-PAM retain their homeostatic (Tmem119, P2ry12, Cx3cr1) or activated (Trem2, Apoe, Itgax) core panels. GSEA of PAM (Csf1 vs PBS) shows decreased inflammatory response, type I/II interferon signaling and TNFA_SIGNALING_VIA_NFKB, and increased oxidative phosphorylation and autophagy of mitochondrion; similar trends occur in non-PAM.
- **Status**: supported
- **Falsification criteria**: If Csf1 shifted the core homeostatic/activation signatures (i.e., converted non-PAM identity), or failed to reduce inflammatory gene sets, the "functional-fitness without identity switch" claim fails.
- **Proof**: [E11]
- **Evidence basis**: Fig 7a–i (UMAP, clusters, composition, DE heatmap, signature feature plots, GSEA running-sum plots).
- **Interpretation**: Csf1 does not reprogram state identity but improves PAM functional fitness (phagocytosis, mitochondrial metabolism), producing amyloid-competent PAM.
- **Sources**:
  - 2,686 cells / eight clusters ← Methods «For the CSF1-treated scRNA-seq dataset, 2,686 cells were embedded using the first five principal components» and Results «Eight distinct microglial clusters, designated C0–C7» (Fig 7a caption states N = 2,687) [result]
  - two Csf1-induced PAM clusters ← Results «We identified two specific Csf1-induced clusters in the CD11c+ PAM population, namely C1 and C7, but no cluster specifically enriched for CD11c− non-PAM» [result]
  - core signatures retained ← Results «both PAM and non-PAM retained their respective homeostatic (Tmem119, P2ry12, Cx3cr1, etc.) or activated (Trem2, Apoe, Itgax, etc.) gene panel upon Csf1 treatment, indicating that there is no therapy-induced shift of non-PAM toward PAM involving their core signatures» [result]
  - inflammation down / oxphos + autophagy up ← Results «Csf1 treatment induced a profound decrease in gene sets associated with inflammatory response, including type I or type II interferon signaling or NF-κB activation via TNF signaling (Fig. 7h), and an upregulation of genes associated with metabolic regulation toward autophagy and oxidative phosphorylation» [result]
- **Dependencies**: C10
- **Tags**: scRNA-seq, GSEA, oxidative phosphorylation, autophagy, amyloid-competent PAM
