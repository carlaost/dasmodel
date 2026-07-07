# Related Work — Typed Dependency Graph

Type legend: `imports` (uses directly), `extends` (builds on/updates), `bounds` (defines methodological limits), `baseline` (comparator/data source), `refutes`. Full `RW` blocks are given for works with a specific technical delta (the primary GBD data source, the risk-factor PAF methodology, the statistical methods adopted, and the prior GBD dementia analyses this paper explicitly contrasts against); brief grouped entries below preserve the paper's full 51-reference footprint.

## RW01: GBD 2021 Diseases and Injuries Collaborators — Global incidence, prevalence, YLDs, DALYs, HALE for 371 diseases and injuries (ref 15)
- **DOI**: 10.1016/S0140-6736(24)00757-8 (Lancet. 2024;403(10440):2133-61)
- **Type**: imports (primary data source)
- **Delta**:
  - What changed: Supplies the entire underlying dataset for this paper — location/year/age/sex estimates of incidence, mortality, and DALYs for 371 diseases/injuries (ADOD among them) in 204 countries/territories and 811 subnational locations, 1990-2021.
  - Why: This paper is explicitly a "secondary analysis of GBD 2021" — every headline number in `logic/claims.md` C01-C08 and `evidence/tables/table1.md`/`table2.md` is derived from this source.
- **Claims affected**: C01, C02, C03, C04, C05, C06, C07, C08, C11
- **Adopted elements**: The full incidence/mortality/DALY estimation framework, age-standardization methodology, and SDI-quintile/GBD-region classification scheme.

## RW02: GBD 2021 Risk Factors Collaborators — Global burden and strength of evidence for 88 risk factors (ref 17)
- **DOI**: 10.1016/S0140-6736(24)00933-4 (Lancet. 2024;403(10440):2162-203)
- **Type**: imports (primary risk-factor data source and PAF methodology)
- **Delta**:
  - What changed: Supplies the relative-risk data, exposure distributions, and theoretical-minimum-risk-exposure distributions this paper uses to compute population attributable fractions (PAF) for smoking, high FPG, and high BMI attributable to ADOD deaths/DALYs.
  - Why: "The specific methods are outlined in the previous study [17]" (§Methods "Attributable risk factors") — this paper directly reuses the GBD comparative-risk-assessment PAF formula and underlying risk-factor exposure/RR data rather than deriving its own.
- **Claims affected**: C09, C10, C12, C13
- **Adopted elements**: PAF formula (`logic/concepts.md` "Population attributable fraction"); comparative risk assessment methodology.

## RW03: Murray CJL — The Global Burden of Disease study at 30 years (ref 16)
- **DOI**: 10.1038/s41591-022-01990-1 (Nat Med. 2022;28(10):2019-26)
- **Type**: imports
- **Delta**:
  - What changed: Cited alongside GBD 2021 Diseases and Injuries Collaborators as a description of GBD input sources and methodology ("Details of input sources and methodology descriptions have been described elsewhere [15, 16]").
  - Why: Establishes the GBD study's overall data-quality and methodology track record, supporting the paper's treatment of GBD estimates as globally recognized.
- **Claims affected**: none directly (background/methodology citation)
- **Adopted elements**: General GBD-methodology framing (not a specific numeric input).

## RW04: Farcomeni A, Geraci M — Multistate quantile regression models (ref 18)
- **DOI**: 10.1002/sim.8393 (Stat Med. 2020;39(1):45-56)
- **Type**: imports (statistical method)
- **Delta**:
  - What changed: Supplies the quantile-regression estimator (minimum weighted absolute deviation) this paper applies to the 204-country, 2021 cross-sectional SDI-ASR analysis.
  - Why: Chosen because quantile regression "can estimate the linear relationship between different quantiles of dependent and independent variables, and can observe the changes in regression coefficients under different distributions... giving it an advantage over traditional linear regression models" (§Methods).
- **Claims affected**: C04, C05
- **Adopted elements**: Quantile regression estimator (`logic/concepts.md` "Quantile regression"); used in E04.

## RW05: Bai J, Cui J, Shi F, Yu C — Global epidemiological patterns in non-communicable diseases, relationships with SDI (ref 19)
- **DOI**: 10.3389/ijph.2023.1605502 (Int J Public Health. 2023;68:1605502)
- **Type**: imports / baseline
- **Delta**:
  - What changed: A prior application of joinpoint + SDI-association methodology to a different disease group (main non-communicable diseases, 1990-2019), cited alongside ref 18 as methodological precedent for combining joinpoint regression with an SDI-relationship analysis.
  - Why: Provides methodological precedent that this paper extends specifically to ADOD.
