# Problem Specification

## Observations

### O1: The global dementia burden is large and costly
- **Statement**: According to the GBD 2021 report, Alzheimer's disease/AD-related dementias (AD/ADRD) is the 8th leading cause of death worldwide; global economic costs of dementia exceed US$1.3 trillion for 55 million people with dementia, or almost US$24,000 per person with dementia.
- **Evidence**: paper.pdf p.1 (Introduction), citing refs 1 (IHME GBD 2021) and 2 (Wimo et al. 2023).
- **Implication**: Dementia is a major, high-cost global health burden, but AD/ADRD "does not strike countries equally" — both prevalence and costs vary greatly across countries, motivating internationally comparable data.

### O2: Prior multi-country European prevalence studies are not methodologically harmonized
- **Statement**: Large research consortia (EURODEM, EuroCoDe, Prince et al., Alzheimer Europe, OECD) have produced European dementia prevalence estimates mainly via systematic reviews of epidemiological/clinical studies with heterogeneous methodology, populations, diagnostic criteria, age groups, and study years; where population studies are scarce or missing (particularly Central and Eastern Europe), prevalence had to be imputed from neighboring countries.
- **Evidence**: paper.pdf p.1 (Introduction), citing refs 3–11.
- **Implication**: Lack of harmonization threatens international comparability, is an obstacle to unbiased population estimates, and may distort cross-national associations with risk factors (age, sex, education) due to comparability artefacts.

### O3: SHARE offers ex-ante harmonized cognition measures but existing SHARE-based dementia classifications are unvalidated
- **Statement**: SHARE is a longitudinal aging study (started 2004) representative of the 50+ population in 27 European countries and Israel, with strictly harmonized instruments including identical cognition measures. Machine-learning (ML)-based algorithms have been applied to SHARE data to assess probable dementia, but these approaches lack a validated method to identify individuals as MCI or demented; one such approach (Klee et al. 2024) instead scales prevalence estimates to national OECD estimates, which "suffer from the above-mentioned shortcomings" (O2).
- **Evidence**: paper.pdf pp.1–2 (Introduction), citing refs 12 (SHARE data resource profile), 13 (Klee et al. 2024), 15–17 (ML-based approaches).
- **Implication**: A validated, harmonized classification method — not reliant on rescaling to non-harmonized external estimates — is missing for SHARE-wide prevalence estimation.

### O4: The 2022 SHARE Wave 9 + SHARE-HCAP validation design
- **Statement**: Wave 9 of the SHARE parent study (data collection October 2021–September 2022) includes individuals aged 65 and older across 28 SHARE units (27 European countries + Israel); the SHARE-HCAP validation subsample was drawn from five countries representing East (Czech Republic), West (France, Germany), North (Denmark) and South (Italy) Europe, oversampling low word-recall scorers, collected May–November 2022, achieving a 75.8% response rate.
- **Evidence**: paper.pdf pp.2–3 (Methods) — "Of the 3,546 eligible individuals, 2,687 participated in the SHARE-HCAP study, resulting in an overall response rate of 75.8% (Table 1)."
- **Implication**: The paper's methodological core is a four-step design (draw an HCAP validation subsample → classify it via a validated protocol → relate the classification to cognition items shared with the SHARE parent study → predict cognitive-status probabilities for the full parent sample) rather than a single cross-sectional measurement.

### O5: New estimates reveal larger and more varied prevalence than previously reported
- **Statement**: Dementia prevalence ranges from 4.5% in Switzerland to 22.7% in Spain (Abstract), and MCI prevalence ranges from 17.2% in Sweden to 31.1% in Portugal — with prevalence rates "much higher than previously reported" in the Mediterranean and Southeastern European countries.
- **Evidence**: paper.pdf p.1 (Abstract); p.4 (Results) — "Prevalence rates are particularly high in the Mediterranean and Southeastern countries, much higher than previously reported."
- **Implication**: Existing (non-HCAP-validated) European estimates likely understate both the level and the cross-national variation of cognitive impairment, "with potential adverse consequences for healthcare planning and prevention" (p.6, Discussion).

### O6: Childhood education is strongly and plausibly associated with cross-national variation
- **Statement**: An increase in the age- and sex-adjusted level of education is associated with a decrease in the risk of both MCI and dementia (all pairwise group-difference p-values below 0.0001, Table 4); a counterfactual simulation equalizing education across countries dramatically compresses the cross-national variation in dementia prevalence (Figure 2).
- **Evidence**: paper.pdf p.5 (Results) — "An important finding is the strong association on the international level between cognitive performance and the respondents' educational achievement when they were young... all p-values below 0.0001"; p.6 — "Figure 2 shows how the probability of dementia would vary counterfactually... This variation is dramatically smaller than the actual variation."
- **Implication**: Differences in national education systems when SHARE respondents were young are proposed as a major driver of the international variation in MCI/dementia prevalence, "a potential anchor for preventative measures" (p.2, p.6).

