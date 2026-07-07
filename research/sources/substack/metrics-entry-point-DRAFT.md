# Metrics Are the Way In

**working draft — companion to the layer-cake substrate post. this one argues metrics are the entry point to the whole thing, shows the tournaments and experiments that produced them, infers the data shapes they demand, says where existing efforts fall short, lists the ideal metrics, and ends with an ask to funders. figure notes in [brackets]; new sketches inline — redraw before publishing.**

---

i've written about a better *medium* for science — a layer cake of narrative, particles, and latent space. but if i had to pick the single lever that moves the whole system, it wouldn't be the medium. it would be the **metrics**.

here's why metrics are the way in, not a nice-to-have at the end.

**nothing changes until what *counts* changes.** researchers assemble papers not out of preference but because grants, jobs, and tenure are denominated in papers, and papers are scored by citations. every prior attempt at a better medium — nanopublications, research objects, my old project Oshima, DeSci where i was PM — died on the same rock: no incentive to do the extra work, because nothing rewarded it. you cannot out-*design* that. the incentive has to change at the source, and the source is what gets measured and rewarded.

**and metrics are also the diagnostic.** here's the part i didn't expect. when you actually try to build good metrics over the scientific record, you find out — precisely, painfully — what the record is missing. the metrics tell you what the substrate has to be. so metrics aren't just the reward that would make a new medium worth adopting; they're the *forcing function* that reveals what the medium must look like. that's the strongest sense in which they're the entry point: chase the metrics far enough and they hand you the spec for everything else.

which is what happened. this post is the metrics half of the story. the substrate half is the layer-cake post; this is where it came from.

## the thesis: reward what citations punish

citations are a Goodharted proxy. they reward *citable* work — reviews, positive results, broad confident narratives — and are structurally blind to the things everyone agrees are undervalued: negative results, replications, refutations, datasets, methods reused downstream. once the paper is the unit and the citation is the score, the rational move is to optimize for citability, not for discovery.

so the design goal is blunt: **reward what citations punish.** measure the corrective, cumulative, reusable labor that the citation graph can't see. and defend against the obvious objection — that any new metric gets gamed the moment it's a target — not with one clever number but with a *diversity of independent signals*, and with a process that stops a metric from being graded by whoever proposed it.

## how i built them: seven directions, sixty-four indicators, two tournaments

i didn't want a metric i liked. i wanted metrics that survive adversarial pressure. so the process was built to be hostile to its own outputs.

- **seven directions.** i started from seven families of good-science signal: (1) reproducibility & specification completeness; (2) claim & evidence integrity; (3) process transparency & negative knowledge — dead-end density, failure-knowledge preservation, negative-result share; (4) novelty & dependency structure, including a *corrective-science score* that weights refutations above imports; (5) the flagship — a **cross-library claim graph** whose edges are evidential (corroboration, contradiction, replication depth, reuse) rather than social, as a genuine alternative to the citation network; (6) real-world grounding (trial registries, chemical databases, datasets); (7) representation quality as a trust weight.
- **sixty-four candidate indicators.** i drafted 64 concrete indicators (one ledger, M01–M64) across every surface a structured record exposes — claims, concepts, problem, experiments, related work, methods, exploration trace, evidence, code, data — then pruned and merged to 23 survivors and a top 10.
- **two tournaments, blind and adversarial.** a metric can't be trusted if its author also grades it. so: **round one** ran a tournament over the eleven artifact surfaces — four clean-room proposers per surface (no sight of any existing metric), a meta-science judge picking the best two, critique-driven revision, a single winner (~88 agents in total). **round two** ran a `4 → 2 → 1` tournament per *metric* from the top-10 ledger — four independent proposers, judged finalists, three refine cycles each. **[FIG A — new; the 4→2→1 tournament: 4 blind proposers → judge picks 2 → refine → 1 winner. sketch below.]**

```
[FIG A — the metric tournament (per metric)]

  4 blind proposers ──► meta-science judge ──► 2 finalists ──► refine ×3 ──► 1 winner
  (no sight of existing   picks best 2 +                      (steal best,
   metrics or the         writes critiques                    address critique)
   verifier)
```

