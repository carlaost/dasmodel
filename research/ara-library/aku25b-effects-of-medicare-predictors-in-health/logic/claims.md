# Claims

## C01: PAF-based Cox decomposition splits any disparity into exact exposure × vulnerability factors
- **Statement**: For a Cox model with a disparity indicator `r` and binary predictors `x_i`, the observed subpopulation risk ratio factorizes as `RR = R_r · Π_i f_i` where `f_i = (1 − PAF_0i)/(1 − PAF_1i) = [1 + P_1i(R_1i − 1)] / [1 + P_0i(R_0i − 1)]`, and each `f_i` decomposes exactly and multiplicatively into an exposure effect `E_i` and a vulnerability effect `V_i` (`f_i = E_i · V_i`); the shared baseline hazard `h_0(t)` cancels in the ratio, so no baseline-hazard assumption is required.
- **Status**: supported
- **Falsification criteria**: Show that `f_i ≠ E_i·V_i` under the stated definitions, or that the derivation of Eq. 6 requires assumptions about `h_0(t)`, or that `Π_i f_i · R_r` does not reproduce the modeled `RR`.
- **Proof**: [E01]
- **Evidence basis**: Analytic derivation Eqs. 1–6; the exact identity `f_i = E_i V_i` with closed forms for `E_i`, `V_i` (Eq. 6); Table 4 presents every predictor cell in the `total = exposure * vulnerability` form, confirming the multiplicative split numerically.
- **Interpretation**: The method belongs to the family of parametric causal-mediation / hazard-rate decomposition algorithms and is "straightforward to implement" once the Cox model and prevalences are estimated (§4).
- **Sources**: `f_i = E_i V_i` ← Table 4 footnote c «The effects of predictors are determined by factors f_i in Equation (6) that are multiplicatively decomposed by the exposure and vulnerability effects: f_i = E_j V_j.» [result]; `RR = R_r Π_i f_i` ← §2 Eq. 6 «RR = R_r Π_i f_i, f_i = (1−PAF_0i)/(1−PAF_1i) = (1+P_1i(R_1i−1))/(1+P_0i(R_0i−1)) = E_i V_i» [input]
- **Dependencies**: none
- **Tags**: methodology, PAF, decomposition, Cox model

## C02: Low income (dual eligibility) is the main predictor of most AD-risk disparities, acting through exposure
- **Statement**: Medicare/Medicaid dual eligibility (low income) is the largest single contributor to most of the studied disparities, and its contribution is dominated by the exposure channel — the low-income prevalence is higher in non-White subpopulations (e.g., 50.9% Hispanic vs 7.9% White at age 70) so its decomposition factor is carried by `E_i` (e.g., Black–White age 70 `1.11 = 1.15 * 0.97`, exposure 1.15 > vulnerability 0.97).
- **Status**: supported
- **Falsification criteria**: Show for the affected disparities that the low-income total factor `f` is not the largest among predictors, or that its vulnerability factor `V` exceeds its exposure factor `E`.
- **Proof**: [E02, E03]
- **Evidence basis**: Table 4 low-income rows (exposure factor exceeds vulnerability factor across BW/SB/WA cells); Table 2 low-income prevalences (7.9% White vs 24.8–50.9% non-White at age 70); Figure 1 dashed low-income series moves the unexplained curve toward observed for BW, WA, SB.
- **Interpretation**: Income-related disparities call for socioeconomic intervention rather than clinical management (§4, Discussion).
- **Sources**: exposure dominance ← §3 «The effect of low income is dominated by the exposure effect: prevalence of dual eligibility is higher for non-White subpopulations.» [result]; BW age-70 low income `1.11=1.15 * 0.97` ← Table 4, Black–White block [result]; prevalence 50.9% vs 7.9% ← Table 2, Low income/dual eligibility age 70 (Hispanic 50.9, White 7.9) [result]; "low income was the main predictor for most of the studied disparities" ← §4 Discussion (p. 9) [result]
- **Dependencies**: C01
- **Tags**: low income, dual eligibility, exposure, socioeconomic status

