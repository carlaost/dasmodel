# ARA compiler artifact data shape (clean-room reference)

This is the complete data shape for ONE artifact the ARA compiler emits. Design your metrics against exactly this structure.

---

## 3. `logic/concepts.md` (technical terms)

### Artifact + path
`logic/concepts.md`, e.g. `research/ara-library/che26-diagnostic-performance-of-plasma-p-tau217/logic/concepts.md`.

### Purpose
Formal, self-contained definitions of the paper's genuine technical vocabulary — the terms a reader
must understand to parse the claims and methods. Not a glossary of borrowed/generic terms; each entry
should be something specific to this paper's contribution or field.

### Structure
One `## {Term Name}` section per concept (a plain markdown heading, not an ID scheme). Each has:

| Field | Type | Real example |
|---|---|---|
| `**Notation**` | string — LaTeX/symbolic notation, or `"—"` if none | `p217 (nodes: p217_MS, p217_Ratio, p217_ALZpath, p217_Lumi, p217_IA, p217_Lilly, p217_Serum, p217_AutoIA)` |
| `**Definition**` | markdown-prose, formal | `"Tau phosphorylated at threonine 217. In this NMA it is the top-performing isoform for detecting amyloid-beta pathology..."` |
| `**Boundary conditions**` | markdown-prose — when it applies/doesn't, or `"Not specified in paper"` | `"Performance is highest when measured by mass spectrometry or as an automated p-tau217/Abeta42 ratio."` |
| `**Related concepts**` | comma-separated list of other concept names (loose text, not IDs) | `p-tau, mass spectrometry, p-tau217/Abeta42 ratio, automated immunoassay` |

### A full realistic example

```markdown
## Network meta-analysis (NMA)
- **Notation**: NMA
- **Definition**: A meta-analytic method comparing multiple interventions/tests simultaneously by
  combining direct (head-to-head) and indirect evidence within a connected network of comparisons,
  referenced to a common comparator. Here a random-effects frequentist NMA (netmeta) compares
  biomarker+platform nodes.
- **Boundary conditions**: Requires a connected network; assumes transitivity/consistency across the
  evidence base; between-study heterogeneity captured by I2.
- **Related concepts**: network geometry, P-score, mean difference, direct/indirect evidence

## P-score (SUCRA analog)
- **Notation**: P-score in [0, 1]
- **Definition**: A frequentist ranking metric (analogous to SUCRA in Bayesian NMA) giving the
  probability that a treatment/test is better than a competing one, averaged over all competitors.
  Higher values indicate a higher probability of being the best diagnostic marker.
- **Boundary conditions**: Ranks relative performance within a specific outcome/network; not an
  absolute accuracy value.
- **Related concepts**: SUCRA, NMA, ranking, network geometry
```

### Cardinality / variability
Target is ≥5 sections (Seal Level 1 checks this as a soft count target, never a padding license); the
two ARAs read here have 13 (che26, meta-analysis with heavy method vocabulary) and 10 (huu25, wet-lab
genomics — cell-type/assay vocabulary). A theory paper's concepts skew toward formal
objects/operators with dense `Notation`; a clinical-trial ARA's concepts skew toward endpoint
definitions and instrument names with `Notation: —`.

### Availability notes
Never fully absent (mandatory core). Thinness signals to watch:
- Fewer than 5 genuine sections **is correct, not a defect**, if the paper truly introduces fewer
  distinct terms (Rule 14/15 — source-bounded, not a quota) — a metric must not penalize an honestly
  short concepts.md the same way it penalizes a padded one with borrowed/trivial terms.
- `Boundary conditions: Not specified in paper` appearing on most/all entries signals a shallow read
  of the source (the compiler didn't work hard to locate applicability limits) rather than a genuine
  absence — this is a legitimate quality signal for a tournament metric to catch, distinct from an
  honest "the paper doesn't state this."
- Abstract-only sources: concepts.md will contain only what can be defined from the title/abstract
  vocabulary — visibly fewer, shallower `Definition` fields.

---