- **and then i ran the experiments.** not just designed metrics — *ran* them, over a real corpus (~140 Alzheimer's papers, ~60 compiled into a structured format), and measured what they actually did. that's where the story turns.

## what the experiments found (the negative result that reframed everything)

the headline is negative, and it's the most useful thing the whole exercise produced:

> **metrics computed over a record's own structure measure the fidelity of the record, not the quality of the science.**

a well-compiled record of bad science and a well-compiled record of good science were indistinguishable to every structural metric in the pool. zero of six paper-level rankers survived the validity check. genuine signal appeared *only* at the claim level, and only when it reached outside the record — claims checked against registered clinical-trial endpoints, priority claims checked against prior literature, one compiler polarity-inversion caught. (i also measured extractive fidelity against full text directly: ~92% faithful, and the failures were exactly the dense multi-cohort comparison papers where a transposed table flips a result.)

the lesson isn't "structural metrics are impossible." it's sharper: **the signal you want lives outside the record's own walls, and the record's *shape* determines whether you can reach it.** which is the question that produced the substrate.

## inferring the ideal data shapes — and where existing efforts fall short

so i asked, for every metric i wanted but couldn't build: *why not?* almost never because the information was missing. because it was stored in a shape only an LLM could re-extract — a number hand-retyped as prose in four places instead of one typed value, citations as author-year strings instead of resolvable IDs, honest absence indistinguishable from lazy omission. **the record doesn't lack the knowledge; it lacks the shape.**

every blocked metric sorts into one of three classes, and each tells the substrate what to emit:

- **format-recoverable** — the fact is there as prose; emit it *typed* and the metric becomes a deterministic join (numeric reconciliation, claim typing, genre-conditioned absence).
- **anchor-dependent** — the fact points outside the record; the format must guarantee *resolvable external IDs* (DOIs, registrations, accessions) so registries and literature indices can be joined against.
- **irreducibly semantic** — novelty, entailment quality, assumption realism; no format change makes these deterministic. a calibrated judge, forever. the format's only job is to feed the judge cleaner, pinned inputs.

that taxonomy is what the layer-cake post builds on. here it's the diagnostic that shows where today's efforts stop short — and there are three of them, each measuring a *different axis*, none calibrated against the others: **[FIG B — new; three orthogonal axes, no calibration between them. sketch below.]**

```
[FIG B — three efforts, three axes, no shared ground truth]

  CITATIONS          →  social attention (Goodharted; blind to negatives,
                        replications, reuse, refutations)
  ARA-style SEAL     →  internal INTEGRITY: is the argument sound, coherent,
                        falsifiable? one LLM grade, no external anchor,
                        never asks "is it novel / does it matter"
  LENS / Novelty     →  NOVELTY: externally calibrated to expert ratings —
  Challenge             but only novelty, and it reads whole papers, not a
                        structured record
  ── my tournament   →  FIDELITY: is the record a faithful extraction?
     metrics            (the negative result: NOT quality)

  none of these is calibrated against the others, and none covers the
  "reward what citations punish" set: negatives, replication, reuse,
  corrective work, contribution significance.
```

- **citations** measure social attention, and we know how that fails.
- **the ARA-style rigor seal** measures internal *integrity* — is the argument coherent, falsifiable, well-grounded — as a single LLM grade. useful, but it never asks "is this novel" or "does it matter," and it's calibrated to nothing external. (i use ARA as my testbed and this is a critique of its *data shapes* from a metrics point of view, not of the effort — it's the best structured record going.)
- **LENS and the Metascience Novelty Indicators Challenge** are the strongest external benchmark around: 100k papers rated by domain experts for novelty, and an LLM pipeline that gets ~2× closer to the human median than humans get to each other. but it measures *one axis* — novelty — and it reads whole papers rather than a structured, machine-native record.

three axes — integrity, novelty, fidelity — orthogonal, uncalibrated, and none of them covering the contribution types citations punish. that's the hole. and it's a *substrate* hole first: you can't compute most of the ideal set until the record carries the right shapes.

## the ideal metrics

here's the target set — the ten highest-signal survivors of the tournaments, chosen for measuring what neither citations nor the rigor seal can. i've tagged each by what tier of rigor it can honestly reach — **[det]** deterministic (a structural join), **[anc]** anchored (needs an external resolver but is then reliable), **[jud]** judged (needs a calibrated judge, forever) — because pretending a judged number is a deterministic one is how you build the next Goodhart. **[FIG C — new; the ideal metrics as a table by rigor tier. render the list below as a clean table.]**

