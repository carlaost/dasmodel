# Cycle 2 — Fable metascientist critique of V3 (post-claim_graph, honest 1/6 state)

Critique round 2. Reviewing implementation cycle 3's inputs against Cycle-1 P1–P9. Verbatim deliverable.

## (1) Blunt verdict

This cycle did the honest thing where it was cheap and dodged it where it was expensive. **The spine
corrections are real, not theater** — verified in code: `judge_scored` exists and is excluded from
`usable`; the three [sem] fidelity judges are gone from `PAPER_RANKERS` and folded into a single
`compiler_fidelity` trust component (one signal not three); `falsification_writing_quality` is
report-only, excluded from `w`. The κ study is genuine and independently confirmed P2/P6. Usable fell
4/9→1/6. Credit: P1, P2, P6, P8 substantively fixed.

Three things now clear:
1. **The honest usable count is 0, not 1.** The lone survivor `translation_trial_linkage` is the exact
   metric P7 said to give a denominator or retire — an unnormalized NCT-mention count where cum26=8.0 (a
   narrative review) "wins" SYNTHESIS by name-dropping 8 trials its own RC2 harness labels
   `not_applicable`. Labeled `source_bound` only because a ref-string exists; P4's `source_bound`→
   `ref_string_bound` rename was never applied. 1/6 is 0/6 with a ref-string.
2. **`abstract_bound` is a cosmetic flag with no gate — P1's disease one layer out.** Nothing in the
   `usable` gate or `scoped_ranking` reads it. Result: ahm26b (abstract-only) sits at the TOP of two
   PRIMARY_CLINICAL rankings (novel_claim_count=8.0 rank 1; semantic_grounding=1.0 rank 1); the25 ranked
   throughout SYNTHESIS. A label that changes no decision.
3. **Full text acquired (10/12) and never used.** The fidelity judges — and thus `compiler_fidelity` —
   are still scored against `metadata.md` (the abstract). jes26's "clearance maintained vs reaccumulates"
   inversion is now directly checkable and was not checked. The C16/N47 contradiction remains 100%
   unmeasured while the evidence sits in `fulltext/`. Single largest gap.

The claim_graph is the right direction with one genuinely novel capability (novelty-vs-prior-lit), but as
shipped it's a semi-manual n=12 proof-of-concept with two of three anchors measuring the wrong thing.

## (2) P1–P9 fixed vs still-broken

- **P1** ✅ FIXED — judge_scored below source_bound, excluded from usable; validated reserved for external.
- **P2** ✅ FIXED — [sem] judges out of PAPER_RANKERS, folded into one compiler_fidelity signal; κ corroborates.
- **P3** ❌ NOT DONE — full text acquired but judges still score vs metadata.md; no extractive_fidelity metric; N47 open. Enabling data now exists and is unused.
- **P4** ⚠️ HALF — acquisition succeeded (10/12); but re-grounding not done, source_bound→ref_string_bound rename not done, abstract_bound not enforced. Text acquired, not consumed.
- **P5** ⚠️ PARTIAL — claim_graph built+wired; novelty check real (caught 2 over-claims); but ChEMBL + corroboration anchors measure the wrong thing, and it's semi-manual.
- **P6** ✅ FIXED — falsifiability_quality gone from rankers and dropped from w after κ=−0.031. Report-only.
- **P7** ❌ NOT DONE — translation_trial_linkage still raw n_clinical_trials_linked, still source_bound, still the only usable metric. corrective_science still regex-pinned 0.0×12.
- **P8** ✅ FIXED — validator_reliability.md, n=20 independent rater, κ acted on. Best work in the cycle. Caveat: n=20, single pair, single topic — "high/≈0" not 3-decimal.
- **P9** ❌ NOT DONE — no CI/applicable-n; still reporting n=2 pairwise buckets as rankings.

Score: 4 fixed (P1,P2,P6,P8), 2 partial (P4,P5), 3 untouched (P3,P7,P9). Fixed = cheap spine edits + audit; untouched = the expensive ones (re-run judges on full text, redesign trial metric, add statistics).

## (3) Hard critique of claim_graph

- **(a) ChEMBL resolvability measures drug-nameability, not science — and its "hard negative" is a DB
  artifact.** 69/72 resolve (~96%) → non-discriminating by construction. It only fires on a hallucinated
  entity → it's a FABRICATION/fidelity detector (belongs on trust axis, per P2), not a science signal.
  "APOE does NOT resolve = hard un-fakeable negative" is a FALSE signal: ChEMBL is a bioactivity DB;
  APOE/GFAP are a lipid-transport gene and an astrocyte filament with ~no small-molecule ligand data —
  their absence says nothing bad about huu25 (a legit APOE-ε4 genetics paper). If weighted, it would
  penalize exactly the non-druggable-target biomarker/genetics papers. Keep only as a fabrication check
  on trust; NEVER let non-resolution count against a claim.
