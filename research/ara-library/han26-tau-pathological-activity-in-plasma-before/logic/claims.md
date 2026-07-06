# Claims

All numbers are copied exactly from the paper (Hanseeuw, Quenon et al., "Tau pathological activity in plasma before the onset of symptomatic Alzheimer's disease," medRxiv, 2026; DOI 10.64898/2026.04.03.26350110). Page references are to the supplied 48-page preprint PDF. All reported statistics carry the `[result]` tag (this is an observational/analytical study, not a code run) and are grounded to a verbatim quote from the cited page/table/figure.

## C01: High overall diagnostic accuracy for tau-PET positivity
- **Statement**: In the entire sample (n=145), VeraBIND Tau achieved 94.2% sensitivity (95% CI 85.8–98.4), 96.1% specificity (95% CI 88.9–99.2), and 95.2% accuracy (95% CI 90.3–98.0) for predicting tau-PET positivity (Braak-like tau-PET stage>0), with AUC=0.974.
- **Status**: supported
- **Falsification criteria**: An independent validation cohort using the same assay and tau-PET reference standard yielding materially lower sensitivity, specificity, or AUC would refute this claim.
- **Proof**: [E02, E03]
- **Evidence basis**: Table 3 (entire-sample row) and Figure 2A ROC curve.
- **Interpretation**: This is a high-level accuracy figure computed over the whole sample; it does not by itself establish performance in the clinically hardest subgroup (CU individuals) or at the earliest pathology stages — see C03 and C04.
- **Sources**:
  - 94.2% sensitivity, 96.1% specificity ← Abstract, PDF p.3 «VeraBIND Tau demonstrated 94.2% sensitivity and 96.1% specificity for predicting tau-PET positivity (AUC=0.97).» [result]
  - Accuracy 95.2%, 95% CI 90.3–98.0 ← Table 3, PDF p.42 «Entire sample (n=145) ... Accuracy 95.2% 90.3 – 98.0» [result]
  - AUC=0.974 ← Figure 2A legend, PDF p.44 «VeraBIND Tau: AUC = 0.974» [result]
- **Dependencies**: none
- **Tags**: diagnostic-accuracy, tau-PET, ROC

## C02: VeraBIND Tau outperforms other plasma biomarkers for tau-PET positivity; pTau217 remains superior for amyloid positivity
- **Statement**: DeLong tests showed VeraBIND Tau (AUC=0.974) better predicted tau-PET positivity than plasma pTau217 (AUC=0.924; z=1.96, p=0.049), pTau181 (AUC=0.84), pTau231 (AUC=0.753), and the Aβ42/Aβ40 ratio (AUC=0.768) (each of the latter three: z>3.68, p<0.001 vs. VeraBIND Tau). For predicting amyloid status, plasma pTau217 had the highest AUC (0.932, vs. VeraBIND Tau 0.866; DeLong z=1.89, p=0.058).
- **Status**: supported
- **Falsification criteria**: A head-to-head re-analysis in an independent cohort showing pTau217 (or another biomarker) with an equal or higher AUC than VeraBIND Tau for tau-PET positivity, at conventional significance, would refute the tau-PET-superiority portion of this claim.
- **Proof**: [E02]
- **Evidence basis**: Figure 2 (panels A and B) ROC curves with printed AUC values; Results text with DeLong test statistics.
- **Interpretation**: VeraBIND Tau's advantage is specific to tau pathology detection; pTau217 remains the better plasma correlate of amyloid pathology — motivating a complementary two-test (Core 1 + Core 2) rather than a replacement framing (see Discussion, PDF p.24–25).
- **Sources**:
  - VeraBIND Tau AUC=0.974 (panel A) ← Figure 2A legend, PDF p.44 «VeraBIND Tau: AUC = 0.974» [result]
  - pTau217 AUC=0.924 (panel A), z=1.96, p=0.049 ← Results, PDF p.19 «the largest AUC was found for VeraBIND Tau (AUC=0.97), followed by pTau217 plasma concentration (AUC=0.92). DeLong Tests indicated that VeraBIND Tau better predicted tau-PET positivity compared to all the other blood-based biomarkers (VeraBIND Tau vs. pTau217: z=1.96, p=0.049...)» [result]
  - pTau181/pTau231/Aβ42-Aβ40 vs VeraBIND: all z>3.68, p<0.001 ← Results, PDF p.19 «VeraBIND Tau vs. pTau181 [missing data=3], pTau231 [missing data=27] or Aβ42/Ab40 [missing data=6]: all z's>3.68, p<0.001» [result]
  - pTau217 AUC=0.932 (panel B, amyloid), z=1.89 vs VeraBIND, p=0.058 ← Results, PDF p.19 «the highest AUC (AUC=0.93) for predicting the Aβ status was found for plasma pTau217 (Fig. 2.B; DeLong Tests: pTau217 vs. VeraBIND Tau: z=1.89, p=0.058...)» [result]
  - Panel A AUCs 0.974/0.924/0.84/0.753/0.768 ← Figure 2A legend, PDF p.44 [result]
  - Panel B AUCs 0.866/0.932/0.813/0.757/0.82 ← Figure 2B legend, PDF p.44 [result]
