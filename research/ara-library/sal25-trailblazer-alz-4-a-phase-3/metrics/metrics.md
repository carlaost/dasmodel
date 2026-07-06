# Metrics — sal25-trailblazer-alz-4-a-phase-3

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 8 · Experiments: 6 · DOI: 10.1002/alz.70293

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (24/24 links)
- Environment completeness: **1.0** (7/7 fields)
- Spec-completeness (setup proxy): 0.0
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.725** (58/80 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 8}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.125** (1 complete dead-ends)
- Decision branching factor: 2
- Explicit-vs-inferred ratio: 1.0
- Failure-knowledge preservation: 0.091
- Negative-result share: 0.111
- Node types: {'question': 2, 'decision': 2, 'experiment': 6, 'dead_end': 1}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 5, 'extends': 2, 'refutes': 0, 'bounds': 0, 'baseline': 1}
- Corrective-science score: **2**
- Concepts defined: 10 · related-work blocks: 8

## D6 Real-world grounding & translation
- Clinical trials linked: **1** (verified NCTs: ['NCT05108922'])
- Datasets linked: 1 (1 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
