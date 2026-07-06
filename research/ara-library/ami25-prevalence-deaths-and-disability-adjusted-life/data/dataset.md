# Dataset — GBD 2021 (Alzheimer's disease and other dementias, MENA)

## Provenance
- **Name**: Global Burden of Disease (GBD) Study 2021.
- **Producer**: Institute for Health Metrics and Evaluation (IHME).
- **Access point**: IHME GHDx GBD Results Tool (http://ghdx.healthdata.org/gbd-results-tool);
  GBD Compare / VizHub (https://vizhub.healthdata.org/gbd-compare/).
- **Access type**: OPEN / publicly available (verified in `sources.yaml`; data-availability
  statement confirmed via PMC PMC11868542).
- **Verified**: yes (per provided `sources.yaml`; treated as first-class grounded input, not
  re-verified here).

## Selection / scope for this study
- **Cause**: Alzheimer's disease and other dementias.
- **Locations**: "North Africa and Middle East" GBD region and its 21 countries/territories —
  Afghanistan, Algeria, Bahrain, Egypt, Iran (Islamic Republic of), Iraq, Jordan, Kuwait, Lebanon,
  Libya, Morocco, Oman, Palestine, Qatar, Saudi Arabia, Sudan, Syrian Arab Republic, Tunisia, Turkey,
  United Arab Emirates, Yemen.
- **Years**: 1990–2021 (2021 reference; 1990 comparison).
- **Stratifiers**: age (five-year bands 40–44 … 95+), sex (male, female), Socio-demographic Index.

## Variables extracted
- Prevalence: counts and age-standardised rate per 100,000, with 95% UI.
- Deaths: counts and age-standardised rate per 100,000, with 95% UI.
- DALYs: counts and age-standardised rate per 100,000, with 95% UI.
- Percentage change in age-standardised rates, 1990→2021, with 95% UI.
- (For Fig 4) Socio-demographic Index per country/year.
- (For Fig 3) Global DALY rates by age/sex for the MENA/Global ratio.

## Case definition (as inherited from GBD 2021)
- Reference: DSM III/IV/V or ICD; ICD-10 F00, F01, F02, F03, G30, G31; ICD-9 290, 291.2, 291.8, 294,
  331. Severity reference: Clinical Dementia Rating (CDR). See `logic/solution/study_design.md`.

## Licensing / ethics
- Aggregate, de-identified modelled estimates; publicly available.
- This analysis approved by Ethics Committee of Shahid Beheshti University of Medical Sciences
  (IR.SBMU.RETECH.REC.1403.067).
- Article open access under CC BY-NC-ND 4.0.

## Size / granularity
- 21 countries + 1 regional aggregate + Global (for ratio) × 3 measures × (counts, ASR, %change) ×
  (1990, 2021) × age/sex strata. The main article surfaces the aggregate + per-country 2021 values in
  Table 1 and the age/sex/SDI structure in Figures 1–4; finer per-country strata reside in the online
  Supplementary Tables S1–S3 (not part of the provided input — see `evidence/README.md`).

## Preprocessing
- No preprocessing by the authors beyond selection/extraction and descriptive plotting; all data
  cleaning, sex/age-splitting, crosswalking, and modelling are performed upstream by IHME (see
  `logic/solution/study_design.md` §3–4). No separate `preprocessing.md` is warranted.
