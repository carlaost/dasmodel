# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 11. `data/dataset.md` (+ `data/preprocessing.md`)

### Artifact + path
`data/dataset.md`, optionally `data/preprocessing.md`. Present only for data-driven work. Examples:
`research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/data/dataset.md` (secondary
summary-data reuse case), `research/ara-library/huu25-apoe-e4-alzheimer-s-risk-converges/data/dataset.md`
(primary-data-generation case).

### Purpose
Provenance, access, and structural description of the dataset(s) the work is built on — whether the
paper *generated* new data (with accessions, consent/IRB, and technical specs) or merely *reused*
existing summary statistics from prior studies. This is what tells a downstream agent whether the
work's numbers are independently reproducible from public data or gated behind consortium access.

### Structure
Free-form markdown-prose organized under `##` headings; no fixed field schema, but recurring
sub-blocks across both genres:

| Section | Type | Notes |
|---|---|---|
| Intro paragraph | markdown-prose | states data type (primary-generated vs. secondary-reused), total N, and whether primary patient-level data were released |
| `## {Accession} — {short description}` (one per generated dataset) | markdown-prose, structured sub-bullets | present only for primary-data-generation papers |
| `**Provenance**` (within an accession block) | string | how/what was generated, instrument, depth |
| `**Source / access**` (within an accession block) | string, states **access tier explicitly** | `"GEO record/metadata and processed data are **open**. **Raw sequencing reads are controlled access via dbGaP**"` |
| `**Size / content**` (within an accession block) | string, exact dims | `"SpatialExperiment spe_ERC_annotated = 30,494 genes × 122,202 in-tissue spots"` |
| `**Licensing / consent**` (within an accession block) | string | IRB/consent framework |
| `**Key variables**` (within an accession block) | list/string | covariates available |
| `## Provenance and access` (secondary-reuse genre) | markdown-prose | states release status verbatim from the paper's Data Availability Statement |
| `## Included cohorts` (secondary-reuse genre) | markdown-table | cohort-level provenance table (see example) |
| `## External datasets used (not generated here)` | markdown-prose bullets | cross-referenced datasets used only for validation/enrichment, not the study's own data |
| `## Consent / ethics` | markdown-prose | IRB numbers, or "not applicable at the review level" for secondary-data work |
| `## Preprocessing` | markdown-prose, or pointer to `data/preprocessing.md` / `logic/solution/method.md` | QC/cleaning/normalization steps |

### A full realistic example

Primary-data-generation genre (huu25):
```markdown
## GSE307990 — Visium spatially-resolved transcriptomics (SRT), human ERC
- **Provenance**: Generated in this study; 10x Genomics Visium Spatial Gene Expression, one section
  per donor (31 samples), NovaSeq 6000, min 60,000 reads/spot; SpaceRanger v2.1.0 (GRCh38, 2020-A).
- **Source / access**: NCBI GEO accession GSE307990 — https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE307990 .
  GEO record/metadata and processed data are **open**. **Raw sequencing reads are controlled access
  via dbGaP** (postmortem human genomic data).
- **Size / content**: Processed SpatialExperiment `spe_ERC_annotated` = 30,494 genes × 122,202
  in-tissue spots (post-QC), 9 annotated spatial domains.
- **Licensing / consent**: Postmortem human tissue under IRB #12-24 (Maryland DoH), WCG #20111080
  (Santa Clara ME), NIH #90-M-0142 (NIMH IRP), informed consent from legal next-of-kin.
- **Key variables**: APOE carrier (E2+/E4+), ancestry (AA/EA), sex, age, Braak (18 donors), CERAD,
  pTau status (t+/t−), spatial domain, Visium slide.
```

Secondary-reuse genre (che26):
```markdown
## Provenance and access
- **Type**: secondary summary data extracted from published diagnostic-accuracy studies.
- **Release status**: no accessioned dataset; "included in the article/Supplementary material,
  further inquiries can be directed to the corresponding author." (Data Availability statement, verbatim).
- **Registration**: PROSPERO CRD420261327845 (open).

## Included cohorts (from Table 1; access controlled/by-request via each consortium)
| Cohort | Source study | N | Disease stage | Reference standard | Platform/manufacturer |
|--------|--------------|---|---------------|--------------------|-----------------------|
| BioFINDER-1 | Janelidze et al. (2023) | 135 | MCI (prodromal AD) | CSF Abeta42/40 | IP-MS and Simoa |
| TRIAD | Benedet et al. (2026) | 100 | AD continuum | Amyloid-PET | Automated IA (serum focus) |

## Consent / ethics
- Not applicable at the review level (secondary summary data). Individual cohorts carry their own
  IRB approvals and consent (not restated in this article).
```

