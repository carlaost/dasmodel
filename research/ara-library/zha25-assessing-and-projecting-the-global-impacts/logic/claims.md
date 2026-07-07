# Claims

All numeric values are copied exactly from the source (abstract, running text, or Table 1), with
their original precision preserved even where abstract/body-text/table precision disagree. A
change or comparison is treated as "significant" per the paper's own convention: a 95% CI/UI that
excludes zero, or (for group comparisons) a stated "significant"/"highly significant" p-value.
Each `**Sources**` entry cites a location whose verbatim quoted text contains the value. Several
of this paper's own numbers are internally inconsistent (duplicated across variables, or differ
between abstract/body-text precision); these are preserved verbatim and catalogued in
`logic/solution/constraints.md` rather than silently corrected (Rule 10).

## C01: Global AD burden (DALYs, deaths, incidence) declined 1990–2021 and is projected to keep declining 2022–2030
- **Statement**: Global age-standardized EAPC for DALYs was −1.5552 (95% CI −1.6338, −1.4765) for
  1990–2021 and is projected at −1.4375 (95% CI −1.4548, −1.4201) for 2022–2030. The death-rate
  EAPC was −1.5340 (−1.6420, −1.4259) for 1990–2021, projected −1.7982 (−1.8254, −1.7711) for
  2022–2030. The incidence-rate EAPC was −1.5811 (−1.6515, −1.5106) for 1990–2021, projected
  −1.2718 (−1.2854, −1.2583) for 2022–2030. All six values are negative with 95% CIs excluding
  zero. In 1990 the DALY ASR was 644.16 (95% UI 640.90, 647.43), projected to fall to 299.92
  (274.94, 324.91) by 2030; the death rate in 1990 was 14,775.89 (14,760.61, 14,791.18), projected
  to 7,210.92 (6,730.65, 7,691.19) by 2030; the incidence rate in 1990 was 4,483.76 (4,475.36,
  4,492.18), projected to 2,199.67 (2,054.49, 2,344.86) by 2030.
- **Status**: supported
- **Falsification criteria**: A re-run GBD-2021-based EAPC calculation for the Global aggregate
  yielding a positive (rising) EAPC for any of DALYs/deaths/incidence in either window, or a 95%
  CI/UI that includes zero.
- **Proof**: [E01]
- **Evidence basis**: Table 1, Global row; Results §3.1, p.3; Abstract.
- **Interpretation**: The paper attributes the projected decline to advances in early detection,
  screening, pharmacological/non-pharmacological interventions, and public awareness — this
  attribution is discussion-level narrative, not separately tested by the study's own data.
- **Dependencies**: none
- **Tags**: global-trend, EAPC, DALY, mortality, incidence, projection
- **Sources**:
  - DALYs EAPC 1990–2021 −1.5552 (−1.6338,−1.4765); 2022–2030 −1.4375 (−1.4548,−1.4201) ← evidence/tables/table1.md, Global row «−1.5552 (−1.6338, −1.4765) | −1.4375 (−1.4548, −1.4201)» [result]
  - Deaths EAPC 1990–2021 −1.5340 (−1.6420,−1.4259); 2022–2030 −1.7982 (−1.8254,−1.7711) ← evidence/tables/table1.md, Global row «−1.5340 (−1.6420, −1.4259) | −1.7982 (−1.8254, −1.7711)» [result]
  - Incidence EAPC 1990–2021 −1.5811 (−1.6515,−1.5106); 2022–2030 −1.2718 (−1.2854,−1.2583) ← evidence/tables/table1.md, Global row «−1.5811 (−1.6515, −1.5106) | −1.2718 (−1.2854, −1.2583)» [result]
  - rounded confirmation ← Results §3.1, p.3 «The EAPC for DALYs shows a decrease of −1.56 (95% CI: −1.63, −1.48) from 1990 to 2021 and a projected EAPC of −1.44 (95% CI: −1.45, −1.42) from 2022 to 2030» [result]
  - 1990 DALY ASR 644.16 (640.90,647.43) → 2030 299.92 (274.94,324.91); 1990 death rate 14775.89 (14760.61,14791.18) → 2030 7210.92 (6730.65,7691.19); 1990 incidence 4483.76 (4475.36,4492.18) → 2030 2199.67 (2054.49,2344.86) ← Results §3.1, p.3 «In 1990, the DALYs for ASR were 644.16 (95% UI: 640.90, 647.43), with a projected decrease to 299.92 (95% UI: 274.94, 324.91) by 2030. The death rate in 1990 was 14775.89 … 7210.92 … the incidence rate in 1990 stood at 4483.76 … 2199.67 …» [result]

