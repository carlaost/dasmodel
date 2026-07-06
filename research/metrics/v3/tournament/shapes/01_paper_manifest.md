# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 1. `PAPER.md` (root manifest)

### Artifact + path
`PAPER.md` at the ARA root, e.g. `research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/PAPER.md`.

### Purpose
The single entry point and progressive-disclosure Level-1 view (~200 tokens) of the whole ARA. An
agent reads only this file to decide whether the paper is relevant before drilling into any layer.
It is the manifest: bibliographic identity, one-paragraph synthesis of the contribution, and an
index of every other file the compiler actually generated for this paper.

### Structure

YAML frontmatter (between `---` fences) — every key is mandatory except where noted:

| Field | Type | Real example |
|---|---|---|
| `title` | string | `"Diagnostic performance of plasma p-Tau217, p-Tau181, and p-Tau231 across the Alzheimer's disease continuum: a network meta-analysis"` |
| `authors` | list[string] | `["Xiaofeng Chen", "Tingting Huang", "Chao Shi", "Shuizhi Xu", "Shuwei Fan"]` |
| `year` | int | `2026` |
| `venue` | string | `"Frontiers in Aging Neuroscience"` |
| `doi` | string (DOI or arXiv ID, or "Not specified in paper") | `"10.3389/fnagi.2026.1834591"` |
| `ara_version` | string | `"1.0"` |
| `domain` | string, free text | `"Alzheimer's disease diagnostics — blood-based biomarkers; Bayesian/frequentist network meta-analysis of diagnostic test accuracy"` |
| `keywords` | list[string], 5–10 items | `["Alzheimer's disease continuum", "diagnostic performance", "network meta-analysis", ...]` (10 items) |
| `claims_summary` | list[string], one line per main claim (mirrors `logic/claims.md` count) | `["Plasma p-tau217 measured by mass spectrometry (p217_MS) has the highest diagnostic accuracy for amyloid-beta pathology (P-score = 0.859), far outranking standard p-tau181 immunoassay (P-score = 0.117)."]` (7 lines in this ARA, one per claim group) |
| `abstract` | string, full paper abstract verbatim | (full ~250-word abstract, verbatim from the source) |

Body (markdown, after the closing `---`):

| Block | Type | Notes |
|---|---|---|
| `# {Paper Title}` | markdown H1 | repeats the title |
| `## Overview` | markdown-prose, 1–2 paragraphs | free-form synthesis of the contribution |
| `## Layer Index` | structured markdown | one sub-table per layer that actually has files (see below) |

The Layer Index is itself structured — one table per present layer, each row a
`[relative/path.md](relative/path.md) \| one-line description` pair:

- `### Cognitive Layer (/logic)` — table columns `File \| Description`
- `### Physical Layer (/src)` (sometimes titled "Implementation Layer") — table columns
  `File \| Description` or `File \| Description \| Claims` (a third column linking files to `C##` ids)
- `### Data Layer (/data)` — present only when `data/` exists
- `### Exploration Graph (/trace)` — table columns `File \| Description`, description states the node
  count, e.g. `"14-node research DAG of the review's decision trajectory"`
- `### Evidence (/evidence)` — table columns `File \| Description`; description states counts, e.g.
  `"Index of 2 tables + 3 figures"`

### A full realistic example

