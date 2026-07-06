# Problem Specification

## Observations

### O01: AD has unresolved epigenetic underpinnings
- **Statement**: Alzheimer's disease is described as a neurodegenerative disorder with progressive cognitive decline, while its epigenetic underpinnings remain elusive.
- **Evidence**: `metadata.md:13` abstract: "Alzheimer's disease (AD) is a neurodegenerative disorder characterized by progressive cognitive decline, yet its epigenetic underpinnings remain elusive."
- **Implication**: A study design that can connect epigenomic state to disease progression and cognition is needed.

### O02: The study integrates a large postmortem single-cell multiomic atlas
- **Statement**: The abstract reports single-cell epigenomic and transcriptomic profiles of 3.5 million cells from 384 postmortem brain samples across 6 regions in 111 AD and control individuals.
- **Evidence**: `metadata.md:13` abstract.
- **Implication**: The input scale supports multiregion and cell-type-resolved analysis, though region names and cohort breakdowns are not available from provided input.

### O03: Regulatory elements and modules are mapped across cell subtypes
- **Statement**: The abstract reports over 1 million candidate cis-regulatory elements organized into 123 regulatory modules across 67 cell subtypes.
- **Evidence**: `metadata.md:13` abstract.
- **Implication**: The paper frames AD progression through regulatory element organization and subtype-resolved regulatory modules.

### O04: AD progression is associated with epigenomic stability dynamics
- **Statement**: The abstract reports widespread epigenome relaxation and brain-region-specific and cell-type-specific epigenomic erosion signatures during AD progression.
- **Evidence**: `metadata.md:13` abstract.
- **Implication**: Disease-associated regulatory changes are not presented as uniform; they vary by region and cell type.

## Gaps

### G01: Epigenetic mechanisms connecting AD progression and cognition are unresolved
- **Statement**: The abstract states that AD's epigenetic underpinnings remain elusive.
- **Caused by**: O01.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

### G02: Abstract-level metadata does not expose detailed methodology
- **Statement**: The provided input does not identify assays, preprocessing, statistical tests, region names, sample inclusion criteria, or effect sizes.
- **Caused by**: Only `metadata.json` and `metadata.md` are available; no full text or PDF was provided.
- **Existing attempts**: Not available from provided input.
- **Why they fail**: Not available from provided input.

## Key Insight

- **Insight**: Integrating single-cell epigenomic and transcriptomic profiles across multiple brain regions can expose regulatory elements, regulatory modules, and epigenomic stability dynamics linked to AD progression and cognitive resilience.
- **Derived from**: O02, O03, O04.
- **Enables**: A multiregion, cell-subtype-resolved atlas of AD-associated epigenomic rewiring.

## Assumptions

- A1: AD and control individuals are included as stated by the abstract; exact diagnostic and control definitions are not available from provided input.
- A2: Postmortem brain samples are the source tissue; exact brain regions and sample distribution are not available from provided input.
- A3: Claims are limited to abstract-supported associations and atlas contents, not causal mechanisms.
