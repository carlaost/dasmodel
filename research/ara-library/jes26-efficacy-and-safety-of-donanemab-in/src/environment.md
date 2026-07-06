# Environment

This is a **post-hoc, analytical** study of existing clinical-trial data. There is no released code
repository (no code-availability statement in the article and none located via search — expected for
a clinical-trial post-hoc analysis; per `sources.yaml`, `code: []`). No concrete code artifact
exists to capture in `src/execution/`.

- **Language/runtime**: Statistical software only — SAS version 9.4 (most analyses); R version 4.3.0 (some time-based progression analyses). No custom code released.
- **Framework**: Standard SAS/R statistical procedures (MMRM, Cox proportional hazards, generalized mixed models, multiple imputation, propensity score weighting, time-progression model for repeated measures). No public analysis scripts.
- **Hardware**: n/a (analytical work).
- **Data sources**:
  - **TRAILBLAZER-ALZ 2 individual participant data** (NCT04437511; sponsor Eli Lilly and Company). Access: **on request via Vivli** (www.vivli.org), controlled/request access. Per the Data statement: "Lilly provides access to all individual participant data collected during the trial, after anonymization, with the exception of pharmacokinetic or genetic data." Available 6 months after the studied indication is approved in the US and EU and after primary publication acceptance (whichever is later), subject to approval by an independent review committee and a signed data-sharing agreement; delivered in a secure data-sharing environment (study protocol, SAP, CSR, blank/annotated CRFs). Verified via `sources.yaml` (data[], access=request, verified=true).
  - **ADNI** (Alzheimer's Disease Neuroimaging Initiative; adni.loni.usc.edu) — external comparison cohort for the LTE (propensity-weighted). Funded by NIA (NIH Grant U19AG024904). Access via ADNI's application process.
- **Key dependencies**: SAS 9.4, R 4.3.0; MedDRA v25.1 for AE coding.
- **Protocols**: TRAILBLAZER-ALZ 2 phase 3 protocol (NCT04437511), conducted per the Declaration of Helsinki and ICH Good Clinical Practice; independent ethics committee/IRB approval at each site; written informed consent. Analyses post-hoc, exploratory, not controlled for multiplicity.
- **Random seeds**: Not specified in paper (multiple-imputation seeds not reported).

## Underlying clinical trial (grounded, from `sources.yaml` — verified)
- **NCT**: NCT04437511
- **Title**: Assessment of Safety, Tolerability, and Efficacy of Donanemab in Early Symptomatic Alzheimer's Disease (TRAILBLAZER-ALZ 2)
- **Phase**: PHASE3 · **Status**: ACTIVE_NOT_RECRUITING · **Sponsor**: Eli Lilly and Company
- **Source**: clinicaltrials.gov (verified=true). Cross-referenced against the paper's Ethical statement (§ "Ethical statement", `paper.pdf` p8) which cites the same NCT.
