# Claims

All numbers are copied exactly from the paper's main text, Table 1, Table 2, Fig. 1, and Fig. 2. This is an original cohort study (not a synthesis report), so reported statistics carry the `[result]` tag and are grounded to the page (of 9) and section whose verbatim text was opened and confirmed. Status is `supported` where the paper presents the association as its finding; claims about supplementary-only analyses (subgroup/sensitivity numbers not in the provided PDF) are marked accordingly.

## C01: Cohort composition, baseline MCI prevalence, and follow-up incidence
- **Statement**: The analytic cohort comprised 2148 dementia-free SNAC-K participants with available follow-up (median age 72.2 years [Q1-Q3 60.9-81.2], 61.5% female, 35.4% university-educated), followed for a mean of 9.6 (SD 4.3) years (up to 16 years total). At baseline, 381 (17.7%) participants had MCI. During follow-up, 286 participants (16.2% of those without baseline MCI) developed MCI, 364 (16.9%) developed all-cause dementia (212 cases, 58.2%, of AD type), and 1101 (51.3%) died.
- **Status**: supported
- **Falsification criteria**: A re-analysis of the same SNAC-K follow-up dataset yielding materially different baseline prevalence or incidence counts would refute it.
- **Proof**: [E01]
- **Evidence basis**: Table 1 (baseline characteristics, N=2148); Results §1 (p.2) incidence figures.
- **Interpretation**: The 17.7% baseline MCI prevalence and long (up to 16-year) follow-up give the cohort statistical power to observe all three transition types (NC→MCI, MCI→NC, MCI→dementia) that motivate the study.
- **Sources**:
  - 2148 dementia-free individuals; up to 16 years ← p.1 (Abstract) «We followed 2148 dementia-free individuals from a Swedish population-based cohort for up to 16 years.» [result]
  - median age 72.2 years, 61.5% female, 35.4% university ← p.2 (Results) «At baseline, median age of study participants was 72.2 years, 61.5% were females, and 35.4% had a university level of education or higher.» [result]; corroborated by Table 1 p.2 «Overall N=2148 ... Age 72.2 (60.9–81.2) ... Sex (F) 1322 (61.5%) ... Education (University) 760 (35.4%)» [result]
  - 381 (17.7%) MCI at baseline ← p.2 «At baseline, 381 (17.7%) participants had MCI.» [result]
  - mean follow-up 9.6 (4.3) years ← p.2 «During a mean follow up of 9.6 (4.3) years,» [result]
  - 286 (16.2%) developed MCI; 364 (16.9%) developed all-cause dementia; 212 (58.2%) AD type; 1101 (51.3%) died ← p.2 «286 (16.2% of participants who did not have MCI at baseline) participants developed MCI and 364 (16.9%) developed all-cause dementia, which in 212 cases (58.2%) was of AD type; 1101 (51.3%) participants died.» [result]
- **Dependencies**: none
- **Tags**: cohort, SNAC-K, baseline-characteristics, incidence

## C02: Continuous biomarker levels and progression across cognitive stages (non-linear)
- **Statement**: Modeled continuously (z-scored, restricted cubic splines), elevated levels of all six biomarkers except the Aβ42/40 ratio were associated with faster progression from MCI to all-cause and AD dementia, following a non-linear relationship; elevated GFAP was also associated with lower hazard of MCI reversion to normal cognition; no biomarker was associated with progression from normal cognition to MCI.
- **Status**: supported
- **Falsification criteria**: A re-fit of the spline multistate model on independent data showing a monotonically flat (null) relationship for these biomarkers in the MCI-to-dementia transition would refute it.
- **Proof**: [E02]
- **Evidence basis**: Fig. 1 (18-panel grid: 6 biomarkers × 3 transitions, HR on log scale 0.1-10 vs biomarker z-score -1 to 2).
- **Interpretation**: The non-linear, transition-specific pattern (flat for NC→MCI, rising steeply for MCI→dementia) is the paper's central visual argument that these biomarkers carry information specifically at the MCI stage, not for detecting incipient MCI in cognitively normal people.
- **Sources**:
  - all except Aβ42/40 faster progression MCI→dementia, non-linear ← p.2 (Results, "Individual blood biomarkers of AD and HR...") «Elevated levels of all biomarkers, except for the Aβ42/40 ratio, were associated with a faster progression from MCI to all-cause and AD dementia, following a non-linear relationship.» [result]
  - elevated GFAP → lower hazard of MCI reversion ← p.2 «Elevated levels of GFAP were also associated with lower hazard of reversion from MCI to normal cognition.» [result]
  - no association NC→MCI ← p.2 «No association was found between AD blood biomarkers and the progression from normal cognition to MCI.» [result]
  - visual confirmation: Fig. 1 NfL/GFAP/p-tau217/t-tau/p-tau181 "From MCI to all-cause dementia" panels show curves rising well above HR=1 with increasing z-score (steepest for NfL, reaching ≈5 at z=2; Aβ42/40 panel stays close to HR≈1 across the range) ← Fig. 1 p.3 (own visual reading; extraction method `visual_description`/`digitized_estimate`, reading confidence: medium — see `evidence/figures/figure1.md`) [result]
