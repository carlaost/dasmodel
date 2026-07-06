# Constraints, Assumptions, and Limitations

## Boundary conditions
- **Snapshot in time**: All counts are a census on the single Index Date of 1 January 2026. Trials
  completing before, or registered after, that date are excluded. The picture changes annually.
- **Pharmacological interventions only**: Devices, gene therapies, stem-cell therapies, exercise,
  lifestyle/cognitive-behavioral/caregiver interventions, supplements, medical foods, and
  intervention-free biomarker trials are excluded. Phase 0 and Phase 4 trials are excluded.
- **AD-specific populations only**: Trials with mixed/non-AD dementias, or MCI from a non-AD cause,
  are excluded.

## Assumptions (see problem.md A1–A4)
- Registry registration is a valid, reasonably comprehensive proxy for the active pipeline.
- Declared therapeutic intent, sponsor, and mechanism (supplemented by literature/ALZFORUM) correctly
  reflect each agent's DTT/STT class and CADRO target.
- Higher-phase assignment for two-phase trials; each novel agent counted once.

## Known limitations (stated in §4 Discussion and §2)
- **Not exhaustive**: ClinicalTrials.gov is comprehensive but not complete; some drugs in trials —
  particularly those conducted at non-North American sites — may not be registered and are not
  included. The 158/192 counts are therefore a lower bound on true global activity.
- **Data-entry irregularity**: Registration of US trials is mandated but not completely
  standardized; irregularities in data entry could affect the report.
- **Classification ambiguity**: DTT vs STT and CADRO categories are assigned from registry text,
  sponsor information, and published reports; these may not accurately characterize the intended
  purpose of all compounds. Some agents have multiple mechanisms and/or both DTT and STT properties.
- **Overlapping population categories**: Continuum-stage categories are not mutually exclusive, so
  per-stage trial counts can sum to more than the number of active trials (>100%).
- **Curation/interpretation error**: Although the database team follows good data-management and
  governance practice, errors in data capture or interpretation are possible.
- **No efficacy inference**: The review characterizes pipeline composition and trajectory; it does
  not evaluate the efficacy or safety of any individual agent. There have been no new AD drug
  approvals since 2023, and the overall late-stage failure rate remains high.
