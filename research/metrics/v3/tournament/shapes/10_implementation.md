# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 10. `src/environment.md` + `src/artifacts.md` / `src/configs/*.md` / `src/execution/*`

### Artifact + path
`src/environment.md` (always present); `src/artifacts.md`, `src/configs/{name}.md`,
`src/execution/{module}.{py,r,...}`, `src/prompts/*` (all "as warranted"). Examples:
`research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/src/{environment.md,artifacts.md}`;
`research/ara-library/huu25-apoe-e4-alzheimer-s-risk-converges/src/{environment.md,artifacts.md}`;
`research/ara-library/aki26-molecular-signatures-of-resilience-to-alzheimer/src/{execution/pretrained_model.py,configs/pipeline_parameters.md}`.

### Purpose
The concrete, physical implementation layer — reproducibility metadata plus whatever real
code/config/artifact content the source actually contains, captured in native form rather than
re-encoded as prose. The governing rule: **capture every concrete artifact that exists; never
manufacture one that doesn't.** A prose-only method already lives in `logic/solution/` — duplicating
it here as a fabricated code stub is explicitly forbidden.

### Structure

**`src/environment.md`** (mandatory core, one per ARA):

| Field | Type | Real example |
|---|---|---|
| `**Language/runtime**` | string, or `"analytical — none"` for non-computational work | `"R versions 4.3 to 4.5 (Bioconductor 3.18 to 3.21); Python (nuclei-count workflow, LIANA+); Shell"` |
| `**Framework**` | string | `` `netmeta` R package, version **4.5.2** `` |
| `**Hardware**` | string, or `"n/a"` | `"Joint High Performance Computing Exchange (JHPCE) cluster, Johns Hopkins Bloomberg School..."` |
| `**Data sources**` | string/list | GEO accessions, cohort names, access levels |
| `**Key dependencies**` | string/list, versioned | `"SpaceRanger v2.1.0 (+ v4.0.1 segment), CellRanger v7.2.0; ... edgeR v4.6.2, limma v3.64.1, ..."` |
| `**Protocols**` | string | `"PRISMA-DTA. Prospectively registered on PROSPERO, CRD420261327845."` |
| `**Random seeds**` | string, or `"Not specified in paper"`/`"n/a"` | `"Not specified in paper (BayesSpace nrep=20000... are stated; explicit RNG seeds are in repo log files, not the manuscript)."` |

Often extended with a `## Code availability` subsection (markdown-prose explaining *why* no code
exists, when that's the case) and a `## Data availability` subsection (verbatim quote of the paper's
own Data Availability Statement).

**`src/artifacts.md`** (for non-code deliverables, or when a repo exists but wasn't cloned/captured
into `src/execution/`) — one block per artifact:

```markdown
## {Artifact name}
- **File(s) in repo**: {real path(s), verified to exist, or "not a repo file" for registrations}
- **Nature**: {tool / library / skill spec / system / dataset / registration}
- **What it does / contains**: {grounded description}
- **How to use / run**: {entry point, command, or interface}
- **Claims supported**: {C## ids, or "all"}
```
Field types: all markdown-prose strings except `Claims supported` (list[ref-id] or `all`).

**`src/configs/{name}.md`** — one file per config category the work actually has (e.g.
`pipeline_parameters.md`, `assay_parameters.md`), each a sequence of per-parameter blocks:

```markdown
## {Parameter name}
- **Value**: {exact value}
- **Rationale**: {why this value, or "Not specified in paper"}
- **Search range**: {if mentioned}
- **Sensitivity**: {low|medium|high|"Not specified in paper"}
- **Source**: {section/table}
```

**`src/execution/{module}.py`** (or `.r`, etc.) — present only when the source provides concrete
code-shaped content. First line always declares grounding:
```python
# Grounding: transcribed   — adapted from repo code; cite file:line in docstrings
# Grounding: reconstructed — from explicit paper pseudocode/equations; cite §/eq
```
`transcribed` files are copied faithfully in native form (full function bodies, real imports, real
CLI/argparse/logging scaffolding) — never stripped to signatures-only. `reconstructed` files are
minimal stubs of only the novel mechanism, typed signatures using only source-stated names, with
unspecified logic left as `raise NotImplementedError("Not specified in paper")`.

### A full realistic example

`src/environment.md` (che26 — the "no code" case, explicitly justified):
```markdown
# Environment

This is an **analytical secondary-data study** (systematic review + network meta-analysis). No
primary data were collected, no model was trained, and no analysis code or accessioned dataset was
released by the authors.

- **Language/runtime**: R (Foundation for Statistical Computing). Version not specified in paper.
- **Framework**: `netmeta` R package, version **4.5.2** — random-effects frequentist network
  meta-analysis (§2.5).
- **Hardware**: n/a (statistical synthesis of summary data).
...

## Code availability
No Code Availability statement; no GitHub/GitLab/Zenodo/OSF/Dryad repository is referenced in the
article or found via web search (sources.yaml, verified). As a summary-data NMA, no analysis code was
released — hence no `src/execution/` code files (a `.py` stub reconstructed from the prose methodology
would only duplicate `logic/solution/study_design.md`).
```

