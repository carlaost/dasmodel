# Claims

All numbers are copied exactly from the guideline text (paper.pdf) or its tables/figures. Values the panel/design chose in advance (e.g., country selection, classification thresholds) are tagged `[input]`; values produced by the estimation/regression/statistical-testing pipeline are tagged `[result]`. Two internal numeric discrepancies in the source (Abstract vs. Methods/Table 1 sample sizes; Figure 2 bar values vs. Table 3 cell values) are surfaced explicitly rather than silently resolved — see `logic/solution/constraints.md`.

## C01: Cross-national dementia prevalence range
- **Statement**: Dementia prevalence among individuals aged 65+ ranges from 4.5% (Abstract) / 4.6% (Table 3) in Switzerland to 22.7% in Spain.
- **Status**: supported
- **Falsification criteria**: Disproved if Table 3 shows a lower Demented,% value for a country other than Switzerland, or a higher value for a country other than Spain, or if the Abstract/Table 3 figures for Switzerland do not both fall in the 4–5% range.
- **Proof**: [E03]
- **Evidence basis**: Abstract states the range directly; Table 3 provides the underlying per-country Demented,%(SE) values.
- **Interpretation**: The ~18-percentage-point spread between the lowest- and highest-prevalence countries is far larger than has been reported in prior, non-HCAP-validated European studies (see C04).
- **Dependencies**: none
- **Sources**:
  - "Dementia prevalence ranges from 4.5% in Switzerland to 22.7% in Spain" ← paper.pdf p.1 Abstract «Dementia prevalence ranges from 4.5% in Switzerland to 22.7% in Spain, MCI prevalence from 17.2% in Sweden to 31.1% in Portugal.» [result]
  - Switzerland Demented 4.6% (SE 0.5) ← paper.pdf Table 3 «Switzerland | 1,425 | 17.8 (1.0) | 4.6 (0.5) | 11.1 (0.8) | 2.1 (0.4)» [result]
  - Spain Demented 22.7% (SE 1.1) ← paper.pdf Table 3 «Spain | 1,458 | 29.1 (1.2) | 22.7 (1.1) | 28.7 (1.2) | 29.1 (1.2)» [result]
  - **Discrepancy note**: the Abstract states 4.5% for Switzerland while Table 3 states 4.6% (SE 0.5) for Switzerland's HCAP-validated Demented,% — a 0.1-point internal inconsistency between the Abstract and the main results table. Not resolved by the authors; reported here as-is.
- **Tags**: dementia-prevalence, cross-national-variation, main-result

## C02: Cross-national MCI prevalence range
- **Statement**: MCI prevalence ranges from 17.2% in Sweden to 31.1% in Portugal.
- **Status**: supported
- **Falsification criteria**: Disproved if Table 3 shows a lower MCI,% value for a country other than Sweden or a higher value for a country other than Portugal.
- **Proof**: [E03]
- **Evidence basis**: Abstract states the range directly; Table 3 confirms both endpoint values exactly.
- **Interpretation**: Unlike the dementia-range discrepancy in C01, the MCI range is internally consistent between Abstract and Table 3.
- **Dependencies**: none
- **Sources**:
  - "MCI prevalence from 17.2% in Sweden to 31.1% in Portugal" ← paper.pdf p.1 Abstract «MCI prevalence from 17.2% in Sweden to 31.1% in Portugal.» [result]
  - Sweden MCI 17.2% (SE 0.8) ← paper.pdf Table 3 «Sweden | 2,010 | 17.2 (0.8) | 5.0 (0.5) | 10.9 (0.7) | 2.7 (0.4)» [result]
  - Portugal MCI 31.1% (SE 1.5) ← paper.pdf Table 3 «Portugal | 924 | 31.1 (1.5) | 21.1 (1.3) | 32.0 (1.5) | 28.6 (1.5)» [result]
- **Tags**: MCI-prevalence, cross-national-variation, main-result

