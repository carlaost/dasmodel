# Study Design

An observational, claims-based epidemiology study applying the PAF-based disparity decomposition to
US Medicare data. Source: §2 Methods.

## Data source
- Administrative claim records from a **nationally representative 5% sample** of the US Medicare
  population, spanning **1991–2020**.
- Data allow reconstruction of individual trajectories with identified initial/final age of
  follow-up, dates of death and disease onset, and basic demographics.

## Cohorts and follow-up
- **Four cohorts** with baseline ages **70, 75, 80, and 85**, formed with data from the 2000–2020
  period and using data from 1991–2000 for look-back.
- **Follow-up time: 5 years.**
- **Outcome**: AD onset, with **death treated as independent censoring**.
- **Exclusions**: individuals with claims for AD/ADRD at baseline; individuals who spent **>20% of
  their study time enrolled in Medicare Advantage** (analysis restricted to fee-for-service
  beneficiaries).

## Disparities studied (six)
1. Black–White (BW)
2. White–Native American (WN)
3. Hispanic–White (HW)
4. White–Asian (WA)
5. female–male (FM)
6. stroke-belt states vs states without a common border with the stroke belt (SB)

Disparity pairs are ordered so the first subpopulation is the higher-risk one (observed disparity
numerically > 1).

## Predictors
- **Low income**: Medicare/Medicaid **dual eligibility** (binary).
- **10 candidate AD/ADRD-related diseases** (Table S1, supporting information), each measured as a
  binary, time-independent indicator at baseline via previously published Medicare ascertainment
  algorithms (ref 18).
- **First-stage screening** removed four conditions with no significant contribution across all
  cohorts: **rheumatic heart disease, systemic hypotension, chronic liver disease, and traumatic
  brain injury**.
- **Six retained disease predictors**: cerebrovascular disease (stroke), arterial hypertension,
  diabetes mellitus, renal disease, heart failure, and depression — plus low income (7 predictors
  total in the final decomposition).

## Estimation and inference
- Univariable Cox model → observed disparity per pair.
- Multivariable Cox model (Eq. 1) → unexplained disparity `R_r` and relative risks `R_0i`, `R_1i`.
- Decomposition (Eq. 6) → total, exposure, and vulnerability factors (Table 4).
- **Bootstrap**: resampling with replacement to create **100 random samples** for standard errors
  and confidence intervals.
- **Sensitivity analyses** (three alternatives): 180-day AD-onset confirmation period; no
  confirmation period; and ADRD instead of AD as the outcome (Table S3, supporting information).

## Ethics
Data analysis was designed and performed per the ethical standards of the responsible committee on
human studies and the Declaration of Helsinki (1975, revised 1983); approved by the University
Health System Institutional Review Board. Informed consent was not necessary (Consent Statement).