```markdown
---
title: "Diagnostic performance of plasma p-Tau217, p-Tau181, and p-Tau231 across the Alzheimer's disease continuum: a network meta-analysis"
authors: ["Xiaofeng Chen", "Tingting Huang", "Chao Shi", "Shuizhi Xu", "Shuwei Fan"]
year: 2026
venue: "Frontiers in Aging Neuroscience"
doi: "10.3389/fnagi.2026.1834591"
ara_version: "1.0"
domain: "Alzheimer's disease diagnostics — blood-based biomarkers; Bayesian/frequentist network meta-analysis of diagnostic test accuracy"
keywords: ["Alzheimer's disease continuum", "diagnostic performance", "network meta-analysis", "plasma biomarkers", "plasma phosphorylated tau 181", "plasma phosphorylated tau 217", "plasma phosphorylated tau 231", "mass spectrometry", "automated immunoassay", "p-tau217/Abeta42 ratio"]
claims_summary:
  - "Plasma p-tau217 measured by mass spectrometry (p217_MS) has the highest diagnostic accuracy for amyloid-beta pathology (P-score = 0.859), far outranking standard p-tau181 immunoassay (P-score = 0.117)."
  - "The p-tau217/Abeta42 ratio on automated platforms yields a significant incremental AUC gain of 0.025 (95% CI 0.005-0.045; I2 = 0%) over single-analyte assays."
abstract: "Blood-based biomarkers (BBMs) are transforming the diagnostic workflow for Alzheimer's disease (AD). ... [full abstract]"
---

# Diagnostic performance of plasma p-Tau217, p-Tau181, and p-Tau231 across the Alzheimer's disease continuum: a network meta-analysis

## Overview

This is a PRISMA-DTA systematic review and network meta-analysis (NMA) that, for the first time,
simultaneously compares plasma phosphorylated-tau isoforms ... The review is prospectively
registered on PROSPERO (CRD420261327845). No analysis code or accessioned primary dataset was
released; the work reuses extracted summary AUC statistics from established AD cohorts.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations (biomarker/platform heterogeneity) → gaps → key insight (simultaneous NMA) |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01-C08) with pooled diagnostic-performance findings |
| [concepts.md](logic/concepts.md) | 13 technical terms (p-tau isoforms, P-score/SUCRA, NMA, AUC, ratio metric, matrices, AT(N)) |
| [experiments.md](logic/experiments.md) | 6 declarative NMA/analysis plans (E01-E06), directional only |
| [related_work.md](logic/related_work.md) | Typed dependency graph over the paper's 30 references + PROSPERO registration |
| [solution/study_design.md](logic/solution/study_design.md) | PRISMA-DTA search, inclusion/exclusion, cohort de-overlap, NMA model, ranking |
| [solution/constraints.md](logic/solution/constraints.md) | Limitations, assumptions, boundary conditions |

### Physical Layer (`/src`)
| File | Description |
|------|-------------|
| [environment.md](src/environment.md) | Analytical environment: netmeta R package, PROSPERO protocol, cohorts, data access |
| [artifacts.md](src/artifacts.md) | Non-code deliverables: PROSPERO registration, extracted summary-data (no released dataset/code) |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 14-node research DAG of the review's decision trajectory |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Index of 2 tables + 3 figures |
| [tables/table1.md](evidence/tables/table1.md) | Characteristics of included studies and cohorts |
| [tables/table2.md](evidence/tables/table2.md) | SUCRA-based P-score rankings across 4 outcomes |
| [figures/figure1.md](evidence/figures/figure1.md) | PRISMA flow diagram of study selection |
| [figures/figure2.md](evidence/figures/figure2.md) | Evidence network plots (Abeta, Tau-PET) |
| [figures/figure3.md](evidence/figures/figure3.md) | Forest plots of AUC mean differences vs. p-tau181 baseline |
```

### Cardinality / variability
Exactly one `PAPER.md` per ARA — never zero, never more than one. `claims_summary` length always
equals (or closely tracks) the number of top-level claim groups in `claims.md` (self-consistency
check). The Layer Index adapts: a data-rich genomics preprint (huu25) has a `### Data Layer (/data)`
table and a `Claims` column in its Physical Layer table; a pure meta-analysis (che26) has neither the
extra column nor much in `/src`. A theory paper would instead show `evidence/proofs/` rows.

### Availability notes
`PAPER.md` itself is never absent (Seal Level 1 fails the whole ARA otherwise) — but its **richness**
varies with paper genre and is a real scoring axis:
- **Paywalled / abstract-only source**: `abstract` may be the only rich field; `domain`/`keywords`
  still populate from title+abstract, but `claims_summary` will be thin (fewer, vaguer lines) and the
  Layer Index will show correspondingly thin `logic/`/`evidence/` files — this should be *penalized*,
  not silently treated as equivalent to a full compilation.
- **doi**: for datasets/cohorts without a formal DOI, or for non-indexed preprints, this is
  `"Not specified in paper"` rather than fabricated.
- **Frontmatter/Layer-Index count mismatch** is itself a defect Seal Level 1 checks for (§12 of the
  validation checklist): if `claims_summary` lists 7 items but `claims.md` has 8 `## C##` blocks, that
  is a self-consistency failure a metric should catch.

---

