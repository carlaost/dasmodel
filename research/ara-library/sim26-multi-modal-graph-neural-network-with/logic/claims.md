# Claims

> All values are point estimates (mean ± std over 5-fold cross-validation) copied exactly from
> Table 1 / Table 2 and the surrounding prose. The paper reports no confidence intervals or
> significance tests beyond the fold standard deviations shown. Page numbers below refer to the
> printed page number of the 10-page PDF.

## C01: GTAD achieves the best classification performance across all four modality combinations
- **Statement**: On 3-way (CN/SMC/EMCI) preclinical AD classification over ADNI (N=919, 5-fold CV), GTAD attains the highest accuracy, precision, and recall of all 10 compared methods (9 baselines + GTAD) in every one of four modality combinations: Cortical Thickness & β-Amyloid (0.945±0.02 / 0.901±0.03 / 0.919±0.02), Cortical Thickness & FDG (0.963±0.01 / 0.935±0.02 / 0.948±0.01), β-Amyloid & FDG (0.962±0.01 / 0.935±0.02 / 0.946±0.02), and All Imaging Features (0.963±0.01 / 0.943±0.01 / 0.941±0.02).
- **Status**: supported
- **Falsification criteria**: If any of the nine baselines (GCN, GAT, GraphHeat, GDC, ADC, LSAP, NodeFormer, DIFFormer, SGFormer) matches or exceeds GTAD's accuracy in any one of the four modality combinations in Table 1, the claim fails for that combination.
- **Proof**: [E01]
- **Evidence basis**: Table 1 rows for GTAD (Ours) are the bolded/shaded maximum in every one of the 4 modality-combination × 3 metric blocks (12 cells total).
- **Interpretation**: The paper further states "accuracy from most experiments showed over 96% except for the case using cortical thickness and β-Amyloid" (p.5), i.e., 3 of 4 modality combinations exceed 96% accuracy for GTAD, with the Cortical Thickness & β-Amyloid combination the sole exception at 94.5%.
- **Dependencies**: none
- **Tags**: classification, ADNI, benchmark, multi-modal, GNN
- **Sources**:
  - 0.945±0.02 / 0.901±0.03 / 0.919±0.02 (CT & β-Amyloid) ← `evidence/tables/table1.md` «GTAD (Ours) | 0.945±0.02 | 0.901±0.03 | 0.919±0.02» [result]
  - 0.963±0.01 / 0.935±0.02 / 0.948±0.01 (CT & FDG) ← `evidence/tables/table1.md` «GTAD (Ours) | 0.963±0.01 | 0.935±0.02 | 0.948±0.01» [result]
  - 0.962±0.01 / 0.935±0.02 / 0.946±0.02 (β-Amyloid & FDG) ← `evidence/tables/table1.md` «GTAD (Ours) | 0.962±0.01 | 0.935±0.02 | 0.946±0.02» [result]
  - 0.963±0.01 / 0.943±0.01 / 0.941±0.02 (All Imaging Features) ← `evidence/tables/table1.md` «GTAD (Ours) | 0.963±0.01 | 0.943±0.01 | 0.941±0.02» [result]
  - "accuracy from most experiments showed over 96% except for the case using cortical thickness and β-Amyloid" ← paper p.5 «and accuracy from most experiments showed over 96% except for the case using cortical thickness and β-Amyloid.» [result]