## C02: Projected 2022–2030 decline holds for both sexes, but the paper prints an identical EAPC for female incidence and female deaths
- **Statement**: The global projected (2022–2030) death-rate EAPC is −2.28 (95% CI −2.32, −2.23)
  for males and −1.03 (−1.04, −1.02) for females. The global projected incidence-rate EAPC is
  −1.73 (−1.75, −1.70) for males and −1.03 (−1.04, −1.02) for females — printed identically to the
  female death-rate EAPC just above. In 2030 the age-standardized death rate is 6,786.66 (95% UI
  6,401.84, 7,171.47) for males vs. 6,751.16 (6,389.90, 7,112.42) for females; DALY rate 289.55
  (269.55, 309.55) for males vs. 298.85 (279.72, 317.97) for females; incidence rate 2,009.00
  (1,895.67, 2,122.33) for males vs. 1,947.26 (1,843.42, 2,051.10) for females.
- **Status**: supported (declines in both sexes) / **flagged** (the identical male-EAPC-distinct,
  female-EAPC-identical pattern between incidence and deaths is an unresolved internal
  inconsistency — see Interpretation).
- **Falsification criteria**: A re-run analysis showing female incidence EAPC materially different
  from female death-rate EAPC (which the paper's own male figures, −1.73 vs −2.28, show should be
  expected — male incidence and death EAPCs differ substantially, so identical female values for
  two distinct measures is inherently suspect).
- **Proof**: [E02]
- **Evidence basis**: Results §3.2, p.3 (and identically worded in the Abstract).
- **Interpretation**: The paper offers biological/social explanations (estrogen's protective
  effect, sex-specific lifestyle and healthcare-seeking differences) for the male–female EAPC gap
  in Discussion, p.7. However, the fact that female incidence and female death-rate EAPCs are
  printed as the exact same value (−1.03, 95% CI −1.04 to −1.02) — while the corresponding male
  values differ sharply (−1.73 vs −2.28) — is not addressed by the authors and reads as a probable
  copy/transcription duplication rather than a genuine finding; treated here as an unresolved
  data-quality flag, not silently corrected (Rule 10).
- **Dependencies**: C01
- **Tags**: sex-difference, EAPC, projection, data-quality-flag
- **Sources**:
  - male death EAPC −2.28 (−2.32,−2.23); female death EAPC −1.03 (−1.04,−1.02) ← Results §3.2, p.3 «The global EAPC for males is −2.28 (95% CI: −2.32, −2.23) and for females is −1.03 (95% CI: −1.04, −1.02)» [result]
  - male incidence EAPC −1.73 (−1.75,−1.70); female incidence EAPC −1.03 (−1.04,−1.02) ← Results §3.2, p.3 «the incidence rates for both sexes also exhibit a decrease, with the EAPC for males at −1.73 (95% CI: −1.75, −1.70) and for females at −1.03 (95% CI: −1.04, −1.02)» [result]
  - 2030 ASRs by sex (death, DALY, incidence) ← Results §3.2, p.3 «the age-standardized death rate for males was 6786.66 … 6751.16 … The age-standardized DALY rate for males was 289.55 … 298.85 … the age-standardized incidence rate for males in 2030 was 2009.00 … 1947.26 …» [result]

## C03: Andean/Southern Latin America and the Caribbean have the highest projected 2022–2030 DALY EAPC; Eastern/Central Europe and East Asia the lowest
- **Statement**: Regions with the highest positive (rising) projected DALY EAPC are Andean Latin
  America 0.94 (95% CI 0.93, 0.94), Southern Latin America 0.77 (0.76, 0.77), and the Caribbean
  0.59 (0.59, 0.60); Central Latin America 0.51 (0.51, 0.51) and Oceania 0.39 (0.39, 0.39) are also
  positive. Regions with the lowest (most negative) projected DALY EAPC are Eastern Europe −16.31
  (−18.60, −13.95), Central Europe −12.03 (−13.26, −10.78), and East Asia −2.77 (−2.83, −2.70);
  Southeast Asia −2.29 (−2.34, −2.25) and Western Europe −2.12 (−2.16, −2.08) also negative.
