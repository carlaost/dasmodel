# Metrics — kes25-the-alzheimer-s-disease-diagnosis-and

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 10 · Experiments: 9 · DOI: 10.1002/alz.71147

## D1 Reproducibility
- Cross-layer binding resolvability: **0.971** (33/34 links)
- Environment completeness: **0.714** (5/7 fields)
- Spec-completeness (setup proxy): 0.0
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.722** (57/79 numbers)
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
- Node types: {'question': 7, 'experiment': 8, 'decision': 3, 'dead_end': 3}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 1, 'extends': 2, 'refutes': 0, 'bounds': 2, 'baseline': 4}
- Corrective-science score: **6**
- Concepts defined: 9 · related-work blocks: 9

## D6 Real-world grounding & translation
- Clinical trials linked: **0** (verified NCTs: [])
- Datasets linked: 4 (4 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
