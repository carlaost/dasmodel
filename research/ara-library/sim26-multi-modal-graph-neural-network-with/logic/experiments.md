# Experiments

## E01: Main classification benchmark against nine GNN baselines
- **Verifies**: C01
- **Setup**:
  - Model: GTAD (adaptive convolution block + modality-wise self-attention block + classifier),
    compared against nine baselines in three families — convolution-based (GCN, GAT),
    diffusion-based (GraphHeat, GDC, ADC, LSAP), and graph-transformer (NodeFormer, DIFFormer,
    SGFormer)
  - Hardware: Not specified in paper
  - Dataset: ADNI, N=919 preclinical AD subjects (CN=333, SMC=172, EMCI=414), 160-ROI Destrieux
    parcellation, DTI-derived structural brain networks as graph structure
  - System: 5-fold cross-validation; four separate modality combinations (Cortical Thickness &
    β-Amyloid; Cortical Thickness & FDG; β-Amyloid & FDG; All Imaging Features) each run as an
    independent 3-way classification task
- **Procedure**:
  1. For each modality combination, construct per-subject brain graphs with the Destrieux
     parcellation and DTI tractography-derived edges.
  2. Assign nodal features from the specified imaging modality/modalities (cortical thickness,
     FDG-PET SUVR, β-Amyloid PET).
  3. Train each of the 10 methods (9 baselines + GTAD) under 5-fold CV to predict the 3-way
     CN/SMC/EMCI label.
  4. Compute mean and standard deviation of accuracy, precision, and recall across the 5 folds for
     each method and modality combination.
- **Metrics**: Accuracy, precision, recall (mean ± std over 5 folds), each in [0, 1]
- **Expected outcome**:
  - GTAD outperforms all nine baselines on all three metrics in all four modality combinations.
  - Graph-transformer baselines (NodeFormer, DIFFormer, SGFormer) outperform convolution-based and
    single-mechanism diffusion baselines, consistent with the paper's motivating claim that
    long-range attention captures information convolution/diffusion-only methods miss.
  - GTAD's fold-to-fold standard deviations are comparably low to the best baselines, supporting a
    stability claim.
- **Baselines**: GCN [12], GAT [22], GraphHeat [26], GDC [7], ADC [27], LSAP [18], NodeFormer [24],
  DIFFormer [23], SGFormer [25]
- **Dependencies**: none

## E02: Ablation on convolution-block type and attention mechanism
- **Verifies**: C02, C03
- **Setup**:
  - Model: Three convolution-block variants (Multi-Layer Perceptron, Graph Convolution Layer,
    Adaptive Convolution Layer) crossed with two attention variants (position-wise attention from
    concatenated per-modality features into a single encoder [21], vs. the paper's multi-modal
    (MM) per-modality-head attention), yielding 6 configurations
  - Hardware: Not specified in paper
  - Dataset: ADNI (same cohort/parcellation as E01); modality combination(s) used for this ablation
    not explicitly restated in §4's ablation subsection (paper text does not specify which of the
    four E01 modality combinations underlies Table 2)
  - System: 5-fold cross-validation (consistent with the rest of the paper's protocol)
- **Procedure**:
  1. For each of the 3 convolution-block types, build an encoder producing per-node representations
     (MLP/GraphConv/Adaptive Convolution in place of Eq. 3's adaptive convolution).
  2. Attach either position-wise attention (single encoder over concatenated multi-modal features)
     or the paper's multi-modal per-modality-head attention (Eq. 4–5).
  3. Train and evaluate each of the 6 combinations under the same classification protocol as E01.
  4. Compare accuracy/precision/recall across the 6 rows.
- **Metrics**: Accuracy, precision, recall (mean ± std over 5 folds)
- **Expected outcome**:
  - Adaptive Convolution Layer outperforms both MLP and Graph Convolution Layer as the convolution
    block, regardless of attention type.
  - Adding multi-modal attention improves every convolution-block variant, but the improvement is
    substantially larger for the Adaptive Convolution Layer than for MLP or Graph Convolution Layer.
  - The best overall configuration is Adaptive Convolution Layer + multi-modal attention.
- **Baselines**: The 5 non-best configurations within Table 2 serve as each other's baselines (no
  external baseline models from E01 are re-used here)
- **Dependencies**: none

## E03: Post-hoc interpretation of trained scales and attention scores
- **Verifies**: C04, C05
- **Setup**:
  - Model: The trained GTAD model (from E01, "All Imaging Features" or per-modality setting — the
    paper does not disambiguate which trained instance produced Fig. 2/Fig. 3)
  - Hardware: Not specified in paper
  - Dataset: ADNI, same 160-ROI parcellation as E01
  - System: Analysis performed on trained-model parameters and forward-pass attention weights, not
    a retraining experiment
- **Procedure**:
  1. Extract the final trained node-wise scale vectors `s^m` for each modality `m`.
  2. Visualize `s^m` per ROI on brain-surface renderings, separately per modality and hemisphere.
  3. Identify the 8 ROIs with the smallest trained scale per modality.
  4. Extract per-ROI total attention scores from the trained self-attention block per modality;
     compute Importance Rate (IR) as the fraction of ROIs whose highest attention score points to
     each ROI.
  5. Identify the 5 ROIs with the highest IR per modality.
  6. Cross-reference the resulting ROI lists (smallest-scale and highest-IR) against prior
     neuroscience/AD literature citations.
- **Metrics**: Node-wise scale value (unitless, positive real); total attention score (count);
  Importance Rate (%)
- **Expected outcome**:
  - Smallest-scale ROIs differ across modalities even at the same anatomical location, supporting
    the interpretability claim that scale encodes modality-specific local/global information need.
  - A consistent top-IR ROI (or small set of ROIs) emerges across modalities, and this ROI set
    overlaps with regions independently reported as AD-relevant in cited prior work.
- **Baselines**: none (descriptive/interpretive analysis, not a comparative benchmark)
- **Dependencies**: E01