### Cardinality / variability
0 or 1 `data/` directory per ARA (che26 and huu25 both have exactly one `data/dataset.md`; a pure
theory or code-tool paper would have none). Number of accession/cohort blocks scales with how many
distinct datasets the work touches — huu25 has 2 generated accessions + 4 external reference datasets;
che26 has 12 reused cohorts (from Table 1) + 3 additionally-named screened cohorts. `preprocessing.md`
as a *separate* file is less common than folding preprocessing into `logic/solution/method.md` (as
huu25 does) — both are valid; which one the compiler picks tracks how much QC/preprocessing detail
exists relative to the rest of the method.

### Availability notes
`data/` is the most genre-conditioned "as warranted" directory in the schema:
- **Correctly absent**: pure theory papers, tool/spec releases with no dataset, and code-only papers
  legitimately have no `data/` directory at all — this must not be penalized as a gap.
- **Access-tier honesty is the key scoring axis** for data-driven work: a well-compiled
  `dataset.md` states explicitly which parts are open (metadata, processed objects) vs.
  controlled-access (raw reads via dbGaP, cohort data via consortium request) — collapsing this
  distinction into a blanket "available" or "not available" is a real defect a metric can check by
  looking for the co-occurrence of both an access claim and its qualifier.
- **Secondary-reuse papers cannot have a `Preprocessing` section describing raw-data QC** (there is no
  raw data) — their `dataset.md` correctly ends at cohort-level provenance; expecting cell/read-level
  QC parameters here would be a genre-mismatched expectation.
- **Internal count mismatches**: che26's own `dataset.md` explicitly flags that its 12 tabulated
  cohorts don't sum to the paper's stated "18 studies / 24 independent datasets" — a well-compiled
  ARA surfaces this discrepancy rather than silently picking one number, and a metric can check
  whether such stated-vs-tabulated mismatches are flagged anywhere in the ARA (here, cross-referenced
  in `constraints.md` too) rather than left uncommented.
- Abstract-only sources: `data/dataset.md`, if generated at all, will state only the sample size/
  population mentioned in the abstract (e.g. "N=4,736 participants") with no accession, no access
  tier, no cohort table — a clear floor case distinguishable from a real provenance record.

---

## Final enumerated artifact list (drives the tournament)

| # | Artifact | Path pattern | Mandatory core? |
|---|---|---|---|
| 1 | Root manifest | `PAPER.md` | Yes |
| 2 | Claims | `logic/claims.md` | Yes |
| 3 | Concepts | `logic/concepts.md` | Yes |
| 4 | Problem statement | `logic/problem.md` | Yes |
| 5 | Experiments (analysis plans) | `logic/experiments.md` | Yes |
| 6 | Related work (typed dependency graph) | `logic/related_work.md` | Yes |
| 7 | Solution / method layer | `logic/solution/constraints.md` + warranted method files (`study_design.md`, `method.md`, `heuristics.md`, `architecture.md`, `algorithm.md`, ...) | `constraints.md` yes; siblings as warranted |
| 8 | Exploration tree (research DAG) | `trace/exploration_tree.yaml` | Yes |
| 9 | Evidence (index + tables + figures) | `evidence/README.md`, `evidence/tables/*.md`, `evidence/figures/*.md` (+ `.png` siblings; `evidence/proofs/*.md` as warranted) | Yes |
| 10 | Implementation / reproduction layer | `src/environment.md` (+ `src/artifacts.md`, `src/configs/*.md`, `src/execution/*` as warranted) | `environment.md` yes; rest as warranted |
| 11 | Dataset descriptors | `data/dataset.md` (+ `data/preprocessing.md`) | As warranted (data-driven work only) |

11 top-level artifact sections, above the "Final enumerated artifact list" summary table.
