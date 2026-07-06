# Figure 3: Markers of layer 4 across neocortical regions
- **Source**: Figure 3, §"Identification of layer 4 excitatory neurons across BA9 and BA17 in AD"
- **Caption**: "UMAP plots highlighting the top L4 marker genes in BA17 (a) compared to BA9 (b). The Ex5 cluster (blue) and its top marker genes (EYA4, KCNH8, LAMA3, VAV3, KCNIP1, TRPC3) are overrepresented in BA17, whereas Ex6 (MME) and Ex7 (GABRG1) are overrepresented in BA9. c UMAP plots from mouse neocortex snRNA-seq highlighting the conserved expression of top Ex5 marker genes in a cluster annotated as L4/5 intratelencephalic (IT). d Representative L4 cells and their top marker genes in Xenium… e Spatial maps of the annotated L4 excitatory clusters across Xenium sections, highlighting the relative abundance of Ex5 (blue) in BA17 and of Ex6 (orange) and Ex7 (green) in BA9. f KCNH8 expression map and spatial maps of L4 clusters in… BA17 and adjacent BA18… g,h Identification of Ex5 neurons in L4 of BA17 histological sections… EYA4 and KCNH8 in L4 (Allen Human Brain Atlas)… boundaries of L4 defined by Nissl and VGLUT2 expression."
- **Screenshot**: figure3.png
- **Figure type**: mixed (qualitative UMAP + spatial maps + ISH micrographs)
- **Extraction method**: exact_from_labels (text-stated cross-dataset counts) + visual_description
- **Reading confidence**: high (labels/ISH); medium (UMAP density)

## Visual description
- **Panels a,b (UMAP)**: Ex5 top markers EYA4, KCNH8, LAMA3, VAV3, KCNIP1, TRPC3 abundant in BA17, sparse in BA9; Ex6 (MME) and Ex7 (GABRG1) more abundant in BA9.
- **Panel c (UMAP)**: mouse neocortex — Ex5 markers conserved in an L4/5 IT cluster (Trpc3, Eya4, Lama3, Vav3, Kcnip1, Kcnh8).
- **Panel d (Xenium micrograph)**: transcripts (RORB, CUX1, CUX2, EYA4, TRPC3, KCNH8, VAV3) overlaid on segmented L4 cells; relative specificity for Ex5/Ex6/Ex7.
- **Panel e (spatial maps)**: Ex5 (blue) enriched BA17; Ex6 (orange)/Ex7 (green) enriched BA9. In BA17 Ex5 shows density gradient (deeper = higher, sharp L5 boundary).
- **Panel f (spatial maps)**: BA17→BA18 transition (red arrow); in BA18 Ex5 more abundant, Ex6 less abundant vs BA9.
- **Panels g,h (ISH)**: Allen Human Brain Atlas — EYA4 and KCNH8 highest in deep layer 4c (low in 4a/4b); matches VGLUT2 thalamocortical (LGN) terminals; Nissl defines L4 boundaries.

## Key text-stated quantities (scANVI cross-dataset Ex5 prediction, from §Results)
| Reference dataset | Ex5 cells | % of excitatory | denominator |
|-------------------|-----------|-----------------|-------------|
| BA17 reference (Jorstad 2023) | 63,870 | 34.42% | 185,565 |
| SEA-AD DLPFC | 2,152 | 0.33% | 660,751 |
| Green et al. 2024 | 19,360 | 3.03% | 637,968 |
| Mathys et al. 2023 | 3,361 | 3% | 112,143 |
| This study, BA9 | 7,943 | 4.36% | 182,140 |

## Trend / structural summary
Ex5 is a BA17-specialized L4 IT population (deep 4c, VGLUT2/LGN input zone), conserved in mouse and
consistently mapped across datasets; Ex6/Ex7 are the association-cortex L4 IT counterparts.
Supports C10 (and C01).