- **Claims affected**: C02, C05, C06, C07, C08 (methodological precedent only, not a data input)
- **Adopted elements**: The general joinpoint + SDI-relationship analytic template.

## RW06: GBD 2019 Dementia Forecasting Collaborators (ref 20) — refuted/updated by this paper's risk-factor finding
- **DOI**: 10.1016/S2468-2667(21)00249-8 (Lancet Public Health. 2022;7(2):e105-25)
- **Type**: refutes (partially — specifically on leading risk factor)
- **Delta**:
  - What changed: Ref 20 reported smoking as the predominant risk factor among males and high BMI as predominant among females; this paper's GBD-2021-based analysis instead finds high FPG has become the leading attributable risk factor for ADOD overall, especially in the high-SDI region.
  - Why: "Unlike previous GBD estimates [20, 21], high FPG became the most important attributable risk factor for ADOD, especially in high SDI region" (§Discussion) — an explicit, named update to this prior GBD dementia vintage's risk-factor ranking.
- **Claims affected**: C09, C10
- **Adopted elements**: none (this is a contrast/update, not an adopted element); the GBD 2019 forecasting/prevalence estimates themselves are not reused here (this paper explicitly excludes prevalence, see `logic/problem.md` A5).

## RW07: GBD 2016 Dementia Collaborators (ref 21) — earlier-vintage comparator
- **DOI**: 10.1016/S1474-4422(18)30403-4 (Lancet Neurol. 2019;18(1):88-106)
- **Type**: baseline / refutes (jointly with RW06 on risk-factor ranking)
- **Delta**:
  - What changed: An earlier (GBD 2016) global/regional/national ADOD burden analysis, superseded in this paper by the GBD 2021 data vintage and by the updated risk-factor finding described in RW06.
  - Why: Cited jointly with ref 20 as the "previous GBD estimates" this paper's high-FPG finding departs from.
- **Claims affected**: C09
- **Adopted elements**: none (superseded comparator).

## Brief citation footprint (no distinct technical delta beyond the above)

