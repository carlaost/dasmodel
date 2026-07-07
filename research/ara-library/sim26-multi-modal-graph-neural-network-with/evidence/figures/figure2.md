# Figure 2: Learned scales on cortical regions + 8 localized ROIs with smallest trained scales

- **Source**: Figure 2, §4 (Interpretation of the Trained GTAD — Discussion on the Scales)
- **Caption**: "Top: Visualization of learned scales on the cortical regions of left (top) and
  right (bottom) hemispheres. Bottom: 8 Localized ROIs with the smallest trained scales for
  classification. (L) and (R) denote left and right hemisphere, respectively."
- **Screenshot**: figure2.png
- **Figure type**: mixed (top = quantitative heatmap rendered as brain-surface diagram;
  bottom = exact-value table)
- **Extraction method**: visual_description (top) + exact_from_labels (bottom table)
- **Reading confidence**: medium (top — colors are visually distinguishable but per-ROI scale
  cannot be read precisely off the color scale without the underlying data); high (bottom — table
  values are printed exactly)

## Top: Visual description (brain-surface scale maps)

- **Shows**: Six brain-surface renderings per modality-row-pair (lateral + medial views ×
  left/right hemisphere), one column-group per modality: **Cortical Thickness**, **β-Amyloid**,
  **FDG** (2 hemisphere views × 2 rows = 4 brain renders per modality, 12 total renders).
- **Color encoding**: A yellow→orange→red heatmap colormap, with a vertical color bar labeled from
  `0.00` (red, bottom) to `1.13` (top) — this is the shared scale range for the learned node-wise
  scale value `s^m_n` across all three modalities' brain maps.
- **Pattern observed**: Each modality's brain maps show a visually distinct spatial pattern of
  color (i.e., different ROIs are shaded red/dark vs. pale yellow) — for example, the Cortical
  Thickness maps show isolated small dark-red patches (near cingulate/temporal regions) against a
  mostly pale-yellow background, while the β-Amyloid and FDG maps show broader mid-orange shading
  across more of the lateral surface with scattered darker patches. This qualitatively supports the
  paper's statement that "even for the same region in the brain, the local ranges are set
  differently depending on the modalities" (p.6).
- **Demonstrates**: That the trained per-node scale `s^m_n` (Modality-wise Adaptive Convolution
  Block, Eq. 3) is not a single global constant but varies both by ROI and by modality — the
  qualitative basis for claim C04.
- **Supports**: C04

## Bottom: 8 Localized ROIs with the smallest trained scales per modality (exact table)

| Cortical Thickness — ROI | Scale | β-Amyloid — ROI | Scale | FDG — ROI | Scale |
|---|---|---|---|---|---|
| (R) S.cingul.Marginalis | 0.0089 | (R) Lat.Fis.ant.Horizont | 0.0662 | (L) sub.putamen | 0.0187 |
| (L) G&S.occipital.inf | 0.0153 | (L) S.oc.middle&Lunatus | 0.0771 | (L) G&S.cingul.Mid.Ant | 0.0231 |
| (L) S.front.sup | 0.0252 | (R) S.calcarine | 0.0868 | (R) S.temproal.sup | 0.0254 |
| (R) S.suborbital | 0.0254 | (R) sub.thalamus | 0.1124 | (R) sub.globus.pallidus | 0.0255 |
| (L) S.oc.temp.med&Lingual | 0.0387 | (R) G.oc.temp.lat.fusifor | 0.1159 | (L) sub.globus.pallidus | 0.0303 |
| (R) S.pericallosal | 0.0387 | (L) S.calcarine | 0.1166 | (R) G&S.cingul.Mid.Ant | 0.0451 |
| (R) S.front.middle | 0.0420 | (R) G.temporal.inf | 0.1208 | (L) S.temporal.sup | 0.0609 |
| (R) G.parietal.sup | 0.0500 | (R) S.orbital.lateral | 0.1224 | (L) S.calcarine | 0.0662 |

> Note: "S.temproal.sup" is transcribed exactly as printed in the source table (likely a
> typographical rendering of "S.temporal.sup"); no correction is applied to preserve fidelity to
> the original.

## Trend summary
Each modality's smallest-scale ROI set is distinct: Cortical Thickness's smallest scales are all
below 0.05 (cingulate/occipital/frontal/parietal regions), β-Amyloid's smallest scales are
markedly larger (0.0662–0.1224, all above the largest Cortical Thickness value in this list) and
concentrated in occipital/temporal/orbital/subcortical (thalamus) regions, while FDG's smallest
scales are intermediate (0.0187–0.0662) and concentrated in subcortical (putamen, globus pallidus)
and cingulate/temporal regions. No single ROI appears in more than one modality's top-8 smallest-
scale list in this table. Supports C04.
