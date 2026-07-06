# Metrics — jes26-efficacy-and-safety-of-donanemab-in

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 10 · Experiments: 8 · DOI: 10.1016/j.tjpad.2026.100605

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (31/31 links)
- Environment completeness: **1.0** (7/7 fields)
- Spec-completeness (setup proxy): 0.25
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.939** (108/115 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 10}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.0** (0 complete dead-ends)
- Decision branching factor: 0
- Explicit-vs-inferred ratio: 1.0
- Failure-knowledge preservation: 0.143
- Negative-result share: 0.0
- Node types: {'question': 1, 'decision': 3, 'experiment': 8, 'dead_end': 2}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 4, 'extends': 2, 'refutes': 0, 'bounds': 5, 'baseline': 0}
- Corrective-science score: **12**
- Concepts defined: 14 · related-work blocks: 11

## D6 Real-world grounding & translation
- Clinical trials linked: **1** (verified NCTs: ['NCT04437511'])
- Datasets linked: 1 (1 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
