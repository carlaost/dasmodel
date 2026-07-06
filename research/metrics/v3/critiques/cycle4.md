# Cycle 4 — Fable convergence check

**VERDICT: CONVERGED**

The loop has genuinely reached its honest endpoint. R1–R7 are real (verified in code + JSON, not
cosmetic), the severity-weighted gate demonstrably flipped the partition, and `outcome_switching` — a
better-built signal than its predecessor — produced 0 misconduct hits on this corpus, exactly as the
corpus-limit thesis predicts. No science-measuring in-place work remains; remaining moves are more
labeling (excluded by mandate) or a corpus change (outside this loop).

## (1) R1–R7 addressed vs cosmetic — verified
- R1 ✅ REAL — paper_ranking_axis_status=RETIRED in JSON; diagnose()/scoped_rankings filter rank_eligible.
- R2 ✅ REAL (build) / ⚠️ epistemics (§2) — outcome_switching.py + 3 frozen caches; "switched" branch fired.
- R3 ✅ REAL — partition flipped confirmed: jes26 (0.9, polarity_inversion)→ineligible; che26 (0.625,
  only unsupported_addition)→eligible; woj25→hard-fail. Genuine behavior change vs old flat-0.9 gate.
- R4 ✅ REAL — novelty_audit status=audited_spotlight; 27/98 checked, 71 pending disclosed; 7 ahm26b
  artifacts suppressed; "do NOT read as corpus rate."
- R5 ✅ WRITTEN — FINDINGS.md, correct thesis (one count error fixed post-hoc).
- R6 ~ PARTIAL (honestly labeled) — 71/98 pending disclosed not fixed; acceptable (fixing = more labeling,
  shown to catch nothing new).
- R7 ✅ REAL — loop-log che26/woj25 mislabel corrected to match yamls.
Cleanest cycle of the four; no fake/hollow items.

## (2) outcome_switching — genuine design advance, 0 real misconduct hits (corpus-limited, not mislabeled)
In kind it is sounder than claim_level_validation: compares paper's claimed-primary to the EARLIEST
timestamped registered primary (ct.gov internal history API) — external, un-fakeable, live failing branch.
BUT its one firing (jes26 "switched") is a false positive for misconduct on three grounds from its own
cache: (1) the CDR-SB→iADRS change is the TRIAL's event (TRAILBLAZER-ALZ 2, v21, 2021-03-24), years before
this post-hoc reanalysis paper existed — attributing a trial event to a paper that didn't commit it; the
module fell back to C01 because no claim is even tagged primary. (2) Benign: amendment predates earliest
unblinded readout by ~8mo → blinded, pre-specified (the legitimate kind). (3) n=3, all industry
donanemab/biomarker trials, clean/benign, no positive control. Honest reading: a well-built template that
found a real registry fact but not misconduct → 0 real hits. Reinforces convergence (scaffolding sound,
corpus has no case to exercise it), does not reopen the loop.

## (3) FINDINGS.md accuracy — core claim CORRECT and HONEST
Stress-tested "measures fidelity not science; unlock is a CORPUS change not another metric" — holds. Every
external anchor available on this corpus is exhausted and each collapses to a non-science signal (ChEMBL
resolvability=fabrication check; endpoint concordance=transcription; novelty=unauditable spotlight;
outcome-switching=benign/n=3). No un-exhausted external anchor, no compiler-internal signal escaping the
fidelity trap. Honest endpoint, not premature surrender. Two defects flagged (both fixed post-critique):
count 3→4 (add woj25:C04); soften "returned a real negative" → "live failing branch, but 0 detected
misconduct."

## (4) CONVERGED — highest-value next steps for Carla (outside the loop)
1. **Execute the corpus change — the whole unlock.** Cross-domain, multi-topic corpus with CODE-SHIPPING
   computational papers (→ reproduction, the only un-gameable science signal) + a HELD-OUT EXPERT-LABELED
   quality subset (the missing ingredient every cycle; without an external quality label every metric is
   definitionally a fidelity check). Scaffolding is built and waiting.
2. **Give outcome_switching a positive control.** Import 2–3 trials with documented data-driven primary
   switches (COMPare/RIAT catalogs these) and confirm the branch flags misconduct while sparing benign
   amendments like jes26. Cheapest way to prove it discriminates, not just fires.
3. **Close the two open decisions + the latent bug.** N47/C16: evidence (fidelity 0.918; 2/10 ARAs
   ranking-flipping) supports "narrow to per-ARA gate," not "withdraw." Confirm claim-level ledger as the
   headline unit. Fix compute_metrics._field() single-line regex (silently truncates multi-line claim
   Statements — harmless here, will corrupt parsing on a new corpus).

**Bottom line:** loop not rubber-stamped, no work manufactured — R1–R7 verified, new signal scrutinized and
found correctly-built-but-corpus-starved, no science-measuring in-place work remains. Stop the loop; the
next move is Carla's corpus.
