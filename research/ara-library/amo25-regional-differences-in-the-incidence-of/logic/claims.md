# Claims

All numbers are per 100,000 population unless stated. IRR = incidence rate ratio (Poisson).

## C01: Crude ADRD incidence differs significantly across all four public health regions, and is highest in Pee Dee
- **Statement**: The 2021 crude incidence of ADRD differed statistically significantly across all four SC public health regions (every pairwise comparison p < 0.05); it was highest in Pee Dee (896 per 100,000) and lowest in Midlands (684 per 100,000), with Low Country (764) and Upstate (840) between.
- **Status**: supported
- **Falsification criteria**: One or more pairwise crude-incidence comparisons across PHRs are non-significant (p ≥ 0.05), or the region ordering (Pee Dee highest) does not hold.
- **Proof**: [E01, E02]
- **Evidence basis**: Figure 3 legend gives region crude values (Midlands 684, Low Country 764, Upstate 840, Pee Dee 896). Table 2 "Crude incidence" column: all six pairwise IRRs are bolded significant (LC vs Midlands p<0.0001; LC vs Pee Dee p<0.0001; LC vs Upstate p=0.0001; Midlands vs Pee Dee p<0.0001; Midlands vs Upstate p<0.0001; Pee Dee vs Upstate p=0.0225).
- **Interpretation**: The authors read this as evidence of regional disparities in ADRD diagnosis linked to healthcare access, socioeconomic conditions, and rurality (Discussion) — an association, not a causal claim (see C07).
- **Dependencies**: none
- **Sources**:
  - 896 ← Figure 3 legend «896 - Pee Dee» [result]; also abstract «higher in the Pee Dee PHR (896 per 100,000)» [result]
  - 684 ← Figure 3 legend «684 - Midlands» [result]
  - "differed significantly across all PHRs (p < 0.05)" ← Results §"ADRD-specific incidence by PHRs" «The crude incidence of ADRD differed statistically significantly across all the PHRs (p < 0.05; Table 2)» [result]; Table 2 crude column all six p-values bolded [result]
- **Tags**: incidence, crude, regional-disparity, Poisson, ADRD

## C02: Alzheimer's disease (AD) incidence is highest in Pee Dee and significantly exceeds the other regions
- **Statement**: AD-specific incidence was highest in Pee Dee (727 per 100,000). Pairwise AD IRRs show Pee Dee significantly higher than Low Country (LC vs Pee Dee IRR 0.853, p<0.0001), Midlands (Midlands vs Pee Dee IRR 0.763, p<0.0001), and Upstate (Pee Dee vs Upstate IRR 1.111, p "<0.0002").
- **Status**: supported
- **Falsification criteria**: AD incidence not highest in Pee Dee, or one of the Pee Dee-vs-other AD comparisons is non-significant.
- **Proof**: [E03]
- **Evidence basis**: Figure 4 legend (Midlands 555, Low Country 620, Upstate 655, Pee Dee 727). Table 2 AD column: Pee Dee vs each other region significant and in the direction of higher Pee Dee incidence. (Note: Low Country vs Upstate AD IRR 0.947 is NOT significant, p=0.1402 — the two mid regions do not differ on AD.)
- **Interpretation**: Consistent with Pee Dee's rurality/social vulnerability and lower educational attainment (Discussion).
- **Dependencies**: C01
- **Sources**:
  - 727 ← Figure 4 legend «727 - Pee Dee» [result]; abstract «AD incidence was higher in the Pee Dee PHR (727 per 100,000)» [result]
  - Midlands vs Pee Dee AD IRR 0.763, p<0.0001 ← Table 2 AD column, row "Midlands vs. Pee Dee" «0.763 | <0.0001 (0.724–0.803)» [result]
  - Pee Dee vs Upstate AD IRR 1.111 ← Table 2 AD column, row "Pee Dee vs. Upstate" «1.111 | <0.0002 (1.058–1.167)» [result]
- **Tags**: Alzheimer, AD, incidence, Pee Dee, IRR

