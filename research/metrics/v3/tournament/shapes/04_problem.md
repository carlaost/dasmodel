# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 4. `logic/problem.md` (problem statement)

### Artifact + path
`logic/problem.md`, e.g. `research/ara-library/huu25-apoe-e4-alzheimer-s-risk-converges/logic/problem.md`.

### Purpose
The "why" layer: what was empirically known before this work (Observations), what was missing or
broken (Gaps), the creative leap that resolves the gap (Key Insight), and the assumptions the whole
argument rests on. This is what lets a downstream agent understand *why* the paper's specific method
was chosen, not just what the method is.

### Structure

```markdown
# Problem Specification

## Observations
### O{N}: {title}
- **Statement**: {precise empirical fact, with numbers, drawn from the source's Introduction/prior work}
- **Evidence**: {citation(s) or section ref}
- **Implication**: {what this means for the problem}

## Gaps
### G{N}: {title}
- **Statement**: {what's missing or broken}
- **Caused by**: {observation IDs, e.g. O1, O2}
- **Existing attempts**: {what's been tried}
- **Why they fail**: {specific failure mode}

## Key Insight
- **Insight**: {the creative leap, precisely stated}
- **Derived from**: {observation IDs}
- **Enables**: {what solution approach this unlocks}

## Assumptions
- A1: {assumption}
- A2: {assumption}
```

| Field | Type | Real example |
|---|---|---|
| `### O{N}` heading | ref-id (O1, O2, ...) + string title | `### O2: Plasma p-tau isoforms are the most promising BBMs, but the optimal isoform is contested` |
| `**Statement**` (in O) | markdown-prose, often verbatim-quoting the source | `"Among candidate BBMs, plasma phosphorylated tau (p-tau) species are most promising. ... p-tau217 shows exceptional concordance with CSF/PET..."` |
| `**Evidence**` (in O) | string — citation list or section ref | `"§1 Introduction (Karikari et al., 2020; Mila-Aloma et al., 2022; ...)"` |
| `**Implication**` (in O) | markdown-prose | `"Inconsistent cross-cohort findings sustain an ongoing debate about which isoform is optimal..."` |
| `### G{N}` heading | ref-id (G1, G2, ...) + string title | `### G1: No consensus on the optimal p-tau isoform across disease stages` |
| `**Caused by**` (in G) | list[ref-id] of O-numbers | `O2, O5` |
| `**Existing attempts**` / `**Why they fail**` (in G) | markdown-prose | see example |
| `**Insight**` | markdown-prose, precise | `"Cast every biomarker+platform combination ... as a distinct node in a network meta-analysis..."` |
| `**Derived from**` | list[ref-id] of O-numbers | `O5, G1, G2, G3` (Key Insight may cite gaps too) |
| `**Enables**` | markdown-prose | `"A unified P-score (SUCRA-analogous) ranking that resolves the isoform, platform, and matrix debates..."` |
| `A{N}:` | ref-id + inline markdown-prose | `A2: Selecting the single most comprehensive dataset per cohort yields statistically independent nodes (no patient counted twice).` |

### A full realistic example

```markdown
### O2: Plasma p-tau isoforms are the most promising BBMs, but the optimal isoform is contested
- **Statement**: Among candidate BBMs, plasma phosphorylated tau (p-tau) species are most promising.
  Initial studies highlighted p-tau181; more recent evidence suggests p-tau217 and p-tau231 may
  offer superior accuracy and dynamic range. p-tau217 shows exceptional concordance with CSF/PET;
  p-tau231 may rise earliest in the preclinical phase; p-tau217 correlates more strongly with
  longitudinal decline and pathological staging.
- **Evidence**: §1 Introduction (Karikari et al., 2020; Mila-Aloma et al., 2022; Janelidze et al.,
  2023; Palmqvist et al., 2024; Ashton et al., 2024a,b; Ashton et al., 2021; Mattsson-Carlgren et
  al., 2023).
- **Implication**: Inconsistent cross-cohort findings sustain an ongoing debate about which isoform
  is optimal for clinical implementation.

### G1: No consensus on the optimal p-tau isoform across disease stages
- **Statement**: It is unknown which p-tau isoform (217, 181, or 231) is optimal for detecting Abeta
  pathology, tau pathology, and predicting cognitive decline, or whether the answer differs by
  disease stage.
- **Caused by**: O2, O5
- **Existing attempts**: Individual head-to-head studies and pairwise meta-analyses.
- **Why they fail**: They compare limited assay pairs in single cohorts, cannot integrate indirect
  evidence, and produce inconsistent conclusions.

## Key Insight
- **Insight**: Cast every biomarker+platform combination (e.g., p217_MS, p217_Ratio, p181_IA,
  p231_UGOT) as a distinct node in a network meta-analysis. This lets direct (head-to-head) and
  indirect evidence be integrated to rank all options simultaneously with a single reference
  comparator (p181_IA), across four separate diagnostic outcomes, while a hierarchical
  cohort-selection rule preserves statistical independence.
- **Derived from**: O5, G1, G2, G3
- **Enables**: A unified P-score (SUCRA-analogous) ranking that resolves the isoform, platform, and
  matrix debates in one framework, and supports stage-specific clinical recommendations.

## Assumptions
- A2: Selecting the single most comprehensive dataset per cohort yields statistically independent
  nodes (no patient counted twice).
```

### Cardinality / variability
Typically 3–5 Observations, 2–4 Gaps, exactly one Key Insight block, 3–5 Assumptions. RCTs tend to
have Observations framed around disease epidemiology and prior-trial results, with a single crisp Gap
("no approved therapy demonstrates X at an acceptable safety margin"); lab/mechanistic papers have
denser, more technical Observations (assay/cell-biology facts) and Gaps about unresolved cell-type or
pathway attribution; meta-analyses have Gaps about methodological fragmentation (as in the che26
example above).

### Availability notes
Mandatory core, never absent. Degradation signals:
- **Abstract-only sources** produce Observations that are just restatements of the abstract's
  background sentence, with `Evidence: Abstract` for every one of them — no section-level citations,
  no depth. This should score as materially weaker than an Observation grounded in an Introduction
  citation chain.
- **A Key Insight that merely restates the paper's method name** (rather than stating the actual
  creative leap connecting Observations/Gaps to the solution) indicates a shallow read; a real
  compiler run derives it from the actual `Derived from` chain, not the title.
- Gaps with generic `Existing attempts`/`Why they fail` (e.g. "prior work is limited") without
  specifics is a compression/laziness signal a metric should catch, distinguishable from a genuinely
  short paper by cross-checking against `related_work.md` breadth.

---