1. **Reference-landscape completeness** [anc] — does the work cite the true relevant neighborhood, name the work that *contradicts* it, and not miss what a search agent would surface? the single biggest hole; neither citations nor the seal reach external literature at all.
2. **Novelty vs the literature** [anc][jud] — "done before?" for the claim, the insight, the gap, the method — resolved against the literature neighborhood at publication time, not asserted.
3. **Claim drift / reference truthfulness** [anc][jud] — do the cited sources actually say what they're cited for? (turns a self-quote check into a real does-the-source-support-it check.)
4. **Claim ↔ experiment ↔ evidence entailment, with publication-bias** [det+jud][anc] — does the evidence actually entail the claim, given the claim's *type*? plus a clinical-trial-registry cross-check that flags a reported outcome diverging from the registered one.
5. **End-to-end reproducibility bundle** [det] — do figure + data + code co-exist and cross-link for actual replication? (honest scope: this is *presence and linkage*, not running the code.)
6. **Multi-perspective triangulation** [det+jud] — is a result corroborated across genuinely independent lenses (e.g. wet-lab × computational), or one pipeline relabeled? independence is structural; agreement is judged.
7. **Assumption realism & limitation validity** [jud] — are the load-bearing assumptions realistic, and do the stated limitations add real conditions rather than boilerplate?
8. **Method validity & verification status** [jud] — is the method sound, and is it an accepted one or an over-generalized stretch?
9. **Controlled-vocabulary & latent-space anchoring** [anc] — are terms and datasets anchored to real ontologies / canonical datasets / embedding spaces, so the same entity is recognizable across records?
10. **FOL-ability** [det+jud] — can a clean first-order-logic graph be drawn over the claims (so contradictions and scope are machine-checkable)? the form is deterministic; whether it faithfully captures the paper is judged.

and three from the directions that the top-10 presupposes and i want as first-class:

- **the cross-library evidential claim graph** — the flagship. a knowledge graph whose edges are *evidential* (corroborates / contradicts / replicates / reuses) rather than social. this is the direct structural alternative to the citation network, and every metric above is a query over it.
- **negative-knowledge density** — dead-end density, and whether an abandoned path carries *enough* context to stop the next lab repeating it. citations can't see a dead end at all; this rewards it.
- **the corrective-science score** — replications and refutations weighted *above* imports. the single cleanest inversion of the citation incentive.

the through-line: the deterministic tier is cheap and scales; the anchored tier is reliable once you build the resolvers; the judged tier is where novelty and validity live and it needs calibration and does not fully scale. **importance is judged, not computed** — and that's the honest frontier, not a bug to engineer away.

## steps forward: improve the tooling we already have

none of this needs a green field. it needs four moves, roughly in dependency order:

1. **emit the shapes.** extend the compilers that already exist (ARA, Oshima-style) to write the typed sidecars the affordance analysis specified — a canonical quantity ledger, claim types + logical form, a normalized resolvable reference table, claim→registered-outcome links, an ontology-anchored entity table, a genre manifest that makes honest absence declarable. this alone unlocks the entire **[det]** tier and is the cheapest, highest-leverage step.
2. **build the resolvers.** the **[anc]** tier is only as good as its anchors: a reference resolver over a pinned literature index (semantic-scholar / undermind / OpenAlex-style), a clinical-trial and accession-registry resolver, an ontology + embedding resolver. reliable, reusable, and mostly plumbing.
3. **stand up calibration.** the **[jud]** tier needs human-labeled ground truth and judge ensembles across model families, with the calibration sets versioned and governed against capture — exactly the kind of asset the Novelty Challenge created for one axis. build it for the rest.
4. **run the discrimination experiment.** the open question the negative result left: does *any* of this actually separate good science from bad, and is it only the anchored/judged tiers that carry the signal? run the ideal metrics over existing literature (start with the corpora we have, add a contrasting second domain), validate against external ground truth — trial concordance, retraction/correction records, prior-literature novelty. this is the experiment that tells us whether the ideal set is real or aspirational.

## a callout to funders

here's the part only you can do.

you are where *measurable → rewarded* becomes real. researchers optimize for what you count. so the metrics over the scientific record shouldn't be designed in a lab and handed to you — they should be shaped **by** you, according to what you actually want to reward. i want to build them with funders in the room.

concretely, three ways to get involved:

- **tell us what you want to reward.** which contributions are undervalued in your portfolio — replications, shared datasets, negative results, methods reused across your grantees, corrective work? that list *is* the metric spec. the affordance model then tells you what the record must carry for that metric to be valid rather than gameable.
- **supply the ground truth.** the judged tier lives or dies on human-labeled calibration data. the Novelty Challenge proved a funder-backed labeled corpus can move a whole field on one axis; the other axes need the same. you have the reviewers, the panels, the outcome data.
- **fund the public goods.** the shapes, the resolvers, and the calibration sets are shared infrastructure — most useful when open, and under-provided by anyone with a product to sell. this is the kind of thing non-traditional funders are already piloting as *funding conditions* (Gates, Astera); i'd love to build it with the larger innovation agencies too — ARIA, NADI, ARPA, SPRIND — and with the metascience units already procuring next-generation indicators.

the honest status is the same as the substrate's: the metrics are designed and adversarially stress-tested, the negative result is real and clarifying, and the two things still missing are proof they discriminate at scale and a funder willing to make the good ones count. neither is a protocol problem. that's the invitation.

*(companion piece: the layer-cake substrate post, on the medium these metrics run over. this post is why the metrics come first.)*