- **Dependencies**: none
- **Tags**: continuous-biomarker, spline, hazard-ratio, non-linear

## C03: Dichotomized cut-offs — strongest associations with MCI-to-dementia progression (basic model)
- **Statement**: Using predefined high/low cut-offs, the basic model (adjusted for sex and education) showed the strongest associations with progression from MCI to dementia for NfL (HR 1.84, 95% CI 1.43-2.36 for all-cause dementia; HR 2.34, 95% CI 1.77-3.11 for AD dementia) and p-tau217 (HR 1.74, 95% CI 1.38-2.19 for all-cause; HR 2.11, 95% CI 1.61-2.76 for AD dementia), followed by GFAP (HR 1.47, 95% CI 1.17-1.87 all-cause). A lower Aβ42/40 ratio was also associated with faster progression to all-cause dementia (HR 1.30, 95% CI 1.04-1.61, low vs high).
- **Status**: supported
- **Falsification criteria**: A re-analysis with the same cut-offs showing overlapping-null (CI crossing 1 in the opposite direction) HRs for NfL and p-tau217 would refute it.
- **Proof**: [E03]
- **Evidence basis**: Table 2 (basic-model columns, all six biomarkers).
- **Interpretation**: NfL and p-tau217 are highlighted by the authors as the two biomarkers with by far the strongest MCI→dementia signal, consistent with the continuous-spline finding (C02).
- **Sources**:
  - NfL HR 1.84 (1.43,2.36) all-cause; 2.34 (1.77,3.11) AD ← p.2 «NfL (HR 1.84, 95% CI 1.43, 2.36 for all-cause and HR 2.34, 95% CI 1.77, 3.11 for AD dementia)» [result]; corroborated by Table 2 p.4 «NfL ... 267/941 vs 97/1207 ... 1.84 (1.43, 2.36)» [result]
  - p-tau217 HR 1.74 (1.38,2.19) all-cause; 2.11 (1.61,2.76) AD ← p.2 «p-tau217 (HR 1.74, 95% CI 1.38, 2.19 for all-cause and HR 2.11, 95% CI 1.61, 2.76 for AD dementia), followed by GFAP» [result]; Table 2 p.4 «P-tau217 ... 231/803 vs 133/1345 ... 1.74 (1.38, 2.19)» [result]
  - GFAP basic model all-cause 1.47 (1.17,1.87) ← Table 2 p.4 «GFAP ... 253/879 vs 111/1269 ... 1.47 (1.17, 1.87)» [result]
  - Aβ42/40 low vs high, all-cause 1.30 (1.04,1.61) ← Table 2 p.4 «Aß42/40 Low vs High ... 241/1119 vs 123/1029 ... 1.30 (1.04, 1.61)» [result]; text corroboration p.2 «A lower Aβ42/40 ratio was also associated with faster progression from MCI to all-cause and AD dementia.» [result]
  - "similar results...dichotomized" ← p.2 «Similar results were obtained when baseline AD blood biomarkers were dichotomized using predeﬁned cut-off values, as shown in Table 2» [result]
- **Dependencies**: C02
- **Tags**: dichotomized-cutoff, hazard-ratio, NfL, p-tau217, basic-model