## C03: 28-unit average prevalence
- **Statement**: Averaged across all 28 SHARE units (27 European countries + Israel), HCAP-validated dementia prevalence is 10.9% (SE=0.1, rounded to "11%" in the Results text) and MCI prevalence is 23.9% (SE=0.2, rounded to "24%" in the Results text).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 3's "SHARE Wave 9" row reports different Demented/MCI percentages or standard errors, or if the Results text states a different rounded figure.
- **Proof**: [E03]
- **Evidence basis**: Results text states the rounded averages with SE; Table 3's summary row gives the exact underlying values.
- **Interpretation**: The average dementia prevalence is described as "roughly comparable to the results by Manly et al. for the US," situating the SHARE-HCAP estimate within the same range as the US HCAP-validated benchmark.
- **Dependencies**: C01, C02
- **Sources**:
  - "On average across all 28 SHARE countries, it is 11% (SE = 0.1)" ← paper.pdf p.4 Results «On average across all 28 SHARE countries, it is 11% (SE = 0.1), roughly comparable to the results by Manly et al. for the US.» [result]
  - "MCI is on average 24% (SE = 0.2)" ← paper.pdf p.4 Results «MCI is on average 24% (SE = 0.2) in the 27 European countries and Israel» [result]
  - SHARE Wave 9 row: MCI 23.9 (0.2), Demented 10.9 (0.1) ← paper.pdf Table 3 «SHARE Wave 9 | 47,193 | 23.9 (0.2) | 10.9 (0.1) | 17.8 (0.2) | 9.4 (0.1)» [result]
- **Tags**: average-prevalence, main-result

## C04: Prevalence is concentrated in Mediterranean and Southeastern Europe
- **Statement**: Dementia and MCI prevalence are particularly high in the Mediterranean and Southeastern European countries — MCI reaches "almost a third" in Bulgaria, Cyprus, Greece and Portugal — and are described as much higher than previously reported in these regions; the lowest MCI prevalence (~17%) clusters in Austria, Germany, Sweden, Denmark and Switzerland.
- **Status**: supported
- **Falsification criteria**: Disproved if Table 3 shows the named low-prevalence countries with MCI/dementia rates comparable to or above the Mediterranean/Southeastern group, or if the named high-MCI countries (Bulgaria, Cyprus, Greece, Portugal) do not have MCI rates near 30%.
- **Proof**: [E03]
- **Evidence basis**: Results text directly names the regional pattern and the specific countries at each extreme; Table 3 confirms MCI values of 29.9% (Bulgaria), 30.3% (Cyprus), 30.4% (Greece), 31.1% (Portugal), vs. 16.9–17.8% for Austria/Germany/Sweden/Denmark/Switzerland.
- **Interpretation**: The paper frames this regional concentration as evidence that "the risk of dementia is seriously underestimated in many European countries with potential adverse consequences for healthcare planning and prevention" (Discussion).
- **Dependencies**: C01, C02
- **Sources**:
  - "Prevalence rates are particularly high in the Mediterranean and Southeastern countries, much higher than previously reported" ← paper.pdf p.4 Results «Prevalence rates are particularly high in the Mediterranean and Southeastern countries, much higher than previously reported¹,³⁻⁹,¹³.» [result]
  - "reaching almost a third in Bulgaria, Cyprus, Greece, and Portugal" ← paper.pdf p.4 Results «again varying greatly between Austria, Germany, Sweden, Denmark and Switzerland on the lower side (about 17%) and the Mediterranean and Southeastern countries on the higher side, reaching almost a third in Bulgaria, Cyprus, Greece, and Portugal.» [result]
  - Bulgaria/Cyprus/Greece/Portugal MCI 29.9/30.3/30.4/31.1 ← paper.pdf Table 3 (rows for Bulgaria, Cyprus, Greece, Portugal) [result]
- **Tags**: regional-variation, Mediterranean, Southeastern-Europe

