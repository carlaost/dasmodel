# Claims

All numbers are copied exactly from paper.pdf (main text; the paper also references a separate Supplementary Material file — Table S1-S3, Figure S1-S7 — which was not provided as input and could not be independently verified against a table/figure; where a claim relies on such a supplementary object, this is noted and the claim is grounded only in the main-text sentence that reports the number). Values reporting the study's own GBD-derived results are tagged `[result]`; values that are pre-specified methodological parameters (SDI quintile cut-points, formulas) are tagged `[input]`.

## C01: Global 2021 ADOD burden: 9.84 million incident cases, 1.95 million deaths, 36.33 million DALYs
- **Statement**: Globally in 2021, ADOD caused 9.84 million incident cases (9837.06×10³, 95% UI 8620.52-11163.70; ASIR 119.76 per 100,000, 95% UI 104.96-135.89), 1.95 million deaths (1952.68×10³, 95% UI 512.98-4984.74, of which 67.9% occurred in females), and 36.33 million DALYs.
- **Status**: supported
- **Falsification criteria**: Disproved if the Abstract's headline 2021 figures (9.84 million cases, 1.95 million deaths, 36.33 million DALYs) differ from the Results section's more precise incidence/death figures, or if Table 1's 2021 "Overall" row does not match the Abstract's incidence figure.
- **Proof**: [E01]
- **Evidence basis**: Abstract ("Globally, 9.84 million cases of ADOD occurred in 2021, with 1.95 million ADOD-related deaths, causing 36.33 million DALYs.") and §Results "Incidence of Alzheimer's disease and other dementias" / "Mortality and DALYs of ADOD".
- **Interpretation**: The 2021 incidence figure (9.84M) is precisely reproduced in Table 1's "Overall" row (9837.06×10³), confirming internal consistency between the Abstract and the main results table; the death and DALY figures rely on Table S1 (supplementary, not provided) for their fuller breakdown but the headline numbers themselves are stated directly in the main-text Results.
- **Dependencies**: none
- **Sources**:
  - 9.84 million incident cases, 1.95 million deaths, 36.33 million DALYs ← paper.pdf Abstract "Globally, 9.84 million cases of ADOD occurred in 2021, with 1.95 million ADOD-related deaths, causing 36.33 million DALYs." [result]
  - 9837.06×10³ (8620.52,11163.70) incident cases; ASIR 119.76 (104.96,135.89) ← paper.pdf §Results "In 2021, the number of global incident cases of ADOD was 9837.06 × 103 (95%UI: 8620.52, 11163.70) for both sexes and all ages, and an age‐standardized rate of 119.76 (104.96,135.89) per 100,000 (Table 1)." [result]
  - Same figures independently confirmed in Table 1 "Overall" row, 2021 columns: "9837.06(8620.52,11163.7)" and "119.76(104.96,135.89)" ← `evidence/tables/table1.md` row "Overall". [result]
  - 1952.68×10³ (512.98,4984.74) deaths, 67.9% female ← paper.pdf §Results "The number of death cases of ADOD was 1952.68 × 103 (512.98, 4984.74) in 2021 globally, of which 67.9% occurred in females, and the high SDI region contributed the most (Table S1)." [result] — Table S1 itself is supplementary material not provided with this input; the number is grounded in the main-text sentence, not independently cross-checked against a table.
- **Tags**: headline-burden, 2021, GBD-2021