## Gaps

### G1: No validated classification base existed for SHARE-wide dementia/MCI prevalence
- **Statement**: Prior SHARE-based ML approaches to identifying probable dementia lacked a validated ground truth; the one validation route used (scaling to OECD national estimates) inherits OECD's own harmonization shortcomings.
- **Caused by**: O2, O3.
- **Existing attempts**: Unsupervised ML clustering approaches (de Cleret et al. 2018, 2020; Gharbi-Meliani et al. 2023) and OECD-rescaled ML prevalence (Klee et al. 2024, using the 2017 SHARE wave and a Langa-Weir-scale variant).
- **Why they fail**: These approaches either have no independent clinical validation of the MCI/dementia boundary, or import the comparability problems of the very OECD/systematic-review estimates the field is trying to improve on.

### G2: Central and Eastern European countries were data-poor, requiring imputation in earlier consortium studies
- **Statement**: Population studies of dementia prevalence have been "scarce or missing completely" in certain regions, particularly Central and Eastern Europe, so earlier consortium estimates had to impute missing country data from neighboring countries.
- **Caused by**: O2.
- **Existing attempts**: EURODEM, EuroCoDe, and related consortium reviews (refs 3–9).
- **Why they fail**: Imputation from neighbors does not capture actual within-region heterogeneity, and — per this paper's results (O5) — likely understated prevalence in exactly these regions (Mediterranean/Southeastern/Eastern Europe).

### G3: MCI/CIND is comparatively understudied at the European multi-country level
- **Statement**: Recent European-wide studies have focused on dementia diagnosis or been limited to selected countries, without a comparably harmonized measurement of MCI (CIND) across all countries.
- **Caused by**: O3.
- **Existing attempts**: Country-limited or dementia-only European studies (not individually enumerated in the source beyond general reference).
- **Why they fail**: Without MCI measurement, the field lacks a comprehensive understanding of preclinical stages of dementia across Europe, limiting early-stage prevention research.

## Key Insight
- **Insight**: An internationally harmonized cognitive-assessment protocol (HCAP) — already used to validate US dementia/MCI prevalence estimates (Manly et al. 2022) and adopted by other HCAP-network aging studies — can be administered to a representative multi-country SHARE subsample and used as a validation base; a regression-based approach (following Hurd et al. 2013) can then transfer this validated classification to the entire 28-unit SHARE parent sample by relating HCAP classification to cognition/health/demographic items available in both samples, yielding prevalence estimates that are simultaneously (a) validated against standard clinical diagnostic criteria and (b) available for all 28 SHARE countries and Israel without OECD-rescaling or cross-country imputation.
- **Derived from**: O3, O4, G1.
- **Enables**: A four-step estimation pipeline (validation subsample → HCAP classification → regression-based relation → full-sample prediction, see `logic/solution/study_design.md`) that produces the paper's main result (Table 3) and supports downstream face-validity checks against age, sex, education, and comorbidities (Table 4, Figure 1) and an education-standardization counterfactual (Figure 2).

## Assumptions
- A1: The five SHARE-HCAP countries (Czech Republic, France, Germany, Denmark, Italy) are sufficiently representative to act as validation for the European context and to provide cognition-item weights that apply to all 27 European countries and Israel — explicitly flagged by the authors as a limitation given "substantial inhomogeneity within these five countries" (p.7, Discussion).
- A2: The Manly et al. (2022) classification thresholds, developed and calibrated in a US context, apply equally to all SHARE countries; the authors note there is no "gold standard" European calibration target analogous to the US ADAMS study, and prefer this assumption to relying on estimates with the shortcomings described under O2.
- A3: The regression-based relation between SHARE-HCAP classification and shared SHARE-parent cognition/health items (Hurd et al. 2013 approach) is sufficiently accurate and consistent to extend classification to the full parent sample; the authors argue Table 2's close correspondence between classified and predicted prevalence supports this.
- A4: Non-response bias — higher among individuals with dementia — is adequately mitigated via proxy interviews (3.1% of Wave 9 respondents) and by following individuals into nursing homes/institutions where proxies include nurses, though the authors acknowledge results "may underestimate the prevalence of dementia" despite these efforts (p.7, Discussion).
