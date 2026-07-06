# Cycle 3 — Fable metascientist critique of V3 (post-fidelity-gate + claim_level_validation, honest 0/6)

Critique round 3. Verbatim deliverable.

## (1) Blunt verdict

The most honest cycle yet, and the honesty surfaced the real result: **the paper-ranking axis is dead,
and what replaced it (claim_level_validation) is a transcription check wearing a validation hat — the
round-1 category error relocated from the paper to the claim.** Spine work is genuine (rank_eligible,
ref_string_bound, abstract_bound, grounding self-catch all real in code). Three facts now dominate:
1. **Paper-ranking produces one 3-way bucket on zero usable metrics.** After rank_eligible + K_MIN=3,
   every scoped_ranking collapses to diagnostic_accuracy_study={kes25,sal26,tit26}, ranked on 6 metrics
   all invalid_fabricated/pending_sem/judge_scored/ref_string_bound — none usable. An axis empirically
   retired and not yet buried.
2. **claim_level_validation's "3 concordant" is number-copying and cannot fail.** All 3 (jes26:C01,
   sal25:C01/C02) are the ARA's number = the registry's posted value for the trial the paper IS. 0/18
   discordant — the negative branch has never fired. Measures transcription, not science.
3. **Novelty's "11" is 73% one abstract-only paper.** 8/11 overclaim_risk = ahm26b (abstract_bound,
   rank_eligible=False), descriptive CDC-WONDER mortality tabulations, flagged only because a [sem] judge
   tagged every ahm26b claim novel. Artifact.

## (2) Round-2 C1–C7: fixed vs cosmetic

- C1 ✅ mechanical / ⚠️ hollow — trial_linkage ref_string_bound (real); but the promoted replacement is number-copying. Traded name-drop for transcription. Usable floor correctly 0.
- C2 ✅ FIXED — rank_eligible enforced in diagnose() + scoped_ranking(); ahm26b/the25 excluded.
- C3 ✅ done / ⚠️ incoherent gate — measured vs full text, but severity-blind (see §3c).
- C4 ✅ FIXED — ChEMBL trust_fabrication_check + db_coverage_artifact; corroboration exploratory.
- C5 ❌ COSMETIC — pool widened in code but caught nothing new: all 11 prior_found are self_declared; 0 from non-self-declared. 71/98 pending (cum26/jes26/kes25/pal25 wholly unchecked). Dodge still open.
- C6 ✅ FIXED — real date comparator; manual_review when uncomputable.
- C7 ✅ FIXED — sub-K_MIN → bucket_too_small_to_rank (n=2 problem gone; bootstrap CIs still absent).

Score: 4 real (C2,C4,C6,C7), 1 hollow (C1), 1 incoherent (C3), 1 cosmetic (C5). Pattern: labeling/gating ships clean; the two things requiring *measuring science* (C1 validation, C5 novelty) ship as fidelity-checks/spotlights.

## (3) Hard critique of the two new headline signals + the gate

### 3a. claim_level_validation — fidelity one level in, cannot fail
"Concordant" = ARA number equals registry's posted value for the paper's own trial → measures the
compiler copied the paper's trial numbers correctly (extractive fidelity vs a 2nd source), not science.
0/18 discordant → no demonstrated discrimination. Not independent (both are Lilly donanemab TRAILBLAZER
RCTs). **Fix:** check against the PRE-REGISTERED protocol, not posted results — flag OUTCOME SWITCHING
(reported primary ≠ pre-registered primary). That is un-fakeable (timestamped pre-results), CAN return a
negative, and measures a research behavior. `_registered_primary_outcomes` already parses primaryOutcomes;
pivot to registered-primary-name vs paper's-claimed-primary.

### 3b. novelty overclaim_risk — spotlight, not metric
27/98 checked, 71 pending (non-random), whole ARAs at 0 checks → recall undefined, precision unauditable.
8/11 flags are the ahm26b abstract-only artifact. overclaim_risk ≡ prior_literature_found (11=11) → the
priority-language guard is inert. 3 real catches survive (sal25:C01, sal26:C01, huu25:C05) — report those
as "3 hand-audited priority over-claims," not "11 overclaim_risk."

### 3c. extractive_fidelity gate — arbitrary threshold AND severity-blind (the worse bug)
Bimodal: 8 at 1.0, 2 at 0.625, jes26 alone at exactly 0.9 → any cutoff in (0.625,0.9] gives the same
partition, so 0.9 isn't chosen. But `>=0.9` admits jes26 DESPITE its confirmed C09 polarity inversion,
while excluding che26 whose every number is correct (3 unsupported_additions only). A flipped conclusion
is categorically worse than an added clause. **Fix: severity-weight** — polarity_inversion/number_mismatch
on a headline claim = hard fail; unsupported_addition = soft demerit. Also: circularity (LLM checking LLM
vs pdftotext) already produced ONE retracted false finding (huu25 MAPT, italic-gene-symbol stripping) →
re-verify every exclusion against rendered PDF pages, not the .txt dump.

## (4) Ranked → fixes (cycle 4)

- **R1 [BLOCKER — architectural cut] Retire the paper-ranking axis; make the claim the unit of record.**
  6 rankers, 1 bucket, 0 usable = dead. Move scoped_rankings/diagnose to an appendix labeled "retired
  axis: does not measure science on any corpus tested." Headline = a claim-level ledger (per claim:
  fidelity status, external-anchor verdict, novelty verdict).
- **R2 [BLOCKER] Re-found claim validation on pre-registration concordance (outcome-switching), not
  posted-result transcription.** A signal that can fail, is un-fakeable, measures a research behavior.
- **R3 [HIGH] Severity-weight extractive_fidelity; re-verify exclusions vs rendered PDF.** Hard-fail on
  polarity_inversion/number_mismatch (excludes jes26); spare unsupported_addition (spares che26).
- **R4 [HIGH] Novelty = audited spotlight, not metric.** Report only the 3 verified; suppress
  overclaim_risk on abstract_bound ARAs (removes the 8 ahm26b artifacts); stop quoting a corpus count.
- **R5 [HIGH — the actual unlock] Name the corpus/design limit and change it.** Honest finding after 3
  cycles: this system measures fidelity, not science, because a 12-paper single-topic industry-biomarker
  corpus (2 abstract-only, no code, no independent replication) structurally cannot supply a
  science-quality signal. Unlocks: (a) corroboration→replication needs a MULTI-TOPIC independent-discovery
  corpus; (b) "validated" needs a HELD-OUT EXPERT-LABELED quality set to correlate against; (c) the only
  un-gameable signal is REPRODUCTION → needs CODE-SHIPPING papers (runnable code+data). AD clinical papers
  have no code, hence the ceiling. Cross-domain corpus incl. computational papers is the concrete unlock.
- **R6 [MEDIUM] Close the C5 dodge for real or drop the widened-pool pretense** (71/98 pending = inert).
- **R7 [MEDIUM] Fix loop-log's own record** — line mislabels che26/woj25 exclusions as transposition.

**Single highest-value move:** R1+R2 — retire the dead axis, re-found validation on outcome-switching (a
signal that can fail). But be clear-eyed (R5): deeper signals stay out of reach until the corpus changes.
After 3 cycles this is converging on an honest "cannot, on this corpus" — the right cycle-4 deliverable is
to SAY that in the headline and specify the corpus change, not add a seventh metric.