## C02: Global ADOD incidence rose slightly 1990-2021, but SDI-region trajectories diverged (only high-middle and middle SDI rose)
- **Statement**: The global both-sex age-standardized incidence rate (ASIR) increased from 116.97(102.77,132.32) per 100,000 in 1990 to 119.76(104.96,135.89) in 2021, an AAPC of 0.06(0.05,0.07). Every SDI region saw a decrease in ASIR over 1990-2021 except the high-middle SDI region (AAPC 0.32, 95%CI 0.27-0.38) and the middle SDI region (0.26, 95%CI 0.19-0.33).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 1's 1990/2021 ASIR values or Table 2's Global/High-middle/Middle SDI "Overall" AAPC rows differ from these figures, or if any SDI region other than high-middle/middle shows a positive 1990-2021 ETPC in Table 1.
- **Proof**: [E02]
- **Evidence basis**: §Results "Incidence of Alzheimer's disease and other dementias" ("From 1990 to 2021, the global both-sex age‐standardized incidence rate increased from 116.97(102.77,132.32) to 119.76(104.96,135.89), with an AAPC of 0.06(0.05,0.07) (Table 2 and Fig. 1). Every SDI region saw a decrease in their ASIRs, with the exception of high-middle (AAPC: 0.32,95%CI: 0.27,0.38) and middle SDI (0.26[0.19,0.33]) regions.").
- **Interpretation**: The global AAPC (+0.06) masks a bifurcated regional pattern: Table 1's 1990-2021 ETPC of ASIR is negative for High SDI (−3.6), Low-middle SDI (−3.08), and Low SDI (−4.4), but positive for High-middle SDI (+11.84) and Middle SDI (+9.29) — the two "middle-development" SDI tiers are driving essentially all of the net global increase.
- **Dependencies**: C01
- **Sources**:
  - Global ASIR 1990→2021, AAPC ← paper.pdf §Results "the global both-sex age‐standardized incidence rate increased from 116.97(102.77,132.32) to 119.76(104.96,135.89), with an AAPC of 0.06(0.05,0.07) (Table 2 and Fig. 1)." [result]
  - High-middle SDI AAPC 0.32(0.27,0.38), Middle SDI AAPC 0.26(0.19,0.33), as the sole risers ← paper.pdf §Results "Every SDI region saw a decrease in their ASIRs, with the exception of high-middle (AAPC: 0.32,95%CI: 0.27,0.38) and middle SDI (0.26[0.19,0.33]) regions." [result]
  - Table 2 confirms Global ASIR Overall EAPC = 0.06*(0.05,0.07); High-middle SDI ASIR Overall = 0.32*(0.27,0.38); Middle SDI ASIR Overall = 0.26*(0.19,0.33) ← `evidence/tables/table2.md` rows "Global/Overall", "High-middle SDI/Overall", "Middle SDI/Overall". [result]
  - Table 1 ETPC signs: High SDI −3.6(−5.27,−2.08), High-middle SDI +11.84(10.26,13.07), Middle SDI +9.29(7.14,10.88), Low-middle SDI −3.08(−3.94,−2.38), Low SDI −4.4(−5.35,−3.51) ← `evidence/tables/table1.md` "SDI region" rows, "1990-2021 ETPC of ASIR" column. [result]
- **Tags**: incidence-trend, joinpoint, SDI-region, AAPC

## C03: Female ASIR exceeds male ASIR globally (male:female ratio 0.78); highest/lowest ASIR by SDI and GBD region, with regional rank reversal
- **Statement**: Globally the ASIR was significantly higher in females than males (male-to-female ratio 0.78). By SDI region, the highest 2021 ASIR was 132.40(115.43,150.85) per 100,000 in the high-middle SDI region and the lowest was 90.89(79.00,103.12) in the low SDI region. By GBD region, East Asia had the highest 2021 ASIR (149.61, 95%UI 129.58-171.14) and Western Sub-Saharan Africa the lowest (73.18, 95%UI 63.36-83.46). Of the 21 regions, high-income North America ranked 1st in 1990 but only 3rd in 2021, while East Asia rose from 7th in 1990 to 1st in 2021.
- **Status**: supported
- **Falsification criteria**: Disproved if the male:female ASIR ratio differs from 0.78, if Table 1's 2021 ASIR values for high-middle SDI/low SDI/East Asia/Western Sub-Saharan Africa differ from the stated figures, or if the 1990-to-2021 regional rank order for high-income North America/East Asia differs from 1st→3rd / 7th→1st.
- **Proof**: [E01]
- **Evidence basis**: §Results "Incidence of Alzheimer's disease and other dementias" (male:female ratio, SDI/region extremes) and following paragraph (regional rank shifts).
- **Interpretation**: The rank reversal (East Asia 7th→1st, high-income North America 1st→3rd) is directionally consistent with C02's finding that high-middle/middle SDI regions are the ones with rising ASIR while historically-highest-ASIR high-SDI regions decline — East Asia is GBD-classified largely within the high-middle SDI tier for this period.
- **Dependencies**: C01, C02
- **Sources**:
  - male-to-female ratio 0.78 ← paper.pdf §Results "Globally, the ASIR was significantly higher in females than in males, with a male-to-female ratio of 0.78." [result]
  - highest ASIR 132.40(115.43,150.85) in high-middle SDI, lowest 90.89(79.00,103.12) in low SDI ← paper.pdf §Results "The highest ASIR was 132.40(115.43,150.85) per 100,000 in the high-middle SDI region whereas the lowest rate was in low SDI area at 90.89(79.00,103.12) per 100,000." [result]
  - East Asia highest 149.61(129.58,171.14), Western Sub-Saharan Africa lowest 73.18(63.36,83.46) ← paper.pdf §Results "Regionally, East Asia had the highest ASIR at 149.61(129.58,171.14), while Western Sub-Saharan Africa had the lowest (73.18[63.36,83.46]), as shown in Table 1." [result]
  - Table 1 confirms: High-middle SDI 2021 ASIR = 132.4(115.43,150.85); Low SDI 2021 ASIR = 90.89(79,103.12); East Asia 2021 ASIR = 149.61(129.58,171.14); Western Sub-Saharan Africa 2021 ASIR = 73.18(63.36,83.46) ← `evidence/tables/table1.md`. [result]
  - regional rank shift: "high-income North America ranked 1st in 1990 and 3rd in 2021... East Asia ranked rose from 7th to 1st in 2021" ← paper.pdf §Results "Of the 21 regions, high-income North America ranked 1 st in 1990 and 3rd in 2021 for ASIR of ADOD, while conversely, East Asia ranked rose from 7 th to 1 st in 2021." [result]
