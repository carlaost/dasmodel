# The Grounded Research Object (GRO)

### A publishing format whose unit of record computes its own credibility — so funders can measure good science, not just count papers

> **Status & lineage.** This is the synthesis of twelve independent design tournaments (run
> `wf_f0bc615b-a88`), each closing one gap identified in `AFFORDANCE_GAP.md` between the metrics we
> want and the data the current ARA compiler emits. Each gap ran four proposers (two GPT‑5.5/Codex,
> two Sonnet), a critical meta‑science judge that picked and critiqued the best two, and a refine round
> where finalists hardened their designs. The raw winning designs are preserved verbatim‑structured in
> `TOURNAMENT_DESIGNS.md`. GRO is **not** "ARA v2" — the inherited ARA format is the substrate this
> work *critiques*; GRO is the substrate the metrics actually require. It absorbs ARA's good ideas
> (progressive disclosure, honest absence, grounding discipline) and fixes the shape.

---

## 0. Manifesto

Today a paper is a PDF: prose optimized to be *read*, with data and code bolted on as afterthoughts in
a supplement. Every metric we might want — is this claim supported, is it novel, does the number match
the source, is the method sound — must be recovered by an LLM re‑reading that prose, non‑deterministically
and unverifiably. So we fall back to counting papers and citations, and we fund the wrong things.

GRO inverts the default. **The unit of publication is a typed, resolvable, externally‑anchored knowledge
object that still renders to readable prose, but whose every load‑bearing fact exists once, as data, with
a machine‑checkable provenance anchor.** Assume a world where everyone publishes this way and makes all
artifacts available — code, data, protocols, the lot. In that world:

- **Correctness checks become joins, not guesses.** "Does the claim's number match the evidence table
  and the source?" is a lookup over one canonical value, not a fuzzy match of four hand‑typed copies.
- **Novelty and significance become reproducible, auditable judgements** — calibrated against human
  experts, grounded in a publication‑time‑frozen map of the field, with the score *defined as the hash
  of an archived reasoning transcript* rather than a re‑rollable LLM opinion.
- **Gaming gets expensive by construction.** Length, boilerplate, fabricated‑but‑consistent content,
  citation‑count inflation, and outcome‑switching each hit a specific structural defense.
- **Honesty is never punished.** Every field has a first‑class `not_specified` / `not_applicable` value
  scored *equal to* an honest presence, so a typed slot never pressures anyone to fabricate.

The output is a **funder‑facing credibility dossier**: a decomposed, per‑dimension, calibrated read on a
piece of work — deterministic where it can be, reliably anchored where it must reach the outside world,
and reproducibly judged where the question is irreducibly semantic.

---

## 1. One‑glance architecture

GRO is three tiers of verification stacked on one graph. Everything above references everything below
**by stable id** — no fact is ever re‑typed.

```
                          ┌───────────────────────────────────────────────┐
   TIER C · JUDGED        │  P1 Novelty/Significance   P2 Entailment        │  reproducible,
   (semantic, calibrated) │  P3 Realism/Validity       P4 Frontier/Triangn │  human-calibrated,
   append-only verdicts   │  ── ride on the graph, never author it ──       │  content-hash = truth
                          └───────────────▲───────────────────────────────┘
                                          │ reads by id
                          ┌───────────────┴───────────────────────────────┐
   TIER B · ANCHORED      │  L6 Reference Spine   L7 Registry Join          │  reliable given a
   (external resolution)  │  L8 Delta / SOTA Anchor Ledger                  │  pinned resolver;
   pinned resolvers +     │  ── resolve ids to the outside world ──         │  failures quarantined
   quarantined judgement  └───────────────▲───────────────────────────────┘
                                          │ references by id
                          ┌───────────────┴───────────────────────────────┐
   TIER A · DETERMINISTIC │  L1 Quantity Ledger   L2 Claim Logical Form     │  exact, reproducible
   (the computable core)  │  L3 Entity Spine      L4 Cross-Layer Graph      │  run-to-run;
   one canonical record   │  L5 Genre Contract                              │  pure functions
   per fact, by id        └───────────────────────────────────────────────┘

   Cross-cutting substrate:  human-readable prose renders FROM the typed layers (or is round-trip
   reconciled AGAINST them) · inline anchor tokens · honest-absence symmetry · shared VERSIONED
   ecosystem artifacts (vocabularies, taxonomies, calibration sets, pinned resolvers/classifiers).
```

The design rule every layer obeys, and the reason the tiers don't contaminate each other:

