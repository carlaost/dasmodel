# Ongoing critique — good-science metrics over the ARA library

A running, adversarial review of `metrics-directions.md` and the computed `/metrics` layer.
Append new entries at the top under a dated heading. The job of this doc is to be the harshest
honest reader in the room: why a metric is **bad**, **not useful**, or **nothing new**.

Companion records in the ARA trace: `research/ara/staging/observations.yaml` (O04–O11+),
`research/ara/trace/exploration_tree.yaml` (N27 = the metrics question, N30 = the wave-1 run).

---

## 2026-07-05 — Deep critique of the wave-1 run (10 AD-biomarker ARAs)

Sources read: `metrics-directions.md`, `research/metrics/compute_metrics.py`, the wave-1 outputs
(`library_metrics.md`, `coverage-gaps.md`), both founding essays, and the compiled ARAs directly
(che26 full claims/related_work/trace, woj25 claims, per-ARA `metrics.json` for all 10).

**One-line verdict.** The *framing* (many independent, structure-derived signals; reward what
citations punish) is genuinely good. The *metrics as built* mostly measure **compiler
template-compliance**, and the corpus they ran on is structurally incapable of testing whether they
mean anything.

### 1. The system Goodharts itself — the exact failure it claims to defend against

- **`falsifiability_presence = 1.0` for every claim, all 10 ARAs** (mean=median=min=max=1.0). The
  "Falsification criteria" field holds mechanical post-hoc inversions the compiler wrote, not
  pre-committed criteria. che26 C01: *"Refuted if p181_IA outranked p217_MS."* Any claim inverts
  this way, so the metric is pinned at 1.0 by construction. It measures whether a text field is
  non-empty — the textbook gamed proxy.
- **`claim_grounding_ratio` measures the `«…»` quote syntax, not grounding.** woj25 scores **0.0**
  yet is one of the *better*-sourced papers (exact AUCs/CIs/Cohen's d + figure/table pointers in its
  Evidence-basis prose) — it just didn't use the quote wrapper. A well-sourced paper is penalized
  for a formatting choice; a paper that quotes a caption around a meaningless number would score
  well. (Note: even at 1.0 this only proves a quote is *present beside* a number, not that the quote
  is real or supports it — presence ≠ verification.)

### 2. The "negative knowledge" direction (D3) — the self-declared unique differentiator — is fabricated or blind

- **Dead-ends are compiler-manufactured.** che26 is a network meta-analysis with no exploration
  process of its own, yet its trace carries `dead_end` nodes N11/N12 with straw hypotheses
  (*"p-tau181 would remain competitive"*) reformatted from the paper's conclusions. Nobody held and
  abandoned those hypotheses. `dead_end_density` — the D3 anti-Goodhart crown jewel — measures the
  compiler's creative writing, and directly violates the doc's own "no synthetic trace history" rule.
- **The metric can't see the one real negative result in the corpus.** woj25 C04 is a genuine null
  (*"plasma p-tau181&231 fails to differentiate, Cohen's d<0.2, AUC 0.514"*). Its `Status` is
  **`supported`** (the claim that it *fails* is supported). `negative_result_share` counts
  `status: refuted`, so it scores this real negative as **zero** negative-knowledge while crediting
  the fabricated dead-ends. The metric is anti-correlated with its own name.
- **`status_honesty_mix` flags genre, not honesty.** ~100% `supported` across all 10. The doc calls
  that "a red flag"; it's a tautology of publishing. The metric flags *every* corpus of published
  literature, discriminating nothing.

### 3. `corrective_science_score` (D4) rewards the opposite of what it claims

- **`refutes = 0` across all 10 ARAs** — not one refutation edge in the corpus. The score
  (mean 4.6, max 12 for jes26) is driven entirely by `bounds` (14) + `extends` (11), and "bounds"
  tags ordinary baseline-beating: che26 RW14 marks p-tau181 (the prior standard the review improves
  on) as "bounds." The metric built to reward rare, high-value refutation instead rewards the
  citable "we beat the prior method" behavior the founding essay criticizes citations for.

### 4. Everything is measured on the compiler's reconstruction, not the science

