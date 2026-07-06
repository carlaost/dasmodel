# Problem Specification

> Grounding: abstract-only. Observations below are limited to what the published abstract (Key
> Points) and verified metadata support. Quantitative detail beyond participant counts is "Not
> available from provided input (no full text)."

## Observations

### O1: PET-based biological staging is the reference standard but is not scalable
- **Statement**: Alzheimer disease can be biologically staged using amyloid and tau positron
  emission tomography (PET); the study frames its plasma model as an approximation of "an amyloid and
  tau positron emission tomography (PET)–based Alzheimer disease biological staging scheme."
- **Evidence**: Abstract, Key Points — Question (metadata.md).
- **Implication**: A reference biological staging scheme exists in imaging but requires PET, which
  motivates a scalable surrogate.

### O2: Two plasma tau species are candidate staging markers
- **Statement**: The study evaluates plasma %p-tau217 and eMTBR-tau243 as the inputs to a
  blood-based staging model.
- **Evidence**: Abstract — Question and Findings (metadata.md); title.
- **Implication**: These two analytes are hypothesized to carry complementary staging information.

### O3: The analysis was performed in a large primary cohort and an independent validation cohort
- **Statement**: The evaluation used 872 BioFINDER-2 participants and 156 independent Knight
  Alzheimer Disease Research Center participants.
- **Evidence**: Abstract — Findings (metadata.md); `sources.yaml` (data cohorts).
- **Implication**: Findings are tested for external generalizability across two cohorts.

## Gaps

### G1: No scalable, minimally invasive substitute for PET-based AD biological staging
- **Statement**: Biological staging of AD relies on PET imaging, which is costly and not broadly
  accessible; a blood-based equivalent is needed.
- **Caused by**: O1.
- **Existing attempts**: Plasma %p-tau217 alone has been used as a blood marker of AD pathology
  (the study includes it as the comparison model).
- **Why they fail**: A %p-tau217-only model is reported to be outperformed by the combined model,
  "particularly for identifying the intermediate tau stage" — i.e., single-marker plasma staging is
  weaker at the intermediate tau stage. Detailed failure quantification: Not available from provided
  input (no full text).

### G2: Intermediate tau stage is hard to identify from a single plasma marker
- **Statement**: Identifying the intermediate tau stage is the specific regime where the abstract
  reports the combined model's advantage over the %p-tau217-only model.
- **Caused by**: O2, G1.
- **Existing attempts**: %p-tau217-only staging.
- **Why they fail**: Reported to underperform the combined model at the intermediate tau stage;
  mechanism/quantification not available from provided input (no full text).

## Key Insight
- **Insight**: Adding eMTBR-tau243 — a tau microtubule-binding-region species associated with tau
  aggregation/tangle burden — to %p-tau217 lets a purely plasma-based model approximate a PET-based
  amyloid+tau biological staging scheme, especially resolving the intermediate tau stage that a
  single amyloid-associated marker (%p-tau217) misses.
- **Derived from**: O1, O2, G1, G2.
- **Enables**: A scalable, minimally invasive staging tool for stratification, treatment selection,
  and clinical trial enrichment.

## Assumptions
- A1: PET-based amyloid+tau biological staging is a valid reference standard for AD biological stage.
- A2: Plasma %p-tau217 primarily tracks amyloid/early-phosphorylation pathology and eMTBR-tau243
  tracks tau-aggregation burden, so the two are complementary. (Reconstructed from abstract framing;
  detailed rationale not available from provided input.)
- A3: The BioFINDER-2 and Knight ADRC cohorts are representative enough for the staging model to
  generalize.
