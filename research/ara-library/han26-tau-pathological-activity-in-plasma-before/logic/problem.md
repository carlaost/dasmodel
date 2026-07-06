# Problem Specification

## Observations

### O1: Amyloid+/Tau+ status carries a much higher near-term risk of cognitive decline than amyloid-only status
- **Statement**: Clinically unimpaired (CU) individuals with both elevated amyloid and tau-PET signal (A+T+) face a 53–57% risk of cognitive impairment within 3–5 years, compared to 8–17% for amyloid-only (A+T-) individuals and 3–6% for A-T- individuals.
- **Evidence**: Introduction, PDF p.5, citing Ossenkoppele et al. 2022 (ref 5) and Moscoso et al. 2025 (ref 6): "Clinically unimpaired (CU) individuals with both elevated Aβ and tau-PET signals (A+T+) face a high risk of cognitive impairment within 3-5 years (risk=53-57%) compared to those with only high Aβ burden (A+T-, risk=8-17%) and negative individuals (A-T-, risk=3-6%)."
- **Implication**: Detecting tau aggregation specifically (not just amyloid) is the key actionable signal for identifying CU individuals at near-term risk.

### O2: A+T+ individuals are a small, screenable minority of the CU population
- **Statement**: The prevalence of A+T+ status is estimated at ~10% of CU individuals at age 75.
- **Evidence**: Introduction, PDF p.5, citing Moscoso et al. 2025 (ref 6): "Identifying A+T+ individuals in the general population is key for prevention, but challenging as their prevalence is estimated at ~10% of CU individuals at age 75."
- **Implication**: A screening tool for population-level use must have high specificity/PPV, since a low base rate means even a modestly imperfect test generates many false positives.

### O3: Plasma pTau217 — the leading blood biomarker — loses accuracy for tau-PET positivity specifically in CU individuals
- **Statement**: Recent meta-analyses show excellent pTau217 accuracy for predicting amyloid- and tau-PET positivity in cognitively impaired (CI) individuals, but the accuracy of pTau217 for detecting tau-PET positivity is low in CU individuals; low pTau217 thresholds detect both A+T+ and A+T- CU individuals, while high thresholds only capture individuals with already-advanced tau pathology (Braak-like tau-PET stages ≥4).
- **Evidence**: Introduction, PDF p.6, citing Therriault et al. 2025 (ref 24) and Khalafi et al. 2025 (ref 25): "the accuracy of pTau217 for detecting tau-PET positivity is low in CU individuals24,25. Specifically, using high thresholds, plasma pTau217 identifies A+T+ individuals with advanced tau pathology (e.g., Braak-like tau-PET stages≥4)26–29, while using low thresholds detects both A+T+ and A+T- CU individuals."
- **Implication**: pTau217 is diagnostically useful in symptomatic patients (FDA-approved for this use) but is not a reliable stand-alone screening test in asymptomatic/CU individuals for early tau aggregation.

### O4: Tau hyperphosphorylation at a single site is not a specific marker of pathological aggregation
- **Statement**: Tau contains many sites that are reversibly hyperphosphorylated under normal stress conditions (e.g., hypothermia); elevated phosphorylation at any one site therefore does not necessarily indicate tau aggregation.
- **Evidence**: Introduction, PDF p.6, citing Wegmann et al. 2021 (ref 30): "Tau contains many sites at which it is hyperphosphorylated reversibly under various stress conditions such as hypothermia. Consequently, increased levels of tau hyperphosphorylation at any one site does not necessarily result in tau aggregation."
- **Implication**: Site-specific phospho-tau immunoassays (pTau181/205/212/217/231) are measuring a necessary but not sufficient correlate of aggregation; a functional readout of aggregation-competence could be more specific.

### O5: Prion-like tau seeding is a key mechanism of AD tau pathology
- **Statement**: A key mechanism in AD and other tauopathies is tau seeding activity, whereby specific misfolded pTau species bind to and template normal tau, promoting prion-like aggregation and spreading of tau pathology.
- **Evidence**: Introduction, PDF p.6, citing Hu et al. 2016, Alonso et al. 1994/1996 (refs 31–33): "One key pathological mechanism in AD and other tauopathies involves tau seeding activity whereby specific misfolded pTau species binds to and templates normal tau, promoting prion-like aggregation and spreading of tau pathology."
- **Implication**: A plasma assay that directly measures whether purified plasma pTau retains this seeding/binding capacity — rather than just its phosphorylation level — could more specifically capture pathological (rather than merely elevated) tau.