> **Deterministic facts and semantic judgements live in physically separate files.** The graph, the
> ledgers, and the structural checks are pure functions of authored data. Every "does this actually
> hold / is this actually novel / is this realistic" verdict lives in an **append‑only, content‑hashed,
> judge‑authored log** that *references* the deterministic skeleton and can never be edited into it.

---

# TIER A — The deterministic core (Class A)

These five layers make the facts the ARA already contains *computable* instead of *re‑extractable*. They
are pure functions of authored data; every metric they afford is exact and reproducible run‑to‑run.

## L1 · The Quantity Ledger  — *canonical typed numbers with rounding‑aware binding*
*(tournament winner: **CQL‑RAB**, Canonical Quantity Ledger with Rounding‑Aware Binding + independent fidelity audit)*

**Problem it kills.** A load‑bearing number is re‑typed up to four times (claim prose, the `value ← ref
«quote»` DSL, the evidence cell, the tree result). Reconciliation is fuzzy string‑matching of copies.

**Design.** Every load‑bearing number is authored **exactly once** in `logic/quantities.yaml` as a typed
record whose numeric truth is a single full‑precision `value` plus structured `uncertainty` — **never a
frozen printed string**. Prose, tables, and trees keep their own context‑appropriate rendering (`0.859`,
`0.86`, `~0.86` are all legal) and carry an inline tag `[[Q:Q01]]` next to the printed literal. The
validator does **not** byte‑compare; it parses the printed literal to `(number, printed_precision)` and
asserts `round(value, printed_precision) == printed_number` — deterministic **and** rounding‑correct.

```yaml
# logic/quantities.yaml
quantities:
  - id: Q01
    value: 0.859                       # full precision, the ONLY numeric truth
    kind: result                       # input (set) | result (produced)
    quantity_type: p_score
    unit: dimensionless
    uncertainty: {type: none}
    source_anchor: {file: evidence/tables/table2.md, line_range: [14,14],
                    checksum: "sha256:…", quote: "p217_MS (0.859)"}
    reconcile_status: ok               # deterministic: ledger↔tags↔render() all agree
    external_fidelity:                 # written by an INDEPENDENT extraction pass, not the compiler
      status: verified                 # verified | mismatch | unfetchable | not_attempted
      audited_by: "extractor@v3 (different agent than compiler)"
    registry_ref: {registered_value: 0.86, fetch_log: [...]}   # for publication-bias join (L7)
```

Two mechanisms make it trustworthy rather than self‑certifying: **(1)** grounding is split into a
compiler‑set `reconcile_status` (internal consistency) and an `external_fidelity` block written by a
*separate extraction agent* that re‑fetches each anchor by `file+line_range+checksum` and re‑reads the
number — so "the number is in the ledger" and "the number is actually in the source" are different,
independently‑produced facts; **(2)** a `numeral_coverage` audit forces every numeral in prose/tables to
be tagged, matched, or explicitly listed as non‑load‑bearing, so "load‑bearing" can't be gamed by
un‑tagging inconvenient numbers.

**Metrics unlocked (all deterministic, except fidelity which is reliable‑anchored):** cross‑layer numeric
reconciliation · grounding coverage · **extractive fidelity** (value actually at the cited source) ·
self‑consistency recompute of derived numbers · publication‑bias / outcome‑switching join (L7) ·
ordinal‑ranking integrity · honest‑absence rate.

## L2 · Claim Logical Form  — *an Oshima‑style predicate‑argument layer that a solver can check*
*(winner: **CLF/CK**, Claim Logical Form with a Comparability‑Key gate)*

**Problem it kills.** Claims are prose with a `Status` but no `claim_type` and no logical structure — you
cannot draw a clean FOL graph, detect claim↔claim contradictions mechanically, select a type‑aware
entailment rubric, or measure over‑claiming.

**Design.** Every claim keeps its prose block and gains **one** co‑located `**FOL**` field: a
human‑readable rendered logical form plus the typed YAML it is deterministically rendered from. Predicates
come from a **closed, versioned vocabulary**; arguments bind to **entity ids (L3)** and **quantity ids
(L1)**; an explicit quantifier and a **graded generality ladder** encode scope; comparators are interval
constraints; `claim_type` is cross‑validated against the predicate used.

