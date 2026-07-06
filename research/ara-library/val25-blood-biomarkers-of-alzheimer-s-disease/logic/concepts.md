# Concepts

## AD blood biomarkers (six analytes)
Serum concentrations of six molecules measured via Simoa (Single molecule array) immunoassays: amyloid-β42/40 ratio (Aβ42/40), phosphorylated-tau181 (p-tau181), phosphorylated-tau217 (p-tau217), total-tau (t-tau), neurofilament light chain (NfL), and glial fibrillary acidic protein (GFAP). Aβ42/40, Aβ42, and t-tau were measured with the Simoa Neuro 3-plex A Kit; p-tau181 with the Simoa pTau-181 Advantage V2 Kit; p-tau217 with the Simoa ALZpath p-Tau-217 Advantage PLUS Kit; NfL and GFAP with the Simoa Neuro 2-plex B Kit (p.6, Methods).

## Amyloid-β42/40 ratio (Aβ42/40)
Ratio of two amyloid-β peptide species in serum; lower ratio is the direction associated with AD pathology. In this study it showed the weakest associations with cognitive deterioration among the six biomarkers, attributed to blood Aβ levels correlating less directly with brain amyloid deposition than CSF levels and being ~10-fold lower than CSF concentrations (p.5, Discussion).

## p-tau217 (phosphorylated-tau217)
A tau phosphoform proposed as a standalone blood-based AD diagnostic biomarker (ref. 20) and considered the most sensitive blood biomarker for AD pathology (refs. 31-34); in this study, one of the two strongest biomarkers (with NfL) for MCI-to-dementia progression, and specifically more strongly associated with AD dementia than all-cause dementia (p.5).

## Neurofilament light chain (NfL)
A non-specific marker of axonal/neuronal loss; the strongest single biomarker for MCI-to-dementia progression in this study. Because it is not AD-specific, the authors interpret its predictive value in the community as reflecting its sensitivity to all-cause neurodegeneration, relevant given that most late-life dementia in the community results from mixed neuropathology (p.5).

## Glial fibrillary acidic protein (GFAP)
A marker of astrocytic activation, potentially reflecting a response to amyloid plaque formation; the third-strongest biomarker overall, and — together with NfL and p-tau181 — associated with reduced hazard of MCI reversion to normal cognition (p.2, p.5).

## Total-tau (t-tau) and p-tau181
Additional tau-related serum markers; both showed significant but comparatively modest associations with MCI-to-dementia progression, with limitations analogous to Aβ (t-tau) or attenuation after further adjustment (p-tau181-reversion; see C04) (p.5).

## Mild cognitive impairment (MCI) — study operationalization
Defined via a neuropsychological test battery covering five cognitive domains: executive function (Trail Making Test Part B), episodic memory (free recall), visuospatial abilities (mental rotations), language (Category and Letter Fluency), and perceptual speed (digit cancellation, pattern comparison). Domain scores are standardized to age-specific z-scores (averaging multiple tests per domain where available). An individual is classified as having MCI if they score ≤1.5 SD below the age-specific mean in at least one domain, exhibit largely preserved functional independence (no more than one impaired instrumental activity of daily living [IADL] and preserved basic ADLs), and have no dementia diagnosis (p.6, Methods).

## Cognitive impairment, no dementia (CIND) — alternative operationalization
A looser alternative to MCI: scoring ≤1.5 SD below the age-specific mean in at least one cognitive domain, in the absence of a dementia diagnosis, **without** the MCI definition's functional-independence requirement (p.6, Methods). Used in a sensitivity analysis (C13).

## All-cause and AD dementia diagnosis
Diagnosed per DSM-IV criteria (all-cause) and NINCDS-ADRDA criteria (AD dementia), via a three-step procedure: an initial examining physician's diagnosis, a second blinded physician's independent review, and — if they disagree — adjudication by a senior neurologist external to data collection. Deaths without a diagnosis were cross-checked against clinical charts and the Swedish Cause of Death Register (p.7, Methods).

## Four-state multistate Markov model
A parametric survival model (implemented with the R `msm` package, ref. 56) with three cognitive states — normal cognition (NC), MCI, dementia — plus death as an absorbing state (from which no return transition is possible). The model accounts for interval censoring (states observed only at scheduled visits), disallows a direct NC→dementia transition (assumed to pass through an unobserved MCI phase), and treats MCI↔NC as the only reversible transition pair. Baseline transition hazards follow a Gompertz distribution, with **age** (not calendar time or study time) as the model's time scale (p.7, Statistical analysis).

## Restricted cubic spline modeling of biomarker z-scores
Continuous biomarkers are standardized to z-scores and entered into the multistate model as restricted cubic splines with three pre-specified knots at the 25th, 50th, and 75th percentiles, allowing non-linear dose-response shapes; the median value is the reference point for each biomarker's HR curve (Fig. 1 caption, p.3).

## Predefined dichotomization cut-offs (Youden's index-derived)
Cut-off values used to split each biomarker into high/low groups were derived in a prior study (Grande et al., ref. 9) using a non-parametric bootstrapping procedure (5000 iterations) on an 80% training split to identify, per biomarker, the threshold maximizing Youden's Index for predicting 10-year all-cause dementia onset, validated on the remaining 20% test split. The resulting cut-offs applied here: 0.057 (Aβ42/40 ratio), 1.512 pg/mL (p-tau181), 0.134 pg/mL (p-tau217), 0.832 pg/mL (t-tau), 20.171 pg/mL (NfL), 142.515 pg/mL (GFAP) (p.6, Methods; Table 2 footnote).

## Hazard ratio (HR) with 95% confidence interval
The effect-size metric reported throughout: the ratio of transition hazards (e.g., MCI→dementia) comparing a higher biomarker value/group to a reference (median z-score or "low" group), estimated from the multistate Markov model, alongside a 95% CI.

## Basic vs. fully adjusted model
Two covariate-adjustment tiers used throughout Table 2 and the combination analyses: the "basic model" adjusts for sex and education; the "fully adjusted model" further adjusts for chronic kidney disease, heart disease, cerebrovascular disease, anemia, and obesity — comorbidities the authors previously found to be associated with AD blood biomarker levels (ref. 42) (p.7, Statistical analysis).

## Inverse probability weighting (IPW) for attrition
A sensitivity-analysis technique in which each participant's contribution is weighted by the inverse of their estimated probability of remaining in the analytic sample (modeled via logistic regression on age, sex, education, number of chronic diseases, and biomarker levels), used to correct for potential bias introduced by differential dropout/attrition (p.7, Methods).

## SNAC-K cohort
The Swedish National study on Aging and Care in Kungsholmen: an ongoing population-based longitudinal study that enrolled 3363 randomly selected individuals aged 60+ from Stockholm's Kungsholmen district at baseline (2001-2004; 73% participation rate), with re-assessment every six years (age <78) or three years (age ≥78) (p.6, Methods).
