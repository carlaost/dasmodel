# Research program map — what's mine, what's substrate

Working doc. This is the canonical separation between (A) the ARA data shapes and validation machinery — an adopted substrate, not my work — and (B) my own incentive-design program, which uses A as one testbed and explicitly does not marry it. Both applications draw on this doc; keep it the single source of truth so the two applications never drift into claiming the wrong thing.

## The program in one paragraph

Citations are a Goodharted proxy for scientific quality: they reward citable work (reviews, positive results) and structurally cannot see negative results, replications, refutations, or reuse. My program asks whether **structure-derived signals over machine-readable research records** can measure — and therefore let funders reward — what citations cannot. The medium is instrumental: I adopted ARA (Liu et al., 2026) as the best available structured record to stress-test the thesis, and the honest headline result so far is that **metrics computed over a record's own structure measure the fidelity of the record, not the quality of the science** — real signal appeared only at the claim level, anchored to external ground truth (trial registries, prior literature). That finding is not a setback for the program; it is its sharpest output to date, and it drives the next move: if the current media cannot carry the signal, design the medium that can. Medium and metric have to be co-designed.

---

## Part A — Substrate (adopted, not mine)

The ARA (Agent-Native Research Artifact) protocol is due to Jiachen Liu et al. (2026, arXiv:2604.24658v3). I use it; I did not design it, and my program is deliberately not committed to it. What I adopted:

- **The four-layer artifact format**: cognitive layer (`logic/` — problem, claims, concepts, experiments, related work, solution), physical layer (`src/`), exploration graph (`trace/exploration_tree.yaml`), evidence layer (`evidence/`).
- **The 11 data shapes** — the measurable surfaces of an artifact (manifest, claims, concepts, problem, experiments, related work, solution, exploration tree, evidence, implementation, dataset descriptors), with field-level schemas (claim status vocabulary, falsification criteria, typed related-work links: imports / bounds / baseline / extends / refutes).
- **Seal Level 1** — deterministic structural validation (file/field gates, cross-layer binding, citation verification against sources).
- **Seal Level 2** — semantic rigor review scoring six dimensions 1–5: evidence relevance, falsifiability quality, scope calibration, argument coherence, exploration integrity, methodological rigor; mapped to accept/reject grades.

What A gives the program: a corpus. An Alzheimer's-focused library (~140 papers, ~60 compiled artifacts — [verify exact counts]) whose structure is rich enough to compute candidate indicators over.

What A does not give: any claim about scientific quality. The seal validates that a record is well-formed and internally honest. That is the floor my work starts from, not the thing I'm building.

## Part B — My contribution (the incentive-design program)

1. **The seven metric directions** (`metrics-directions.md`): (1) reproducibility & specification completeness; (2) claim & evidence integrity; (3) process transparency & negative knowledge — dead-end density, failure-knowledge preservation, negative-result share; (4) novelty & dependency structure, including a corrective-science score weighting refutations above imports; (5) ★ the **cross-library claim graph** — a knowledge graph whose edges are evidential (corroboration, contradiction, replication depth, knowledge reuse) rather than social, as a genuine alternative to the citation network; (6) real-world grounding (registries, ChEMBL, datasets); (7) representation quality as trust-weighting. Governing thesis: **reward what citations punish** — and defend against Goodhart through diversity of independent signals, not one number.

2. **The indicator ledger**: 64 candidate indicators (M01–M64) drafted per artifact surface, harvested to 23 survivors and a top-10 that deliberately reaches *outside* the record — external-literature novelty (M17), claim-drift vs cited sources (M18), claim↔experiment↔evidence entailment plus publication-bias (M19), end-to-end reproducibility bundles (M48), latent-space anchoring (M64), and so on.

3. **The tournament protocol as method**: blind, adversarial 4→2→1 metric selection (four independent proposers, judge-selected finalists, critique-driven revision rounds), run twice — once over the 11 artifact surfaces (~55 winning metrics), once over the top-10 indicators (three refine cycles each). The protocol exists so metrics can't be gamed by their own proposers; it is itself a small piece of incentive design.

4. **The negative finding** (`research/metrics/v3/FINDINGS.md`): after multiple adversarial cycles, structural metrics measure compiler fidelity, not science quality — "a well-compiled record of bad science and a well-compiled record of good science are indistinguishable." Zero of six paper-level rankers survived. Genuine signal appeared only claim-level with external anchors: claims concordant with registered trial endpoints, priority over-claims caught against prior literature, one compiler polarity inversion caught.

5. **The calibration gap** (`NOVELTY_INDICATORS_COMPARISON.md`): positioning against the Metascience Novelty Indicators Challenge / LENS — external benchmarks measure "is the science novel," the seal measures "is the argument sound," my tournament metrics measure "is the record faithful"; none is calibrated against the others. Calibration is identified, honestly, as the absent layer.

