# Table 2: Performance comparisons of different blocks

- **Source**: Table 2, §4 (Ablation Study on the Blocks)
- **Caption**: "Performance comparisons of different blocks. For attention block, our multi-modal
  (MM) attention and existing position-wise attention are compared."
- **Screenshot**: table2.png
- **Extraction type**: raw_table

All values are mean ± standard deviation over 5-fold cross-validation. The bottom row
(Adaptive Convolution Layer + MM Attention ✓) is bolded in the source as the overall best.
The paper does not restate which of Table 1's four modality combinations underlies this ablation
(see `logic/solution/constraints.md`, L4).

| Convolution Block | MM Attention | Accuracy | Precision | Recall |
|---|---|---|---|---|
| Multi-Layer Perceptron | ✗ | 0.939±0.03 | 0.893±0.05 | 0.913±0.04 |
| Multi-Layer Perceptron | ✓ | 0.947±0.02 | 0.906±0.04 | 0.933±0.02 |
| Graph Convolution Layer | ✗ | 0.899±0.01 | 0.835±0.03 | 0.849±0.03 |
| Graph Convolution Layer | ✓ | 0.900±0.01 | 0.834±0.03 | 0.852±0.02 |
| Adaptive Convolution Layer (Ours) | ✗ | 0.945±0.03 | 0.903±0.05 | 0.922±0.04 |
| **Adaptive Convolution Layer (Ours)** | **✓** | **0.963±0.01** | **0.943±0.01** | **0.941±0.02** |
