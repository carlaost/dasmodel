# Experiments and Analyses

> Grounding: abstract-only. These are declarative reconstructions of the review analyses described by the abstract. Exact numerical results are intentionally omitted here and kept in `claims.md`.

## E01: Systematic-review screening and inclusion flow
- **Verifies**: C01
- **Setup**:
  - Study type: Systematic review
  - Search scope: Five databases searched in June 2024
  - Eligibility: Studies in any country, published from 2010 onward, English or German
  - Review process: Titles/abstracts and full texts screened by at least two reviewers; discrepancies resolved with a third reviewer
- **Procedure**:
  1. Search the specified databases using the review strategy.
  2. Screen titles and abstracts against inclusion criteria.
  3. Screen full texts against inclusion criteria.
  4. Record final included studies.
- **Metrics**: Number of records screened, full texts read, and studies included.
- **Expected outcome**: A narrowed included-study set suitable for narrative synthesis.
- **Baselines**: Not available from provided input.
- **Dependencies**: none

## E02: Narrative synthesis of geographical inequality patterns
- **Verifies**: C02, C03, C04
- **Setup**:
  - Data source: Included studies from E01
  - Extraction: Data extracted by two researchers
  - Synthesis mode: Narrative synthesis
  - Geography variables: Country, within-country region, rural/suburban/urban location, postcode where available
- **Procedure**:
  1. Extract study setting and geography-related access findings.
  2. Group findings by country and geographical inequality mechanism.
  3. Identify recurring patterns in service availability, suitability, and rural access.
- **Metrics**: Directional frequency or salience of country settings and inequality mechanisms.
- **Expected outcome**: Evidence concentrates in some countries and highlights regional service availability/suitability and rural access challenges.
- **Baselines**: Not available from provided input.
- **Dependencies**: E01

## E03: Gap analysis for care domains and underserved dementia groups
- **Verifies**: C04, C05
- **Setup**:
  - Data source: Narrative synthesis outputs from E02
  - Domains: Diagnosis, health care, social care, residential care, rarer dementia forms
  - Population: People with dementia
- **Procedure**:
  1. Map included studies to care domains.
  2. Identify domains without geographical-inequality evidence.
  3. Identify dementia subgroups requiring further research.
- **Metrics**: Presence/absence of evidence by care domain and subgroup.
- **Expected outcome**: Residential care and rarer forms of dementia remain under-addressed.
- **Baselines**: Not available from provided input.
- **Dependencies**: E02

## E04: Identification of innovative rural diagnosis models
- **Verifies**: C05
- **Setup**:
  - Data source: Included-study findings from E02
  - Target setting: Rural service contexts
  - Countries mentioned in abstract: Canada and Australia
- **Procedure**:
  1. Identify studies describing models intended to improve diagnosis-rate efficiency or quantity in rural settings.
  2. Extract model setting, intended mechanism, and reported direction of effect.
  3. Compare model themes with rural access challenges.
- **Metrics**: Directional evidence of improved diagnosis efficiency or quantity; exact metrics not available from provided input.
- **Expected outcome**: Rural Canada and Australia provide examples of innovative diagnosis-service models.
- **Baselines**: Not available from provided input.
- **Dependencies**: E02
