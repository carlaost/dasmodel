# Study Design

Source: Methods §"Study participants", §"Collection of human samples", §"Statistics & Reproducibility".

## Cohorts

- Retrospective cohort of **173 patients** enrolled at the Section of Neurology, University of
  Perugia, split into a **discovery cohort (n = 55)** and a **validation cohort (n = 118)**.
- **Discovery groups**: NDC (n = 15), MCI-AD (n = 21), AD-dem (n = 19). (No pre-AD or FTD.)
- **Validation groups**: NDC (n = 24), pre-AD (n = 19), MCI-AD (n = 20), AD-dem (n = 16),
  FTD (n = 39).
- (Full demographics — age, sex, MMSE, CDR, years of education — in Table 1.)

## Classification (A/T/N framework)

- All patients underwent standardized assessment: medical history, physical/neurological exam,
  laboratory tests, neuropsychological evaluation including MMSE; brain imaging (CT/MRI) or
  ¹⁸F-FDG-PET in selected cases.
- Core CSF AD biomarkers (Aβ42, Aβ40, Aβ42/Aβ40, p-tau181, t-tau) measured with **Lumipulse G600II
  (Fujirebio)**. A/T/N classification (Jack et al., NIA-AA framework, ref 47).
- **Cut-off values**: Aβ42/Aβ40 = **0.072** (95% CI 0.07–0.074); p-tau181 = **50** (95% CI
  46.2–52.3); t-tau = **393** (95% CI 359–396) (ref 48).
- **AD continuum** = A+/T+ CSF profile. Clinical stage set by neuropsychological assessment + CDR.
  - **pre-AD** (preclinical AD): subjective cognitive complaints not confirmed by neuropsychological
    assessment, but with A+/T+ CSF profile.
  - **MCI-AD**: mild cognitive impairment due to AD.
  - **AD-dem**: AD at dementia stage.
- **FTD** (validation only, n = 39): diagnosis supported by ¹⁸F-FDG-PET (refs 49, 50).
- **NDC (control)**: cognitively normal patients with minor neurological disorders (headache,
  psychiatric disorders, mononeuropathies) other than inflammatory/degenerative CNS or peripheral
  nervous system disease, and MCI attributed to cerebrovascular disease; all **A−/T−/N−**.

## Sample collection & handling

- CSF and plasma collected **2012–2021**, international guidelines, same SOP throughout.
- LP and blood sampling **8:00–10:00 a.m. after overnight fasting**.
- CSF: sterile polypropylene tubes, centrifuged 10 min at 2000 × g at room temperature.
- Whole blood: sterile polypropylene tubes with EDTA anticoagulant, centrifuged 10 min at 2000 × g
  (RT) to obtain plasma.
- Processed CSF/plasma stored in 0.5 mL tubes (72.730.007, Sarstedt, Germany), frozen at **−80 °C**.

## Statistical analysis plan

- Continuous variables: median ± 1st–3rd quartile (Q1–Q3).
- Software: **GraphPad Prism 9.5.0**; **R 4.2.2**.
- Power analysis: minimum **4–8 participants per group** to achieve β = 0.2 and α = 0.05 for
  detecting true differences between AD-dem and NDC (estimates from plasma p-tau181/217/231, refs 18, 22).
- In-house Quanterix software for curve fitting and extrapolation from raw **AEB** signal.
- Two-tailed **p < 0.05** considered significant.
- Normality: **D'Agostino–Pearson omnibus K2** test.
- Group comparisons: **Kruskal–Wallis** + **Dunn's post-hoc** (p adjusted for multiple comparisons).
- Categorical prevalence differences: **chi-squared** test.
- Correlations: **Spearman's** correlation coefficient.
- Diagnostic accuracy: **ROC**; 95% CI of AUC via **Wilson/Brown** method; AUC comparison via
  **DeLong** test (**pROC** R package).
- Median concentration fold change = median(AD continuum group) / median(control group).
- Standardized effect size: **Cohen's d** (**effsize** R package); large d > 0.8, medium d > 0.5,
  small d > 0.2, negligible < 0.2 (ref 54).

## Ethics

- Conducted per Declaration of Helsinki and ICH Good Clinical Practice.
- Informed written consent for LP and study inclusion.
- Approved by local Ethics Committee (Comitato Etico Aziende Sanitarie Regione Umbria 19369/AV and
  20942/21/OV).
- Blinding: samples anonymized; researcher performing measurements blinded to patients' clinical
  profile.
