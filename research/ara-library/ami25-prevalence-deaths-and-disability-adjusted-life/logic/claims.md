# Claims

All numeric values are copied exactly from the source. "Statistically significant" follows the
paper's convention: a percentage change whose 95% UI excludes zero. Each `**Sources**` entry cites a
location whose verbatim quoted text contains the value.

## C01: MENA age-standardised prevalence fell 4.9% (significant) from 1990 to 2021
- **Statement**: In 2021 the MENA region age-standardised prevalence of AD and other dementias was
  772.7 per 100,000 (95% UI 671.2–877.6), a statistically significant 4.9% decrease relative to 1990
  (95% UI of the change: −6.2 to −3.7 per Table 1; running text reports the change as 4.9%,
  95% UI 3.7–6.3). Absolute prevalent cases in 2021: 2,684,371 (2.68 million; 95% UI 2,322,373–3,040,389).
- **Status**: supported
- **Falsification criteria**: Re-running GBD 2021 for MENA yields a 2021 age-standardised prevalence
  materially different from 772.7 per 100,000, or a 1990→2021 change whose 95% UI includes 0 (i.e.
  not significant), or a change of opposite sign.
- **Proof**: [E01]
- **Evidence basis**: Table 1 regional row (772.7; −4.9 (−6.2, −3.7); 2,684,371); abstract and
  Results text.
- **Interpretation**: The decline reverses the +3.0% (1990–2019) prevalence trend reported by the
  prior GBD 2019 MENA analysis (ref 6); the authors attribute it to declining smoking and CVD and to
  demographic shifts, but this is interpretive, not directly tested here.
- **Dependencies**: none
- **Tags**: prevalence, MENA, age-standardised-rate, trend
- **Sources**:
  - 772.7 per 100,000 (95% UI 671.2–877.6) ← Results §"The MENA region", p.4 «772.7 patients per 100,000 (95% UI 671.2–877.6) were observed in 2021, which was 4.9% (95% UI 3.7–6.3) lower compared to 1990» [result]
  - −4.9 (−6.2, −3.7) ← evidence/tables/table1.md, Prevalence, North Africa and Middle East «772.7 (671.2, 877.6) | − 4.9 (− 6.2, − 3.7)» [result]
  - 2,684,371 (2,322,373, 3,040,389) ← evidence/tables/table1.md, Prevalence, North Africa and Middle East «2,684,371 | (2,322,373, 3,040,389)» [result]

## C02: MENA age-standardised death and DALY rates fell significantly (8.6% and 7.7%) from 1990 to 2021
- **Statement**: In 2021 the MENA age-standardised death rate was 25.6 per 100,000 (95% UI 6.3–66.8),
  a significant 8.6% decrease vs 1990 (95% UI −14.1 to −2.4); deaths totalled 73,791 (≈73.79 thousand;
  95% UI 18,123–190,474). The age-standardised DALY rate was 476.3 per 100,000 (95% UI 225.6–1004.2),
  a significant 7.7% decrease (95% UI −11.7 to −3.4); DALYs totalled 1,566,073 (≈1.56 million;
  95% UI 753,719–3,314,933).
- **Status**: supported
- **Falsification criteria**: GBD 2021 MENA 2021 death or DALY ASR materially different from 25.6 /
  476.3, or a 1990→2021 change whose 95% UI includes 0, or of opposite sign.
- **Proof**: [E01]
- **Evidence basis**: Table 1 regional row (deaths 25.6; −8.6 (−14.1, −2.4); DALYs 476.3;
  −7.7 (−11.7, −3.4)); Results text.
- **Interpretation**: Death and DALY declines are steeper than the prevalence decline, consistent
  with mortality being more sensitive to the modelled reductions in smoking/CVD burden.
- **Dependencies**: none
- **Tags**: mortality, DALY, MENA, trend
- **Sources**:
  - deaths 73,791; ASR 25.6 (6.3, 66.8); −8.6 (−14.1, −2.4) ← evidence/tables/table1.md, Deaths, North Africa and Middle East «73,791 | (18,123, 190,474) | 25.6 | (6.3, 66.8) | − 8.6 | (− 14.1, − 2.4)» [result]
  - DALY 1,566,073; ASR 476.3 (225.6, 1004.2); −7.7 (−11.7, −3.4) ← evidence/tables/table1.md, DALYs, North Africa and Middle East «1,566,073 | (753,719, 3,314,933) | 476.3 | (225.6, 1004.2) | − 7.7 | (− 11.7, − 3.4)» [result]

## C03: Country-level 2021 prevalence ranged from UAE (lowest) to Lebanon (highest)
- **Statement**: In 2021 national age-standardised point prevalence ranged from 652.43 to 828.25 per
  100,000. The highest rates were Lebanon 828.25 (95% UI 710.40–948.14), Turkey 819.36 (706.20–936.59),
  and Tunisia 791.09 (685.56–901.07); the lowest were United Arab Emirates 652.43 (552.16–753.80),
  Saudi Arabia 701.74 (600.97–807.91), and Egypt 726.90 (630.54–823.49).