## C02: The adaptive convolution block outperforms MLP and non-adaptive graph convolution as the local-feature block
- **Statement**: With multi-modal attention held fixed (either off or on), replacing the convolution block with the paper's Adaptive Convolution Layer yields the highest accuracy: 0.945±0.03 (no MM attention) and 0.963±0.01 (with MM attention), versus 0.939±0.03 / 0.947±0.02 for a Multi-Layer Perceptron block and 0.899±0.01 / 0.900±0.01 for a non-adaptive Graph Convolution Layer block.
- **Status**: supported
- **Falsification criteria**: If the MLP or Graph Convolution Layer block matches or exceeds the Adaptive Convolution Layer's accuracy at either MM-attention setting in Table 2, the claim fails.
- **Proof**: [E02]
- **Evidence basis**: Table 2, all 6 rows (3 convolution-block types × 2 MM-attention settings): Adaptive Convolution Layer is the accuracy maximum in both the ✗ and ✓ MM-attention rows, and the ✓ row (0.963±0.01/0.943±0.01/0.941±0.02) is bolded as the overall best.
- **Interpretation**: The paper attributes this to adaptive convolution's "flexible capture of local properties for each node," in contrast to MLP (which "connects all ROIs globally") and Graph Convolution (which "is not adaptively guided by the transformer") (p.8).
- **Dependencies**: none
- **Tags**: ablation, convolution-block, adaptive-diffusion
- **Sources**:
  - 0.945±0.03 / 0.963±0.01 (Adaptive Conv, MM✗/✓) ← `evidence/tables/table2.md` «Adaptive Convolution Layer (Ours) | ✗ | 0.945±0.03 ... | ✓ | 0.963±0.01» [result]
  - 0.939±0.03 / 0.947±0.02 (MLP, MM✗/✓) ← `evidence/tables/table2.md` «Multi-Layer Perceptron | ✗ | 0.939±0.03 ... | ✓ | 0.947±0.02» [result]
  - 0.899±0.01 / 0.900±0.01 (Graph Conv, MM✗/✓) ← `evidence/tables/table2.md` «Graph Convolution Layer | ✗ | 0.899±0.01 ... | ✓ | 0.900±0.01» [result]
  - "flexible capture of local properties ... exhibits better expressive power with 94.5% accuracy" ← paper p.8 «The flexible capture of local properties for each node using adaptive graph convolution exhibits better expressive power with 94.5% accuracy.» [result]

## C03: Multi-modal attention gives its largest benefit when paired with adaptive convolution
- **Statement**: Adding multi-modal (per-modality-head) attention improves accuracy by +1.8 percentage points for the Adaptive Convolution block (94.5%→96.3%), versus +0.8pp for the MLP block (93.9%→94.7%) and +0.1pp for the non-adaptive Graph Convolution block (89.9%→90.0%).
- **Status**: supported
- **Falsification criteria**: If the accuracy delta between MM-attention off/on for the Adaptive Convolution row in Table 2 is not the largest of the three convolution-block deltas, the claim fails.
- **Proof**: [E02]
- **Evidence basis**: Table 2 deltas computed from the six accuracy cells: Adaptive Conv Δ=+0.018 (0.945→0.963), MLP Δ=+0.008 (0.939→0.947), Graph Conv Δ=+0.001 (0.899→0.900).
- **Interpretation**: The paper interprets the small MLP/GraphConv deltas as showing multi-modal attention's benefit is "very marginal" for blocks that either already connect all ROIs globally (MLP) or are not diffusion-adaptive (Graph Convolution), and states the boosted 96.3% "demonstrat[es] capturing local and global features with separate blocks but training them jointly is highly effective" (p.8).
- **Dependencies**: C02
- **Tags**: ablation, attention, joint-training
- **Sources**:
  - "This metric was boosted up to 96.3% by the multi-modal attention" ← paper p.8 «This metric was boosted up to 96.3% by the multi-modal attention, demonstrating capturing local and global features with separate blocks but training them jointly is highly effective.» [result]
  - "the effect of the multi-modal attention was very marginal" ← paper p.8 «As the MLP connects all ROIs globally and the Graph Convolution is not adaptively guided by the transformer, the effect of the multi-modal attention was very marginal.» [result]
  - Table 2 six accuracy cells ← `evidence/tables/table2.md` [result]