## C03: Vascular, Mixed, and "Other" dementia incidence is highest in Upstate (Other tied with Pee Dee)
- **Statement**: Among ADRD subtypes, Vascular dementia (VaD, 59 per 100,000) and Mixed dementia (24 per 100,000) incidence were highest in Upstate; "Other" dementia-type incidence was highest and tied in both Pee Dee and Upstate (102 per 100,000 each). Midlands vs Upstate is significant for VaD (IRR 0.642, p<0.0001) and Mixed (IRR 0.450, p<0.0001).
- **Status**: supported
- **Falsification criteria**: VaD or Mixed incidence not highest in Upstate, or the Midlands-vs-Upstate VaD/Mixed IRRs are non-significant.
- **Proof**: [E03]
- **Evidence basis**: Figure 5 (VaD: Midlands 38, Low Country 41, Pee Dee 50, Upstate 59), Figure 6 (Mixed: Midlands 11, Pee Dee 16, Low Country 18, Upstate 24), Figure 7 (Other: Midlands 80, Low Country 84, Pee Dee 102, Upstate 102). Table 2 Midlands-vs-Upstate: VaD IRR 0.642 (p<0.0001), Mixed IRR 0.450 (p<0.0001), both significant.
- **Interpretation**: The authors attribute higher Upstate VaD to a high cluster of healthcare facilities enabling more VaD diagnosis, plus cardiovascular risk factors (Discussion). Several subtype comparisons are non-significant (e.g., VaD LC vs Midlands p=0.7571; Mixed LC vs Pee Dee p=0.9524), so not all regional subtype contrasts differ.
- **Dependencies**: C01
- **Sources**:
  - VaD Upstate 59 ← Figure 5 legend «59 - Upstate» [result]; abstract «Vascular dementia (VaD) and Mixed dementia incidences were higher in the Upstate PHR» [result]
  - Mixed Upstate 24 ← Figure 6 legend «24 - Upstate» [result]
  - Other Pee Dee = Upstate = 102 ← Figure 7 legend «102 - Pee Dee», «102 - Upstate» [result]; Results §"ADRD incidence by PHR" «Incidence of other dementia types was highest in both the Pee Dee and Upstate regions (102 per 100,000)» [result]
  - Midlands vs Upstate Mixed IRR 0.450, p<0.0001 ← Table 2 Mixed column, row "Midlands vs. Upstate" «0.450 | <0.0001 (0.329–0.615)» [result]
- **Tags**: vascular-dementia, mixed-dementia, Upstate, subtype, IRR

## C04: The SCADR analytic cohort (N = 18,955) is predominantly AD, aged 75+, female, and White
- **Statement**: Of 18,955 analyzed registrants, 14,896 (78.59%) had an Alzheimer's disease diagnosis; the largest age group was 75–84 (6,755; 38.18%) with ≥85 next (6,194; 35.01%); 10,374 (58.96%) were female; and 12,537 (66.14%) were White individuals. Only 442 (2.33%) had Mixed dementia.
- **Status**: supported
- **Falsification criteria**: The reported composition percentages do not match the registry counts / Table 1.
- **Proof**: [E05]
- **Evidence basis**: Table 1 (overall column) and Figure 1 (N = 18,955). Abstract summarizes "about 38% between 75 and 84 years" and "about 79% had Alzheimer's (AD) diagnosis."
- **Interpretation**: Composition is a diagnosed-registry sample, not a population sample; the AD-dominant, older, female, White profile shapes the incidence estimates.
- **Dependencies**: none
- **Sources**:
  - N = 18,955 ← Figure 1 «n = 18,955» [result]; Methods «(N = 18,955; Figure 1)» [result]
  - AD 14,896 (78.59%) ← Table 1 row "Alzheimer's Disease", All-participants «14,896 (78.59)» [result]
  - 75–84 6,755 (38.18%) ← Table 1 row "75–84", All-participants «6,755 (38.18)» [result]
  - Female 10,374 (58.96%) ← Table 1 row "Female", All-participants «10,374 (58.96)» [result]
  - White 12,537 (66.14%) ← Table 1 row "White individuals", All-participants «12,537 (66.14)» [result]
- **Tags**: cohort, descriptive, demographics, SCADR

## C05: Age-stratified pattern — AD incidence rises with age and is consistently highest in Pee Dee among 65+, while VaD/Mixed are consistently highest in Upstate
- **Statement**: In each 65+ age band (65–74, 75–84, ≥85), AD incidence was highest in Pee Dee and VaD/Mixed incidence highest in Upstate; AD incidence rises steeply with age (e.g., Pee Dee AD: 388.184 at 65–74 → 1913.741 at 75–84 → 7955.116 at ≥85 per 100,000). Among registrants <65, AD, Mixed and Other were highest in Upstate and VaD highest in Pee Dee.
- **Status**: supported
- **Falsification criteria**: Table 3 shows a different region as highest for AD in any 65+ band, or the monotonic age gradient in AD incidence does not hold.
- **Proof**: [E04]
- **Evidence basis**: Table 3 and the Results §"Age-specific incidence" prose. Pee Dee AD by age band: 69.534 (<65), 388.184 (65–74), 1913.741 (75–84), 7955.116 (≥85). Upstate is highest for VaD and Mixed in every band.
- **Interpretation**: The authors emphasize the younger-than-65 Upstate/Pee Dee signal as a target for early screening. **Internal source discrepancy (reproduced, not corrected):** the Discussion states "higher incidence of AD, VaD, and Mixed dementia among participants younger than 65 years in the Pee Dee PHR," which contradicts Table 3 and the Results/Conclusion (where Upstate is highest for AD and Mixed among <65; only VaD is highest in Pee Dee for <65). Also, the 75–84 "Midlands lowest across all types" prose is not exact for AD and Other (Low Country is lower). See evidence/tables/table3.md.
- **Dependencies**: C02, C03
- **Sources**:
  - Pee Dee AD <65..≥85 = 69.534 / 388.184 / 1913.741 / 7955.116 ← Table 3 Pee Dee rows, AD column «69.534», «388.184», «1913.741», «7955.116» [result]
  - Upstate VaD ≥85 = 396.294 (highest) ← Table 3 Upstate "85 and above", VaD column «396.294» [result]
  - <65 AD highest Upstate 80.837 ← Table 3 Upstate "<65", AD column «80.837» [result]