`cross_layer_binding_resolvability` (0.99), the trace-derived D3 metrics, and D7 all read files the
compiler wrote. High binding = the compiler kept its own pointers consistent. High branching = the
compiler enumerated alternatives. The doc's own cited failure modes (L2 misses 78% of orphans; LLM
judges inflate grades — N12/N13) apply to this very substrate. `compilation_fidelity`, the proposed
fix, is another LLM judging the LLM. No layer is anchored to ground truth — a hall of mirrors.

### 5. The flagship (D5) is vaporware at this scale

Computed D5: **0 shared-trial clusters, 0 citation-reuse edges, 0 near-duplicates, FOL graph
`pending_model`.** Every number zero or absent. The real version needs the oshima typed-claim/FOL
store, which the coverage doc admits doesn't exist for compiler-ARAs. And the merge threshold τ *is*
the metric — corroboration/redundancy/confidence all swing on it — yet it's filed as an "open
question." Calling the claim-normalization problem a parameter doesn't solve it.

### 6. Nothing new — and the incumbents are validated

Stripped of ARA vocabulary these restate existing meta-science, often weaker: D1 spec-completeness
= PaperBench / ML-repro checklist / CONSORT / STARD / TRIPOD; D2 = SciScore / statcheck / GRIM /
Ripeta; D4 typed edges = CiTO/SPAR + scite.ai (deployed at 100M-citation scale); D5 claim graph =
ORKG / nanopublications / SemMedDB; D6 = Open Targets / trial-linkage mining. The incumbents ship
with construct-validation studies. These ship with none.

### 7. No validation, and a corpus that makes validation impossible

- **Not one metric is checked against an external quality signal** (expert rating, held-out
  reproduction, retraction). "Hard to fake without doing the good-science thing" is untestable
  hand-waving until a metric is shown to move with the good-science thing.
- **The corpus pins the interesting metrics to zero.** All AD blood-biomarker reviews/trials/
  guidelines: 0 code, request-only data. So D1-L3 (the "hardest to fake" metric), D3 (the "unique"
  one), and D5 (the flagship) are all N/A or zero. O04 already concedes the only discriminating axis
  here is grounding + trial-linkage — i.e. a ClinicalTrials.gov lookup. The exercise can neither
  succeed nor fail; it just produces numbers.

### Bar for making this defensible (not fixing now — just the bar)

1. Corpus with runnable code + replication pairs so D1-L3 and D5 aren't dead on arrival.
2. Validate ≥1 metric against an external quality signal.
3. Compute grounding/falsifiability/dead-ends against **source PDFs**, not the compiler's YAML.
4. Drop or rethink `falsifiability_presence` and `status_honesty_mix` — constant across all real
   literature, discriminate nothing.
5. Stop calling compiler-manufactured dead-ends "preserved failure knowledge."

**Credit where due:** `coverage-gaps.md` and observation O04 already document most of this honestly.
The gap is that the main doc still sells the directions as a working citation-alternative when the
run shows two-thirds of them produce zeros or artifacts on real data.

---

## 2026-07-05 — Round-2: critique of the V2 redesign

Reviewed `research/metrics/v2/` (compute_metrics_v2.py, library_metrics_v2.md, comparison_v1_v2.md),
the per-ARA `metrics/v2/metrics.json`, and the crystallized heuristics H01–H05. Full per-response
rebuttal is inline in `metrics-directions.md` → "Round-2 critique of the V2 responses". Summary:

**V2 fixed (surface):** gates-vs-rankers split (real improvement); verified grounding replaces
presence-only for the 4/10 ARAs where quotes cite in-repo files; a discrimination diagnostic that
honestly flags non-informative rankers.

**V2 did not fix (the parts that mattered):**
- Fabricated dead-ends survive — che26 still scores `dead_end_density=0.25` / `negative_result_share=0.2`
  entirely from the compiler-invented straw dead-ends N11/N12, now *certified* "discriminating".
- `corrective_science_score` still `refutes=0` library-wide, still bounds/extends baseline-relabeling.
- woj25 C04 (real null) still `status: supported` → still invisible to negative-result share.
- **No external validation.** The discrimination diagnostic measures variance, not validity — it
  greenlights the fabricated metrics because compiler artifacts vary. Confidently, discriminatingly wrong.
- Everything still computed from the compiler's YAML, not the source PDFs.

**V2 introduced new problems:**
- `paper_quality` vs `artifact_quality` is a label only — every ranker is tagged `paper_quality`,
  including compiler-determined ones.
