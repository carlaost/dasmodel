# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 9. `evidence/` (README.md index + `tables/*.md` + `figures/*.md`)

### Artifact + path
`evidence/README.md`, `evidence/tables/table{N}.md` (+ sibling `.png`), `evidence/figures/figure{N}.md`
(+ sibling `.png`); optionally `evidence/proofs/{name}.md` for theory/derivation work (not present in
either fully-read example ARA, but specified by the schema for theorem/lemma statements + proof
sketches). Example: `research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/evidence/{README.md,tables/table1.md,tables/table2.md,figures/figure1.md,figures/figure2.md,figures/figure3.md}` (plus matching `.png` files).

### Purpose
The grounded, verbatim record of every numbered table and figure in the source, transcribed
completely and in order — the raw material every number in `claims.md` ultimately traces back to.
This is a **systematic sweep**, not a sample: every `Table N`/`Figure N` in the main text (and
appendices) gets filed, or is explicitly accounted for in `README.md` with a reason if deliberately
skipped (e.g. an exact duplicate, or supplementary material not present in the fetched source).

### Structure

**`evidence/README.md`** — an index:
```markdown
# Evidence Index

## Tables
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/{name}.md](tables/{name}.md) | Table N, §X.Y | C01, C02 | {one sentence} |

## Figures
| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/{name}.md](figures/{name}.md) | Figure N, §X.Y | C03 | {one sentence} |

## Completeness note / Supplementary objects — accounted for, not filed
{prose explaining exactly what was filed, what wasn't, and why}
```
Fields: `File` = ref-path; `Source` = string (`"Table 2, §3.2-3.5"`); `Claims` = list[ref-id] or `—`;
`Description` = one-line string. The closing prose section is mandatory-in-spirit even though
free-form: it must state the exact count of numbered objects in the source and confirm none were
silently skipped, or name precisely which ones were not filed and why.

**`evidence/tables/{name}.md`** (+ sibling `.png`):

| Field | Type | Real example |
|---|---|---|
| `# Table {N} - {Caption or short description}` | markdown H1 | `# Table 2 - Ranking of diagnostic accuracy based on SUCRA values` |
| `**Source**` | string | `"Table 2 in \"Diagnostic performance of plasma p-Tau217...\" (Chen et al., 2026), page 6"` |
| `**Caption**` | string, verbatim or near-verbatim | `"Ranking of diagnostic accuracy based on SUCRA values."` |
| `**Screenshot**` | ref-filename | `table2.png` |
| `**Extraction type**` | enum{`raw_table`, `derived_subset`} | `raw_table` |
| (if `derived_subset`) `**Derived from**` | ref-filename of the parent raw table | `` `table3_imagenet_validation.md` `` |
| table body | markdown-table, exact cell values, never rounded | see example below |
| `**Notes**` (optional) | markdown-prose bullets — caveats, internal-consistency flags | see example below |

**`evidence/figures/{name}.md`** (+ sibling `.png`) — shared header on every figure regardless of
type, then a type-specific body:

| Field | Type | Real example |
|---|---|---|
| `**Source**` | string | `"Figure 3, Section 3.2 / 3.4, page 6"` |
| `**Caption**` | string, verbatim/near-verbatim | full caption text |
| `**Screenshot**` | ref-filename | `figure3.png` |
| `**Figure type**` | enum{`quantitative_plot`, `diagram`, `qualitative_sample`, `mixed`} | `quantitative_plot` |
| `**Extraction method**` | enum{`exact_from_labels`, `digitized_estimate`, `visual_description`} | `exact_from_labels` |
| `**Reading confidence**` | enum{`high`, `medium`, `low`} | `high` |