- **Tags**: sex-difference, regional-ranking, SDI-region, ASIR

## C04: At the 204-country level, China/USA/India have the highest incident-case counts; 152/204 countries exceed ASIR 100
- **Statement**: Among 204 countries/territories in 2021, China (SDI=0.722) has the highest number of ADOD incident cases, followed by the United States (SDI=0.862), then India (SDI=0.575). Of the 204 countries, 152 had an ASIR greater than 100 per 100,000, and 85.5% of those 152 had SDI levels above 0.5; 74 countries (48.68%) belonged to high or high-middle SDI quintiles.
- **Status**: supported
- **Falsification criteria**: Disproved if Fig. 2's country-level rankings differ from China>USA>India for incident cases, or if the 152/204, 85.5%, and 74 (48.68%) counts differ from the text.
- **Proof**: [E04]
- **Evidence basis**: §Results "Correlations between ADOD incidence, death, DALYs and sociodemographic transition" and Fig. 2.
- **Interpretation**: China's top rank is a population-size effect (largest incident-case count) rather than a rate effect — China's own SDI (0.722) falls in the "middle-to-high-middle" band, not among the very highest-SDI countries, consistent with C02's finding that high-middle/middle SDI regions are the ones driving rising incidence.
- **Dependencies**: C01, C03
- **Sources**:
  - China (SDI=0.722) highest, USA (SDI=0.862) 2nd, India (SDI=0.575) 3rd ← paper.pdf §Results "China, with an SDI value of 0.722, has the highest number of incident cases of ADOD, followed by the United States of America (SDI = 0.862), and India (0.575), as shown in the solid circle in Fig. 2." [result]
  - 152/204 countries ASIR>100, 85.5% SDI>0.5, 74 countries (48.68%) high/high-middle SDI ← paper.pdf §Results "Out of the 204 countries, 152 countries had an ASIR greater than 100 per 100,000, with 85.5% of them having SDI levels above 0.5. Among these countries, 74 countries(48.68%) belong to high or high-middle SDI quantiles." [result]
- **Tags**: country-level, 204-countries, SDI, incidence

