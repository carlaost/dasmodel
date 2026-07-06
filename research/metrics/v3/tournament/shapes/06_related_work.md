# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 6. `logic/related_work.md` (typed dependency graph)

### Artifact + path
`logic/related_work.md`, e.g. `research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/logic/related_work.md`.

### Purpose
A typed graph of how this work depends on, extends, bounds, is baselined against, or refutes prior
work — preserving the paper's *full* citation footprint (not just the closest predecessors), so a
downstream agent can trace provenance of data, methods, and comparator claims.

### Structure
Full blocks for every citation with a **specific technical delta** (a dataset it supplied, a method it
contributed, a claim it bounds/extends/refutes):

```markdown
## RW{NN}: {Author et al., Year}
- **DOI**: {DOI or arXiv ID, or "Not specified in paper"}
- **Type**: {imports|bounds|baseline|extends|refutes}
- **Delta**:
  - What changed: {specific technical delta}
  - Why: {motivation}
- **Claims affected**: {claim IDs, or "none directly (motivation)"}
- **Adopted elements**: {what was kept/reused}
```

| Field | Type | Real example |
|---|---|---|
| `## RW{NN}` heading | ref-id + string | `## RW01: Janelidze et al., 2023` |
| `**DOI**` | string | `10.1093/brain/awac333` |
| `**Type**` | enum{`imports`, `bounds`, `baseline`, `extends`, `refutes`} (compound forms seen, e.g. `imports (data source)`, `imports (framework)`, `baseline / bounds`) | `imports (data source)` |
| `**Delta** → What changed` | markdown-prose | `"head-to-head comparison of 10 plasma phospho-tau assays in prodromal AD."` |
| `**Delta** → Why` | markdown-prose | `"selected as the most comprehensive head-to-head dataset for the BioFINDER-1 cohort."` |
| `**Claims affected**` | list[ref-id] of claim IDs, or `none` | `C01, C07` |
| `**Adopted elements**` | markdown-prose | `"BioFINDER-1 dataset (N=135; MCI/prodromal AD; p-tau 217/181/231; IP-MS and Simoa; CSF Abeta42/40)."` |

Beyond the full `RW##` blocks, remaining citations without a specific technical delta (background,
historical, infrastructure, inline-comparison references) are captured **briefly**, typically as a flat
bulleted list grouped under a heading like `## Background / supporting references (brief)` or folded
into an `## Additional citation footprint (briefer)` section — one bullet per reference:
`**Author et al., Year** (DOI) — one-line role.`

A special case seen in both real ARAs: a **non-bibliographic grounded source** the paper itself
depends on but that isn't an "RW" citation — e.g. a trial/review registration. This is folded in as its
own small block before the numbered RW list, e.g. `## Review registration (folded-in grounded source)`.

### A full realistic example

```markdown
## RW01: Janelidze et al., 2023
- **DOI**: 10.1093/brain/awac333
- **Type**: imports (data source)
- **Delta**:
  - What changed: head-to-head comparison of 10 plasma phospho-tau assays in prodromal AD.
  - Why: selected as the most comprehensive head-to-head dataset for the BioFINDER-1 cohort.
- **Claims affected**: C01, C07
- **Adopted elements**: BioFINDER-1 dataset (N=135; MCI/prodromal AD; p-tau 217/181/231; IP-MS and
  Simoa; CSF Abeta42/40).

## Background / supporting references (brief)
- **Hansson et al., 2023** (10.1038/s41582-023-00403-3) — blood biomarkers in clinical practice/trials; motivation.
- **Schindler et al., 2022** (10.1212/WNL.0000000000200358) — effect of race on plasma-based amyloid prediction; cross-ethnic motivation (C05).
```

### Cardinality / variability
Full `RW##` block count scales with how many primary sources/datasets/methods the paper actually
draws on: che26 (a meta-analysis synthesizing 18 studies) has 16 full RW blocks (12 "included primary
studies," 4 "conceptual/methodological anchors") plus ~19 brief background references; huu25 (a
single-cohort wet-lab study) has 18 full RW blocks (mostly method/tool citations: BayesSpace, Harmony,
spatialLIBD, RCTD, LIANA+, MOFAcellulaR, ...) plus a long "additional citation footprint" grouping
~40 more references by reference-number range. A theory paper's RW graph skews toward `extends` and
`bounds` types (prior theorems it builds on/is bounded by); a meta-analysis skews toward `imports
(data source)`; an applied ML paper skews toward `baseline` (methods it benchmarks against).

### Availability notes
Mandatory core, never structurally absent. Signals of thinness:
- **Only full RW blocks, no "brief" tier** — means the compiler didn't sweep the full References list,
  failing the coverage requirement that the ARA "reflect the paper's full citation footprint," not
  just the closest predecessors (Seal Level 1 explicitly checks for this).
- **`refutes`-type edges are rare in practice** — most papers build on rather than refute prior work;
  their absence is normal, not a defect, unless the source paper explicitly states it's overturning a
  specific prior finding and the ARA fails to capture that edge.
- Abstract-only sources: `related_work.md` will contain at most 1–3 RW blocks (whatever's citable from
  the abstract itself) and no meaningful "brief" tier — a stark, scoreable gap versus a full-text
  compile with 15+ blocks.

---