## C03: Vulnerability to arterial hypertension is a consistent dominant disease predictor
- **Statement**: Among the disease predictors, arterial hypertension is the strongest predictive factor of AD-risk disparities, and its contribution is dominated by the **vulnerability** channel (exposure factor ≈ 1.00), e.g., Hispanic–White age 85 `1.27 = 0.99 * 1.28` and Black–White age 75 `1.16 = 1.01 * 1.14`.
- **Status**: supported
- **Falsification criteria**: Show that hypertension's vulnerability factor is not the dominant disease-predictor contribution for the affected disparities, or that its effect is carried by exposure rather than vulnerability.
- **Proof**: [E02, E03]
- **Evidence basis**: Table 4 arterial-hypertension rows (vulnerability factor >> exposure factor ≈1.00 for BW and HW); §3/§4 text naming hypertension the strongest disease predictor via vulnerability.
- **Interpretation**: Hypertension-related disparities suggest a focus on managing vulnerability — better hypertension control, treatment adherence, and access (§4).
- **Sources**: "arterial hypertension is the strongest predictive factor … effect of vulnerability of hypertension dominates" ← §3 (p. 5)/§4 «the effect of vulnerability of hypertension dominates to the extent that arterial hypertension becomes the main disease-related predictor in the generation of health disparities related to the AD risk» [result]; HW age-85 `1.27=0.99 * 1.28` ← Table 4, Hispanic–White block [result]; BW age-75 `1.16=1.01 * 1.14` ← Table 4, Black–White block [result]
- **Dependencies**: C01
- **Tags**: hypertension, vulnerability, disease predictor

## C04: Cerebrovascular disease and depression are notable secondary predictors
- **Statement**: Cerebrovascular diseases (stroke) and depression are the notable secondary disease predictors of AD-risk disparities, with depression carrying the largest raw per-predictor hazard ratios (up to 3.12) and a slightly higher exposure effect, and cerebrovascular disease a slightly higher vulnerability effect.
- **Status**: supported
- **Falsification criteria**: Show that predictors other than stroke and depression rank as the leading secondary contributors, or that depression's per-predictor hazard ratios are not the largest in Table 3.
- **Proof**: [E02]
- **Evidence basis**: Table 3 depression hazard ratios reach 3.12 (White–Asian, age 70) — the largest single value in the table; §4 text names depression and cerebrovascular disease as the two other strong disease-related factors with similar-magnitude contributions.
- **Interpretation**: Depression is underdiagnosed among the Black subpopulation, which "should be kept in mind when interpreting PAFs for depression" (§4, refs 38–40).
- **Sources**: "cerebrovascular diseases and depression as notable secondary predictors" ← Abstract [result]; depression HR 3.12 ← Table 3, Depression age 70 White–Asian cell `2.57,3.12` [result]; "Two other strong disease-related factors with approximately similar contributions are depression and cerebrovascular diseases … slightly higher exposure effect for depression, and a slightly higher vulnerability effect for cerebrovascular diseases" ← §4 (p. 9) [result]
- **Dependencies**: C01
- **Tags**: cerebrovascular disease, stroke, depression, secondary predictor

## C05: Predictors explain about half the Black–White disparity, over-explain Hispanic–White, and inflate Native-American/Asian disparities
- **Statement**: The examined predictors explain approximately half of the observed Black–White disparity and more than fully explain the Hispanic–White disparity (unexplained factor < 1: 0.77–0.96), whereas for White–Native American and White–Asian the unexplained disparity exceeds the observed disparity (e.g., WN age 70: observed 1.26 vs unexplained 2.10; WA age 70: observed 1.40 vs unexplained 1.86), so the predictors act to *increase* the apparent disparity.
- **Status**: supported
- **Falsification criteria**: Show the unexplained Black–White factor is not roughly midway between 1 and the observed disparity, or that unexplained < observed for WN/WA, contradicting the tabulated values.
- **Proof**: [E03]
- **Evidence basis**: Table 4 observed vs unexplained rows (BW 70: 1.65 → 1.43; HW unexplained 0.77–0.96 < 1; WN 70: 1.26 vs 2.10; WA 70: 1.40 vs 1.86); Figure 1 (open dots above solid points for WN/WA).
- **Interpretation**: Because observed risk in Asian and Native-American subpopulations is lower than in White Americans, "removing" the predictors' protective bookkeeping increases the residual gap (§4).
- **Sources**: "explain approximately half of the observed Black–White disparities" ← §3 (p. 4) «The contributions of the risk factors used in the analysis explain approximately half of the observed Black–White disparities.» [result]; WN observed 1.26 / unexplained 2.10 ← Table 4, White–Native American block, age 70 [result]; WA observed 1.40 / unexplained 1.86 ← Table 4, White–Asian block, age 70 [result]; regular situation `r_unex < r_unob` for Black–White and Hispanic–White ← §4 Discussion (p. 6) [result]
- **Dependencies**: C01, C02, C03
- **Tags**: Black–White, Hispanic–White, Native American, Asian, unexplained disparity

