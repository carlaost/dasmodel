# Evidence Index

Source: Zimmer et al. (2025), "Donanemab in early symptomatic Alzheimer's disease: results from
the TRAILBLAZER-ALZ 2 long-term extension." *The Journal of Prevention of Alzheimer's Disease*
13:100446, doi:10.1016/j.tjpad.2025.100446. Grounding: full-text (Open Access, CC BY 4.0),
9-page PDF (`paper.pdf`), cross-checked against the EuropePMC/PMC full text (PMC12869028).

## Tables (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Table 1 | [tables/table1.md](tables/table1.md) | Safety overview and AEs of special interest during the LTE period, by treatment-sequence group (donanemab→placebo N=393; donanemab→donanemab N=157; placebo→donanemab N=657) | C11 | `tables/table1.png` |

## Figures (all filed, in order)

| Object | File | Content | Claims | Screenshot |
|---|---|---|---|---|
| Figure 1 | [figures/figure1.md](figures/figure1.md) | (a) TRAILBLAZER-ALZ 2 study design (76-week placebo-controlled period + 78-week LTE, randomization N=1736, treatment-course-completion switch points); (b) percentage of donanemab vs placebo infusions over time for early-start and delayed-start participants | O2, O4, C11 | `figures/figure1.png` |
| Figure 2 | [figures/figure2.md](figures/figure2.md) | CDR-SB LS mean change from baseline vs weighted ADNI cohort: (a) early-start group, (b) delayed-start group, (c) early-start subset meeting treatment course completion criteria by 52 weeks | C01, C02, C03, C06 | `figures/figure2.png` |
| Figure 3 | [figures/figure3.md](figures/figure3.md) | CDR-Global hazard progression, early- vs delayed-start (Cox proportional hazards model; HR=0.73 [0.62-0.86], p<0.001) | C04 | `figures/figure3.png` |
| Figure 4 | [figures/figure4.md](figures/figure4.md) | Brain amyloid plaque: (a) mean CL reduction over time, early- vs delayed-start; (b) amyloid clearance (<24.1 CL) rates at weeks 24/52/76 post-initiation; (c) amyloid reaccumulation among 52-week completers | C07, C08, C10 | `figures/figure4.png` |

## Accounted-for omissions

The provided `paper.pdf` is the 9-page main-text article only; it references, but does not
include, the following supplementary objects (confirmed absent by full-text search of
`fulltext.xml` and by page-by-page reading of `paper.pdf` — no supplementary appendix pages are
present in the file):

- **Table S1** — demographics/disease characteristics at LTE start for early-start
  placebo-switchers (N=393), early-start donanemab-continuers (N=157), and delayed-start (N=657)
  participants. Referenced in §3.1 (`paper.pdf` p4). Not included in the provided PDF.
- **Table S2** — baseline disease characteristics for the subset of early-start participants who
  met treatment course completion criteria by 52 weeks. Referenced in §3.1 (`paper.pdf` p4). Not
  included in the provided PDF.
- **Table S3** — demographics/disease characteristics of early-start participants who did not
  achieve amyloid clearance (<24.1 CL) by the end of the LTE (N=33). Referenced in §3.3
  (`paper.pdf` p6). Not included in the provided PDF.
- **Table S4** — overview of numbers/percentages of early- and delayed-start participants who
  achieved amyloid clearance or met treatment course completion criteria. Referenced in §3.3
  (`paper.pdf` p6). Not included in the provided PDF.
- **Table S5** — ARIA frequencies (any ARIA, ARIA-E, ARIA-H) for early-start 52-week completers
  after switching to placebo, with no ARIA-related SAEs. Referenced in §3.4 (`paper.pdf` p7). Not
  included in the provided PDF; the underlying narrative numbers (20.3%/2.0%/18.3%) are captured
  in `logic/claims.md` C12 from the main text.
- **Fig. S1** — unweighted sensitivity analysis of ADNI participants with amyloid pathology
  (≥37 CL) and global tau PET positivity. Referenced in §2.5.1 (`paper.pdf` p3). Not included.
- **Fig. S2** — full study disposition of participants receiving ≥1 LTE infusion. Referenced in
  §3.1 (`paper.pdf` p4). Not included.
- **Fig. S3a/S3b** — ADNI propensity-weighting diagrams for the early-start (ESS=268) and
  delayed-start (ESS=301) comparisons. Referenced in §3.1 (`paper.pdf` p4). Not included.
- **Fig. S4** — covariate balance of propensity weights for early- and delayed-start groups.
  Referenced in §3.1 (`paper.pdf` p4). Not included.
- **Fig. S5** — validation plot of the weighted ADNI cohort's trajectory vs the TRAILBLAZER-ALZ 2
  internal placebo arm through 76 weeks. Referenced in §3.1 (`paper.pdf` p4). Not included.
- **Fig. S6** — AUC (cumulative CDR-SB benefit) analysis underlying the 0.97-point/78-week,
  p<0.001 result reported narratively in §3.2 (`paper.pdf` p6, C05). Not included.
- **Fig. S7** — time-to-first-ARIA-E-event analysis among all donanemab-exposed participants.
  Referenced in §3.4 (`paper.pdf` p7, C12). Not included.
- **Fig. S8** — 6-month-interval post-discontinuation ARIA-E/ARIA-H incidence. Referenced in §3.4
  (`paper.pdf` p7, C12). Not included.

No other numbered table or figure appears in the main text beyond Table 1 and Figures 1–4 (verified
by `grep`-ing `fulltext.xml` for all `Table [0-9S]*` and `Fig\. [0-9S]*` occurrences).

## Screenshot rendering notes

- All screenshots were rendered directly from `paper.pdf` using PyMuPDF (`fitz`), cropped to the
  relevant page region (figure/table plus its caption), by the prior compilation pass. Table 1's
  crop captures the complete data table (all rows through "SAE of macrohemorrhage"); the table's
  footnote/legend row (definitions of superscripts a–g) is captured in `tables/table1.md`'s
  transcription but not separately re-screenshotted.
- Figures 1, 2, and 4 are multi-panel (1a/1b; 2a/2b/2c; 4a/4b/4c); each multi-panel figure is kept
  as a single screenshot/markdown pair per its original `Fig. N` numbering, consistent with the
  rule against splitting one source figure across differently-named files.