## C05: The SDI-ASIR relationship is nonlinear and sex-specific (steep rise for males at low SDI, plateau/decline above SDI≈0.6; accelerating rise for females above a threshold)
- **Statement**: As SDI increases, ASIR shows an upward trend overall, with a positive relationship observed for both sexes and for females specifically. For women, ASIR remains stable or slightly decreases at low SDI levels, then the increase rate accelerates once SDI passes a certain level. For men, ASIR increases rapidly when SDI is low, but the growth rate slows and even slightly declines once SDI exceeds 0.6.
- **Status**: supported
- **Falsification criteria**: Disproved if the restricted-cubic-spline-derived SDI-ASIR association described in Figure S5 does not show this male-plateau/female-late-acceleration asymmetric nonlinear pattern.
- **Proof**: [E03]
- **Evidence basis**: §Results "Incidence of Alzheimer's disease and other dementias" (final paragraph) referencing Figure S5, and the RCS methodology in §Methods "Statistical analysis".
- **Interpretation**: This is a qualitative/directional description of a restricted-cubic-spline fit; Figure S5 itself (the plot showing this relationship at the 21-region/multi-year level) is supplementary material not provided with this input, so the shape is grounded here only in the main-text prose description, not independently re-read from the spline plot. The complementary Fig. 2 scatter (204 countries, 2021 only; `evidence/figures/figure2.md`) shows a qualitatively consistent — though independently derived and cross-sectional rather than longitudinal — nonlinear rising ASIR-SDI pattern.
- **Dependencies**: C01
- **Sources**:
  - male/female nonlinear SDI-ASIR pattern ← paper.pdf §Results "As SDI increases, the incidence showed an upward trend, positive relationships were observed between ASIR and SDI in both sexes and females. ASIR in women remained stable or even slightly decreased at low SDI levels, and the increase rate accelerated after SDI reached a certain level. When SDI level was low, the ASIR for males increased rapidly, but after reaching 0.6, the growth rate slowed down, and even showed a slightly declining trend." [result]
  - RCS methodology (4 knots, dummy variables for outlier regions) ← paper.pdf §Methods "We also used restricted cubic splines with four knots centiles to flexibly model the association of incidence, mortality, and DALY rates with SDI. Dummy variables were used for outlier regions that skewed the fit to capture the average relationship for each group, using GBD estimates from all 21 regions across all years from 1990 to 2021." [input]
- **Tags**: SDI-association, restricted-cubic-spline, nonlinear, sex-difference

## C06: Low-middle SDI region has the fastest-rising ADOD death rate (ASDR AAPC 0.41[0.31,0.52]) of any SDI quintile
- **Statement**: Among all SDI quintiles, the ASDR (age-standardized death rate) of ADOD in the low-middle SDI quintile increased the fastest over the 32-year period (1990-2021), with the highest AAPC of any quintile: 0.41(95%CI 0.31,0.52).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 2's "Low-middle SDI / Overall / ASDR / EAPC(95%CI)" value differs from 0.41*(0.31,0.52), or if any other SDI quintile's ASDR AAPC in Table 2 exceeds this value.
- **Proof**: [E05]
- **Evidence basis**: Abstract ("with the fastest increase in age-standardized death rate in low-middle SDI quintiles, experienced the highest estimated annual percentage changes (0.41[0.31,0.52])") and §Results "Mortality and DALYs of ADOD".
- **Interpretation**: This is the paper's single most emphasized quantitative finding (repeated verbatim in the Abstract) — despite low-middle SDI having one of the lowest absolute incidence/ASIR levels (C03), its mortality burden is worsening faster than any other SDI tier, the opposite direction from the SDI-mortality "improves with development" intuition suggested by the high-SDI decline (C07).
- **Dependencies**: C01
- **Sources**:
  - "fastest increase in age-standardized death rate in low-middle SDI quintiles... highest estimated annual percentage changes (0.41[0.31,0.52])" ← paper.pdf Abstract. [result]
  - "For SDI regions, ASDR in low-middle SDI quintile increased the fastest and experienced the highest AAPC (0.41[0.31,0.52]) over the 32-year period, as shown in Table 1 and Figure S3." ← paper.pdf §Results "Mortality and DALYs of ADOD". [result]
  - Table 2 confirms: Low-middle SDI / Overall / ASDR EAPC(95%CI) = 0.41*(0.31,0.52) — the only other quintile approaching this value is Low SDI at 0.41*(0.32,0.50), a narrower but overlapping interval ← `evidence/tables/table2.md` row "Low-middle SDI | Overall". [result]
- **Tags**: mortality-trend, ASDR, low-middle-SDI, AAPC