## C04: Attenuation after full adjustment for chronic diseases
- **Statement**: After further adjustment for chronic kidney disease, heart disease, cerebrovascular disease, anemia, and obesity, the association between p-tau181 and MCI reversion was attenuated and became non-significant (fully adjusted HR 0.60, 95% CI 0.32-1.13, versus basic-model HR 0.50, 95% CI 0.30-0.84), though the point estimate remained similar.
- **Status**: supported
- **Falsification criteria**: An independent replication in which the p-tau181-reversion association remains significant after equivalent comorbidity adjustment would refute the specific attenuation claim.
- **Proof**: [E03]
- **Evidence basis**: Table 2 (p-tau181 row, basic vs fully adjusted "From MCI to NC" columns).
- **Interpretation**: The authors treat this attenuation as evidence that part of the crude p-tau181-reversion signal may be confounded by comorbidity burden rather than reflecting a direct neuropathological effect.
- **Sources**:
  - attenuated, non-significant, similar point estimates ← p.2 «After further adjustment for chronic diseases (Table 2), the association between p-tau181 and MCI reversion was attenuated becoming non-signiﬁcant, yet with similar point estimates.» [result]
  - basic 0.50 (0.30,0.84) vs fully adjusted 0.60 (0.32,1.13) ← Table 2 p.4 «P-tau181 High vs Low ... 77/781 vs 216/1367 ... 0.50 (0.30, 0.84) ... 0.60 (0.32, 1.13)» [result]
- **Dependencies**: C03
- **Tags**: adjustment, confounding, attenuation, p-tau181, MCI-reversion

## C05: No biomarker predicts progression from normal cognition to MCI
- **Statement**: Neither continuous nor dichotomized levels of any of the six AD blood biomarkers were associated with the transition from normal cognition to MCI; all "From NC to MCI" hazard ratios in Table 2 have 95% confidence intervals spanning 1 in both basic and fully adjusted models.
- **Status**: supported
- **Falsification criteria**: A biomarker showing a confidence interval excluding 1 for the NC→MCI transition, replicated independently, would refute this null-result claim.
- **Proof**: [E02], [E03]
- **Evidence basis**: Fig. 1 ("From NC to MCI" column, all six biomarkers); Table 2 ("From NC to MCI" columns, basic and fully adjusted, all six biomarkers).
- **Interpretation**: The authors interpret this null result as showing AD blood biomarkers' utility is concentrated at the MCI stage rather than for detecting risk of incident cognitive impairment among cognitively normal community members — consistent with recommendations against biomarker use in asymptomatic individuals (see `related_work.md`).
- **Sources**:
  - no association NC→MCI (continuous) ← p.2 «No association was found between AD blood biomarkers and the progression from normal cognition to MCI.» [result]
  - no association NC→MCI (dichotomized) ← p.2 «No association was found with the progression from normal cognition to MCI.» [result]
  - all six "From NC to MCI" HRs cross 1 ← Table 2 p.4, e.g. «Aß42/40 ... 0.98 (0.72, 1.34) ... 0.99 (0.70, 1.41)»; «NfL ... 0.91 (0.57, 1.45) ... 0.70 (0.42, 1.19)»; «GFAP ... 0.91 (0.63, 1.30) ... 0.86 (0.57, 1.31)» [result]
- **Dependencies**: C02, C03
- **Tags**: null-result, NC-to-MCI, dichotomized, continuous

## C06: High p-tau181, NfL, and GFAP reduce hazard of MCI reversion (basic model)
- **Statement**: In the basic model, participants with high (vs low) p-tau181, NfL, and GFAP had lower hazard of reversion from MCI to normal cognition: p-tau181 HR 0.50 (95% CI 0.30-0.84), NfL HR 0.56 (95% CI 0.31-1.00), and GFAP HR 0.53 (95% CI 0.33-0.85). In the fully adjusted model, the NfL and GFAP associations remained significant (NfL HR 0.41, 95% CI 0.22-0.78; GFAP HR 0.50, 95% CI 0.30-0.85) while p-tau181's became non-significant (see C04).
- **Status**: supported
- **Falsification criteria**: An independent cohort showing null or reversed HRs for NfL/GFAP on MCI reversion after equivalent adjustment would refute it.
- **Proof**: [E03]
- **Evidence basis**: Table 2 ("From MCI to NC" columns).
- **Interpretation**: Elevated neurodegeneration/astrocytic-activation markers (NfL, GFAP) mark MCI cases less likely to be transient/reversible, supporting their use to distinguish neuropathological MCI from non-progressive causes (e.g., depression, transient medical conditions).
- **Sources**:
  - p-tau181 basic 0.50 (0.30,0.84) ← Table 2 p.4 «P-tau181 ... 77/781 vs 216/1367 ... 0.50 (0.30, 0.84)» [result]
  - NfL basic 0.56 (0.31,1.00); fully adjusted 0.41 (0.22,0.78) ← Table 2 p.4 «NfL ... 84/941 vs 209/1207 ... 0.56 (0.31, 1.00) ... 0.41 (0.22, 0.78)» [result]
  - GFAP basic 0.53 (0.33,0.85); fully adjusted 0.50 (0.30,0.85) ← Table 2 p.4 «GFAP ... 87/879 vs 206/1269 ... 0.53 (0.33, 0.85) ... 0.50 (0.30, 0.85)» [result]
  - narrative confirmation ← p.2 «Participants with high, compared to low, p-tau181, NfL, and GFAP also exhibited lower hazard of reversion from MCI to normal cognition.» [result]
