# Concepts

## Limited-duration dosing / treatment course completion criteria
- **Notation**: <11 CL (single scan) or <25 CL (two consecutive scans)
- **Definition**: A dosing design in which participants receiving donanemab are switched, in a blinded fashion, to placebo infusions once they meet amyloid-based "treatment course completion criteria": an amyloid plaque level of <11 Centiloids (CL) on any single PET scan, or <25 CL on two consecutive PET scans. Assessed at weeks 24, 52, 76 (placebo-controlled period) and 102, 130 (LTE).
- **Boundary conditions**: Implemented "to eliminate potentially unnecessary treatments and reduce cost for future patients" (§1); applies only to participants originally/currently receiving donanemab, not those on placebo.
- **Related concepts**: Early-start group, delayed-start group, amyloid clearance

## Early-start group / delayed-start group
- **Notation**: —
- **Definition**: "Early-start" = participants initially randomized to donanemab during the 76-week placebo-controlled period (N=860), including those later switched to blinded placebo upon treatment course completion. "Delayed-start" = participants initially randomized to placebo (N=876) who continued into the LTE and started donanemab at LTE entry (78 weeks post-randomization), including those later switched to blinded placebo upon treatment course completion during the LTE.
- **Boundary conditions**: Only participants who entered the LTE and received ≥1 infusion are analyzed as early-/delayed-start (550/860 = 64.0% and 657/876 = 75.0%, respectively); participants who discontinued before the LTE are excluded from these groups.
- **Related concepts**: Long-term extension (LTE), limited-duration dosing

## Long-term extension (LTE)
- **Notation**: —
- **Definition**: A participant- and investigator-blinded 78-week extension period following the 76-week placebo-controlled period of TRAILBLAZER-ALZ 2, bringing total observation to 154 weeks (~3 years). The LTE has no internal placebo control.
- **Boundary conditions**: Blinding to treatment assignment (donanemab vs placebo infusion) is retained throughout, including after participants are switched to placebo upon treatment course completion — this is explicitly noted as reducing participant/observer bias relative to a traditional open-label extension design.
- **Related concepts**: Early-start group, delayed-start group, ADNI external control cohort

## ADNI external control cohort / propensity score weighting
- **Notation**: ATT (average treatment effect among the treated), IPW (inverse probability weighting)
- **Definition**: Because the LTE has no internal placebo, CDR-SB trajectories are compared against an external, amyloid-targeting-therapy-naïve cohort drawn from the Alzheimer's Disease Neuroimaging Initiative (ADNI) database, selected on cognitive impairment plus CSF total-tau/amyloid-β42 ratio >0.28. Propensity score weights for the ADNI cohort were estimated with the ATT estimand using inverse probability weighting from a generalized linear model (WeightIt R package), on covariates: age, sex, APOE ε4 status (non-carrier/heterozygous/homozygous), CDR-SB score, ADAS-Cog13 score, and screening MMSE score.
- **Boundary conditions**: Baseline amyloid CL level was excluded from the weighting covariates because it was missing for 43% of the eligible ADNI-derived population; weights were checked for covariate balance (standardized mean difference <0.10 per covariate) and trimmed at the 95th percentile to limit the influence of extreme weights.
- **Related concepts**: Effective sample size (ESS), MMRM, LTE

## Effective sample size (ESS)
- **Notation**: ESS
- **Definition**: The reduced, weight-adjusted sample size of the ADNI cohort after propensity-score weighting, reflecting the loss of precision from unequal weights; reported alongside each CDR-SB comparison timepoint (e.g., ESS=268 for the early-start weighting, ESS=301 for the delayed-start weighting, at their respective analysis baselines).
- **Boundary conditions**: Declines over follow-up as ADNI participants are lost to the visit schedule (e.g., early-start ESS falls from 268 at baseline to 122 at 36 months).
- **Related concepts**: ADNI external control cohort, propensity score weighting

## CDR-Sum of Boxes (CDR-SB) and CDR-Global (CDR-G)
- **Notation**: CDR-SB (0–18); CDR-G (0–3)
- **Definition**: The Clinical Dementia Rating (CDR) scale measures both cognition and function. CDR-SB is the sum of six domain box scores (0–18, higher = greater impairment), used as the primary continuous efficacy outcome for LTE comparisons to the ADNI cohort. CDR-Global (CDR-G) is the overall staging score (0 = no dementia to 3 = severe dementia, higher = greater impairment), used to define discrete disease-stage progression events for the early- vs delayed-start hazard analysis.
- **Boundary conditions**: CDR-SB is compared to ADNI because of its availability in the ADNI database; CDR-G progression requires an increase in score at two consecutive visits (participants assessed every 3 months).
- **Related concepts**: MMRM, Cox proportional hazards model, minimal clinically important difference (MCID)

## Minimal clinically important difference (MCID) — inapplicability to between-group LTE comparison
- **Notation**: —
- **Definition**: A patient-level threshold for what constitutes a clinically important individual change on a scale (e.g., CDR-SB); the paper explicitly argues these thresholds are designed to evaluate individual patient change and "are not fit to interpret between-group differences at a study endpoint" (§4, citing [16]).
- **Boundary conditions**: The paper instead treats any CDR-G stage transition as inherently clinically meaningful, and additionally reports time-saved as a complementary framing.
- **Related concepts**: CDR-Sum of Boxes and CDR-Global, time saved (time-progression framing)

