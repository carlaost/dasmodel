# Environment

This is an observational clinical biomarker-validation study. There is **no code repository**
(no Code Availability statement; no GitHub/GitLab/Zenodo/OSF repo found via publisher/PMC/web
search — verified in sources.yaml). The "environment" is the analytical software, laboratory
platforms, and data cohorts used.

- **Language/runtime**:
  - R — RStudio v2024.12.0 (Posit Software, PBC) for main statistics and plots.
  - Python 3.6 (Jupyter Notebook platform) for pre-analytical sample-handling analysis.
- **Framework / key libraries**:
  - Python: `scipy`, `scikit_posthocs` (Nemenyi post hoc), plus custom-written code.
  - R: custom scripts (specific packages not named in paper).
- **Statistical methods**: Spearman rank correlation (rho); Passing–Bablok regression; Wilcoxon signed-rank test; Shapiro–Wilk normality test; DeLong test (AUC comparison); Akaike information criterion (AIC; reduction ≥ 20 deemed significant); logistic regression (ROC/AUC with 95% CI); Friedman test with Nemenyi post hoc (α = 0.05); multiple linear regression (log-transformed p-tau217); CKD-EPI 2021 creatinine eGFR equation.
- **Hardware / laboratory platforms**:
  - Lumipulse G1200 fully automated immunoassay platform (Fujirebio Europe) — plasma p-tau217, LLOQ 0.03 pg/mL (CV < 10%); also CSF Aβ42/Aβ40 and p-tau181 (G1200; Innotest ELISA for earlier CSF samples Aug 2017–Mar 2020).
  - Simoa HD-X immunoassay platform (Quanterix) — ALZpath p-tau217 v2 kit, LLOQ 0.06 pg/mL. Acquired via National Brain Appeal and UCLH Charity funding.
  - Siemens Biograph 64 PET/CT scanner — ¹⁸F-florbetaben amyloid PET.
- **Data sources** (all UK cohorts; controlled / on-request access — verified, sources.yaml):
  - **Wolfson CSF study** — ethics 12/0344 (NRES London Queen Square, Aug 2013, PI Schott). Repository: UCL, on request. Access: **request**. Role: CSF derivation cohort (n = 257) + pre-analytical handling experiments.
  - **Biomarkers and Genetics in Dementia study** — ethics 03/N049 (NRES London, Apr 2003, PI Fox). Repository: UCL, on request. Access: **request**. Role: pre-analytical handling experiments (n = 40).
  - **Imperial Amyloid PET Cohort Study** — ethics 20/LO/0442 (NRES London Camden and Kings Cross, June 2020, PI Malhotra). Repository: Imperial College London, on request. Access: **request**. Role: amyloid PET validation cohort (n = 76) + transport comparison (n = 10).
  - **Polycystic Kidney Disease (PKD) Biobank / CN-CKD cohort** — ethics 05/Q0508/6, sponsored by PKD Charity at Royal Free (identifier null in sources.yaml). Repository: UCL / Royal Free, on request. Access: **request**. Role: renal-function analysis (n = 58 CN-CKD, stages G1–G4, aged < 60).
  - **Data availability statement (verified, PMC12917852)**: "The anonymized data that support the findings of this study are available on request from qualified academic investigators, after approval of a proposal and with a signed data access agreement." Contact: a.keshavan@ucl.ac.uk.
- **Sample-collection reagents**: K2-EDTA (8 mL, CSF cohort & handling experiments; K2-EDTA CKD cohort) and K3-EDTA (4 mL, amyloid PET cohort) tubes; storage −80°C (or −20°C / 2–8°C per protocol experiments).
- **Consent/ethics**: All participants provided written informed consent (or assent via consultees). Ethics per the four cohort approvals above.
- **Funding**: Alzheimer's Research UK / Blood Biomarker Challenge, grant **ARUK-BBC2023-002** (funding partners: Alzheimer's Society, Alzheimer's Research UK, Postcode Innovation Trust, People's Postcode Lottery, National Institute for Health and Social Care Research). Additional support: UCLH NIHR BRC; UK Dementia Research Institute (UKDRI-1003); NIHR UCLH BRC; National Brain Appeal / UCLH Charity (Simoa HD-X).
- **Random seeds**: Not applicable / not specified (no stochastic model training).
- **Protocols**: Analysis protocol as described in §2 Methods; the derived sample-handling protocol (heuristics.md) is the operational output for ADAPT stage-3 trial sites.
- **IDs**: DOI 10.1002/alz.71147; PMID 41711262; PMCID PMC12917852; medRxiv preprint DOI 10.1101/2025.09.08.25335317.

## Related future study (not part of this artifact's data)
The **ADAPT stage-3 randomized controlled trial** (disclosure of plasma p-tau217 results to ~1,100
UK memory-clinic patients across ~20 NHS centres; first site Essex Partnership University NHS FT,
recruiting from Aug 2025) is a **separate, future, unregistered** study within the same ADAPT
programme. No NCT/ISRCTN identifier is cited in this paper, so it is not recorded as a clinical
trial for this artifact.
