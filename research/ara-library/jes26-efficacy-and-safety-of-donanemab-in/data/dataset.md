# Dataset

## Primary dataset — TRAILBLAZER-ALZ 2 individual participant data (IPD)
- **Provenance**: Phase 3 randomised, double-blind, multicentre, placebo-controlled trial of donanemab in early symptomatic AD (NCT04437511), sponsored by Eli Lilly and Company. Primary report: Sims et al. 2023 (JAMA) [2].
- **Source / access**: On request via **Vivli** (www.vivli.org) — controlled/request access. Per the article Data statement: Lilly provides access to all IPD collected during the trial after anonymization, **excluding pharmacokinetic and genetic data**. Available 6 months after the indication is approved in the US and EU and after primary publication acceptance (whichever is later); requires approval by an independent review committee and a signed data-sharing agreement; delivered in a secure data-sharing environment with study protocol, SAP, CSR, and blank/annotated CRFs. Verified in `sources.yaml` (data[], access=request, verified=true).
- **Size (this analysis)**:
  - Randomised in 76-week placebo-controlled period: 1736; APOE ε4 non-homozygotes: 1447.
  - EU-eligible population (efficacy, Table 1): placebo N=604, donanemab N=614.
  - EU-eligible safety population (Table 4): placebo N=603, donanemab N=609.
- **Licensing / ethics**: Conducted per Declaration of Helsinki and ICH GCP; independent ethics committee/IRB approval at each site; written informed consent from participants and study partners. No animal studies.
- **Key variables**: Clinical scales (iADRS, CDR-SB and 6 domains, CDR-G, ADAS-Cog13, ADCS-iADL, MMSE); biomarkers (amyloid PET Centiloids, plasma P-tau217, ¹⁸F-flortaucipir tau); APOE ε4 genotype; demographics; baseline BP, superficial siderosis, anticoagulant use (used to define EU-eligibility); safety/TEAE/ARIA data.
- **Notable subset definitions**: EU-indicated = APOE ε4 non-homozygotes; EU-eligible = EU-indicated minus baseline superficial siderosis, anticoagulant use, or uncontrolled hypertension (seated systolic BP ≥140 and diastolic BP ≥90 mmHg); low-medium tau subpopulation by ¹⁸F-flortaucipir PET.

## External comparison dataset — ADNI
- **Provenance**: Alzheimer's Disease Neuroimaging Initiative (adni.loni.usc.edu), funded by NIA (NIH Grant U19AG024904), with contributions from many public/private partners (see Acknowledgements).
- **Use**: Untreated external comparison cohort for the LTE (no internal placebo). Propensity score weighting balanced baseline disease characteristics against TRAILBLAZER-ALZ 2 arms (per Zimmer et al. [7]).
- **Access**: Via ADNI's data application process.
- **Limitation**: Superficial siderosis, anticoagulant use, and blood pressure were **not collected** in ADNI, so an EU-eligible propensity-weighted control could not be built; LTE analyses used the non-homozygote population. May differ from the LTE cohort in study conduct, era, geography, and unmeasured confounders.