- **Status**: supported
- **Falsification criteria**: GBD 2021 shows a different country holding the max or min 2021
  prevalence ASR, or values outside the reported UIs.
- **Proof**: [E02]
- **Evidence basis**: Results §"Country level", p.4; Table 1; Figure 1a.
- **Interpretation**: The ~1.27× spread across countries is modest relative to the wide 95% UIs; the
  authors attribute variation to environmental, risk-factor, genetic, demographic, and health-system
  differences.
- **Dependencies**: C01
- **Tags**: country-ranking, prevalence, Lebanon, UAE
- **Sources**:
  - Lebanon 828.25 (710.40–948.14), highest; UAE 652.43 (552.16–753.80), lowest ← Results §"Country level", p.4 «The highest ASRs were reported in Lebanon [828.25 (95% UI 710.40–948.14)] … the United Arab Emirates [652.43 (95% UI 552.16–753.80)] … had the lowest ASRs» [result]
  - range 652.43 to 828.25 ← Results §"Country level", p.4 «the national age-standardised point prevalence of AD ranged from 652.43 to 828.25 cases per 100,000» [result]

## C04: Prevalence decreased significantly in 13 of 21 MENA countries; no significant change in 8
- **Statement**: The age-standardised point prevalence decreased from 1990 to 2021 in 13 of the 21
  MENA countries, with no significant change in the remaining 8. The largest decreases were United
  Arab Emirates −9.9 (95% UI −13.3 to −6.2), Yemen −9.2 (−12.8 to −5.9), and Syrian Arab Republic
  −8.1 (−11.2 to −4.6). (By comparison, significant death-rate decreases occurred only in UAE −16.2,
  Bahrain −12.5, Iran −7.8; significant DALY-rate decreases in five countries, largest UAE −15.7,
  Turkey −10.8, Bahrain −10.6.)
- **Status**: supported
- **Falsification criteria**: A different count of countries with significant prevalence decline
  (≠13), or a listed country's change UI actually including 0.
- **Proof**: [E02]
- **Evidence basis**: Results §"Country level", p.4; Table 1 (% change columns and their UIs).
- **Interpretation**: The declines concentrate in higher-income Gulf states (UAE, Bahrain), aligning
  with the SDI discussion, though the paper reports no clear SDI dose–response (C08).
- **Dependencies**: C01
- **Tags**: country-trend, prevalence, significance
- **Sources**:
  - 13 of 21 decreased, rest no significant change ← Results §"Country level", p.4 «The age-standardised point prevalence decreased from 1990 to 2021 in 13 of the 21 MENA countries, with no significant changes in the rest of the countries» [result]
  - UAE −9.9 (−13.3, −6.2); Yemen −9.2 (−12.8, −5.9); Syrian Arab Republic −8.1 (−11.2, −4.6) ← evidence/tables/table1.md, Prevalence «United Arab Emirates … − 9.9 | (− 13.3, − 6.2)»; «Yemen … − 9.2 | (− 12.8, − 5.9)»; «Syrian Arab Republic … − 8.1 | (− 11.2, − 4.6)» [result]

## C05: Female burden exceeded male across all measures, but the sex difference was not significant
- **Statement**: In 2021, in all three measures (prevalence, deaths, DALYs), both in counts and in
  age-standardised rates, females were the dominant cases in all age groups; however this difference
  was not statistically significant.
