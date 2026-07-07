# A Layer Cake for Science

**working draft — supersedes the earlier layer-cake draft. integrates the ideal-affordance work as a deep dive into the middle layer, resolves the places where the new view trumps the old, and updates next steps. figure notes in [brackets]; new figure sketches inline as fenced blocks — redraw them properly before publishing.**

---

papers suck. but what's a better medium?

we've established that the current medium of publishing locks us into a suboptimal mode of discovery. so what substrate of communication unlocks this latent potential?

i think it's a layer cake, each layer catering to a slightly different need. here's the recipe. take a **top layer of narrative-form objects**, much like papers or blog posts, made for human consumption — either written by a human or compiled on-demand by AIs. add a **middle layer of typed particles** — claims, evidence, methods, data, code — as the connective tissue; this part is agent-native, and the particles are what narratives compile from. finally, a **latent embedding space** (or many — see the alien-proteins post) anchoring everything else, native to LLMs and other ML models.

a system like this would allocate expert attention far more efficiently while letting silicon intelligences operate on and extend scientific knowledge. it would also blow open the design space for metrics that can represent real scientific contribution — beyond "was it cited a lot."

but i want to be precise about one thing up front, because i got it wrong in an earlier version of this and the work since has corrected me: **the middle layer is really two jobs, and they're not equally solved.** one is turning a single piece of work into typed, inspectable particles that a narrative can compile from. that job is well specified now — i'll show you exactly what it has to afford. the other is stitching particles *across* projects into a git-style contribution graph where a replication or a reused method counts as its own contribution. that job is the harder, more novel one, and it's still open. i'll be honest about which is which.

## architecture

the scientific record stops being a single artifact and becomes three representations of the same knowledge, each in the modality that fits a different consumer: humans read narrative, agents operate on particles, models compute over latent space. they aren't separate stores — a narrative compiles from particles; a particle anchors in latent space. one canonical knowledge object, three views onto it. **[fig 1 — the three views over one object; keep as is.]**

## the narrative layer

the human-facing layer, and the closest to what we have now — except it's no longer the source of truth and no longer authored once and frozen. narratives compile on demand from particles, in whatever format fits the reader: a paper, a short explainer, slides, a video, a dialogue, shaped by the reader's background and what they're trying to do. the paper survives, but as a *view* — a rendering of the underlying particles for a particular human at a particular moment, not the thing itself. each narrative links back down to the particles it's built from, so a claim in prose is one hop from its evidence. **[fig 2 — narrative links down to particles; keep.]**

one refinement the metrics work forced on me, and it matters: there are **two ways prose can relate to particles, and only one of them is trustworthy.** prose can be *rendered* from the particles — generated out of the typed record — in which case it agrees with the record by construction and that agreement tells you nothing about whether the record is faithful. or prose can be *authored independently* and then *reconciled* against the particles — checked, after the fact, for agreement. only the second case makes narrative↔particle agreement a real signal against fabrication. the on-demand compiled paper is the first case; a human's own write-up, checked against the particles, is the second. worth naming both, because a system that only ever renders can look self-consistent while hiding a lie.

## the particle layer

this is the connective tissue, and the primary medium of contribution. particles are granular, typed units — claims, evidence, methods, data, code — each a standalone, valid contribution with typed links to the others. **[fig 3 — the git-style contribution graph, fork/merge/extend; keep.]**

the point of going granular is what it makes *countable*. today a replication, a shared dataset, a confirmation or refutation of someone else's hypothesis, a method reused three projects downstream — most of this is invisible labor that never accrues to anyone's reputation. as particles, each is a first-class contribution that can be pointed at, credited, and built on. data and code live here too, not as supplementary files hanging off a paper but as their own particle types, reusable on their own terms.

this layer is agent-native: too granular and too voluminous to read directly, but exactly the full-context substrate agents work best on. individual particles are and must be inspectable by humans.

### deep dive: what the middle layer has to *afford*

here's where i've done the most new work, and where i have to split the two jobs i flagged up top.