- Genre classifier is brittle first-match keyword matching, already **wrong for cum26** (pipeline
  review labeled `clinical_trial`).
- Genre-split atomizes 10 papers across 6 genres into **singletons** → within-genre ranking is unrankable.
- Verified grounding is computable for only **4/10** (rest cite paper.pdf/§) and only checks the quote
  *string exists*, not that it supports the number/claim — "presence≠truth" narrowed to
  "quote-string-in-file≠truth".
- Crit-#5 clinical spec rubric is listed as a delivered fix but spec-completeness was **dropped**, not
  reimplemented — vaporware in the response table.

**Verdict:** a competent, honest engineering reshape that makes the system admit more of what it can't
do, but a better-instrumented way to measure the same wrong thing. The round-1 prerequisites stand:
validate ≥1 ranker against an external signal; compute against source PDFs; use a heterogeneous
code-shipping corpus; add a validity check, not just a variance check.

---

## 2026-07-05 — Round-3: critique of the V3 redesign

Reviewed `research/metrics/v3/` end to end: `compiler-model.md` (the adopted C16 axiom), `v3-spec.md`,
`detectors.py` (the RC3/4/5 code), `comparison_v2_v3.md`, `library_metrics_v3.{md,json}`, and the cached
external-validation payloads. V3 delivers what the spec promised — two axes, a validity-vs-variance
lattice, genre ladders, fabrication detectors, a real ClinicalTrials.gov lookup — and it is a real
integrity gain over V2. But the apparatus that produces the "1/5 usable" headline does not survive its
own evidence. New findings, not restatements of rounds 1–2:

### 1. The one surviving ranker is a citation-counter, and its top value is thrown out by its own validator

