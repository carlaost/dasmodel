# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 8. `trace/exploration_tree.yaml` (the exploration DAG)

### Artifact + path
`trace/exploration_tree.yaml`, e.g. `research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/trace/exploration_tree.yaml`.

### Purpose
The "git log" for the research — a structured, traversable record of the paper's actual decision
trajectory: every question asked, experiment run, decision made with rejected alternatives, dead end
hit, and pivot taken. **Dead-end nodes are the single most valuable node type for downstream agents**
because they save future work from rediscovering known failures.

### Structure
Top-level YAML key `tree:`, a list of nodes; nodes nest via a `children:` list (primary DAG structure)
plus an `also_depends_on:` list on any node for cross-edges beyond simple nesting (turning the nested
tree into a true DAG). Every node, regardless of type, has:

| Field | Type | Example |
|---|---|---|
| `id` | string, `N{NN}` | `N04` |
| `type` | enum{`question`, `experiment`, `dead_end`, `decision`, `pivot`} | `experiment` |
| `support_level` | enum{`explicit`, `inferred`} | `explicit` |
| `source_refs` | list[string] (recommended for `explicit` nodes; table/figure/section refs) | `["Table 2 Outcome 1", "Figure 3A", "§3.2"]` |
| `title` | string | `"NMA of diagnostic accuracy for amyloid-beta positivity (E01)"` |
| `also_depends_on` | list[ref-id] (optional; DAG convergence only) | `[N04]` |
| `children` | list[node] (optional — absent for `dead_end`, which is always a leaf) | — |

Type-specific **required** fields beyond the shared set:

| Type | Required fields | Type |
|---|---|---|
| `question` | `description` | markdown-prose |
| `experiment` | `result`; optional `evidence` | `result`: markdown-prose; `evidence`: list[ref-id \| string] mixing claim IDs and figure/table/section refs, e.g. `[C01, C08]` or `["Figure 3"]` |
| `decision` | `choice`, `alternatives`; optional `evidence` | `choice`: string; `alternatives`: list[string]; `evidence`: string (informal, prose — not a list here) |
| `dead_end` | `hypothesis`, `failure_mode`, `lesson` | all markdown-prose strings |
| `pivot` | `from`, `to`, `trigger` | all strings |

### A full realistic example (one of each node type, drawn from real trees)

```yaml
tree:
  - id: N01
    type: question
    support_level: explicit
    source_refs: ["§1 Introduction", "§2 Methods", "Abstract"]
    title: "Which plasma p-tau isoform, platform, and matrix is optimal across the AD continuum?"
    description: "No consensus exists on the optimal p-tau isoform (217/181/231), analytical platform (MS vs. immunoassay), or matrix (plasma vs. serum) for detecting Abeta pathology, tau pathology, and predicting cognitive decline. The review asks this simultaneously via network meta-analysis."
    children:
      - id: N03
        type: decision
        support_level: explicit
        source_refs: ["§2.3"]
        title: "Hierarchical de-overlapping of shared cohorts (crucial step)"
        choice: "For each shared cohort (BioFINDER-1/2, ADNI, TRIAD, WRAP), select only the single most comprehensive dataset (or one per distinct clinical outcome)."
        alternatives:
          - "Pool all studies naively (double-counts patients)"
          - "Exclude all overlapping cohorts entirely"
        evidence: "Yielded 24 statistically independent datasets from 18 publications; preserves statistical independence."
        children:
          - id: N04
            type: experiment
            support_level: explicit
            source_refs: ["Table 2 Outcome 1", "Figure 3A", "§3.2"]
            title: "NMA of diagnostic accuracy for amyloid-beta positivity (E01)"
            result: "p217_MS ranked first (P-score 0.859), then p217_Ratio (0.783) and p217_ALZpath (0.686); p181_IA ranked last (0.117). p217_MS AUC advantage vs. baseline MD 0.10 [0.04; 0.16]."
            evidence: [C01, C08]

  - id: N05
    type: experiment
    support_level: explicit
    source_refs: ["§3.6", "Supplementary Table S2"]
    title: "Meta-analysis of the incremental AUC gain from the ratio (E02)"
    result: "Ratio vs. single-analyte gave a significant MD of 0.025 (95% CI 0.005-0.045) with zero heterogeneity (I2 = 0%)."
    also_depends_on: [N04]
    evidence: [C02]

  - id: N11
    type: dead_end
    support_level: explicit
    source_refs: ["Table 2", "§4.1"]
    title: "Standard p-tau181 immunoassay as a high-precision AD marker"
    hypothesis: "p-tau181 (the historical plasma standard) would remain competitive for high-precision diagnosis and staging."
    failure_mode: "p181_IA ranked last or near-last on every outcome (Abeta 0.117; MCI-to-AD 0.159; Tau-PET 0.090; platform 0.006) and failed to discriminate Tau-PET status."
    lesson: "Standard p-tau181 is effectively obsolete for high-precision AD diagnostics (P-score < 0.20); use p-tau217 variants instead."

  - id: N14
    type: pivot
    support_level: inferred
    title: "Reframe isoform choice as a stage-dependent 'relay' rather than a single winner"
    from: "Seeking one universally optimal p-tau isoform"
    to: "A relay: p-tau231 for earliest asymptomatic amyloidosis, p-tau217 for symptomatic diagnosis/staging/prognosis"
    trigger: "Divergent subgroup rankings (N09, N12): p-tau231 tops the preclinical subgroup while p-tau217 dominates symptomatic outcomes."
    also_depends_on: [N09, N12]
```

