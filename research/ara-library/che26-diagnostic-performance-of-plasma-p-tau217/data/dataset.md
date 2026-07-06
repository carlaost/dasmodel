# Datasets

This NMA reuses **summary diagnostic-accuracy statistics** (AUC ± 95% CI, sensitivity, specificity)
extracted from 18 publications yielding 24 independent datasets (4,736 participants total). No primary
patient-level data were released. The underlying cohorts and their access status are below. Full
demographic characteristics are transcribed in `evidence/tables/table1.md`.

## Provenance and access
- **Type**: secondary summary data extracted from published diagnostic-accuracy studies.
- **Release status**: no accessioned dataset; "included in the article/Supplementary material, further
  inquiries can be directed to the corresponding author" (Data Availability statement, verbatim).
- **Registration**: PROSPERO CRD420261327845 (open).
- **De-overlap rule**: only the single most comprehensive dataset per cohort was selected to preserve
  statistical independence (§2.3).

## Included cohorts (from Table 1; access controlled/by-request via each consortium)
| Cohort | Source study | N | Disease stage | Reference standard | Platform/manufacturer |
|--------|--------------|---|---------------|--------------------|-----------------------|
| BioFINDER-1 | Janelidze et al. (2023) | 135 | MCI (prodromal AD) | CSF Abeta42/40 | IP-MS and Simoa |
| BioFINDER-PC | Palmqvist et al. (2024) | 307 | Primary care (SCD/MCI) | CSF Abeta42/40 | IP-MS (C2N) |
| WRAP | Ashton et al. (2024a) | 323 | Preclinical AD (CU) | Amyloid-PET | Simoa (ALZpath) |
| SPIN | Ashton et al. (2024b) | 195 | AD continuum | CSF Abeta42/40 | Simoa (ALZpath) |
| Clarity AD | Devanarayan et al. (2025) | 98 | MCI and mild AD | Tau-PET | IP-MS (C2N) |
| ALZAN | Lehmann et al. (2025) | 423 | Cognitive complaints | CSF Abeta42/40 | Simoa (Fujirebio) |
| ALFA+ | Mila-Aloma et al. (2022) | 397 | Preclinical AD (CU) | CSF Abeta42/40 | Simoa and MSD |
| TRIAD | Benedet et al. (2026) | 100 | AD continuum | Amyloid-PET | Automated IA (serum focus) |
| MCSA | Mielke et al. (2022) | 1,051 | Community (CU/MCI/Dem) | Amyloid/Tau-PET | MSD (Lilly) |
| Coimbra | Silva-Spinola et al. (2026) | 395 | Tertiary clinic | CSF Abeta42/40 | Automated IA |
| Huashan | Han Chinese cohort (*) | 297 | Clinic (MCI/Dementia) | Amyloid-PET | AutoIA (Lilly) |
| Greater-Bay (GBA) | Han Chinese cohort (*) | 425 | Community-based (CU) | Amyloid-PET | AutoIA (ALZpath) |

(*) Marked with an asterisk in Table 1; no separate primary-study citation is given in the paper.

## Additionally named (screened) cohorts
- **BioFINDER-2, ADNI, TRIAD** — named in the abstract/§2.3 as large overlapping cohorts that were
  rigorously screened; ADNI is named in the Table 1 caption but has **no row** in Table 1 (see
  `logic/solution/constraints.md` for this discrepancy).

## Consent / ethics
- Not applicable at the review level (secondary summary data). Individual cohorts carry their own IRB
  approvals and consent (not restated in this article). Risk of bias assessed via QUADAS-2
  (Supplementary Table S1).

## Notes
- The 12 cohorts tabulated in Table 1 do not sum to the stated 18 studies / 24 independent datasets;
  Table 1 presents the "6 core representative cohorts" per its caption (see constraints.md).
