# Claims

> Grounding: abstract/metadata only. Every load-bearing number is copied from the abstract in `metadata.md:13`; each `Sources` entry includes a verbatim quote and `[result]` because the values are reported outputs of the study. No table, figure, supplementary result, or method section was available.

## C01: The study generated and integrated a large multiregion single-cell multiomic AD atlas
- **Statement**: The study generated and integrated single-cell epigenomic and transcriptomic profiles of 3.5 million cells from 384 postmortem brain samples across 6 regions in 111 AD and control individuals.
- **Status**: supported
- **Falsification criteria**: Access to the full paper or dataset documentation showing that the reported cell, sample, region, or individual counts differ from the abstract.
- **Proof**: [E01]
- **Evidence basis**: The abstract directly states the data types, cell count, sample count, region count, and individual count.
- **Interpretation**: The dataset is positioned as a comprehensive single-cell multiomic atlas for AD, but exact assay platforms and cohort composition are not available from provided input.
- **Sources**:
  - 3.5 million cells, 384 postmortem brain samples, 6 regions, 111 AD and control individuals <- metadata.md:13 «Here, we generate and integrate single-cell epigenomic and transcriptomic profiles of 3.5 million cells from 384 postmortem brain samples across 6 regions in 111 AD and control individuals.» [result]
- **Dependencies**: none
- **Tags**: atlas, single-cell, epigenomics, transcriptomics, postmortem-brain

## C02: The atlas identifies cCREs and regulatory modules across cell subtypes
- **Statement**: The study identifies over 1 million candidate cis-regulatory elements, organized into 123 regulatory modules across 67 cell subtypes.
- **Status**: supported
- **Falsification criteria**: Access to full methods, supplementary tables, or released atlas files showing materially different cCRE, module, or subtype counts.
- **Proof**: [E02]
- **Evidence basis**: The abstract directly reports the cCRE count scale, regulatory module count, and cell subtype count.
- **Interpretation**: The abstract supports a regulatory-element and module map; it does not specify module construction, cCRE calling criteria, or subtype taxonomy.
- **Sources**:
  - over 1 million cCREs, 123 regulatory modules, 67 cell subtypes <- metadata.md:13 «We identify over 1 million candidate cis-regulatory elements (cCREs), organized into 123 regulatory modules across 67 cell subtypes.» [result]
- **Dependencies**: C01
- **Tags**: cCRE, regulatory-modules, cell-subtypes

## C03: AD progression shows epigenome relaxation and region/cell-type-specific erosion signatures
- **Statement**: The study delineates AD-associated epigenomic dynamics, revealing widespread epigenome relaxation and brain-region-specific and cell-type-specific epigenomic erosion signatures during AD progression.
- **Status**: supported
- **Falsification criteria**: Full-text or independent reanalysis showing no widespread epigenome relaxation, no region-specific signatures, or no cell-type-specific erosion signatures during AD progression.
- **Proof**: [E03]
- **Evidence basis**: The abstract directly reports these qualitative findings.
- **Interpretation**: The abstract establishes directional patterns, but not the metrics, affected regions, affected cell types, or effect sizes.
- **Sources**:
  - widespread epigenome relaxation and region/cell-type-specific erosion <- metadata.md:13 «We define large-scale epigenomic compartments and single-cell epigenomic information and delineate their dynamics in AD, revealing widespread epigenome relaxation and brain-region-specific and cell-type-specific epigenomic erosion signatures during AD progression.» [result]
- **Dependencies**: C01, C02
- **Tags**: AD-progression, epigenome-relaxation, epigenomic-erosion

## C04: Epigenomic stability dynamics are associated with cellular, molecular, pathological, and cognitive features
- **Statement**: The study reports that epigenomic stability dynamics are closely associated with cell-type proportion changes, glial cell-state transitions, coordinated epigenomic and transcriptomic dysregulation, AD pathology, cognitive impairment, and cognitive resilience.
- **Status**: supported
- **Falsification criteria**: Full-text or independent reanalysis showing that these reported associations are absent or unsupported for the study cohort.
- **Proof**: [E04]
- **Evidence basis**: The abstract directly states the associated feature classes and disease/cognition links.
- **Interpretation**: This supports association, not causality. Exact association statistics, covariates, and resilience definitions are not available from provided input.
- **Sources**:
  - association targets <- metadata.md:13 «These epigenomic stability dynamics are closely associated with cell-type proportion changes, glial cell-state transitions, and coordinated epigenomic and transcriptomic dysregulation linked to AD pathology, cognitive impairment, and cognitive resilience.» [result]
- **Dependencies**: C03
- **Tags**: cognitive-resilience, AD-pathology, glial-cell-state, multiomic-dysregulation