### Cardinality / variability
Target is ~8+ nodes for a rich paper, but this is source-bounded, never a quota — a paper that hides
its failures yields a smaller, honest tree. The two read ARAs have 14 nodes (che26: 1 question, 4
decisions, 6 experiments, 2 dead_ends, 1 pivot) and 17 nodes (huu25: 1 question, 2 decisions, 9
experiments, 4 dead_ends, 1 pivot). `dead_end`/`decision` nodes are expected whenever the paper reveals
ablations, rejected alternatives, or explicit design choices, but must never be invented to hit a
count — a systematic review with no stated failed approaches legitimately has zero `dead_end` nodes.
`support_level: inferred` is common specifically on `pivot` nodes, since a pivot is usually the
compiler's own narrative reconstruction of the paper's trajectory rather than something the paper
states in so many words — real trees mark this honestly rather than dressing an inferred pivot up as
`explicit`.

### Availability notes
Mandatory core — the file must exist and parse as valid YAML with a `tree:` key, but its **richness**
is the single biggest genre-dependent variable in the whole ARA:
- **Reviews/meta-analyses have no first-person "we tried and failed" narrative** in the way a single
  wet-lab study does — their dead_ends instead come from the paper's own explicit ranking failures
  (e.g. che26's N11: p181_IA is a "dead end" only in the sense that the review's own data shows it
  fails as a diagnostic — this is a legitimate, explicit dead_end even in a synthesis genre).
- **A tree with zero `dead_end`/`decision` nodes** is not automatically a defect — it can mean the
  paper genuinely reports no rejected alternatives — but combined with a `support_level: explicit`
  paper of a genre known to involve iteration (e.g. a method paper), it is a strong signal of shallow
  extraction and should be scored down.
- **Invented/unsupported nodes are the specific thing Seal Level 1's "Trace Hygiene" check targets**:
  any `dead_end`, `decision`, or `experiment` node not traceable to the source material fails outright
  — a metric can spot-check `source_refs` against the paper the same way the validator does.
  Corresponding is the softer companion check ("no synthetic trace history"): a node with no
  `source_refs` and `support_level: explicit` (mismatched signaling) is itself a defect even short of
  outright invention.
- **Abstract-only compilation**: the tree collapses to essentially one `question` node and maybe one
  `experiment` node paraphrasing the abstract's method sentence — no decisions, no dead ends, because
  none of that granularity is recoverable from an abstract. This is the clearest "floor" example for
  this artifact.

---

