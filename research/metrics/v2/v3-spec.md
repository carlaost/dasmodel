# V3 spec — adjudicated from cycle-1 design proposals

Master (critic) adjudication of the improver agents' Phase-B proposals against the round-2 backlog
(`critiques-round2.md`, RC1–RC11). This is the implementable spec for `compute_metrics_v3.py`. Four
clusters came from sub-agents (RC1+2, RC6+7, RC8+9, RC10+11); the RC3+4+5 cluster is designed here by
the master because that agent died on the account spend limit.

**Corpus reality (verified by the agents):** the scored set is now **12 ARAs** (ahm26b, che26, cum26,
huu25, jes26, kes25, pal25, sal25, sal26, the25, tit26, woj25); `library_metrics_v2.md` is stale at 11.
`huu25` is the lone code-linked paper (external R repo, not checked into the ARA). PDFs missing for
huu25/sal26/the25. ClinicalTrials.gov MCP reachable; no oshima/FOL store.

---

## Adjudicated architecture (the spine all clusters plug into)

**Two output axes, not one score** (agents 1/3/5 converged):
- `paper_rankers` — computed on the paper; the only things ranked.
- `artifact_trust` — compiler-determined signals reduced to a single **trust-weight `w` = geometric
  mean** of normalized components. `w` **never lowers a paper's own rank** (the woj25 fix); it scales
  the ARA's *contribution to library-level metrics* and, below a threshold, flags "low-trust — interpret
  with caution." Report components, never just `w`.

**Ranker → axis routing (adjudicated):**

| Ranker | Axis | Notes |
|---|---|---|
| `grounding_verified` (+ self_contained ratio, coverage) | artifact_trust | RC6 Option B; `None`→trust classes `pdf_pointer`/`no_parseable_quotes`/`no_source` |
| `environment_completeness` | artifact_trust | presence-count of compiler-filled fields |
| `falsifiability_presence` | artifact_trust | presence-only proxy; genuine quality is `[sem]`-pending |
| `all_links_resolve`, `seal_L1`, `no_orphan_experiments`, `grounding_layer_present` | artifact_trust (gates) | keep as pass/fail, feed `w`; not paper hygiene verdicts |
| `corrective_science_score` | paper_ranker | RC4-fixed |
| `translation_trial_linkage` | paper_ranker | RC2-validatable via ClinicalTrials |
| `negative_result_share` | paper_ranker | RC5-fixed; dead-end component uses RC3 genuine-only |
| `dead_end_density` | paper_ranker | RC3-fixed (genuine-only) |
| `executable_reproduction_L3` | paper_ranker | N/A on this corpus (no in-repo runnable code) |

---

## RC1 — validity axis (BLOCKER) — ACCEPTED as proposed
Add `validity()` parallel to `discrimination()`. Rename discrimination output `verdict`→`variance_verdict`.
Verdict lattice: `{validated, source_bound, artifact_bound, invalid_fabricated, pending_sem}`. Derived
`usable = (variance_verdict == discriminating) AND (validity_verdict ∈ {validated, source_bound})`.
Diagnostic table columns: `variance_verdict | validity_verdict | usable` — **no bare "discriminating."**
Validity sub-checks reuse the RC3/RC4/RC5 detectors (source-binding ratio), the RC6 compiler-determinism
flag (`artifact_bound`), and the RC2 harness (`validated`). **Expected honest result: 0–1 rankers survive
as `usable` on this corpus.** That is the gate working, not a bug.

## RC2 — external validation harness (BLOCKER) — ACCEPTED as *partial*, with the ceiling stated
Build `validate_external.py` → `external_validation` block. Reachable signals:
- **ClinicalTrials.gov endpoint concordance** (MCP) — genuinely external, non-gameable; label the
  central claim of each trial-linked ARA `concordant/discordant/neutral`; validates
  `translation_trial_linkage` / a new `claim_endpoint_concordance`. **n≈4.** Cache responses under
  `external_cache/` for reproducibility.
- **Retraction / EoC lookup** (Europe PMC/PMC via WebFetch) — run it, but report the label as
  **degenerate** (all 12 are 2025–26, clean; zero variance).