## C05: HCAP-validated estimates are higher on average but less relatively variable than Langa-Weir estimates
- **Statement**: The original Langa-Weir (LW) scale produces generally lower prevalence estimates than the HCAP-validated scale (28-unit average MCI: 17.8% LW vs. 23.9% HCAP-validated) but exhibits much larger relative cross-national variation, as indicated by the coefficient of variation for Demented,% (0.80 for LW vs. 0.46 for HCAP-validated).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 3's coefficient-of-variation row shows LW variation ≤ HCAP-validated variation, or if the LW-based 28-unit average MCI/dementia exceeds the HCAP-validated average.
- **Proof**: [E04]
- **Evidence basis**: Results/Discussion text states the comparison directly; Table 3 gives the exact coefficients of variation and averages.
- **Interpretation**: The paper attributes the difference to the larger breadth of cognition measures in the HCAP-validated scale relative to the LW scale (which uses only word recall, serial 7s, and backwards counting), reducing the impact of any single measure and detecting earlier/milder impairment via informant and self-reports.
- **Dependencies**: C03
- **Sources**:
  - "generally lower... but exhibit a much larger variation as indicated by the coefficient of variation" ← paper.pdf p.4 Results «The prevalence estimates based on the original LW scale are generally lower than the HCAP-validated estimates but exhibit a much larger variation as indicated by the coefficient of variation (i.e., the variance of the estimated effect scaled by the average effect size)» [result]
  - CV Demented: 0.46 (HCAP-validated) vs 0.80 (Langa-Weir) ← paper.pdf Table 3 «Coefficient of variation | 0.46 | | | 0.80» [result]
  - "23.9% averaged over all countries... much higher than measured by the LW scale (17.8%)" ← paper.pdf p.4 Results «The MCI prevalence rates measured by the HCAP-validated scale (23.9% averaged over all countries) are much higher than measured by the LW scale (17.8%).» [result]
- **Tags**: Langa-Weir, scale-comparison, coefficient-of-variation

## C06: Regression-based prediction closely replicates HCAP classification
- **Statement**: The regression-based prediction of cognitive status (Hurd et al. approach), applied within the SHARE-HCAP subsample, closely replicates the direct HCAP classification (Manly et al. approach): for the full SHARE-HCAP subsample (N=2,687), classified Normal/MCI/Demented are 72.6%/20.4%/7.0% vs. predicted 71.5%/21.5%/7.0%.
- **Status**: supported
- **Falsification criteria**: Disproved if the classified-vs-predicted percentages in Table 2 differ by a large margin (e.g., >5 percentage points) for the subsample total, or if the text does not characterize the replication as close.
- **Proof**: [E02]
- **Evidence basis**: Table 2 gives the exact classified vs. predicted percentages for the subsample overall and for each of the 5 constituent countries; the Results and Discussion text state the model "replicates the classification results... very well" and that this "documents [the] validity" of the regression-based refinement.
- **Interpretation**: This within-subsample validation step is what licenses extending the regression to predict cognitive-status probabilities for the entire SHARE parent sample (Table 3), since the HCAP classification itself is only available for the 5-country subsample.
- **Dependencies**: none
- **Sources**:
  - "the prediction by our regression model replicates the classification results from Step (b) very well" ← paper.pdf p.3 Methods «Table 2 shows that the prediction by our regression model replicates the classification results from Step (b) very well.» [result]
  - SHARE-HCAP subsample: classified 72.6/20.4/7.0, predicted 71.5/21.5/7.0 ← paper.pdf Table 2 «SHARE-HCAP subsample | 2,687 | 72.6 | 20.4 | 7.0 | 71.5 | 21.5 | 7.0» [result]
  - "We believe that Table 2 documents this validity" ← paper.pdf p.7 Discussion «Validity requires a sufficient accuracy of the prediction equation and a reasonable extent of consistency between the cognition measurements in SHARE-HCAP and the SHARE parent study. We believe that Table 2 documents this validity.» [result]
- **Tags**: validation, regression, Hurd-approach, Table2