- **Dependencies**: none
- **Tags**: ROC, DeLong-test, comparative-biomarkers, amyloid-vs-tau

## C03: Substantially higher positive predictive value than pTau217 in CU individuals
- **Statement**: In CU individuals (n=79), VeraBIND Tau achieved PPV=85.9% (95% CI 46.3–97.7) for tau-PET positivity, regardless of the pTau217 threshold compared against — the best pTau217 threshold (0.256 pg/mL) achieved only PPV=57.5% (95% CI 29.5–81.4), with the 0.142 and 0.193 pg/mL thresholds achieving PPV=33.6% and 51.3% respectively.
- **Status**: supported
- **Falsification criteria**: An independent CU cohort in which the best pTau217 threshold matches or exceeds VeraBIND Tau's PPV for tau-PET positivity would refute this claim.
- **Proof**: [E03]
- **Evidence basis**: Table 3 (CU individuals block, PPV row).
- **Interpretation**: Because PPV depends on the low tau-PET prevalence assumed for CU individuals (10%; see A3 in `problem.md`), this is the metric most relevant to real-world population screening, where most CU individuals tested will be tau-PET negative.
- **Sources**:
  - VeraBIND Tau PPV=85.9% (CU) ← Abstract, PDF p.3 «It outperformed plasma pTau217 in CU individuals (PPV=85.9%), regardless of the pTau217 threshold used (maximal PPV of 57.5% using the 0.256pg/mL pTau217 threshold).» [result]; Table 3, PDF p.42 «CU individuals (n=79) ... PPV‡ 85.9% 46.3 – 97.7» [result]
  - pTau217 PPV 33.6% / 51.3% / 57.5% at 0.142/0.193/0.256 pg/mL ← Table 3, PDF p.42 «PPV‡ ... 33.6% 22.8 – 46.4 ... 51.3% 30.4 – 71.8 ... 57.5% 29.5 – 81.4» [result]
- **Dependencies**: C01
- **Tags**: PPV, CU, population-screening

