# Figure 3: Distribution of attention scores across brain regions + top-5 ROIs by Importance Rate

- **Source**: Figure 3, §4 (Interpretation of the Trained GTAD — Pre-clinical AD via ROI Attention)
- **Caption**: "Top: Distribution of attention scores across all brain regions with cortical
  thickness (left), β-Amyloid (center) and FDG (right). Bottom: Corresponding ROIs with the 5
  highest attention scores for classification. Importance Rate (IR) indicates how many ROIs pay
  attention. (L) and (R) denote left and right hemisphere, respectively."
- **Screenshot**: figure3.png
- **Figure type**: mixed (top = quantitative bar chart; bottom = exact-value table)
- **Extraction method**: digitized_estimate (top bar heights) + exact_from_labels (bottom table
  percentages)
- **Reading confidence**: medium (top — bar peak heights read against gridlines, not exact data
  labels); high (bottom — table values printed exactly)

## Top: Quantitative plot (per-modality total attention score vs. ROI index)

- **Plot kind**: bar chart (one panel per modality, three panels total)
- **Axes**: X = ROI index (0–160, linear, unitless — one bar per one of the 160 ROIs), Y = "Total
  attention scores" (count, linear scale; Cortical Thickness panel ticks at 0/5/10/15/20/25/30/35;
  β-Amyloid panel ticks at 0/10/20/30/40; FDG panel ticks at 0/10/20/30/40/50)

| Modality | Approx. tallest bar (ROI index ≈, score ≈) | Approx. 2nd tallest (ROI index ≈, score ≈) | Approx. 3rd tallest (ROI index ≈, score ≈) |
|---|---|---|---|
| Cortical Thickness | ROI≈22, score≈36 | ROI≈160, score≈25 | ROI≈128, score≈19 |
| β-Amyloid | ROI≈100, score≈38 | ROI≈160, score≈24 | ROI≈120, score≈9 |
| FDG | ROI≈100, score≈48 | ROI≈50, score≈40 | ROI≈120, score≈13 |

> All numeric bar-height readings above are digitized estimates (`≈`) from visual inspection of
> bar tops against gridlines; they are not printed as exact data labels in the source and should
> not be treated as precise values. The bottom table's Importance Rate percentages (below) ARE
> exact source values and should be preferred for any quantitative claim.

## Trend summary
Each modality shows a small number of ROIs with a sharply higher total attention score than the
rest of the ~160 ROIs (a peaked, non-uniform distribution), with the tallest peak concentrated in
a different region of the 0–160 ROI-index range per modality (Cortical Thickness peak near
ROI≈20; β-Amyloid and FDG both show a tall peak near ROI≈100, plus FDG has a second comparably
tall peak near ROI≈50). This peaked-distribution pattern is the visual basis for defining
"Importance Rate" as a small top-K ranking (bottom table) rather than a continuous measure over
all ROIs.

## Bottom: Top-5 ROIs by Importance Rate (IR) per modality (exact table)

| Cortical Thickness — ROI | IR | β-Amyloid — ROI | IR | FDG — ROI | IR |
|---|---|---|---|---|---|
| (L) G.oc.temp.med.Lingual | 23.13 % | (R) G.oc.temp.med.Lingual | 28.75 % | (R) G.oc.temp.med.Lingual | 30.00 % |
| (R) sub.putamen | 15.63 % | (R) G.subcallosal | 16.88 % | (L) S.collat.transv.post | 25.00 % |
| (R) S.interm.prim.Jensen | 11.88 % | (R) sub.putamen | 14.38 % | (R) S.collat.transv.post | 08.13 % |
| (R) S.front.inf | 07.50 % | (L) Pole.occipital | 10.63 % | (R) sub.hippocampus | 06.25 % |
| (L) sub.globus.pallidus | 06.88 % | (R) S.collat.transv.post | 05.63 % | (R) G.subcallsoal | 05.63 % |

> Note: "G.subcallsoal" (FDG column, row 5) is transcribed exactly as printed in the source table
> (compare "G.subcallosal" in the β-Amyloid column, row 2) — no spelling correction applied, to
> preserve fidelity to the original.

Supports C05: lingual gyrus (G.oc.temp.med.Lingual) is the rank-1 IR ROI in all three modalities;
putamen appears in both the Cortical Thickness and β-Amyloid top-5 lists; hippocampus appears in
the FDG top-5 list.
