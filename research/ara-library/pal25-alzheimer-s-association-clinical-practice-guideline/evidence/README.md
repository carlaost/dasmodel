# Evidence Index

Source: Palmqvist et al. (2025), "Alzheimer's Association Clinical Practice Guideline on the use of blood-based biomarkers in the diagnostic workup of suspected Alzheimer's disease within specialized care settings." *Alzheimer's & Dementia*, doi:10.1002/alz.70535. Grounding: full-text (OA via PMC12306682).

## Tables (all filed, in order)

| Object | File | Content | Screenshot |
|---|---|---|---|
| Table 1 | `tables/table1.md` | GRADE certainty-of-evidence definitions; strong vs. conditional recommendation implications | `tables/table1.png` |
| Table 2 | `tables/table2.md` | Triaging + confirmatory BBM recommendations, acceptable-accuracy thresholds, good practice statement, remarks | `tables/table2.png` |
| Table 3 | `tables/table3.md` | Assay/analyte combinations studied (analyte × method × brand) | `tables/table3.png` |

## Figures

The guideline contains **no numbered figures** in the main text (it is a recommendations document; the diagnostic pathway is conveyed via the recommendation tables). No `figures/` objects to file.

## Accounted-for omissions

- **Table S1** (completed Evidence-to-Decision / EtD form) is online supplementary material, not in the main article PDF — referenced in `logic/` but not filed as a separate evidence object.
- The living systematic review of test-accuracy estimates is hosted on the MAGICapp platform (https://app.magicapp.org/#/guideline/nyO1Yj); pooled per-assay sensitivity/specificity values live there rather than in the article, and are cited as an external artifact in `src/environment.md`.

## Note on completion

`table1.md`, `table2.md`, `table3.md`, this README, and `trace/exploration_tree.yaml` were written in the main session after the compile subagent terminated early on a transient/spurious output content-filter error (the table contents — GRADE definitions, clinical recommendations, and an assay catalog — are routine biomedical text). The table PNGs were rendered by the original subagent; transcriptions here were verified against those PNGs.
