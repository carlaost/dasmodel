# Metrics — tit26-automated-high-throughput-quantification-of-plasma

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 11 · Experiments: 9 · DOI: 10.1186/s13195-026-01996-8

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (32/32 links)
- Environment completeness: **0.714** (5/7 fields)
- Spec-completeness (setup proxy): 0.0
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.796** (78/98 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 11}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.091** (1 complete dead-ends)
- Decision branching factor: 1.5
- Explicit-vs-inferred ratio: 1.0
- Failure-knowledge preservation: 0.077
- Negative-result share: 0.083
- Node types: {'question': 1, 'decision': 2, 'experiment': 9, 'dead_end': 1}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 3, 'extends': 1, 'refutes': 0, 'bounds': 4, 'baseline': 5}
- Corrective-science score: **9**
- Concepts defined: 13 · related-work blocks: 13

## D6 Real-world grounding & translation
- Clinical trials linked: **0** (verified NCTs: [])
- Datasets linked: 1 (1 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
