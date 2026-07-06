# Experiments (Analysis Plans)

> Grounding: abstract-only. These are declarative analysis plans reconstructed from the abstract highlights. No exact numerical results appear because the abstract provides none. Procedural detail beyond the highlights is marked unavailable.

## E01: Practical adoption and harmonization overview
- **Verifies**: C01, C02
- **Setup**:
  - Design: Practical overview.
  - Inputs: Studies, clinical trials, tracers, and amyloid-PET quantitation methods discussed by the paper.
  - Data availability: Not available from provided input.
- **Procedure**:
  1. Review use of amyloid-PET quantitation in research and clinical trials.
  2. Describe how the Centiloid scale harmonizes measurements across tracers and methods.
  3. Identify the practical contexts where harmonization matters.
- **Metrics**: Adoption contexts; tracer/method comparability; qualitative harmonization rationale.
- **Expected outcome**: Amyloid-PET quantitation is presented as increasingly adopted, and Centiloid is presented as the harmonizing framework.
- **Baselines**: Non-harmonized tracer- or method-specific amyloid-PET measures.
- **Dependencies**: none

## E02: Centiloid threshold comparison by standards of truth
- **Verifies**: C03
- **Setup**:
  - Design: Cross-study threshold comparison.
  - Included studies: Not available from provided input.
  - Standards of truth: Comparable standards are required, but their identities are not available from provided input.
- **Procedure**:
  1. Group studies by comparable standards of truth.
  2. Compare reported Centiloid thresholds within those comparable groups.
  3. Assess whether threshold values are similar when validation targets are comparable.
- **Metrics**: Directional similarity or divergence of Centiloid thresholds across studies.
- **Expected outcome**: Studies with comparable standards of truth report similar Centiloid thresholds.
- **Baselines**: Studies using non-comparable standards of truth, if discussed in the full paper; not available from provided input.
- **Dependencies**: E01

## E03: Applied use-case and caveat assessment
- **Verifies**: C04
- **Setup**:
  - Use cases: Patient selection and patient characterization.
  - Caveats: Methodological caveats are flagged by the abstract but not enumerated in provided input.
  - Data/software: Not available from provided input.
- **Procedure**:
  1. Evaluate how Centiloid values support patient selection.
  2. Evaluate how Centiloid values support patient characterization.
  3. Identify methodological caveats that condition interpretation.
- **Metrics**: Robustness of use-case interpretation; caveat coverage; applicability to research and clinical trial workflows.
- **Expected outcome**: Centiloid values support patient selection and characterization when interpreted with methodological caveats.
- **Baselines**: Qualitative interpretation without caveat-aware use of Centiloid values.
- **Dependencies**: E01, E02
