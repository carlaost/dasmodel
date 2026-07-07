# Concepts

## SHARE (Survey of Health, Ageing and Retirement in Europe)
- **Notation**: —
- **Definition**: A longitudinal population-aging study, started in 2004, representative of the 50+ population in 27 European countries and Israel (28 units total). A key feature is strict ex-ante harmonization of instruments and protocols across countries, including identical cognition measures, making it a resource for cross-national comparisons of health and socioeconomic status.
- **Boundary conditions**: Covers individuals with regular residence in the respective SHARE country, not incarcerated/hospitalized/out of the country during the survey period, able to speak the country's language(s); follows individuals into nursing homes; current partners in the household are interviewed regardless of age.
- **Related concepts**: SHARE-HCAP, SHARE parent Wave 9, ISCED.

## SHARE Wave 9 (parent study)
- **Notation**: N as stated in the source (see discrepancy note in `logic/solution/constraints.md`: Abstract states 47,773; Methods text and Table 1 header state 47,733; the analytical sample used for prevalence estimation is N=47,193).
- **Definition**: The most recent available wave of the SHARE parent study at the time of writing, collected October 2021–September 2022, comprising individuals aged 65 and older across 28 SHARE units.
- **Boundary conditions**: Distinguishes three respondent groups for cognitive-status assessment: those completing cognition items directly (95.7%), those assessed via informant proxy report (3.1%), and those excluded due to missing data (1.2%).
- **Related concepts**: SHARE, SHARE-HCAP, FIML.

## SHARE-HCAP
- **Notation**: —
- **Definition**: The European arm of the international Harmonized Cognitive Assessment Protocol (HCAP) network of aging studies, developed by the US Health and Retirement Study (HRS) as part of an NIA-funded international collaboration to harmonize cognition measurement globally. SHARE-HCAP administers an in-depth neuropsychological battery (27 cognitive indicators across five domains: memory, executive functioning, visuospatial skills, language and fluency, orientation) plus an informant report, to a validation subsample drawn from five SHARE countries (Czech Republic, France, Germany, Denmark, Italy).
- **Boundary conditions**: Data collected May–November 2022, on average about five months after the SHARE parent Wave 9 data collection; validation subsample of N=2,687 (Table 1, Results text) — though the Methods introduction separately states N=2,678 (see discrepancy note).
- **Related concepts**: HCAP, SHARE, Manly et al. classification, Hurd et al. regression approach.

## HCAP (Harmonized Cognitive Assessment Protocol)
- **Notation**: —
- **Definition**: An internationally harmonized cognitive-assessment protocol originating from the US Health and Retirement Study, used across a global network of aging studies to standardize the measurement of cognition and enable cross-study/cross-national comparability and validation of dementia/MCI classification.
- **Boundary conditions**: This paper uses HCAP specifically as a "validation tool" for the 2022 SHARE wave (i.e., not as the primary data source for the full sample, but as the ground truth against which a regression-based extension is validated).
- **Related concepts**: SHARE-HCAP, Manly et al. classification, cross-HCAP comparisons (e.g., LASI-DAD in India, rural South Africa).

## Manly et al. (2022) classification algorithm
- **Notation**: —
- **Definition**: A classification rule assigning respondents to normal / MCI / demented categories based on factor-score estimates across five cognition domains and an informant report of functional impairment. An individual is classified as demented if factor scores in at least two cognitive domains are ≥1.5 SD below the mean of a normative sample AND functional impairment is reported by an informant. MCI is assigned if only one domain is below threshold with an informant report of functional impairment, or at least one domain below threshold without an informant report, or one domain below threshold with a self-report of memory concerns (no informant report). Normal is assigned if no domain meets the impairment criteria, or if one domain is below threshold but neither self- nor informant-report indicates concern.
- **Boundary conditions**: Relies on diagnostic criteria from the National Institute on Aging and Alzheimer's Association (NIA-AA); the paper explicitly assumes these US-derived thresholds apply equally across all SHARE countries, absent a European "gold standard" calibration target (see `logic/solution/constraints.md`).
- **Related concepts**: SHARE-HCAP, HCAP, factor score / normative sample threshold, Hurd et al. regression approach.