## C07: Dementia/MCI risk rises with age; women have higher age-adjusted MCI risk but no significant sex difference in dementia
- **Statement**: Every 5-year increase in age increases the risk of dementia (all pairwise group-difference p-values below 0.0001 in Table 4's Age panel except one). Age-adjusted, women have a higher risk of MCI than men (p<0.0001), but there is no statistically significant sex difference in dementia risk (p=0.153).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 4 shows a non-significant (p≥0.05) age-group comparison for dementia, or if the Female-vs-Male dementia p-value is below 0.05, or if MCI does not differ significantly by sex.
- **Proof**: [E05]
- **Evidence basis**: Results text states both findings directly; Table 4 provides all pairwise p-values, including the single exception (age 85–89 vs 80–84, MCI, p=0.288).
- **Interpretation**: The sex difference in MCI (but not dementia) is discussed as potentially reflecting sex differences in education/access to education "over and above what is measured by education," linking this claim to C08/C11.
- **Dependencies**: C03
- **Sources**:
  - "Every 5-year increase in age increases the risk of dementia (all p-values below 0.0001)" ← paper.pdf p.5 Results «Every 5-year increase in age increases the risk of dementia (all p-values below 0.0001).» [result]
  - "Women have an age-adjusted higher risk of MCI... p < 0.0001... no significant difference in dementia" ← paper.pdf p.5 Results «Women have an age-adjusted higher risk of MCI compared to men (p < 0.0001) but there is no significant difference in dementia.» [result]
  - Female vs Male Demented p-value = 0.153 ← paper.pdf Table 4 «Female | 27,015 | 69.3 | 22.1 | 8.6 | ... | 0.000 | 0.000 | 0.153» [result]
  - Sole non-significant age comparison: 85–89 vs 80–84, MCI p=0.288 ← paper.pdf Table 4 «85–89 | 3,881 | 52.9 | 29.8 | 17.4 | (0.6) (0.3) (0.5) | 0.000 | 0.288 | 0.000» [result]
- **Tags**: age-effect, sex-difference, Table4

## C08: Higher childhood education is associated with lower dementia/MCI risk
- **Statement**: An increase in the age- and sex-adjusted level of education is associated with a decrease in the risk of both MCI and dementia; all pairwise between-education-group differences in Table 4 are statistically significant (p<0.0001).
- **Status**: supported
- **Falsification criteria**: Disproved if any of the three education-panel pairwise comparisons in Table 4 (≤Primary vs Some high school; Some high school vs High school/college; High school/college vs ≥College) has p≥0.05 for either MCI or Demented, or if higher education is not associated with lower prevalence.
- **Proof**: [E05]
- **Evidence basis**: Results text states the finding directly ("An important finding..."); Table 4's Education panel shows monotonically decreasing MCI/Demented prevalence with increasing education (Demented: 13.7% ≤Primary → 5.6% ≥College) and all p-values = 0.000.
- **Interpretation**: This is described as "an important finding" motivating the paper's central explanatory claim (C11) that education differences drive much of the cross-national variation in prevalence.
- **Dependencies**: C03
- **Sources**:
  - "An increase in the age and sex-adjusted level of education is associated with a decrease in the risk of both MCI and dementia (all p-values below 0.0001)" ← paper.pdf p.5 Results «An increase in the age and sex-adjusted level of education is associated with a decrease in the risk of both MCI and dementia (all p-values below 0.0001).» [result]
  - Demented prevalence by education: ≤Primary 13.7%, Some high school 10.3%, High school/some college 6.8%, ≥College 5.6% ← paper.pdf Table 4 (Education panel rows) [result]
- **Tags**: education-effect, main-finding, Table4

## C09: Stroke, depression, and diabetes are significant comorbidity risk factors for dementia; blood pressure and cholesterol are not
- **Statement**: Conditional on age, sex and education, a self-reported doctor's diagnosis of stroke increases the probability of being demented by 7.2 percentage points, a EURO-D depression score exceeding 4 increases it by 4.0 percentage points, and diabetes increases it by 0.8 percentage points; all three associations are statistically significant. High blood pressure and high cholesterol do not have statistically significant associations with dementia conditional on the other comorbidities.
- **Status**: supported
- **Falsification criteria**: Disproved if the stated percentage-point effects for stroke/depression/diabetes differ from 7.2/4.0/0.8, or if high blood pressure or high cholesterol are reported as statistically significant.
- **Proof**: [E06]
- **Evidence basis**: Results text and Figure 1's caption both state the stroke, diabetes, and EURO-D>4 effect sizes exactly, and both explicitly note blood pressure's non-significance; Figure 1 shows all nine point estimates and 95% CIs, with cholesterol's and pressure's CIs crossing zero.
- **Interpretation**: These comorbidity associations are presented as face-validity evidence for the prevalence estimates — "The probability of being demented also varies plausibly with comorbidities associated with dementia."
- **Dependencies**: none
- **Sources**:
  - "A diagnosis of stroke increases the probability of being demented by 7.2% points, diabetes by 0.8% points" ← paper.pdf p.5 Results «A diagnosis of stroke increases the probability of being demented by 7.2% points, diabetes by 0.8% points.» [result]
  - "A value exceeding 4 increases the probability of being demented by 4.0% points" ← paper.pdf p.5 Results «Depression is measured by the EURO-D scale. A value exceeding 4 increases the probability of being demented by 4.0% points.» [result]
  - "high blood pressure and high cholesterol values do not have a statistically significant association" ← paper.pdf p.5 Results «These associations are statistically significant, while high blood pressure and high cholesterol values do not have a statistically significant association with dementia conditional on the other co-morbidities.» [result]
  - Figure 1 caption confirms: "having had a diagnose of a stroke increases the probability of being demented by 7.2% which is statistically significant, while high blood pressure does not have a statistically significant association" ← paper.pdf Fig. 1 caption, p.7 [result]
- **Tags**: comorbidity, stroke, depression, diabetes, face-validity, Figure1

## C10: Physical activity is protective, smoking increases dementia risk; excessive alcohol shows no significant association in Wave 9
- **Statement**: Conditional on age, sex and education, current physical activity reduces the probability of being demented while smoking increases it; there is no statistically significant association between excessive alcohol use and dementia in Wave 9.
- **Status**: supported
- **Falsification criteria**: Disproved if physical activity is not associated with reduced dementia probability, if smoking is not associated with increased probability, or if excessive alcohol shows a statistically significant association in Wave 9.
- **Proof**: [E06]
- **Evidence basis**: Results text states all three findings directly; Figure 1 shows physical activity's point estimate (≈ −3 percentage points) and CI clearly excluding zero, smoking's point estimate positive with CI excluding zero, and excessive alcohol's CI clearly crossing zero (widest CI of the nine factors).
- **Interpretation**: These lifestyle associations are presented alongside the comorbidity associations (C09) as further face-validity evidence, aligned with risk factors identified in the 2024 Lancet Commission report on dementia prevention.
- **Dependencies**: none
- **Sources**:
  - "Current physical activity reduces the probability of being demented while smoking increases it" ← paper.pdf p.6 Results «Current physical activity reduces the probability of being demented while smoking increases it.» [result]
  - "We do not find a statistically significant association with excessive alcohol use in the current Wave 9" ← paper.pdf p.6 Results «We do not find a statistically significant association with excessive alcohol use in the current Wave 9.» [result]
- **Tags**: lifestyle, physical-activity, smoking, alcohol, Figure1

## C11: Equalizing education across countries would dramatically compress cross-national dementia-prevalence variation
- **Statement**: A counterfactual simulation of dementia prevalence assuming each country had the average level of childhood education across all 27 European countries and Israel produces a cross-national variation that is "dramatically smaller" than the actual observed variation (Figure 2), which the paper interprets as showing the strength of the association between education and the probability of being demented.
- **Status**: supported
- **Falsification criteria**: Disproved if the counterfactual (grey) bars in Figure 2 show comparable or greater cross-national spread than the actual (red) bars.
- **Proof**: [E07]
- **Evidence basis**: Results text states the counterfactual comparison and its interpretation directly; Figure 2 visually shows the red (actual) bars ranging from roughly 4% to roughly 18% while the grey (counterfactual) bars cluster much more narrowly (this ARA's digitized reading: roughly 8–9.4%, with Spain ≈10.7% as an outlier — see `evidence/figures/figure2.md`).
- **Interpretation**: This is the paper's headline explanatory claim: national differences in childhood education systems are proposed as a major driver of the large observed cross-national variation in dementia/MCI prevalence (O6), with the authors suggesting this may also help explain disproportionate dementia burden among African Americans in the US and global GBD/OECD-reported differences.
- **Dependencies**: C08, C01, C04
- **Sources**:
  - "This variation is dramatically smaller than the actual variation, showing the strength of the association between education and the probability of being demented" ← paper.pdf p.6 Results «Figure 2 shows how the probability of dementia would vary counterfactually across countries if education had been the same in all SHARE countries, namely the average of the 27 European countries and Israel. This variation is dramatically smaller than the actual variation, showing the strength of the association between education and the probability of being demented.» [result]
  - Figure 2 caption ← paper.pdf Fig. 2, p.8 «The red bars show the actual estimated share of demented individuals in each country. The grey bars show the counterfactual share of demented individuals if education in each country had been equal to the average of the 28 countries.» [result]
- **Tags**: education, counterfactual, key-finding, Figure2

## C12: The SHARE-HCAP validation subsample achieved a 75.8% response rate across five countries
- **Statement**: Of 3,546 eligible individuals sampled (aged 65+) in Czech Republic, France, Germany, Denmark and Italy, 2,687 participated in the SHARE-HCAP study, an overall response rate of 75.8%; participants averaged 75.5 years (SD=7.5), were 56.2% female, and 65.1% had completed secondary education (ISCED).
- **Status**: supported
- **Falsification criteria**: Disproved if the eligible/participant counts, response rate, or demographic percentages differ from those stated.
- **Proof**: [E01]
- **Evidence basis**: Methods text states the recruitment funnel and subsample demographics directly; Table 1 corroborates response rate, age, sex, and education distributions for the "SHARE-HCAP subsample (N=2687)" column.
- **Interpretation**: This response rate and demographic profile underlie the subsample's use as a validation base (A1 in `logic/problem.md`); the authors note the five countries were chosen to represent East/West/North/South Europe with oversampling of low word-recall scorers to ensure adequate MCI/dementia cases.
- **Dependencies**: none
- **Sources**:
  - "Of the 3,546 eligible individuals, 2,687 participated... overall response rate of 75.8%" ← paper.pdf p.3 Methods «Of the 3,546 eligible individuals, 2,687 participated in the SHARE-HCAP study, resulting in an overall response rate of 75.8% (Table 1).» [result]
  - "on average 75.5 (SD = 7.5) years old and primarily female (56.2%). 65.1% completed secondary education" ← paper.pdf p.3 Methods «They were on average 75.5 (SD = 7.5) years old and primarily female (56.2%). 65.1% completed secondary education as assessed by ISCED.» [result]
  - **Discrepancy note**: the Methods introduction (p.2) states "we drew a validation subsample (N = 2,678)" — 2,678 vs. the 2,687 used everywhere else (Table 1, Results text, Table 2's "SHARE-HCAP subsample" row) — a digit-transposition inconsistency within the source, not resolved by the authors and reported here as-is.
- **Tags**: SHARE-HCAP, response-rate, study-design, sample-characteristics

## C13: The SHARE-HCAP subsample closely resembles the SHARE parent Wave 9 sample on observed characteristics
- **Statement**: Weighted sample characteristics of the SHARE-HCAP subsample (N=2,687) and the SHARE parent Wave 9 sample (N=47,733, per Table 1's header) are similar on age (75.5 vs 75.6 years), sex (56.2% vs 56.6% female), and health (ADL+IADL 0.9 vs 1.2), though the HCAP subsample has somewhat more college-educated respondents (25.3% vs 21.4%) and higher household income (median €2000 vs €1600).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 1's SHARE-HCAP and SHARE-parent columns diverge substantially (e.g., by more than a few percentage points) on age or sex distribution, undermining the subsample's representativeness assumption (A1).
- **Proof**: [E01]
- **Evidence basis**: Table 1 provides the full weighted comparison of both samples across response rate, age, sex, education, health, and income.
- **Interpretation**: The close match on age, sex and health (but not on education or income) is consistent with the deliberate oversampling of low word-recall scorers in the HCAP design (C12), rather than representing an uncontrolled recruitment bias; it partially supports assumption A1 in `logic/problem.md` while leaving open whether education/income differences bias the classification-transfer step (C06).
- **Dependencies**: C12
- **Sources**:
  - Age: HCAP 75.5 (7.5) vs parent 75.6 (7.7); Female: 56.2% vs 56.6% ← paper.pdf Table 1 «Mean (SD), y | 75.5 (7.5) | 75.6 (7.7)» and «Female,% | 56.2 | 56.6» [result]
  - College degree or more: 25.3% (HCAP) vs 21.4% (parent); Median household income: 2000 (1700) vs 1600 (1800) Euro ← paper.pdf Table 1 «college degree or more, % | 25.3 | 21.4» and «Median in Euro (IQR) | 2000 (1700) | 1600 (1800)» [result]
- **Tags**: representativeness, Table1, sample-comparison
