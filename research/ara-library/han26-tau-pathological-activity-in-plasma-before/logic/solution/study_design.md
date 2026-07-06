# Study Design

## Overview
This is a single-center, cross-sectional-with-longitudinal-substudy, diagnostic-accuracy study comparing a novel plasma functional assay (VeraBIND Tau) against [18F]MK6240 tau-PET (reference standard) and against several existing plasma biomarkers (pTau217, pTau181, pTau231, Aβ42/Aβ40 ratio), in a mixed cognitively-unimpaired (CU) / cognitively-impaired (CI) cohort.

## Cohort
- **Total N**: 145 individuals, age >45.
- **Composition**: 76 patients recruited at the Memory Clinic of the Cliniques Universitaires Saint-Luc (Brussels, Belgium) + 69 volunteers selected from a registry established in another academic study, the latter enriched for APOE ε4 carriers to match patient carriership frequency.
- **Recruitment window**: June 2019 – April 2025.
- **Exclusions**: Neurological conditions with long-term dementia risk (e.g., multiple sclerosis, Huntington's disease), focal brain lesions, psychiatric disorders (major depression, schizophrenia, bipolar disorder), active alcohol/drug abuse, participation in an investigational-product clinical trial.
- **Ethics**: Approved by the UCLouvain Ethical Committee (#UCL-2016-121, 13/05/2019; Eudra-CT 2018-003473-94); conducted per the Declaration of Helsinki; written informed consent obtained from all participants.
- **Clinical classification**: CU (n=79, 54.5%) vs. CI (n=66, 45.5%; mild cognitive impairment n=43, dementia n=23), based on a neuropsychological battery (see below); a domain is impaired if z-score < -1.5 (relative to an independent 32-person stable-CU normative sample followed 8 years); CI = at least one impaired domain.
- **Longitudinal subsample**: 88 participants (58 CU, 30 CI: 46 A-T-, 7 A+T-, 32 A+T+, 3 A-T+) with 2–5 repeated VeraBIND Tau measurements (207 total samples), mean follow-up 1.72±0.94 years (range 0.35–3.85).

## Measurements
- **Blood collection**: 21g venipuncture into K2-EDTA tubes; plasma isolated within 2 hours (centrifuged 2000×g, 10 min, 4°C), aliquoted (500 μL), frozen within 2 hours at −80°C.
- **VeraBIND Tau assay**: Performed at Veravas, Inc. and Access Genetics & OralDNA Labs; see `logic/solution/method.md` and `src/configs/assay_protocol.md`. Cross-sectional analyses used the VeraBIND Tau score closest in time to tau-PET (mean delay 0.4±0.8 years).
- **Plasma pTau217**: Lumipulse G600II analyzer, Lumipulse® G pTau217 Plasma RUO assay (Fujirebio).
- **Plasma pTau181, pTau231, Aβ40/Aβ42**: SIMOA (Quanterix) — pTau-181 Advantage V2.1, pTau-231 Advantage, Neurology Plex 3A kits.
- **Amyloid status**: Lumbar puncture (CSF Aβ42, Lumipulse; n=44) or amyloid-PET ([18F]Flutemetamol or [11C]PiB; n=101), processed via PNEURO v4.1 (PMOD) and the Centiloid pipeline; A+ = Centiloid≥20 or CSF Aβ42≤544 pg/mL.
- **Tau-PET**: [18F]MK6240 (Lantheus Inc., investigational; synthesized at KU Leuven), 30-min dynamic acquisition on a Philips Vereos digital PET-CT 90 min post-injection (185±5 MBq); visual Braak-like staging (0–6) by two trained nuclear physicians (T+ = stage>0); regional SUVr (entorhinal, inferior temporal) via PetSurfer/FreeSurfer registration to 3T MRI and the Desikan-Killiany atlas, cerebellar gray matter reference.
- **Cognition**: MMSE (global); four domain composites — verbal episodic memory (Free and Cued Selective Reminding Test), language (LEXIS, category/letter fluency), executive function (Trail Making A/B, Luria's Graphic Sequences), visuospatial function (Clock Drawing, CERAD praxis) — z-scored against an independent 32-person stable-CU 8-year cohort.

## Statistical Analysis Plan
- **Software**: R (2022.07.2); α=0.05; uncorrected for multiple comparisons unless otherwise stated.
- **Group comparisons**: t-tests (normal continuous) / Mann-Whitney U (non-normal continuous) / χ² (categorical: sex, APOE ε4, amyloid positivity).
- **Diagnostic performance**: Sensitivity/accuracy in concordant PET groups (A-T-, A+T+), overall and by clinical group; Fisher's Exact test for discordant-group (A+T-, A-T+) positivity-rate comparison.
- **Cross-biomarker comparison**: ROC/AUC analysis + DeLong tests across VeraBIND Tau, Aβ42/Aβ40, pTau217, pTau181, pTau231, for both tau-PET and amyloid-PET outcomes.
- **Threshold-based comparison**: Sensitivity/specificity/accuracy/PPV/NPV (with 95% CI) for VeraBIND Tau vs. pTau217 at three literature-derived thresholds (0.142/0.193/0.256 pg/mL), using external prevalence priors (10% CU, 60% CI) for PPV/NPV.
- **Braak-stage stratification**: Regression models (adjusted age/sex/education, Bonferroni-corrected) comparing biomarker levels across Braak-like 0 / 1–3 / 4–6 groups; McNemar tests (sensitivity) and DeLong tests (AUC) for Braak 1–3-vs-0 and 4–6-vs-0 contrasts; linear regression of continuous entorhinal SUVr on each biomarker, restricted to Braak-like 0–3, adjusted for age/sex/education.
- **Correlational analyses**: Age-adjusted Spearman's rank correlations between VeraBIND Tau score and MMSE, episodic memory z-score, entorhinal/inferior-temporal tau-PET SUVr, and plasma pTau217/181/231 — in the entire sample and in the CU-only subset.
- **Longitudinal analyses**: Per-participant linear regression of VeraBIND Tau score on time to derive an annual rate of change; age-adjusted Spearman correlations between this rate of change and cross-sectional disease-severity proxies; descriptive characterization of participants who converted from VeraBIND Tau-negative to -positive over follow-up.

## Reference Standard and Comparators
- **Reference standard**: [18F]MK6240 tau-PET (Braak-like stage>0 = T+).
- **Index test**: VeraBIND Tau (Score≥1.0 = positive).
- **Comparator plasma biomarkers**: pTau217 (at 3 thresholds), pTau181, pTau231, Aβ42/Aβ40 ratio.
