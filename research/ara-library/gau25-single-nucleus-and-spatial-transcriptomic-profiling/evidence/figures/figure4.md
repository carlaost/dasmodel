# Figure 4: Characterization of plaque and tangle pathology in brain sections and validation of snRNA-seq derived associations via spatial analysis

- **Source**: Fig. 4, Gaur et al. (2025), *Nature Communications* 16:10395, doi:10.1038/s41467-025-65350-6, page 9 of 17 (panels rendered on page 8; caption printed on page 9).
- **Caption**: "Fig. 4 | Characterization of plaque and tangle pathology in brain sections and validation of snRNA-seq derived associations via spatial analysis. a A visual representation of the spatial distribution of cells in the specified samples (from control to progressing AD pathology), with a background grid for all samples based on cell coordinates, while different layers highlighting cells expressing specific markers (Oligodendrocytes = light blue to dark blue, RORB = green and LAMP5 = orange). GM and WM are well distinguished with plaque deposition sites (blue squares) on tissue. b Same as a except for tangles deposition instead of plaques in magenta squares. c Boxplots of the genes found to have significant associations with Braak stages in GM and WM of TC in tissue, validating snRNA trait association signatures, as determined by linear mixed-effects models using the lmerTest R package. Two-sided tests were performed, and no correction was applied for multiple comparisons. Statistical significance indicated by */** on the plots corresponds to p-values derived from the model output, not from tests performed separately on the plotted data (GM and WM samples from n = 11 individuals). '*' represents p-value <=0.05 and '**' represents p-value <=0.01. Specific p-values GM: ACTG1_Glut- 0.02, CC2D1B_Glut- 0.001, PPP1R1A_Glut- 0.02, ALDH1A1_Glut-0.011, TM2D1_Glut-0.02, ACTG1_GABA- 0.006, SCG3_GABA- 0.016, 0.002, PDCD6_GABA- 0.013, CD74_Microg- 0.012, P2RY12_Microg- 0.001, GFAP_Astro- 0.0001. Specific p-values WM: PDCD6_GABA- 0.03, ANXA7_GABA- 0.012. Boxplot: center line = median; box = upper and lower quartiles; whiskers = values within +/- 1.5*IQR. Source data are provided as a Source Data file."
- **Screenshot**: figure4.png (full journal page 8, all 3 panels a-c; caption on page 9 quoted above)
- **Figure type**: mixed (panels a, b = spatial-coordinate diagrams/qualitative_sample of tissue sections; panel c = quantitative box/violin plots with exact printed p-values, quoted in the caption itself)
- **Extraction method**: exact_from_labels (panel c per-gene p-values are printed verbatim in the caption); visual_description (panels a, b are spatial tissue-section renderings, not numeric plots)
- **Reading confidence**: high (panel c p-values are directly quoted text, not digitized); medium (panels a/b qualitative spatial pattern reading)

## Visual description

- **Panel a (diagram/qualitative_sample, plaques)**: 7 tissue-section renderings, one per donor,
  labeled "AD001- CTR," "AD003- Braak1," "AD007- Braak2," "AD004- Braak3," "AD010- Braak4,"
  "AD005- Braak5," "AD013- Braak6," each a pale-blue-to-dark-blue speckled cell-coordinate grid
  (oligodendrocyte-density shading) with scattered small colored dots (other cell markers) and dark
  navy squares marking plaque locations. Plaque density visibly increases from AD001 (almost no
  dark squares) through AD005/AD013 (dense dark-blue plaque clusters, especially concentrated along
  what appears to be the GM/WM boundary), consistent with increasing Braak stage.
- **Panel b (diagram/qualitative_sample, tangles)**: 6 tissue sections ("AD004- Braak3,"
  "AD002- Braak4," "AD010- Braak4," "AD005- Braak5," "AD008- Braak6," "AD013- Braak6"), same
  cell-coordinate grid format, with magenta/pink squares marking tangle locations instead of plaques.
  Tangle density is visibly sparser and more scattered than plaque density in panel a, with
  AD005/AD013 showing the most magenta markers.
- **Panel c (box/violin plots, exact p-values quoted in caption)**: A grid of gene-by-cell-type
  violin+box plot panels, split into a "Counts per cell (GM)" section (green left-margin bar; 11
  panels: ACTG1_Glut, CC2D1B_Glut, PPP1R1A_Glut, ALDH1A1_Glut, TM2D1_Glut, ACTG1_GABA, SCG3_GABA,
  PDCD6_GABA, CD74_Microg, P2RY12_Microg, GFAP_Astro) and a "Counts per cell (WM)" section (orange
  left-margin bar; 2 panels: PDCD6_GABA, ANXA7_GABA), each showing three Braak-stage-tertile
  distributions (0-1/2-4/5-6, legend at bottom) with red asterisk(s) marking statistical
  significance. Visually: ACTG1_Glut, PDCD6_GABA (GM and WM), TM2D1_Glut, ALDH1A1_Glut show a
  decreasing trend into Braak 5-6 (one red asterisk each); CC2D1B_Glut and GFAP_Astro show an
  *increasing* trend into Braak 5-6 (CC2D1B with two asterisks, GFAP with two asterisks); PPP1R1A_Glut
  shows a rise at Braak 2-4 (one asterisk on that bracket); CD74_Microg and P2RY12_Microg both show a
  decreasing trend (P2RY12 with two asterisks); ANXA7_GABA (WM) shows a decreasing trend (one
  asterisk).

## Data table (panel c — exact p-values quoted verbatim in the figure caption)

| Gene_CellType | Tissue | p-value | Significance |
|---|---|---|---|
| ACTG1_Glut | GM | 0.02 | * |
| CC2D1B_Glut | GM | 0.001 | ** |
| PPP1R1A_Glut | GM | 0.02 | * |
| ALDH1A1_Glut | GM | 0.011 | * |
| TM2D1_Glut | GM | 0.02 | * |
| ACTG1_GABA | GM | 0.006 | ** |
| SCG3_GABA | GM | 0.016, 0.002 | * / ** (two comparisons) |
| PDCD6_GABA | GM | 0.013 | * |
| CD74_Microg | GM | 0.012 | * |
| P2RY12_Microg | GM | 0.001 | ** |
| GFAP_Astro | GM | 0.0001 | ** |
| PDCD6_GABA | WM | 0.03 | * |
| ANXA7_GABA | WM | 0.012 | * |

## Trend summary
Panel a's plaque density visibly tracks Braak stage from AD001 (control) to AD013 (Braak6), and
panel c's 13 exact p-values are the direct source of `logic/claims.md` C09's per-gene Braak-stage
validation statistics in intact CARTANA tissue (matching values transcribed there verbatim).
