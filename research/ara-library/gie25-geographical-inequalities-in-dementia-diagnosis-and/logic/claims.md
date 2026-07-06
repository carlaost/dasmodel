# Claims

> Grounding: abstract-only. Every load-bearing number is copied verbatim from the abstract in `metadata.md`; qualitative claims are limited to the wording supported by the abstract. No full text was available, so no table or figure evidence backs these claims.

## C01: The review included 32 studies after screening 1321 records
- **Statement**: The systematic review screened 1321 studies, read 49 full texts, and included 32 studies in the final review.
- **Status**: supported
- **Falsification criteria**: Full-text PRISMA flow data showing different screened, full-text-read, or included-study counts.
- **Proof**: [E01]
- **Evidence basis**: The abstract reports the study-flow counts directly.
- **Interpretation**: The synthesis draws on a screened corpus narrowed to 32 included studies; attrition reasons are not available from provided input.
- **Sources**:
  - 1321 studies screened; 49 full texts read; 32 studies included <- metadata.md (abstract Results) «From 1321 studies screened and 49 full texts read, 32 studies were included in the final review.» [result]
- **Dependencies**: none
- **Tags**: systematic-review, study-flow, evidence-base

## C02: Evidence is concentrated in the US and UK
- **Statement**: Most included studies were conducted in the US, followed by the UK.
- **Status**: supported
- **Falsification criteria**: Full-text study-characteristics extraction showing that another country contributed more studies than the US, or that the UK was not second.
- **Proof**: [E02]
- **Evidence basis**: The abstract reports the country distribution qualitatively without exact country counts.
- **Interpretation**: The reviewed evidence may underrepresent non-US and non-UK health and social care systems.
- **Sources**:
  - US followed by UK distribution <- metadata.md (abstract Results) «Most studies were conducted in the US, followed by the UK.» [result]
- **Dependencies**: C01
- **Tags**: geography, country-distribution, generalizability

## C03: Inequalities are most often evidenced through regional service availability and suitability
- **Statement**: Geographical inequalities in dementia diagnosis and care are most often evidenced in relation to the availability and suitability of services in different regions within a country, or a lack thereof.
- **Status**: supported
- **Falsification criteria**: Full-text synthesis showing another category was more frequent or central than regional service availability/suitability.
- **Proof**: [E02]
- **Evidence basis**: The abstract reports this as the most common evidentiary pattern.
- **Interpretation**: The review frames unequal service configuration as a major mechanism linking place to dementia care access.
- **Sources**:
  - most-often evidenced pattern <- metadata.md (abstract Results) «Geographical inequalities in dementia are most often evidenced in relation to availability and suitability of services in different regions within a country, or a lack thereof.» [result]
- **Dependencies**: C01
- **Tags**: service-availability, suitability, regional-inequality

## C04: Rural residents often face timely-diagnosis and care-access challenges
- **Statement**: People with dementia residing in rural areas often experience challenges in receiving a timely diagnosis and accessing health and social care.
- **Status**: supported
- **Falsification criteria**: Full-text synthesis showing rural residence is not associated with timely-diagnosis or health/social-care access challenges in the included evidence.
- **Proof**: [E02, E03]
- **Evidence basis**: The abstract reports this rural-access pattern directly.
- **Interpretation**: Rurality is a priority axis for service redesign and national dementia strategies.
- **Sources**:
  - rural timely diagnosis and access challenges <- metadata.md (abstract Results) «People with dementia residing in rural areas often experience challenges in receiving a timely diagnosis and accessing health and social care.» [result]
- **Dependencies**: C03
- **Tags**: rurality, diagnosis-delay, health-care-access, social-care-access

## C05: Residential care inequalities are an evidence gap, while rural Canada and Australia show innovative diagnosis models
- **Statement**: The abstract reports that no research has addressed geographical inequalities in accessing residential care, and that innovative models for improving efficiency and quantity of diagnosis rates emerged in rural Canada and Australia.
- **Status**: supported
- **Falsification criteria**: Full-text evidence identifying included studies on geographical inequalities in residential care access, or showing no rural Canada/Australia diagnosis-rate models were identified.
- **Proof**: [E03, E04]
- **Evidence basis**: The abstract states both the residential-care gap and the emergence of rural diagnosis-rate models.
- **Interpretation**: The paper distinguishes between an unstudied care-setting gap and promising place-adapted diagnosis-service models, but implementation details are not available from provided input.
- **Sources**:
  - no residential care research <- metadata.md (abstract Results) «No research has addressed geographical inequalities in accessing residential care.» [result]
  - rural Canada and Australia models <- metadata.md (abstract Results) «Innovative models on improving efficiency and quantity of diagnosis rates in rural Canada and Australia emerged.» [result]
- **Dependencies**: C01, C04
- **Tags**: residential-care, evidence-gap, rural-models, Canada, Australia