**job one — the within-a-work particle format — is now specified in detail, and it did not come from wishful design.** it came backwards, from metrics. i spent a year building indicators of scientific contribution over a structured corpus (the ARA format, on an Alzheimer's library) and the headline result was a negative one: *metrics computed over a record's own structure measure the fidelity of the record, not the quality of the science.* a well-compiled record of bad science and a well-compiled record of good science were indistinguishable. real signal appeared only at the claim level, anchored to something outside the record — trial registries, prior literature.

that negative result turned into a design spec by asking a different question: for every metric i *wanted* but couldn't build, **why** couldn't i build it? almost never because the information was missing. because it was stored in a shape only an LLM could re-extract — a number hand-retyped as prose in four places instead of one typed value, citations as author-year strings instead of resolvable IDs, honest absence indistinguishable from lazy omission. the record didn't lack the knowledge; it lacked the *shape*.

every blocked metric sorts into one of three classes, and each class tells the format what to do. **[fig 6 — new; sketch below.]**

```
[FIG 6 — the three affordance classes]

  BLOCKED METRIC             WHY IT'S BLOCKED            WHAT THE FORMAT MUST DO
  ─────────────────────────  ──────────────────────────  ────────────────────────────────
  format-recoverable         the fact is there, but as    emit the same fact TYPED →
  (numeric reconciliation,   prose an LLM must re-read    the metric becomes a
   claim typing, genre-                                   deterministic join
   conditioned absence)
  ─────────────────────────  ──────────────────────────  ────────────────────────────────
  anchor-dependent           the fact points outside      guarantee RESOLVABLE external
  (novelty vs prior work,    the record and nothing       IDs (DOIs, registrations,
   registry concordance,     resolves the pointer         accessions) so registries and
   claim-drift)                                           indices can be joined against
  ─────────────────────────  ──────────────────────────  ────────────────────────────────
  irreducibly semantic       no format change makes it    a calibrated judge, forever —
  (novelty judgment,         computable                   the format's only job is to
   entailment quality,                                    feed the judge cleaner,
   assumption realism)                                    pinned inputs
```

so the particle format isn't one flat pile of typed fields. it's **three tiers of rigor**, and the honest move is to keep them visibly separate so nobody mistakes one for another:

```
[FIG 5 — new; the middle layer as three rigor tiers feeding a funder view]

        ┌───────────────────────────────────────────────┐
        │  JUDGED     novelty · significance · validity   │  a calibrated judge +
        │             (irreducibly semantic)              │  human calibration set
        ├───────────────────────────────────────────────┤
        │  ANCHORED   refs · registrations · datasets     │  resolved against the
        │             (join to the outside world)         │  outside world; failures
        ├───────────────────────────────────────────────┤  quarantined, not faked
        │  DETERMINISTIC  typed quantities · claim logic  │  pure structural joins;
        │                 · cross-layer graph · genre     │  exact + reproducible
        └───────────────────────────────────────────────┘
                              │
                              ▼
              a decomposed credibility view for a funder —
              never one collapsed number; each line labelled
              with which tier it came from
```

the discipline that makes this work: **the tier is on the label.** a deterministic "these two numbers reconcile" is not dressed up as the same kind of fact as a judged "this looks novel." a reader — or a funder — can gate on the deterministic floor, rank on the judged tier, and *audit any number back to its source and its rigor class.* honest absence ("not specified," "not applicable," "unresolved") is a first-class value scored equal to an honest answer, so a typed field never creates pressure to fabricate.

i didn't hand-design this. i derived it by running the three affordance classes back through the same adversarial tournament i use for metrics, then red-teaming the result. the method section at the end walks through how. **[fig 7 — the method pipeline; sketch in the method section.]**

**and here's where the new view trumps the old.** the earlier draft implied this middle layer both structured a single work *and* formed the cross-project contribution graph, seamlessly. it doesn't, not yet. everything above is **job one — within a single work.** it's specified, adversarially stress-tested, and it makes the "measurable" prerequisite real for one work at a time.

**job two — the cross-object contribution graph — is still the open frontier.** the fork/merge/extend picture in fig 3, where a replication in lab B or a method reused in project C accrues credit back to its origin across the whole graph, is a *different* engineering problem, and the affordance spec barely touches it. its cross-work surfaces — resolving a citation to the exact prior work, recognizing the same entity across two records — exist but are deliberately unscored today. i'd rather say that plainly than let the diagram promise something the spec doesn't deliver. the credit graph is the part i most want to build next, and the part with the least ground under it.

existing efforts sit almost entirely in job one. **ARA** and **Oshima** are the only two i know that bind *all* the particle types with typed cross-layer links and compile a narrative from them; **nanopublications** do the claims-particle beautifully but stop there, with no execution or exploration layer. ARA in particular proves the core bet — that a granular, standardized layer improves what agents can do *today*, even compiled from lossy existing papers — and pilots agent-assisted review that's far faster than current peer review, precisely because the format is granular and standardized. none of them build the cross-project credit graph either. that's the gap.

## the latent layer

the anchor. every particle embeds into one or more learned spaces — the multi-omics embedding space from the alien-proteins post is one; there will be others, and they may overlap or compose. this is the model-native layer: not meant to be read, meant to be computed over.

geometry does the work keywords and citation graphs can't. retrieval becomes meaning-based — every claim related to A-beta, all evidence produced by method X in context Y — surfaced by proximity rather than string match. and automated discovery becomes a property of the space itself: gaps, dense regions, and unexpected adjacencies between distant particles are where new hypotheses come from. the synthetic-ideal-node trick from the alien-proteins post lives here: generate the point that *would* explain the disease, then read off the nearest real particles. **[fig 4 — latent-space discovery; keep. optionally reuse the alien-proteins synthetic-node figure.]**

the affordance spec only touches this layer instrumentally — it anchors particles into a pinned embedding space so entities can be recognized and novelty can be judged against a neighborhood. building the latent layer into a first-class discovery surface is its own project, mostly still ahead.

## how i derived the ideal affordances (method)

worth showing, because the middle-layer spec is the one part of this that's more than a sketch, and because the *method* is itself a small piece of the argument — you can design incentive-resistant infrastructure with an incentive-resistant process.

1. **start from failure.** the metrics testbed's negative result (structure measures fidelity, not quality) is the input, not an embarrassment. it tells you the current shape can't carry the signal.
2. **audit every blocked metric against the shape that blocked it.** this produces the three affordance classes above — format-recoverable, anchor-dependent, irreducibly semantic. it separates, empirically, what better *shape* can fix from what will always need judgment.
3. **tournament the design, don't author it.** for each of twelve affordance gaps, four independent proposers (two on one model family, two on another) each designed a solution; a deliberately harsh, meta-science-literate judge picked the best two and wrote critiques; the finalists refined and merged. the point of the tournament is the same as the point of the metrics tournament — a design can't be graded by the agent that proposed it.
4. **merge, then red-team.** the twelve winning designs were merged into one spec, then put through an adversarial critique pass whose only job was to find over-claims and internal contradictions. every over-claim it found was forced down to an explicit, labelled limitation rather than quietly kept. the changed labels are the audit trail.

```
[FIG 7 — new; the design method]

  12 affordance gaps
      │  each gap:
      ▼
  4 proposers ──► harsh judge picks 2 ──► refine + merge ──► gap design
  (2 model fam A,
   2 model fam B)
      │  (×12)
      ▼
  merge 12 gap designs ──► adversarial red-team ──► FINAL affordance spec
                            (forces every over-claim         (3 rigor tiers +
                             down to a stated limit)          funder view)
```

**honest status of the spec.** it's adversarially hardened but *empirically unvalidated.* three things i can't yet claim: it has **not** been shown to actually separate good science from bad (the discrimination test hasn't been run); its judged tier does **not** scale to a whole corpus (you can run the cheap deterministic + anchored tiers at scale, but the calibrated-judge tier only on a triage set plus an audit sample); and its anti-fabrication guarantees rest on an **independence between automated checkers that i can assert but not yet measure** — genuinely independent, non-correlated checking is earned at exactly one point in the design, where a non-LLM matcher does the work. everywhere else, "independent" means "a different model," and two different models can share the same blind spot.

that last point generalizes into something i now believe about this whole category: **a record that computes its own credibility doesn't eliminate trust, it relocates it** — from trusting the author's prose to trusting a calibration set and an assumed independence between judges. that's real progress, because the trust is now somewhere you can audit. but it's not the free lunch the phrase suggests, and pretending otherwise is how you build the next Goodharted metric.

## related work

**Oshima** ingested paper PDFs and decomposed each into three particle types — claims, the evidence backing them, the methods that produced the evidence — each pinned to its exact source location, extraction fully automated, with a deterministic path that tried to render claims into first-order logic. but that's the whole of it: Oshima only ever *read* papers. no native authoring, and nothing connecting particles across papers beyond read-only theme groupings. it failed for the reason they all fail — the incentives are so intertwined with the current mode of publishing that switching costs are immense, especially when it costs extra work. backprocessing alone adds little (though it can lay the groundwork for agents to assess and review, as ARA showed).

**Agent-Native Research Artifacts (ARA).** i was excited when i saw someone had built a mature version of the Oshima idea. ARA is a filesystem protocol where the paper is a compiled view of four layers — `/logic` (claims + verifying experiments + typed related-work), `/src` (code), `/trace` (exploration DAG with dead ends), `/evidence` (raw outputs) — stitched by cross-layer bindings so a claim links to the code that tests it and the evidence that grounds it. the team showed that structure beats narrative for agents even when compiled from the same lossy PDF+repo — no new information, just reorganized [verify against Liu et al. 2026 before publishing: PDF-answerable fidelity ~95.6% vs ~80.8% at ~12% fewer tokens; reproduction ~64.4 vs ~57.4, gap widening with difficulty]. **Discourse Graphs** (an early, lab-internal implementation) inspired a lot of my thinking here [confirm attribution].

**the rest of the ecosystem** each solves one fragment; none binds logic + code + exploration + evidence with typed cross-layer links. **FAIR**: principles for data (findable/accessible/interoperable/reusable) — standardizes data metadata, silent on the structure of the argument. **RO-Crate**: bundles artifacts into archival packages — wrapping, not decomposition. **DeSci (Nodes/Publish/Codex)**: the full-stack version — research objects bundling manuscript + data + code, persistent IDs, decentralized substrate, FAIR-by-construction. i was PM there, where the unit was the "research object" — but a node isn't actually granular; it's a compiled paper-plus-data-plus-code, which made it hard to adopt for two reasons. first, friction on the inputs — researchers are shy about their code and don't want to expose their data. second, and decisive, no incentive to assemble these objects instead of just writing a paper, because the funding incentives are so ingrained. we pushed hard, never got adoption wide enough to matter, and the systems change never landed.

## what now?

i don't have the answer to the adoption problem. the architecture is the tractable part; the wall every prior effort hit — Oshima, DeSci, nanopubs — is incentives, and i expect it's where ARA will strain too.

what's *different* now is that the authoring burden is dissolving. particles no longer have to be hand-assembled by a researcher with no reason to assemble them — agents already sit inside the scientific workflow, and the research trace they generate is the raw material. capture can be largely automated; even a lossy backfill from papers pays off. necessary, nowhere near sufficient.

and there's a second wall i under-rated in the earlier draft: **even the measurement isn't free.** going granular and standardized gets you *fidelity*-measurable cheaply and deterministically — is the record faithful, do the numbers reconcile, is every claim typed. but the thing funders actually want to reward — *is this novel, is it valid, does it matter* — stays in the judged tier: calibrated, human-anchored, and not fully scalable. standardization opens the door to importance-measurement; it doesn't walk through it. that's not a reason to stop; it's the actual frontier of "reward what citations punish."

so the next steps are concrete, and they're both about closing the gap between "designed" and "shown to work":

**1. run the affordance-derived metrics over previous literature — the discrimination test the spec hasn't had.** compile existing corpora into the particle format (starting from the ones i already have, then a contrasting second domain) and ask the question the negative result left open: does *any* of this actually separate a well-done study from a poorly-done one — and if so, is it only the externally-anchored tier that carries the signal, as the testbed suggested? validate against external ground truth: trial-registry concordance, retraction and correction records, prior-literature novelty baselines like the Metascience Novelty Indicators Challenge / LENS. this is the experiment that tells us whether the middle layer's *measurable* promise is real or whether importance genuinely lives only in judgment. it also stress-tests the three affordance classes: do the predicted boundaries (format-recoverable / anchor-dependent / irreducibly semantic) hold up when you actually try to compute across a corpus?

**2. work with funders to improve their metrics-based insights — and make measurable → rewarded real.** funders are where the incentive actually lives; you can't out-design a system where grants, jobs, and tenure are denominated in papers, so it has to change at the source. two directions, both two-way. first, the affordance model directly sharpens the metric efforts funders are *already* running: for any indicator they want (novelty, reproducibility, contribution significance), it says what the underlying record must carry for that indicator to be valid rather than gameable — so their metrics get a theory of their own preconditions instead of being computed over whatever shape happens to exist. second, co-design the metrics they'd actually reward, on the particle substrate, so that adopting the substrate finally *pays* — which is the only thing that ever moved adoption. non-traditional funders are already experimenting with new publishing practices as funding conditions (Gates, Astera); i want to also reach the larger innovation-minded agencies (ARIA, NADI, ARPA, SPRIND) whose insight-generation could be materially improved by an affordance-aware view of the record.

honest status: the medium is designable and partly demonstrated; the middle layer's within-work half is specified and adversarially hardened; capture is finally yielding to agents; and the two things still missing are the same two as before — an institution willing to experiment and a funder willing to change what counts — plus the empirical proof that the metrics discriminate at all. none of those is a protocol problem. that's exactly why the next steps are experiments and funder collaboration, not more schema.

---

## appendix a — design principles

with the architecture on the table, here's what it has to afford. two tiers: the ways of working we want, and the prerequisites that make them possible.

**affordances**

- **collaborative.** the best ideas are approached from different angles. papers have a closed author group and exclude perspectives at the outset. a better medium allows git-style forking, merging, collaboration. *(this is job two — the cross-object contribution graph — and it's the least-built part; see the particle-layer deep dive.)*
- **iterative.** research is iterative — ideas, tries, changes. all of it needs to be rewarded, which means first making it visible, then measurable, then incentivized. researchers publish as they go, each contribution counting, even "just" an idea or "just" a dataset.
- **fast.** we publish at the speed of discovery, not reviewer 2 — continually capturing progress, including ideation, failure paths, pivots. anyone can pick up anyone's work at any point.
- **comprehensive.** we publish everything. too much for humans — but that's already true of papers, and agent capability scales with context. everything-as-we-go means agents get full context, learn from prior mistakes, and everyone avoids the same dead ends.

**prerequisites**

- **composable.** particles build on each other by direct reference and import; links must be typed to be interpretable. each particle is like a code package — it extends every importing project while staying a standalone contribution.
- **referential.** science builds on prior science; the record must reflect it. particles anchor in conceptual/latent space, which is what creates AI-native access and discovery.
- **standardized.** typed links and machine-actionability only work if particles share schemas — a claim is always statement + falsification + proof; data always carries units and provenance. matters most on data, where format/metadata heterogeneity is what kills reuse. keep it light enough not to reintroduce the authoring burden.
- **measurable.** *(rewritten — this is where the new work changed my mind.)* you can only reward what you can measure, and only measure what's standardized. but standardization buys you two very different things, and conflating them is a trap: it makes **fidelity** measurable cheaply and deterministically (is the record faithful to itself and its sources), and it makes **importance** *approachable* but not automatic — novelty, validity, and contribution significance still need a calibrated judge and external anchors, and don't fully scale. so "measurable → rewarded" is real, but it splits: reward the fidelity floor deterministically, and reward importance through judgment you've made auditable and calibration you've made honest. this is the hinge `iterative` pointed at (visible → measurable → rewarded) and the direct answer to why granular publishing hasn't stuck: until each particle *counts*, the rational move is still to just write the paper — and until the importance metrics are validated, "counts" is a promise, not a fact.

## appendix b — provenance

the affordance model, the three rigor tiers, and the method above come from a documented body of work: the metrics testbed and its negative result; the affordance-gap audit that produced the three-class taxonomy ("the record doesn't lack the knowledge, it lacks the shape"); and the adversarial design tournament that turned the taxonomy into the middle-layer spec. all of it, including the honest limitations, is written up and can be linked as an appendix or repo pointer when this goes public. [decide how much of the repo work to make public before publishing — the negative-result report and the affordance audit are the strongest exhibits.]