- **Status**: supported
- **Falsification criteria**: A re-run GBD-2021-based projection in which a different region holds
  the maximum or minimum 2022–2030 DALY EAPC, or any listed region's 95% CI including 0.
- **Proof**: [E03]
- **Evidence basis**: Table 1 (DALYs, 2022–2030 column, all 18 GBD regions); Results §3.3, p.5;
  Figure 1 panel C.
- **Interpretation**: The paper attributes rising-burden regions to urbanization/lifestyle
  modification and healthcare-access/diagnostic-delay challenges, and falling-burden regions to
  advanced healthcare systems and risk-factor management (Discussion, p.8) — interpretive, not
  separately tested.
- **Dependencies**: C01
- **Tags**: region-ranking, EAPC, DALY, projection
- **Sources**:
  - Andean Latin America 0.9371 (0.9298,0.9445); Southern Latin America 0.7651 (0.7602,0.7700); Caribbean 0.5931 (0.5902,0.5961); Central Latin America 0.5100 (0.5078,0.5122) ← evidence/tables/table1.md rows «Andean Latin America … 0.9371 (0.9298, 0.9445)»; «Southern Latin America … 0.7651 (0.7602, 0.7700)»; «Caribbean … 0.5931 (0.5902, 0.5961)»; «Central Latin America … 0.5100 (0.5078, 0.5122)» [result]
  - Eastern Europe −16.3071 (−18.6030,−13.9464); Central Europe −12.0323 (−13.2652,−10.7819); East Asia −2.7709 (−2.8354,−2.7064) ← evidence/tables/table1.md rows «Eastern Europe … −16.3071 (−18.6030, −13.9464)»; «Central Europe … −12.0323 (−13.2652, −10.7819)»; «East Asia … −2.7709 (−2.8354, −2.7064)» [result]
  - rounded confirmation of both extremes ← Results §3.3, p.5 «Andean Latin America has the highest EAPC at 0.94 … Eastern Europe shows the lowest EAPC at −16.31 (95% CI: −18.60, −13.95), followed by Central Europe at −12.03 …, and East Asia at −2.77 …» [result]

## C04: Central/Eastern/Southern Sub-Saharan Africa and Oceania have the highest projected 2030 DALY ASR; Eastern/Central Europe and High-income Asia Pacific the lowest
- **Statement**: In 2030, the highest projected DALY ASRs are Central Sub-Saharan Africa 22,703.53
  (95% UI 21,500.55, 23,906.51), Eastern Sub-Saharan Africa 15,299.70 (14,724.70, 15,874.71),
  Oceania 13,522.19 (12,900.14, 14,144.24), and Southern Sub-Saharan Africa 13,477.61 (12,428.99,
  14,526.24). The lowest are Eastern Europe 1,404.84 (0.05, 3,014.43), Central Europe 1,872.69
  (330.75, 3,414.64), High-income Asia Pacific 4,365.22 (4,190.62, 4,539.83), Western Europe
  4,555.77 (3,986.67, 5,124.87), and Australasia 4,581.69 (4,256.90, 4,906.48).
- **Status**: supported
- **Falsification criteria**: A re-run projection yielding a different region for the maximum or
  minimum 2030 DALY ASR, or values materially outside the stated UIs.
- **Proof**: [E03]
- **Evidence basis**: Results §3.3, p.5 (values are cited to Supplementary Tables 2, 5 which were
  not part of the provided input — see `evidence/README.md`); qualitatively visible in Figure 2
  panel C (Central Sub-Saharan Africa tallest bar, Eastern Europe shortest).
- **Interpretation**: The paper frames the Sub-Saharan African maxima as reflecting socio-economic
  challenges, political instability, and limited healthcare resources (Discussion, p.8) and the
  European/Asia-Pacific minima as reflecting robust healthcare infrastructure — interpretive.