`translation_trial_linkage` is the sole "usable" paper-ranker — and it is an unnormalized count of NCT
mentions. In the SYNTHESIS bucket **cum26 wins at 8.0** (vs 0.0 for che26/pal25/the25) purely because a
drug-pipeline review name-drops eight trials. That is exactly the "cite more" behavior the founding
essay set out to replace, now crowned as the project's one validated signal. Worse: the RC2 harness
labels those **same eight NCTs `not_applicable`** ("landscape citations, not the paper's own subject
trial"). So the ranker's headline value is precisely the value its validator discards. "1/5 usable"
overcounts — the 1 reduces to "count trial IDs in the free text," and its largest score is unvalidatable
by construction.

### 2. The one genuinely-external signal validates compiler fidelity, not good science

RC2's ClinicalTrials concordance (jes26, sal25 → concordant; aggregate 0.667, n=4) checks whether the
ARA's headline number matches the trial registry's posted primary endpoint. That is a **transcription
check on the extractive layer** — the exact layer `compiler-model.md` already *assumes* faithful (C16).
Confirming donanemab's ARA copied "−10.6 vs −13.0" correctly tells us the compiler read the number right;
it says nothing about whether jes26 is good science (the science lives in trial design, not in
registry-vs-ARA number agreement). The flagship "first external signal" therefore corroborates the axiom
V3 granted itself, not the claim that any metric tracks quality. External-but-wrong-axis.

### 3. Not one ranker reaches `validated` — the validity gate only ever prints "unknown"

The lattice has five verdicts. Across all 12 ARAs the rankers populate only `invalid_fabricated`,
`pending_sem`, and (for trial-linkage) `source_bound`. **Zero rankers reach `validated`.** The RC1
validity axis — the round-2 BLOCKER — is a well-engineered mechanism whose only outputs on this corpus
are "fabricated" and "not checked." Substantively that is the V1/V2 result: no metric is shown to measure
anything. V3's advance is that it now says so in a typed field instead of a green checkmark.

### 4. The detectors fight fabrication using other fields of the fabricated layer

RC3 decides genuine-vs-synthetic from the compiler's own `support_level`, `source_refs`, and `hypothesis`
wording (`detectors.py:_classify_dead_end`). But a compiler that fabricates a dead-end also writes those
three fields. A synthetic node dressed with one methods-section ref and a hypothesis lexically distinct
from the headline (Jaccard < 0.22) passes as **genuine**. The detector trusts compiler metadata to catch
compiler invention — self-referential. The genuine/synthetic split is never checked against the paper;
it is a re-partition of the same untrusted YAML.

### 5. "source_bound" overclaims — it means "compiler-ref-string-present," verified against nothing

huu25 keeps `dead_end_density = 0.5`, stamped **`source_bound`** ("bound to real author-documented
failure"). But `v3-spec.md` records huu25's **PDF is missing**. The binding to a real author-reported
failure is therefore literally uncheckable — "source_bound" here is asserted from the compiler's
`source_refs` strings alone. This is the round-1 presence≠truth bug at one remove: *ref-string-exists ≠
ref-is-real*. The verdict name promises source-grounding the pipeline never performed.

### 6. RC4 is dead by construction, not just on this corpus

`corrective_science` can only fire if the compiler's `Delta` prose literally contains
`contradict|fails to replicate|overturn|refut|revises down|…` (`detectors.py:_CORRECTIVE_RE`). It is
keyword-gated on the compiler's vocabulary in a free-text field. Real corrective work phrased any other
way scores 0. So `0.0 across all 12` is not only "this literature does little corrective work" (the doc's
read) — the metric would read ≈0 on almost **any** corpus, because it matches a handful of exact rare
phrases. A metric that is structurally pinned near zero discriminates nothing, the mirror image of V1's
`falsifiability_presence` pinned at 1.0.

### 7. The rankings that remain are mostly ties and provisional buckets

`corrective_science_score` = 0.0 for all 12 — a "ranking" of universal ties. Every genre-scoped ranking
except one (`diagnostic_accuracy_study`, n=3) is tagged `coarse_provisional` or `pairwise_caveated`, and
inside the one real bucket the rankers are {one nonzero, two zeros}. K_MIN=3 is honest, and what it
honestly reveals is that **12 papers cannot be ranked within genre at all.** The genre ladder is
machinery for admitting the corpus is too small, which is the same message as the empty validity column.

### 8. The trust-weight `w` is ornamental

`w` (0.599–1.0, geometric mean of presence components) is computed and reported per ARA, but no
library-level aggregate in `library_metrics_v3.json` actually consumes it, and the RC10 invariance test
(two ARAs identical but for `environment.md` → same rank, different `w`) is asserted in the spec, not
demonstrated in the output. Right now `w` is a number that scales nothing.

### 9. Meta: the apparatus confirmed a pre-registered verdict without testing itself

`v3-spec.md`'s standing verdict predicted "~0–1 paper-rankers survive" **before any V3 code was written**,
and `compiler-model.md` adopts the faithful-extractive axiom **by fiat** ("a design contract, not a
validated fact"). V3 then built detectors, a lattice, ladders, trust weights, and an external harness —
and landed exactly on the pre-registered number. That is honest, but it means the loop validated its own
prediction, not the metrics. And the price was **new unvalidated knobs**: the Jaccard=0.22 mirror
threshold, the SYNTHESIS ≥2-ref rule, `_CORRECTIVE_RE`, `_NEG_RE`, the geometric-mean `w`, K_MIN=3 —
none checked against ground truth. Round-1's "τ *is* the metric" (D5) has multiplied into six τ's. The
count of confidently-wrong numbers went down; the count of hand-tuned, unvalidated heuristics went up.

**Credit where due (kept, don't relitigate):** the two-axis routing (never rank on homogenized presence
fields) is a genuine conceptual fix; separating variance from validity is correct and should stay;
stripping the fabricated che26 dead-ends and reporting an honest 0.0 corrective score is real integrity;
caching the ClinicalTrials JSON for reproducibility is good practice.

**Verdict:** V3 is the most honest version yet and the best-instrumented — and it demonstrates, more
cleanly than V1/V2, that there is nothing here to measure *on this corpus*. Every load-bearing result is
either fabrication-stripped to zero, pinned near a constant, tagged `pending_sem`, or — for the single
survivor — a citation count whose top value its own validator rejects. The bar is unchanged and now
sharper:

1. Heterogeneous, code-shipping, replication-paired corpus (still the precondition for D1-L3 and D5).
2. Validate a ranker against a signal that is about **science quality**, not transcription fidelity —
   ClinicalTrials number-matching does not count.
3. Compute the detectors' genuine/synthetic and negative-result labels against **source PDFs**, and
   rename `source_bound` to what it is until then (`ref-string-bound`).
4. Validate the new heuristics themselves (the six knobs above) before trusting the residue they leave.
5. Either give `translation_trial_linkage` a denominator that stops rewarding trial name-dropping, or
   retire it — a citation counter is not the citation-alternative this project is for.