## C04: Superior detection of early (low Braak-like) tau pathology stages
- **Statement**: For distinguishing Braak-like 1–3 from Braak-like 0 individuals, VeraBIND Tau achieved AUC=0.96 versus AUC=0.74 for plasma pTau217 (DeLong z=2.99, p=0.003). In Braak-like 1–3 individuals (group n=17), VeraBIND Tau sensitivity was 88.2% (n=15/17), compared to 64.7% (n=11/17), 41.2%, and 23.5% (n=4/17) for pTau217 at the 0.142, 0.193, and 0.256 pg/mL thresholds respectively — the 41.2% figure is printed in the source as "n=7/11", which is internally inconsistent (7/17=41.2% is arithmetically correct for this group of 17; 7/11=63.6% is not), so the denominator is reproduced here as printed but flagged rather than silently corrected (see Sources below); McNemar tests showed VeraBIND Tau sensitivity was significantly higher than pTau217 at the 0.193 (χ²=4.90, p=0.03) and 0.256 (χ²=7.69, p=0.006) thresholds, with no significant difference at the 0.142 threshold (χ²=1.1, p=0.29) — though at that threshold pTau217 was also positive in 28.9% (22/76) of Braak-like 0 (T-negative) individuals, versus only 3.9% (3/76) for VeraBIND Tau.
- **Status**: supported
- **Falsification criteria**: An independent cohort showing no AUC/sensitivity advantage of VeraBIND Tau over pTau217 specifically in Braak-like 1–3 individuals would refute this claim.
- **Proof**: [E04]
- **Evidence basis**: Figure 3A–B (score distributions and positivity tables by Braak-like stage group).
- **Interpretation**: The paper attributes VeraBIND Tau's overall diagnostic edge (C01–C03) specifically to this early-stage detection advantage — described in the paper's own section heading as "VeraBIND Tau outperforms plasma pTau217 to detect low tau pathology stages."
- **Sources**:
  - AUC 0.96 vs 0.74, z=2.99, p=0.003 ← Results, PDF p.20 «The AUC for detecting tau-PET signals in Braak-like 1-3 vs. Braak-like 0 individuals was higher for VeraBIND Tau (AUC=0.96) than for plasma pTau217 concentration (AUC=0.74, z=2.99, p=0.003).» [result]
  - Sensitivity 88.2% (n=15/17) vs 64.7%/41.2%/23.5% ← Results, PDF p.20 «VeraBIND Tau was positive in 88.2% (n=15/17) individuals, whereas pTau217 was positive in 64.7% (n=11/17), 41.2% (n=7/11), and 23.5% (n=4/17) individuals at the 0.142, 0.193, and 0.256 thresholds, respectively» [result] — NOTE: the source's printed "n=7/11" for the 41.2% figure is arithmetically inconsistent with a Braak-like 1-3 group of n=17 (7/17=41.2% checks out; 7/11=63.6% does not); reproduced verbatim rather than silently corrected to "7/17"
  - McNemar χ²=4.90 p=0.03 (0.193); χ²=7.69 p=0.006 (0.256); χ²=1.1 p=0.29 (0.142) ← Results, PDF p.20 «McNemar tests indicated that VeraBIND Tau sensitivity was higher than pTau217 sensitivity at the 0.193 (c2=4.90, p=0.03) and 0.256 cutoffs (c2=7.69, p=0.006). At the 0.142 threshold, the sensitivity did not differ between VeraBIND Tau and pTau217 (c2=1.1, p=0.29)» [result]
  - pTau217 false-positive 28.9% (22/76) vs VeraBIND 3.9% (3/76) at Braak 0 ← Results, PDF p.20 «pTau217 was also positive in 28.9% (n=22/76) Braak-like 0 participants (T-) against only 3.9% (n=3/76) for VeraBIND Tau» [result]
  - Fig 3A/B positivity tables, thresholds 0.142/0.193/0.256, Braak 1-3 column ← Figure 3, PDF p.45 «≥ 0.142 pg/mL 28.9% 64.7% 100% / ≥ 0.193 pg/mL 14.5% 41.2% 100% / ≥ 0.256 pg/mL 7.9% 23.5% 92.3%» and «≥ 1.0 3.9% 88.2% 96.2%» [result]
- **Dependencies**: C01
- **Tags**: early-stage-detection, Braak-staging, sensitivity, McNemar

