# Study Design (TRAILBLAZER-ALZ 2 Long-Term Extension)

## Underlying trial
- **Trial**: TRAILBLAZER-ALZ 2, phase 3, randomized, double-blind, parallel-group, multicenter, placebo-controlled trial (NCT04437511), with an additional 78-week long-term extension (LTE) period. Conducted at 277 centers in eight countries (Australia, Canada, Czech Republic, Japan, Netherlands, Poland, United Kingdom, United States).
- **Drug/dosing**: Donanemab administered intravenously at 700 mg for the first three doses and 1400 mg thereafter, every 4 weeks (Q4W).
- **Randomization**: 1736 participants randomized 1:1 to donanemab (N=860) or placebo (N=876) for the 76-week placebo-controlled period.
- **Eligibility (placebo-controlled period)**: Age 60–85, screening MMSE 20–28, amyloid pathology (≥37 CL) by ¹⁸F-florbetapir or ¹⁸F-florbetaben PET, and tau pathology by ¹⁸F-flortaucipir PET with central image evaluation. Key exclusions: ARIA-E at baseline, more than four cerebral microhemorrhages, more than one area of superficial siderosis, any intracerebral hemorrhage >1 cm, or severe white matter disease on MRI. (Full criteria previously reported [2].)
- **Treatment course completion criteria**: Amyloid plaque level <11 CL on any single PET scan, or <25 CL on two consecutive PET scans — triggers a blinded switch from donanemab to placebo infusions (saline), assessed at weeks 24, 52, 76 (placebo-controlled period) and 102, 130 (LTE).
- **Ethics**: All procedures complied with relevant laws and institutional guidelines and were approved by appropriate institutional committees; all participants and study partners provided written informed consent.

## LTE structure and groups
- **Eligibility for LTE**: Participants completing the 76-week placebo-controlled period could enter the 78-week, participant- and investigator-blinded LTE with no additional eligibility criteria.
- **Early-start group**: Randomized to donanemab in the placebo-controlled period (N=860); 550 (64.0%) received ≥1 LTE infusion. Of these, 393 were switched to placebo (having met completion criteria at 24/52/76 weeks) and 157 continued donanemab in the LTE (continuing until meeting completion criteria at 102 or 130 weeks, or through 154 weeks).
- **Delayed-start group**: Randomized to placebo in the placebo-controlled period (N=876); 657 (75.0%) entered the LTE and started donanemab at LTE entry (following the same dose-titration schedule as placebo-controlled-period donanemab recipients), with a possible blinded switch to placebo at 102 or 130 weeks upon meeting completion criteria.
- **Completion rates**: Among early-start participants dosed in the LTE, 74.3% of placebo-switchers and 81.5% of donanemab-continuers completed the LTE; among delayed-start participants, 72.3% completed the LTE.
- **Total observation window**: 154 weeks (~3 years) from original randomization.

## External ADNI control cohort (LTE efficacy comparator)
- **Rationale**: The LTE has no internal placebo control, so CDR-SB efficacy is compared against an external cohort from the Alzheimer's Disease Neuroimaging Initiative (ADNI) database — an amyloid-targeting-therapy-naïve AD population.
- **ADNI eligibility for matching**: Cognitive impairment plus CSF total-tau/amyloid-β42 ratio >0.28 (established amyloid-pathology criterion [4]).
- **Matching pool**: Of 2430 ADNI participants evaluated, 534 met eligibility criteria and were included in propensity weighting.
- **Effective sample size (ESS) after weighting**: 268 for the early-start comparison; 301 for the delayed-start comparison.
- **Weighting method**: Propensity score weights estimated with the average-treatment-effect-among-the-treated (ATT) estimand, inverse probability weighting (IPW) from a generalized linear model, via the WeightIt R package. Covariates: age, sex, APOE ε4 status (non-carrier/heterozygous/homozygous), CDR-SB score, ADAS-Cog13 score, screening MMSE score. Baseline amyloid CL was not used as a covariate (missing for 43% of the ADNI-derived population).
- **Weight diagnostics**: Covariate balance checked (standardized mean difference <0.10 per covariate); extreme weights trimmed at the 95th percentile to limit impact on effective sample size.
- **Validation**: A supporting MMRM compared the weighted ADNI cohort's progression to the TRAILBLAZER-ALZ 2 internal placebo arm through 76 weeks, to assess whether the weighted ADNI cohort's trajectory was an appropriate proxy (closely aligned per the paper's Fig. S5, not included in the provided PDF).

## Outcomes measured
- **Efficacy**: CDR-SB (Clinical Dementia Rating Scale–Sum of Boxes, 0–18, higher=worse) least-squares mean change from baseline, compared to the weighted ADNI cohort. CDR-G (CDR–Global, 0–3, higher=worse) used to define disease-stage progression events for the early- vs delayed-start hazard comparison.
- **Biomarkers**: Amyloid plaque (Centiloids) reduction and clearance (<24.1 CL) at weeks 24/52/76 post-donanemab-initiation and beyond; amyloid reaccumulation after treatment course completion.
- **Safety**: AE reporting (deaths, SAEs, TEAEs, discontinuations) and centrally read MRI scans for ARIA-E/ARIA-H, by treatment-sequence group.

## Statistical approach (see also `statistical_methods` concepts in `logic/concepts.md`)
- Three MMRM analyses of CDR-SB change from baseline using ADNI weights: (1) validation of the weighted ADNI cohort vs the internal placebo arm through 76 weeks; (2)/(3) early-start/delayed-start donanemab arm vs the corresponding weighted ADNI cohort through 154 weeks.
- AUC (area-under-curve, trapezoidal-rule-weighted) analysis of early-start vs ADNI cumulative CDR-SB benefit.
- Time-saved analysis by back-calculating the ADNI-cohort timepoint matching the treated group's mean CDR-SB change.
- Cox proportional hazards model (stratified by pooled investigator and baseline tau level; covariates age, CDR-G score, AChEI/memantine use) for early- vs delayed-start CDR-G progression risk.
- MMRM for amyloid CL change from baseline (treatment, visit, treatment-by-visit interaction; covariates score, score-by-visit, age, tau category); clearance defined as <24.1 CL.
- Cross-study exposure-response model (updating a prior model built from a phase 1b study, TRAILBLAZER-ALZ, and TRAILBLAZER-EXT) for the amyloid reaccumulation rate.
- Descriptive safety tabulation by treatment-sequence group; time-to-first-ARIA-E and 6-month-interval post-discontinuation ARIA incidence; observation-time-adjusted incidence rate (OAIR) for cross-period comparison.
- All analyses exploratory, not controlled for multiplicity.

## Data provenance and software
- Trial registration: ClinicalTrials.gov identifier NCT04437511.
- External control: ADNI database (adni.loni.usc.edu), funded by the National Institute on Aging (NIH Grant U19AG024904), grantee organization the Northern California Institute for Research and Education.
- Propensity weighting performed with the WeightIt R package (inverse probability weighting, generalized linear model); no explicit R or package version stated in the paper. No SAS version, data-availability/IPD-sharing statement, or code-availability statement is present in this paper's main text (contrast with the related post-hoc analysis by Jessen et al., which does state SAS 9.4/R 4.3.0 and a Vivli data-access statement for the same underlying trial dataset).