**Dementia/AD background, disease burden, and prevention framing** (refs 1, 4-14): Matej et al. (AD/neurodegenerative dementia comorbidity, clinical/neuropathological overview); Long/Benoist/Weidner (World Alzheimer Report 2023, source of the "139 million by 2050" projection in `logic/problem.md` O1); 2023 Alzheimer's disease facts and figures (source of the US 6.7M→13.8M-by-2050 projection); Scheltens et al. (Alzheimer's disease, Lancet overview, source of the "strongest contributors to global disease burden" framing in §Discussion); Winblad et al. (Defeating Alzheimer's disease and other dementias, European priority framing); Baumgart et al. (modifiable risk factors for cognitive decline, population-based review); Tin et al. (genetic risk + Life's Simple 7 + incident dementia, ARIC study); Yu et al. (evidence-based AD prevention, systematic review/meta-analysis of 243 observational + 153 RCT studies); Nianogo et al. (AD/dementia risk factors by sex/race/ethnicity, US); Livingston et al. (2024 Lancet Commission report — source of the "nearly half of dementia cases theoretically preventable by eliminating 14 risk factors" figure in `logic/problem.md`); Mazure & Swendsen (sex differences in AD/dementias, motivating this paper's sex-stratified design); Kalaria et al. (AD/vascular dementia in developing countries, prevalence/management/risk-factor review).

**Health economics / global burden context** (refs 2, 3): World Health Organization (Dementia fact sheet — source of the "50 million people living with dementia... 60% in LMICs" figure in `logic/problem.md` O1); Wimo et al. (worldwide costs of dementia 2019 — source of the "$1.3 trillion... 50% informal caregiver cost" figure in O2).

**Regional/comparative GBD-based dementia burden studies** (refs 22, 23): Agudelo-Botero et al. (systematic/comparative AD-and-other-dementias burden analysis, Mexico, 1990-2019); Schwinne et al. (AD-related blood-based biomarkers vs. cognitive screening, Congolese population, medRxiv preprint) — cited in §Discussion to support the "largest ADOD increase projected in LMICs, particularly East Asia and Sub-Saharan Africa" framing.

**Healthcare access / health-system-capacity literature** (refs 24, 25): Mukadam et al. (improving dementia service access for minority ethnic groups); GBD 2019 Human Resources for Health Collaborators (availability of health-workforce resources and universal health coverage, 204 countries) — cited in §Discussion to interpret the Central Sub-Saharan Africa mortality-burden finding (C12/C13) via "unequal access to healthcare, poor quality of medical facilities, and delayed or inadequate health services."

**Regional prevalence studies corroborating the Central Sub-Saharan Africa / Brazil / Japan findings** (refs 26-32): Wang et al. (GBD 2019 metabolic risk factors, ischemic heart disease — cited for PAF-methodology parallel); Ikanga et al. (suspected dementia prevalence, Kinshasa-DRC, 6.2%); Guerchet et al. (EDAC survey, Central Africa: 8.1% Bangui, 6.7% Brazzaville); Feter et al. (AD hospitalization trends, Brazil, 87.7% increase over 10 years); Ikeda et al. (economic burden of AD dementia, Japan: 7.404 or 12.628 trillion yen/year, 65% public long-term-care costs); Ohara et al. (dementia prevalence/incidence/survival trends, Japanese community); Shimizu et al. (dementia prevalence trends, Nakayama Study, Japan) — all cited in §Discussion as corroborating context for this paper's own GBD-2021-derived regional findings (C12, C13), not as data inputs to the GBD estimates themselves.

**Sex/gender-difference mechanism literature (Discussion, "gender perspective")** (refs 33-39): GBD 2016 Disease and Injury Incidence and Prevalence Collaborators; Kolahchi et al. (sex/gender differences in AD: genetic, hormonal, inflammation); Zhu, Montagne & Zhao (AD pathogenic mechanisms and sex difference); Ardekani, Convit & Bachman (MIRIAD data, sex differences in hippocampal atrophy progression); Mosconi et al. (perimenopause and AD bioenergetic phenotype, refs 37-38, brain imaging of endocrine vs. chronologic aging); Eid, Gobinath & Galea (sex differences in depression) — cited to interpret why females show higher ADOD burden beyond a pure longevity effect (C03, C11).

**Metabolic/behavioral risk-factor mechanism literature (Discussion, "risk factors")** (refs 40-46): Serrano-Pozo & Growdon (is AD risk modifiable?); Charlot et al. (time-restricted feeding and metabolic disease); Hillari, Frank & Cadar (systemic inflammation, lifestyle, dementia, 10-year follow-up); Katzmarzyk et al. (physical inactivity and NCD burden by country income level); Ho et al. (obesity linked to lower brain volume in AD/MCI patients); Maesako et al. (exercise vs. diet control, high-fat-diet-induced amyloid deposition in transgenic AD mice); Fernandes & Caramelli (ischemic stroke and infectious diseases in LMICs) — cited to mechanistically interpret the rising high-BMI/high-FPG and the region-specific patterns in C09/C10.

**Smoking-cessation and tobacco-policy literature (Discussion, "smoking")** (refs 47-49): Almeida et al. (24-month effect of smoking cessation on cognitive function/brain structure); Schiavone et al. (second-hand tobacco smoke prevalence vs. smoke-free legislation, EU); Radó et al. (comprehensive smoke-free legislation and neonatal/infant mortality, 106 middle-income countries, synthetic control study) — cited to interpret the declining smoking-attributable ADOD trend (C09) and to discuss policy levers.

**Global dementia-policy context (Discussion, closing)** (refs 50, 51): World Health Organization (World failing to address dementia challenge, 2021 news item); World Health Organization (Draft Intersectoral Global Action Plan on Epilepsy and Other Neurological Disorders 2022-2031) — cited to situate the paper's prevention/policy recommendations within ongoing WHO-level initiatives, not as evidence inputs to any claim.

## Datasets and Clinical Trials (typed data dependencies)
Per `sources.yaml` (verified; do not re-verify): **no released dataset**, **no code**, and **no registered clinical trial** are associated with this paper. `code: []`, `data: []`, `clinical_trials: []`.
- **Data dependency (type: baseline/imports, access: public registry query tool)**: GBD 2021 estimates, queried from the Global Health Data Exchange (GHDx) at http://ghdx.healthdata.org/ and the GBD Results Tool at http://ghdx.healthdata.org/gbd-results-tool. Per the paper's own "Data availability" statement: "No datasets were generated or analysed during the current study" (i.e., GBD's own public query tool is the access mechanism; no new dataset artifact is released by this paper).
- **No PROSPERO ID, NCT ID, or software repository** appears anywhere in the paper's full text; ethical approval was deemed not applicable since GBD's underlying data sources are all publicly listed.