- **Expert labels** (`expert_labels.yaml`, n≈12) — compute Spearman ρ, n; **state the circularity
  caveat** (labeler ≈ author) plainly.
- **Master ruling:** a properly-powered, *held-out* validation is **NOT honestly achievable at n=12** —
  ship the harness + the thin ClinicalTrials partial + caveated expert ρ, and mark held-out validation
  `pending: larger heterogeneous code-shipping corpus`. Do not launder underpowered ρ as "validated."

## RC3 — fabricated dead-ends (HIGH) — designed by master
**Rule: count a dead-end only on a positive binding to author-documented failure; never infer one.** A
`dead_end` node contributes to `dead_end_density` / `negative_result_share` iff ALL hold:
1. `support_level: explicit`; AND
2. `source_refs` point to a *failed attempt / abandoned approach / methods-level negative*, NOT to the
   paper's own results/conclusions — exclude refs matching `/Table|Outcome|Abstract|§?\s*[34]\.|Results|Discussion|Conclusion/`; AND
3. its `hypothesis` is **not** a negation/mirror of one of the paper's headline claims (compare against
   `claims.md` statements: if `hypothesis` ≈ NOT(a supported claim), it's a reframed conclusion → synthetic); AND
4. genre is not a synthesis class (review/meta-analysis/guideline structurally have no exploration
   process → default their dead-ends to synthetic unless 1–3 strongly hold).
Otherwise tag `synthetic_dead_end: true` and exclude. **Wave-1 check:** che26 N11/N12 (`source_refs:
["Table 2","§4.1"]`, hypothesis = "p-tau181 would remain competitive" = NOT(C-supported)) → synthetic →
che26 `dead_end_density → 0`. Feeds RC1 as `source_binding_ratio`; if 0 → `invalid_fabricated`.

## RC4 — corrective_science_score (HIGH) — designed by master
Corrective credit only for an edge that *addresses the prior claim's evidence*, per the doc's own D4
guard. An RW edge counts iff: `Type ∈ {refutes, bounds}` AND `Claims affected` non-empty AND the `Delta`
contains contrastive/overturning language (`/contradict|fails to replicate|overturn|did not hold|lower
than reported|not reproducible|refut|revises? down/`). Weight `refutes` > `bounds`; **baseline-naming
scores 0** (`Type` containing `baseline`, or Delta of the form "prior standard we improve on"). **Wave-1
check:** `refutes=0` library-wide, and che26 RW14 ("p-tau181 … now argued obsolete") is a synthesis
conclusion, not an evidence-addressing refutation → corrective score collapses toward ~0 across the
corpus. That near-zero is the honest signal that this corpus does little corrective work. Validity =
`source_bound` if any genuine edge, else `invalid_fabricated`.

## RC5 — negative_result_share blindness (HIGH) — designed by master
Detect negative/null findings by **claim semantics**, not `status: refuted`. `[det]` first pass: a claim
is a negative finding if its `Statement` matches `/no significant difference|did not differ|was not
associated|failed to|no correlation|not superior|did not improve|no benefit|non-?significant|Cohen'?s d
\s*<\s*0\.2|AUC\s*(=|of)?\s*0\.5|CI[^.]*cross/`i. Then `negative_result_share = (negative-finding claims
+ refuted claims + genuine dead-ends[RC3]) / total claims`. **Wave-1 check:** woj25 C04 ("fails to
differentiate", "Cohen's d < 0.2") → counted. Validity = `pending_sem` (the regex is an approximation;
an `[sem]` pass with deterministic scoring from findings refines it). Do not double-count a claim already
caught by RC3.

## RC6 — grounding coverage (MEDIUM) — ACCEPTED Option B
Reclassify grounding-verifiability to `artifact_trust` (above); stop ranking papers on it. Replace `None`
with explicit trust classes. PDF resolution (PyMuPDF, a *new gated dependency*) is an optional coverage
booster **inside** the trust axis only — not a paper ranker, and it can never reach corpus-wide (3 PDFs
missing; woj25 is a format bug). Normalization layer (NFKC, dash-fold, whitespace) + a
`quote_not_found_extraction` verdict so extraction misses ≠ grounding failures.

