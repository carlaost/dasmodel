# Metrics — che26-diagnostic-performance-of-plasma-p-tau217

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 8 · Experiments: 6 · DOI: 10.3389/fnagi.2026.1834591

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (26/26 links)
- Environment completeness: **1.0** (7/7 fields)
- Spec-completeness (setup proxy): 0.0
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.921** (35/38 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 8}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.25** (2 complete dead-ends)
- Decision branching factor: 1.75
- Explicit-vs-inferred ratio: 0.929
- Failure-knowledge preservation: 0.214
- Negative-result share: 0.2
- Node types: {'question': 1, 'decision': 4, 'experiment': 6, 'dead_end': 2, 'pivot': 1}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 14, 'extends': 1, 'refutes': 0, 'bounds': 1, 'baseline': 0}
- Corrective-science score: **3**
- Concepts defined: 13 · related-work blocks: 16

## D6 Real-world grounding & translation
- Clinical trials linked: **0** (verified NCTs: [])
- Datasets linked: 2 (2 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
