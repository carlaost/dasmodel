# Evidence Index

Source: Sorrentino et al. (2025), "Barriers for access and utilization of dementia care services in Europe: a systematic review." *BMC Geriatrics* 25:162, doi:10.1186/s12877-025-05805-z. Grounding: full-text (Open Access, CC-BY 4.0), 15-page PDF.

## Tables (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Table 1 | [tables/table1.md](tables/table1.md) | Eligibility (inclusion/exclusion) criteria | C01, C02 | `tables/table1.png` |
| Table 2 | [tables/table2.md](tables/table2.md) | PICO-framework research string per domain | C01 | `tables/table2.png` |
| Table 3 | [tables/table3.md](tables/table3.md) | Full characteristics of all 29 included studies (author/year, nation, design, methods, population, sample, setting, barriers, MMAT quality score) | C03, C04, C05, C06, C07, C08, C09, C10 | `tables/table3_part1.png` (page 5, rows 1-14), `tables/table3_part2.png` (page 6, rows 15-29) |

## Figures (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Figure 1 | [figures/figure1.md](figures/figure1.md) | PRISMA flow diagram: identification (1748+4) → screening (1202, 1129 excluded) → eligibility (73, 44 excluded with 4 reasons) → included (29) | C01, C02 | `figures/figure1.png` |

## Accounted-for omissions

- The paper contains **no supplementary tables or figures** referenced beyond Table 1, Table 2, Table 3, and Figure 1 — no "Table S1", "Fig. S1", or similar appear anywhere in the full text or references.
- No additional appendix material (worked examples, extended data, prompt templates) is present; this is a standard 15-page journal article with References as its final section.

## Screenshot rendering notes

- All screenshots were rendered directly from `paper.pdf` at 3x zoom using PyMuPDF (`fitz`), cropped to the relevant page region (not full pages), to keep each table/figure legible and self-contained.
- Table 3 spans two printed pages (page 5, rows 1-14, ending "Table 3 (continued)"; page 6, rows 15-29); both page-crops are saved and the single `table3.md` transcription merges them into one continuous, correctly-numbered table (not two separate "Table 3" objects), per the evidence-fidelity rule against splitting one source table across differently-named files.

## Note on internal source inconsistencies (see `logic/claims.md` for full detail)

Two numeric inconsistencies were found *within the source paper itself* during transcription and are flagged, not silently resolved:
1. The Abstract states "Over 1298 articles, 29 studies met the inclusion criteria," which does not reconcile with the Results/Fig. 1 pipeline (1748 database-identified + 4 reference-mined = 1752 total identified; 1202 unique after dedup; 73 full-text reviewed) — see C01.
2. The Results text states the cultural/stigma-related barrier category as n=10 but lists only 7 citation numbers ([42, 48, 52, 54, 57, 58, 66]) immediately after it — see C04.
