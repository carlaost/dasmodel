# Constraints, Assumptions, and Limitations

## Boundary conditions
- Scope is limited to **blood-based p-tau biomarkers** (plasma or serum) for AD; only isoforms
  p-tau217, p-tau181, p-tau231 on platforms MS/Simoa/MSD/Lumipulse were compared.
- Only studies with a **biologically confirmed reference standard** (CSF Abeta42/40 or p-tau; amyloid-
  or tau-PET) were included; clinical-diagnosis-only studies were excluded.
- Findings are relative **rankings (P-scores) and AUC mean differences vs. a p181_IA baseline**, not
  absolute pooled sensitivity/specificity/AUC for each marker.
- Search window: January 1, 2020 - March 2026; four databases plus GBSC reports.

## Assumptions
- A1: Extracted AUCs are comparable across studies once mapped to biomarker+platform nodes.
- A2: Selecting the single most comprehensive dataset per cohort yields statistically independent
  nodes (no patient double-counted).
- A3: The random-effects frequentist NMA (netmeta) transitivity/consistency assumptions hold across
  the connected evidence network.
- A4: Where 95% CIs were unreported, values reconstructed from SE or estimated from sample size and
  p-values are valid inputs to the NMA.

## Known limitations (§4.5)
- **Batch effects**: although platforms were adjusted for, batch effects in manual immunoassays may
  still exist.
- **Heterogeneous reference thresholds**: the definition of amyloid positivity varied slightly
  between CSF and PET standards across studies.
- **Limited longitudinal "slope" data**: longitudinal biomarker-slope data remain limited; future
  research should examine how these isoforms change over time during disease-modifying therapies.

## Additional caveats surfaced during compilation (data-quality notes)
These are internal inconsistencies observed in the published figures/tables; transcribed faithfully
in the evidence layer but flagged here so downstream agents do not over-trust the process counts.
- **Table 1 vs. its caption**: Table 1 lists **12 cohort rows**, but its caption says it details "the
  6 core representative cohorts (BioFINDER, ADNI, TRIAD, WRAP, ALFA+, and Han Chinese cohorts)." ADNI
  is named in the caption and abstract as a screened overlapping cohort but has **no row** in Table 1.
  The 12 tabulated cohorts also do not equal the stated 18 studies / 24 datasets.
- **Figure 1 (PRISMA) internal arithmetic**: the caption says "20 + high-impact publications were
  initially screened" whereas the text (§3.1) and the diagram give 601 records screened, 106 full-text
  assessed, and 18 studies included. Database counts (n = 179 + 311 + 256 + 195 = 941) minus duplicates
  (219) do not reconcile to the 601 screened. The "Wrong population (n=47e...)" box contains an apparent
  typo ("47e"). These are transcribed verbatim in `evidence/figures/figure1.md`.
- **Study vs. dataset count**: the paper reports 18 studies / 24 independent datasets throughout, and
  the Figure 1 "Studies included in review (n = 18)" is consistent with the study count (not the
  dataset count).
- **Generative AI use**: the authors disclose ChatGPT was used for translation and language polishing
  during manuscript preparation (Generative AI statement, page 8).
