# Concepts

Genuine technical terms used by the paper, defined as the source uses them.

## Disability-Adjusted Life Year (DALY)
- **Notation**: DALY
- **Definition**: A summary measure of disease burden combining years of life lost to premature
  mortality (YLL) and years lived with disability (YLD). Reported here as counts and as
  age-standardised rates per 100,000 with 95% UIs, for AD and other dementias.
- **Boundary conditions**: In GBD 2021, computed for 371 diseases/injuries across 204 countries and
  territories, 1990–2021. For dementia, morbidity and mortality are modelled together (see "Fatal
  modelling strategy").
- **Related concepts**: Age-standardised rate, YLD, prevalence, deaths, Socio-demographic Index

## Age-standardised rate (ASR)
- **Notation**: ASR (per 100,000)
- **Definition**: A rate adjusted to a standard age structure so that populations with different age
  distributions can be compared without confounding by age. The paper reports age-standardised point
  prevalence, death, and DALY rates per 100,000.
- **Boundary conditions**: Age was separated into five-year intervals; standardisation enables the
  cross-country and 1990-vs-2021 comparisons that drive every claim.
- **Related concepts**: DALY, prevalence, percentage change, uncertainty interval

## 95% Uncertainty Interval (UI)
- **Notation**: 95% UI
- **Definition**: The interval spanning the 2.5th to 97.5th percentiles of 1000 posterior draws
  generated for each prevalence, death, or DALY estimate, summed across age, cause, and location. It
  conveys the full estimation uncertainty of the GBD pipeline.
- **Boundary conditions**: A percentage change is treated as "statistically significant" when its
  95% UI excludes zero. Wide UIs (notably for deaths and in low/middle-income countries) are a stated
  limitation.
- **Related concepts**: Draws, statistical significance, DisMod-MR 2.1

## DisMod-MR 2.1
- **Notation**: DisMod-MR 2.1 (Model 1, Model 2)
- **Definition**: The Bayesian meta-regression disease model IHME uses to synthesise sparse and
  heterogeneous epidemiological data into internally consistent prevalence/incidence estimates.
  Model 1 incorporated two country-level covariates (age-standardised education; age-standardised
  smoking prevalence for both sexes); Model 2 integrated cause-specific mortality from the fatal
  estimates and adjusted for double-counting of dementia caused by other conditions.
- **Boundary conditions**: Used for non-fatal (prevalence/incidence) modelling; combined with fatal
  modelling because dementia's prevalence and cause-of-death records diverge.
- **Related concepts**: MR-BRT, PAF, GBD study, relative risk

## MR-BRT (Meta-Regression—Bayesian, Regularised, Trimmed)
- **Notation**: MR-BRT
- **Definition**: The Bayesian meta-regression tool used to derive a model ratio of female-to-male
  prevalence, allowing data points labelled "both sexes" to be split into male- and female-specific
  points. Also used (as a "second Bayesian bias-reduction meta-regression model") to estimate
  relative risks in the fatal-modelling step.
- **Boundary conditions**: Applied during sex-splitting, crosswalking, and relative-risk estimation.
- **Related concepts**: DisMod-MR 2.1, crosswalking, relative risk

## Population Attributable Fraction (PAF)
- **Notation**: PAF
- **Definition**: The fraction of dementia prevalence attributable to a specific antecedent cause
  (stroke, Parkinson's disease, TBI, Down's syndrome), computed from age-specific relative risks
  (derived via logistic regression on the ADAMS dataset plus systematic reviews). Multiplying the PAF
  by total prevalence and subtracting isolates dementia not caused by other GBD causes, avoiding
  double-counting.
- **Boundary conditions**: Used in the non-fatal modelling adjustment step (Model 2).
- **Related concepts**: DisMod-MR 2.1, relative risk, ADAMS study

## Socio-demographic Index (SDI)
- **Notation**: SDI (0–1 scale)
- **Definition**: A composite GBD indicator of a location's development level (income per capita,
  education, fertility) used to define expected disease rates. Here it is the X-axis of Figure 4,
  where each MENA country's observed age-standardised DALY rate is compared against the SDI-expected
  value (a smoothing-spline "Smooth" line).
- **Boundary conditions**: MENA countries span SDI ≈0.2–0.85; the observed relationship is
  non-monotonic and no clear trend is claimed.
- **Related concepts**: DALY, smoothing splines, expected value

## Severity split (Clinical Dementia Rating, CDR)
- **Notation**: CDR (reference); CDR-SB, BIMC, GDS, GMS, CAMDEX, Karasawa's scale (accepted tools)
- **Definition**: The GBD procedure (restructured since GBD 2019 via a new systematic review) that
  distributes the dementia population across severity classes. CDR is the reference severity scale;
  doctor-given diagnoses under DSM III/IV/V or ICD are the reference case definitions. Cognition-only
  scales (e.g. MMSE) that do not assess activities of daily living were excluded.
- **Boundary conditions**: Severity classification is required because dementia's disability weight
  depends on severity distribution.
- **Related concepts**: Case definition, YLD, DALY

## Cognitive reserve
- **Notation**: —
- **Definition**: The capacity, built through education, occupation, and lifestyle, to buffer against
  clinical expression of dementia pathology. Invoked to explain the higher female burden: historical
  gaps in women's education/high-skill occupations may leave them with less cognitive reserve.
- **Boundary conditions**: An explanatory (interpretive) concept in the Discussion, not measured in
  this study.
- **Related concepts**: Sex difference, ApoE4, risk factors

## Global Burden of Disease (GBD) study
- **Notation**: GBD 2021 (and GBD 2016, 2019 for comparison)
- **Definition**: IHME's systematic, standardised programme estimating incidence, prevalence, YLDs,
  DALYs, and healthy life expectancy for 371 diseases/injuries across 204 countries/territories (and
  811 subnational locations) and 21 regions, 1990–2021. It is the sole data source for this paper.
- **Boundary conditions**: Core principle "some data is better than no data"; quality depends on
  local data-collection policies and disease type.
- **Related concepts**: DisMod-MR 2.1, DALY, GHDx, SDI
