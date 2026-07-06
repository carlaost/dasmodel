# Claims

> Grounding: abstract-only. Every load-bearing number below is quoted verbatim from the paper's
> abstract as reproduced in `metadata.json` / `metadata.md`, or from the verified dataset record
> in `sources.yaml`. Full text was unavailable (the provided PDF is a different paper — see
> PAPER.md). Statuses reflect what the abstract *asserts as results*; they could NOT be
> independently verified against tables/figures because no full text was extracted. Evidence
> basis makes the abstract-only limitation explicit for each claim.

## C01: MobileNet-V3 Large is the most accurate of the three architectures
- **Statement**: Among MobileNet-V3 Large, EfficientNet-B4, and ResNet-50, MobileNet-V3 Large achieved the highest AD-severity classification accuracy: 99.18% on the augmented test set and 99.47% on the original dataset.
- **Status**: supported (per abstract; not independently verifiable here)
- **Falsification criteria**: A per-model accuracy table showing EfficientNet-B4 or ResNet-50 equalling or exceeding MobileNet-V3 Large on the augmented test set or the original dataset would refute this.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract directly states MobileNet-V3's accuracies and that they are "the highest". No per-model results table was available (no full text), so the ranking rests on the abstract's own summary.
- **Interpretation**: Accuracy ≥99% on both augmented and original data suggests strong in-distribution performance, but abstract-level numbers cannot confirm the absence of overfitting to the augmented distribution.
- **Sources**:
  - 99.18% ← Abstract «MobileNet-V3 achieved the highest accuracy (99.18% on the augmented test set; 99.47% on the original dataset)» [result]
  - 99.47% ← Abstract «(99.18% on the augmented test set; 99.47% on the original dataset)» [result]
- **Dependencies**: none
- **Tags**: accuracy, model-comparison, MobileNet-V3, benchmark

## C02: MobileNet-V3 Large is the most parameter-efficient of the three
- **Statement**: MobileNet-V3 Large achieves the best accuracy while using the fewest parameters (4.2M) of the three architectures, making it the most computationally efficient and clinically suitable.
- **Status**: supported (per abstract; not independently verifiable here)
- **Falsification criteria**: A parameter-count table showing EfficientNet-B4 or ResNet-50 with ≤4.2M parameters, or MobileNet-V3 Large with more parameters than a competing model that also matched its accuracy, would refute the efficiency claim.
- **Proof**: [E01]
- **Evidence basis**: The abstract states MobileNet-V3 uses "the fewest parameters (4.2M)". EfficientNet-B4 and ResNet-50 parameter counts were not available (no full text); the "fewest" ordering rests on the abstract.
- **Interpretation**: Combining highest accuracy with lowest parameter count is what the authors use to argue clinical suitability; the efficiency-vs-accuracy trade-off is resolved in MobileNet-V3's favour.
- **Sources**:
  - 4.2M ← Abstract «while using the fewest parameters (4.2M), confirming its efficiency and suitability for clinical use» [result]
- **Dependencies**: C01
- **Tags**: efficiency, parameter-count, MobileNet-V3, clinical-deployment

## C03: XRAI attribution maps align with known AD neuroanatomy
- **Statement**: The integrated XRAI region-based attribution maps produced visualizations that aligned with known neuroanatomical patterns of AD progression, enhancing clinical interpretability.
- **Status**: supported (per abstract; qualitative, not independently verifiable here)
- **Falsification criteria**: XRAI attribution maps concentrating on regions unrelated to established AD neuroanatomy (e.g. non-brain background or regions not implicated in AD), or a formal overlap analysis showing no correspondence, would refute this.
- **Proof**: [E03]
- **Evidence basis**: The abstract asserts alignment with "known neuroanatomical patterns of AD progression". No attribution-map figures or quantitative overlap metrics were available (no full text); this is a qualitative abstract-level assertion.
- **Interpretation**: Neuroanatomically plausible attributions are used as evidence that the model's decisions are clinically trustworthy, though the abstract reports no quantitative alignment metric.
- **Sources**:
  - alignment claim ← Abstract «XRAI visualizations aligned with known neuroanatomical patterns of AD progression, enhancing clinical interpretability» [result]
- **Dependencies**: C01
- **Tags**: explainability, XRAI, attribution, interpretability

## C04: The Gradio web interface delivers sub-20-second, high-confidence inference
- **Statement**: The web-based Gradio clinical interface delivered sub-20-second inference with high classification confidence across all four AD severity levels.
- **Status**: supported (per abstract; not independently verifiable here)
- **Falsification criteria**: Measured end-to-end inference latency ≥20 seconds, or low/uncertain confidence for one or more severity classes on the deployed interface, would refute this.
- **Proof**: [E04]
- **Evidence basis**: The abstract states "sub-20 second inference with high classification confidence across all AD severity levels". No latency table or confidence distribution was available (no full text).
- **Interpretation**: The latency and confidence figures are the authors' argument for real-world deployability; exact per-class latencies and confidences are not recoverable from the abstract.
- **Sources**:
  - sub-20 second ← Abstract «The web interface delivered sub-20 second inference with high classification confidence across all AD severity levels» [result]
- **Dependencies**: C01
- **Tags**: deployment, latency, Gradio, usability

## C05: First systematic integration of XRAI into MRI-based AD severity classification
- **Statement**: This work is the first systematic integration of XRAI into AD severity classification using MRI and deep learning.
- **Status**: hypothesis (novelty claim; not independently verifiable here)
- **Falsification criteria**: A prior peer-reviewed study applying XRAI to AD severity classification on MRI with deep learning would refute the novelty claim.
- **Proof**: [E03]
- **Evidence basis**: The abstract's Conclusion states "This research presents the first systematic integration of XRAI into AD severity classification using MRI and deep learning." No literature comparison table was available (no full text), so the novelty priority claim cannot be checked here.
- **Interpretation**: A priority/novelty claim; treated as a hypothesis in this ARA because verifying "first" requires the full related-work analysis, which was not available.
- **Sources**:
  - novelty claim ← Abstract «This research presents the first systematic integration of XRAI into AD severity classification using MRI and deep learning» [result]
- **Dependencies**: C03
- **Tags**: novelty, XRAI, contribution