## C07: High SDI is the only region with a declining ADOD death rate in the most recent joinpoint segment (2016-2021)
- **Statement**: Looking at sub-regional secular trends, only the high SDI region showed a downward trend in ASDR in its latest joinpoint segment, with EAPC(2016-2021) = −0.24(95%CI −0.32,−0.16).
- **Status**: supported
- **Falsification criteria**: Disproved if Table 2's High SDI ASDR "Trend 4" (2016-2021) row differs from −0.24*(−0.32,−0.16), or if any other SDI region's most recent ASDR joinpoint segment is also negative.
- **Proof**: [E05]
- **Evidence basis**: §Results "Mortality and DALYs of ADOD" ("From the perspective of the secular trends of sub-regions, ASDR only in high SDI region showed a downward trend in the latest segment (EAPC2016-2021 = −0.24[−0.32,−0.16] (Table 2).").
- **Interpretation**: This directly corroborates the Discussion's framing that high-SDI regions show declining mortality/DALY burden even while their ASIR is comparatively high and still rising in absolute terms in some sub-periods (Table 1's High SDI ETPC is negative for ASIR too, −3.6, but the mortality decline is a separate, most-recent-segment-specific finding).
- **Dependencies**: C02
- **Sources**:
  - "ASDR only in high SDI region showed a downward trend in the latest segment (EAPC2016-2021 = −0.24[−0.32,−0.16] (Table 2)" ← paper.pdf §Results "Mortality and DALYs of ADOD". [result]
  - Table 2 confirms: High SDI / Trend 4 / ASDR / Year 2016–2021 / EAPC(95%CI) = −0.24*(−0.32,−0.16) ← `evidence/tables/table2.md` row "High SDI | Trend 4". [result]
- **Tags**: mortality-trend, ASDR, high-SDI, joinpoint, recent-segment

## C08: Low-middle SDI has the highest overall-population and male DALY AAPC; low SDI has the highest female DALY AAPC
- **Statement**: Among all SDI quintiles, the AAPC of DALYs was highest in the low-middle SDI region for both the entire population (AAPC 0.24, 95%CI 0.19-0.30) and specifically the male population (AAPC 0.22, 95%CI 0.21-0.23). For the female population, the highest DALY AAPC was found in the low SDI region (AAPC 0.25, 95%CI 0.18-0.31).
- **Status**: supported (overall-population figure independently verified in main-text Table 2; male/female sex-specific figures rely on Table S3, not provided)
- **Falsification criteria**: Disproved if Table 2's Low-middle SDI ASR-DALYs "Overall" EAPC differs from 0.24*(0.19,0.30), or if a provided Table S3 shows different male/female DALY AAPC values than 0.22(0.21,0.23) for low-middle SDI males or 0.25(0.18,0.31) for low SDI females.
- **Proof**: [E05]
- **Evidence basis**: §Results "Mortality and DALYs of ADOD" ("Among all SDI quintiles, the AAPC of DALYs in the entire population and specifically in the male population, was highest in the low-middle SDI region, with AAPC of 0.24(0.19,0.30) and 0.22(0.21,0.23), respectively (Table 2 and Table S3)... For the female population, the highest AAPC of DALYs was found in the low SDI region, with AAPC of 0.25(0.18,0.31) (Table S3).").
- **Interpretation**: The overall-population figure (0.24[0.19,0.30]) is independently cross-checked against Table 2 in this ARA and matches exactly, giving high confidence in the source transcription; the sex-specific figures (male 0.22[0.21,0.23], female 0.25[0.18,0.31]) come only from Table S3, which is supplementary material not included in the provided PDF, so those two sub-values are reported as stated in text but not independently re-verified against their source table.
- **Dependencies**: C06
- **Sources**:
  - overall AAPC 0.24(0.19,0.30), male AAPC 0.22(0.21,0.23) for low-middle SDI ← paper.pdf §Results "Among all SDI quintiles, the AAPC of DALYs in the entire population and specifically in the male population, was highest in the low-middle SDI region, with AAPC of 0.24(0.19,0.30) and 0.22(0.21,0.23), respectively (Table 2 and Table S3)." [result]
  - female AAPC 0.25(0.18,0.31) for low SDI ← paper.pdf §Results "For the female population, the highest AAPC of DALYs was found in the low SDI region, with AAPC of 0.25(0.18,0.31) (Table S3)." [result]
  - Table 2 independently confirms the overall-population figure: Low-middle SDI / Overall / ASR-DALYs / EAPC(95%CI) = 0.24*(0.19,0.30) ← `evidence/tables/table2.md` row "Low-middle SDI | Overall". [result]
- **Tags**: DALY-trend, low-middle-SDI, low-SDI, sex-stratified, AAPC