- **Dependencies**: C03, C04
- **Tags**: MCI-reversion, NfL, GFAP, p-tau181, dichotomized

## C07: Dose-response with number of elevated biomarkers (p-tau217, NfL, GFAP)
- **Statement**: The hazard of progression from MCI to all-cause dementia increased with the number of elevated biomarkers (among p-tau217, NfL, GFAP) at baseline: HR 1.41 (95% CI 0.98-2.02) for one, 2.36 (95% CI 1.61-3.46) for two, and 2.22 (95% CI 1.50-3.28) for three, versus none. For AD dementia, three elevated biomarkers gave HR 3.71 (95% CI 2.22-6.20) versus none. Conversely, the hazard of MCI reversion to normal cognition decreased with more elevated biomarkers, roughly 70% lower with three versus none elevated (HR 0.26, 95% CI 0.11-0.61). No association was found between the number of elevated biomarkers and progression from normal cognition to MCI.
- **Status**: supported
- **Falsification criteria**: A replication showing no monotonic trend in hazard with increasing biomarker count for MCI-to-dementia transitions would refute the dose-response claim.
- **Proof**: [E04]
- **Evidence basis**: Fig. 2 (three forest-plot panels: NC→MCI, MCI→NC, MCI→all-cause dementia, by count of 0/1/2/3 elevated biomarkers among p-tau217, NfL, GFAP).
- **Interpretation**: Combining the three strongest univariate markers into a simple count produces a stronger, dose-graded risk signal for dementia progression than any single marker, and a similarly graded protective/anti-reversion signal.
- **Sources**:
  - three vs none all-cause dementia HR 2.22 (1.50,3.28) ← p.2 «Participants with three elevated biomarkers had more than twice the hazard of progressing to all-cause dementia (HR 2.22, 95% CI 1.50, 3.28) compared to those with none» [result]
  - three vs none AD dementia HR 3.71 (2.22,6.20) ← p.2 «an even higher hazard of progression to AD dementia (HR 3.71, 95% CI 2.22, 6.20)» [result]
  - one/two/three all-cause dementia HRs 1.41 (0.98,2.02) / 2.36 (1.61,3.46) / 2.22 (1.50,3.28) ← Fig. 2 p.4 «HR 1.41 (0.98, 2.02) ... HR 2.36 (1.61, 3.46) ... HR 2.22 (1.50, 3.28)» [result]
  - reversion 70% lower (three vs none) ← p.5 «the hazard of MCI reversion to normal cognition decreased with the number of elevated biomarkers at baseline and was 70% lower in individuals with three compared to those with no elevated biomarkers» [result]
  - reversion HR three vs none 0.26 (0.11,0.61) ← Fig. 2 p.4 «HR 0.26 (0.11, 0.61)» [result]
  - no association with NC→MCI (combination) ← p.5 «No association was found between biomarker combinations and the progression from normal cognition to MCI (Fig. 2).» [result]
- **Dependencies**: C03
- **Tags**: combination, dose-response, p-tau217, NfL, GFAP

