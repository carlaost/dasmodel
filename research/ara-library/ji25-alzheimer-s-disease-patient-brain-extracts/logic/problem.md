# Problem Specification

> Grounding: abstract/metadata only. No full-text PDF, methods, tables, figures, or supplementary data were provided.

## Observations

### O01: Alzheimer's disease has high worldwide prevalence and limited treatment
- **Statement**: The abstract states that Alzheimer's Disease is the most common cause of dementia, afflicts 55 million individuals worldwide, and has limited treatment available.
- **Evidence**: `metadata.md` Abstract: "Alzheimer's Disease (AD) is the most common cause of dementia, afflicting 55 million individuals worldwide, with limited treatment available."
- **Implication**: The disease burden motivates translational models for mechanism study and therapeutic testing.

### O02: Sporadic AD is underrepresented in current models
- **Statement**: The abstract states that current AD models mainly focus on familial AD, while sporadic AD represents over 95% of AD cases and lacks specific genetic mutations.
- **Evidence**: `metadata.md` Abstract: "Current AD models mainly focus on familial AD (fAD), which is due to genetic mutations. However, models for studying sporadic AD (sAD), which represents over 95% of AD cases without specific genetic mutations, are severely limited."
- **Implication**: A model designed around patient-derived sporadic AD material could address a major modeling gap.

### O03: Species differences may limit animal-model translation
- **Statement**: The abstract states that fundamental species differences between humans and animals might significantly contribute to clinical failures for AD therapeutics that succeeded in animal models.
- **Evidence**: `metadata.md` Abstract: "the fundamental species differences between humans and animals might significantly contribute to clinical failures for AD therapeutics that have shown success in animal models"
- **Implication**: Human-cell three-dimensional models are positioned as more translationally relevant than animal models for some AD therapeutic questions.

### O04: The reported organoid model includes multiple AD-relevant human cell types
- **Statement**: The abstract reports an hPSC-based vascularized neuroimmune organoid model containing human neurons, microglia, astrocytes, and blood vessels.
- **Evidence**: `metadata.md` Abstract: "we developed a complex human pluripotent stem cell (hPSC)-based vascularized neuroimmune organoid model, which contains multiple cell types affected in human AD brains, including human neurons, microglia, astrocytes, and blood vessels."
- **Implication**: The model is intended to capture multicellular brain and vascular interactions relevant to AD pathology.

## Gaps

### G01: Human sporadic AD models are limited
- **Statement**: The abstract identifies a severe limitation in models for sporadic AD.
- **Caused by**: O02
- **Existing attempts**: Current AD models mainly focus on familial AD.
- **Why they fail**: Not available from provided input beyond the abstract's statement that fAD models focus on genetic mutations while sAD cases lack specific genetic mutations.

### G02: Animal-model therapeutic success may not translate to humans
- **Statement**: The abstract identifies species differences as a possible contributor to clinical failures.
- **Caused by**: O03
- **Existing attempts**: Animal models for AD therapeutics.
- **Why they fail**: Not available from provided input beyond the abstract's species-difference rationale.

### G03: Drug-development models need immune and vascular context
- **Statement**: The abstract implies that a pathophysiologically relevant three-dimensional human-cell environment should include multiple AD-affected cell types, including vascular and immune components.
- **Caused by**: O04
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

## Key Insight

- **Insight**: Exposing human hPSC-based vascularized neuroimmune organoids to brain extracts from individuals with sporadic AD can model multiple AD pathologies in a three-dimensional human-cell environment.
- **Derived from**: O02, O03, O04
- **Enables**: Mechanistic study of sporadic AD-like pathology and abstract-level drug-response testing with Lecanemab.

## Assumptions

- A1: Patient brain extracts can carry disease-relevant factors sufficient to induce AD-like pathology in human organoids.
- A2: Including neurons, microglia, astrocytes, and blood vessels better represents affected human AD brain cell types than models lacking those components.
- A3: The abstract's reported outcomes are taken as author-reported results; full protocol details, sample sizes, controls, statistical tests, and effect sizes are not available from provided input.