Type-specific body:
- **`quantitative_plot`**: `**Plot kind**` enum{line,bar,scatter,box,histogram,heatmap,forest plot,...};
  `**Axes**` string stating label/units/**scale** (`linear`|`log`) for X and Y; a markdown data table
  (columns = X + one per series; values `≈`-prefixed if `digitized_estimate`, bare if
  `exact_from_labels`); a `## Trend summary` prose paragraph (mandatory even when exact points are
  unreadable — in that case `Reading confidence: low` plus the trend summary substitutes for the
  table).
- **`diagram`**: NO data table. A `## Visual description` block with `**Components**`,
  `**Connections**`, `**Annotations**`, `**What it conveys**` — all markdown-prose strings.
- **`qualitative_sample`**: NO data table. A `## Visual description` block with `**Shows**`,
  `**Demonstrates**`, `**Supports**` (the last a claim/gap ref-id).
- **`mixed`**: figure is split per panel, each panel classified and handled per its own type (a
  diagram panel gets a Visual description, a data panel gets a table) — never collapsed together.

### A full realistic example

`evidence/tables/table2.md` (raw_table):
```markdown
# Table 2 - Ranking of diagnostic accuracy based on SUCRA values

**Source**: Table 2 in "Diagnostic performance of plasma p-Tau217, p-Tau181, and p-Tau231 across the
Alzheimer's disease continuum: a network meta-analysis" (Chen et al., 2026), page 6
**Caption**: "Ranking of diagnostic accuracy based on SUCRA values." Footnote: "SUCRA (surface under
the cumulative ranking) and P-scores for each biomarker across different diagnostic outcomes."
**Screenshot**: table2.png
**Extraction type**: raw_table

Values are P-scores (SUCRA analog, 0-1); higher = higher probability of being the best test. "—" = no
entry (fewer nodes ranked for that outcome).

| Rank | Outcome 1: diagnostic accuracy (Aβ pathology) — Biomarker (P-score) | ... |
|------|--------------------------------------------------------------------|-----|
| 1 | p217_MS (0.859) | ... |
| 8 | p181_IA (0.117) | ... |

**Notes**:
- Node labels: p217 = p-tau217, p181 = p-tau181, p231 = p-tau231; MS = mass spectrometry...
- p217_MS ranks 1st on all four outcomes.
```

`evidence/figures/figure3.md` (`quantitative_plot`, `exact_from_labels`):
```markdown
# Figure 3 - Relative diagnostic performance of plasma p-tau biomarkers vs. p-Tau181 (IA)
- **Source**: Figure 3, Section 3.2 / 3.4, page 6
- **Caption**: "Relative diagnostic performance of plasma p-tau biomarkers compared to p-Tau181 (IA). ..."
- **Screenshot**: figure3.png
- **Figure type**: quantitative_plot
- **Extraction method**: exact_from_labels
- **Reading confidence**: high
- **Plot kind**: forest plot (two panels)
- **Axes**: Panel A — X = AUC Difference vs. p-Tau181 (Baseline), linear, ticks at −0.15..0.15; Y = biomarker (categorical).

## Panel A — AUC Difference vs. p-Tau181 for detecting amyloid-β pathology
| Biomarker (Site_Platform) | MD | 95% CI |
|---------------------------|------|--------------|
| p217_MS | 0.10 | [0.04; 0.16] |
| p231_UGOT | 0.00 | [−0.07; 0.07] |

## Trend summary
Panel A: p217_MS, p217_Ratio, p217_ALZpath, and p217_Lumi have 95% CIs excluding 0 (significant AUC
advantage over p-tau181); p217_IA, p217_Lilly, and p231_UGOT have CIs crossing 0 (not significant).
```

`evidence/figures/figure1.md` (`diagram`, `visual_description`) — the PRISMA flow diagram:
```markdown
# Figure 1 - PRISMA flow diagram of study selection
- **Figure type**: diagram
- **Extraction method**: visual_description
- **Reading confidence**: high

## Visual description
- **Components**: "Records identified from Pubmed, Embase, Cochrane, WOS (n = 179+311+256+195)" →
  "Records removed before screening" → "Records screened (n = 601)" → ... → "Studies included (n=18)".
- **Connections**: standard top-down PRISMA flow with right-pointing arrows to exclusion boxes.
- **What it conveys**: the funnel from initial database records to the final 18 included studies.

## Transcribed numbers (verbatim from the diagram)
| Stage | Value |
|-------|-------|
| Records screened | n = 601 |
| Studies included in review | n = 18 |

**Data-quality caveats**: the database counts (179+311+256+195 = 941) do not reconcile with 601
screened after removing 219 duplicates; values are transcribed exactly as printed, not corrected.
```

### Cardinality / variability
Exactly one pair (`.md` + `.png`) per numbered table and per numbered figure in the source, no more,
no fewer — che26 has 2 tables + 3 figures (all filed); huu25 has 0 numbered main-text tables (all 17
tables are supplementary) + 6 numbered main-text figures (all filed). `quantitative_plot` is the most
common figure type in quantitative papers; `diagram` dominates in method-overview figures (PRISMA
flows, pipeline schematics, network-geometry plots); `qualitative_sample` appears for representative
images/failure cases; `mixed` appears for multi-panel figures combining several of the above (seen in
`ave25-uncovering-plaque-glia-niches-in-human/evidence/figures/figure3.md`, a 9-panel figure with
diagram, Venn-count table, box-plot data, and representative-image panels all in one file, each
sub-scored with its own `Reading confidence`).

### Availability notes
Mandatory core, and this is the artifact where "absence must be accounted for, not skipped" is most
explicit and most checkable:
- **Every numbered object not filed must be named in `README.md` with a reason** — an ARA that quietly
  files only some of the source's tables/figures fails Seal Level 1 outright (§11, Evidence Ledger
  Completeness). This is directly checkable: count `Table N`/`Figure N` mentions in the source vs.
  files present vs. objects named as intentionally-skipped in README.
- **Supplementary-only material genuinely absent from the fetched source** (huu25's Fig S1–S47 / Table
  S1–S17 live in a separate 39MB supplement PDF not part of the fetched HTML) is the correct, honest
  form of absence — `README.md` names this explicitly rather than silently omitting it, and downstream
  layers still summarize supplementary content where it supports a claim (e.g. "Table S13 Oligo.3 DEG
  counts → C01").
- **A `quantitative_plot` with no data table and no low-confidence trend-summary fallback** is a
  structural failure — the spec requires one or the other, never neither.
- **An estimated reading mislabeled `exact_from_labels`** (should be `digitized_estimate` with `≈`
  markers) is a specific, checkable honesty violation the validation checklist calls out.
- **A `diagram`/`qualitative_sample` file containing a fabricated numeric table** is an explicit
  violation (Critical Rule #11) — these types must never masquerade as quantitative.
- Paywalled/abstract-only sources: **`evidence/` is the artifact hit hardest** — typically zero or
  near-zero tables/figures filed (nothing to screenshot), which should read as a near-total loss of
  grounding capacity, not a small gap, since almost every claim's `Sources` entry depends on this
  layer existing.

---