## C08: Pairwise combination of p-tau217 and NfL gives the fastest progression
- **Statement**: Among pairs of biomarkers, individuals with both p-tau217 and NfL elevated had the fastest progression from MCI to dementia. Relative to individuals with low levels of both, the HRs of progression to all-cause dementia were 1.59 (95% CI 1.13-2.22) for high NfL only, 1.71 (95% CI 1.11-2.63) for high p-tau217 only, and 2.29 (95% CI 1.62-3.24) for both elevated. For progression to AD dementia, the HRs were 2.09 (95% CI 1.37-3.17) for high NfL only, 2.03 (95% CI 1.23-3.36) for high p-tau217 only, and 3.07 (95% CI 2.04-4.60) for both elevated.
- **Status**: supported
- **Falsification criteria**: A replication showing the both-elevated group does not exceed either single-marker-elevated group's hazard would refute it.
- **Proof**: [E05]
- **Evidence basis**: Text-reported values from Supplementary Tables S12-S13 (pairwise combination analysis); the underlying supplementary tables themselves are not in the provided input.
- **Interpretation**: p-tau217 (AD-pathology-specific) and NfL (non-specific neurodegeneration marker) appear to capture complementary information, so their joint elevation identifies the highest-risk MCI subgroup.
- **Sources**:
  - fastest progression with p-tau217+NfL elevated ← p.2 «the fastest progression from MCI to all-cause and AD dementia was observed in individuals with elevated levels of both p-tau217 and NfL» [result]
  - all-cause dementia HRs 1.59/1.71/2.29 ← p.2 «the HRs of progression to all-cause dementia were 1.59 (95% CI 1.13, 2.22) for those with high NfL only, 1.71 (95% CI 1.11, 2.63) for those with high p-tau217 only, and 2.29 (95% CI 1.62, 3.24) for those with both biomarkers elevated.» [result]
  - AD dementia HRs 2.09/2.03/3.07 ← p.5 «For progression to AD dementia, the HRs were 2.09 (95% CI 1.37, 3.17) for high NfL only, 2.03 (95% CI 1.23, 3.36) for high p-tau217 only, and 3.07 (95% CI 2.04, 4.60) when both biomarkers were elevated.» [result]
- **Dependencies**: C07
- **Tags**: pairwise-combination, p-tau217, NfL, AD-dementia

## C09: Age-stratified associations (directional; supplementary detail not provided)
- **Statement**: Associations between biomarkers and progression from MCI to all-cause and AD dementia were slightly stronger in participants under 78 years old compared to those older; results for MCI reversion were mixed across age groups. Exact stratum-specific HRs are reported only in Supplementary Tables S2-S3, which are not part of the provided input.
- **Status**: supported (directional only — exact figures not available from provided input)
- **Falsification criteria**: A stratified re-analysis showing equal or stronger associations in the ≥78 group would refute the "slightly stronger under 78" direction.
- **Proof**: [E06]
- **Evidence basis**: Text-only statement; Supplementary Tables S2-S3 not provided.
- **Interpretation**: Consistent with the authors' own prior finding that AD blood biomarker levels rise with age even in unimpaired individuals, motivating consideration of age-adjusted cut-offs (Discussion, p.5).
- **Sources**:
  - slightly stronger under 78; mixed for reversion ← p.2 «The associations between biomarkers and progression from MCI to all-cause and AD dementia were slightly stronger in participants under 78 years old, compared to those older. Results for MCI reversion were instead mixed (Supplementary Tables S2 and S3).» [result]
  - exact stratum HRs: Not specified in paper (Supplementary Tables S2-S3 not in provided input)
- **Dependencies**: C03
- **Tags**: subgroup, age, sensitivity, not-fully-available

## C10: Sex-stratified associations (directional; supplementary detail not provided)
- **Statement**: Sex-stratified analyses showed stronger associations between AD blood biomarkers and progression from MCI to all-cause dementia in women than in men, though the authors note overlapping confidence intervals preclude definitive conclusions. Exact sex-specific HRs are reported only in Supplementary Tables S4-S5, not part of the provided input.
- **Status**: supported (directional only — exact figures not available from provided input)
- **Falsification criteria**: A stratified re-analysis with non-overlapping CIs showing stronger or equal associations in men would refute the "stronger in women" direction.
- **Proof**: [E07]
- **Evidence basis**: Text-only statement; Supplementary Tables S4-S5 not provided.
- **Interpretation**: The authors explicitly flag this as inconclusive rather than a firm sex-difference finding, and call for dedicated studies of sex-adjusted cut-offs.
- **Sources**:
  - stronger in women ← p.2 «Sex-stratiﬁed analyses (Supplementary Tables S4 and S5) showed stronger associations between AD blood biomarkers and progression from MCI to all-cause dementia in women.» [result]
  - cannot draw definitive conclusions (overlapping CIs) ← p.5 «the association between AD blood biomarkers and the progression to all-cause dementia appeared stronger in women than in men. However, we cannot draw deﬁnitive conclusions due to overlapping conﬁdence intervals.» [result]
  - exact stratum HRs: Not specified in paper (Supplementary Tables S4-S5 not in provided input)
- **Dependencies**: C03
- **Tags**: subgroup, sex, sensitivity, not-fully-available

