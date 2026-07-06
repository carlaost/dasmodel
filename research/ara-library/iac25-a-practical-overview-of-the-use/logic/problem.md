# Problem Specification

> Grounding: abstract-only. Source is `research/data/lib/iac25-a-practical-overview-of-the-use/metadata.md`; no full text, PDF, figures, tables, or reference list were provided.

## Observations

### O01: Amyloid-PET quantitation is increasingly used
- **Statement**: Amyloid-PET quantitation is increasingly adopted in research and clinical trials.
- **Evidence**: metadata.md abstract highlight: "Amyloid-PET quantitation is increasingly adopted in research and clinical trials."
- **Implication**: Practical guidance on quantitative amyloid-PET values is relevant to both trial and research workflows.

### O02: Centiloid is positioned as a harmonization scale
- **Statement**: The Centiloid scale harmonizes amyloid-PET data from different tracers and methods.
- **Evidence**: metadata.md abstract highlight: "The Centiloid scale harmonizes amyloid-PET data from different tracers and methods."
- **Implication**: A common scale can reduce incompatibility between tracer-specific or method-specific PET measurements.

### O03: Comparable truth standards produce similar thresholds
- **Statement**: Studies with comparable standards of truth reported similar Centiloid thresholds.
- **Evidence**: metadata.md abstract highlight: "Studies with comparable standards of truth reported similar Centiloid thresholds."
- **Implication**: Threshold interpretation depends on the standard of truth used, but comparable validation targets may converge.

### O04: Interpretation requires methodological caution
- **Statement**: Methodological caveats should be considered when interpreting Centiloid values.
- **Evidence**: metadata.md abstract highlight: "Methodological caveats should be considered when interpreting Centiloid values."
- **Implication**: The paper does not present Centiloid values as context-free measurements; methodological conditions affect interpretation.

## Gaps

### G01: Cross-tracer and cross-method comparability
- **Statement**: Amyloid-PET values from different tracers and quantitation methods need harmonization before they can be compared across studies or trials.
- **Caused by**: O01, O02
- **Existing attempts**: Centiloid scaling, per the abstract.
- **Why they fail**: Not available from provided input.

### G02: Threshold portability depends on validation target
- **Statement**: Centiloid thresholds are only presented as similar when studies use comparable standards of truth.
- **Caused by**: O03
- **Existing attempts**: Threshold studies using standards of truth.
- **Why they fail**: Not available from provided input.

### G03: Robust use still requires caveat-aware interpretation
- **Statement**: Even if Centiloid values can support patient selection and characterization, the abstract flags methodological caveats as necessary for interpretation.
- **Caused by**: O04
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

## Key Insight
- **Insight**: A harmonized Centiloid framework can make amyloid-PET quantitation practically useful across tracers and methods, but only when thresholds and interpretations are tied to comparable truth standards and methodological caveats.
- **Derived from**: O01, O02, O03, O04
- **Enables**: Caveat-aware use of Centiloid values for patient selection, characterization, and cross-study interpretation.

## Assumptions
- A1: The abstract highlights accurately summarize the full paper's practical overview.
- A2: No unprovided full-text details, thresholds, figures, tables, or caveats are inferred beyond the metadata.
- A3: "Standards of truth" refers to validation references used to derive or compare Centiloid thresholds, but the specific standards are not available from provided input.