## C06: Female–male and stroke-belt disparities are less influenced by the examined predictors than racial disparities
- **Statement**: Disease-related and income predictors explain only a small part of female–male and stroke-belt disparities relative to racial disparities; for female–male, predictors explain a larger share of male risk at advanced ages, so the unexplained female–male disparity becomes larger than the observed one (e.g., age 85: observed 1.19 vs unexplained 1.27), and for stroke-belt the dominant explanatory channel is exposure to cerebrovascular disease.
- **Status**: supported
- **Falsification criteria**: Show that the examined predictors explain as large a fraction of FM/SB disparities as of racial disparities, or that the FM unexplained factor does not exceed the observed factor at advanced ages.
- **Proof**: [E03]
- **Evidence basis**: Table 4 FM block (observed 1.19 vs unexplained 1.27 at age 85; per-predictor factors near 1.00); SB block (cerebrovascular and low-income factors slightly above 1, hypertension below 1 at older ages).
- **Interpretation**: FM and SB disparities are driven largely by factors outside the examined Medicare predictor set (§4).
- **Sources**: "disease-related predictors explained only a small part of female–male and stroke-belt disparities" ← §4 (p. 9) [result]; FM age-85 observed 1.19 / unexplained 1.27 ← Table 4, female–male block [result]; "exposure effect from cerebrovascular diseases was identified as the dominant exposure factor in explaining the stroke-belt disparities" ← §4 (p. 9) [result]
- **Dependencies**: C01
- **Tags**: female–male, stroke belt, geographic disparity

## C07: A majority of the exposure/vulnerability effects are statistically significant, with exposure significant more often than vulnerability
- **Statement**: Bootstrapping (100 resamples) shows that 57.4% of the exposure and vulnerability effects are significant; the fractions of significant **exposure** effects are 86% (Black–White), 39% (White–Native American), 86% (Hispanic–White), 75% (White–Asian), 96% (female–male), 96% (stroke-belt), while the fractions of significant **vulnerability** effects are lower: 61% (Black–White), 7% (White–Native American), 25% (Hispanic–White), 32% (White–Asian), 57% (female–male), 29% (stroke-belt).
- **Status**: supported
- **Falsification criteria**: Show that fewer than a majority of effects are significant, or that the reported per-disparity significant fractions differ from the tabulated bootstrap results.
- **Proof**: [E04]
- **Evidence basis**: §3 text (p. 5) reporting bootstrap significance fractions; standard errors/CIs computed from 100 bootstrap resamples (§2). The top-40 highest effects are in supporting-information Table S2 (not in the provided main text).
- **Interpretation**: Exposure effects are more consistently significant than vulnerability effects, reinforcing the exposure-driven reading of income-related disparities.
- **Sources**: "the majority of the exposure and vulnerability effects (57.4%) are significant" ← §3 (p. 5) [result]; exposure fractions 86/39/86/75/96/96% and vulnerability fractions 61/7/25/32/57/29% ← §3 (p. 5) «The fractions of significant exposure effects are 86% for Black–White, 39% for White–Native American, 86% for Hispanic–White, 75% for White–Asian, 96% for female–male, and 96% for stroke-belt disparities. The fractions of significant vulnerability effects are 61% for Black–White, 7% for White–Native American, 25% for Hispanic–White, 32% for White–Asian, 57% for female–male, and 29% for stroke-belt disparities.» [result]; 100 bootstrap resamples ← §2 «resampling with replacement to create 100 random samples from our original sample» [input]
- **Dependencies**: C02, C03
- **Tags**: bootstrap, significance, exposure, vulnerability

## C08: Results are stable across outcome-ascertainment sensitivity analyses
- **Statement**: Sensitivity analyses using three alternatives to the base AD-onset ascertainment — 180-day confirmation period, no confirmation period, and using ADRD instead of AD as the outcome — yield only minor differences; differences for 90- vs 180-day confirmation are negligible, differences without a confirmation period tend to be slightly lower, and ADRD effects are higher for the exposure component and lower for the vulnerability component than AD.
- **Status**: supported
- **Falsification criteria**: Show that any alternative ascertainment materially changes the ranking or sign of the exposure/vulnerability contributions.
- **Proof**: [E05]
- **Evidence basis**: §3 text (p. 5) describing the sensitivity analysis; results detailed in supporting-information Table S3 (not in the provided main text).
- **Interpretation**: The decomposition is robust to reasonable choices in the disease-onset algorithm and to broadening AD to ADRD.
- **Sources**: "Sensitivity analysis demonstrated the stability of the results" ← §3 (p. 5) [result]; "differences between estimates for 90- and 180-day confirmation periods were negligible … effects in ADRD are higher for the exposure component and lower for the vulnerability component" ← §3 (p. 5) [result]
- **Dependencies**: C01
- **Tags**: sensitivity analysis, robustness, ADRD