## C04: Trained per-modality node scales are interpretable as local/global information need
- **Statement**: The trained node-wise scales `s^m_n` differ across imaging modalities even for the same anatomical ROI, and the paper interprets small-scale ROIs as requiring only neighboring-ROI information while large-scale ROIs require distant features because they are "less effective individually"; the 8 smallest-scale ROIs per modality (Fig. 2) span subcortical regions (thalamus, putamen, globus pallidus), temporal regions (inferior/superior/occipito-temporal), and frontal regions (middle/superior/orbital).
- **Status**: supported
- **Falsification criteria**: If the smallest-scale ROI set were identical across all three modalities (no modality-specific variation), or if the paper's stated interpretation rule (small scale ↔ local, large scale ↔ distant) were contradicted by the reported scale values, the claim would fail.
- **Proof**: [E03]
- **Evidence basis**: Figure 2 top (brain-surface scale maps) shows visually distinct color patterns per modality for the same hemispheres; Figure 2 bottom table lists the 8 smallest-scale ROIs per modality with exact scale values (e.g. Cortical Thickness smallest = (R) S.cingul.Marginalis at 0.0089; β-Amyloid smallest = (R) Lat.Fis.ant.Horizont at 0.0662; FDG smallest = (L) sub.putamen at 0.0187) — none of the three modalities' top-8 lists are identical.
- **Interpretation**: "ROIs with small trained scales require information from neighboring ROIs on the classification, ROIs with large scales need distant features as they are less effective individually" (p.6); this is the paper's own interpretive claim about what the learned scale magnitude means, not an independently validated causal mechanism.
- **Dependencies**: none
- **Tags**: interpretability, scale, ROI, diffusion-kernel
- **Sources**:
  - "ROIs with small trained scales require information from neighboring ROIs ... ROIs with large scales need distant features as they are less effective individually" ← paper p.6 «Therefore, while ROIs with small trained scales require information from neighboring ROIs on the classification, ROIs with large scales need distant features as they are less effective individually.» [result]
  - "GTAD selected most independent ROIs in the subcortical regions (i.e., thalamus, putamen and globus pallidus), temporal regions ..., frontal regions ..." ← paper p.6 «GTAD selected most independent ROIs in the subcortical regions (i.e., thalamus, putamen and globus pallidus), temporal regions (i.e., inferior, superior and occipito temporal regions), frontal regions (i.e., middle, superior and orbital regions) and other important regions that are closely linked to AD.» [result]
  - Per-modality smallest-scale ROI values ← `evidence/figures/figure2.md` [result]

## C05: Attention-based Importance Rate identifies AD-associated ROIs, led by lingual gyrus
- **Statement**: Ranking ROIs by total-attention-score-derived Importance Rate (IR), the lingual gyrus (G.oc.temp.med.Lingual) is the single highest-IR ROI in all three modalities (23.13% Cortical Thickness, 28.75% β-Amyloid, 30.00% FDG); hippocampus (R. sub.hippocampus) has a high IR specifically in FDG (6.25%), and putamen (R. sub.putamen) has a high IR in both Cortical Thickness (15.63%) and β-Amyloid (14.38%).
- **Status**: supported
- **Falsification criteria**: If the top-IR ROI differed across the three modalities in Figure 3's bottom table, or if putamen/hippocampus were absent from the reported top-5 IR lists for the stated modalities, the claim fails.
- **Proof**: [E03]
- **Evidence basis**: Figure 3 bottom table lists the top-5 IR ROIs per modality with exact percentages; G.oc.temp.med.Lingual is rank 1 in all three modality columns.
- **Interpretation**: The paper links this finding to prior neuroscience literature — lingual gyrus is "especially related to processing logical order of events and encoding visual memories ... highly linked to AD [10,13]" and hippocampus/putamen are described as "one of the first areas to be affected in AD" (p.8) — but the ARA does not independently verify those cited claims; they are the paper's own citations.
- **Dependencies**: none
- **Tags**: interpretability, attention, ROI, importance-rate
- **Sources**:
  - Lingual gyrus IR 23.13% / 28.75% / 30.00% ← `evidence/figures/figure3.md` «(L/R) G.oc.temp.med.Lingual | 23.13% / 28.75% / 30.00%» [result]
  - hippocampus IR 6.25% (FDG) ← `evidence/figures/figure3.md` «(R) sub.hippocampus | 06.25 %» [result]
  - putamen IR 15.63% (CT) / 14.38% (β-Amyloid) ← `evidence/figures/figure3.md` «(R) sub.putamen | 15.63 %» and «(R) sub.putamen | 14.38 %» [result]
  - "Lingual gyrus ... is belong to temporal regions and highly linked to AD" ← paper p.8 «Notably, Lingual gyrus was detected with the highest importance rate from all modalities in common. Lingual gyrus, which is especially related to processing logical order of events and encoding visual memories, is belong to temporal regions and highly linked to AD [10,13].» [result]
  - "These regions are one of the first areas to be affected in AD" ← paper p.8 «These regions are one of the first areas to be affected in AD, indicating that they are closely associated with pre-clinical AD [16,9].» [result]