## C09: High fasting plasma glucose (FPG) is the leading 2021 risk factor for ADOD deaths/DALYs; its and high-BMI's attributable burden rose 1990-2021 while smoking's fell
- **Statement**: From 1990 to 2021, ADOD deaths and DALYs attributable to smoking decreased (with notable declines in the high SDI region), while ADOD ASDR attributable to high BMI and high FPG increased globally and in all SDI regions. High FPG's ASDR fluctuation was largest in the high SDI region. Globally in 2021, high FPG was the leading risk factor for both ASDR and DALYs, accounting for 3.73(0.15,11.84) and 66.42(3.83,178.85) per 100,000 respectively, followed by high BMI, then smoking.
- **Status**: supported
- **Falsification criteria**: Disproved if the global 2021 high-FPG ASDR/DALY figures (3.73[0.15,11.84], 66.42[3.83,178.85]) differ from the text, or if Figure 3/Figure 4's plotted/tabulated smoking trend is not declining while BMI/FPG trends are not rising over 1990-2021.
- **Proof**: [E05]
- **Evidence basis**: Abstract and §Results "Risk factors attributable to ADOD burden".
- **Interpretation**: This finding explicitly updates prior GBD-based dementia risk-factor rankings (see `logic/related_work.md` RW: GBD 2019 Dementia Forecasting Collaborators, ref 20, which found smoking predominant in males and BMI predominant in females as the leading factors) — high FPG's emergence as the single leading risk factor is a genuinely new finding relative to that earlier GBD vintage.
- **Dependencies**: C01
- **Sources**:
  - smoking-ASDR/DALY declined (notably in high SDI); BMI/FPG-ASDR rose globally and in all SDI regions ← paper.pdf §Results "From 1990 to 2021, both the age-standardized death and DALY rate of ADOD attributable to smoking decreased, with notable declines occurred in high SDI region (Fig. 3 and Figure S6). On the contrary, high BMI and high FPG attributable ASDRs of ADOD increased globally and in all SDI regions during the study period. The fluctuation of ASDR with high FPG attribution was the largest in high SDI region, with the heaviest burden." [result]
  - high FPG leading 2021 risk factor: ASDR 3.73(0.15,11.84), DALYs 66.42(3.83,178.85) per 100,000, followed by BMI then smoking ← paper.pdf §Results "Globally, high FPG was the leading risk factor for age-standardized deaths rates and DALYs, accounting for 3.73(0.15,11.84) and 66.42(3.83,178.85) per 100,000, respectively, in 2021, followed by high BMI, and smoking." [result]
  - Abstract summary confirms directional finding ← paper.pdf Abstract "High fasting plasma glucose was the main risk factor, particularly in high SDI region, with an increasing trend in attributable burden. The burden attributable to high BMI was increasing, whereas the burden associated with smoking steadily decreased." [result]
  - Fig. 4 heatmap independently confirms the 1990→2021 direction for the Global column: Smoking Both-sexes 1.1→0.8 (down), High BMI Both-sexes 1.2→1.8 (up), High FPG Both-sexes 2.6→3.7 (up) ← `evidence/figures/figure4.md`. [result]
- **Tags**: risk-factor, high-FPG, high-BMI, smoking, PAF, 2021