```yaml
# a **FOL** field inside a ## C01 block in logic/claims.md
FOL: "∀ x ∈ Pop:amyloid_cohort . rank(p217_MS, x) = 1  ∧  auc_diff(p217_MS, p181_IA) > 0"
```
```clf
claim_type: comparative_superiority          # cross-checked against predicate `rank`/`auc_diff`
predicate: rank
args: {marker: E:p217_MS, outcome: E:abeta_positivity}    # E: → entity spine
quantifier: {type: forall, over: Pop:amyloid_cohort}      # → population registry
scope_generality: 3                          # graded ladder: 1 sample … 5 universal
comparators:
  - {op: gt, lhs: Q:Q07, rhs: 0, comparability_key: CK:auc_diff@vocab_v3}
```

The decisive innovation is the **Comparability Key (CK)**: no solver ever sees a raw pile of comparator
intervals. Every constraint first emits a deterministic CK — an equivalence‑class label — and the numeric
SAT pass only compares constraints that share a CK, so it can't "prove a contradiction" between an
accuracy and a runtime. A shared **predicate vocabulary**, a **population/scope registry** (making
over‑claiming a mechanical field diff: does the claim's `scope_generality` exceed what its data/experiment
support?), a **verb→predicate cue lexicon** (catching causal‑cued prose bound to a merely‑correlational
predicate), and a **derived, hash‑gated AST** (single source of truth — the YAML block generates the
graph; the graph is never hand‑authored) complete it.

**Metrics unlocked:** M09 FOL‑ability · M08 contradiction (symbolic polarity/predicate half + numeric
interval‑UNSAT half) · D3 over‑claiming (cohort→population leap magnitude) · D1/S4 `claim_type`↔predicate
and predicate‑selection integrity (the *rubric selector* for Tier‑C entailment) · prose↔FOL fidelity
(fabrication surface) · cross‑ARA consistency.

## L3 · The Entity Spine  — *stable ids + ontology xrefs + reproducible embedding anchors*
*(winner: **Entity Identity Layer**, anchored registry + hybrid two‑arm resolution)*

**Problem it kills.** Concepts/methods/variables are prose headings and free‑text "related" lists; nothing
maps them to a controlled vocabulary, so claims↔concepts is fuzzy overlap and cross‑ARA interop is
impossible.

**Design.** `logic/entities.yaml` gives every entity *mechanically referenced by another layer* a stable
local id, optional external‑ontology xrefs, and a reproducibility‑checked embedding anchor. The Class‑B
reliability does **not** rest on "two LLMs agreeing": an xref reaches `resolved` only when a
**deterministic literal matcher** (exact + registered‑synonym lookup against the pinned vocabulary's own
labels) **and** a **semantic LLM linker** concur, with thresholds from a corpus‑shared
`resolver_calibration.yaml` gold set. A derived `symbol_table.yaml` gives L2's FOL symbols a bijective,
collision‑checked mapping.

```yaml
# logic/entities.yaml
entities:
  - id: E:p217_MS
    surface: "mass-spectrometry-derived plasma p-tau217"
    kind: measure
    xrefs:
      - {vocab: "NCIt", term_id: "C…", label: "phospho-tau 217",
         literal_match: exact, semantic_match: 0.94, status: resolved}   # both arms agreed
    embedding_anchor: {vector_ref: "vec://…", text_hash: "sha256:…"}      # text DERIVED from provenanced fields
```

**Metrics unlocked:** M10 controlled‑vocabulary referenceability · M12/M64 latent‑space anchoredness ·
M13 claims↔concepts consistency (a set operation) · resolver precision (calibration‑audited) · cross‑ARA
entity‑recognition rate.

## L4 · The Typed Cross‑Layer Graph  — *the artifact as a real multigraph, not markdown with ids*
*(winner: **Edge Ledger v2**, nodes.yaml + edge_schema.yaml + edges.yaml + separate verdict log)*

**Problem it kills.** The `C##/E##/RW##` id system supports only *existence* binding. Every "X↔Y match"
metric must reconstruct the relationship from prose.

**Design.** A global `nodes.yaml` gives every addressable object one typed id + resolvable locator; an
ecosystem‑level `edge_schema.yaml` declares legal endpoint type‑pairs and required attributes per edge
type; a per‑ARA `edges.yaml` emits **once** every relation prose buries (`Proof`, `Verifies`, `Caused by`,
`Derived from`, `Baselines`, RW `extends/refutes`). Four hardenings make "deterministic" real rather than
a costume:

1. **Prose is authored independently and edges are reconciled *against* it** (round‑trip), restoring the
   independent second source — edges are not rendered *from* prose nor prose *from* edges.
