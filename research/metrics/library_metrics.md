# Library metrics rollup

Computed over **10** compiled ARAs by `research/metrics/compute_metrics.py`.
`pending_*` metrics need an LLM judge / sandbox / external DB and are not fabricated.

## Aggregate distributions (per-ARA [det] metrics)

| Metric | mean | median | min | max | n |
|---|---|---|---|---|---|
| cross_layer_binding_resolvability | 0.988 | 1.0 | 0.933 | 1.0 | 10 |
| environment_completeness | 0.814 | 0.928 | 0.429 | 1.0 | 10 |
| claim_grounding_ratio | 0.796 | 0.889 | 0.0 | 1.0 | 10 |
| falsifiability_presence | 1.0 | 1.0 | 1.0 | 1.0 | 10 |
| dead_end_density_per_claim | 0.086 | 0.045 | 0.0 | 0.25 | 10 |
| decision_branching_factor | 1.361 | 1.75 | 0 | 3 | 9 |
| explicit_vs_inferred_ratio | 0.841 | 1.0 | 0.0 | 1.0 | 10 |
| corrective_science_score | 4.6 | 3.5 | 0 | 12 | 10 |
| clinical_trials_linked | 1.1 | 0.0 | 0 | 8 | 10 |
| seal_L1_structural_score | 0.98 | 1.0 | 0.8 | 1.0 | 10 |

## D5 Cross-library claim graph

- Papers: 10 · total claims: 84
- Shared clinical-trial clusters (corroboration proxy): **0**
- In-library citation-reuse edges: **0**
- Claim redundancy (proxy): 0 near-dup pairs, rate 0.0
- FOL claim graph: pending_model

