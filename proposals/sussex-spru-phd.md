# Sussex SPRU PhD — Research Proposal Draft

Working draft for the SPRU PhD (Science and Technology Policy Studies pathway). Sussex asks for a research proposal with the application; typical social-science length is ~2,000–3,000 words — [verify the current word limit and whether you're applying to the integrated PhD (MSc + PhD, ~4 yrs) or the straight PhD given your professional experience]. Placeholders in [brackets]. See `00-research-program-map.md` for the evidence base and the ARA-vs-own-work separation.

---

## Title (pick one, or blend)

1. **Rewarding what citations cannot see: indicator design for machine-readable research records**
2. Medium and measure: co-designing scientific knowledge representations and the incentives built on them
3. Beyond the Goodharted citation: structure-derived research indicators and their limits

## Abstract (~150 words)

Research assessment still runs on citation-derived indicators despite two decades of documented dysfunction: citations reward citable outputs and are structurally blind to negative results, replications, refutations, and reuse. Meanwhile the scientific record itself is changing — AI agents increasingly read, reproduce, and extend research, and machine-readable structured records (typed claims, evidence links, exploration traces) are emerging as a publication layer. This project asks whether **indicators derived from the structure of such records** can measure what citations cannot, and what responsible evaluation designs could be built on them. It builds on my prior empirical work — an adversarially validated indicator study over a ~140-paper structured corpus whose central finding is cautionary: structural indicators measure record fidelity, not science quality, unless anchored to external ground truth. The PhD develops this into a theory and empirical test of **medium–metric co-design**: what a research record must capture for quality signals to be measurable, Goodhart-resistant, and fit for use by funders.

## Background and rationale

Two literatures motivate the project and neither currently talks to the other.

**Research evaluation and responsible metrics.** The critique of citation-based assessment is mature: DORA (2013), the Leiden Manifesto (Hicks et al., 2015), and The Metric Tide (Wilsdon et al., 2015) — the last a SPRU-rooted contribution — established that indicator misuse distorts research behaviour, and CoARA (2022) is institutionalising reform. But the reform agenda is largely *subtractive* (use fewer numbers, more narrative); it has few *constructive* proposals for indicators that measure the things everyone agrees are undervalued: negative results, replication, data/method reuse, corrective work. Goodhart's law is the standing objection to any new indicator, usually asserted rather than empirically tested.

**Machine-readable research records.** A parallel engineering literature is rebuilding the research object: FAIR data, nanopublications, RO-Crate, and most recently agent-native formats such as ARA (Liu et al., 2026) that bind claims, evidence, code, and exploration traces into typed, validated structures. These formats create, for the first time, artifact surfaces over which non-citation indicators could actually be computed — dead-end density, claim–evidence entailment, typed dependency deltas (imports/extends/refutes), replication depth, external-registry concordance. The UK's Metascience Unit (DSIT/UKRI) and initiatives like the Metascience Novelty Indicators Challenge show funders actively procuring exactly such next-generation indicators — currently without a theory of what the underlying record must contain for the indicators to be valid.

The gap this PhD occupies: **indicator design and record design are treated as separate problems, and they are not.** My preliminary work (below) provides direct empirical evidence: over a richly structured corpus, every indicator computed from the record's internal structure collapsed into a measure of how well the record was compiled, not how good the science was; signal recoverable only via external anchors. The measurable is determined by the medium. Evaluation reform that ignores the record format will keep producing gameable proxies; record formats designed without evaluation in mind will keep failing to carry the signals funders need.

## Research questions

**RQ1 (measurement).** What can indicators derived from the structure of machine-readable research records measure that citation-based indicators cannot — specifically negative knowledge (dead ends, refutations), replication and reuse, and claim-level corroboration/contradiction — and with what validity against external ground truth (trial registries, prior literature, expert judgment)?

**RQ2 (limits).** Where and how do such indicators fail? Under what conditions do they collapse into record-fidelity measures (my preliminary finding), and how do they behave under adversarial optimisation — i.e., an empirical Goodhart test rather than an asserted one?

**RQ3 (record design).** What must a research record capture *natively* — at authoring time — for the RQ1 signals to be computable and hard to fake? This treats the medium as a design variable and is already grounded: my preliminary work doubles as a systematic critique of ARA's data shapes, and its running finding is that the ideal indicators need better-scoped shapes than any existing format provides. Part of the contribution is converting each indicator failure into a formal shape requirement any successor substrate must meet — a conversion I have already run once end-to-end, producing the Grounded Research Object specification; the PhD's task is to test whether its predicted rigor-tier boundaries (format-recoverable vs. anchor-dependent vs. irreducibly semantic) actually hold, rather than to invent the design from scratch.

**RQ4 (evaluation design and use).** What evaluation arrangements could funders and institutions responsibly build on such indicators — consistent with the responsible-metrics principles (contextual, humble, plural) — and how do evaluators and researchers themselves judge their legitimacy? [This is the most SPRU-native question; develop with supervisor.]

## Preliminary work

I enter with an unusual empirical base (documented, sharable):

- A structured corpus: ~140 Alzheimer's-domain papers, ~60 compiled into the ARA format with validated claims, evidence links, and exploration traces [verify counts].
- An indicator programme: seven design directions organised around the thesis "reward what citations punish"; 64 candidate indicators refined to a top 10 via blind adversarial tournaments (independent proposers, judged finalists, critique-driven revision) — a validation protocol designed so indicators cannot be gamed by their own authors.
- A central negative result: structural indicators measured compilation fidelity, not science quality; genuine signal appeared only at claim level with external anchoring (registered-trial endpoint concordance; priority claims checked against prior literature).
- A calibration analysis positioning this against the Metascience Novelty Indicators Challenge (LENS) benchmark.
- An affordance-gap critique of the ARA format itself: a systematic audit of every blocked ideal indicator against the data shape that blocks it, yielding a three-class taxonomy — format-recoverable (fact present but stored as prose; typed emission restores deterministic computation), anchor-dependent (needs resolvable external identifiers so registries/literature indices can be joined), and irreducibly semantic (needs a calibrated judge regardless of format) — plus a seven-element specification for a successor record format. This taxonomy is the seed of the medium–metric co-design theory (RQ3/WP3): it separates, empirically, what evaluation reform can get from better record design versus what will always require judgment and calibration.
- A worked successor-format specification (the Grounded Research Object): the seven-element sketch developed — by running the twelve blocked-metric classes through the same adversarial tournament, then an adversarial red-team pass — into a full record design that sorts every quality signal into three rigor tiers (deterministically checkable, externally anchored, calibration-judged) and a funder-facing dossier. It is the concrete object RQ3/WP3 can test rather than a schema I must first invent; and its own red-team surfaced the sharpest questions this PhD formalises: that such a format **relocates** trust (from the author's prose onto a human calibration set and an *assumed* independence between automated judges) rather than eliminating it; that its importance-measuring tier does not scale to a whole corpus; and that "independence" between checkers is, throughout, asserted rather than measured. Those are RQ2 (limits/Goodhart) and RQ4 (legitimacy) stated as testable propositions, not slogans.

The PhD turns this practitioner prototype into defensible research: proper validity testing, human calibration, theoretical grounding in the evaluation literature, and the qualitative work with evaluators the prototype entirely lacks.

## Methodology

Mixed methods across four workpackages, mapped to RQ1–4:

- **WP1 — Systematic indicator validation (yr 1–2).** Extend the corpus [second domain for contrast — verify feasibility]; compute the surviving indicators; validate against external ground truth: registry concordance, retraction/correction records, post-publication outcomes, and expert ratings on a sample. Quantitative; scientometrics methods.
- **WP2 — Adversarial Goodhart experiments (yr 2).** Red-team studies: task agents (and, where ethical, humans) with maximising each indicator on synthetic/modified records; measure divergence between indicator score and blinded quality judgment. To my knowledge the first systematic empirical Goodhart test of structural research indicators. This WP also tests the successor format's central anti-gaming assumption directly: the GRO spec defends fabrication with a second, "independent" automated checker, but concedes that independence is asserted, not measured — WP2 measures it (do two nominally-independent LLM judges actually fail independently, or do shared training priors let a single adversarial edit fool both?).
- **WP3 — Record-design requirements (yr 2–3).** From WP1/WP2 failures, derive and formalise what native capture must include — starting from my existing Grounded Research Object specification (typed quantity ledger, claim logical form, normalized resolvable references, typed cross-layer graph, declarable absence, the deterministic/anchored/judged tier split) rather than a blank page; instantiate as a minimal reference schema and test whether re-authored records recover the lost signal, and whether the predicted class boundaries (format-recoverable vs. anchor-dependent vs. irreducibly semantic) hold under WP2's adversarial pressure. Design-science method.
- **WP4 — Evaluator study (yr 3).** Semi-structured interviews / workshops with funders and assessment reformers ([UKRI Metascience Unit, Wellcome, CoARA members — develop access via SPRU networks]) on legitimacy, usability, and failure modes of structure-derived indicators in real allocation decisions. Qualitative; STS/evaluation-studies framing.

Ethics: WP4 human-subjects protocols; WP2 agent red-teaming is low-risk but pre-registered.

## Why SPRU

This project needs a home where research evaluation is a first-class research object, not a service function. SPRU is where The Metric Tide tradition lives, hosts active metascience expertise ([Paul Nightingale — metascience, management of uncertainty; Daniele Rotolo — scientometrics and emerging-technology indicators; verify current availability and add 1–2 more]), and connects to the Research on Research Institute network. The project is issue-focused and interdisciplinary in exactly SPRU's registered sense: it spans scientometrics, STS, information systems design, and science funding policy, and its findings are directly consumable by the UK metascience policy apparatus. Conversely I bring SPRU something scarce: a practitioner's corpus and tooling already built, plus direct industry/funder networks (DeSci Labs, ARIA-project interviews, funder conversations) that make WP4 access realistic.

## Contribution

1. First adversarially validated empirical study of what structural indicators over machine-native research records can and cannot measure (RQ1–2).
2. A theory of medium–metric co-design: record-format requirements derived from indicator validity, bridging the evaluation-reform and research-object literatures (RQ3) — with a worked, adversarially-stress-tested exemplar (the Grounded Research Object spec) to test and critique rather than a purely abstract proposal.
3. Policy-usable guidance for funders on next-generation indicators, grounded in evaluator legitimacy evidence (RQ4).
4. Open artifacts throughout: corpus, indicator code, protocols — including negative results as first-class outputs, practising what the project preaches.

## Timeline (3-yr PhD registration; prepend MSc year if integrated route)

Yr 1: literature + theory; corpus extension; WP1. Yr 2: WP2; WP3 begins; first paper (indicator validity). Yr 3: WP3 completes; WP4; second paper (Goodhart experiments) + policy brief; write-up.

## References

[To compile: DORA 2013; Hicks et al. 2015 Leiden Manifesto; Wilsdon et al. 2015 Metric Tide; CoARA 2022; Goodhart/Campbell sources; Liu et al. 2026 ARA; nanopublications (Groth/Mons); RO-Crate; FAIR; Metascience Novelty Indicators Challenge/LENS docs; James Evans lab on novelty measures; Rafols & Rotolo on indicator diversity; add supervisor's own relevant work once identified. Own preliminary artifacts (link when public): affordance-gap critique `AFFORDANCE_GAP.md`; Grounded Research Object spec `IDEAL_FORMAT_SPEC.md`; negative-result report `FINDINGS.md`.]

---

## Pre-submission checklist

- [ ] Identify and email prospective supervisor(s) *before* submitting — Sussex effectively expects pre-contact; Nightingale and Rotolo are the leads to verify [confirm they take students 2026/27; Josie Coburn appears to have left SPRU — do not name without checking].
- [ ] Confirm route: integrated PhD (MSc + PhD) vs straight PhD given professional experience; affects timeline section.
- [ ] Confirm proposal word limit and required structure from the current application portal.
- [ ] Funding: check SEDarc (ESRC DTP) 2026/27 deadlines and any live SPRU studentships; note ESRC funding usually requires the proposal to foreground social-science methods — WP4 helps here.
- [ ] Verify corpus counts and decide how much of the repo work is public/sharable at application time.
- [ ] Align story with Astera application if both proceed (see `astera-residency.md` checklist — residency is Emeryville-based; PhD is Brighton; sequencing or part-time arrangements need a decision before interviews).