- **Dependencies**: C01
- **Tags**: region-ranking, ASR, DALY, projection
- **Sources**:
  - Central Sub-Saharan Africa 22703.53 (21500.55,23906.51); Eastern Sub-Saharan Africa 15299.70 (14724.70,15874.71); Oceania 13522.19 (12900.14,14144.24); Southern Sub-Saharan Africa 13477.61 (12428.99,14526.24) ← Results §3.3, p.5 «Central Sub-Saharan Africa is expected to have the highest ASR at 22703.53 (95% UI: 21500.55, 23906.51), followed by Eastern Sub-Saharan Africa at 15299.70 … and Oceania at 13522.19 … Southern Sub-Saharan Africa also exhibits a high ASR of 13477.61 …» [result]
  - Eastern Europe 1404.84 (0.05,3014.43); Central Europe 1872.69 (330.75,3414.64); High-income Asia Pacific 4365.22 (4190.62,4539.83); Western Europe 4555.77 (3986.67,5124.87); Australasia 4581.69 (4256.90,4906.48) ← Results §3.3, p.5 «Eastern Europe has the lowest ASR at 1404.84 (95% Uncertainty Interval [UI]: 0.05, 3014.43), followed by Central Europe at 1872.69 …, and High-income Asia Pacific at 4365.22 … Western Europe and Australasia exhibit low ASRs of 4555.77 … and 4581.69 …» [result]

## C05: Cyprus, Serbia, and Montenegro have the highest projected country-level DALY EAPC; Bahrain, Armenia, and Qatar the lowest
- **Statement**: Countries with the highest positive projected (2022–2030) DALY EAPC are Cyprus
  12.55 (95% CI 11.21, 13.91), Serbia 9.64 (8.85, 10.43), and Montenegro 5.16 (4.93, 5.38); Andorra
  5.11 (4.89, 5.33) and Cuba 4.95 (4.74, 5.15) also positive. The lowest are Bahrain −87.28 (95% CI
  −94.66, −69.69), Armenia −85.40 (−92.80, −70.41), and Qatar −85.39 (−93.13, −68.92); Romania
  −84.49 (−92.08, −69.66) and Guatemala −78.37 (−90.61, −50.17) also strongly negative.
- **Status**: supported
- **Falsification criteria**: A re-run projection with a different country holding the maximum or
  minimum 2022–2030 DALY EAPC.
- **Proof**: [E04]
- **Evidence basis**: Results §3.4, p.6 (cited to Supplementary Tables 6, 8 / Supplementary Figure
  1, not part of the provided input). The Abstract restates Cyprus/Serbia/Bahrain/Armenia at
  slightly different precision (Serbia 9.6416 vs 9.64; Armenia −85.41 vs −85.40 and UI −69.70 vs
  −69.69) — same quantities, differing rounding; both reproduced verbatim (see
  `logic/solution/constraints.md`).
- **Interpretation**: The paper attributes rising-EAPC countries to aging populations, dietary
  shift, and diagnostic/resource-allocation challenges, and falling-EAPC countries to robust
  healthcare infrastructure and health literacy (Discussion, p.8) — interpretive, not tested here.
- **Dependencies**: C03
- **Tags**: country-ranking, EAPC, DALY, projection
- **Sources**:
  - Cyprus 12.55 (11.21,13.91); Serbia 9.64 (8.85,10.43); Montenegro 5.16 (4.93,5.38); Andorra 5.11 (4.89,5.33); Cuba 4.95 (4.74,5.15) ← Results §3.4, p.6 «Cyprus leads with an EAPC of 12.55 (95% CI: 11.21, 13.91), followed by Serbia at 9.64 …, and Montenegro at 5.16 … Andorra and Cuba also exhibit positive EAPCs of 5.11 … and 4.95 …» [result]
  - Bahrain −87.28 (−94.66,−69.69); Armenia −85.40 (−92.80,−70.41); Qatar −85.39 (−93.13,−68.92); Romania −84.49 (−92.08,−69.66); Guatemala −78.37 (−90.61,−50.17) ← Results §3.4, p.6 «Bahrain has the lowest EAPC at −87.28 (95% CI: −94.66, −69.69), followed by Armenia at −85.40 …, and Qatar at −85.39 … Romania and Guatemala also demonstrate negative EAPCs of −84.49 … and −78.37 …» [result]
  - abstract-precision variants ← Abstract, p.1 «Cyprus and Serbia with the highest positive EAPCs for DALYs at 12.55 (95% UI: 11.21, 13.91) and 9.6416 (95% CI: 8.86, 10.4333) … Bahrain and Armenia exhibit significant negative EAPCs at −87.28 (95% CI: −94.66, −69.70) and −85.41 (95% CI: −92.80, −70.41)» [result]

