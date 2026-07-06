# Metrics — cum26-alzheimer-s-disease-drug-development-pipeline

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 10 · Experiments: 8 · DOI: 10.1002/trc2.70251

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (26/26 links)
- Environment completeness: **0.857** (6/7 fields)
- Spec-completeness (setup proxy): 0.031
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **0.857** (24/28 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported': 10}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.0** (0 complete dead-ends)
- Decision branching factor: 3
- Explicit-vs-inferred ratio: 1.0
- Failure-knowledge preservation: 0.0
- Negative-result share: 0.0
- Node types: {'question': 1, 'decision': 1, 'experiment': 8}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 7, 'extends': 2, 'refutes': 0, 'bounds': 1, 'baseline': 0}
- Corrective-science score: **4**
- Concepts defined: 9 · related-work blocks: 10

## D6 Real-world grounding & translation
- Clinical trials linked: **8** (verified NCTs: ['NCT05026866', 'NCT03887455', 'NCT04468659', 'NCT05463731', 'NCT04777396', 'NCT05531526', 'NCT06709014', 'NCT05564169'])
- Datasets linked: 3 (2 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
