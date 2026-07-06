# Dataset — AD Pipeline Census (Index Date 1 January 2026)

## Provenance
- **Primary source**: ClinicalTrials.gov, the NIH/NLM clinical-trial registry. Accessed via the
  ClinicalTrials.gov API; raw JSON parsed for >30 key fields; loaded into PostgreSQL databases at the
  UNLV Clinical Trial Observatory and the Cleveland Clinic Laboratory of Network Medicine.
- **Summary mirror**: alzpipeline.com (verified live). Planned deposit: AD Workbench (Gates Ventures'
  AD Data Initiative).
- **Repurposing reference**: DrugBank. **Mechanism/CADRO references**: literature + ALZFORUM.

## Size and scope
- **Index Date**: 1 January 2026.
- **Records**: 192 active AD clinical trials assessing 158 unique drugs.
  - Phase 3: 54 trials / 36 drugs (Table 1)
  - Phase 2: 89 trials / 84 drugs (Table 2)
  - Phase 1: 49 trials / 45 drugs (Table 3)
- **Trials referencing NCTs**: ~190 NCT identifiers appear across Tables 1–3. A verified flagship
  subset of 8 Phase 3 NCTs is recorded in `src/environment.md` and `logic/related_work.md`.

## Variables captured per trial/agent (Tables 1–3 columns)
Agent name; therapeutic purpose (DTT/STT + modality); CADRO target category; mechanism of action;
clinical trial (NCT) identifier(s); lead sponsor; start date; primary completion date. Additional
analysis-level variables: trial phase, status, biomarker use (eligibility/outcome/modality),
population/continuum stage, geography, target enrollment (participants), sponsor type
(industry/non-industry), and repurposing status.

## Licensing / consent / ethics
- All data derive from an anonymized, publicly available registry; no individual participant-level
  data are used. Consent statement: "Not applicable."
- The paper itself is gold open access (CC BY-NC-ND); PMID 42095064, PMCID PMC13140253.

## Quality notes
- Registration of US trials is mandated but not fully standardized; data-entry irregularities are
  possible. Non-North-American-only trials may be under-registered and thus under-captured. See
  `logic/solution/constraints.md`.
