# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 5. `logic/experiments.md` (declarative verification/analysis plans)

### Artifact + path
`logic/experiments.md`, e.g. `research/ara-library/huu25-apoe-e4-alzheimer-s-risk-converges/logic/experiments.md`.

### Purpose
"Experiment" generalized to the field's way of testing a claim — an eval run, a statistical test, a
sequencing+clustering pipeline stage, a clinical-trial analysis, a proof obligation. These are
**declarative plans, never scripts, and contain NO exact numerical results** — exact numbers live only
in `evidence/`. This file is what `claims.md`'s `Proof` field points into.

### Structure
One `## E{NN}: {Short title}` block per experiment/analysis. Every block has:

| Field | Type | Real example |
|---|---|---|
| `**Verifies**` | list[ref-id] — claim IDs from claims.md | `C01, C02, C05, C06` |
| `**Setup**` | nested key: value bullets — subkeys vary by field (`Design`, `Model`, `Hardware`, `Dataset`, `System`, `Assay`, `Sequencing`, `Pipeline`, `Reference standard`, etc. — free-form, whatever the work has) | `Assay: 10x Visium spatial gene expression, one section per donor, 31 samples` / `Pipeline: VistoSeg → SpaceRanger (GRCh38, 2020-A) → spatialLIBD QC → SpotSweeper → nnSVG → harmony → BayesSpace` |
| `**Procedure**` | numbered list[string], each an imperative step | `1. Segment slides, align capture areas, run SpaceRanger; QC spots (manual + SpotSweeper).` |
| `**Metrics**` | markdown-prose or list, what is measured (with units), NOT the value | `"per-SpD DEG counts (up/down, FDR<0.05); enriched GO terms; ancestry/sex-specific DEG counts."` |
| `**Expected outcome**` | list[string], directional/relative language ONLY — never an exact number | `"DEGs concentrate in white-matter and vascular SpDs; ancestry-specific sets differ; male-dominated sex-specific sets."` |
| `**Baselines**` | string — comparator method/group, or `none` | `"within-study comparison across SpDs."` or `"p181_IA reference comparator."` |
| `**Dependencies**` | list[ref-id] of other experiment IDs, or `none` | `E02` or `none` |

### A full realistic example

```markdown
## E03: APOE carrier DGE in spatial domains (+ ancestry- and sex-specific)
- **Verifies**: C03, C05, C06
- **Setup**: Visium pseudobulk per SpD (registration_pseudobulk, min_ncells=10); edgeR filtering;
  voomLmFit + limma.
- **Procedure**:
  1. Fit carrier model `~0 + APOE_syn + Sex + Age + Anc_Afr + pseudo_expr_chrM_ratio`, block on
     Visium slide; contrast E4+ vs E2+.
  2. Repeat with ancestry-combined covariate (carrier_Anc) and sex-combined covariate (carrier_Sex,
     excluding X/Y genes).
  3. GO overrepresentation on DEG sets (clusterProfiler).
- **Metrics**: per-SpD DEG counts (up/down, FDR<0.05); enriched GO terms; ancestry/sex-specific DEG
  counts.
- **Expected outcome**: DEGs concentrate in white-matter and vascular SpDs; ancestry-specific sets
  differ; male-dominated sex-specific sets.
- **Baselines**: within-study comparison across SpDs.
- **Dependencies**: E02
```

### Cardinality / variability
Seal Level 1 targets ≥3 blocks (never padded to hit the number). The two read ARAs have 6 (che26,
each block = one NMA outcome/subgroup analysis) and 8 (huu25, each block = one pipeline
stage/analysis: atlas-building, DGE, GO, trajectory, cross-dataset enrichment, MOFA). `Setup` subkeys
adapt heavily to genre: ML papers use `Model`/`Hardware`/`Dataset`; clinical trials use
`Population`/`Intervention`/`Endpoint`/`Randomization`; wet-lab/omics papers use
`Assay`/`Sequencing`/`Reference standard`; theory papers might replace `Procedure` steps with proof
obligations. The one invariant is **no exact numbers anywhere in this file**.

### Availability notes
Mandatory core. What signals thinness or a defect:
- **A number leaking into `Expected outcome` or `Metrics`** (e.g. "achieves 92% accuracy" instead of
  "achieves higher accuracy than baseline") is an explicit Critical Rule #3 violation — exact numbers
  belong only in `evidence/`. A metric can grep for digit patterns here as a cheap defect detector.
  (Percent symbols, CIs, and p-value thresholds that are themselves the *design* of the study — e.g. "FDR<0.05" as a stated significance threshold — are acceptable since they describe the test's decision rule, not its result.)
- **`Proof`/`Verifies` not resolving** — every `C##` cited here must exist in `claims.md` and every
  `E##` an experiment's `Dependencies` cites must exist in this same file (cross-layer binding, Seal
  Level 1 §9). A dangling reference is a structural defect.
  (Note: `Proof` lives on the *claim* block in `claims.md`, and it must point to an `E##` id here;
  `Verifies` lives on the *experiment* block here and must point back to a `C##` id in `claims.md` —
  the check runs in both directions.)
- **Systematic reviews / meta-analyses**: `Setup.Hardware`/`Model` fields are typically absent or
  `n/a`; `Setup.Design` (statistical model spec) dominates instead — this is correct, not thin.
- **Abstract-only compilation**: often produces the statutory minimum 3 experiments with generic,
  interchangeable `Procedure` steps inferred from the abstract's method sentence rather than a real
  Methods section — visibly less specific `Setup` detail than a full-text compile.

---

