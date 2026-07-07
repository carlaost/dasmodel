# Study Design: Four-Step Estimation Pipeline

This is the "method" of the work: how validated, harmonized prevalence estimates of MCI and dementia
were produced for all 28 SHARE units from a 5-country validation subsample. (Mirrors §Methods.)

## Overview of the four steps (paper's own framing, p.2 Methods)
> "We proceeded in four steps detailed below. (a) We drew a validation subsample (N=2,678) of the
> most recent SHARE wave and administered the neuropsychological battery of SHARE-HCAP in this
> validation sample. (b) Based on these results, we classified individuals as normal, MCI or
> demented. (c) We related this classification to those cognition measures that are available in
> both the SHARE-parent sample and the SHARE-HCAP validation subsample. (d) Using this relation, we
> predicted for each individual in the analytical SHARE parent sample (N=47,193) the probabilities
> of cognitive status normal, MCI and demented."

(Note: this text states N=2,678 for the validation subsample, while Table 1/Table 2/Results text
state N=2,687 — see `logic/solution/constraints.md` for the discrepancy note.)

## Step (a): Validation subsample sampling design
- **Country selection**: Five countries chosen to represent East (Czech Republic), West (France,
  Germany), North (Denmark), and South (Italy) of Europe.
- **Sampling frame**: A weighted subsample of individuals aged 65+ drawn from the SHARE parent study
  in these five countries.
- **Oversampling rule**: Based on performance in a word-recall test in the SHARE parent study,
  heavily oversampling those with low test scores "to ensure an adequate number of individuals who
  are at a high risk of MCI or dementia."
- **Recruitment funnel**: 3,546 eligible individuals → 2,687 participants → 75.8% overall response
  rate (Table 1).
- **Timing**: Data collected May–November 2022, on average about five months after the SHARE parent
  Wave 9 data collection.
- **Instrument**: SHARE-HCAP neuropsychological battery — 27 cognitive indicators (Supplementary
  Table S3) spanning five domains: memory, executive functioning, visuospatial skills, language and
  fluency, orientation (domain selection based on prior theoretical/empirical work, ref 22) — plus
  an informant's report from a family member or friend.
- **Missing data handling**: Item nonresponse was below 2.3% except for story recall/recognition
  (21.9%), HRS Number Series (15.4%), and TMT part B (12.6%), all concentrated in Italy. Addressed
  via Full Information Maximum Likelihood (FIML) estimation in the factor analysis (ref 23),
  "ensuring that incomplete cases contribute to the estimation process proportionally to their
  available information."

## Step (b): Classification into normal / MCI / demented
Detailed in `logic/solution/classification_method.md` (Manly et al. 2022 decision rule).

## Step (c): Relating HCAP classification to shared SHARE-parent cognition items
- **Method**: Regression-based approach developed by Hurd et al. (2013) for estimating US dementia
  costs, adapted "to our multi-country setting."
- **Shared variables used**: Cognitive — orientation in time, immediate and delayed word recall,
  serial 7s, animal naming (Supplementary Table S4). Health — sum of Activities of Daily Living
  (ADL) + Instrumental Activities of Daily Living (IADL).
- **Effect**: "This approach effectively weighs the cognition items of the SHARE parent study by
  their weights in the SHARE-HCAP sample."
- **Internal validation**: Applying the fitted regression back onto the validation subsample itself
  and comparing predicted vs. directly classified normal/MCI/demented percentages (Table 2) —
  "the prediction by our regression model replicates the classification results from Step (b) very
  well" (see `logic/claims.md` C06).
- Full technical detail relegated to Supplementary Section S2 / Table S5 (not available from
  provided input — see `evidence/README.md`).

## Step (d): Predicting cognitive-status probabilities for the full SHARE parent sample
- **Three respondent groups distinguished** (SHARE parent Wave 9, N=47,733 per Table 1 header /
  N=47,193 analytical sample per Table 3):
  1. **95.7%** completed the cognition items directly → probabilities of normal/MCI/demented
     predicted via the Step (c) regression equation, using the same demographic/cognition/health
     variables as the validation subsample.
  2. **3.1%** had health information obtained via informant proxy (unable to complete cognition
     items themselves) → classified via a separate, simpler informant-based rule (see below).
  3. **1.2%** excluded from the analytical sample due to missing data.
- **Probabilistic (not hard) classification**: "We recognize the uncertainty in classification by
  predicting probabilities rather than a cognitive class." Country-specific prevalence rates of
  normal/MCI/demented are calculated as country-specific *average predicted probabilities*, not as
  counts of hard-classified individuals.
- **Informant-based rule for the 3.1% proxy group** (Supplementary Section S3 / Table S6 — not
  available from provided input): "If the respondent's memory function was assessed poor (fair), the
  respondent was classified as demented (MCI), else normal."
- **Aggregation**: Country-level prevalence = average of individual predicted probabilities within
  each of the 28 SHARE units; 28-unit pooled average computed by further aggregating across units.

## Comparison methodology: original Langa-Weir (LW) scale (Table 3)
- **Score construction**: Immediate + delayed word recall (0–20) + serial 7s (0–5) + backwards
  counting (0–2).
- **Cutoffs**: Demented = 0–6; Normal = 12–27; the 7–11 range is termed "CIND" (cognitively impaired
  but not demented) by Langa-Weir, compared conceptually (not identically) to this paper's MCI
  category.
- **External validation basis**: The original LW scale "has been validated against diagnostic
  information from the ADAMS study" (US Aging, Demographics, and Memory Study, ref 30) — a different
  (US-based) validation target than this paper's own HCAP-based validation.
- **Variant note**: This paper's LW variant differs from the LW variant used in an earlier SHARE-based
  study (Klee et al. 2024, ref 10/13) because backwards counting was not available in the 2017 SHARE
  data used by that earlier study.

## Counterfactual simulation methodology (Figure 2, education-standardization)
- Recompute each individual's predicted probability of being demented (Step d's regression equation)
  substituting the 28-unit-average childhood-education level for the individual's actual education
  level, holding all other covariates (age, sex, cognition/health items) at their actual values.
  Aggregate to country level exactly as in Step (d) and compare to the actual (non-counterfactual)
  distribution.

## Statistical software
- Stata (version 14.2) and Mplus (version 8.10) — "All statistical analyses were conducted with
  Stata (version 14.2) and Mplus (version 8.10)" (p.4, Methods). No analysis code is released with
  the paper (see `src/environment.md`).

## Ethics
- Written informed consent obtained from all individuals.
- SHARE and SHARE-HCAP protocols approved by the Ethics Committee of the Max Planck Institute in
  Germany.
- Performed in accordance with the Declaration of Helsinki.
