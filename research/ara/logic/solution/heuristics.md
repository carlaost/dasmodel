# Heuristics

Design rules for the good-science metrics system (N27), crystallized after the wave-1 test run and
the V2 redesign committed them in code (`research/metrics/v2/compute_metrics_v2.py`). Each was staged
as an observation and matured on artifact-commitment + the user's directive to act on the critiques.

## H01: Separate validity gates from quality rankers
- **Rationale**: Some metrics (cross-layer binding resolvability, seal-L1 structural completeness) are
  binary hygiene checks a well-formed ARA must pass — near-ceiling with ~0 variance. Averaging them
  into a continuous quality score is a category error; they gate, they don't rank. V2 reports `gates`
  (pass/fail) apart from `rankers` (continuous quality).
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: medium — misclassifying a ranker as a gate hides real quality variance.
- **Code ref**: [research/metrics/v2/compute_metrics_v2.py]
- **Source**: staged O08; wave-1 review (N30)

## H02: Make metrics genre-aware; never score a paper 0 for its genre
- **Rationale**: Clinical trials/reviews/guidelines structurally lack code (no L3), documented failures
  (D3 floors), and negative results. Scoring 0 there penalizes a paper for its genre. Use an
  applicability model that returns `N/A (genre)` where a dimension doesn't apply, and rank only
  *within* a genre. Cross-genre, those dimensions are still informative (a genre can score low as a
  class); within-genre they must not be forced to 0.
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: high — this is the biggest single fairness fix; wrong applicability rules distort rankings.
- **Code ref**: [research/metrics/v2/compute_metrics_v2.py]
- **Source**: staged O07 (+O05 spec-rubric mismatch); wave-1 review (N30)

## H03: Verify grounding by re-opening the cited source — presence ≠ truth
- **Rationale**: A grounding metric that only checks a `«quote»` is present measures decoration, not
  truth. Re-open the cited file and confirm the quote string is actually there. This also exposes a
  real distinction: *self-contained* grounding (cites in-repo evidence files, verifiable) vs
  *PDF-pointer* grounding (cites `paper.pdf §…`, unverifiable within the ARA). On wave-1, most ARAs
  were PDF-pointer only; V1's high presence scores were largely unverifiable.
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: high — presence-only scoring is exploitable; a compiler can decorate with plausible quotes.
- **Code ref**: [research/metrics/v2/compute_metrics_v2.py]
- **Source**: staged O09; wave-1 review (N30)

## H04: Tag every metric paper-quality vs artifact-quality
- **Rationale**: A low score can be the paper's fault or the compile's fault. woj25's grounding 0.0 is
  a compiler omission (no Sources layer), not bad authorship. Tag each metric's `quality` axis and keep
  artifact-quality out of the paper ranking; use it as a trust weight instead. When backprocessing
  legacy PDFs, normalize/interpret within a compiler version.
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: medium — conflation slanders papers for compiler defects.
- **Code ref**: [research/metrics/v2/compute_metrics_v2.py]
- **Source**: staged O06; wave-1 review (N30)

## H05: Emit a discrimination diagnostic; a zero-variance metric is non-informative here
- **Rationale**: A metric that returns the same value for every artifact in a corpus cannot rank within
  it. Compute per-ranker variance/range across the library and label each `discriminating` /
  `low_variance` / `non_discriminating`, so the tool self-reports which metrics a given corpus can't
  exercise (rather than presenting a flat score as if it were meaningful). Also guards against
  evaluating metrics on an adversarial (single-genre, homogeneous) test bed without noticing.
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: low — diagnostic only; does not change scores, just flags them.
- **Code ref**: [research/metrics/v2/compute_metrics_v2.py]
- **Source**: staged O10; wave-1 review (N30)

## H06: Score metric candidates on a held-out split, never on training rho
- **Rationale**: On small evaluation sets (here 40 train / 26 test) formula complexity buys overfitting, not signal. A 16→4→2→1 tournament optimizing training ρ selected a winner at 0.77 train that fell to 0.53 test, below a one-feature baseline at 0.57 with no gap. Only the held-out column reveals which metrics generalize; train ρ ranks them wrong.
- **Sources**: [winner 0.771→0.534, plain-depth 0.546→0.572 ← research/metrics/v5-breakthrough/corpus/apply_formula.py --split train|test [result]]
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: high
- **Code ref**: [research/metrics/v5-breakthrough/corpus/apply_formula.py, corpus/split.json, tournament16_workflow.js]

## H07: Sign-flip a negative feature only if it is a true inverse construct, not a confound proxy
- **Rationale**: `1 − anchor_overlap` is legitimate (novelty IS distance from prior art — causal, generalizes). Subtracting `delta`/`n_deltas` is not (they correlate with breakthrough only because report-genre papers pile up deltas in this corpus); the delta-hack underperformed doing nothing on held-out data and misfired on real discoveries. Test: would intervening on the feature causally change the target?
- **Sources**: [delta-hack 0.712→0.449 vs plain-depth 0.572 ← research/metrics/v5-breakthrough/corpus/apply_formula.py [result]]
- **Status**: active
- **Provenance**: user-revised
- **Sensitivity**: high
- **Code ref**: [research/metrics/v5-breakthrough/corpus/FEATURES.md, RESULTS_PAPER.md §7]
