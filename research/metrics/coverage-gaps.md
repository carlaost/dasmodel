# Metrics coverage & gaps — wave-1 test run (10 OA papers)

Ran `compute_metrics.py` over the 10 compiled ARAs in `research/ara-library/` and their
`sources.yaml` discovery records. This is the readiness report: what computed, and what's
missing to compute the rest.

## Corpus reality (what's actually available)
- **10 / 142** papers compiled (wave-1); 8 OA full-text PDFs, 2 paywalled (the25, sal26 → abstract-only, 7 and 4 claims).
- **0 code repositories** found across all 10 (clinical trials / reviews / guidelines don't ship code).
- **Datasets are controlled-access** (Vivli IPD, BioFINDER-2, UK cohorts) — linked, not openable.
- **No oshima store** — these are compiler-ARAs, so there is no typed-evidence / `fol_json` layer.

## Fully computable now — and computed ✅
| Direction | Metrics | Wave-1 result |
|---|---|---|
| D1 | cross-layer binding resolvability, environment completeness | 0.99 / 0.81 mean |
| D2 | claim-grounding ratio, falsifiability presence, orphan counts, status mix | 0.80 mean grounding; **woj25 = 0** |
| D3 | dead-end density, decision branching, explicit/inferred, failure-preservation, negative-result share | computed for 9/10 (pal25 null) |
| D4 | typed-delta profile, corrective-science score, concept count, RW blocks | corrective score mean 4.6 |
| D6 | trials linked, datasets linked, code repos, PDF OA | cum26 = 8 NCTs |
| D7 | seal L1 structural, orphan-experiment blind-spot | 0.97 mean |
| D5 | shared-trial clusters, in-library citation reuse, claim-redundancy proxy | all 0 (see scale gap) |

## Blocked or degraded — exactly what's missing

**1. Executable reproduction (D1 L3) + replication depth (D5) — BLOCKED: no runnable artifacts.**
0/10 have code; datasets are request-only. Nothing can be sandbox-run. Intrinsic to this domain —
likely stays N/A unless a paper ships code + open data. *Missing: a code repo and an openable dataset.*

**2. All `[sem]` metrics — MISSING: an LLM-judge pass (not built into the script).**
Evidence relevance (D2), falsifiability *quality* (D2), scope calibration (D3-sense), spec-completeness
rubric (D1), novel-claim originality (D4), concept-introduction rate (D4), compilation fidelity (D7).
The script emits these as `pending_model` with inputs gathered. *Missing: a second pass that has an
LLM emit findings, score computed deterministically from them.* — buildable now.

**3. `[ext]` grounding metrics (D6) — MISSING: live API calls (tools are available).**
Claim-vs-endpoint concordance needs a ClinicalTrials.gov endpoint pull; target/compound resolvability
needs ChEMBL. The MCP tools exist in-session but aren't wired into the standalone script.
*Missing: an enrichment pass calling those APIs.* — buildable now.

**4. D5 FOL claim graph — MISSING: the oshima typed-claim/FOL store.**
Corroboration / contradiction / true redundancy need typed evidence (support/contradict/contextual) +
`fol_json` claim clustering. Current D5 falls back to shared-NCT and token-Jaccard proxies.
*Missing: run oshima over the PDFs, or an LLM cross-library claim-linking pass.*

**5. Per-artifact compile defects (fixable by recompiling) — data quality, not tooling.**
- **pal25** — no `trace/exploration_tree.yaml` → all D3 metrics null. Incomplete compile.
- **woj25** — no `**Sources**` / `«quote»` blocks → grounding = 0. Compiler omitted the grounding layer.
- **the25, sal26** — paywalled, abstract-only → sparse evidence layer, few claims.
*Missing: a clean recompile of pal25 + woj25; licit full text for the25 + sal26.*

**6. Metric-design mismatch (flag, not a data gap).**
`spec_completeness_setup_proxy` scores ML-style slots (Model/Hardware/Dataset/System) → ~0 for every
clinical paper. The proxy is domain-inappropriate here; it needs a **clinical reproduction rubric**
(cohort, assay/platform, positivity cutoffs, statistical model, sample size) instead.
*Missing: a domain-appropriate rubric for D1 spec-completeness.*

**7. Scale gap (expected, not broken).**
D5's 0 shared-trial clusters / 0 citation-reuse / 0 near-duplicates is because wave-1 is only 10
diverse papers. These metrics become meaningful across the full 142. *Missing: more compiled waves.*

## One-line answer
Everything deterministic and artifact-local computes today; what's missing splits into (a) an
LLM-judge pass for `[sem]`, (b) ClinicalTrials/ChEMBL calls for `[ext]`, (c) an oshima/FOL layer for
the real D5 graph, (d) two recompiles (pal25, woj25) + full text for 2 paywalled papers, and (e) a
clinical (not ML) reproduction rubric for D1 spec-completeness. No code/open-data means L3 stays N/A
for this corpus.
