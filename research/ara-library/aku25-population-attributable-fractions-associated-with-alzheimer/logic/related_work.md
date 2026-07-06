# Related Work / Typed Dependency Graph

> **Citation-footprint note.** The source is a two-page conference meeting abstract with **no
> reference list**. It names no specific prior studies, so no scholarly `RW` blocks with a concrete
> technical delta can be extracted without fabrication (Rule 2 / Rule 9). The one grounded, typed
> dependency the abstract does declare is its **data source**, captured below from `sources.yaml`
> (verified) and the abstract text. Broader field context is noted narratively without inventing
> citations.

## RW01: CMS Medicare 5% Sample (data-source dependency)
- **DOI**: Not applicable (administrative data resource, not a publication). Access resource: CMS / ResDAC (Research Data Assistance Center).
- **Type**: imports (data source — a concrete input the study depends on)
- **Delta**:
  - What changed: The study consumes a "high-power 5%-sample of the Medicare population" (CMS administrative claims/enrollment data) as the cohort from which AD/ADRD outcomes, comorbid diseases, dual-eligibility status, and race/sex strata are derived.
  - Why: Medicare's scale supports jointly-adjusted Cox modeling and PAF decomposition down to race- and sex-specific subpopulations that are usually under-powered.
- **Claims affected**: C01, C02, C03, C04, C05, C06, C07, C08, C09
- **Adopted elements**: Beneficiary enrollment records, diagnosis claims, dual Medicare/Medicaid eligibility flag (used as the low-income proxy), and demographic (race/sex/age) fields.
- **Access**: Controlled — obtainable only through standard CMS/ResDAC research data request procedures; no public accession identifier (per `sources.yaml`, verified). See `data/dataset.md` and `src/environment.md`.

## Background context (no specific citations available)
- **Prior AD/ADRD risk-factor literature**: The abstract's opening premise — "numerous risk factors for Alzheimer's disease (AD) and related dementias (ADRD) have been identified, their combined influence on risk remains uncertain" — positions the work against a body of prior single-risk-factor studies. That body is **not cited** in the abstract, so specific works, DOIs, and technical deltas are Not specified in the published abstract and are not reconstructed here.
- **Related author work**: The author group (Akushevich, Yashkin, Ukraintseva, Yashin, Kravchenko, Duke University) has a broader program on Medicare-based aging and disease modeling; the abstract cites none of it, so no specific entries are added.

> No clinical-trial dependencies exist: this is an observational study, not an interventional
> trial; no NCT or PROSPERO registration exists or was found (per `sources.yaml`, verified).
