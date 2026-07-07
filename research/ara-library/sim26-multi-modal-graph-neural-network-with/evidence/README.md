# Evidence Index

This paper contains exactly 2 numbered tables and 3 numbered figures in its 10-page main text (no
appendix/supplementary material was provided with this ARA's input, per the paper's own statement
that "More details are given in the supplementary," §3). All 2 tables and all 3 figures are filed
below — a complete, ordered sweep with no omissions.

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1.md](tables/table1.md) | Table 1, §3 | C01 | Main benchmark: GTAD vs. 9 baselines (GCN, GAT, GraphHeat, GDC, ADC, LSAP, NodeFormer, DIFFormer, SGFormer) × 4 modality combinations, 3-way (CN/SMC/EMCI) classification, 5-fold CV. |
| [tables/table2.md](tables/table2.md) | Table 2, §4 | C02, C03 | Ablation: 3 convolution-block types (MLP, Graph Convolution, Adaptive Convolution) × 2 attention settings (position-wise vs. multi-modal). |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1.md](figures/figure1.md) | Figure 1, §2 | (architecture; not directly cited by a specific claim) | GTAD architecture diagram: adaptive convolution block → self-attention block → classifier, with the scale-update backprop loop. |
| [figures/figure2.md](figures/figure2.md) | Figure 2, §4 | C04 | Brain-surface visualization of learned per-modality node scales + exact table of the 8 smallest-scale ROIs per modality. |
| [figures/figure3.md](figures/figure3.md) | Figure 3, §4 | C05 | Per-modality total-attention-score bar charts + exact table of the top-5 ROIs by Importance Rate per modality. |

## Accounting

No numbered table or figure was excluded. Figure 1 supports the architectural description in
`logic/solution/architecture.md` rather than a specific falsifiable claim in `logic/claims.md`
(it is a diagram, not a results figure), so it is not listed under a claim ID above but is
cross-referenced from the architecture file.
