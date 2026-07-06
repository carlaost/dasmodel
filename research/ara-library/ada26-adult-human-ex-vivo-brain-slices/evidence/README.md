# Evidence Index

## Grounding & completeness note (abstract-only compile)

**No full text was available**, so the paper's numbered **main-text Tables and Figures could NOT be
extracted** — the bioRxiv PDF and JATS full text are behind a Cloudflare challenge (403) and
Unpaywall does not index the `10.64898` DOI prefix (`sources.yaml` → `pdf.downloaded: false`). No
page renders / screenshots of the paper's figures were produced, and **no numbers were transcribed
from figures or main-text tables**. Evidence-ledger completeness for the paper's numbered
figures/tables is therefore **N/A** for this compile (the count and inventory of `Figure N` /
`Table N` in the paper are unknown without the PDF), not a case of silent omission.

What *is* filed comes from the **verified analysis repository** (`naomihabiblab/HumanOrganotypicTNF`
@ `89ed326`), which openly bundles **Supplementary Tables 1–5** (`.xlsx`):

- **Supplementary Table 1** is small and fully transcribed below (with a rendered screenshot).
- **Supplementary Tables 2–5** are large gene/pathway/signaling matrices; they are **described** in
  `src/artifacts.md` (sheet inventory) but **not transcribed** as evidence files here — full numeric
  transcription is out of scope for an abstract-only compile with no full text to cross-check, and
  reproducing thousands of DE/enrichment rows would risk presenting unverified derived values as if
  paper-grounded. They remain available in the cloned repo for downstream drill-in.

No claim in `logic/claims.md` quotes a numeric *result*; the load-bearing values there are
enumerations/thresholds defined in the released **code** (grounded via `[input]` Sources), not
figure readings.

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/supp_table1_samples.md](tables/supp_table1_samples.md) | Supplementary Table 1 (repo `data/`) | C01 | Donor cohort: age, sex, area, tumor type, assay (9 donors) |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| — | — | — | None filed. No full text → the paper's numbered figures could not be rendered/extracted (see note above). |

## Not-filed accounting (numbered objects)

| Object | Status | Reason |
|--------|--------|--------|
| Paper main-text Figures (all) | not filed | No full text (PDF/JATS behind Cloudflare); count unknown |
| Paper main-text Tables (all) | not filed | No full text; count unknown |
| Supplementary Table 2 (WGCNA) | not filed (described in `src/artifacts.md`) | Large multi-sheet matrix; not transcribed in abstract-only compile |
| Supplementary Table 3 (bulk TNF DE + pathways) | not filed (described in `src/artifacts.md`) | Large multi-sheet matrix |
| Supplementary Table 4 (glial snRNA-seq DE + pathways) | not filed (described in `src/artifacts.md`) | Large 6-sheet matrix |
| Supplementary Table 5 (MultiNicheNet signaling) | not filed (described in `src/artifacts.md`) | Large signaling/ligand-receptor matrix |