- **(b) TF-IDF corroboration at n=12 single-topic is noise dressed as replication.** 4 clusters/8 edges
  over 100 claims at hand-picked cosine≥0.30. Top cluster is jes26+sal25 both reporting ARIA-E — both
  donanemab TRAILBLAZER trials: one drug measured twice, NOT independent corroboration. kes25/tit26/woj25
  cluster is same-biomarker labs that cite each other. Corroboration is meaningful only under
  independence, which a single-topic convenience sample structurally cannot supply. Demote to exploratory.
- **(c) The novelty check is the one real thing — and it's a manual literature review, not yet a metric.**
  Catching sal25 C01 "first head-to-head" (predated by Feb-2025 review) and sal26 C01 is something no
  compiler-fidelity check can do — vindicates "anchor externally." But: coverage 10/22 (12 pending); the
  PubMed date_to filter is broken (returned 2026 articles for a 2024 cutoff) so prior-vs-subsequent was
  hand-classified (`_classify_novelty` returns "see_detail"); several "no_prior_evidence_found" are
  weak-query artifacts (woj25 C01 self-coined assay names). A metric needing per-claim manual verification
  is a workflow, not a metric. Proves the direction; doesn't instrument it.

Net: one-third (novelty) is the right idea at PoC maturity; two-thirds (ChEMBL, TF-IDF) are mislabeled
fidelity check or single-topic noise. The one clean computable Goodhart-resistant metric — **per-claim
trial concordance** (jes26 C01, sal25 C01/C02 concordant vs registered primary outcomes' posted numbers,
3/18 with honest not_applicable) — is the best thing in the cycle and is WALLED OFF from usable. You built
the principled replacement for translation_trial_linkage and left the name-drop count as the official metric.

## (4) Ranked problems → fixes for cycle 3

- **C1 [BLOCKER] Honest usable = 0: sole "usable" metric is the name-drop count (P7); its principled
  replacement sits unused in claim_graph.** → Retire translation_trial_linkage. Promote
  `per_claim_trial_concordance` to a first-class CLAIM-level validated signal: a claim is `validated` iff
  its number reproduces a registered primary outcome's posted value within tolerance (3 concordant
  already computed). Report "N claims externally validated across M ARAs," not "1/6 papers." The claim,
  not the paper, is the unit that anchors externally.
- **C2 [BLOCKER] abstract_bound is a flag with no gate — ahm26b (abstract-only) ranks #1 in two
  PRIMARY_CLINICAL metrics.** → Make abstract_bound force usable=False and drop the ARA from every
  scoped_ranking bucket (or an explicit `unverifiable` list). One-line gate + filter. Non-negotiable
  before publishing any ranking.
- **C3 [BLOCKER] C16/N47 still unmeasured though enabling data is on disk (P3).** compiler_fidelity is
  fidelity-to-abstract, not to-paper. → Re-run evidence_relevance + scope_calibration against
  fulltext/<slug>.txt for the 10 covered ARAs. Compute per-ARA `extractive_fidelity` = fraction of claims
  whose numbers AND direction match the full paper. Check the known inversions (jes26 clearance, huu25
  MAPT; the25 stays unverifiable, abstract-only). No paper-ranker is sound until extractive_fidelity is
  measured; gate ranking on it.
- **C4 [HIGH] Reclassify the two mislabeled claim_graph anchors.** ChEMBL resolvability → trust axis
  fabrication check; NEVER penalize non-resolution (APOE/GFAP = DB-coverage artifacts). TF-IDF
  corroboration → demote to exploratory (can't establish independence at single-topic n=12).
- **C5 [HIGH] The gaming strategy relocated; close it.** New equilibrium: paste more NCT IDs (tops the one
  usable ranker); emit terse claims never exceeding the abstract (compiler_fidelity pins 9/12 at 1.0);
  cite an approved drug (auto-resolves); copy the registry number (concordance = transcription check);
  never say "first" (novelty check only fires on self-declared-novel claims → rewards silence about
  novelty). → Run novelty on ALL headline claims naming a testable finding, not only self-declared-novel.
  Give compiler_fidelity a discrimination floor (if >75% score ==1.0, report non-discriminating).
- **C6 [MEDIUM] Novelty must become computable or be labeled manual review.** date_to broken; hand-
  classified; 10/22 coverage. → Build a real publication-date comparator (parse metadata publication_date
  vs the ARA's confirmed pub date), re-run all 22, label residual hand cases `manual_review`.
- **C7 [MEDIUM] P9 statistics absent — stop printing n=2 buckets as rankings.** → Attach applicable-n +
  bootstrap CI (or "too few to rank"); suppress buckets below K_MIN=3 from ranking output, not just caveat.

**Single highest-value next move:** C1+C3 together — make the externally-validated claim the unit of
"usable," and re-ground fidelity on the full text already fetched. Retire translation_trial_linkage,
promote per-claim trial concordance to claim-level `validated`, re-run fidelity judges against fulltext/
to measure extractive_fidelity, enforce abstract_bound. Converts the hollow "1/6 papers" into a
defensible "N claims validated against registered endpoints, on ARAs whose extractive layer is
measured-faithful" — the first thing in the project actually measuring science instead of the compiler.