## C06: Cyprus and North Macedonia have the highest projected 2030 country DALY ASR; the five lowest countries are all floored at 0.05
- **Statement**: The highest projected 2030 DALY ASRs are Cyprus 296,472.95 (95% UI 127,878.51,
  465,067.40), North Macedonia 260,543.83 (202,167.92, 318,919.74), and the United Arab Emirates
  82,789.36 (79,632.65, 85,946.07); Eswatini 52,861.67 (49,104.71, 56,618.63) and the Central
  African Republic 52,156.45 (47,941.08, 56,371.83) also high. The five lowest — Armenia, Bulgaria,
  Romania, Guatemala, and Bahrain — are all printed with an identical point estimate of 0.05, with
  upper 95% UI bounds of 1,653.38, 54,018.61, 2,897.19, 4,016.29, and 12,522.80 respectively.
- **Status**: supported (as printed) / **flagged** (five countries sharing an identical point
  estimate to two decimal places, each with a very different and very wide upper UI, indicates the
  point projection is floored/degenerate for these low-count countries rather than a genuine
  shared value).
- **Falsification criteria**: A re-run projection in which the minimum-ASR countries do not show
  this floor-value pattern, or in which a different country holds the 2030 maximum DALY ASR.
- **Proof**: [E04]
- **Evidence basis**: Results §3.4, p.6 (cited to Supplementary Tables 7, 9 / Supplementary Figure
  1, not part of the provided input).
- **Interpretation**: The uniform 0.05 floor plausibly reflects a GAM/EAPC projection artifact for
  countries with very small or sparse AD case counts (consistent with the paper's own
  data-availability limitation, see `logic/solution/constraints.md` L2), rather than five
  countries independently converging on the same burden level.
- **Dependencies**: C05
- **Tags**: country-ranking, ASR, DALY, projection, data-quality-flag
- **Sources**:
  - Cyprus 296472.95 (127878.51,465067.40); North Macedonia 260543.83 (202167.92,318919.74); UAE 82789.36 (79632.65,85946.07); Eswatini 52861.67 (49104.71,56618.63); Central African Republic 52156.45 (47941.08,56371.83) ← Results §3.4, p.6 «Cyprus is expected to have the highest ASR at 296472.95 … followed by North Macedonia at 260543.83 …, and the United Arab Emirates at 82789.36 … Eswatini and the Central African Republic also exhibit high ASRs of 52861.67 … and 52156.45 …» [result]
  - Armenia/Bulgaria/Romania/Guatemala/Bahrain all 0.05 (upper UIs 1653.38/54018.61/2897.19/4016.29/12522.80) ← Results §3.4, p.6 «Armenia records the lowest ASR at 0.05 (95% UI: 0.05, 1653.38), followed by Bulgaria at 0.05 (95% UI: 0.05, 54018.61), and Romania at 0.05 (95% UI: 0.05, 2897.19). Guatemala and Bahrain also display low ASRs of 0.05 (95% UI: 0.05, 4016.29) and 0.05 (95% UI: 0.05, 12522.80)» [result]

## C07: In 2030, countries at or above SDI 0.8 (and, separately, 0.7) show significantly higher ASIR, ASDR, and DALY ASR than countries below the threshold; the five-tier SDI breakdown is monotonic
- **Statement**: In 2030, countries with SDI ≥0.8 show notably higher ASIR, ASDR, and
  age-standardized DALY rate than countries with SDI <0.8; the same pattern holds at an SDI
  threshold of 0.7. Across the five SDI categories (low, low-middle, middle, high-middle, high),
  high-SDI regions show the highest ASIR/ASDR/DALY values and low-SDI regions the lowest, with all
  comparisons described as demonstrating "highly significant p-values."
- **Status**: supported (direction and significance qualifier as stated) — exact p-values, test
  statistics, and group Ns are **not specified in paper** (deferred to Supplementary Figures 2–4,
  not part of the provided input).
- **Falsification criteria**: A re-run Mann-Whitney U (or equivalent) comparison in which the
  high-SDI group does not show significantly higher 2030 ASIR/ASDR/DALY ASR than the low-SDI
  group at either threshold, or in which the five-category breakdown is non-monotonic.
- **Proof**: [E05]
- **Evidence basis**: Results §3.5, p.6.
- **Interpretation**: The paper attributes the higher high-SDI burden to longer life expectancy,
  improved diagnosis/reporting, and urbanization/lifestyle factors, while noting low-SDI regions
  may be underestimated due to underdiagnosis (Discussion, p.9) — interpretive.