- **Tags**: age-specific, age-adjustment, Table3, discrepancy

## C06: Missing region data are not completely at random, and complete-case analysis underestimates incidence by ~20.6% consistently across PHRs
- **Statement**: Missing county/zip data were associated with age-group (p < 0.0001, Cramér's V = 0.15), ADRD-specific diagnosis (p < 0.0001, Cramér's V = 0.12), and weakly with sex (p = 0.020, Cramér's V = 0.018), indicating data missing at random on those variables but not completely at random. A proportional-redistribution sensitivity analysis showed a consistent ~20.6% increase in incidence across all PHRs relative to complete-case analysis (i.e., complete-case underestimates incidence); extreme-case reassignment changed only Midlands and Pee Dee, leaving other PHRs stable.
- **Status**: supported
- **Falsification criteria**: The missingness associations are non-significant, or the sensitivity analyses do not show a consistent cross-PHR underestimation by complete-case analysis.
- **Proof**: [E06]
- **Evidence basis**: Sensitivity-analyses §. Supporting detail is in Supplementary Table 1 and Supplementary Figure 1 (online supplement; not in the provided PDF), but the in-text values are stated in the article body.
- **Interpretation**: The authors argue the primary PHR estimates are robust to missing-data assumptions, strengthening the regional-difference conclusion.
- **Dependencies**: C01
- **Sources**:
  - "~20.6% increase across all PHRs; complete case analyses underestimate the true incidence" ← Sensitivity analyses §, «The results showed a consistent increase of about 20.6% across all PHRs (complete case analyses underestimates the true incidence)» [result]
  - age-group p<0.0001, Cramér's V = 0.15; ADRD-diagnosis Cramér's V = 0.12 ← Sensitivity analyses §, «Missing data were associated with age-group (p < 0.0001) and ADRD specific diagnosis (p < 0.0001) with small to moderate effect sizes (Cramer's V = 0.15 and 0.12, respectively)» [result]
  - sex p = 0.020, Cramér's V = 0.018 ← Sensitivity analyses §, «Missingness was weakly associated with sex (p = 0.020, Cramer's V = 0.018)» [result]
- **Tags**: missing-data, sensitivity-analysis, robustness, Cramers-V

## C07: Regional ADRD-incidence differences reflect (associational) disparities in healthcare access, socioeconomic conditions, and rurality
- **Statement**: The observed regional differences in ADRD incidence are consistent with, and interpreted by the authors as reflecting, disparities in healthcare access, socioeconomic conditions, and rural/urban factors (e.g., Pee Dee's highest social vulnerability index and rurality; Upstate's dense healthcare facilities driving VaD diagnosis).
- **Status**: hypothesis
- **Falsification criteria**: This is an interpretive association; it would be undermined if regional incidence differences did not track social-vulnerability/rurality indicators, or if a controlled analysis attributed the differences to other factors. The study cannot establish causation (explicitly stated).
- **Proof**: [E01, E02, E03]
- **Evidence basis**: Discussion synthesis linking findings to social vulnerability index (ref 10), rurality (ref 26 OMB), education/teacher shortages (refs 31, 32), cardiovascular risk / stroke belt (refs 36, 37), and healthcare-access reviews (refs 55, 56). No individual-level confounders (education, lifestyle, environment) were measured.
- **Interpretation**: Authors explicitly caution ("Findings... should be interpreted with caution as this is an observational study and is not intended to establish causal associations").
- **Dependencies**: C01, C02, C03
- **Sources**:
  - causation caveat ← Conclusion, «Findings in this research should be interpreted with caution as this is an observational study and is not intended to establish causal associations» [result]
  - Pee Dee highest social vulnerability index ← Introduction, «The Pee Dee PHR has the highest social vulnerability index... and lack of access to transportation and housing community (10)» [input]
- **Tags**: interpretation, disparities, social-vulnerability, rurality, observational
