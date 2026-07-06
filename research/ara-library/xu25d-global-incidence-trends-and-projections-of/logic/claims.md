# Claims

> Grounding: abstract-only. Every load-bearing number is copied from `metadata.md` or `metadata.json`; no full text, tables, figures, code, or supplements were provided.

## C01: Global case counts rose while global ASIR was relatively stable during 1992-2021
- **Statement**: Between 1992-2021, global Alzheimer disease and other dementia cases increased from 4.078 million to 9.837 million, while global ASIR rose only slightly from 117.7 to 119.8 per 100,000.
- **Status**: supported
- **Falsification criteria**: Reanalysis of GBD 2021 incidence data showing materially different global case counts or ASIR values for 1992 and 2021, or showing that the ASIR did not remain relatively stable.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly reports the historical case and ASIR values.
- **Interpretation**: The divergence between case counts and ASIR supports the authors' conclusion that population ageing contributes to rising absolute burden.
- **Sources**:
  - 1992-2021, 4.078 million, 9.837 million, 117.7, 119.8 per 100,000 ← metadata.md (Abstract, Results) «Between 1992–2021, global AD cases increased from 4.078 million to 9.837 million, while the global age-standardised incidence rate (ASIR) remained relatively stable, rising slightly from 117.7 to 119.8 per 100 000.» [result]
- **Dependencies**: none
- **Tags**: incidence, ASIR, GBD-2021, historical-trend

## C02: ASIR trends differed by sociodemographic-index region
- **Statement**: ASIR increased significantly in high-middle and middle-sociodemographic-index regions but declined in low-sociodemographic-index regions.
- **Status**: supported
- **Falsification criteria**: Stratified APC analysis showing no significant increase in high-middle or middle-SDI regions, or no decline in low-SDI regions.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly states the direction of SDI-stratified ASIR changes.
- **Interpretation**: Regional economic and health-system contexts may shape incidence detection and burden patterns, but mechanisms are not specified in the provided input.
- **Sources**:
  - high-middle, middle, low-SDI trend directions ← metadata.md (Abstract, Results) «ASIR increased significantly in high-middle and middle-sociodemographic index regions, but declined in the low-sociodemographic index regions.» [result]
- **Dependencies**: C01
- **Tags**: ASIR, SDI, regional-stratification

## C03: Women had consistently higher incidence rates than men
- **Statement**: Women consistently exhibited higher Alzheimer disease and other dementia incidence rates than men across all regions.
- **Status**: supported
- **Falsification criteria**: Sex-stratified incidence analysis showing that men equal or exceed women in incidence rates in one or more global regions over the relevant period.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly reports higher incidence rates for women across all regions.
- **Interpretation**: Sex disparities are part of the burden pattern; causal explanation is not available from provided input.
- **Sources**:
  - women higher across all regions ← metadata.md (Abstract, Results) «Women consistently exhibited higher incidence rates than men across all regions.» [result]
- **Dependencies**: none
- **Tags**: sex-disparity, incidence, regional-stratification

## C04: BAPC projections report substantially higher global cases and ASIR by 2036
- **Statement**: The paper projects that 2036 global Alzheimer disease and other dementia cases will reach 19.117 million, with ASIR of 418.92 per 100,000.
- **Status**: supported
- **Falsification criteria**: Reproduction of the BAPC forecast from the same GBD 2021 inputs yielding materially different 2036 global cases or ASIR, or a documented correction to the published projection.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly reports the 2036 projected case count and ASIR.
- **Interpretation**: The projected ASIR is reported as written in the abstract; the full text is unavailable to reconcile it with the historical ASIR scale or uncertainty intervals.
- **Sources**:
  - 2036, 19.117 million, 418.92 per 100,000 ← metadata.md (Abstract, Results) «Projections indicate that 2036 global AD cases will reach 19.117 million, with an ASIR of 418.92 per 100 000.» [result]
- **Dependencies**: C01
- **Tags**: BAPC, forecast, 2036, ASIR

## C05: Rising absolute burden motivates early diagnosis and targeted interventions
- **Statement**: The authors conclude that stable global ASIR with rising case counts due to population ageing, plus regional resource limitations and gender disparities, supports prioritizing early diagnosis and targeted interventions to reduce future burden and health-care inequalities.
- **Status**: hypothesis
- **Falsification criteria**: Evidence that projected incidence burden does not translate into increased health-system need, or that early diagnosis and targeted interventions do not affect future burden or inequality in the relevant settings.
- **Proof**: [E01, E02, E03]
- **Evidence basis**: The abstract's Conclusions state the interpretation and recommended priorities.
- **Interpretation**: This is a policy and public-health implication drawn from the reported trend and projection analyses, not a directly tested intervention result.
- **Sources**:
  - population ageing, early diagnosis, targeted interventions ← metadata.md (Abstract, Conclusions) «While global ASIR has remained stable, the number of AD cases continues to rise due to population ageing, particularly in middle- and high-income regions. Low-income regions face additional challenges due to limited health care resources. Gender disparities and unequal access to health care contribute to the variations in disease burden. These findings emphasise the need to prioritise early diagnosis and implement targeted interventions to reduce future disease burdens and address global health care inequalities.» [result]
- **Dependencies**: C01, C02, C03, C04
- **Tags**: public-health, early-diagnosis, interventions, inequality
