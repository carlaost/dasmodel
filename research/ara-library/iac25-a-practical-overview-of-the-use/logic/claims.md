# Claims

> Grounding: abstract-only. The source is `metadata.md`; the abstract contains highlights only and no full methods/results tables. No load-bearing numerical paper result is stated in the abstract. Metadata counts such as citation count are not treated as paper claims.

## C01: Amyloid-PET quantitation is increasingly adopted
- **Statement**: Amyloid-PET quantitation is increasingly adopted in research and clinical trials.
- **Status**: supported
- **Falsification criteria**: Evidence from the full paper or field-level usage data showing that amyloid-PET quantitation is not increasingly adopted in research and clinical trial contexts.
- **Proof**: [E01]
- **Evidence basis**: The abstract states this as a highlight.
- **Interpretation**: The paper is motivated by growing practical use rather than by a purely theoretical measurement problem.
- **Sources**:
  - adoption claim <- metadata.md (Abstract) «Amyloid-PET quantitation is increasingly adopted in research and clinical trials.» [result]
- **Dependencies**: none
- **Tags**: amyloid-PET, quantitation, clinical-trials, research

## C02: Centiloid harmonizes amyloid-PET data across tracers and methods
- **Statement**: The Centiloid scale harmonizes amyloid-PET data from different tracers and methods.
- **Status**: supported
- **Falsification criteria**: Evidence that the Centiloid scale fails to place amyloid-PET data from different tracers and methods onto a comparable scale under the conditions discussed by the paper.
- **Proof**: [E01]
- **Evidence basis**: The abstract states this harmonization role directly.
- **Interpretation**: Centiloid is the central practical construct for cross-study and cross-tracer interpretation in this paper.
- **Sources**:
  - harmonization claim <- metadata.md (Abstract) «The Centiloid scale harmonizes amyloid-PET data from different tracers and methods.» [result]
- **Dependencies**: C01
- **Tags**: Centiloid, harmonization, amyloid-PET, tracers

## C03: Comparable standards of truth yield similar Centiloid thresholds
- **Statement**: Studies with comparable standards of truth reported similar Centiloid thresholds.
- **Status**: supported
- **Falsification criteria**: A review of the studies discussed by the paper showing materially divergent Centiloid thresholds despite comparable standards of truth.
- **Proof**: [E02]
- **Evidence basis**: The abstract states that threshold similarity was reported when standards of truth were comparable.
- **Interpretation**: The comparability of the truth standard is a key condition for interpreting threshold agreement.
- **Sources**:
  - threshold claim <- metadata.md (Abstract) «Studies with comparable standards of truth reported similar Centiloid thresholds.» [result]
- **Dependencies**: C02
- **Tags**: Centiloid-thresholds, standards-of-truth, comparability

## C04: Centiloid values can support patient selection and characterization under caveat-aware interpretation
- **Statement**: Centiloid values can be robustly used for patient selection and characterization, provided methodological caveats are considered when interpreting them.
- **Status**: supported
- **Falsification criteria**: Evidence from the full paper or subsequent studies showing that Centiloid values are not robust for patient selection or characterization even when methodological caveats are addressed.
- **Proof**: [E03]
- **Evidence basis**: The abstract separately states robust use for patient selection/characterization and the need to consider methodological caveats.
- **Interpretation**: The paper's applied recommendation is conditional: use Centiloid values, but do not detach them from methodological context.
- **Sources**:
  - robust-use claim <- metadata.md (Abstract) «Centiloid values can be robustly used for patient selection and characterization.» [result]
  - caveat condition <- metadata.md (Abstract) «Methodological caveats should be considered when interpreting Centiloid values.» [result]
- **Dependencies**: C02, C03
- **Tags**: patient-selection, characterization, methodological-caveats, Centiloid
