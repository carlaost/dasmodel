# Claims

> Grounding: abstract-only. All load-bearing numbers below are stated verbatim in the paper's
> abstract; each is grounded to the abstract text via a `**Sources**` entry. No numbers were taken
> from a full text (none was available) and none were computed by this ARA. `[result]` tags mark
> values the paper reports as outcomes; `[input]` tags mark values that are design/configuration
> settings.

## C01: Near-centralized balanced accuracy under federation
- **Statement**: The privacy-preserving federated framework achieves a balanced accuracy of 80.7%
  on a stratified four-client federation derived from ADNI, closely approaching the centralized
  upper bound of 82.1%.
- **Status**: supported (per abstract; not independently verifiable without full text)
- **Falsification criteria**: Reproducing the framework on an equivalent ADNI four-client
  federation yields balanced accuracy materially below 80.7%, or the centralized upper bound is not
  ≈82.1%, or the federated–centralized gap is substantially larger than the reported ~1.4 points.
- **Proof**: [E01]
- **Evidence basis**: The abstract reports both figures directly for the ADNI four-client
  evaluation. No per-class or per-client breakdown is available (no full text).
- **Interpretation**: A ~1.4-point balanced-accuracy gap to centralized training suggests the
  federated design pays only a small accuracy cost for privacy — but this synthesis rests solely on
  the two headline numbers.
- **Dependencies**: none
- **Sources**:
  - 80.7% ← metadata.md abstract «our framework achieved a state-of-the-art balanced accuracy of 80.7%, closely approaching the centralized upper bound (82.1%)» [result]
  - 82.1% ← metadata.md abstract «closely approaching the centralized upper bound (82.1%)» [result]
  - four-client federation ← metadata.md abstract «Evaluated on a stratified four-client federation derived from the Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort» [input]
- **Tags**: federated-learning, balanced-accuracy, ADNI, AD-staging

## C02: 99% reduction in federated communication overhead
- **Statement**: Low-Rank Adaptation (LoRA) combined with dynamic token gating reduces
  communication overhead by 99% — to 140 KB/round — compared to standard federated averaging.
- **Status**: supported (per abstract)
- **Falsification criteria**: Measured per-round communication of the described method is not
  ≈140 KB, or does not represent a ≈99% reduction relative to a standard FedAvg baseline of the
  same model.
- **Proof**: [E02]
- **Evidence basis**: The abstract states the reduction (99%) and the absolute per-round payload
  (140 KB/round) against standard federated averaging.
- **Interpretation**: Parameter-efficient adaptation makes each communication round cheap enough for
  scalable distributed clinical training; the baseline payload size is not given (no full text).
- **Dependencies**: none
- **Sources**:
  - 99% ← metadata.md abstract «Low-Rank Adaptation (LoRA) and dynamic token gating, reducing communication overhead by 99% (to 140 KB/round) compared to standard federated averaging» [result]
  - 140 KB/round ← metadata.md abstract «reducing communication overhead by 99% (to 140 KB/round)» [result]
- **Tags**: LoRA, token-gating, communication-efficiency, federated-averaging

## C03: Uncertainty-driven hierarchical attention fusion
- **Statement**: A hierarchical attention fusion mechanism dynamically weights the four input
  modalities based on predictive uncertainty.
- **Status**: hypothesis (mechanism asserted in abstract; supporting evidence not available)
- **Falsification criteria**: Ablating or replacing the uncertainty-driven weighting with static
  fusion does not change modality weights or does not affect performance/robustness, contradicting
  the claim that weighting is dynamic and uncertainty-driven.
- **Proof**: [E03]
- **Evidence basis**: The abstract describes the mechanism; no ablation numbers are available
  (no full text).
- **Interpretation**: Dynamic, uncertainty-aware fusion is plausibly the source of the reported
  robustness to domain shift, but the abstract does not quantify its isolated contribution.
- **Dependencies**: C01
- **Sources**:
  - hierarchical attention fusion / predictive uncertainty ← metadata.md abstract «A hierarchical attention fusion mechanism that dynamically weights modalities based on predictive uncertainty» [input]
- **Tags**: attention-fusion, multimodal, uncertainty, modality-weighting

## C04: Consensus cross-site explainability without sharing raw data
- **Statement**: A fuzzy-rough hybrid explainability pipeline synthesizes client-specific saliency
  maps into a consensus-driven, clinically coherent interpretation without sharing raw data, with
  consistent cross-site interpretability measured at a Dice similarity of 0.84.
- **Status**: supported (per abstract)
- **Falsification criteria**: Cross-site saliency agreement is materially below a Dice similarity
  of 0.84, or the pipeline requires exchanging raw patient data to reach consensus.
- **Proof**: [E04]
- **Evidence basis**: The abstract reports both the mechanism (fuzzy-rough hybrid, no raw-data
  sharing) and the cross-site consistency metric (Dice similarity 0.84).
- **Interpretation**: The Dice figure is presented as evidence of "consistent cross-site
  interpretability"; whether it measures agreement between clients, or against a reference, is not
  specified (no full text).
- **Dependencies**: C01
- **Sources**:
  - Dice similarity 0.84 ← metadata.md abstract «consistent cross-site interpretability (Dice similarity: 0.84)» [result]
  - fuzzy-rough hybrid / no raw-data sharing ← metadata.md abstract «A fuzzy-rough hybrid explainability pipeline that synthesizes client-specific saliency maps into a consensus-driven, clinically coherent interpretation without sharing raw data» [input]
- **Tags**: explainability, fuzzy-rough, saliency, Dice, privacy

## C05: Superior robustness to simulated domain shifts
- **Statement**: The framework demonstrates superior robustness to simulated domain shifts relative
  to the compared approaches.
- **Status**: hypothesis (comparative claim asserted in abstract; magnitudes not available)
- **Falsification criteria**: Under simulated domain shift, the framework's performance degrades as
  much as or more than standard federated baselines.
- **Proof**: [E01]
- **Evidence basis**: The abstract asserts "superior robustness to simulated domain shifts"; no
  quantitative shift-robustness figures are available (no full text).
- **Interpretation**: Robustness is attributed (implicitly) to the uncertainty-driven fusion (C03),
  but the abstract does not isolate the mechanism responsible.
- **Dependencies**: C01, C03
- **Sources**:
  - superior robustness to simulated domain shifts ← metadata.md abstract «demonstrating superior robustness to simulated domain shifts» [result]
- **Tags**: robustness, domain-shift, federated-learning
