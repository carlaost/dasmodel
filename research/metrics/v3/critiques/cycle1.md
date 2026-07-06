# Cycle 1 — Fable metascientist critique of V3 (post-[sem], 4/9 usable state)

Author: Fable metascientist+incentive-designer agent. Verbatim deliverable preserved as the changelog.

## (1) Blunt verdict

V3-with-[sem] is the most honest scaffolding in the project and the most dishonest headline. The
scaffolding — two axes, a variance⟂validity lattice, fabrication detectors, genre ladders, a cached
external harness — is real engineering and should survive. The headline — "**4/9 usable paper-rankers,
3 of them `validated`**" — is theater, and the frozen findings prove it in the system's own words.
`sem_metrics.py` defines `validity="validated"` to mean *"a sem_findings/<slug>.yaml file exists"*
(the judge findings ARE the [sem] pass). That is not validation; it is "an LLM ran." The round-2
BLOCKER RC2 ("validate ≥1 ranker against an external quality signal") has been closed by **renaming "an
LLM judge produced output" to "validated."** Worse, when you read what the three "validated" judges
actually flagged — the25, jes26, huu25 — **every single over-claim/irrelevance they caught is a compiler
transcription error, not a flaw in the paper.** So the three new "usable paper-rankers" are
compiler-fidelity detectors wearing a paper-quality label; they re-import the exact woj25 bug V3 claimed
to have fixed, they double- and triple-count one compiler typo across two axes that are supposed to be
orthogonal, and — the richest irony — **they empirically falsify the compiler-model axiom (C16) that
licenses them to rank papers at all.** Net: the usable count rose from 1 to 4 by adding three metrics
that are invalid for the reason the whole architecture was built to prevent.

## (2) Per-metric gaming analysis

