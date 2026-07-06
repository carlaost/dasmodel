# Problem Specification

> Grounding: abstract-only. Observations are copied from the provided abstract/metadata. Full-text methods, inclusion criteria, and source tables are not available from provided input.

## Observations

### O01: The review covers a broad digital-biomarker literature
- **Statement**: The review conducts a bibliometric analysis of 431 studies from five online databases: Web of Science, PubMed, Embase, IEEE Xplore, and CINAHL.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: The paper positions itself as a landscape-level synthesis rather than a single-model empirical study.

### O02: The AI-model subset is smaller than the bibliometric corpus
- **Statement**: The abstract reports a scoping review of 86 artificial intelligence models.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: AI-model evidence is a curated subset of the larger digital-biomarker literature.

### O03: The research ecosystem is geographically and institutionally distributed
- **Statement**: The field is reported as supported by 224 grants across 54 disciplines and 1403 institutions in 44 countries, with 2571 contributing researchers.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: Digital biomarkers for AD are multidisciplinary and internationally distributed.

### O04: The review identifies four key focus areas
- **Statement**: Key focuses include motor activity, neurocognitive tests, eye tracking, and speech analysis.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: The reviewed digital biomarkers are organized around behavioral, cognitive, ocular, and speech signals.

### O05: AI model reporting and validation remain limited
- **Statement**: Classical machine learning models dominate AI research, many models lack performance reporting, only 2 studies incorporated external validation, and 3 studies performed model calibration.
- **Evidence**: metadata.md:13 abstract.
- **Implication**: Translation into clinical practice is constrained by incomplete performance reporting and sparse validation/calibration.

## Gaps

### G01: Full reproducibility details are unavailable
- **Statement**: Search strings, eligibility criteria, extraction forms, study-level data, and model-level tables are not available from provided input.
- **Caused by**: Abstract-only source availability.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

### G02: Clinical-readiness evidence appears sparse
- **Statement**: The abstract reports only 2 externally validated studies and 3 calibrated studies among the scoped AI-model literature.
- **Caused by**: O05.
- **Existing attempts**: External validation and calibration in a small subset of studies.
- **Why they fail**: The abstract does not provide enough detail to assess study quality, cohort independence, calibration method, or deployment readiness.

## Key Insight
- **Insight**: A landscape review can expose both the breadth of AD digital-biomarker research and the translation bottleneck: many AI models exist, but reporting, external validation, and calibration remain limited.
- **Derived from**: O01-O05.
- **Enables**: Source-bounded mapping of claims about literature scale, focus areas, model performance summaries, and validation/calibration gaps.

## Assumptions
- A1: Counts and averages in the abstract are treated as review results.
- A2: No table, figure, appendix, or full reference-list claims are inferred without full text.
- A3: "Classical machine learning models dominate" is retained as an abstract-supported qualitative claim; exact model-family counts are not available from provided input.
