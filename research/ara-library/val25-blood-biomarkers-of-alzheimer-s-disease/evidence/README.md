# Evidence Index

The compiled input (`paper.pdf`) is the 9-page *Nature Communications* main text. It contains exactly **2 numbered tables** and **2 numbered figures**, all in the main text (no numbered tables/figures appear in an appendix within this file — the paper's Supplementary Information, containing Figs. S1-S3 and Tables S1-S14, was **not provided** as part of the compiled input and is therefore not filed here; every reference to it in `logic/` is marked "Not specified in paper / not available from provided input"). This is a complete, ordered sweep of every numbered object in the provided PDF — nothing is skipped.

| Object | Page | Filed as | Notes |
|--------|------|----------|-------|
| Table 1 | p.2 | `tables/table1.md` + `tables/table1.png` | Baseline characteristics, overall + age-stratified (N=2148) |
| Table 2 | p.4 | `tables/table2.md` + `tables/table2.png` | Dichotomized biomarker HRs, basic + fully adjusted, 3 transitions |
| Figure 1 | p.3 | `figures/figure1.md` + `figures/figure1.png` | 18-panel grid: 6 biomarkers (continuous z-score, splines) × 3 transitions, log-scale HR |
| Figure 2 | p.4 | `figures/figure2.md` + `figures/figure2.png` | 3 forest plots: HR by count (0-3) of elevated p-tau217/NfL/GFAP, by transition |

## Objects referenced in text but not filed (not in provided input)
The following are cited by the paper but their source files are part of the Supplementary Information, which was not supplied to this compilation. They are recorded here, not silently omitted, and are treated in `logic/claims.md` / `logic/experiments.md` as directional-only ("Not specified in paper"):
- Supplementary Fig. S1 (AD-dementia-specific continuous-biomarker HR curves, analogous to Fig. 1 but for AD dementia outcome)
- Supplementary Fig. S2 (cohort flow diagram: 3363 → 3123 → 2290 → 2148)
- Supplementary Fig. S3 (multistate Markov model transition diagram)
- Supplementary Tables S1 (AD-dementia dichotomized HRs, analogous to Table 2), S2-S3 (age-stratified), S4-S5 (sex-stratified), S6-S7 (baseline-MCI-excluded), S8-S9 (IPW sensitivity), S10-S11 (biomarker-count combination, all-cause + AD dementia detail), S12-S13 (pairwise p-tau217×NfL combination detail), S14 (assay precision/CV)

No derived subsets were created from Table 1/2 or Figure 1/2 beyond the transcriptions below, which faithfully reproduce the originals in full.
