# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 7. `logic/solution/` (method layer: `constraints.md` + warranted method files)

### Artifact + path
`logic/solution/constraints.md` (always present) plus zero or more sibling files named for what the
work actually has: `study_design.md`, `method.md`, `architecture.md`, `algorithm.md`,
`heuristics.md`, `formalization.md`, `proofs.md`, `design.md`. Example paths:
`research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/logic/solution/{constraints.md,study_design.md}`,
`research/ara-library/huu25-apoe-e4-alzheimer-s-risk-converges/logic/solution/{constraints.md,method.md,study_design.md}`.

### Purpose
The "how" layer: the concrete method(s) the paper used, expressed at whatever granularity and in
whatever file(s) genuinely fit this work — plus, always, the boundary conditions / assumptions /
limitations that bound how far the results generalize. There is no fixed template — the compiler
picks file names that describe THIS paper's actual method structure.

### Structure

**`constraints.md`** (always present, free-form but conventionally three sections):
```markdown
# Constraints, Assumptions, and Limitations

## Boundary conditions
- {bullet: scope limits}

## Assumptions
- A1: {assumption, may re-list from problem.md or be method-specific}

## Known limitations (§X.Y)
- **{limitation name}**: {markdown-prose}
```
Types: every bullet is markdown-prose string; assumption IDs are ref-ids (`A1`, `A2`, ...).

An additional, compiler-added subsection is common and valuable:
`## Additional caveats surfaced during compilation (data-quality notes)` — internal
inconsistencies the compiler noticed in the source (e.g. a table's row count not matching its
caption, or PRISMA-diagram arithmetic not reconciling) that are transcribed faithfully in the
evidence layer but flagged here so downstream agents don't over-trust process counts. Type: markdown-
prose bullets, each naming the specific object and the specific discrepancy.

**Method files** (`study_design.md`, `method.md`, etc.) — no fixed schema; each is markdown-prose
organized under `##`/`###` headings that mirror the paper's own Methods structure. Common recurring
sub-patterns across genres:
- Clinical/review genre (`study_design.md`): `## Reporting standard and registration`,
  `## Search strategy and data sources`, `## Inclusion / exclusion criteria`,
  `## Statistical analysis`, `## Outcomes analyzed`.
- Omics/wet-lab genre (`study_design.md` + `method.md`): `## Cohort`, `## Assays (paired, per donor)`,
  `## Analysis pipeline (high level)`, `## Statistical models`, and a separate detailed `method.md`
  with per-substage QC parameters (`## Visium raw processing & QC`, `## snRNA-seq clustering`, ...),
  each line densely grounded with exact pipeline values (`"BayesSpace v1.11.0 spatialCluster(nrep=20000)
  over k=2..28; optimal k=9"`).
- ML/architecture genre (not in the two read ARAs, per schema): `architecture.md` (component graph:
  name/purpose/inputs/outputs/interactions per component), `algorithm.md` (LaTeX formulation +
  reconstructed pseudocode + complexity analysis "only if the paper states or clearly implies it").

**`heuristics.md`** (present only when the paper states implementation tricks/gotchas — optional even
among method-file-rich ARAs; neither che26 nor huu25 has one, but `ali25-multimodal-self-supervised-
learning-for-early` does). One `## H{NN}: {description}` block per heuristic:

| Field | Type | Real example |
|---|---|---|
| `**Rationale**` | markdown-prose | `"The learned gate α=σ(w^T[1_MRI,1_PET]) drives α→1 (so (1-α)→0) when PET is missing, enabling robust MRI-only inference..."` |
| `**Sensitivity**` | enum{`low`,`medium`,`high`} or `"Not specified in paper"` | `high — §3.8 plans to remove histogram matching / ComBat / both and measure cross-site impact (results not reported)` |
| `**Bounds**` | string — acceptable range/limits, or `"Not specified in paper"` | `α∈[0,1]; late fusion at embedding level` |
| `**Code ref**` | list[ref-path] to a real `src/execution/` file, or `"Not specified"` | `[src/execution/ssl_losses.py]` |
| `**Source**` | string — section/table in paper | `§3.4, Eq. 8, Figure 5` |

### A full realistic example

`constraints.md` (che26):
```markdown
## Boundary conditions
- Scope is limited to **blood-based p-tau biomarkers** (plasma or serum) for AD; only isoforms
  p-tau217, p-tau181, p-tau231 on platforms MS/Simoa/MSD/Lumipulse were compared.
- Findings are relative **rankings (P-scores) and AUC mean differences vs. a p181_IA baseline**, not
  absolute pooled sensitivity/specificity/AUC for each marker.

## Assumptions
- A2: Selecting the single most comprehensive dataset per cohort yields statistically independent
  nodes (no patient double-counted).

## Known limitations (§4.5)
- **Batch effects**: although platforms were adjusted for, batch effects in manual immunoassays may
  still exist.

## Additional caveats surfaced during compilation (data-quality notes)
- **Table 1 vs. its caption**: Table 1 lists **12 cohort rows**, but its caption says it details "the
  6 core representative cohorts..." ADNI is named in the caption and abstract as a screened
  overlapping cohort but has **no row** in Table 1. The 12 tabulated cohorts also do not equal the
  stated 18 studies / 24 datasets.
```

A heuristic block (from `ali25-multimodal-self-supervised-learning-for-early/logic/solution/heuristics.md`):
```markdown
## H03: Train-time PET→MRI distillation for MRI-only deployment
- **Rationale**: When both modalities are present in training, distilling stop-gradient PET
  embeddings into the MRI pathway (Eq. 11) retains molecular knowledge for later MRI-only inference.
- **Sensitivity**: Not specified in paper
- **Bounds**: Active only for subjects with PET; training-only (not at inference)
- **Code ref**: [src/execution/ssl_losses.py](../../src/execution/ssl_losses.py)
- **Source**: §3.4, Eq. 11
```

### Cardinality / variability
`constraints.md`: always exactly one file, 2–4 top-level sections, several bullets each. Method files:
0 to 3+ additional files depending on how the paper's method decomposes — che26 has just
`study_design.md` (one method file, since it's pure statistical synthesis); huu25 has
`study_design.md` + `method.md` (cohort/pipeline design split from detailed per-substage QC
parameters). `heuristics.md`, when present, typically has 3–8 `H##` blocks.

### Availability notes
`constraints.md` is mandatory core — never absent, though it can be thin (a bare "no limitations
stated" is a red flag, since essentially every paper states some caveat). Beyond it:
- **`heuristics.md` correctly absent** for most papers — do NOT penalize its absence generically; only
  penalize it when the paper visibly states implementation tricks/gotchas (e.g. an ML paper with an
  "Implementation details" subsection) and none were captured.
- **Method-file naming forced onto the wrong genre** is itself a defect: e.g. a `training.md`/
  `model.md` appearing for a paper that trained no model, or an `architecture.md` for a pure
  statistical-synthesis review — Seal Level 1 explicitly flags this (§2 of the validation checklist).
- **Data-quality-caveats subsection missing** when the source table/figure numbers actually don't
  reconcile (as in che26's Table 1 vs. caption mismatch) is a coverage gap a metric can specifically
  probe by cross-checking `evidence/` tables' own internal-consistency notes against whether
  `constraints.md` mentions them.
- Abstract-only sources: `constraints.md` reduces to whatever caveats the abstract itself states
  (often none), and no method file is generated at all beyond the bare mandatory `constraints.md` —
  a stark, easily-detected floor case.

---

