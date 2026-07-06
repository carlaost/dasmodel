# Related Work

Typed dependency graph over the paper's cited literature (references numbered as in the paper, 1-56). Works with a specific technical delta to this study get a full `RW` block; the remaining cited literature (largely epidemiological/mechanistic context and biomarker-validity background) is listed briefly at the end by role.

## RW01: Grande et al. 2025, *Nat. Med.* 31:2027-2035 (ref. 9) — imports / extends
- **Relationship**: imports (cut-offs) and extends (population, outcome scope)
- **Description**: The authors' own prior SNAC-K study, which showed p-tau isoforms, NfL, and GFAP accurately predict future all-cause and AD dementia in **cognitively unimpaired** community-dwelling older adults, and derived the bootstrap/Youden's-index cut-offs (0.057 Aβ42/40; 1.512 p-tau181; 0.134 p-tau217; 0.832 t-tau; 20.171 NfL; 142.515 GFAP pg/mL) that the present paper imports unchanged (p.6, Methods: "Blood biomarkers were also dichotomized (high/low) using cut-offs derived in a previous study9").
- **Delta**: This paper extends RW01's cognitively-unimpaired-to-dementia prediction scope to the full transition structure — NC→MCI, MCI→NC (reversion), and MCI→dementia — via multistate modeling, and concludes biomarkers are more informative at the MCI stage than for detecting incipient decline in unimpaired individuals (p.5, Discussion: "Our previous study suggested that while AD blood biomarkers could potentially be used to exclude impending dementia, they are not yet suitable as standalone screening tools for cognitively unimpaired individuals").

## RW02: Valletta et al. 2024, *Alzheimers Dement.* (ref. 42) — imports
- **Relationship**: imports (covariate selection)
- **Description**: A companion study by the same group showing AD blood biomarker levels vary by chronic disease and inflammatory status.
- **Delta**: Directly motivates this paper's choice of the "fully adjusted" covariate set (chronic kidney disease, heart disease, cerebrovascular disease, anemia, obesity) beyond the basic sex/education adjustment (p.7, Statistical analysis: "as we previously found that AD blood biomarker levels vary with these comorbidities42").

## RW03: Jackson 2011, *J. Stat. Softw.* 38 (ref. 56) / van den Hout, Chan & Matthews 2019 (ref. 55) — imports (methods)
- **Relationship**: imports
- **Description**: The `msm` R package for multi-state panel-data models (Jackson) and the Gompertz continuous-time multi-state estimation approach (van den Hout et al.).
- **Delta**: These supply the statistical machinery (parametric multistate Markov model, Gompertz baseline hazard) this paper applies to biomarker data; no methodological modification is described beyond the four-state/absorbing-death specification.

## RW04: Cullen et al. 2021 (ref. 1); Palmqvist et al. 2021, *Nat. Med.* (ref. 2) — baseline
- **Relationship**: baseline
- **Description**: Foundational studies showing plasma AD biomarkers (p-tau combinations) improve prediction of cognitive decline/dementia, but in **specialized clinical/memory-clinic cohorts**, not general-population samples.
- **Delta**: This paper's central motivating gap — extending biomarker-dementia associations from clinical to community settings, and specifically to intermediate-stage transitions — is defined directly against this baseline (p.1, Introduction).

## RW05: Community-cohort biomarker-dementia studies — Lu et al. 2024, *JAMA* (ref. 5); de Wolf et al. 2020, *Brain* (ref. 6); Stocker et al. 2023, *Alzheimers Dement.* (ref. 7); Cronjé et al. 2023 (ref. 8) — baseline / corroborates
- **Relationship**: baseline
- **Description**: A "growing body" of population-based studies linking AD blood biomarker changes to incident all-cause dementia.
- **Delta**: This paper's finding that p-tau217, NfL, and GFAP show the strongest associations is explicitly presented as "consistent with previous findings from SNAC-K9 and other community-based cohorts5-8" (p.5) — i.e., corroborating rather than contradicting this baseline, while adding the novel MCI-transition/reversion angle these studies did not examine.

## RW06: Clinical MCI-progression biomarker studies — Cullen et al. 2021, *Nat. Aging* (ref. 13); Pichet Binette et al. 2022 (ref. 14); Groot et al. 2022 (ref. 15); Oeckl et al. 2022 (ref. 16); Lehmann et al. 2024 (ref. 17); Kivisäkk et al. 2023 (ref. 23); Silva-Spínola et al. 2023 (ref. 24) — baseline
- **Relationship**: baseline
- **Description**: Clinical-setting (memory clinic) studies showing AD blood biomarkers stratify risk of MCI-to-dementia progression.
- **Delta**: This paper explicitly positions itself as confirming and extending these clinic-based findings to the general community population (p.5: "Our study confirms these findings and extends them to the community").