- **Dependencies**: none
- **Tags**: SDI, threshold-comparison, Mann-Whitney, significance
- **Sources**:
  - SDI ≥0.8 vs <0.8 ← Results §3.5, p.6 «In 2030, countries with a SDI of 0.8 or higher exhibit notably higher values in ASIR, ASDR, and age-standardized DALY rate compared to countries with an SDI below 0.8» [result]
  - SDI ≥0.7 vs <0.7 ← Results §3.5, p.6 «when using an SDI threshold of 0.7, the same patterns emerge, with higher SDI categories showing significantly higher ASIR, ASDR, and age-standardized DALY rates» [result]
  - five-category breakdown, "highly significant p-values" ← Results §3.5, p.6 «High-SDI regions show the highest values for ASIR, ASDR, and age-standardized DALY rates, while low-SDI regions have the lowest values. All comparisons demonstrate highly significant p-values» [result]

## C08: Oceania shows the strongest SDI–burden correlation across all three measures; Africa the weakest for ASIR — but two of the reported (R², p) pairs are exact duplicates of each other
- **Statement**: By continent, SDI-vs-ASIR correlation: Oceania R²=0.203, p=0.0463; Africa
  R²=0.008, p=0.0699; America R²=0.088, p=0.0699; Asia R²=0.055, p=0.1093. SDI-vs-ASDR: Oceania
  R²=0.144, p=0.0984; America R²=0.091, p=0.0652; Africa R²=0.099, p=0.0539 (Asia, Europe not given
  numerically). SDI-vs-DALY: Oceania R²=0.204, p=0.0459; America R²=0.099, p=0.0539 (Africa, Asia,
  Europe not given numerically). Oceania is the only continent with a p<0.05 result for both ASIR
  (p=0.0463) and DALY (p=0.0459); all other reported continent correlations have p≥0.05.
- **Status**: supported (direction/ranking as stated) / **flagged**: the ASIR p-values for Africa
  and America are printed as an identical 0.0699 despite very different R² (0.008 vs 0.088), and
  the (R²=0.099, p=0.0539) pair is printed twice — once for Africa's ASDR correlation and again,
  identically, for America's DALY correlation. Reproduced verbatim; not corrected (Rule 10).
- **Falsification criteria**: A re-run continent-stratified linear regression of SDI on
  ASIR/ASDR/DALY ASR in which Oceania is not the strongest correlation, or in which the flagged
  duplicate (R², p) pairs resolve to genuinely distinct values.
- **Proof**: [E06]
- **Evidence basis**: Results §3.5, pp.6–7; Discussion, p.7 (restates Oceania-strongest,
  Africa-weakest framing).
- **Interpretation**: The paper interprets Oceania's correlation as showing "improved longevity and
  healthcare access contribute to a higher prevalence" and Africa's near-zero correlation as
  showing "socio-economic advancements alone are insufficient" given healthcare-infrastructure and
  cultural factors (Discussion, p.9) — interpretive framing built on statistics that include at
  least two duplicate-value instances (see Interpretation above).
- **Dependencies**: C07
- **Tags**: SDI, correlation, continent, data-quality-flag
- **Sources**:
  - ASIR correlations (Oceania, Africa, America, Asia) ← Results §3.5, pp.6–7 «Oceania exhibits the highest correlation with an R2 of 0.203 and a p-value of 0.0463 … Africa demonstrates a negligible correlation (R2 = 0.008, p = 0.0699) … America (R2 = 0.088, p = 0.0699) and Asia (R2 = 0.055, p = 0.1093)» [result]
  - ASDR correlations (Oceania, America, Africa) ← Results §3.5, p.7 «Oceania exhibits a moderate correlation with an R2 of 0.144 and a p-value of 0.0984 … America shows a weak correlation (R2 = 0.091, p = 0.0652) … Africa, for instance, has an R2 of 0.099 and a p-value of 0.0539» [result]
  - DALY correlations (Oceania, America) ← Results §3.5, p.7 «The age-standardized DALY rate in Oceania shows a notable correlation, with an R2 of 0.204 and a p-value of 0.0459 … America displaying a weak correlation (R2 = 0.099, p = 0.0539)» [result]