Unifying fact: **every metric is computed over the compiler's output, and there is no source PDF for
most ARAs** — the "source" the judges check against is `research/data/lib/<slug>/metadata.md`, which is
**the abstract plus metadata** (the25's is 837 words; all 7 claims trace to `Abstract FINDINGS`). So the
optimizing agent is not the researcher — it is whoever writes the compiler prompt.

- **evidence_relevance** ✅validated — Compiler-fidelity detector mislabeled paper-quality. All 3 non-1.0
  scores are compiler insertions: the25 (0.29, compiler added "all…at moderate certainty" the abstract
  doesn't grade); jes26 (0.90, compiler wrote "amyloid clearance was maintained" when the paper says it
  **reaccumulates** — an inversion); huu25 (0.88, ungrounded "MAPT downregulated"). Game: tune compiler
  to never add clauses → 1.0 for everyone. Ceiling-pins like V1 falsifiability_presence.
- **scope_calibration** ✅validated — Same event, same three ARAs, double-counted. the25 (0.29) is the
  *identical* insertion already dinged in evidence_relevance. 15 corpus "over_claims" are compiler
  over-generalizations, not author ones.
- **falsifiability_quality** ✅validated — Directly violates the compiler-model's own routing rule.
  "Falsification criteria" is the archetypal *homogenization* field (compiler-authored for every claim);
  Rule 2 says such fields go to trust, never rank papers. "79 post_hoc / 16 real / 5 trivial" is a fact
  about how the compiler writes the field. cum26 (narrative review, no experiments) "wins" SYNTHESIS at
  1.00 with 10 real_precommitted — a genre with nothing to pre-register scoring perfect is the tell.
- **translation_trial_linkage** ✅source_bound — Unnormalized NCT-mention count. cum26=8.0 wins by
  name-dropping trials (the "cite more" behavior the project exists to replace); its top value is the 8
  NCTs its own RC2 harness labels `not_applicable`.
- **novel_claim_count** pending_sem — Raw count, no denominator, no FOL dedup. "Novelty" = how many claim
  blocks the compiler split the abstract into.
- **semantic_grounding** pending_sem — presence≠truth family; huu25 unrankable (bucket=1).
- **negative_result_share** pending_sem — woj25 now 0.375 (good) but huu25=0.5 in a 2-member bucket is
  noise; `_NEG_RE` keyword-gated.
- **dead_end_density** invalid_fabricated — correctly demoted, but huu25 keeps 0.5 stamped `source_bound`
  with no PDF to bind to; detector uses the compiler's own support_level/source_refs (self-referential).
- **corrective_science** invalid_fabricated — 0.0 for all 12; `_CORRECTIVE_RE` structurally pins near
  zero on any corpus. Mirror image of V1 falsifiability=1.0.
- **artifact_trust `w`** — ornamental AND double-books: compilation_fidelity dings the25/jes26/che26 for
  the same compiler errors the paper-axis judges already penalized. Axes not independent.
- **D5 claim graph** — all zeros; FOL pending. Flagship contributes nothing → system is 100% local metrics.
- **external (RC2)** — concordance = a transcription check on the extractive layer C16 already assumes
  faithful. jes26/sal25 "concordant" = compiler copied the numbers correctly, not that the science is good.

## (3) Architecture & incentive-design critique

- **A. "validated" is a lie the lattice tells to pass its own gate.** `usable = discriminating AND
  validity∈{validated,source_bound}`; `validated` = a findings file exists. So the gate = "discriminating
  AND (an LLM ran OR a ref-string exists)" = variance-with-extra-steps. Precisely RC1's "confidently,
  discriminatingly wrong." Rename to `judge_scored`/`internally_consistent`; must NOT satisfy `usable`.
- **B. The [sem] judges falsify the axiom that licenses them.** C16 adopts by fiat that the extractive
  layer is a faithful re-view — the sole justification for ranking papers. The judges found extractive
  infidelity: added clauses, a flipped conclusion (jes26). So (1) the axiom is empirically false here;
  (2) the judges are the compiler QA suite, not paper-rankers. Flip their role → trust axis.
- **C. Two axes that share the same errors are one axis.** the25's one over-generalization moves
  evidence_relevance↓, scope_calibration↓ (paper), AND compilation_fidelity↓→w↓ (trust). The promise
  "artifact quality feeds trust, never paper rank" is violated whenever the flaw is compiler infidelity —
  which here is every flaw found.
- **D. Equilibrium: gamed by prompt-engineering, not science.** Dominant strategy: compiler emits terse
  claims never exceeding a quoted source, template-writes independent-sounding falsification criteria,
  pastes NCT IDs, fills every presence slot. Garbage science + good compiler prompt tops the leaderboard.
  Nine metrics on one gameable substrate = one metric → the diversity defense is void.
- **E. n=12, single-topic, abstract-only is below the floor for every conclusion.** "79% post-hoc" is
  100 criteria the compiler wrote. You cannot assess falsifiability/scope/dead-ends of a *paper* from its
  250-word abstract. Every paper-quality claim here is really an abstract-quality claim.
- **F. Is "ranking papers" even the right frame? No.** The unit that is checkable against external ground
  truth AND Goodhart-resistant is the **claim**, not the paper. Paper-level scalars average over the
  claim-level structure that carries the signal. D5 already points here; the rest points away.

## (4) Ranked problems → directions (feeds next cycle)

- **P1 [BLOCKER] `validated` means "an LLM ran" and satisfies the usable gate.** Rename to `judge_scored`;
  remove from the `usable` set. Reserve `validated` for a measured association to a science-quality signal
  external to the compiler (expert rating, retraction/EoC, held-out reproduction, guideline adoption).
  Honest usable count until then: 0–1.
- **P2 [BLOCKER] The [sem] "paper-rankers" are compiler-fidelity detectors; reroute them.** Move
  evidence_relevance + scope_calibration to the trust/fidelity axis with compilation_fidelity; compute
  ONE compiler-infidelity rate per ARA (stop triple-counting). Restores axis orthogonality.
- **P3 [BLOCKER] The compiler-model axiom (C16) is empirically false on this corpus.** Demote C16 from
  axiom to measured quantity. Compute extractive-fidelity per ARA vs the source PDF. No metric ranks
  papers on a layer whose fidelity is below threshold; if unmeasurable (no PDF) → `unverifiable`, not
  `validated`.
- **P4 [HIGH] No source PDF; the system scores abstracts.** Acquire full text (PubMed
  `get_full_text_article` / bioRxiv PDFs — live MCPs) and re-ground judges against the paper. Rename
  `source_bound`→`ref-string-bound` until a real source backs it. Abstract-only ARAs barred from
  paper-quality ranking.
- **P5 [HIGH] Restructure from paper-rankers to a claim graph with external anchors.** Make the claim the
  unit. Build the FOL/claim-cluster graph; anchor with live MCPs: ChEMBL target/compound resolvability,
  CT.gov endpoint concordance per-claim, PubMed/bioRxiv novelty-vs-prior-literature. A claim corroborated
  by N independent ARAs and concordant with a registered endpoint is Goodhart-resistant. Only direction
  that measures science, not compiler behavior.
- **P6 [HIGH] falsifiability_quality ranks compiler-authored text; retire as paper-ranker.** Route to
  trust as "compiler falsification-writing quality," OR only score where the author pre-registered
  (PROSPERO/CT.gov protocol), extracted from the registry not the compiler. cum26=1.00 proves it measures
  the template.
- **P7 [MEDIUM] Kill trivially-pinned metrics honestly.** corrective_science is regex-pinned near 0 on
  any corpus — retire or rebuild as a claim-graph `contradict`-edge count (P5). translation_trial_linkage
  rewards name-dropping and its top value is `not_applicable` — give it a denominator (the paper's own
  subject trial only) or retire.
- **P8 [MEDIUM] The judges are unvalidated instruments; validate the validators.** Inter-rater
  reliability (2+ models, or model-vs-hand-label on a 20-claim gold set); report κ before any judge
  output counts. Project's own trace (N12/N13) documents LLM-judge grade inflation.
- **P9 [MEDIUM] CI / power discipline on all corpus numbers.** Attach applicable-n and a bootstrap CI (or
  "too few to rank") to every headline; stop reporting n=2 pairwise buckets as rankings.

**Bottom line:** Cycle 0's [sem] pass added three compiler-QA signals mislabeled `validated` — the
round-1/round-2 disease with a new coat of paint. Productive next cycle: P1–P3 (stop the mislabeling,
reroute the fidelity metrics, demote the axiom), then P4/P5 (real full text; move to a claim graph
anchored on the now-live external MCPs). Keep the scaffolding; the leaderboard is not yet measuring science.
