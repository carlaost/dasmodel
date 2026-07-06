# Metrics — woj25-immunoassay-detection-of-multiphosphorylated-tau-proteoforms

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 8 · Experiments: 7 · DOI: 10.1038/s41467-024-54878-8

## D1 Reproducibility
- Cross-layer binding resolvability: **0.974** (37/38 links)
- Environment completeness: **0.429** (3/7 fields)
- Spec-completeness (setup proxy): 0.0
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.0** (0/35 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 8}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.0** (0 complete dead-ends)
- Decision branching factor: 0
- Explicit-vs-inferred ratio: 1.0
- Failure-knowledge preservation: 0.077
- Negative-result share: 0.0
- Node types: {'question': 1, 'decision': 3, 'experiment': 8, 'dead_end': 1}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 6, 'extends': 0, 'refutes': 0, 'bounds': 1, 'baseline': 1}
- Corrective-science score: **2**
- Concepts defined: 12 · related-work blocks: 8

## D6 Real-world grounding & translation
- Clinical trials linked: **0** (verified NCTs: [])
- Datasets linked: 2 (2 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
