# Metrics — the25-blood-phosphorylated-tau-for-the-diagnosis

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 7 · Experiments: 4 · DOI: 10.1016/S1474-4422(25)00227-3

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (26/26 links)
- Environment completeness: **1.0** (7/7 fields)
- Spec-completeness (setup proxy): 0.125
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **1.0** (89/89 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 6, 'hypothesis': 1}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.143** (1 complete dead-ends)
- Decision branching factor: 2
- Explicit-vs-inferred ratio: 0.818
- Failure-knowledge preservation: 0.182
- Negative-result share: 0.125
- Node types: {'question': 1, 'decision': 4, 'experiment': 4, 'dead_end': 1, 'pivot': 1}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 4, 'extends': 0, 'refutes': 0, 'bounds': 1, 'baseline': 0}
- Corrective-science score: **2**
- Concepts defined: 9 · related-work blocks: 5

## D6 Real-world grounding & translation
- Clinical trials linked: **0** (verified NCTs: [])
- Datasets linked: 0 (0 verified) · code repos: 0
- PDF: OA=True, downloaded=False

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
