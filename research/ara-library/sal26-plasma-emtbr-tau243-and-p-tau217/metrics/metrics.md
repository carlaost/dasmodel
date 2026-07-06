# Metrics — sal26-plasma-emtbr-tau243-and-p-tau217

Extra ARA layer computed by `research/metrics/compute_metrics.py`. `[det]` = computed exactly;
`pending_*` = needs an LLM judge / sandbox run / external DB (not fabricated).

- Claims: 4 · Experiments: 4 · DOI: 10.1001/jamaneurol.2026.1405

## D1 Reproducibility
- Cross-layer binding resolvability: **0.933** (14/15 links)
- Environment completeness: **1.0** (7/7 fields)
- Spec-completeness (setup proxy): 0.25
- Executable reproduction (L3): pending_exec (has code repo: False)

## D2 Claim & evidence integrity
- Claim-grounding ratio: **1.0** (2/2 numbers)
- Falsifiability presence: 1.0
- Status mix: {'supported (per abstract; effect sizes not available from provided input)': 3, 'hypothesis (interpretive "meaning" statement; not directly tested in the abstract\'s': 1}
- Orphan claims (no proof): []
- Orphan experiments (no claim): []

## D3 Process transparency & negative knowledge
- Dead-end density / claim: **0.25** (1 complete dead-ends)
- Decision branching factor: 2
- Explicit-vs-inferred ratio: 0.667
- Failure-knowledge preservation: 0.222
- Negative-result share: 0.2
- Node types: {'question': 1, 'decision': 2, 'experiment': 4, 'dead_end': 1, 'pivot': 1}

## D4 Novelty & dependency structure
- Typed-delta profile: {'imports': 3, 'extends': 0, 'refutes': 0, 'bounds': 0, 'baseline': 0}
- Corrective-science score: **0**
- Concepts defined: 7 · related-work blocks: 3

## D6 Real-world grounding & translation
- Clinical trials linked: **1** (verified NCTs: ['NCT03174938'])
- Datasets linked: 2 (2 verified) · code repos: 0
- PDF: OA=True, downloaded=False

## D7 Artifact quality (meta)
- Seal L1 structural: **1.0** (10/10 core files)
- Auditor blind-spot (orphan experiments): []