6. **The affordance-gap critique** (`research/metrics/v3/tournament/AFFORDANCE_GAP.md`) — the systematic version of the data-shape critique, and the bridge from B to C. Its thesis: "most of our ideal metrics are blocked not because the information is missing from the ARA, but because it is stored in a shape only an LLM can re-extract — which defeats the determinism the whole tournament was built to prize." It classifies every blocked ideal metric three ways: **Class A — format-recoverable** (the fact exists but is prose; emit it typed and the metric becomes a deterministic join: numeric reconciliation, claim typing, genre-conditioned absence), **Class B — anchor-dependent** (needs an external resolver; the format's job is to guarantee resolvable IDs: normalized references, registrations linked to claims), **Class C — irreducibly semantic** (novelty, entailment quality, assumption realism — a judge plus calibration set, forever; the format can only feed the judge cleaner inputs). It ends with a concrete successor-substrate spec: seven typed-sidecar additions (quantity ledger, `claim_type` enum, concept ontology xrefs, normalized `refs.yaml`, structured provenance, genre/warranted manifest, external-anchor + claim→registered-outcome links) plus two honest design tensions (typed fields invite fabrication — every field needs a first-class `not_specified` scored equal to honest absence; prose/sidecar duplication creates a new consistency obligation that doubles as an anti-fabrication signal). Closing line, quotable: "ARA doesn't lack the knowledge; it lacks the *shape*."

7. **The successor-format specification** (`research/metrics/v3/tournament/IDEAL_FORMAT_SPEC.md`; design log `TOURNAMENT_DESIGNS.md`; adversarial-pass record `TAIL_SYNTHESIS_LOG.md`) — the affordance gap's endpoint, and the clearest evidence that the tournament protocol (B.3) scales from *selecting metrics* to *designing a whole substrate*. Each of the affordance gap's twelve blocked-metric classes was run through its own four-proposer → judge → refine tournament; the twelve winning designs were merged into one spec and then put through an adversarial red-team pass that forced every over-claim down to an explicit limitation. The result — the **Grounded Research Object (GRO)**, deliberately a clean-sheet design and *not* an ARA-by-inheritance successor — organises everything a record must carry into three rigor tiers: **deterministic** (facts the format makes computable by structural join), **reliable-anchored** (facts resolved against external registries/indices), and **reproducible-judged** (novelty, entailment, realism — a calibrated judge, with the format only feeding it cleaner, pinned inputs) — and rolls them into a funder-facing credibility dossier that never collapses to a single number. It is a specification, adversarially hardened but empirically **unvalidated**: it has not been shown to discriminate good science from bad; its judged tier does not scale to a whole corpus (only triage-plus-audit-sample); and its anti-gaming guarantees rest on an independence between checkers the spec itself concedes is *asserted, not measured* (genuine decorrelation is earned at exactly one non-LLM checkpoint). Those three gaps are the honest bridge to the build (Astera) and the study (SPRU) — they are the work to be improved upon, not hidden.

## Part C — The medium question (the substrate critique IS part of the work)

My relationship to ARA is not just "user of a substrate": running the metrics program over ARA is a deliberate, systematic **critique of ARA's data shapes** — the demo doubles as a stress test of the format. The finding is now documented, not just emerging (`AFFORDANCE_GAP.md`, Part B.6): a large share of the "we can't build this" indicator list is a format problem masquerading as a feasibility problem — computable facts written as prose ("structure-in-prose": identifiers in markdown bullets, numbers hand-retyped in four places, citations as author-year strings). The negative finding in Part B.4 cuts both ways — either structure-derived quality metrics are impossible, or the current shapes are too poorly scoped to carry the signal — and the affordance-gap analysis resolves the ambiguity: Class-A gaps are recoverable by format design, Class-B by anchor discipline, and only Class-C is the true ceiling. Creating that better-scoped substrate is therefore part of the contribution, not a fallback: ARA is the instrument being critiqued; the particle layer (see Astera draft) starts from the successor-substrate spec the critique produced — since developed, by running the affordance gap's twelve blocked-metric classes back through the same adversarial tournament, into a complete stress-tested specification (the Grounded Research Object, `tournament/IDEAL_FORMAT_SPEC.md`, Part B.7). If metrics need more fertile ground, build the ground — but note the spec is a design artifact to validate and prune, not a finished system.

---

## Evidence pointers (repo)

| Claim | Where |
|---|---|
| Seven directions + "reward what citations punish" | `metrics-directions.md` |
| Adversarial self-critique | `metrics-critique.md` |
| 11 data shapes | `research/metrics/v3/tournament/DATA_SHAPES.md` |
| Merged metrics reference (Parts A–E) | `research/metrics/v3/tournament/ALL_METRICS_MERGED.md` |
| Indicator ledger 64→23→10 | `research/metrics/v3/tournament2/METRICS_CANDIDATES.md` |
| Tournament protocols | `tournament/TOURNAMENT_LOG.md`, `tournament2/TOURNAMENT2_LOG.md` |
| Negative finding + claim-level signal | `research/metrics/v3/FINDINGS.md` |
| Affordance-gap critique (three-class taxonomy) | `research/metrics/v3/tournament/AFFORDANCE_GAP.md` |
| Successor-format spec (GRO) + design log + adversarial pass | `tournament/IDEAL_FORMAT_SPEC.md`, `tournament/TOURNAMENT_DESIGNS.md`, `tournament/TAIL_SYNTHESIS_LOG.md` |
| LENS / novelty-benchmark comparison | `research/metrics/v3/tournament/NOVELTY_INDICATORS_COMPARISON.md` |
| Essays (public framing) | `research/sources/substack/papers-block-scientific-progress.md`, `alien-proteins.md` |

## How the two applications draw on this

- **Astera** (build): Parts B+C as the project — ship the medium (particle layer, now specified as the GRO successor-format spec, Part B.7) and the metrics prototype as open public goods; Parts B.4 and B.7's honest-limitations section are the "share what didn't work" exhibits.
- **Sussex SPRU** (study): Parts B+C as the research questions — what can structure-derived indicators measure, where do they Goodhart, what evaluation designs could funders responsibly deploy; Part A is just the instrument of study.
