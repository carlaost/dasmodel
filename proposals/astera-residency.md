# Astera Residency — Application Draft (v2)

Working draft, revised from v1. Built around Astera's four published criteria (Fit / Useful / Open-First / People-Project Fit). Placeholders in [brackets]. Sentence case for a funder audience. See `00-research-program-map.md` for the ARA-vs-my-work separation this draft now respects, and "Edit notes" at the bottom for what changed from v1.

---

## Project

**The particle layer: a substrate for granular, agent-native scientific contribution — and the metrics layer that makes it worth adopting.**

A working schema, typed-link specification, and trace-to-particle compiler that lets scientific work be published as composable particles — claims, evidence, methods, data, code — instead of papers. Built and demonstrated on my own research corpus, validated with research groups whose incentives already favor openness, and capped with a contribution-metrics prototype co-designed with funders — a prototype I am not starting cold: I have already run a year of adversarial metrics experiments over structured research records, including an honest negative result that shapes this design.

This sits squarely in Astera's Open Science focus area, and it is infrastructure, not commentary: the deliverable is a thing people use, not an essay about what science should be.

## The problem

The paper is the wrong primary medium for science, and increasingly so as AI agents become the main consumers of the scientific record. A paper compresses a branching, iterative research process into a linear narrative, discarding failed paths, implementation detail, and most of what was actually learned. That was tolerable when every reader was human. It is not, now that agents read, reproduce, and extend published work — each of those tasks needs precisely what the paper throws away.

The fix is structural: decompose research into granular, typed, composable particles that humans read as on-demand narratives, agents operate on directly, and models anchor in latent space. The architecture is the tractable part. The hard part — the wall every prior effort has hit — is adoption, and it is owned by incentives, not technology.

## Why this is different now

I am not the first to propose granular publishing, and I have watched the category fail twice from the inside (see below). Two things have changed:

**The authoring burden is dissolving.** The thing that sank prior efforts was asking researchers to hand-assemble structured objects they had no reason to assemble. But agents now sit inside the actual research workflow — writing code, running analyses, drafting — and the trace they generate is the raw material for particles. Capture can be largely automated. The recent ARA work (Liu et al., 2026) demonstrates that even a lossy backfill from existing papers already improves what agents can do with the record; native capture only makes it richer.

**The consumer has changed.** Earlier efforts needed humans to adopt a new reading format before any value appeared. When the primary consumer is an agent, value accrues immediately and adoption doesn't have to clear the human-habit bar first.

This does not solve the incentive problem. It changes the cost side of the ledger enough to make the experiment worth running — which is exactly the early, high-unknown stage Astera funds.

## What I already know (evidence from my own experiments)

Over the past year I built a testbed to pressure-test the incentive half of this project before asking anyone to fund it: I compiled an Alzheimer's-focused corpus (~140 papers, ~60 structured artifacts — [verify counts]) into the ARA format, drafted 64 candidate contribution indicators over its data shapes, and ran them through blind adversarial tournaments (four independent proposers per metric, judge-selected finalists, critique-driven revision rounds) so no metric could be gamed by its own author.

The headline result is negative, and I consider it the most valuable thing the testbed produced: **metrics computed over a record's own structure measure the fidelity of the record, not the quality of the science.** A well-compiled record of bad science and a well-compiled record of good science were indistinguishable to every structural metric in the pool. Genuine signal appeared only at the claim level, anchored to external ground truth — claims checked against registered clinical-trial endpoints, priority claims checked against prior literature.

