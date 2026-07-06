# Metrics — pal25-alzheimer-s-association-clinical-practice-guideline

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 8 · Experiments: 6 · DOI: 10.1002/alz.70535

## D1 Reproducibility
- Cross-layer binding resolvability: **1.0** (24/24 links)
- Environment completeness: **0.429** (3/7 fields)
- Spec-completeness (setup proxy): 0.0
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **1.0** (24/24 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported (as a conditional, low-certainty recommendation)': 2, 'supported': 6}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.0** (0 complete dead-ends)
- Decision branching factor: None
- Explicit-vs-inferred ratio: 0.0
- Failure-knowledge preservation: 0.0
- Negative-result share: 0.0
- Node types: {}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 6, 'extends': 2, 'refutes': 0, 'bounds': 2, 'baseline': 1}
- Corrective-science score: **6**
- Concepts defined: 10 · related-work blocks: 11

## D6 Real-world grounding & translation
- Clinical trials linked: **0** (verified NCTs: [])
- Datasets linked: 0 (0 verified) · code repos: 0
- PDF: OA=True, downloaded=True

## D7 Artifact quality (meta)
- Seal L1 structural: **0.8** (8/10 core files)
- Auditor blind-spot (orphan experiments): []
