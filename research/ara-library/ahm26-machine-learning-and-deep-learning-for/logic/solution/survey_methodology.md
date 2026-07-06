# Survey Methodology (Design and Study Selection)

Grounded in "Scope and Selection of Representative Studies" (PDF p.623) and the Introduction.

## Survey type
- A **structured narrative survey**, explicitly not a formal systematic review. Purpose: synthesize a
  representative body of influential work, not exhaustively catalogue the literature.

## Organizing axes
- The literature is organized into **five broad groups**: (1) traditional machine learning,
  (2) convolutional deep learning, (3) multimodal fusion, (4) transformer and hybrid attention models,
  (5) graph neural networks with explainability components.
- Emphasis is on **conceptual evolution**, **comparative strengths of model families**, and
  **methodological features relevant to clinical translation** — deliberately over leaderboard-style
  numerical comparison.

## Selection criteria (as stated)
- Target coverage: **approximately 10 to 15 representative and influential studies** spanning early
  MRI-based CNNs, multimodal MRI+PET systems, attention-based fusion, GNNs, transformer-equipped
  architectures, and explainability-oriented approaches.
- Review papers are additionally included when they support broader observations about datasets,
  modality trends, evaluation practices, and unresolved limitations.
- Studies were "chosen because they are methodologically distinct, widely discussed in the field, and
  collectively adequate to support a coherent survey taxonomy."

## The 8 named primary studies (Table 1)
| # | Study | Year | Modality / Data | Core Method |
|---|-------|------|-----------------|-------------|
| 1 | Islam & Zhang | 2018 | MRI | Ensemble CNN |
| 2 | Lu et al. | 2018 | MRI + FDG-PET | Multimodal multiscale DNN |
| 3 | Golovanevsky et al. | 2022 | Imaging + genetic + clinical | Attention-based multimodal DL |
| 4 | Qiu et al. | 2022 | Imaging + non-imaging multimodal | Successive-step multimodal DL |
| 5 | Zhang et al. | 2023 | sMRI + PET + phenotypic | Multi-modal GNN |
| 6 | Castellano et al. | 2024 | 2D/3D MRI + amyloid PET | Uni-modal and multimodal CNNs |
| 7 | Hu et al. | 2024 | Claims / relational health data | Self-explainable GNN |
| 8 | Zhao et al. | 2024 | 3D MRI | Transformer-equipped CNN |

## Analytical structure
The survey proceeds: Introduction → Scope/Background → Datasets & Input Modalities → Taxonomy of
Methods (six families) → Survey of Representative Studies → Comparison (Figure 6, Table 1) → Critical
Discussion (why multimodal matters; why accuracy alone is insufficient; reproducibility &
generalizability; explainability & trust; strengths/weaknesses of transformers & GNNs) → Open
Challenges → Future Directions → Conclusion.