The follow-up analysis turned that negative result into a design specification. Auditing every blocked "ideal" metric against the format that blocked it showed that most were stopped not by missing information but by information stored in a shape only an LLM can re-extract — numbers hand-retyped as prose in four places instead of one typed value, citations as author-year strings instead of resolvable IDs, honest absence indistinguishable from lazy omission. Each blocked metric falls into one of three classes: **format-recoverable** (emit the same fact typed and the metric becomes a deterministic join), **anchor-dependent** (the format must guarantee resolvable external IDs so registries and literature indices can be joined against), and **irreducibly semantic** (novelty, entailment quality — a calibrated judge, forever; the format's job is only to feed it cleaner inputs). The first two classes are format problems masquerading as feasibility problems. In one line: the current substrate doesn't lack the knowledge; it lacks the shape.

This is exactly the "share what did not work" that Astera's Open Science policy asks for, and it directly shapes the build. The critique produced a concrete starting specification for the particle schema — a thin typed layer alongside the prose: a canonical quantity ledger, typed claims, concept-to-ontology anchors, a normalized reference table, structured provenance, a genre manifest that makes honest absence declarable, and claim-to-registry links. It also produced the honest design tensions the schema must hold (typed fields invite fabrication, so every field needs a first-class "not specified" scored equal to honest absence). I then put that sketch through the same adversarial tournament I use for metrics — twelve format gaps, four independent proposers each, judge-selected finalists, then a red-team critique pass that forced every over-claim down to a stated limitation — and it produced a complete successor-format specification: the Grounded Research Object, a record whose unit carries its own credibility evidence across three rigor tiers (deterministically checkable, externally anchored, and calibration-judged), rolled into a funder-facing dossier that never collapses to one number. The medium and the metrics have to be co-designed; that co-design is this project, and it starts not from a blank page but from a written, stress-tested spec. I am careful about what that spec is and isn't: it is a design artifact to validate and prune, not a finished system — it has not yet been shown to separate good science from bad, its judged tier does not scale to a whole corpus, and its anti-gaming rests on an independence between checkers I can assert but not yet measure. Closing those three gaps is the build.

## What I'll build (the public goods)

1. An **open particle schema + typed-link specification** — the standard others can build on.
2. A **trace-to-particle compiler** that turns research traces (agent sessions, repositories, papers) into particles, demonstrated first on my own corpus so it's real independent of any pilot.
3. An **honest field report** from 1–3 lightweight pilots: what got adopted, what didn't, where the authoring cost actually fell.
4. A **contribution-metrics prototype**, co-designed with funders, that credits work citations miss — replications, shared datasets, refutations, methods reused downstream — seeded from my existing indicator ledger and tournament results, and calibrated against external ground truth from day one (the lesson above).

All open by default, including what didn't work — which is itself the value the system is built to capture.

## 18-month plan

**WP0 — Early-adopter & corpus selection (mo 0–2).** Identify the sub-field whose researchers will actually publish this way. Psychiatry is the leading candidate — Oshima already tested there, so there's prior signal and a warm start — but adoption-fit is precisely what killed prior efforts, so I treat the choice as work to be validated, not assumed. This phase de-risks the whole project.

**A — Substrate (mo 1–7).** Schema, typed links, and compiler, bootstrapped on my own ARIA / omics / Oshima corpus so it ships regardless of what any external group decides. This no longer starts from a blank page: the design constraints are the Grounded Research Object spec the affordance-gap tournament produced — every load-bearing quantity exists once as a typed value referenced by ID everywhere else; every cited work and dataset resolves to an external identifier; claims carry types (and a checkable logical form) so evidence requirements are testable; a typed cross-layer graph makes claim↔evidence correspondence a structural join rather than a re-read; absence is declarable so honesty is distinguishable from omission; and deterministic, anchored, and judged facts are kept in physically separate layers so no self-certified number masquerades as a checked one. The residency work is implementing a minimal, buildable subset of that spec and discovering which parts survive contact with a real corpus — the spec is the hypothesis, not the deliverable.

**B — Pilots (mo 5–14).** 1–3 lightweight pilots with research groups I convene. Arcadia is a candidate site (in conversation). Study adoption honestly against pre-committed measures.

**C — Metrics (mo 10–18).** A metrics layer over the pilot particles, co-designed with funders so it measures what they would actually reward. Not from scratch: the seven metric directions, the 64→10 indicator ledger, the tournament validation protocol, and now a concrete target shape — the GRO spec's three rigor classes and its funder-facing credibility dossier — already exist; the residency work is porting the survivors onto native particles and running the validation the spec has not yet had. The single most important open test is discrimination: does any of this actually separate a well-done study from a poorly-done one, or (as my testbed found for record-internal metrics) does the signal live only in the externally-anchored tier? That is answered by calibrating against external ground truth (registries, prior-literature novelty baselines such as the Metascience Novelty Indicators Challenge / LENS), not by more design. This is also where the incentive wall gets tested — the real blocker, addressed directly rather than wished away.

Each phase produces a durable public good that stands even if the next phase underperforms.

## Fit with the existing landscape

The most relevant current effort is ARA (Agent-Native Research Artifacts; Liu et al., 2026), and my position is complementary, not competitive. I know ARA from the inside as its most demanding user: I adopted it as the substrate for my metrics testbed because it was the best structured record available, and ran what is in effect the first systematic critique of its data shapes from a metrics perspective — which is precisely what surfaced its limits (the shapes are not scoped for the indicators that matter; structure alone doesn't carry science-quality signal; native capture and external anchoring do). I'm building the layers ARA doesn't attempt — native authoring from live workflows, cross-project and cross-domain composition, and the contribution-metrics layer. I'm in active contact with the ARA team and routing adoption questions through them, since they hold the most recent data on where this breaks.

Prior efforts each solved one fragment and none bound logic + code + exploration + evidence with typed cross-layer links: FAIR standardizes data metadata but not the structure of the argument; nanopublications atomize claims but have no execution layer; RO-Crate bundles artifacts without decomposing them. DeSci built the full-stack research-object version — which I know intimately, having been its PM, and which taught me the core lesson below.

## Team

Me — the science model, schema design, pilot and funder relationships, and funder co-design. One technical hire — compiler engineering, infrastructure, and metrics tooling. I can and do build, but my differentiator is the conception, the network, and the earned judgment about why this category fails — so I want to do the irreplaceable part and hire for engineering support.

## Why me

I've worked inside this problem from several angles: I was an early hire at DeSci Labs (decentralized publishing and reproducibility infrastructure), worked with Undermind on LLM-based scientific search, built Oshima — which decomposed papers into claims, evidence, and methods. Alongside that I ran an interview series across ARIA-funded AI-scientist projects on knowledge representation, hosted a podcast on metascience with guests like James Evans who still shape my thinking. Most recently I designed and ran the metrics testbed described above — the only adversarially validated study I know of on what structure-derived indicators can and cannot measure over machine-native research records. [link the writeup when public]

The throughline: I have watched experimental publishing efforts break and I understand why. Oshima only ever read papers, with no native authoring and no incentive to switch; DeSci's "research object" turned out to be infeasible for scientists to assemble — a compiled paper-plus-data-plus-code that researchers resisted because their code and data felt exposed and nothing rewarded the extra work. In both cases the failure was incentives and authoring burden, not the technology. This project is designed around that knowledge, not in ignorance of it. I'm also already connected to the efforts and people any solution has to engage — ARA, and the funders whose incentives would need to move (in conversation with NADI; [validate Onno before naming]).

## What I don't know yet

Adoption is the open question, and I won't pretend otherwise. I don't yet know which field's researchers are the real early adopters, or whether funder co-design can shift incentives at a meaningful scale. Those are not protocol problems and a better spec won't solve them. The measurement side is genuinely open too: my successor-format spec is adversarially hardened but unvalidated — I do not yet know whether its metrics discriminate good science from bad, its calibration-judged tier is honestly acknowledged not to scale to a whole corpus, and its anti-gaming guarantees rest on an independence between automated checkers I can currently only assert. These are exactly the high-unknown, build-to-learn questions this residency exists to fund — and the reason the plan front-loads adoption scouting, treats the spec as a hypothesis to test rather than a system to ship, and ends with funders in the room.

---

## Pre-submission checklist

- [ ] Validate Onno / NADI before naming as co-design partner; otherwise soften to "in conversation with a funder."
- [ ] Confirm Arcadia framing is "candidate, in conversation" — not a promised pilot.
- [ ] Decide relocation to Emeryville (in-person hub, 12–18 mo) and state it plainly if asked.
- [ ] Pull the real template and remap sections; trim to any length limit.
- [ ] Replace remaining brackets; add links (Oshima, ARA paper, your two Substack posts).
- [ ] Verify corpus counts (~140 papers / ~60 compiled artifacts) before citing.
- [ ] Decide whether/where the metrics testbed writeup will be public before submission — a public negative-result report is a strong Astera exhibit.
- [ ] If also pursuing the Sussex PhD: decide sequencing/compatibility before either interview (see `sussex-spru-phd.md`).

## Edit notes (v1 → v2)

- Added "What I already know" — v1's biggest gap. You have a year of empirical results, including a publishable negative finding that is tailor-made for Astera's "share what did not work" criterion; v1 mentioned none of it and treated the metrics WP as pure future work.
- Repositioned ARA per your instruction (updated per your follow-up): you're not an ARA builder — you're running the first systematic *critique* of ARA's data shapes via the metrics testbed, and the shape requirements it produces are the starting spec for the particle layer (medium–metric co-design).
- WP A and WP C now carry design constraints from the metrics results instead of starting cold.
- Fixed the garbled sentence in "Why me" ("turned out not to infeasible" → "turned out to be infeasible… to assemble").
- Added Liu et al. attribution for ARA, and LENS as the external calibration baseline.
- v2.1: folded in `research/metrics/v3/tournament/AFFORDANCE_GAP.md` — the three-class blocked-metric taxonomy, the "lacks the shape, not the knowledge" line, and the seven-sidecar successor spec now ground both "What I already know" and WP A.
- v2.2: upgraded the seven-sidecar sketch to the full successor-format spec it became — the Grounded Research Object (`tournament/IDEAL_FORMAT_SPEC.md`), produced by running the affordance gap's twelve blocked-metric classes back through the adversarial tournament + a red-team pass. It now grounds "What I already know," WP A (design constraints = the spec's three rigor tiers), and WP C (target shape = the credibility dossier). Framed strictly as her substrate-design thesis fed by the ARA critique — NOT as building ARA v2 (GRO is explicitly clean-sheet). Kept honest: the spec is unvalidated (discrimination untested), its judged tier doesn't scale, and checker-independence is asserted not measured — added to WP C and "What I don't know yet" as the work-to-improve, per the "exemplary outcomes and work to be improved upon" brief.
- Everything else — structure, voice, honest-uncertainty framing, checklist — kept from v1.