## RW07: Jack et al. 2024, *Alzheimers Dement.* (ref. 20); Dubois et al. 2024, *JAMA Neurol.* (ref. 21) — bounds
- **Relationship**: bounds
- **Description**: Revised diagnostic-criteria and clinical-biological-construct recommendations that discourage use of AD biomarkers in **asymptomatic** individuals.
- **Delta**: This paper's null NC→MCI finding (C05) is presented as empirical support consistent with these recommendations' scope-limiting stance (p.5: "This result aligns with current recommendations that discourage the use of AD biomarkers in asymptomatic individuals").

## RW08: Bouteloup et al. 2025, *JAMA Neurol.* (ref. 22) — corroborates
- **Relationship**: corroborates
- **Description**: Prior evidence suggesting AD blood biomarkers may be more informative specifically at the MCI stage.
- **Delta**: Directly aligned with and cited alongside this paper's central finding that biomarker-transition associations concentrate at MCI→dementia rather than NC→MCI (p.5).

## RW09: MCI heterogeneity / spontaneous-reversion literature — Canevelli et al. 2016 (ref. 25); Malek-Ahmadi 2016 (ref. 26); Salemme et al. 2025 (ref. 27) — baseline
- **Relationship**: baseline
- **Description**: Systematic reviews/meta-analyses documenting that a non-negligible fraction of MCI cases spontaneously revert to normal cognition, and that MCI is not necessarily a dementia prodrome.
- **Delta**: This paper's MCI-reversion finding (C06/C07 reversion arm) builds on this literature's premise, adding that specific blood biomarkers (NfL, GFAP, p-tau181) can help distinguish neuropathological MCI (less likely to revert) from transient/non-neuropathological MCI (p.5, Discussion).

## RW10: Blood vs. CSF/PET biomarker-validity literature — Roher et al. 2009 (ref. 28); Zetterberg & Blennow 2021 (ref. 29); Mattsson et al. 2016 (ref. 30) — bounds
- **Relationship**: bounds
- **Description**: Evidence that blood Aβ and t-tau correlate less directly with brain pathology than CSF measures (blood Aβ up to 10-fold lower than CSF, largely of peripheral origin).
- **Delta**: Used to explain (bound the interpretation of) this paper's own weak Aβ42/40 and modest t-tau findings (p.5, Discussion).

## RW11: p-tau217 diagnostic-accuracy literature — Palmqvist et al. 2020, *JAMA* (ref. 31); Ashton et al. 2024, *JAMA Neurol.* (ref. 32); Janelidze et al. 2023, *Brain* (ref. 33); Therriault et al. 2025, *Lancet Neurol.* (ref. 34) — corroborates
- **Relationship**: corroborates
- **Description**: Literature establishing p-tau217 as the most sensitive blood biomarker of AD pathology and a candidate standalone diagnostic marker.
- **Delta**: Cited to explain why p-tau217 in this study was more strongly associated with AD dementia specifically than with all-cause dementia (p.5).

## RW12: Neurofilament-specificity literature — Bridel et al. 2019 (ref. 35); Khalil et al. 2018 (ref. 36); MRC CFAS 2001 (ref. 37); White et al. 2005 (ref. 38); Schneider et al. 2007, 2009 (refs. 39-40) — bounds
- **Relationship**: bounds
- **Description**: Evidence that NfL is a non-specific neurodegeneration marker, and that most late-life community dementia reflects mixed neuropathology.
- **Delta**: Used to interpret why NfL — despite lacking AD specificity — was the single strongest biomarker for all-cause dementia progression in this community sample (p.5).

## RW13: Serum-plasma equivalence literature — Kac et al. 2022 (ref. 44); Koerbel et al. 2024 (ref. 45); Chen et al. 2025 (ref. 46) — bounds
- **Relationship**: bounds
- **Description**: Evidence that serum biomarker levels correlate closely with, and show comparable diagnostic performance to, plasma levels.
- **Delta**: Used to bound (mitigate) the limitation that this study measured biomarkers in serum rather than the more commonly used plasma matrix (p.6, Discussion/Limitations).

## Other cited works (brief, by role)
- **Methods/criteria imports**: Pantzar et al. 2014 (ref. 49, cognitive test battery); Dunne et al. 2020 (ref. 50, MCI/IADL Manchester consensus); Guze 1995 (ref. 51, DSM-IV); McKhann et al. 1984 (ref. 52, NINCDS-ADRDA); Calderón-Larrañaga et al. 2017 (ref. 53, ICD-10 chronic-disease coding); von Elm et al. 2007 (ref. 48, STROBE reporting).
- **Cohort infrastructure**: Lagergren et al. 2004 (ref. 47, SNAC study design).
- **Context/motivation**: Grande et al. 2020 (ref. 10); Vermunt et al. 2019 (ref. 11); Self & Holtzman 2023 (ref. 12, disease-modifying therapy rationale); Brookmeyer & Abdalla 2018 (ref. 18); Villain & Planche 2024 (ref. 19); Khalil et al. 2020 (ref. 43, NfL and aging); Hampel et al. 2018 (ref. 3); Teunissen et al. 2022 (ref. 4); De Strooper & Karran 2016 (ref. 41, GFAP/amyloid mechanism).