## C10: Risk-factor attribution is strongly sex-differentiated (smoking higher in males, FPG/BMI higher in females); High-income North America has the highest FPG-attributable burden
- **Statement**: The ASDR caused by smoking was higher in males than females in both 1990 and 2021, while ASDRs due to high FPG and high BMI were much higher in females. For males, smoking-attributable ADOD burden was highest in East Asia and smallest in Andean Latin America in 2021. Across sexes, the ADOD burden attributed to high FPG was highest in High-income North America, with ASDRs of 5.92 per 100,000 in females and 5.34 per 100,000 in males. Two (unnamed) regions had ASDR attributable to both high BMI and high FPG below 1.50 per 100,000.
- **Status**: supported
- **Falsification criteria**: Disproved if Figure 4's High-income North America column does not show the highest 2021 High-FPG values among all 27 columns for both sexes, or if the smoking-ASDR values for East Asia (male) do not exceed all other regions' male smoking-ASDR in 2021.
- **Proof**: [E05]
- **Evidence basis**: §Results "Risk factors attributable to ADOD burden".
- **Interpretation**: The High-income North America FPG figures (5.92 female, 5.34 male) are independently cross-checked against Figure 4's heatmap, where the "High-income North America" column at rows "2021, High FPG, Female" and "2021, High FPG, Male" reads 5.9 and 5.3 respectively — matching at the heatmap's printed 1-decimal precision and confirming both the transcription and the column identification.
- **Dependencies**: C09
- **Sources**:
  - smoking higher in males, FPG/BMI higher in females (both years) ← paper.pdf §Results "The attributable burden of ADOD also varied by sex both in 1990 or 2021, the ASDR caused by smoking was higher in males than in females, the ASDRs due to high FPG and BMI were much higher in females (Fig. 4)." [result]
  - male smoking burden highest East Asia, smallest Andean Latin America (2021) ← paper.pdf §Results "For males, ADOD burden attributed to smoking was highest in East Asia, and smallest in Andean Latin America in 2021." [result]
  - High-income North America highest FPG burden: 5.92 (female), 5.34 (male) per 100,000 ← paper.pdf §Results "Across gender groups, the ADOD burden attributed to high FPG were highest in High-income North America, with ASDRs of 5.92 per100,000 in females and 5.34 per100,000 in males, respectively." [result]
  - 2 regions <1.50 per 100,000 for both high BMI and high FPG (regions not individually named in text) ← paper.pdf §Results "Conversely, 2 regions had ASDR attributed to high BMI and high FPG less than 1.50 per 100,000." [result]
  - Figure 4 heatmap cross-check: "High-income North America" column, "2021, High FPG, Female" row = 5.9; "2021, High FPG, Male" row = 5.3 ← `evidence/figures/figure4.md` ("Cross-check against in-text values" section). [result]
- **Tags**: risk-factor, sex-difference, regional-extreme, high-FPG, smoking

## C11: Overall ADOD burden is higher in females, but males show a faster rate of increase in death/DALY burden during the study period
- **Statement**: The overall ADOD burden is higher in the female population than in males (consistent across incidence, and per the Discussion, mortality). However, the estimated annual percentage change (AAPC) of death and DALYs was relatively higher in males than in females during the study period, indicating the disease burden in males has also been rapidly increasing recently.
- **Status**: supported
- **Falsification criteria**: Disproved if Table 1's female incidence-case/ASIR/ETPC figures are not consistently higher than male figures (they are: Table 1 shows female 2021 ASIR 132.29 vs. male 103.4, and female ETPC 3.5 vs. male 2.69), or if no male AAPC for death/DALYs in any SDI-region breakdown exceeds the corresponding female AAPC.
- **Proof**: [E01]
- **Evidence basis**: §Discussion ("From a gender perspective, we found that the overall burden is higher in the female population than in males... However, we also found that the estimated annual percentage change of death and DALYs were relatively higher in males than those in females during the study period, suggesting that the disease burden in males has also rapidly increased in recent times, which means that prevention and control of male populations should not be ignored.").
- **Interpretation**: This is a genuine both-directions finding, not a simple "women bear more burden" statement: absolute burden (levels) skews toward women, but the growth rate (AAPC) of death/DALY burden skews toward men in the paper's own framing — the paper does not supply exact male-vs-female AAPC numbers for death/DALYs in the main text beyond the low-middle-SDI 0.22 vs. low-SDI 0.25 figures already captured in C08 (which come from supplementary Table S3).
- **Dependencies**: C03, C08
- **Sources**:
  - "the overall burden is higher in the female population than in males" ← paper.pdf §Discussion, opening paragraph. [result]
  - "the estimated annual percentage change of death and DALYs were relatively higher in males than those in females during the study period" ← paper.pdf §Discussion, paragraph beginning "In terms of gender, the age-standardized incidence of ADOD was higher in women than in men..." [result]
  - Table 1 cross-check of female>male incidence burden: 2021 ASIR female 132.29(116.3,149.8) vs. male 103.4(89.45,118.45); 1990-2021 ETPC female 3.5(2.31,4.43) vs. male 2.69(0.87,3.9) ← `evidence/tables/table1.md` rows "Female", "Male". [result]
- **Tags**: sex-difference, discussion-synthesis, growth-rate-vs-level

