# Problem Specification

> Grounding: abstract-only. Observations/gaps below are what the abstract and the verified analysis
> repository support. Quantitative motivating numbers from the paper's introduction are **not
> available from provided input (no full text)**.

## Observations

### O1: Glia are central modulators of brain function across health, aging, and disease
- **Statement**: Glial cells (microglia, astrocytes, OPCs, oligodendrocytes) are critical modulators
  of brain function in health, aging, and disease.
- **Evidence**: Abstract, sentence 1 ("Glial cells are critical modulators of brain function in
  health, aging, and disease.").
- **Implication**: Understanding glial responses and glia–glia/glia–neuron crosstalk requires a
  model system that preserves the human, multicellular context.

### O2: Existing model systems trade off human relevance against multicellular context
- **Statement**: Cell-type-specific interrogation of glial responses and multicellular crosstalk
  in *human* tissue with preserved architecture is not routinely available.
- **Evidence**: Abstract frames the contribution as *establishing* "a robust ex vivo platform for
  cell-type-specific interrogation of glial responses and multicellular crosstalk" — i.e. the
  platform is the novelty.
- **Implication**: A human ex vivo system retaining tissue architecture and mature cell identities
  would fill a gap between reductionist cultures/iPSC models and inaccessible in vivo human brain.

### O3: Glial stress responses are stimulus-specific and multicellular
- **Statement**: Distinct stressors elicit distinct ("stimulus-specific") transcriptional programs,
  and the TNFα response is coordinated across multiple glial cell types (microglia, astrocytes,
  OPCs) including pro-/anti-inflammatory loops.
- **Evidence**: Abstract ("elicit stimulus-specific transcriptional programs to diverse stressors …
  coordinated glial responses to TNFα … pro-/anti-inflammatory loops among microglia, astrocytes,
  and OPCs"). Repo README lists treatments TNFα, LPS, H₂O₂, BLM, control.
- **Implication**: Capturing this requires both bulk (programs across stimuli) and single-nucleus
  (cell-type resolution) transcriptomics plus cell-cell communication inference.

## Gaps

### G1: No adult human ex vivo platform preserving architecture and mature glial identity for weeks
- **Statement**: Lacking is a human system that keeps tissue architecture and mature cell identities
  intact over weeks while allowing controlled perturbation of glial responses.
- **Caused by**: O1, O2.
- **Existing attempts**: Rodent slices, dissociated cultures, iPSC-derived glia, postmortem tissue
  (details of prior attempts: Not available from provided input — no full text).
- **Why they fail**: Not available from provided input (no full text); the abstract positions the
  new platform as the remedy but does not enumerate prior failure modes in the portion available.

### G2: Coordinated multicellular glial crosstalk is hard to resolve in humans
- **Statement**: Resolving *coordinated* glial responses and the ligand–receptor signaling that
  links microglia, astrocytes, and OPCs in human tissue is difficult.
- **Caused by**: O2, O3.
- **Existing attempts**: Not available from provided input (no full text).
- **Why they fail**: Reductionist systems lose the multicellular context; postmortem tissue is a
  static snapshot without controlled perturbation.

## Key Insight
- **Insight**: Adult human organotypic brain slice cultures prepared from *living neurosurgical
  resection* tissue can serve as a controllable ex vivo platform that preserves architecture and
  mature cell identities long enough (weeks) to apply defined stressors and read out cell-type-
  specific, coordinated glial responses — then cross-validate the TNFα response against postmortem
  human brain.
- **Derived from**: O1, O2, O3.
- **Enables**: Bulk RNA-seq across stressors (WGCNA programs), cell-type-resolved snRNA-seq of the
  TNFα response, external-dataset validation, and MultiNicheNet cell-cell communication inference
  (all present in the verified repo).

## Assumptions
- A1: Slice cultures derived from tumor-adjacent neurosurgical resection tissue reflect
  physiologically relevant adult human glial biology (see constraints.md for the tumor-margin
  caveat).
- A2: Transcriptional state measured over the culture window reflects preserved mature cell
  identity rather than culture-induced dedifferentiation.
- A3: A TNFα response reproduced in postmortem human brain and external datasets is a genuine,
  transferable signature rather than a slice-culture artifact.