`src/artifacts.md` (huu25 — the "repo exists but wasn't cloned" case):
```markdown
## LFF_spatial_ERC analysis pipeline (R + Shell + Python)
- **File(s) in repo**: GitHub `LieberInstitute/LFF_spatial_ERC` (default branch `devel`). Verified
  top-level entries: `code/`, `processed-data/`, `raw-data/`, ... (verified via GitHub contents API).
- **Nature**: Full end-to-end analysis pipeline (specialized to this project's data).
- **What it does / contains**: `code/` numbered stages: `00_project_prep`, `01_spaceranger`, ...
  `14_MOFA` — multicellular factor analysis (Figure 6). ...
- **How to use / run**: `git clone` (README notes this may take up to an hour due to size); open
  `LFF_spatial_ERC.Rproj`; run stage scripts on an HPC/JHPCE-like environment.
- **Claims supported**: all (C01–C08).
```

`src/execution/pretrained_model.py` (aki26 — the `transcribed` case, real notebook code kept native):
```python
# Grounding: transcribed
# Source: pretrained_model.ipynb (author repo AkilaRanjith/Molecular-Signatures-of-Resilience...); code cells only (outputs stripped).

import os
import scanpy as sc
import scvi
...
vae_q = scvi.model.SCANVI.load_query_data(adata_query, "path to downloaded pretrained exc model")
vae_q.train(max_epochs=200, n_samples_per_label=2000, plan_kwargs=dict(weight_decay=0.0), check_val_every_n_epoch=10)
```

A config block (aki26 `src/configs/pipeline_parameters.md`):
```markdown
### Minimum genes per nucleus (initial → final)
- **Value**: initial filter <200 genes removed (→549,074); final cutoff **300** genes (tested 200–500)
- **Rationale**: Ex5 has low gene counts; 300 balances retention vs quality; separate rescue of
  200–300-gene nuclei (62,498; 48,849 kept at 99% scANVI probability).
- **Sensitivity**: high (drove a dedicated sensitivity analysis).
- **Source**: Methods; Supplementary Fig. 8.
```

### Cardinality / variability
`environment.md`: always exactly one. `artifacts.md`: 0–1 file but internally 1–4+ blocks (che26 has
3: PROSPERO registration, extracted summary-data, underlying cohorts; huu25 has 3: the analysis
pipeline, released processed-data objects, interactive web apps + Zenodo archive). `configs/`: 0 to
several files, each with anywhere from 3 (woj25's two-assay config) to a dozen+ per-parameter blocks
(aki26's pipeline_parameters.md has ~20). `execution/`: 0 to many files; when a repo is provided as
input, every real runnable file of substance (≥~30 lines or a named module/entrypoint) must be
captured, not merely pointed at.

### Availability notes
This is the artifact whose absence is most tightly conditioned on paper genre, and getting it wrong
in either direction is a checkable defect:
- **Correct absence**: a pure meta-analysis/systematic review with no released code (che26) legitimately
  has `environment.md` + `artifacts.md` and nothing else — Seal Level 1 explicitly forbids fabricating
  a `.py` stub here, since it would just duplicate `study_design.md`.
- **Correct near-absence despite real code existing**: huu25's underlying work has a full ~15GB GitHub
  repo with real R/Python/Shell code, yet `src/execution/` is legitimately absent in this ARA because
  the compiler explicitly did not clone the repo (stated in `artifacts.md`) — this is flagged
  in-artifact as a scope decision, not silently hidden. A tournament metric evaluating "does src/
  capture real code" must distinguish this honestly-disclosed non-capture from a silent coverage
  failure where a provided repo's code was dropped without comment.
- **Failure mode to penalize**: a provided repo's real source files reduced to a pointer in
  `artifacts.md` instead of being copied into `src/execution/` — explicitly called out as a FAIL
  condition in the validation checklist (§5, Implementation layer).
- **Failure mode to penalize (other direction)**: a `.py`/pseudo-code stub manufactured from a
  prose-only method description, or code with invented API names/constants/function bodies not
  traceable to any real source — also an explicit FAIL condition.
- **Grounding tag missing or wrong** on any `src/execution/*.py` file — every such file must open with
  `# Grounding: transcribed` or `# Grounding: reconstructed`; absence of this line is itself a defect.
- Abstract-only sources: `environment.md` is reduced to whatever the abstract states about
  methodology (often nothing computational at all) — `artifacts.md`/`configs/`/`execution/` are all
  absent, correctly, since nothing concrete is knowable.

---

