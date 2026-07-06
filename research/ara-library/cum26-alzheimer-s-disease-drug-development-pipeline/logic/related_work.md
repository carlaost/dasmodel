# Related Work & Dependencies

Typed dependency graph reflecting the paper's 10-reference footprint plus the data sources and
flagship clinical trials it is built on (the latter grounded in the verified `sources.yaml`).

## RW01: Brookmeyer et al., 2018 — Forecasting AD prevalence in the US
- **DOI**: 10.1016/j.jalz.2018.02.001 (Alzheimers Dement. 2018;14(2):121–129)
- **Type**: bounds
- **Delta**:
  - What changed: Provides the epidemiological projections (46.7M biomarker-positive in 2017 →
    75.68M in 2060; ~90M with AD-type brain changes) that quantify the unmet need this pipeline
    addresses.
  - Why: Motivates the urgency of AD drug development.
- **Claims affected**: C01 (context), problem O1
- **Adopted elements**: US prevalence forecasts across the continuum.

## RW02: Cummings, 2025 — Anti-amyloid MAB benefit/risk management
- **DOI**: 10.1016/j.neurot.2025.e00570 (Neurotherapeutics. 2025;22(3):e00570)
- **Type**: imports
- **Delta**:
  - What changed: Background on managing the recently approved anti-amyloid monoclonal antibody class.
  - Why: Establishes the current standard of DTT care against which the pipeline is framed.
- **Claims affected**: C02, C07
- **Adopted elements**: Characterization of the approved anti-amyloid MAB mechanism.

## RW03: Lee et al., 2023 — Brexpiprazole for agitation in AD dementia
- **DOI**: 10.1001/jamaneurol.2023.3810 (JAMA Neurol. 2023;80(12):1307–1316)
- **Type**: imports
- **Delta**:
  - What changed: The RCT underpinning the approved multi-transmitter antipsychotic STT for agitation.
  - Why: Anchors the NPS-targeting STT class as one of four verified mechanisms.
- **Claims affected**: C02
- **Adopted elements**: Evidence for an approved NPS/agitation STT.

## RW04: Cummings et al., 2025 — AD drug development pipeline: 2025
- **DOI**: 10.1002/trc2.70098 (Alzheimers Dement TRCI. 2025;11(2):e70098)
- **Type**: extends
- **Delta**:
  - What changed: The immediately preceding annual census (182 trials / 138 drugs; 46 repurposed,
    33%). This 2026 review extends the same methodology one year forward (192 trials / 158 drugs).
  - Why: Enables the direct 2025→2026 year-over-year comparison.
- **Claims affected**: C08, C10
- **Adopted elements**: Census methodology, CADRO classification, Index-Date framework.

## RW05: Cummings et al., 2024 — AD drug development pipeline: 2024
- **DOI**: 10.1002/trc2.12465 (Alzheimers Dement TRCI. 2024;10(2):e12465)
- **Type**: extends
- **Delta**:
  - What changed: Earlier census establishing the annual-review methodology the present paper builds on.
  - Why: Part of the longitudinal series enabling the 2017–2026 trajectory analysis.
- **Claims affected**: C08, C10
- **Adopted elements**: Methodologic approach ("builds on our previous AD pipeline studies").

## RW06: Liggins et al., 2014 — IADRP / CADRO
- **DOI**: 10.1016/j.jalz.2013.12.017 (Alzheimers Dement. 2014;10(3):405–408)
- **Type**: imports
- **Delta**:
  - What changed: Source of the Common Alzheimer's Disease Research Ontology (CADRO) used to classify
    every agent's target process.
  - Why: CADRO is the classification backbone of the entire analysis.
- **Claims affected**: C07, C10
- **Adopted elements**: The CADRO target-process categories.

## RW07: Cummings et al., 2025 — Biomarker-guided decision making
- **DOI**: 10.1038/s41573-025-01203-7 (Nat Rev Drug Discov. 2025;24(8):589–609)
- **Type**: imports
- **Delta**:
  - What changed: Framework for biomarker use (eligibility, stratification, pharmacodynamic outcome)
    in neurodegenerative drug development.
  - Why: Underpins the biomarker-in-trials analysis (§3.6).
