# Problem

## Observations

1. Blood biomarkers of AD (p-tau isoforms, NfL, GFAP) are established predictors of future all-cause and AD dementia **in specialized clinical settings** and are cost-effective/minimally invasive compared to CSF and PET (p.1, Introduction: "Blood biomarkers of Alzheimer's disease (AD) have emerged as reliable indicators of AD pathology and accurate predictors of future clinical AD in specialized clinical settings... Compared to cerebrospinal fluid (CSF) and positron emission tomography (PET), blood biomarkers are cost-effective and minimally invasive").
2. The authors' own prior community-based work (Grande et al., ref. 9) showed p-tau isoforms, NfL, and GFAP can predict future all-cause/AD dementia in a **cognitively unimpaired** community cohort, but concluded biomarkers "are not yet suitable as standalone screening tools for cognitively unimpaired individuals" (p.5, Discussion).
3. A few clinical (non-population-based) studies show MCI patients with elevated AD blood biomarkers are at high risk of progressing to dementia (refs. 13-17), but **population-based** evidence at the MCI stage was lacking (p.1: "data from population-based studies are still lacking").
4. How AD blood biomarkers influence the full set of transitions across the cognitive spectrum — development of MCI from normal cognition, reversion of MCI to normal cognition, and progression from MCI to dementia — "remains poorly understood" (p.1-2).

## Gap

No population-based study had simultaneously modeled baseline AD blood biomarker levels against **all** transitions across normal cognition, MCI, and dementia (bidirectional MCI transitions plus progression), in a community sample followed long enough (up to 16 years) to observe these intermediate-stage transitions with adequate power.

## Key Insight

A four-state parametric multistate Markov model (normal cognition, MCI, dementia, death as absorbing state), fit with age as the time scale, can jointly estimate hazard ratios for every clinically relevant transition (NC→MCI, MCI→NC, MCI→dementia) from a single model, using both continuous (spline) and dichotomized (cut-off-based) representations of six serum AD biomarkers, individually and in combination — turning cross-sectional/prediction-style biomarker evidence into a transition-level picture of where in the cognitive-decline trajectory the biomarkers actually carry information.

## Assumptions

- Direct transition from normal cognition to dementia is disallowed in the model; anyone observed to move directly from NC to dementia is assumed to have passed through an unobserved MCI phase (p.6, Statistical analysis: "The direct transition from normal cognition to dementia was not allowed... assumed to have passed through a MCI phase, although this was not observed due to intermittent observation").
- Baseline transition hazards follow a Gompertz distribution with age as the time scale (p.7).
- Cut-offs for dichotomizing biomarkers were not re-derived in this study; they were imported from a prior bootstrap/Youden-index procedure in the same cohort (Grande et al., ref. 9) and applied here (p.6, Methods: "Blood biomarkers were also dichotomized (high/low) using cut-offs derived in a previous study9").
- MCI/CIND status is defined purely by a fixed neuropsychological test battery threshold (≤1.5 SD below age-specific mean in ≥1 of 5 domains) plus preserved function, not by biomarker or imaging confirmation (p.6).
- Dementia diagnosis relies on clinical assessment (DSM-IV / NINCDS-ADRDA) without routine neuroimaging or CSF confirmation (p.6, Limitations, p.6).