## C12: Central Sub-Saharan Africa (including Congo and Gabon) has the heaviest regional DALY burden; all six of its countries rank in the global top 10
- **Statement**: When using DALYs to measure ADOD burden, Central Sub-Saharan Africa (including Congo and Gabon) had the heaviest burden among the 21 GBD regions; all six countries in this region rank in the top 10 of 204 countries by DALY burden.
- **Status**: supported
- **Falsification criteria**: Disproved if Central Sub-Saharan Africa's DALY rate (per the supplementary Table S3/Figure S4, not provided) is not the highest of the 21 regions, or if fewer than all six of its constituent countries rank in the global top 10.
- **Proof**: [E05]
- **Evidence basis**: §Discussion, paragraph on DALY burden.
- **Interpretation**: This finding relies on Table S3 and Figure S4 (both supplementary, not provided with this input) for its underlying DALY-rate table/plot; it is grounded here only in the Discussion's prose statement, corroborated qualitatively by regional prevalence literature the paper cites for the same region (Kinshasa-DRC dementia prevalence 6.2%; EDAC survey 8.1% Bangui, 6.7% Brazzaville — refs 27, 28).
- **Dependencies**: C01
- **Sources**:
  - "the Central Sub-Saharan Africa, including Congo and Gabon, had the heaviest burden among the 21 regions. All six countries in this region are all in the top 10 with the heaviest disease burden of 204 countries." ← paper.pdf §Discussion. [result]
  - corroborating regional prevalence citations (Kinshasa-DRC 6.2%; Bangui 8.1%, Brazzaville 6.7%) ← paper.pdf §Discussion "the crude prevalence of suspected dementia was 6.2%... the prevalence of dementia was estimated at 8.1% in Bangui and 6.7% in Brazzaville" [result — cited from other primary studies, refs 27-28, not this paper's own GBD estimate]
- **Tags**: DALY-burden, Central-Sub-Saharan-Africa, regional-extreme

## C13: Central Sub-Saharan Africa is separately stated to have the highest ADOD mortality rate with a 14.82% ETPC — a figure that could not be independently verified and numerically coincides with an unrelated incidence-ETPC value elsewhere in the paper
- **Statement**: The Discussion states that Central Sub-Saharan Africa had the highest ADOD mortality rates among the 21 regions, with an estimated total percentage change (ETPC) of 14.82% from 1990 to 2021.
- **Status**: unverified / flagged inconsistency
- **Falsification criteria**: Would be resolved if the supplementary Table S1 (mortality ETPC by region, not provided with this input) showed Central Sub-Saharan Africa's mortality ETPC at 14.82%.
- **Proof**: [E05]
- **Evidence basis**: §Discussion, paragraph beginning "Central Sub-Saharan Africa had the highest ADOD mortality rates among the 21 regions".
- **Interpretation**: This claim cannot be independently checked because it depends on Table S1 (mortality data), which is supplementary material not included with this input. Separately, within the main-text Table 1 (which reports the 1990-2021 ETPC of ASIR — incidence, not mortality), the value "−14.82(−19.55,−10.2)" appears, but attached to a *different* region: Australasia. Central Sub-Saharan Africa's own incidence ETPC in Table 1 is −0.59(−3.02,1.79), not 14.82. This is reported here as an observed numeric coincidence between an incidence-ETPC value elsewhere in the paper and the Discussion's stated mortality-ETPC value for a different region — not asserted as a confirmed transcription error in the source, since the two statistics (incidence ETPC vs. mortality ETPC) are conceptually distinct and the mortality figure's source table (Table S1) is unavailable for direct comparison.
- **Dependencies**: C01
- **Sources**:
  - "Central Sub-Saharan Africa had the highest ADOD mortality rates among the 21 regions, with an estimated total percentage change of 14.82% from 1990 to 2021." ← paper.pdf §Discussion. [result]
  - Table 1 shows "−14.82(−19.55,−10.2)" attached to Australasia's ASIR ETPC (not Central Sub-Saharan Africa) ← `evidence/tables/table1.md` row "Australasia", column "1990-2021 ETPC of ASIR". [result]
  - Table 1 shows Central Sub-Saharan Africa's own ASIR ETPC as −0.59(−3.02,1.79) ← `evidence/tables/table1.md` row "Central Sub-Saharan Africa". [result]
- **Tags**: mortality-trend, Central-Sub-Saharan-Africa, unverified, internal-source-inconsistency-candidate
