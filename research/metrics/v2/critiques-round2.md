# V2 critiques — round 2 (actionable backlog for V3)

Reviewer's round-2 findings on the V2 redesign (`compute_metrics_v2.py`), logged as an iterable
backlog. Each item: **finding → evidence → required fix → acceptance criterion**. Work top-down;
severity order. Prose rationale lives in `metrics-directions.md` ("Round-2 critique of the V2
responses") and `../../../metrics-critique.md`; staged as observations O15/O16 in
`research/ara/staging/observations.yaml`.

Status legend: `open` · `in_progress` · `done` · `wontfix`. Target = the V2 piece to change.

---

## RC1 — Discrimination diagnostic measures variance, not validity  · severity: BLOCKER · status: open
- **Target**: `discrimination()` + H05.
- **Finding**: The diagnostic greenlights a metric as `discriminating` purely because it *varies*, with
  no check that the variation is *real*. It therefore certifies the fabricated/blind metrics
  (`dead_end_density`, `corrective_science_score`, `negative_result_share`) as "discriminating." A
  metric can be confidently, discriminatingly wrong.
- **Evidence**: `library_metrics_v2.md` marks all three `discriminating` while RC3/RC4/RC5 show each is
  driven by compiler artifacts.
- **Fix**: Add a **validity axis** orthogonal to variance. A ranker may not be presented as usable
  unless it passes a validity check (RC2) *and* has variance. Report `{variance_verdict, validity_verdict}`.
- **Acceptance**: No ranker shows a bare "discriminating" verdict; each carries a separate validity
  status, and the three artifact-driven rankers cannot read as usable until their validity item is fixed.

## RC2 — No external validation of any ranker  · severity: BLOCKER · status: open
- **Target**: whole V2 scoring model.
- **Finding**: Nothing checks any ranker against an independent quality signal, so "good-science metric"
  is an assertion. Variance ≠ correctness.
- **Fix**: Validate ≥1 ranker against an external signal — expert quality ratings, held-out reproduction
  outcomes, or known retractions/expressions-of-concern. Report the correlation.
- **Acceptance**: At least one ranker has a documented association with an external quality label on a
  held-out set; the doc states the correlation and n.

## RC3 — Fabricated dead-ends counted as real negative knowledge  · severity: HIGH · status: open
- **Target**: V1 `parse_tree`/D3 dead-end counting, consumed by V2 `dead_end_density` + `negative_result_share`.
- **Finding**: Review/meta-analysis ARAs have no exploration process, yet the compiler manufactures
  `dead_end` nodes with straw hypotheses reformatted from the paper's *conclusions*, and V2 counts them.
- **Evidence**: che26 (meta_analysis) `dead_end_density=0.25`, `negative_result_share=0.2`, both entirely
  from compiler-invented nodes N11/N12 ("p-tau181 would remain competitive").
- **Fix**: Count only dead-ends that bind to real author-documented failure (source_refs to the paper's
  own reported negative/abandoned attempt), not compiler-reframed conclusions. Add a synthetic-dead-end
  detector (hypothesis is a negation of a headline finding + no independent source_ref ⇒ exclude).
- **Acceptance**: che26 dead_end_density → 0 (no genuinely-authored dead-ends); only source-bound dead-ends survive corpus-wide.

## RC4 — corrective_science_score rewards baseline-relabeling (refutes=0)  · severity: HIGH · status: open
- **Target**: V1 D4 `corrective_science_score`, surfaced as a V2 ranker.
- **Finding**: `refutes=0` across all 10 ARAs; the score is driven by `bounds`/`extends`, and `bounds`
  tags ordinary "we improve on the prior standard" (a baseline), not corrective refutation.
- **Evidence**: lib-wide RW types = 34 imports / 14 bounds / 11 extends / 9 baseline / **0 refutes**;
  che26 RW14 tags p-tau181 (the baseline it beats) as `bounds`.
- **Fix**: Apply the doc's own D4 gameability guard — a `refutes`/`bounds` edge counts as corrective only
  if the refuted claim's *evidence is actually addressed* (a D1-style check). Do not weight baseline
  naming as corrective.
- **Acceptance**: corrective score requires a validated corrective edge; che26 RW14 no longer contributes;
  a paper that merely names a baseline scores 0 on this ranker.

## RC5 — negative_result_share blind to real nulls stated as supported claims  · severity: HIGH · status: open
- **Target**: V1 D3 `negative_result_share` (counts `status: refuted`).
- **Finding**: A genuine negative finding is written as a *supported* claim ("X fails to differentiate"),
  so the status-based counter scores it as zero negative-knowledge.
- **Evidence**: woj25 C04 — "plasma p-tau181&231 fails to differentiate, Cohen's d<0.2, AUC 0.514" —
  `status: supported`, counted as non-negative.
- **Fix**: Detect negative-finding claims by *semantics* (asserts a null / no-difference / failure /
  non-significance), not by `status: refuted` alone.
- **Acceptance**: woj25 C04 counts as negative knowledge; the metric picks up null-result claims regardless of status.

## RC6 — Verified grounding is compiler-bound and computable for only 4/10  · severity: MEDIUM · status: open
- **Target**: `verified_grounding()` + H03.
- **Finding**: 6/10 ARAs cite `paper.pdf`/§refs and return `None`; so the metric measures a *compiler
  choice* (cite in-repo evidence vs cite the PDF), i.e. artifact-quality, not paper-quality.
- **Evidence**: `comparison_v1_v2.md` §1 — verified = None for cum26/jes26/kes25/pal25/tit26/woj25;
  diagnostic flags `grounding_verified` low_variance at n=4.
- **Fix**: Resolve §/page refs against the source PDF so all 10 are checkable, **or** explicitly move
  grounding-verifiability to the artifact-quality/trust-weight axis and stop ranking papers on it.
- **Acceptance**: verified grounding is either computable corpus-wide, or tagged artifact_quality and out of the paper ranking; H03 updated.

## RC7 — Verified grounding checks string-presence, not semantic support  · severity: MEDIUM · status: open
- **Target**: `verified_grounding()`.
- **Finding**: It confirms the quote string exists in the cited file, not that the quote *supports the
  number/claim*. "presence≠truth" only narrowed to "quote-string-in-file≠truth." A real table cell
  pasted next to a wrong assertion still scores 1.0.
- **Fix**: Add a `[sem]` support check (does the quoted evidence entail the number/claim), score computed deterministically from findings.
- **Acceptance**: a quote that exists but does not support its number scores as ungrounded.

## RC8 — Genre classifier is brittle and already wrong  · severity: MEDIUM · status: open
- **Target**: `classify_genre()` / `GENRE_RULES`.
- **Finding**: First-match keyword matching mislabels papers, corrupting applicability + within-genre buckets.
- **Evidence**: cum26 (drug-development **pipeline review**) classified `clinical_trial`.
- **Fix**: Classify from `PAPER.md` metadata/venue/type or an LLM label; validate against hand labels for the 10.
- **Acceptance**: cum26 → `review`; classifier agrees with hand labels on the wave-1 set.

## RC9 — Genre-split atomizes n=10 into unrankable singletons  · severity: MEDIUM · status: open
- **Target**: `genre_scoped_ranking()`.
- **Finding**: 10 papers across 6 genres ⇒ most genres have 1 member; "compare like with like" returns
  one-paper "rankings."
- **Fix**: Gate within-genre ranking on a minimum bucket size; otherwise rank cross-genre with genre as a
  covariate/normalizer. Log buckets too small to rank.
- **Acceptance**: no singleton bucket is presented as a ranking; min-bucket-size enforced and logged.

## RC10 — paper_quality vs artifact_quality is label-only  · severity: LOW · status: open
- **Target**: `ranker()` tags + H04.
- **Finding**: Every ranker is tagged `paper_quality`, including compiler-determined ones; the split is a
  string, not a routing.
- **Fix**: Actually route compiler-determined signals (e.g. grounding-verifiability, environment
  completeness) to artifact_quality/trust-weight and keep them out of the paper ranking.
- **Acceptance**: ≥1 ranker tagged `artifact_quality` and excluded from paper ranking.

## RC11 — Doc/impl mismatch: clinical spec rubric listed as fixed but dropped  · severity: LOW · status: open
- **Target**: `metrics-directions.md` critique table row 5.
- **Finding**: Crit-#5's "V2 path forward" claims a genre-parameterized clinical spec rubric, but V2
  removed spec-completeness entirely (no spec ranker in `compute_metrics_v2.py`).
- **Fix**: Either implement the clinical rubric or mark the row "dropped, not implemented."
- **Acceptance**: the response table matches the code.

---

**Meta (do not skip):** RC1+RC2 are the gate. Fixing RC3–RC11 without them yields a better-instrumented
way to measure the same wrong thing — the whole system still runs on the compiler's reconstruction with
no ground truth. V3 should treat "validate against an external signal" and "compute against source PDFs,
not compiler YAML" as prerequisites, not optional extras.