## C05: Comparable performance at advanced tau-PET stages
- **Statement**: For distinguishing Braak-like 4–6 from Braak-like 0 individuals, VeraBIND Tau (96.2% sensitivity, n=50/52; AUC=0.98) and plasma pTau217 (100% sensitivity at the 0.142 and 0.193 pg/mL thresholds, n=52/52; 92.3% at 0.256 pg/mL, n=48/52; AUC=0.98) showed similar sensitivity and AUC (DeLong z=-0.43, p=0.66).
- **Status**: supported
- **Falsification criteria**: A significant DeLong-test difference between VeraBIND Tau and pTau217 AUC for Braak-like 4–6 vs. 0 discrimination in an independent cohort would refute this claim.
- **Proof**: [E04]
- **Evidence basis**: Figure 3A–B (Braak-like 4-6 column, positivity tables).
- **Interpretation**: Combined with C04, this indicates VeraBIND Tau's diagnostic edge over pTau217 is concentrated in early tau pathology; at advanced stages, the two assays converge.
- **Sources**:
  - VeraBIND Tau 96.2% sensitivity (n=50/52), AUC=0.98 ← Results, PDF p.20–21 «VeraBIND Tau (n=50/52, 96.2% sensitivity, AUC=0.98)» [result]
  - pTau217 100%/92.3% sensitivity, AUC=0.98, DeLong z=-0.43, p=0.66 ← Results, PDF p.21 «pTau217 (0.142 and 0.193 thresholds: n=52/52, 100% sensitivity; 0.256 threshold: n=48/52, 92.3% sensitivity; AUC=0.98) had similar sensitivity and AUC (z=-0.43, p=0.66) to distinguish individuals with Braak-like 4-6 from Braak-like 0 participants.» [result]
- **Dependencies**: C04
- **Tags**: advanced-stage, ceiling-effect

