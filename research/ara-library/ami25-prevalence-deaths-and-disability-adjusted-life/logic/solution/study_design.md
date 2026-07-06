# Study Design — GBD 2021 pipeline as applied to AD and other dementias in MENA

This paper does not develop a new method; it applies IHME's GBD 2021 estimation machinery and
presents descriptive summaries for the MENA region. This file documents the pipeline as the paper
describes it (Methods, pp.2–4), which is the "method layer" a downstream agent needs to interpret
the results. Detailed GBD 2021 methodology is deferred to ref 26 (Lancet 2024).

## 1. Scope and framing
- **Design**: Secondary analysis of GBD 2021 estimates; observational, descriptive-epidemiological.
- **Coverage**: GBD 2021 covered 371 diseases/injuries across 204 countries/territories in 21 regions
  (and 811 subnational locations), 1990–2021. This study restricts to "Alzheimer's disease and other
  dementias" within the MENA ("North Africa and Middle East") region — 21 countries.
- **Stratification**: by country, year (1990, 2021 focus), age (five-year bands 40–44 … 95+), sex,
  and Socio-demographic Index.
- **Outputs**: prevalence, deaths, DALYs as counts and age-standardised rates per 100,000, each with
  a 95% UI.

## 2. Case definition and data sources
- **Reference case definitions**: DSM editions III, IV, or V, or ICD case definitions.
  ICD-10 codes: F00, F01, F02, F03, G30, G31. ICD-9 codes: 290, 291.2, 291.8, 294, 331.
- **Severity reference**: Clinical Dementia Rating (CDR) scale.
- **Screening/diagnostic tools recognised**: CDR (primary), MMSE, GMS; and for severity: CDR-SB,
  BIMC, GDS, GMS, CAMDEX, DSM-III-R, Karasawa's scale.
- **Accepted alternative definitions**: algorithmic modelling, general-practitioner data, clinical
  records, the 10/66 algorithm, and NIA-AA criteria.
- **Exclusion**: studies assessing severity via cognition/memory-only scales that do not evaluate
  activities of daily living (e.g. MMSE-only) were omitted.
- **Data inputs**: surveys and administrative/claims data (prevalence, incidence); relative-risk
  studies and linked hospital-to-mortality records (mortality). GBD 2021 introduced incidence data in
  dementia modelling for the first time.

## 3. Non-fatal (prevalence/incidence) modelling
- Prevalence data underwent sex-splitting, crosswalking, and age-splitting. "Both-sexes" data were
  split using an MR-BRT model ratio of female-to-male prevalence; data with age ranges >25 years were
  split using the global age pattern.
- **DisMod-MR 2.1 Model 1** (Bayesian meta-regression) with two country-level covariates:
  age-standardised education (proxy for brain health / protection) and age-standardised smoking
  prevalence (both sexes; positive correlation with dementia risk).
- **DisMod-MR 2.1 Model 2** integrated cause-specific mortality from the final fatal estimates.
- **Double-counting adjustment**: to avoid counting dementia caused by other conditions (stroke,
  Parkinson's disease, TBI, Down's syndrome), age-specific relative risks were derived (logistic
  regression on the ADAMS dataset + systematic reviews), converted to population attributable
  fractions (PAFs) per cause and age, and the attributable prevalence subtracted from total
  prevalence to isolate dementia not resulting from other GBD causes.

## 4. Fatal (mortality) modelling
- Dementia's mortality and morbidity are modelled together, because prevalence data are stable over
  time while vital-registration mortality rose steeply in high-income countries — a discrepancy
  attributed to coding-practice shifts, not real epidemiology.
- Since GBD 2019, fatal modelling removed reliance on vital-registration data. Instead, relative-risk
  of all-cause mortality linked to dementia exposure was extracted via a systematic PubMed review.
- A meta-analysis of attributable-risk data incorporated covariates (age, sex, exposure category
  [all dementia / AD / cognitive impairment], clinical-sample flag) and controlled variables
  (education, CVD comorbidity, smoking, alcohol, ADLs / nursing-home residence).
- A second Bayesian bias-reduction meta-regression (MR-BRT) estimated relative risks; excess deaths
  attributable to dementia were modelled by multiplying adjusted estimates by attributable risk.

## 5. Compilation and presentation
- 1000 draws were generated per estimate and summed across age, cause, and location, propagating
  uncertainty. 95% UIs = 2.5th and 97.5th percentiles of the sorted draws.
- Age separated into five-year intervals.
- Analysis and plotting in **R version 3.5.2**: age-standardised point prevalence, death, and DALY
  rate plots (Figs 1–3).
- **Smoothing-spline models** were applied to examine the SDI–burden relationship (Fig 4), giving the
  expected-value ("Smooth") curve against which observed country rates are compared.

## 6. What is original to THIS paper vs inherited from GBD
- Inherited from IHME/GBD 2021: all estimation (DisMod-MR 2.1, MR-BRT, PAF adjustment, fatal
  modelling, draw-based UIs).
- Original to this paper: the MENA-specific extraction, country/age/sex/SDI decomposition, the
  descriptive plots and smoothing-spline SDI visualisation, the MENA-vs-global DALY-ratio framing,
  and the interpretation.
