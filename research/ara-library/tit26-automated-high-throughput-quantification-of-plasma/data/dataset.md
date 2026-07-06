# Dataset

## Cognitive Centre Ghent University (CCUG) biobank
- **Provenance**: Ghent University Hospital, Cognitive Centre, Department of Neurology. Ongoing prospective biobank initiated in 2021, collecting blood and CSF plus clinical, neuropsychological, and imaging data from patients referred for cognitive-complaint evaluation.
- **Access type**: **request** (verified in sources.yaml). Data Availability statement (verbatim): "The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request." No public accession identifier; no released code repository.
- **Included sample (this study)**: n = 187 consecutively enrolled participants with available plasma up to data extraction.
  - AD: n = 103; non-AD cognitive disorders: n = 84 (ND n = 54, PSY n = 30).
  - Additionally identified but excluded from primary comparisons: 16 discordant-CSF cases (15 A+T−N−, 1 other).
  - Longitudinal subset: 69 AD patients with follow-up (median 2.1 years) for MoCA modelling.
- **Population**: Predominantly Belgian background; memory-clinic (secondary care) referrals; median age ~70–72 years.
- **Reference-standard labelling**: AD vs non-AD by CSF biomarkers (n = 180) or amyloid-PET (n = 7).
- **Consent/ethics**: Written informed consent (or legal representative); ethics approval ONZ-2024-0422 (Ghent University Hospital); Declaration of Helsinki.

## Variables
- **Plasma biomarkers**: Elecsys p-tau181, Elecsys p-tau217, APOE-ε4 carrier status (Roche); Lumipulse p-tau217, Aβ42, Aβ40 (Fujirebio); plasma creatinine → eGFR.
- **CSF biomarkers (reference)**: Aβ42, Aβ42/40 ratio, p-tau181, total tau (Lumipulse).
- **Clinical/imaging**: age, sex, baseline MoCA, longitudinal MoCA, eGFR, Fazekas grade (white-matter hyperintensities), lobar microbleeds (MRI, CAA indicator).
- **Derived**: p-tau217/Aβ42, p-tau217/(Aβ42/Aβ40) ratios.

## Preprocessing / QC (see logic/solution/assay_and_analysis.md for full protocol)
- K2 EDTA plasma, centrifuged and stored at −80 °C; standardized biobank procedures.
- Analytical QC per CLSI EP15-A3; samples below LLOQ interpreted at the LLOQ value (5/187 p-tau217 samples below LOQ 0.10 pg/mL).
- CSF measured blinded; classification by validated reference-lab cut-offs.