## C06: VeraBIND Tau score plateaus early rather than tracking Braak-stage severity, unlike pTau217
- **Statement**: In an age/sex/education-adjusted, Bonferroni-corrected regression model, VeraBIND Tau score was similarly elevated in Braak-like 1–3 (Mean=1.10, SE=0.05; b=0.24 vs. Braak 0, 95% CI [0.11–0.36], p<0.001) and Braak-like 4–6 (Mean=1.16, SE=0.03; b=0.29, 95% CI [0.20–0.37], p<0.001) groups relative to Braak-like 0 (Mean=0.87, SE=0.02), with no significant difference between the 1–3 and 4–6 groups (b=-0.05, 95% CI [-0.07–0.18], p=0.98). In contrast, plasma pTau217 concentration rose specifically at Braak-like 4–6 (Mean=0.71, SE=0.04) relative to both Braak-like 0 (Mean=0.134, SE=0.04; b=0.58, 95% CI [0.44–0.72], p<0.001) and Braak-like 1–3 (Mean=0.320, SE=0.08; b=0.40, 95% CI [0.18–0.61], p<0.001), which did not differ from each other (b=0.19, 95% CI [-0.02–0.40], p=0.10).
- **Status**: supported
- **Falsification criteria**: An independent cohort showing a significant VeraBIND Tau dose-response difference between Braak-like 1–3 and 4–6 groups (matching pTau217's pattern) would refute this claim.
- **Proof**: [E04]
- **Evidence basis**: Figure 3A–B (boxplots by Braak-like stage group with significance brackets).
- **Interpretation**: VeraBIND Tau appears to behave as a binary/early "presence-of-pathological-seeding" signal rather than a graded severity marker, while pTau217 concentration tracks disease burden more continuously but only once pathology is advanced.
- **Sources**:
  - VeraBIND Tau Braak 0/1-3/4-6 means and regression coefficients ← Results, PDF p.20 «the VeraBIND Tau Score was elevated in both Braak-like 1-3 (Mean=1.10, SE=0.05, b=0.24, 95% CI [0.11-0.36], p<0.001) and Braak-like 4-6 groups (Mean=1.16, SE=0.03, b=0.29, 95% CI [0.20-0.37], p<0.001), compared to Braak-like 0 individuals (Mean=0.87, SE=0.02), while Braak-like 1-3 and Braak-like 4-6 groups did not differ (b=-0.05, 95% CI [-0.07-0.18], p=0.98).» [result]
  - pTau217 Braak 0/1-3/4-6 means and regression coefficients ← Results, PDF p.20 «plasma pTau217 was increased in the Braak-like 4-6 group (Mean=0.71, SE=0.04), compared to both Braak-like 0 (Mean=0.134, SE=0.04, b=0.58, 95% CI [0.44-0.72], p<0.001) and 1-3 groups (Mean=0.320, SE=0.08, b=0.40, 95% CI [0.18-0.61], p<0.001), which did not differ (b=0.19, 95% CI [-0.02-0.40], p=0.10).» [result]
  - Significance brackets (****, **, ns) ← Figure 3A-B, PDF p.45 [result]
- **Dependencies**: C04, C05
- **Tags**: dose-response, regression, biomarker-kinetics

## C07: VeraBIND Tau, not pTau217, predicts continuous entorhinal tau-PET signal at early stages
- **Statement**: In a regression model limited to 93 individuals with Braak-like stage 0–3 and adjusted for age, sex, and education, VeraBIND Tau significantly predicted entorhinal tau-PET SUVr (β=1.69, 95% CI [1.27–2.10], p<0.001), whereas plasma pTau217 concentration did not (β=0.31, 95% CI [-0.06–0.68], p=0.10).
- **Status**: supported
- **Falsification criteria**: An independent cohort restricted to Braak-like 0–3 individuals in which pTau217 significantly predicts continuous entorhinal tau-PET SUVr at a comparable effect size to VeraBIND Tau would refute this claim.
- **Proof**: [E05]
- **Evidence basis**: Results text regression coefficients (no dedicated figure/table beyond the Results narrative).
- **Interpretation**: This is the paper's clearest single result supporting a specific early/entorhinal-stage advantage for VeraBIND Tau as a continuous (not just binary) measure.
- **Sources**:
  - β=1.69 [1.27–2.10] p<0.001 (VeraBIND); β=0.31 [-0.06–0.68] p=0.10 (pTau217) ← Results, PDF p.21 «VeraBIND Tau demonstrated a significant association with entorhinal tau-PET signal (β=1.69, 95% CI [1.27-2.10], p<0.001), whereas plasma pTau217 concentration did not (β=0.31, 95% CI [-0.06-0.68], p=0.10).» [result]
- **Dependencies**: C04
- **Tags**: continuous-outcome, entorhinal, early-detection, regression

## C08: VeraBIND Tau cross-sectional score correlates with cognition and tau-PET burden, including in CU individuals alone
- **Statement**: Across the entire sample, age-adjusted Spearman correlations between VeraBIND Tau score and MMSE (rs=-0.42), episodic memory z-score (rs=-0.53), entorhinal tau-PET SUVr (rs=0.71), inferior-temporal tau-PET SUVr (rs=0.62), plasma pTau217 (rs=0.60), and plasma pTau181 (rs=0.44) were all significant (p<0.001). Restricted to the 79 CU participants, VeraBIND Tau remained significantly associated with entorhinal tau-PET SUVr (rs=0.52, p<0.0001), inferior-temporal SUVr (rs=0.43, p<0.0001), pTau217 (rs=0.42, p=0.0001), and pTau181 (rs=0.39, p=0.0005), but not with MMSE (rs=0.10, p=0.38), and only marginally with episodic memory (rs=-0.20, p=0.08) and plasma pTau231 (rs=0.23, p=0.054, n=70/79).
- **Status**: supported
- **Falsification criteria**: A replication cohort finding no significant CU-restricted correlation between VeraBIND Tau and entorhinal tau-PET SUVr would refute the CU-specific portion of this claim.
- **Proof**: [E06]
- **Evidence basis**: Figure 4 (panels A–F, age-adjusted Spearman rho values printed on each panel).
- **Interpretation**: The whole-sample correlations are partly driven by the wide clinical spectrum (CU to dementia); the CU-restricted results indicate the association with tau-PET/plasma pTau markers is not merely an artifact of clinical group differences, though the (low-variance) MMSE association is CU-specific noise, consistent with a ceiling effect on standard cognitive tests in unimpaired adults.
- **Sources**:
  - rs=-0.42 (MMSE), rs=-0.53 (episodic memory), rs=0.71 (entorhinal SUVr), rs=0.62 (inf. temporal SUVr), rs=0.60 (pTau217), rs=0.44 (pTau181) ← Figure 4 panel labels, PDF p.47 «Age-adjusted rs=-0.42, p<0.001 / Age-adjusted rs=-0.53, p<0.001 / Age-adjusted rs=0.71, p<0.001 / Age-adjusted rs=0.62, p<0.001 / Age-adjusted rs=0.60, p<0.001 / Age-adjusted rs=0.44, p<0.001» [result]
  - CU-restricted rs=0.52/0.43/0.42/0.39 and non-significant MMSE/episodic memory/pTau231 ← Results, PDF p.21–22 «high VeraBIND Tau scores were still significantly associated with high entorhinal tau-PET signal (rs=0.52, p<0.0001), inferior temporal tau-PET signal (rs=0.43, p<0.0001), plasma pTau217 (rs=0.42, p=0.0001) and pTau181 (rs=0.39, p=0.0005) concentrations ... VeraBIND Tau scores were not associated with the MMSE scores (rs=0.10, p=0.38) and showed only marginal association with the episodic memory scores (rs=-0.20, p=0.08). A marginal association was also found with plasma concentration of pTau231 in CU individuals (available in 70/79 individuals, rs=0.23, p=0.054)» [result]
- **Dependencies**: none
- **Tags**: correlation, cognition, cross-sectional, CU-subgroup

## C09: VeraBIND Tau annual rate of change tracks disease-progression proxies
- **Statement**: In the 88-participant longitudinal subsample, the annual rate of change in VeraBIND Tau score correlated (age-adjusted Spearman) with cross-sectional entorhinal tau-PET SUVr (rs=0.23, p=0.03), Braak-like tau-PET stage (rs=0.29, p=0.006), MMSE (rs=-0.38, p=0.0003), episodic memory z-score (rs=-0.33, p=0.002), plasma pTau217 (rs=0.29, p=0.007), and plasma pTau181 (rs=0.30, p=0.005); the association with plasma pTau231 (n=84/88) was not significant (rs=0.08, p=0.48), and the association with inferior-temporal tau-PET SUVr was marginal (rs=0.21, p=0.054).
- **Status**: supported
- **Falsification criteria**: A replication longitudinal cohort in which the annual VeraBIND Tau rate of change shows no association with any cross-sectional disease-severity proxy would refute this claim.
- **Proof**: [E07]
- **Evidence basis**: Results text (no dedicated correlation figure; Figure 5 shows the underlying individual longitudinal trajectories by Braak-like group).
- **Interpretation**: The correlations, while modest in magnitude (|rs| 0.21–0.38), support the idea that VeraBIND Tau change over time is at least directionally informative of concurrent disease progression, though the paper explicitly frames longitudinal use for monitoring anti-tau therapy as requiring further study.
- **Sources**:
  - rs=0.23 p=0.03 (entorhinal SUVr); rs=0.29 p=0.006 (Braak stage); rs=-0.38 p=0.0003 (MMSE); rs=-0.33 p=0.002 (episodic memory); rs=0.29 p=0.007 (pTau217); rs=0.30 p=0.005 (pTau181) ← Results, PDF p.21–22 «The annual change in VeraBIND Tau Score correlated with cross-sectional entorhinal tau-PET SUVr (age-adjusted Spearman's rho=0.23, p=0.03), Braak-like tau-PET stages (rs=0.29, p=0.006), MMSE scores (rs=-0.38, p=0.0003), episodic memory z-score (rs=-0.33, p=0.002), plasma concentrations of pTau217 (rs=0.29, p=0.007), and pTau181 (rs=0.30, p=0.005)» [result]
  - pTau231 rs=0.08, p=0.48 (n=84/88); inferior temporal SUVr rs=0.21, p=0.054 ← Results, PDF p.22 «The association between the annual VeraBIND Tau change with pTau231 plasma concentration (available in 84/88 participants) was not significant (rs=0.08, p=0.48), while the association with the inferior temporal tau-PET SUVr was marginal (rs=0.21, p=0.054).» [result]
- **Dependencies**: C08
- **Tags**: longitudinal, rate-of-change, disease-progression

## C10: Good longitudinal test-retest stability of VeraBIND Tau positivity status
- **Statement**: Over a mean follow-up of 1.72±0.94 years (range 0.35–3.85) in 88 participants, 5 individuals (5.7%) converted from a negative to a positive VeraBIND Tau result, while 83/88 (94.3%) maintained a stable (either positive or negative) result throughout follow-up.
- **Status**: supported
- **Falsification criteria**: An independent longitudinal cohort with a substantially lower stable-result rate (e.g., high spontaneous positive-to-negative or negative-to-positive fluctuation unrelated to disease status) would refute the reproducibility claim.
- **Proof**: [E08]
- **Evidence basis**: Figure 5 (individual longitudinal VeraBIND Tau trajectories by Braak-like group, with converters marked as blue dashed lines).
- **Interpretation**: The paper interprets this as evidence of good test-retest reproducibility, distinguishing genuine biological conversion (the 5.7%) from assay noise.
- **Sources**:
  - Mean follow-up 1.72±0.94 years (0.35–3.85) ← Methods, PDF p.17 «The mean follow-up duration was of 1.72±0.94 years (min=0.35 – max=3.85).» [result]
  - 5 participants (5.7%) converted; 83/88 (94.3%) stable ← Results, PDF p.22 and Discussion, PDF p.25–26 «Five participants (5.7%) initially negative on VeraBIND Tau (VB-) converted to positivity (VB+) during follow-up ... five participants (5.7%) converted to VeraBIND Tau positivity, whereas 83/88 (94.3%) maintained stable results (positive or negative) throughout follow-up, indicating good test-retest reproducibility.» [result]
- **Dependencies**: none
- **Tags**: reproducibility, longitudinal, conversion

## C11: Greater concordance with tau-PET than with amyloid-PET/CSF status
- **Statement**: Among individuals with discordant amyloid/tau PET results, VeraBIND Tau was positive in 77.8% (n=7/9) of A-T+ cases (including all 5 A-T+ CI patients) versus only 7.7% (n=1/13) of A+T- cases (Fisher's Exact test p=0.001). Among individuals with concordant PET results (A-T-, A+T+), VeraBIND Tau achieved an overall accuracy of 96.7% (CU: 98.5%, n=66/67; CI: 94.6%, n=53/56).
- **Status**: supported
- **Falsification criteria**: An independent cohort in which VeraBIND Tau positivity is equally (or more) associated with amyloid status as with tau-PET status among discordant cases would refute this claim.
- **Proof**: [E01]
- **Evidence basis**: Table 2 (VeraBIND Tau results by clinical and A/T status).
- **Interpretation**: This pattern supports VeraBIND Tau as a tau-specific (not amyloid-driven) signal, consistent with its mechanism of action (seeding activity of pTau, independent of amyloid).
- **Sources**:
  - A-T+ 77.8% (n=7/9) vs A+T- 7.7% (n=1/13), Fisher p=0.001 ← Results, PDF p.18–19 «positive VeraBIND Tau results were observed in 77.8% (n=7/9) of the A-T+ cases ... The proportion of positive VeraBIND Tau results was higher in A-T+ cases (n=7/9, 77.8%) than in A+T- cases (n=1/13, 7.7%; Fisher's Exact test p=0.001)» [result]; Table 2, PDF p.41 «A+T- ... 12 – 1 + ... 7.7% / A-T+ ... 2 – 7 + ... 77.8%» [result]
  - Concordant-group accuracy 96.7% overall (CU 98.5% n=66/67; CI 94.6% n=53/56) ← Results, PDF p.18 «VeraBIND Tau was positive in 3.2% of the A-T- individuals (n=2/63...), and 96.7% of the A+T+ individuals (n=58/60...), achieving an overall accuracy of 96.7%. The diagnostic accuracy was relatively similar across clinical groups (CU: n=66/67, 98.5%; CI: n=53/56, 94.6%).» [result]
- **Dependencies**: none
- **Tags**: concordance, discordant-groups, tau-specificity

## C12: Possible affinity for non-AD (non-MK6240-avid) tauopathies
- **Statement**: VeraBIND Tau was positive in a single A-T- individual with a clinical phenotype suspected of corticobasal degeneration (a primary 4R-tauopathy poorly detected by [18F]MK6240 tau-PET), and in all 5 A-T+ CI patients suspected of primary age-related tauopathy (PART) or fronto-temporal lobar degeneration (FTLD), suggesting the assay may detect non-AD tauopathies that [18F]MK6240 tau-PET under-detects.
- **Status**: hypothesis
- **Falsification criteria**: Testing VeraBIND Tau against radiotracers with high affinity for 4R tauopathies (e.g., PI-2620) in a cohort of confirmed non-AD tauopathy patients, and finding no elevated positivity relative to true negatives, would refute this claim.
- **Proof**: [E01]
- **Evidence basis**: Table 2 footnote and Results text describing the single A-T- and five A-T+ discordant CI cases.
- **Interpretation**: The paper explicitly flags this as needing further investigation ("The diagnostic performance of the VeraBIND Tau assay for non-AD tauopathies needs to be further investigated using radiotracers that are more sensitive to 4R tauopathies than [18F]MK6240"), so it is marked `hypothesis` rather than `supported` — the current n (1 and 5 cases) is too small to be more than suggestive.
- **Sources**:
  - A-T- corticobasal degeneration case ← Table 2 note, PDF p.41 «The A-T- individual with positive VeraBIND Tau score has a clinical diagnosis of apraxia of speech, a clinical phenotype suspected of cortico-basal degeneration.» [result]; Results, PDF p.18 «The only A-T- CI patient with positive VeraBIND Tau result had apraxia of speech, a clinical phenotype suspected to be due to corticobasal degeneration, a primary 4R-tauopathy that is not detected by [18F]MK6240 tau-PET» [result]
  - 5 A-T+ CI PART/FTLD cases ← Results, PDF p.18 «positive VeraBIND Tau results were observed in 77.8% (n=7/9) of the A-T+ cases, including all five A-T+ CI patients (Braak-like tau-PET stage 1-2 in four cases and one case with Braak-like tau-PET stage 4 and subthreshold amyloidosis), suspected to suffer from primary age-related tauopathy (PART) or fronto-temporal lobar degeneration (FTLD)» [result]
  - Need for further investigation with 4R-sensitive tracers ← Discussion, PDF p.25 «The diagnostic performance of the VeraBIND Tau assay for non-AD tauopathies needs to be further investigated using radiotracers that are more sensitive to 4R tauopathies than [18F]MK624051.» [result]
- **Dependencies**: C11
- **Tags**: non-AD-tauopathy, specificity-limits, hypothesis-generating
