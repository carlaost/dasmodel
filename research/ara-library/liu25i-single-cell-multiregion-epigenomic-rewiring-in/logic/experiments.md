# Experiments (Analysis Plans)

> Grounding: abstract/metadata only. These are declarative reconstructions of analyses the abstract says the study performed or directly implies. Exact quantitative results are intentionally omitted here; method details unavailable from the abstract are marked "Not available from provided input."

## E01: Generate and integrate multiregion single-cell epigenomic and transcriptomic profiles
- **Verifies**: C01
- **Setup**:
  - Data: Postmortem brain samples from AD and control individuals.
  - Modalities: Single-cell epigenomic and transcriptomic profiles.
  - Brain regions: Multiregion design; exact region names not available from provided input.
  - System: Assay platforms, preprocessing, integration model, and quality control are not available from provided input.
- **Procedure**:
  1. Generate single-cell epigenomic profiles.
  2. Generate single-cell transcriptomic profiles.
  3. Integrate profiles across samples, regions, and individuals.
- **Metrics**: Coverage of cells, samples, brain regions, and individuals; integration quality metrics not available from provided input.
- **Expected outcome**:
  - The integrated atlas supports multiregion and cell-resolved AD/control analysis.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Identify cCREs, regulatory modules, and cell subtypes
- **Verifies**: C02
- **Setup**:
  - Input: Integrated single-cell epigenomic and transcriptomic atlas from E01.
  - Targets: Candidate cis-regulatory elements, regulatory modules, and cell subtypes.
  - System: cCRE calling, module construction, and cell-subtype annotation procedures are not available from provided input.
- **Procedure**:
  1. Identify candidate cis-regulatory elements from the single-cell epigenomic data.
  2. Organize cCREs into regulatory modules.
  3. Map modules across cell subtypes.
- **Metrics**: Counts of cCREs, modules, and cell subtypes; quality metrics not available from provided input.
- **Expected outcome**:
  - cCREs organize into regulatory modules that can be interpreted across cell subtypes.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E03: Delineate AD-associated epigenomic compartment and information dynamics
- **Verifies**: C03
- **Setup**:
  - Input: Large-scale epigenomic compartments and single-cell epigenomic information derived from the atlas.
  - Comparison: AD progression state across individuals/samples; exact progression labels not available from provided input.
  - System: Compartment definition and single-cell information metric are not available from provided input.
- **Procedure**:
  1. Define large-scale epigenomic compartments.
  2. Define single-cell epigenomic information.
  3. Evaluate dynamics across AD progression, brain regions, and cell types.
- **Metrics**: Epigenome relaxation and epigenomic erosion signatures; exact statistics not available from provided input.
- **Expected outcome**:
  - AD progression is accompanied by relaxation and erosion signatures that vary by brain region and cell type.
- **Baselines**: AD versus control and/or progression strata; exact design not available from provided input.
- **Dependencies**: E01, E02

## E04: Associate epigenomic stability dynamics with pathology, cognition, and resilience-linked multiomic dysregulation
- **Verifies**: C04
- **Setup**:
  - Input: Epigenomic stability dynamics from E03.
  - Associated features: Cell-type proportions, glial cell states, transcriptomic dysregulation, AD pathology, cognitive impairment, and cognitive resilience.
  - System: Statistical association models, covariates, and phenotype definitions are not available from provided input.
- **Procedure**:
  1. Quantify epigenomic stability dynamics.
  2. Compare those dynamics with cellular state and proportion changes.
  3. Relate coordinated epigenomic/transcriptomic dysregulation to AD pathology, cognitive impairment, and cognitive resilience.
- **Metrics**: Association strength and direction; exact statistics not available from provided input.
- **Expected outcome**:
  - Epigenomic stability dynamics align with cellular, molecular, pathological, and cognitive features of AD.
- **Baselines**: Not available from provided input.
- **Dependencies**: E03