## C11: Sensitivity — excluding participants with baseline MCI
- **Statement**: Most results remained consistent after excluding participants with MCI at baseline (n=381). Only the associations between p-tau181 and progression from MCI to all-cause/AD dementia, and between NfL/GFAP and MCI reversion, were attenuated to non-significance, although point estimates remained similar. Exact re-fit HRs are reported only in Supplementary Tables S6-S7, not part of the provided input.
- **Status**: supported (directional only — exact figures not available from provided input)
- **Falsification criteria**: A re-fit showing the core NfL/p-tau217 MCI-to-dementia associations disappear (not merely the noted p-tau181/NfL/GFAP attenuations) when baseline MCI cases are excluded would refute the "most results consistent" claim.
- **Proof**: [E08]
- **Evidence basis**: Text-only statement; Supplementary Tables S6-S7 not provided.
- **Interpretation**: Because MCI duration prior to baseline was unknown, this sensitivity check addresses possible reverse-causation/prevalent-case bias; the reported consistency supports the robustness of the core NfL/p-tau217/GFAP findings.
- **Sources**:
  - most results consistent after exclusion ← p.2 «Most results remained consistent after excluding participants with MCI at baseline.» [result]
  - p-tau181 and NfL/GFAP attenuated, non-significant, similar point estimates ← p.2 «Only the associations between p-tau181 and progression from MCI to all-cause and AD dementia and between NfL and GFAP and MCI reversion were attenuated, becoming non-signiﬁcant (Supplementary Tables S6 and S7), although point estimates remained similar.» [result]
  - n=381 excluded ← p.7 (Methods, Subgroup and sensitivity analyses) «the analyses were repeated excluding those with MCI at baseline (n = 381)» [result]
- **Dependencies**: C03, C04, C06
- **Tags**: sensitivity, reverse-causation, baseline-MCI-exclusion, not-fully-available

## C12: Sensitivity — inverse probability weighting for attrition
- **Statement**: Sensitivity analyses using inverse probability weighting (IPW) — with weights derived from logistic regression on age, sex, education, number of chronic diseases, and biomarker levels — to account for attrition yielded estimates consistent with the main results. Exact IPW-weighted HRs are reported only in Supplementary Tables S8-S9, not part of the provided input.
- **Status**: supported (directional only — exact figures not available from provided input)
- **Falsification criteria**: An IPW re-analysis showing materially different (e.g., substantially attenuated or reversed) HRs for the core biomarkers would refute the "consistent with main results" claim.
- **Proof**: [E09]
- **Evidence basis**: Text-only statement; Supplementary Tables S8-S9 not provided.
- **Interpretation**: Addresses the documented attrition bias noted in Constraints (dropouts and biomarker-missing participants differed systematically from the analytic sample), supporting that this bias did not materially distort the main findings.
- **Sources**:
  - IPW consistent with main results ← p.2 «Sensitivity analyses using inverse probability weighting (IPW) to account for attrition yielded estimates that were consistent with the main results (Supplementary Tables S8 and S9).» [result]
  - IPW weight covariates ← p.7 «weights derived from logistic regression models including age, sex, education, number of chronic diseases, and biomarker levels» [result]
- **Dependencies**: C03
- **Tags**: sensitivity, attrition, inverse-probability-weighting, not-fully-available

## C13: Sensitivity — CIND operationalization instead of MCI
- **Statement**: When applying the cognitive impairment no dementia (CIND) operationalization instead of MCI (i.e., dropping the requirement of preserved functional independence), the results were comparable to those obtained with the MCI definition. Underlying data are stated as "available upon request" rather than reported in the paper or its supplement.
- **Status**: supported (directional only — no exact figures available; data stated as available upon request, not in provided input)
- **Falsification criteria**: A CIND re-analysis producing materially different biomarker-transition associations from the MCI-based main analysis would refute the comparability claim.
- **Proof**: [E10]
- **Evidence basis**: Text-only statement; no table provided (paper states data available upon request).
- **Interpretation**: Suggests the main findings are not an artifact of the specific functional-independence criterion used to define MCI versus the broader, purely cognitive-test-based CIND definition.
- **Sources**:
  - comparable results with CIND ← p.2 «When applying cognitive impairment no dementia (CIND) operationalization instead of MCI, the results were comparable to those obtained with the MCI deﬁnition (data available upon request).» [result]
  - CIND definition ← p.6 (Methods) «An alternative operationalization—cognitive impairment, no dementia (CIND)—was also adopted, deﬁned as scoring ≤1.5 SD below the age-speciﬁc mean in at least one cognitive domain in the absence of a dementia diagnosis.» [input]
- **Dependencies**: C03
- **Tags**: sensitivity, CIND, operationalization, not-fully-available
