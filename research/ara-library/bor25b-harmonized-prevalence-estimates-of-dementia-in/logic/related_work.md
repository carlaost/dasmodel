# Related Work

Typed dependency graph over the paper's citation footprint (36 in-text references). Works with a specific technical delta relative to this paper get full `RW` blocks; the remainder are captured more briefly to preserve the paper's full citation footprint.

## RW01: Klee, Langa & Leist (2024) — "Performance of probable dementia classification in a European multi-country survey"
- **DOI**: (Sci. Rep. 14, 6657, 2024 — DOI not stated in paper.pdf reference list)
- **Type**: baseline / extends
- **Delta**:
  - What changed: Klee et al. used the earlier (2017) SHARE wave with ML-based algorithmic classification approaches and a Langa-Weir scale variant lacking backwards counting (unavailable in 2017 SHARE data); critically, they scaled their prevalence estimates to national OECD estimates rather than validating against an independent clinical assessment. This paper instead uses the 2022 SHARE Wave 9 and validates directly against the SHARE-HCAP neuropsychological assessment, replacing OECD-rescaling with a genuine harmonized validation base.
  - Why: OECD-rescaled estimates inherit the cross-study harmonization shortcomings (O2 in `logic/problem.md`) this paper aims to overcome.
- **Claims affected**: C01–C05, C11 (all main-result prevalence claims, since this is the paper's direct predecessor on the same SHARE parent study).
- **Adopted elements**: The general "ML/regression-based classification of SHARE respondents" strategy; the Langa-Weir scale as a comparison benchmark (though with a different variant, per the backwards-counting availability difference).

## RW02: Manly et al. (2022) — "Estimating the prevalence of dementia and mild cognitive impairment in the US" (JAMA Neurology)
- **DOI**: Not stated in paper.pdf reference list (ref. 24)
- **Type**: imports
- **Delta**:
  - What changed: this paper directly imports Manly et al.'s classification algorithm (factor-score estimates across five cognition domains, 1.5-SD-below-normative-mean threshold in ≥2 domains plus informant-reported functional impairment) and NIA-AA diagnostic criteria basis, applying it unchanged to the SHARE-HCAP data. The stated reason for choosing this specific algorithm is "to allow cross-HCAP study comparisons" with other HCAP-network studies (e.g., US HRS, LASI-DAD India, rural South Africa).
  - Why: provides an already-validated classification rule rather than requiring this paper to develop a new one from scratch.
- **Claims affected**: C06, C12, C13 (the classification step that grounds the entire prevalence-estimation pipeline).
- **Adopted elements**: The full classification decision rule (see `logic/concepts.md` — "Manly et al. (2022) classification algorithm"); the resulting US dementia prevalence (~11%) used as an informal benchmark ("roughly comparable to the results by Manly et al. for the US," C03).

## RW03: Hurd, Martorell, Delavande, Mullen & Langa (2013) — "Monetary costs of dementia in the United States" (NEJM)
- **DOI**: Not stated in paper.pdf reference list (ref. 29)
- **Type**: imports (methodological)
- **Delta**:
  - What changed: Hurd et al.'s regression-based approach was originally developed to estimate monetary costs of dementia in a single-country (US) setting. This paper adapts it "to our multi-country setting" to relate SHARE-HCAP classification to shared cognition/health/demographic variables and predict cognitive status for the full SHARE parent sample.
  - Why: provides a validated regression framework for extending a validated classification (available only in a subsample) to a much larger sample sharing only a subset of measures.
- **Claims affected**: C06 (validation of the regression-based prediction against direct classification, Table 2).
- **Adopted elements**: The regression-based prediction methodology; adapted (not directly reused) for a multi-country context.

## RW04: Crimmins, Kim, Langa & Weir (2011) — Langa-Weir (LW) cognitive assessment scale
- **DOI**: Not stated in paper.pdf reference list (ref. 14)
- **Type**: baseline
- **Delta**:
  - What changed: this paper reports LW-scale-based prevalence estimates (Table 3) alongside its own HCAP-validated estimates as an explicit comparison, showing the LW scale yields lower average prevalence but larger relative cross-national variation (coefficient of variation 0.80 vs. 0.46; C05).
  - Why: LW is an established scale validated against the US ADAMS study (RW12), providing a widely-used point of comparison, though the paper argues its narrower measure set (word recall, serial 7s, backwards counting only) under-detects milder/earlier impairment relative to the broader HCAP battery.
- **Claims affected**: C05.
- **Adopted elements**: The LW cutoff definitions (demented 0–6; normal 12–27; CIND 7–11) applied to SHARE Wave 9 data, though the specific LW variant here differs from the LW variant used in Kiejna et al. (RW11)-related earlier SHARE work (RW01) due to backwards-counting availability.

## RW05: Langa et al. (2020) — "The health and retirement study harmonized cognitive assessment protocol project: study design and methods" (Neuroepidemiology)
- **DOI**: Not stated in paper.pdf reference list (ref. 18)
- **Type**: imports
- **Delta**: Describes the HCAP protocol design that SHARE-HCAP directly implements as "the European arm of the HCAP network of aging studies." No independent modification beyond adapting the protocol to the SHARE five-country validation subsample.
- **Claims affected**: C12, C13.
- **Adopted elements**: The HCAP battery design and cross-national harmonization rationale.

## RW06: Börsch-Supan et al. (2013) — "Data resource profile: the survey of health, ageing and retirement in Europe (SHARE)" (Int. J. Epidemiol.)
- **DOI**: Not stated in paper.pdf reference list (ref. 12)
- **Type**: imports
- **Delta**: Describes the SHARE parent study infrastructure (28-unit sample, ex-ante harmonized instruments) this paper's Wave 9 data collection builds on. No modification; foundational infrastructure reference.
- **Claims affected**: C01–C13 (all claims rely on SHARE as the underlying survey infrastructure).
- **Adopted elements**: SHARE's cross-national sampling design and harmonized-instrument approach.

## RW07: Albert et al. (2011); McKhann et al. (2011) — NIA-AA diagnostic guideline workgroups (refs 25, 26)
- **Type**: imports
- **Delta**: Provide the underlying NIA-AA diagnostic criteria for MCI and dementia due to Alzheimer's disease that the Manly et al. (RW02) classification algorithm operationalizes; this paper does not modify these criteria.
- **Claims affected**: C06, C12, C13.
- **Adopted elements**: Diagnostic-criteria basis for the classification rule.

## Baseline / bounded prior European and global prevalence estimates
- **Hofman et al. (1991)** — EURODEM collaborative study of 1980–1990 findings (ref. 3). **Type**: bounds/refutes — this paper's estimates suggest EURODEM-era prevalence was understated in some regions.
- **Lobo et al. (2000)** — EURODEM collaborative study of population-based cohorts (ref. 4). **Type**: bounds/refutes, same basis as above.
- **Alzheimer Europe (2006)** — European Collaboration on Dementia (EuroCoDe) first interim report (ref. 5). **Type**: bounds/refutes.
- **Prince et al. (2015)** — World Alzheimer Report 2015 (ref. 6). **Type**: bounds/refutes.
- **Alzheimer Europe (2019)** — Dementia in Europe Yearbook 2019 (ref. 7). **Type**: bounds/refutes.
- **OECD (2018, 2021)** — Health at a Glance: Europe reports (refs. 8, 9). **Type**: bounds/refutes — this paper explicitly critiques OECD-rescaling as inheriting non-harmonized-study shortcomings (G1 in `logic/problem.md`).
- All five are cited collectively as the group of "large research consortia [that] have produced prevalence studies of dementia... which mainly rely on systematic reviews of epidemiological or clinical studies" with comparability limitations (§Introduction), and as the studies this paper's estimates are compared against in C04 ("much higher than previously reported¹,³⁻⁹,¹³").

## Global burden / cost context (not directly compared, framing references)
- **IHME (2024)** — Global Burden of Disease 2021 study (ref. 1). Cited for the "8th leading cause of death" statistic (O1). **Type**: related.
- **Wimo et al. (2023)** — "The worldwide costs of dementia in 2019" (ref. 2). Cited for the US$1.3 trillion / US$24,000-per-person cost statistics (O1). **Type**: related.

## Alternative methodological family: unsupervised ML approaches to survey-based dementia prevalence
- **de Cleret, Bayen & Yaffe (2018, 2020)** (refs. 15, 16) and **Gharbi-Meliani et al. (2023)** (ref. 17) — unsupervised machine-learning clustering approaches to identify high likelihood of dementia in population-based surveys. **Type**: baseline. **Delta**: these approaches lack an independent validated ground truth for the MCI/dementia boundary (G1); this paper's HCAP-based validation directly addresses that gap. **Claims affected**: C06 (the validation step this family of approaches lacks).

## Motivating context for data-poor regions
- **Kiejna et al. (2011)** — epidemiological studies of cognitive impairment/dementia in Eastern and Central Europe (ref. 10). **Type**: related — documents the data scarcity motivating G2; also the source of an earlier LW-scale SHARE variant that (per this paper) differs from the LW variant used here.
- **Misiak et al. (2013)** — call for methodological consensus in European dementia prevalence studies (ref. 11). **Type**: related — reinforces G2/O2.

## Calibration and comparison studies
- **Langa et al. (2005)** — ADAMS (Aging, Demographics, and Memory Study) design and methods (ref. 30). **Type**: related. Provides the US "gold standard" calibration target against which the original LW scale was validated; the paper explicitly notes no equivalent European gold-standard target exists for calibrating the HCAP classification thresholds (assumption A2 in `logic/problem.md`).
- **Gross et al. (2024)** — LASI-DAD prevalence study, India (ref. 27). **Type**: related — cross-HCAP comparison precedent motivating the choice of the Manly et al. classification approach.
- **Farrell et al. (2024)** — dementia prevalence in rural South Africa via remote diagnosis/algorithmic modelling (ref. 28). **Type**: related — further cross-HCAP comparison precedent.

## Measurement instruments imported without modification
- **Jones et al. (2024)** — factor structure of the HCAP neuropsychological battery in HRS (ref. 22). **Type**: imports — basis for the five-domain factor structure used in classification.
- **Enders & Bandalos (2001)** — FIML performance for missing data in structural equation models (ref. 23). **Type**: imports — statistical basis for the FIML estimation used to address item nonresponse.
- **Prince et al. (1999)** — development of the EURO-D depression scale (ref. 32). **Type**: imports — depression measure used in the comorbidity regression (Figure 1).
- **UNESCO (1997)** — International Standard Classification of Education (ISCED) (ref. 20). **Type**: imports — education-classification instrument used throughout (Tables 1, 4; Figure 2).

## Interpretive / discussion context
- **Livingston et al. (2024)** — 2024 Lancet Standing Commission report on dementia prevention, intervention and care (ref. 21). **Type**: related — frames the comorbidity/lifestyle risk-factor discussion (Figure 1) and is cited as calling for further cross-national risk-factor research.
- **Bondi et al. (2014)** — neuropsychological criteria for MCI improving diagnostic precision (ref. 19). **Type**: related — background motivation for measuring MCI as a preclinical stage.
- **Huque et al. (2022)** — systematic review/meta-analysis on country-level factors and sex differences in dementia (ref. 31). **Type**: related — cited to interpret the sex/MCI/education finding (C07, C08).
- **Lövden et al. (2020); Nyberg et al. (2021); Seblova et al. (2023)** (refs. 33–35) — debate on whether the education-cognition association is causal. **Type**: related — cited in the Discussion's causality caveat for C11/C08.
