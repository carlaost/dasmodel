# Constraints

Boundary conditions, assumptions, and limitations, drawn from the paper's own Discussion "limitations" paragraph (p.6) and Methods.

## Diagnostic ascertainment
- Dementia diagnosis was based **solely on clinical assessment** (DSM-IV / NINCDS-ADRDA), without routine neuroimaging or CSF biomarker confirmation, introducing a risk of AD-dementia misclassification. This is inherent to community-based settings where biological confirmation is rarely available and mixed etiologies are common. Mitigation: a standardized three-step procedure (two trained physicians + adjudicating neurologist) plus review of clinical charts and death registers for deceased participants (p.6).

## Biomarker matrix
- Biomarkers were measured in **serum**, where concentrations are lower than in plasma (the more commonly used matrix in this field). Mitigation cited: serum levels correlate closely with plasma levels and show comparable diagnostic performance (refs. 44, 46) (p.6).

## Cut-off generalizability
- Dichotomization cut-offs were derived within the SNAC-K cohort itself (via a prior bootstrap/Youden's-index procedure) and "may not fully extend to more diverse populations or alternative laboratory platforms." Independent validation in other cohorts/platforms is flagged as needed (p.6).

## Missing baseline biomarker data → selection bias
- A substantial number of participants lacked AD blood biomarkers at baseline (n=833 excluded from n=3123 dementia-free candidates) and were "generally older, had lower educational levels, and had a higher prevalence of comorbidities" than included participants. Because these excluded individuals were at higher dementia risk, their exclusion "may have led to an underestimation of the results" (p.6).

## Attrition
- 142 (6.2%) of the n=2290 baseline sample with biomarker data dropped out after baseline with no follow-up (leaving the analytic n=2148). Dropouts were younger (mean age difference −7.52 years, 95% CI −9.27 to −5.76), more educated (university level 47.2% vs. 35.4%, p 0.044 as printed in the source), and had fewer chronic diseases (mean difference −1.00 diseases, 95% CI −1.39 to −0.60) than those retained (p.6). Addressed via an IPW sensitivity analysis (C12), reported consistent with main results.

## Single baseline biomarker measurement
- Biomarkers were measured only at baseline; the study "did not allow us to assess the associations between changes in biomarker levels and progression across stages of cognitive decline" — i.e., no repeated-measures/trajectory analysis of biomarker change over time (p.6).

## Modeling assumptions
- Direct transition from normal cognition to dementia is structurally disallowed in the multistate model; any apparent direct transition is assumed to reflect an unobserved intervening MCI phase (p.7).
- Baseline transition hazards are assumed Gompertz-distributed with age (not calendar time) as the time scale (p.7).
- For participants alive and dementia-free but of unknown MCI status at a given assessment, the model treats their state as uncertain but bounded to {NC, MCI} (p.7).
- When dementia was diagnosed at death, onset was assumed to have occurred between the last assessment and death (p.7).

## Scope of generalization
- Findings represent **robust group-level associations**, not validated individual-level prediction: the paper explicitly frames its conclusion as showing biomarkers "may help stratify the risk of progression to dementia at the MCI stage," and calls for larger MCI-focused cohorts to determine whether biomarkers — alone or combined with clinical data — can support individual-level dementia-prediction tools (p.6, Conclusion).
