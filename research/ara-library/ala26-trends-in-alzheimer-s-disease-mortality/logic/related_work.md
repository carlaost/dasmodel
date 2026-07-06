# Related Work — Typed Dependency Graph

> Grounding: abstract-only. No reference list is available (no full text), so specific prior papers
> and their technical deltas cannot be enumerated. The dependencies below are the methodological and
> data-source dependencies that are explicit in the abstract/metadata, plus the verified data source
> from `sources.yaml`. Bibliographic citation-level related work is "Not available from provided
> input (no full text)".

## RW01: CDC WONDER Multiple Cause of Death database (data source)
- **DOI**: n/a (CDC WONDER, https://wonder.cdc.gov/)
- **Type**: imports (typed dependency: dataset)
- **Access**: open (publicly queryable; no login required). No specific query/accession identifier reported by the authors. Verified in `sources.yaml` (`data[0]`, `access: open`, `verified: true`).
- **Delta**:
  - What changed: The study consumes national US death-certificate records (1999–2020) as its entire empirical basis, restricting to underlying-cause AD among ages ≥75 and the metabolic-syndrome-related subset.
  - Why: Provides population-complete mortality counts enabling age-adjusted rate estimation and disparity analysis.
- **Claims affected**: C01, C02, C03, C04, C05, C06
- **Adopted elements**: Death-certificate cause-of-death coding; demographic, geographic, and place-of-death stratifiers.

## RW02: Joinpoint Regression methodology (analytical method)
- **DOI**: Not available from provided input (no full text; the canonical methodological reference is Kim et al., Stat Med 2000, `10.1002/(SICI)1097-0258(20000215)19:3<335::AID-SIM336>3.0.CO;2-Z`, but the paper's own citation is unconfirmed).
- **Type**: imports (typed dependency: method)
- **Delta**:
  - What changed: Segmented log-linear regression is applied to the annual AAMR series to detect trend inflections across strata.
  - Why: To characterize non-monotonic temporal patterns (e.g., the early-to-mid-2000s peak) rather than a single slope.
- **Claims affected**: C02, C05
- **Adopted elements**: Joinpoint segmentation; annual/average percent change framework.

## RW03: Age-adjustment / direct standardization (statistical convention)
- **DOI**: n/a (standard vital-statistics methodology)
- **Type**: bounds (typed dependency: measurement convention)
- **Delta**:
  - What changed: Mortality is expressed as age-adjusted rates per 100,000, standardizing across the study's age and time strata.
  - Why: Removes age-composition confounding so cross-group and over-time comparisons are valid.
- **Claims affected**: C02, C03, C04, C06
- **Adopted elements**: Direct age standardization to a reference population (reference-population year Not available — no full text).

## RW04: Shared AD–metabolic-syndrome pathophysiology (background rationale)
- **DOI**: Not available from provided input (no full text).
- **Type**: extends (typed dependency: conceptual motivation)
- **Delta**:
  - What changed: The study builds on the premise that AD and metabolic syndrome share pathophysiologies and risk determinants, motivating joint mortality analysis.
  - Why: Justifies isolating the AD+metabolic-syndrome intersection as a distinct surveillance target.
- **Claims affected**: C01 (framing), overall study motivation
- **Adopted elements**: The pathophysiological-overlap hypothesis (stated in the abstract Background; specific citations Not available — no full text).

## Broader citation footprint
Not available from provided input (no full text). The article's full reference list — general AD
mortality surveillance, metabolic-syndrome epidemiology, and prior CDC WONDER trend studies that
would ordinarily appear here as briefer entries — could not be recovered because no open-access or
repository copy of the full text exists (Unpaywall `is_oa:false`; Europe PMC `inPMC:N`).