2. **Every rubric‑gating attribute is itself a typed object with its own anchor** into a resolvable node,
   so a `claim_type` rubric can only be satisfied by anchored evidence, not an asserted string.
3. A **genre‑conditioned nullability table** (`nullability.yaml`, keyed to L5's paper‑type vocabulary)
   says which nulls are *legal* for which genre — killing "not_applicable is the universal escape."
4. **Semantic verdicts live in a separate append‑only `verdicts.yaml`** (Tier C), so the deterministic
   skeleton is structurally incapable of absorbing a judgement; declared **acyclic subgraphs** get cycle
   checks.

**Metrics unlocked:** structural‑correspondence coverage · test adequacy (claims whose type‑required
design is present) · reconciliation integrity (prose↔graph) · honest‑absence legality · `relates` catch‑all
ratio (anti‑laziness) · graph acyclicity · anchor‑licensing rate. (The *semantic* "does the edge hold" is
P2.)

## L5 · The Genre Contract  — *absence becomes declared‑and‑checkable, never silent*
*(winner: **Genre Contract v2**, taxonomy‑derived expectation ledger with a pinned blind classifier)*

**Problem it kills.** Genre‑conditionality is expressed as *silent absence*, so a metric can't tell an
honest "no code because it's a meta‑analysis" from a lazy omission. `domain` is free text.

**Design.** Genre is a first‑class, versioned classification that **derives** a deterministic per‑slot
expectation set from shared tables. Critically, the classification's root is not freely chosen: every GRO
carries both a self‑declared `paper_type` **and** one from a **pinned, checklist‑blind classifier** (fixed
model id + prompt hash + temp 0, inputs restricted to title/abstract/venue). On disagreement, scoring uses
the **union** of both genres' expected sets (the stricter set), so declaring the narrowest genre can never
shrink what you're held to. Each conditional expectation (`expected_if:<fact_id>`) is a **deterministic
predicate** over anchored content in other layers.

```yaml
# logic/genre.yaml
paper_type: {value: network_meta_analysis, anchor: {file: PAPER.md, quote: "PRISMA-DTA network meta-analysis"}}
paper_type_blind: network_meta_analysis          # pinned classifier; agrees → no penalty widening
expectations:                                    # DERIVED from taxonomy/expectation_defaults.vX
  src/execution:      not_applicable             # scored EQUAL to honest presence
  logic/quantities:   expected
  evidence/tables:    expected
  data/preprocessing: expected_if:has_primary_data   # deterministic predicate → false here → n/a
```

**Metrics unlocked:** expectation‑coverage completeness · lazy‑omission count · honest‑absence integrity ·
genre honesty (declared‑vs‑blind contested rate) · padding ratio · taxonomy‑gap load.

---

# TIER B — Anchor layers (Class B: reliable, not deterministic)

These reach outside the artifact. They can't be deterministic, so they are engineered for **reliability**:
identity resolution is deterministic given a *pinned resolver*; the irreducible judgement is *quarantined*
and *audited*; every failure mode is a first‑class, honestly‑labelled state.

## L6 · The Resolved Reference Spine  — *every citation resolves to a real external id*
*(winner: **Resolved Reference Spine v2** / **Resolved Reference Ledger** — near‑identical finalists)*

**Problem it kills.** DOIs live only in full `RW##` blocks; the rest of the citation footprint is
author‑year prose; even present DOIs are format‑checked, not resolved ("well‑formed but fabricated passes").

**Design — the three‑way split that kills the citation‑count Goodhart hole:**
- `refs/reference_spine.yaml` — one canonical `R###` record per distinct cited **work** (dedup across all
  layers), carrying resolved external ids (DOI/arXiv/OpenAlex/S2) + a first‑class resolution status.
- `refs/citation_mentions.yaml` — one `X####` record per citation **occurrence**, pointing to its `R###`;
  prose still renders naturally as `[Janelidze et al., 2023](ref:R014)`.
- `refs/support_edges.yaml` — one `SREF###` per **claim/gap an occurrence supports**, splitting a
  deterministic `anchor_check` (Class B: is the quoted span verbatim present in retrieved source text?)
  from the semantic `does‑the‑source‑support‑the‑claim` verdict (quarantined to Tier C).

The resolver is **falsifiable**: `fabricated` is a hard misconduct signal assertable only after a stated
retry policy; unresolved grey‑literature is an honest first‑class state. A `resolution_candidates.yaml`
sidecar records *every* candidate weighed (not just the winner) so `match_confidence` is recomputable.

**Reliability / protocol / what the ecosystem must provide:** a pinned resolver version + snapshot of the
external index; deterministic candidate scoring; a retry+quarantine policy; verbatim‑span receipts. Failure
modes (registry down, ambiguous match, grey lit) each map to a distinct honest status, never a silent pass.

**Metrics unlocked (reliable‑anchored):** resolution‑integrity rate · reference‑graph structural integrity
· receipt‑backed anchor coverage · **claim‑support fidelity** (S3 claim‑drift) · citation‑dedup compression
(kills count inflation) · honest‑unresolved ratio · dependency‑graph comprehensiveness (M26) ·
reference‑landscape completeness (S1, feeding P1).

## L7 · The Registry Join Layer  — *accessions/registrations become verifiable join keys*
*(winner: **Registry Join Layer v2**, pinned‑resolver manifest + coverage‑complete claim→outcome links)*

**Problem it kills.** Real, resolvable ids (`NCT#`, `CRD#`, `GSE#`, `phs#`) are trapped in prose, unlinked
to any claim, never checked against the issuing registry — so a well‑formed fake passes like a real one and
outcome‑dropping hides in the gap between registered and reported.

**Design.** `registry/accessions.yaml` is a deduplicated manifest with an **immutable verbatim snapshot**
of each registered outcome and a `VerificationRecord` (hashed, dated, re‑checkable, independently produced).
`access_tiers.yaml` replaces the prose access sentence with a per‑component typed, liveness‑checkable object
(processed=open, raw=controlled/dbGaP). `claim_registry_links.yaml` is the **missing join key**: every
`C##` appears **exactly once** (a silently missing claim is a coverage failure, not honest absence), tying
it to a specific registered `outcome_id` with a **structured `planned_direction`/`planned_measure`** so
direction‑switching is detectable. The correspondence verdict (`matches` vs `outcome_switched`) carries a
mandatory `CorrespondenceAssessment` whose assessor **must be provably independent of the authoring
compiler** — the machine‑comparable prefilter is separated from the semantic label.

**Reliability / protocol:** pinned resolver lock (`resolvers.lock`, referenced by hash) so two labs get
the same topic‑match score; verification freshness/channel strength as first‑class fields; prospective‑vs‑
retrospective registration flagged.

**Metrics unlocked:** registry existence & topic binding (accession *is* real and about *this* paper) —
**the most Goodhart‑resistant metric we have** · join‑coverage completeness · **selective‑reporting /
publication‑bias index** (M04, registered‑but‑unreported) · direction‑switch detection · access‑tier
fidelity · verification freshness.

## L8 · The Delta‑Anchor Ledger  — *structured inputs that make novelty scorable*
*(winner: **DAL/2**, precedence‑anchored, compiler‑computed, dual‑rater)*

**Problem it kills.** A novelty judge needs three things the artifact never stores: what *kind* of
contribution this is, how *big* the claimed improvement is over *named* prior work, and a temporally
honest neighborhood to judge against.

**Design — three small, jointly‑referenced, prose‑renderable sidecars:**
- `logic/contributions.yaml` — each contribution typed **twice** (author‑framed vs compiler‑assessed) from
  a closed taxonomy; divergence is a signal, not an error.
- `logic/delta_ledger.yaml` — "we improve on prior work" becomes a **joinable, source‑verified computation**:
  which prior work (`RW##` from L6), which number on each side (`Q##` from L1), the arithmetic done by the
  compiler and re‑checkable.
- `logic/sota_anchor.yaml` — the externally‑resolved citation + kNN neighborhood, **frozen at the paper's
  externally‑timestamped precedence date** (not the author‑movable pub date), via dual resolvers.

**Metrics unlocked:** delta‑computability rate · baseline‑verification rate · contribution‑typing
inter‑rater κ · anchor reproducibility (resolver‑overlap Jaccard) · **missed‑prior‑work signal** (uncited
contemporaneous neighbors) · suppressed‑comparison flags · precedence‑verification rate.

---

# TIER C — Judgement protocols (Class C: reproducible, not deterministic)

The irreducible questions — is it novel, does it truly hold, is it realistic, how far from optimal. No
format change makes these deterministic. GRO instead makes them **reproducible and auditable**: they read
the deterministic graph, they *never author* it, and their verdicts live in append‑only content‑hashed
logs. The shared machinery across all four:

- **The judge only ever sees a mechanically‑assembled packet** (a pure join over Tiers A/B), never raw
  prose — minimizing its degrees of freedom.
- **Confidence is ensemble agreement, never self‑report.** ≥5 judges across ≥2 vendors + ≥1 red‑team.
- **The authoritative score is the hash of an archived reasoning transcript**, not a re‑inference result;
  re‑running is a **drift audit** within a bounded tolerance (hosted LLMs are non‑deterministic — batching,
  MoE, float non‑associativity — so "re‑run reproducibility" is measured as *invariance under
  semantically‑inert perturbations*, not byte‑identity).
- **Calibration is a first‑class, versioned, shared artifact** with a public frozen anchor set (for
  developing/freezing prompts) and a private *rotating blind* set (to catch overfitting), publishing
  per‑discipline MAE/ICC against human experts.
- **`contested` is a first‑class disposition**, scored as a floor (never worse than not‑supported), so
  manufacturing ambiguity buys nothing.

## P1 · Calibrated Novelty & Significance  *(winner: **LENS‑ON‑ARA/2**; runner‑up **LENS‑ARA/CAL**)*

Consumes L8 (the paper's own contribution claim) + L6 (an independently‑resolved, publication‑time‑pinned
SOTA neighborhood — so "done before?" is judged against the field, not the author's citations). A
version‑pinned ensemble produces balanced for/against arguments **grounded in anchor ids**, a
discipline‑normalized 0–100 with a three‑term confidence interval, and diagnostic flags
(neighborhood‑steering, undisclosed‑prior‑art, author‑citation‑overlap). A **comparator‑completeness rule**
prevents cherry‑picking the field; the **run count is pre‑registered and sealed by hash before the first
run**; an **isotonic calibration curve** maps raw ensemble scores to a funder‑defensible 0–100.
**Afforded:** the entire novelty/significance axis (S1/S2/M07/M17/M24/M34) — the thing that lets a funder
tell *new and important* from *merely competent*.

## P2 · Typed‑Rubric Entailment  *(winner: **TREV/2**; runner‑up **Entailment Court v2**)*

Tries every claim↔experiment↔evidence edge (L4) like a case. An `ENTAIL_PACKET` is assembled by a
mechanical join over L2 (typed claim) + L4 (structured correspondence) + L1 (quantities) — no LLM at
assembly. A **type‑conditioned rubric** (causal→ablation, generalization→heterogeneous data,
improvement→baseline…) drives coverage; **planted‑negative gating** catches rubber‑stamping;
**invariance audits** (paraphrase variants, quantity‑row shuffles, panel‑order permutations) measure real
reproducibility. **Afforded:** D1 evidence relevance · D3 scope calibration / over‑claiming · S4/M19/M49
claim↔experiment↔evidence entailment quality — the "is the argument actually supported" verdict.

## P3 · Realism & Validity Dossier  *(winners: **Realism & Validity Dossier** + **Realism Ledger/AMVP**)*

Turns constraints.md prose into a typed assumption→consequence→failure‑mode→applicability graph, with an
explicit **reference‑prior anchor** (`domain_priors.yaml`) so "is this realistic?" is scored against
declared domain baselines, not judge intuition; **stress probes** with breakpoints *declared before
judging*; a `perspectives.yaml` lens registry making multi‑perspective adequacy checkable; and a calibrated
validity panel. **Afforded:** S7/M30 assumption realism & fairness · M31 limitation validity · S8/M32/M35
method validity & verification status · M36 multi‑perspective adequacy.

## P4 · Frontier & Triangulation  *(winners: **FrontierTriangulation Ledger** + **FLCG**)* — the frontier

Makes two never‑before‑measurable signals explicit. **Distance‑from‑optimum:** a heuristic's reference
frontier is a **tagged union keyed by evidentiary tier** (measured ablation > external benchmark >
theoretical bound > argued > n/a) — distance is only ever as precise as its cheapest verifiable anchor, so
you can't fake precision. **Triangulation:** `perspectives.yaml` makes a "lens" a first‑class id‑joined
object, and corroboration = **independence × agreement** (do the lenses genuinely differ on controlled
axes, *and* do their produced quantities concur), separating real triangulation from mere repetition.
**Afforded:** M39 heuristic distance‑from‑optimum · S6/M36 multi‑perspective triangulation strength.

---

## 2. The metrics catalogue — what we can now measure about good science

Organized by the merged‑doc metric families, tagged with the affording layer and its rigor class.
**D = deterministic · A‑R = reliable‑anchored · R‑J = reproducible‑judged.**

| Metric family (from the merged suite) | Afforded by | Rigor |
|---|---|---|
| Numeric grounding fidelity (value∈quote∈source) | L1 (+independent audit) | D→A‑R |
| Cross‑layer numeric reconciliation, self‑consistency recompute | L1 × L4 | D |
| FOL‑ability (M09, Oshima) | L2 | D |
| Claim↔claim contradiction (M08) — symbolic + numeric | L2 (+CK gate) | D |
| Over‑claiming / scope calibration (D3) | L2 populations × P2 | D + R‑J |
| Claim‑type↔experiment‑design adequacy (D1 selector) | L2 × L4 | D |
| Claims↔concepts consistency (M13) | L2 × L3 | D |
| Controlled‑vocab / latent anchoring (M10/M12/M64) | L3 | A‑R |
| Cross‑layer alignment coverage / testability (M15/M50/M51/M57) | L4 | D |
| Honest‑absence vs lazy‑omission, article‑type (M02, genre floors) | L5 | D |
| Reference‑landscape completeness (S1/M14/M16/M40) | L6 | A‑R |
| Claim‑drift / reference truthfulness (S3/M18/M23) | L6 support edges × P2 | A‑R + R‑J |
| Citation dedup / anti‑count‑inflation, dep‑graph (M26) | L6 | D + A‑R |
| Registry realness & topic binding (genre‑scope fidelity) | L7 | A‑R |
| **Publication‑bias / outcome‑switching (M04)** | L7 × L1 registry_ref | A‑R |
| Access‑tier fidelity | L7 | A‑R |
| Contribution typing, delta magnitude, missed‑prior‑work | L8 | D + A‑R |
| **Novelty & significance, calibrated (S2/M07/M17/M24/M34)** | P1 on L6+L8 | R‑J |
| Entailment quality / evidence relevance (D1/S4/M19/M49) | P2 on L1+L2+L4 | R‑J |
| Assumption realism, method & limitation validity (S7/S8/M30‑35) | P3 | R‑J |
| Heuristic distance‑from‑optimum (M39) | P4 | A‑R + R‑J |
| Multi‑perspective triangulation (S6/M36) | P4 | D (structure) + R‑J |
| Exploration/dead‑end integrity (D5/M41/M42/M47) | L4 tree edges + verdict log | D + R‑J |
| Reproducibility bundle: fig+data+code+protocol (S5/M48) | L1×L4×L7 + artifacts | D |

The recurring anti‑Goodhart posture across the catalogue: **length never scores** (every metric is a
ratio or a join, not a count of prose); **fabrication has an independent second checker** (extraction
audit, blind classifier, independent correspondence assessor, dual resolvers); **honest absence is scored
equal to honest presence**; and every self‑certifiable field is split into a deterministic axis plus an
independently‑produced one.

---

## 3. Governance — why the numbers are trustworthy

1. **Honest‑absence symmetry, everywhere.** `not_specified` / `not_applicable` / `unresolved` are
   first‑class values scored *equal* to an honest presence. Typed slots never create fabrication pressure.
2. **Deterministic/semantic separation is physical.** Judgements can't leak into the computable core; they
   live in append‑only, content‑hashed, judge‑authored logs that reference the graph by id.
3. **Everything external is pinned.** Resolvers, blind classifiers, judge ensembles, and calibration sets
   are versioned, hash‑referenced ecosystem artifacts — two labs re‑running get the same inputs, and drift
   is measured, not assumed away.
4. **Independence is engineered.** The compiler that authors a fact never certifies it: extraction
   fidelity, genre classification, registry correspondence, and novelty are produced by *different*
   agents/passes, often adversarial (red‑team judges, planted negatives).
5. **Absence must be accounted for, not skipped** — the one ARA principle GRO keeps verbatim, now made
   mechanically checkable by L5's expectation ledger.

---

## 4. The funder‑facing output — the Credibility Dossier

A GRO reduces, for a program officer, to one decomposed decision object — **never a single collapsed
number** (per‑layer resolution is the whole point):

```
GRO://che26-diagnostic-performance-of-plasma-p-tau217
├─ Integrity (Tier A, deterministic)      ● grounding 0.98 · reconciliation pass · 0 contradictions · over-claim 0.04
├─ Anchoring (Tier B, reliable)           ● 100% refs resolved · registry verified · 0 outcome-switches · access tiers honest
├─ Novelty & significance (Tier C)        ● 71/100  [CI 63–78]  (discipline-normalized; for/against grounded in RW ids)
├─ Support quality (Tier C)               ● entailment 0.86 · 1 contested edge · calibration-trusted
├─ Validity (Tier C)                      ● assumptions realistic (2 flagged) · single-perspective (declared)
└─ Honesty ledger                         ● 0 lazy omissions · 3 honest not-applicable · 2 disclosed data-quality caveats
```

Each dot is drillable to its evidence: the anchor, the quote, the judge transcript hash, the calibration
epoch. A funder can **rank a portfolio on the novelty+significance axis, gate on integrity+anchoring
floors, and read support/validity as risk** — and can *audit any score to its source*. That is the whole
proposition: fund the important work, defensibly.

---

## 5. Migration — from today's papers to GRO

GRO is designed to be reachable, not utopian:

1. **Compile, don't demand.** The existing ARA compiler already extracts most of these facts as prose; GRO
   is a **typed sidecar** emitted alongside the prose (`quantities.yaml`, `entities.yaml`, `refs.yaml`,
   `edges.yaml`, `genre.yaml`, the `logic/*` FOL blocks). Prose renders from — or round‑trips against — the
   sidecar, so nothing human‑readable is lost.
2. **Tiers light up incrementally.** Tier A works on any paper today (deterministic, offline). Tier B
   switches on as the ecosystem provides pinned resolvers over OpenAlex/S2/GEO/dbGaP/PROSPERO. Tier C
   switches on as calibration sets are curated per discipline.
3. **Backfill vs. native.** Legacy PDFs get a best‑effort compile with fidelity flags; **native GRO
   submission** (authors publish the sidecars + all artifacts) is the target state and the thing a funder
   or venue can eventually *require*.
4. **The ecosystem's to‑do list** (what must exist for Tier B/C reliability): versioned predicate & entity
   vocabularies, a paper‑type taxonomy, an edge schema, pinned resolvers with index snapshots, per‑discipline
   human calibration sets, and a commons for cross‑ARA entity/reference binding.

---

## 6. Coda — what becomes fundable

When the record computes its own credibility, the questions we currently answer with proxies become
first‑class measurements. We can ask *of a hundred‑thousand‑paper corpus*, deterministically or
reproducibly: which claims are grounded to source; which are novel against the field at their own
publication moment; which trials switched their outcomes; which methods rest on realistic assumptions;
which dead ends are documented well enough to save the next lab the failure. We can fund the work that is
**both** rigorous **and** important — and show our work. The current substrate can't support that. GRO is
the shape that can.

---

## Appendix · Provenance & method (how this spec was produced)

- **Gap source:** `AFFORDANCE_GAP.md` — the 12 gaps between the ideal metric suite (`ALL_METRICS_MERGED.md`,
  four merged sources) and the current ARA output shapes (`DATA_SHAPES.md`, `ara-schema.md`).
- **Tournaments:** 12 gaps × {4 proposers (2 GPT‑5.5/Codex, 2 Claude Sonnet) → 1 Fable meta‑science judge
  picking + critiquing the best 2 → refine round where finalists hardened and merged}. Run `wf_f0bc615b-a88`;
  99 agents, ~5.55M tokens.
- **What completed:** all 48 proposals, all 12 judge verdicts, and 10/12 gaps' hardened *v2* finalists.
  VALIDITY and HARDSIGNALS lost their refine round to an account rate limit, so their *judge‑selected
  proposals* are used. The final review gate and the workflow's own synthesis pass were cut off by the
  limit; this spec is the synthesis, authored from the cached finalist designs.
- **Raw designs:** preserved verbatim‑structured in `TOURNAMENT_DESIGNS.md` (one section per gap, both
  finalists, judge critiques).
- **Named designs synthesized here:** CQL‑RAB (L1) · CLF/CK (L2) · Entity Identity Layer (L3) · Edge Ledger
  v2 (L4) · Genre Contract v2 (L5) · Resolved Reference Spine v2 (L6) · Registry Join Layer v2 (L7) · DAL/2
  (L8) · LENS‑ON‑ARA/2 & LENS‑ARA/CAL (P1) · TREV/2 & Entailment Court v2 (P2) · Realism & Validity
  Dossier + AMVP (P3) · FrontierTriangulation Ledger & FLCG (P4).

*To complete the intended pipeline — the adversarial‑critique synthesis pass — resume `wf_f0bc615b-a88`
after the rate limit resets; cached agents replay instantly and only the review + synthesis agents re‑run.*