- **Status**: supported
- **Falsification criteria**: A GBD 2021 breakdown in which male rates equal or exceed female in the
  MENA aggregate, or a formal test showing the female–male gap is significant (which would contradict
  the paper's "not statistically significant" qualifier).
- **Proof**: [E03]
- **Evidence basis**: Results §"Age and sex patterns", p.5; Figures 1 and 2 (female bars/lines above
  male at all strata, overlapping wide UIs).
- **Interpretation**: The paper attributes the female excess to women's greater longevity, lower
  historical cognitive reserve (education/occupation), and ApoE4-related biology — interpretive, not
  tested here. The non-significance qualifier is important: the female excess is a consistent point
  estimate, not a demonstrated significant difference.
- **Dependencies**: none
- **Tags**: sex-difference, female, cognitive-reserve
- **Sources**:
  - females dominant in all age groups, not significant ← Results §"Age and sex patterns", p.5 «females were the dominant cases in all age groups, although this difference was not statistically significant (Fig. 2A–C)» [result]

## C06: Burden rose with age, peaking at 80–84 (prevalence, DALYs) or 85–89 (deaths)
- **Statement**: In 2021 the number of prevalent cases increased with age up to the 80–84 bracket
  before declining to 95+; the number of deaths rose to the 85–89 bracket then decreased; the number
  of DALYs increased to 80–84 then declined. For all three, the age-standardised rate rose with
  increasing age in both sexes across the full range.
- **Status**: supported
- **Falsification criteria**: A GBD 2021 age profile in which counts peak at a materially different
  age band, or in which age-standardised rates do not rise monotonically with age.
- **Proof**: [E04]
- **Evidence basis**: Results §"Age and sex patterns", p.4–5; Figure 2a–c.
- **Interpretation**: The divergence between count peak (mid-80s) and still-rising rate at 95+
  reflects shrinking population denominators at the oldest ages.
- **Dependencies**: none
- **Tags**: age-pattern, prevalence, mortality, DALY
- **Sources**:
  - prevalence peaks 80–84, declines to 95+; rate rises with age ← Results §"Age and sex patterns", p.4 «the prevalence of AD and other dementias increased up to the 80–84 age bracket for both sexes, before declining to the 95+ age category. The age-standardised prevalence of dementia rose with age for both sexes» [result]
  - deaths peak 85–89 ← Results §"Age and sex patterns", p.4 «the number of deaths for both sexes rose with age to the 85–89 age bracket, then decreased» [result]
  - DALYs peak 80–84 ← Results §"Age and sex patterns", p.5 «The number of DALYs also increased with age in both sexes to the 80–84 age category, after which it declined» [result]

## C07: MENA burden stayed ≥ global across ages/sexes, but the MENA/Global DALY ratio fell from 1990 to 2021
- **Statement**: The MENA/Global DALY-rate ratio was ≥1 across all age groups and both sexes; the
  highest 2021 ratio was 1.2, observed in males aged 70–79. Compared with 1990, the 2021 ratio was
  lower or equal across all age groups and both sexes, indicating a decreasing trend. Overall the
  MENA burden remained consistently higher than or equal to global rates across nearly all ages and
  both sexes.
- **Status**: supported
- **Falsification criteria**: A GBD 2021 comparison in which any MENA/Global DALY ratio falls below 1,
  or in which the 2021 ratio exceeds the 1990 ratio in some age/sex stratum, or a 2021 maximum ratio
  ≠1.2.
- **Proof**: [E05]
- **Evidence basis**: Results §"Age and sex patterns", p.5; Discussion, p.9; Figure 3 (annotated
  point ratios ≥1.0, 2021 ≤ 1990 at every band).
- **Interpretation**: The declining excess suggests MENA is converging toward the global rate over
  time, though it still bears an above-global burden.
- **Dependencies**: C02
- **Tags**: MENA-vs-global, DALY-ratio, convergence
- **Sources**:
  - highest 2021 ratio 1.2 (males 70–79); 2021 ≤ 1990 across all strata ← Results §"Age and sex patterns", p.5 «The highest MENA/Global DALYs ratio in 2021 was 1.2, observed in males aged 70–79. When compared to 1990 data, it is evident that the MENA/Global DALYs ratio in 2021 was lower or equal across all age groups and both sexes, indicating a decreasing trend» [result]

## C08: Age-standardised DALY rate generally decreased with rising SDI, with country deviations
- **Statement**: In 2021 the age-standardised DALY rate of dementia generally decreased as SDI
  increased (decreasing to SDI≈0.4, a slight rise to ≈0.47, then generally decreasing at higher SDI
  with a minor increase in the 0.6–0.65 range). Burden was higher than SDI-expected in Afghanistan,
  Libya, Turkey, Tunisia, Algeria, and Bahrain, and lower than expected in Sudan, the Syrian Arab
  Republic, Jordan, and Egypt. The authors conclude no clear trend in dementia-burden change relative
  to SDI across MENA countries.
- **Status**: supported
- **Falsification criteria**: A GBD 2021 SDI plot showing a monotonic (not undulating) relationship,
  or the listed above-/below-expected countries falling on the opposite side of the expected line.
- **Proof**: [E06]
- **Evidence basis**: Results §"Relationship with the SDI", p.5, 8; Discussion, p.10; Figure 4
  (observed country tracks vs black expected smoothing-spline line).
- **Interpretation**: The absence of a clean dose–response is attributed to health-system quality,
  focus on elderly care, and genetic/biological factors beyond development level.
- **Dependencies**: C02
- **Tags**: SDI, DALY, socioeconomic-gradient, smoothing-spline
- **Sources**:
  - higher than expected in Afghanistan, Libya, Turkey, Tunisia, Algeria, Bahrain; lower in Sudan, Syrian Arab Republic, Jordan, Egypt ← Results (continued p.8) «The burden of dementia was higher than expected in Afghanistan, Libya, Turkey, Tunisia, Algeria, and Bahrain, while it was lower in Sudan, the Syrian Arab Republic, Jordan, and Egypt (Fig. 4)» [result]
  - DALY rate decreased with SDI up to 0.4, slight rise to ≈0.47, then decreased ← Results §"Relationship with the SDI", p.5 «the age standardised DALY rate of dementia decreased as the SDI increased up to 0.4, followed by a slight rise up to an SDI of approximately 0.47. Beyond this point, the rate generally decreased for higher SDIs» [result]