## RC7 — semantic grounding support (MEDIUM) — ACCEPTED
LLM emits **frozen, versioned** per-(number, quote) findings (`logic/grounding_findings.yaml`) with
`verdict/value_match/polarity_ok/context_match`; deterministic scorer: `grounded = string_present ∧
verdict==supports ∧ value_match∈{exact,rounded,derived} ∧ polarity_ok ∧ context_match`. Route
`quote_not_found` to RC6, not to semantic failure. **Use a different model than the compiler** (avoid
self-grading). Honest note: low yield on this well-compiled corpus — it's a guardrail for worse ARAs.

## RC8 — genre classifier (MEDIUM) — ACCEPTED (three-tier + gold set)
Tier A declared `genre:` in PAPER.md frontmatter (source of truth); Tier B LLM classifier over
*structured fields only* to populate/audit; Tier C deterministic rules fixed to **word-boundary** match
(`\bnma\b` — kills the "Klei**nma**n"→meta_analysis bug), **structured fields only** (not the raw blob),
and **reordered priority** (synthesis/guideline win over trial keywords — kills cum26→clinical_trial).
Fixed enum taxonomy + the agent's **gold labels for all 12** (adopt: cum26=narrative_review_survey,
huu25=primary_experimental, the25=systematic_review_meta_analysis, kes25/sal26/tit26=diagnostic_accuracy_study,
ahm26b=observational_epidemiology, …). CI asserts classifier reproduces gold.

## RC9 — singleton buckets (MEDIUM) — ACCEPTED (coarse rollup + K_MIN gate)
Two-level taxonomy: coarse evidence classes SYNTHESIS(4) / PRIMARY_CLINICAL(6) / PRIMARY_LAB(2).
Resolution ladder per metric with `K_MIN=3`: fine genre if n≥3 → else coarse if n≥3 → else pairwise
(n=2, caveated, not a "ranking") → else `bucket_too_small_to_rank`. **Never emit a singleton ranking.**
Same K_MIN governs `discrimination()`. Log every bucket decision. Label coarse rankings "provisional
(n=3–6)."

## RC10 — quality-axis routing (LOW) — ACCEPTED (this is the spine; see architecture)
Make `quality` a routing key, not a label. `artifact_quality` rankers are excluded from
`genre_scoped_ranking()`/`discrimination()` and feed `w`. Invariance test: two ARAs identical except
`environment.md` presence → identical paper rank, different `w`.

## RC11 — doc/impl mismatch (LOW) — ACCEPTED Option (b)
Correct `metrics-directions.md` row 5 to "dropped in V2, not implemented (spec-completeness is `[sem]`,
deferred)"; fix H02's source note. A real clinical spec rubric, if built later, is `[sem]` and lives on
the trust axis, never the paper ranking. CI: doc↔code ranker-count consistency check.

---

## Implementation order (for Phase D)
1. **Spine first** (RC10 routing + RC1 validity scaffold + RC8/RC9 genre) — everything else plugs in.
2. **Detectors** (RC3, RC4, RC5) — they feed both rankers and RC1's source-binding validity.
3. **Grounding** (RC6 reclassify; RC7 frozen-findings — RC7 needs an LLM pass, gate behind availability).
4. **External** (RC2 harness; ClinicalTrials via MCP; cache).
5. **Doc fix** (RC11).
Run over all 12 ARAs; write `research/metrics/v3/` + per-ARA `metrics/v3/`; produce a
`comparison_v2_v3.md`. Then hand back to the master (critic) for round-3 review against each acceptance
criterion.

## Master's standing verdict (carry into round-3)
V3 will be a genuinely better-instrumented system, but the **honest predicted outcome is that ~0–1
paper-rankers survive the validity gate on this corpus**, and RC2 cannot be properly closed at n=12. The
loop's real finding, if V3 is built faithfully, is the round-1/round-2 conclusion made undeniable: *these
metrics cannot be shown to measure good science until they run on a larger, heterogeneous, code-shipping,
externally-validatable corpus.* Do not let a green "all RCs addressed" scoreboard obscure that.