## Amyloid clearance and Centiloids (CL)
- **Notation**: CL
- **Definition**: Brain amyloid plaque burden measured by amyloid PET on the Centiloid (CL) scale. Amyloid clearance is defined as achieving a level <24.1 CL.
- **Boundary conditions**: Clearance is distinct from the (lower) treatment course completion thresholds of <11 CL (single scan) / <25 CL (two consecutive scans) used to trigger the blinded switch to placebo.
- **Related concepts**: Limited-duration dosing, amyloid reaccumulation rate, MMRM

## Amyloid reaccumulation rate
- **Notation**: CL/year
- **Definition**: The rate at which amyloid plaque re-accumulates after donanemab discontinuation, estimated (2.4 CL/year) by incorporating this LTE's data into an existing exposure-response model built from three earlier donanemab studies: a phase 1b study (NCT02624778), TRAILBLAZER-ALZ (phase 2; NCT03367403), and TRAILBLAZER-EXT (phase 2 LTE parts B and C; NCT04640077), alongside TRAILBLAZER-ALZ 2 itself.
- **Boundary conditions**: Estimated specifically among early-start participants who met treatment course completion criteria by 52 weeks; compared qualitatively (not via formal statistical test in this paper) to independently reported natural amyloid accumulation rates ([14],[15]).
- **Related concepts**: Amyloid clearance and Centiloids, limited-duration dosing

## Mixed model for repeated measures (MMRM)
- **Notation**: —
- **Definition**: The statistical model used for continuous change-from-baseline outcomes (CDR-SB, amyloid CL) across visits. For the CDR-SB LTE analyses, three MMRM analyses were run using ADNI weights: (1) TRAILBLAZER-ALZ 2 placebo arm vs weighted ADNI cohort through 76 weeks (to validate the external control), (2)/(3) donanemab arm (early-/delayed-start) vs weighted ADNI cohort at 154 weeks. Covariates: treatment, age, APOE ε4 status, baseline CDR-SB, baseline ADAS-Cog13, screening MMSE, visit, visit-by-treatment and visit-by-baseline-CDR-SB interactions. For amyloid CL, covariates were treatment, visit, treatment-by-visit interaction, score, score-by-visit interaction, age, and tau category.
- **Boundary conditions**: Treatment differences computed as LS mean differences between TRAILBLAZER-ALZ 2 groups and the external weighted ADNI cohort at each visit.
- **Related concepts**: ADNI external control cohort / propensity score weighting, area under the curve (AUC) analysis

## Area under the curve (AUC) analysis and time saved
- **Notation**: —
- **Definition**: A cumulative-benefit summary computed as the LS mean difference between AUCs (trapezoidal-rule weights) of the early-start group and the weighted ADNI cohort on CDR-SB change. "Time saved" is a complementary framing: the additional time it would take the comparator (ADNI cohort) to reach the same CDR-SB change already observed in the treated group, estimated by calculating the ADNI-cohort and early-start-group lines between 24–36 months and back-calculating the ADNI timepoint matching the mean 36-month early-start value.
- **Boundary conditions**: Time-saved does not account for the generally higher rate of disease progression at later disease stages, so the paper cautions that the estimate may understate the true benefit of earlier initiation.
- **Related concepts**: MMRM, CDR-Sum of Boxes and CDR-Global

## Amyloid-related imaging abnormalities (ARIA-E, ARIA-H) and observation-time-adjusted incidence rate (OAIR)
- **Notation**: ARIA, ARIA-E, ARIA-H, OAIR
- **Definition**: ARIA-E is edema/effusion; ARIA-H is microhemorrhages and hemosiderin deposits (based on MRI or TEAE-cluster reporting). OAIR is the incidence rate adjusted for differing amounts of observation time, calculated as (number of participants with ≥1 AE of a given category × 100) ÷ participant-years at risk — used to compare ARIA incidence across groups/periods with unequal follow-up durations.
- **Boundary conditions**: Time-to-first-ARIA-E analysis covers the treatment period plus 57 days; post-discontinuation ARIA risk assessed in 6-month intervals starting 58 days after the last donanemab dose.
- **Related concepts**: Limited-duration dosing, safety overview (Table 1)

## Cox proportional hazards model (CDR-G progression)
- **Notation**: HR
- **Definition**: Used to estimate the hazard ratio, 95% CI, and p value for early- vs delayed-start progression risk on CDR-G. Stratified by pooled investigator and baseline tau level; includes baseline covariates of age, CDR-G score, and acetylcholinesterase inhibitor/memantine use, with treatment group (early-start or delayed-start) as a fixed factor.
- **Boundary conditions**: Progression defined as an increase in CDR-G score at two consecutive visits (assessed every 3 months); the visit date of the first consecutive visit is used as the event time.
- **Related concepts**: CDR-Sum of Boxes and CDR-Global
