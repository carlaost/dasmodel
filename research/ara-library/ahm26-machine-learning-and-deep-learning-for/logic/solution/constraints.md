# Constraints, Assumptions, and Limitations

## Nature of the work
- This is a **narrative literature survey**, explicitly "designed as a structured narrative survey
  rather than a formal systematic review" (PDF p.623). No PROSPERO registration; no formal search
  protocol, inclusion/exclusion PRISMA flow, or meta-analytic pooling.
- The paper **releases no new code, data, model, or empirical result**. It conducts no experiments of
  its own. All figures/tables are schematic or qualitative summaries.

## Scope boundaries (as stated by the authors)
- Coverage is **~10-15 representative and influential studies** (8 named primary studies), not an
  exhaustive catalogue.
- Emphasis is on **neuroimaging-based** AD diagnosis (structural MRI, PET, and multimodal combinations
  of imaging + non-imaging data); non-imaging variables are considered when they contribute to
  multimodal/graph/explainability discussion.
- The survey **prioritizes methodological contribution and clinical relevance over reported accuracy**
  and deliberately avoids leaderboard-style numerical ranking.

## Assumptions
- A1: A curated narrative sample adequately represents the field's main methodological directions.
- A2: Task difficulty and translational value are more informative than headline accuracy.
- A3: Public benchmark cohorts (ADNI, OASIS-3, AIBL) are representative of the field's data practices.

## Limitations of the survey itself
- **No quantitative synthesis**: because tasks, datasets, splits, and preprocessing differ across
  studies, the paper does not (and argues it cannot) directly compare reported metrics; it therefore
  presents no pooled performance numbers.
- **Selection is curated, not exhaustive**: influential-study selection is subjective and may omit
  relevant work.
- **Dependence on a small evidence base**: conclusions rest on 8 primary studies plus supporting
  reviews.
- **Field-level, not deployment-tested claims**: the survey's conclusions describe trends in the
  literature; it provides no independent validation.

## Limitations of the surveyed field (carried forward as the paper's core critique)
- **Benchmark/dataset dependence** (especially ADNI); limited external and cross-site validation.
- **Evaluation heterogeneity**: inconsistent tasks, splits, diagnostic definitions, and preprocessing.
- **Class imbalance** across diagnostic categories.
- **Missing-modality problems** in real multimodal datasets.
- **Reproducibility weaknesses**: inconsistent preprocessing, incomplete methodological/hyperparameter
  reporting, limited code/data release.
- **Interpretability under-evaluation**: explanations rarely tested for stability, plausibility,
  reproducibility, or clinical utility.
- **Transformer/GNN maturity**: superiority over strong multimodal CNN baselines not yet established;
  transformers are data-hungry, GNNs sensitive to graph-construction choices.
- **Clinical-translation gap**: strong experimental performance does not guarantee usefulness under
  scanner variation, uncertainty, and heterogeneous populations.