### O6: Tau-PET is the only validated in vivo method but cannot be used for population screening
- **Statement**: Tau-PET imaging is the only validated method for detecting tau aggregates in vivo, but its high cost, invasiveness, and limited accessibility restrict its use in clinical settings and preclude large-scale screening.
- **Evidence**: Introduction, PDF p.5: "Currently, tau positron emission tomography (PET) is the only validated method for detecting tau aggregates in vivo. However, its high cost, invasiveness, and limited accessibility restrict its use in clinical settings and preclude large-scale screening."
- **Implication**: A scalable blood-based surrogate for tau-PET positivity is necessary for prevention-oriented screening at population scale.

## Gaps

### G1: No scalable blood test specifically flags AD-type tau aggregation in CU individuals
- **Statement**: There is no reliable, scalable blood-based biomarker that can confirm tau aggregation (rather than merely elevated phospho-tau or amyloid) with adequate specificity/PPV in cognitively unimpaired individuals.
- **Caused by**: O3, O4 (site-specific pTau species are non-specific for aggregation and perform poorly in CU individuals).
- **Existing attempts**: Plasma pTau181, pTau205, pTau212, pTau217, pTau231 immunoassays (refs 10–17); emerging Core 2 biomarkers such as CSF/plasma pTau205 and MTBR-tau243 (refs 58–60); N-terminal tau fragment assays (ref 61).
- **Why they fail**: These assays quantify the concentration of tau phosphorylated at a given residue. They more closely track amyloid-β plaque load than tau tangle pathology, and their heterogeneous/overlapping phosphorylation patterns mean elevated levels do not reliably indicate the prion-like, aggregation-competent (pathologically active) form of tau — especially at the early, low-Braak stages relevant to CU screening.

### G2: Tau-PET cannot be deployed for population-level screening
- **Statement**: The only validated in vivo detection method for tau pathology (tau-PET) is too costly, invasive, and inaccessible for large-scale screening use.
- **Caused by**: O6.
- **Existing attempts**: None — PET remains a confirmatory/research tool.
- **Why they fail**: Radiotracer PET imaging requires specialized equipment, radiochemistry, and clinical infrastructure not compatible with population screening economics.

## Key Insight
- **Insight**: A functional plasma assay that isolates pTau from plasma and directly tests its ability to bind and template recombinant normal tau — i.e., measures pathological seeding *activity* rather than phosphorylation *concentration* at one site — should track the biological process that actually drives aggregation and spreading, and should therefore better discriminate true AD-type tau pathology from incidental phosphorylation, including at the earliest (low Braak-like stage) points where site-specific pTau assays are weakest.
- **Derived from**: O4, O5.
- **Enables**: Development and evaluation of the VeraBIND™ Tau assay — a plasma-based functional seeding assay (see `logic/solution/method.md`) — benchmarked head-to-head against [18F]MK6240 tau-PET (the in vivo reference standard) and against plasma pTau217/181/231 and the Aβ42/Aβ40 ratio, across the full range of clinical (CU/CI) and Braak-like tau-PET stage strata.

## Assumptions
- A1: Visual Braak-like staging of [18F]MK6240 tau-PET (stage 0–6, T+ defined as stage>0) is treated as the valid in vivo ground truth for tau aggregation pathology (Methods, PDF p.13–14).
- A2: Amyloid positivity (A+) determined via amyloid-PET (Centiloid≥20) or CSF Aβ42 (≤544 pg/mL) are treated as interchangeable classifications of amyloid status within the same cohort (Methods, PDF p.12–13).
- A3: External population-level prevalence estimates of tau-PET positivity (10% in CU, 60% in CI, from Moscoso et al. 2025) are valid priors for computing this cohort's PPV/NPV, despite this study's own enriched (non-representative) sampling (Statistical analysis, PDF p.16; Table 3 footnote, PDF p.42).
- A4: A single VeraBIND Tau test result Score, dichotomized at a Standard-derived cutoff (Score ≥1.0 = positive), adequately captures whether pathologically active pTau is present in a plasma sample (Methods, PDF p.11).
- A5: The CU sample, enriched for APOE ε4 carriers to match patient carriership frequency, does not materially bias the assay's measured diagnostic accuracy relative to a general-population CU sample (Discussion, PDF p.26, acknowledged as a limitation).
