# Problem Specification

## Observations

### O1: Donanemab is EU-approved only for APOE ε4 non-carriers and heterozygotes, with additional contraindications
- **Statement**: In the EU, donanemab is indicated for adults with early symptomatic Alzheimer's disease who are apolipoprotein E (APOE) ε4 non-carriers or heterozygotes; among these, eligibility in clinical practice further excludes patients with superficial siderosis at baseline, concomitant anticoagulant use, or uncontrolled hypertension (systolic BP ≥140 mmHg and diastolic BP ≥90 mmHg).
- **Evidence**: Abstract; §1 Introduction; §2.1. (`paper.pdf` p1–2)
- **Implication**: The population expected to receive donanemab in European clinical practice ("EU-eligible") differs from the full randomised TRAILBLAZER-ALZ 2 population, so the pivotal trial's overall estimates do not directly describe the treated European population.

### O2: ARIA risk increases with the number of APOE ε4 alleles
- **Statement**: The risk of amyloid-related imaging abnormalities (ARIA), a known treatment-related adverse event of amyloid-targeting therapies, increases with increasing number of APOE ε4 alleles; this is the rationale for excluding APOE ε4 homozygotes from the indicated population.
- **Evidence**: §1 Introduction, refs [2,6]. (`paper.pdf` p2)
- **Implication**: Restricting treatment to non-homozygotes and excluding contraindicated patients should lower ARIA rates versus the overall trial population, changing the benefit–risk balance.

### O3: The EMA required a conservative missing-data handling method for the indicated population
- **Statement**: For the EU-indicated population, the EMA's Committee for Medicinal Products for Human Use required a hybrid imputation method combining jump-to-reference (J2R) and copy increment reference (CIR) to handle missing values, which is more conservative than the trial's original methodology (no imputation).
- **Evidence**: §1; §2.2. (`paper.pdf` p2)
- **Implication**: Efficacy in the EU-eligible population must be re-estimated under this conservative estimand to be regulatory-relevant, rather than relying on the original analysis.

### O4: The pivotal TRAILBLAZER-ALZ 2 report and its LTE did not isolate the EU-eligible subpopulation
- **Statement**: The primary TRAILBLAZER-ALZ 2 report (Sims et al. [2]) and the long-term extension (LTE) report (Zimmer et al. [7]) characterised the overall population and the APOE ε4 non-carrier/heterozygote population, but did not report efficacy and safety specifically for the EU-eligible subpopulation defined by EU contraindications.
- **Evidence**: §1; §2.1; §2.2. (`paper.pdf` p2)
- **Implication**: A dedicated post-hoc analysis is needed to inform European benefit–risk and shared decision-making, complementing the EU summary of product characteristics [5].

## Gaps

### G1: No efficacy/safety estimates specific to the EU-eligible treated population
- **Statement**: Clinicians in Europe lacked donanemab efficacy and safety estimates computed specifically for the population they will actually treat (non-homozygotes without EU contraindications), under the conservative estimand the regulator uses.
- **Caused by**: O1, O3, O4
- **Existing attempts**: Overall and indicated-population results from the pivotal trial [2] and LTE [7]; EU summary of product characteristics [5].
- **Why they fail**: They do not remove EU-contraindicated patients, do not consistently apply the EMA-required hybrid imputation to the eligible subset, and (for the LTE) an EU-eligible external control could not be constructed because siderosis, anticoagulant use, and blood pressure were not collected in the ADNI dataset.

### G2: Long-term durability of benefit in non-homozygotes with limited-duration dosing is uncharacterised for this subgroup
- **Statement**: Whether the treatment effect continues to increase beyond the 76-week placebo-controlled period, and whether amyloid clearance is maintained after treatment-course completion, was not established specifically for APOE ε4 non-carriers and heterozygotes.
- **Caused by**: O4
- **Existing attempts**: LTE analyses of the broader population [7].
- **Why they fail**: The LTE had no internal placebo comparator; long-term efficacy in this subgroup required an external propensity-weighted comparison (ADNI).

## Key Insight
- **Insight**: Re-analysing the existing TRAILBLAZER-ALZ 2 data restricted to the EU-eligible subpopulation, using the EMA-required conservative hybrid J2R/CIR imputation (and, for the LTE, a propensity-weighted ADNI external control for the non-carrier/heterozygote population), yields regulator-relevant, clinically actionable benefit–risk estimates for the patients actually treated in Europe.
- **Derived from**: O1, O2, O3, O4
- **Enables**: Direct estimation of clinical, biomarker, and safety outcomes for the EU-eligible population, and demonstration that reduced ARIA risk co-occurs with preserved efficacy.

## Assumptions
- A1: The EU-eligible subpopulation, defined post-hoc from baseline covariates, adequately represents patients expected to be treated in European clinical practice.
- A2: The conservative hybrid J2R/CIR imputation appropriately handles missing data caused by serious/severe/symptomatic ARIA or death (J2R) versus all other causes (CIR).
- A3: The propensity-weighted ADNI cohort is an acceptable untreated external comparator for the LTE despite differences in study conduct, era, and geography (a stated limitation).
- A4: Results reflect the TRAILBLAZER-ALZ 2 donanemab dosing regimen, not the more gradual titration to be used in clinical practice.