- **Claims affected**: C09
- **Adopted elements**: Biomarker context-of-use taxonomy.

## RW08: Cummings et al., 2025 — Drug repurposing for AD
- **DOI**: 10.1038/s41467-025-56737-y (Nat Commun. 2025;16(1):1755)
- **Type**: imports
- **Delta**:
  - What changed: Methodology/rationale for identifying and prioritizing repurposed drugs in AD.
  - Why: Underpins the repurposing analysis (§3.9) and DrugBank comparison.
- **Claims affected**: C06
- **Adopted elements**: Repurposing identification approach.

## RW09: Cunha-Oliveira et al., 2024 — Best practices for research data management
- **DOI**: 10.1152/physrev.00043.2023 (Physiol Rev. 2024;104(3):1387–1408)
- **Type**: imports
- **Delta**:
  - What changed: Data-management/governance best practices the authors cite for their curation pipeline.
  - Why: Supports the data-quality/limitations discussion.
- **Claims affected**: constraints.md
- **Adopted elements**: Data governance practices.

## RW10: Hassenstein & Jung, 2025 — Ten simple rules for research data management
- **DOI**: 10.1371/journal.pcbi.1013779 (PLoS Comput Biol. 2025;21(12):e1013779)
- **Type**: imports
- **Delta**:
  - What changed: Data-management guidance cited alongside RW09.
  - Why: Supports the report's data-capture/interpretation caveats.
- **Claims affected**: constraints.md
- **Adopted elements**: Data-management rules.

---

## Data-source dependencies (grounded in sources.yaml — verified)

### DS1: ClinicalTrials.gov AD trial registry (Index Date 2026-01-01)
- **Type**: imports (primary data source)
- **Access**: open (NIH/NLM registry; API)
- **Identifier**: clinicaltrials.gov
- **Role**: The sole primary data source — 158 drugs across 192 AD trials. All counts derive from it.
- **Claims affected**: C01–C10

### DS2: alzpipeline.com / UNLV Clinical Trial Observatory
- **Type**: imports (summary-data mirror)
- **Access**: open (verified live)
- **Identifier**: alzpipeline.com
- **Role**: Cummings-founded AD Clinical Trial Observatory hosting the summary pipeline data
  (Data Availability Statement).
- **Claims affected**: C01–C10 (summary access)

### DS3: Alzheimer's Disease Data Initiative — AD Workbench (Gates Ventures)
- **Type**: imports (planned data deposit)
- **Access**: request (not yet verified)
- **Identifier**: —
- **Role**: Data to be made available via the AD Workbench of Gates Ventures' AD Data Initiative.
- **Claims affected**: data availability

### DS4: DrugBank (https://go.drugbank.com/)
- **Type**: bounds (repurposing reference)
- **Access**: open/subscription
- **Role**: Reference against which agents are judged repurposed vs novel.
- **Claims affected**: C06

### Flagship clinical trials (verified subset of ~190 NCTs cited across Tables 1–3)
The paper's Phase 1–3 tables cite ~190 NCT identifiers; 8 flagship Phase 3 disease-targeting /
repurposed agents were individually verified against ClinicalTrials.gov (`sources.yaml`) and all
appear in the paper's tables:

| NCT | Agent / Study | Phase | Status | Sponsor |
|-----|---------------|-------|--------|---------|
| NCT05026866 | Donanemab, TRAILBLAZER-ALZ 3 | 3 | Active, not recruiting | Eli Lilly |
| NCT03887455 | Lecanemab, Clarity AD | 3 | Active, not recruiting | Eisai |
| NCT04468659 | Lecanemab, AHEAD 3-45 | 3 | Active, not recruiting | Eisai |
| NCT05463731 | Remternetug, TRAILRUNNER-ALZ 1 | 3 | Completed | Eli Lilly |
| NCT04777396 | Semaglutide, EVOKE | 3 | Completed | Novo Nordisk |
| NCT05531526 | AR1001, Polaris-AD | 3 | Active, not recruiting | AriBio |
| NCT06709014 | Buntanetap/Posiphen | 3 | Active, not recruiting | Annovis Bio |
| NCT05564169 | Masitinib add-on, AB21004 | 3 | Not yet recruiting | AB Science |
