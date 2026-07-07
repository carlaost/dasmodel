# Table 1: Safety overview and AEs of special interest during the LTE period

- **Source**: Table 1, Zimmer et al. (2025), *J Prev Alzheimers Dis* 13:100446, doi:10.1016/j.tjpad.2025.100446, `paper.pdf` p7
- **Caption**: "Safety overview and AEs of special interest during the LTE period."
- **Screenshot**: table1.png
- **Extraction type**: raw_table

| Event, n (%) | Donanemab → placebo (N=393) [early-start] | Donanemab → donanemab (N=157) [early-start] | Placebo → donanemab (N=657) [delayed-start] |
|---|---|---|---|
| **Overview** | | | |
| Deaths ᵇ | 8 (2.0%) | 2 (1.3%) | 7 (1.1%) ᶜ |
| SAEs | 80 (20.4%) | 21 (13.4%) | 129 (19.6%) |
| Study discontinuations due to AE | 15 (3.8%) | 6 (3.8%) | 39 (5.9%) |
| Treatment discontinuations due to AE | 15 (3.8%) | 6 (3.8%) | 89 (13.5%) |
| TEAEs ᵈ | 315 (80.2%) | 133 (84.7%) | 568 (86.5%) |
| TEAEs deemed related to study treatment ᵉ | 49 (12.5%) | 52 (33.1%) | 315 (47.9%) |
| **AEs of special interest** | | | |
| ARIA-E | 5 (1.3%) | 13 (8.3%) | 171 (26.0%) |
| ARIA-H | 24 (6.1%) | 30 (19.1%) | 161 (24.5%) |
| Headache | 15 (3.8%) | 11 (7.0%) | 65 (9.9%) |
| Infusion-related reaction | 2 (0.5%) | 11 (7.0%) | 49 (7.5%) |
| Superficial siderosis of the CNS | 4 (1.0%) | 6 (3.8%) | 44 (6.7%) |
| Cerebral microhemorrhage | 5 (1.3%) | 5 (3.2%) | 21 (3.2%) |
| Vomiting | 8 (2.0%) | 4 (2.5%) | 21 (3.2%) |
| Nausea | 6 (1.5%) | 5 (3.2%) | 17 (2.6%) |
| **ARIA overview** | | | |
| Any ARIA ᶠ | 59 (15.0%) | 54 (34.4%) | 289 (44.0%) |
| Any SAE of ARIA ᵍ | 0 (0.0%) | 1 (0.6%) | 9 (1.4%) |
| ARIA-E ᶠ | 6 (1.5%) | 13 (8.3%) | 171 (26.0%) |
| Symptomatic ARIA-E | 1 (0.3%) | 3 (1.9%) | 40 (6.1%) |
| SAE of ARIA-E ᵍ | 0 (0.0%) | 1 (0.6%) | 9 (1.4%) |
| ARIA-H ᶠ | 55 (14.0%) | 50 (31.8%) | 261 (39.7%) |
| Symptomatic ARIA-H | 1 (0.3%) | 0 (0.0%) | 3 (0.5%) |
| SAE of ARIA-H ᵍ | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| Macrohemorrhage ᶠ | 0 (0.0%) | 0 (0.0%) | 7 (1.1%) |
| SAE of macrohemorrhage ᵍ | 0 (0.0%) | 0 (0.0%) | 1 (0.2%) |

**Note** (verbatim, printed under the table): "Note: Participants may be counted in more than one
category."

## Footnotes (verbatim)
- ᵃ Includes participants who received at least one infusion during the LTE.
- ᵇ Deaths are also included as SAEs and discontinuations due to AEs.
- ᶜ Includes two previously reported deaths due to ARIA-E and intracranial hemorrhage. Intracranial
  hemorrhage occurred following thrombolytic administration where an MRI scan on the same day
  showed severe ARIA-E [13].
- ᵈ TEAEs are baseline AEs defined as all ongoing AEs at the first LTE dose; the postbaseline
  period started the day of the first LTE infusion and ended at the earlier date of study
  withdrawal or completion, the end of the LTE period + 57 days, or data cutoff.
- ᵉ Includes events that were considered related to study treatment as judged by the investigator.
- ᶠ Based on MRI or TEAE cluster.
- ᵍ Based on TEAE cluster.

## Notes on interpretation
- Columns are treatment-sequence groups within the LTE, not treatment arms per se: two are
  early-start subgroups (participants who switched to placebo upon meeting treatment course
  completion criteria, N=393; participants who continued donanemab, N=157) and one is the entire
  delayed-start group dosed in the LTE (N=657, who initiate donanemab at LTE entry and may later
  switch to placebo).
- Death/SAE/TEAE incidences quoted from this table match the narrative percentages given in §3.4
  (`paper.pdf` p6–7) exactly: donanemab→placebo 2.0%/20.4%/80.2%; placebo→donanemab
  1.1%/19.6%/86.5% (see `logic/claims.md` C11).
- ARIA-E and ARIA-H incidence rise sharply for the placebo→donanemab (delayed-start) column
  (26.0%/24.5%) relative to the donanemab→placebo column (1.5%/14.0%), consistent with this
  group's more recent/ongoing donanemab exposure at the point ARIA risk is highest (`logic/claims.md`
  C12; `logic/solution/constraints.md` L3).