## Hurd et al. (2013) regression-based approach
- **Notation**: —
- **Definition**: A regression-based method (originally developed to estimate the monetary costs of dementia in the US) adapted here to a multi-country setting to relate the SHARE-HCAP classification outcome (normal/MCI/demented) to a set of demographic, cognitive, and health variables shared between the SHARE-HCAP validation subsample and the SHARE parent study, in order to predict cognitive-status probabilities for individuals who only have SHARE-parent data (no direct HCAP classification).
- **Boundary conditions**: Uses shared variables limited to orientation in time, immediate and delayed word recall, serial 7s, animal naming (cognitive), and the sum of ADL+IADL (health); full details in Supplementary Section S2 / Table S5 (not available from provided input).
- **Related concepts**: SHARE-HCAP, Manly et al. classification, MCI, dementia.

## MCI (Mild Cognitive Impairment)
- **Notation**: —
- **Definition**: An intermediate cognitive-health category between normal cognition and dementia, sometimes referred to as CIND (cognitively impaired not demented); individuals with MCI are at increased risk of progressing to dementia with age.
- **Boundary conditions**: Classified per the Manly et al. rule (one cognitive domain below threshold, with varying informant/self-report conditions — see that concept entry); conceptually overlaps with, but is not identical to, the Langa-Weir scale's "CIND" category.
- **Related concepts**: Langa-Weir scale, dementia, Manly et al. classification.

## Dementia (as operationalized in this paper)
- **Notation**: —
- **Definition**: The most severe cognitive-status category, classified per the Manly et al. rule (factor scores ≥1.5 SD below the normative mean in at least two cognitive domains, plus informant-reported functional impairment), or, under the Langa-Weir comparison scale, a summary score of 0–6.
- **Boundary conditions**: Prevalence is calculated as the country-specific average of predicted individual probabilities of being demented, not as a hard individual-level classification, in the SHARE parent sample (Step (d) of the Methods).
- **Related concepts**: MCI, Manly et al. classification, Langa-Weir scale, coefficient of variation.

## Langa-Weir (LW) scale
- **Notation**: score range 0–27, composed of immediate + delayed word recall (0–20), serial 7s (0–5), and backwards counting (0–2)
- **Definition**: A cognition-summary scoring scale (Crimmins et al. 2011) used to classify individuals as demented (score 0–6), normal (score 12–27), or "CIND" — cognitively impaired but not demented (score 7–11). Validated against diagnostic information from the US ADAMS study. Used in this paper as a comparison scale against the HCAP-validated approach.
- **Boundary conditions**: The LW variant used in this paper differs from the LW variant used in an earlier SHARE-based study (Klee et al. 2024, ref. 10) because backwards counting was not available in the 2017 SHARE data used by that earlier study.
- **Related concepts**: ADAMS study, MCI, dementia, coefficient of variation.

## ISCED (International Standard Classification of Education, 1997)
- **Notation**: —
- **Definition**: A UNESCO-developed internationally harmonized classification of educational attainment, used in SHARE to assess respondents' educational achievement when they were young.
- **Boundary conditions**: Categories used in this paper: primary school or less, some high school, high school or some college, college degree or more.
- **Related concepts**: education-cognition association, counterfactual education-standardization (Figure 2).

## FIML (Full Information Maximum Likelihood) estimation
- **Notation**: —
- **Definition**: A statistical estimation method used in factor analysis to handle item nonresponse, allowing incomplete cases to contribute to estimation proportionally to their available information, producing unbiased parameter estimates and standard errors (Enders & Bandalos 2001).
- **Boundary conditions**: Applied specifically to address item nonresponse on cognitive measures in the SHARE-HCAP sample, where nonresponse was below 2.3% except for three measures (story recall/recognition 21.9%, HRS Number Series 15.4%, TMT part B 12.6%), all concentrated in Italy.
- **Related concepts**: SHARE-HCAP, item nonresponse.

## EURO-D scale
- **Notation**: score threshold ">4" used in this paper
- **Definition**: A depression-symptom scale developed as a European Union initiative to compare symptoms of depression across 14 European centers (Prince et al. 1999), used in this paper as a comorbidity measure in the multivariate regression of dementia probability.
- **Boundary conditions**: A EURO-D value exceeding 4 is associated with a 4.0-percentage-point increase in probability of being demented, conditional on age, sex and education (Figure 1).
- **Related concepts**: comorbidity regression (Figure 1), face validity.

## Coefficient of variation (as used in this paper)
- **Notation**: variance of the estimated effect scaled by the average effect size
- **Definition**: A dispersion measure used to compare the relative cross-national variability of dementia prevalence estimates between the HCAP-validated and Langa-Weir scales, independent of differences in their average level.
- **Boundary conditions**: Reported only for the Demented,% column in Table 3 (0.46 HCAP-validated vs. 0.80 Langa-Weir); not reported for MCI,%.
- **Related concepts**: Langa-Weir scale, Table 3, cross-national variation.
