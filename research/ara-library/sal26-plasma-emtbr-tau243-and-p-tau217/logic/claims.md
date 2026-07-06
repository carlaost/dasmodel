# Claims

> Grounding: abstract-only. Claims are drawn from the published abstract (Key Points: Findings and
> Meaning). The abstract reports no exact effect sizes (no concordance %, AUC, odds ratios, or
> p-values), so `Statement`s are qualitative/directional and load-bearing numbers are limited to
> the cohort sizes stated in the abstract. Effect-size quantification is "Not available from provided
> input (no full text)."

## C01: Combined plasma model concords with PET-based biological staging
- **Statement**: In 872 BioFINDER-2 participants, a plasma model combining %p-tau217 and
  eMTBR-tau243 shows strong concordance with an amyloid- and tau-PET–based AD biological staging
  scheme, with replication in 156 independent Knight ADRC participants.
- **Status**: supported (per abstract; effect sizes not available from provided input)
- **Falsification criteria**: The combined plasma model does not agree with PET-based biological
  stage above chance / above the single-marker baseline in either cohort.
- **Proof**: [E01, E04]
- **Evidence basis**: Abstract states the combined model "showed strong concordance with PET-based
  biological staging" across the stated cohorts. No numeric concordance statistic is available from
  the provided input.
- **Interpretation**: Blood biomarkers may substitute for PET in assigning AD biological stage; the
  strength of substitution cannot be quantified without the full text.
- **Dependencies**: none
- **Sources**:
  - 872 ← metadata.md (Abstract, Findings) «In 872 BioFINDER-2 participants and 156 independent Knight Alzheimer Disease Research Center participants, a plasma model combining %p-tau217 and eMTBR-tau243 showed strong concordance with PET-based biological staging» [input]
  - 156 ← metadata.md (Abstract, Findings) «and 156 independent Knight Alzheimer Disease Research Center participants» [input]
- **Tags**: plasma biomarkers, biological staging, concordance, PET

## C02: Combined model outperforms %p-tau217-only, especially at the intermediate tau stage
- **Statement**: The combined %p-tau217 + eMTBR-tau243 plasma model outperforms a %p-tau217-only
  plasma model at approximating PET-based staging, particularly for identifying the intermediate tau
  stage.
- **Status**: supported (per abstract; effect sizes not available from provided input)
- **Falsification criteria**: A %p-tau217-only model matches or exceeds the combined model at
  identifying the intermediate tau stage (or overall staging).
- **Proof**: [E02, E04]
- **Evidence basis**: Abstract states the combined model "outperformed a %p-tau217–only model,
  particularly for identifying the intermediate tau stage." No numeric margin is available from the
  provided input.
- **Interpretation**: eMTBR-tau243 adds tau-aggregation information that %p-tau217 alone does not
  capture, resolving the intermediate tau stage; the incremental value is not quantifiable from the
  abstract.
- **Dependencies**: C01
- **Sources**:
  - "outperformed a %p-tau217-only model, particularly for identifying the intermediate tau stage" ← metadata.md (Abstract, Findings) «outperformed a %p-tau217–only model, particularly for identifying the intermediate tau stage» [result]
- **Tags**: model comparison, eMTBR-tau243, intermediate tau stage, incremental value

## C03: Advanced plasma stages track clinical severity, other biomarkers, and neuropathology
- **Statement**: More advanced plasma-defined stages are associated with greater clinical severity,
  greater abnormality of other biomarkers, and greater neuropathologic burden.
- **Status**: supported (per abstract; effect sizes not available from provided input)
- **Falsification criteria**: Plasma stage shows no monotonic association with clinical severity,
  other biomarker abnormalities, or neuropathologic burden.
- **Proof**: [E03]
- **Evidence basis**: Abstract states "Advanced plasma stages also aligned with greater clinical
  severity, other biomarker abnormalities, and neuropathologic burden." No numeric associations are
  available from the provided input.
- **Interpretation**: Plasma stage carries biologically and clinically meaningful signal beyond the
  PET-concordance target, supporting construct validity. Strength/direction detail not available.
- **Dependencies**: C01
- **Sources**:
  - "Advanced plasma stages also aligned with greater clinical severity, other biomarker abnormalities, and neuropathologic burden" ← metadata.md (Abstract, Findings) «Advanced plasma stages also aligned with greater clinical severity, other biomarker abnormalities, and neuropathologic burden» [result]
- **Tags**: clinical severity, neuropathology, construct validity

## C04: Plasma-based staging is a scalable, minimally invasive stratification tool (forward-looking)
- **Statement**: Plasma-based staging may provide a scalable, minimally invasive approach to
  biological stratification of AD, with potential value for treatment selection and clinical trial
  enrichment.
- **Status**: hypothesis (interpretive "Meaning" statement; not directly tested in the abstract's
  reported findings)
- **Falsification criteria**: Plasma staging fails to stratify patients usefully for treatment
  selection or trial enrichment in prospective use.
- **Proof**: [E01, E02, E03]
- **Evidence basis**: Abstract "Meaning" statement asserts potential utility; it is a forward-looking
  interpretation, not an outcome measured in the study.
- **Interpretation**: Positions the combined plasma model as a deployable stratification tool;
  prospective validation of the utility claim is not part of the provided input.
- **Dependencies**: C01, C02, C03
- **Sources**:
  - "scalable, minimally invasive approach ... potential value for treatment selection and clinical trial enrichment" ← metadata.md (Abstract, Meaning) «Plasma-based staging may provide a scalable, minimally invasive approach to biological stratification of Alzheimer disease, with potential value for treatment selection and clinical trial enrichment» [result]
- **Tags**: clinical utility, trial enrichment, treatment selection, scalability
