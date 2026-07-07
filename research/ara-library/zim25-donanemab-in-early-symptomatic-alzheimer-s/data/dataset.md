# Dataset

## Primary dataset — TRAILBLAZER-ALZ 2 individual participant data (placebo-controlled period + LTE)
- **Provenance**: Phase 3, randomized, double-blind, parallel-group, multicenter, placebo-controlled
  trial of donanemab in early symptomatic AD (NCT04437511), conducted at 277 centers in 8 countries
  (Australia, Canada, Czech Republic, Japan, Netherlands, Poland, United Kingdom, United States).
  Sponsored by Eli Lilly and Company. Pivotal 76-week report: Sims et al. 2023 (JAMA) [2]. This
  paper reports the subsequent 78-week LTE (154 weeks total).
- **Source / access**: No data-sharing / IPD-access statement is present in this paper (contrast
  with the companion post-hoc analysis on this same trial, which states Vivli on-request access —
  see `src/environment.md`). Not available from provided input for this paper specifically.
- **Size (placebo-controlled period)**: 1736 randomized 1:1 (donanemab N=860, placebo N=876).
- **Size (LTE)**:
  - Early-start (randomized donanemab) dosed in LTE: 550/860 (64.0%) — of whom 393 switched to
    placebo (donanemab→placebo) and 157 continued donanemab (donanemab→donanemab).
  - Delayed-start (randomized placebo) dosed in LTE: 657/876 (75.0%) (placebo→donanemab).
- **Ethics**: All procedures complied with relevant laws and institutional guidelines and were
  approved by appropriate institutional committees; written informed consent obtained from
  participants and study partners (§2.1). No animal studies.
- **Key variables**: CDR-SB (and CDR-G) scores; amyloid PET (Centiloids); APOE ε4 genotype; age;
  sex; ADAS-Cog13 score; screening MMSE score; tau PET category; AChEI/memantine use; treatment
  course completion status; AE/TEAE/SAE/ARIA-E/ARIA-H/infusion-related-reaction data.
- **Notable subset definitions**: Early-start vs delayed-start (defined by original randomization
  arm); donanemab→placebo / donanemab→donanemab / placebo→donanemab treatment-sequence groups
  (Table 1); the subset of early-start participants who met treatment course completion criteria
  by 52 weeks (used for the amyloid-reaccumulation and a CDR-SB sensitivity analysis, Fig. 2c/4c).

## External comparison dataset — ADNI (Alzheimer's Disease Neuroimaging Initiative)
- **Provenance**: Public-private partnership launched in 2003 (PI Michael W. Weiner, MD), funded
  by the National Institute on Aging (NIH Grant U19AG024904); historical funding also from the
  National Institute of Biomedical Imaging and Bioengineering, the Canadian Institutes of Health
  Research, and private-sector contributions via the Foundation for the National Institutes of
  Health (partner list in the paper's Acknowledgements includes AbbVie, Alzheimer's Association,
  Alzheimer's Drug Discovery Foundation, Araclon Biotech, Bioclinica, Biogen, Bristol Myers Squibb,
  CereSpir, Cogstate, Eisai, Elan Pharmaceuticals, Eli Lilly and Company, Euroimmun, Fujirebio, GE
  HealthCare, IXICO, Janssen Alzheimer Immunotherapy R&D, Johnson & Johnson Pharmaceutical R&D,
  Lumosity, Lundbeck, Merck, Meso Scale Diagnostics, NeuroRx, Neurotrack Technologies, Novartis,
  Pfizer, Piramal Imaging, Roche/Genentech, Servier, Takeda Pharmaceuticals, Transition
  Therapeutics).
- **Use**: Untreated (amyloid-targeting-therapy-naïve) external comparison cohort for the LTE
  CDR-SB efficacy analyses, since the LTE has no internal placebo arm.
- **ADNI matching eligibility**: Presence of cognitive impairment and CSF total-tau/amyloid-β42
  ratio >0.28 (established amyloid-pathology criterion per Roche Diagnostics Elecsys total-tau CSF
  method sheet [4]).
- **Matching pool**: 2430 ADNI participants evaluated; 534 met eligibility criteria and were used
  in propensity score weighting calculations.
- **Effective sample size (ESS) after weighting**: 268 (early-start comparison, baseline); 301
  (delayed-start comparison, baseline) — both decline over follow-up (e.g., early-start ESS falls
  to 122 at 36 months).
- **Access**: Via ADNI's standard data-application process (adni.loni.usc.edu).
- **Limitation**: Baseline amyloid CL level was missing for 43% of the eligible ADNI-derived
  population and was therefore excluded from the propensity-weighting covariates. The external
  cohort may also differ from TRAILBLAZER-ALZ 2 in study conduct, assessments, time period, and
  geographic region, and is subject to unmeasured confounding (§4 Discussion).

## Reaccumulation-model source studies (amyloid biomarker data only, not IPD for efficacy)
- Phase 1b study (NCT02624778); TRAILBLAZER-ALZ (phase 2; NCT03367403); TRAILBLAZER-EXT (phase 2
  LTE parts B and C; NCT04640077) — combined with this paper's LTE amyloid data into an existing
  cross-study exposure-response model [5] to estimate the 2.4 CL/year reaccumulation rate (C10).
