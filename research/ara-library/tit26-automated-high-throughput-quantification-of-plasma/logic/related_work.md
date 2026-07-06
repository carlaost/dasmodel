# Related Work (Typed Dependency Graph)

The paper cites 53 references. Works with a specific technical delta to this study get full `RW`
blocks; the remaining citations are captured compactly in the "Additional citations" table to
preserve the full footprint.

## RW01: Therriault, Brum, Trudel et al., 2025 — meta-analysis of blood p-tau
- **DOI**: Lancet Neurol. 2025;24(9):740–52 (ref [14])
- **Type**: bounds / baseline
- **Delta**:
  - What changed: Systematic review/meta-analysis reporting pooled AUC 0.911 (0.889–0.924) for p-tau217 and 0.815 (0.802–0.829) for p-tau181; notably did NOT include Elecsys p-tau217.
  - Why: Establishes the field benchmark this study exceeds (Elecsys p-tau217 AUC 0.939) and the gap it fills.
- **Claims affected**: C01, C03
- **Adopted elements**: Comparative benchmark AUCs; motivation.

## RW02: Hibar, Bauer, Rabe et al., 2026 — Elecsys pTau217 plasma immunoassay
- **DOI**: 10.1002/alz.71009 (Alzheimers Dement. 2026;22(1):e71009) (ref [20])
- **Type**: baseline / extends
- **Delta**:
  - What changed: Positioned Elecsys p-tau217 as a pre-screening tool for amyloid pathology using a low threshold (< 0.189 pg/mL) maximizing sensitivity (95.5–98.6%) and NPV at the cost of low specificity (29.2–50.7%).
  - Why: Direct prior evidence on the same Elecsys p-tau217 assay but a different (rule-out/screening) intended use; contrasts with this study's confirmatory memory-clinic thresholds.
- **Claims affected**: C01, C06
- **Adopted elements**: Establishes prior Elecsys p-tau217 data; intended-use contrast.

## RW03: Palmqvist, Warmenhoven, Anastasi et al., 2025 — fully automated p-tau217 platform
- **DOI**: Nat Med. 2025;31(6):2036–43 (ref [24])
- **Type**: baseline / extends
- **Delta**:
  - What changed: Plasma p-tau217 on a fully automated platform for AD diagnosis across primary and secondary care.
  - Why: Prior automated-platform evidence; this study extends to the Roche Elecsys p-tau217 assay against a CSF reference standard.
- **Claims affected**: C01, C09
- **Adopted elements**: Automated-platform diagnostic framing; cofactor considerations.

## RW04: Warmenhoven, Salvadó, Janelidze et al., 2025 — head-to-head p-tau217 comparison
- **DOI**: 10.1093/brain/awae346 (Brain. 2025;148(2):416–31) (ref [38])
- **Type**: baseline
- **Delta**:
  - What changed: Head-to-head of key p-tau217 assays (ALZpath, Lilly, Janssen/J&J, WashU MS) for amyloid-PET positivity: AUC 0.91–0.96, accuracy 83–93%, sensitivity 84–91%, specificity 85–94%.
  - Why: Benchmark of research/batch assays this study matches on an automated platform.
- **Claims affected**: C01, C02
- **Adopted elements**: Comparative performance range.

## RW05: Janelidze, Bali, Ashton et al., 2022 — head-to-head 10 plasma p-tau assays
- **DOI**: 10.1093/brain/awac333 (Brain. 2022;146(4):1592–601) (ref [15])
- **Type**: baseline
- **Delta**:
  - What changed: Compared 10 plasma phospho-tau assays in prodromal AD, establishing p-tau217 superiority.
  - Why: Supports the choice of p-tau217 as target analyte.
- **Claims affected**: C01, C03
- **Adopted elements**: Assay-comparison methodology and p-tau217 ranking.

## RW06: Lehmann, Gabelle, Duchiron et al., 2025 — pTau/Aβ42 ratios
- **DOI**: EBioMedicine. 2025;117:105805 (ref [25])
- **Type**: extends
- **Delta**:
  - What changed: Proposed combining plasma p-tau217 with Aβ42 (p-tau217/Aβ42 ratio) to improve amyloidosis detection.
  - Why: Motivates the Aβ42 / Aβ42-40 adjustment analysis (C05); this study finds only limited added value.
- **Claims affected**: C05
- **Adopted elements**: Ratio-combination approach.

## RW07: Hu, Yu, Gao, 2025 — first FDA-cleared blood biomarker (pTau217/Aβ42)
- **DOI**: Drug Discov Ther. 2025;19(3):208–9 (ref [50])
- **Type**: bounds
- **Delta**:
  - What changed: Lumipulse plasma p-tau217/Aβ42 became the first FDA-cleared blood test (May 2025) to aid AD diagnosis in symptomatic patients ≥ 55 y.
  - Why: Regulatory context for the p-tau217/Aβ42 combination evaluated here.
- **Claims affected**: C05
- **Adopted elements**: Clinical/regulatory framing.

## RW08: Schindler, Galasko, Pereira et al., 2024 — BBM workgroup acceptable-performance recommendations
- **DOI**: 10.1038/s41582-024-00977-5 (Nat Rev Neurol. 2024;20(7):426–39) (ref [44])
- **Type**: bounds
- **Delta**:
  - What changed: Recommended minimal acceptable performance for confirmatory blood biomarkers (≥ 90% sensitivity and specificity) and a 15–20% acceptable intermediate range.
  - Why: Defines the performance targets this study evaluates itself against (Elecsys p-tau217 near-meets; grey zone 19.9% within range).
- **Claims affected**: C01, C06
- **Adopted elements**: Performance benchmarks and grey-zone target.

## RW09: Dittrich, Blennow, Tan et al., 2025 — plasma APOE proteotyping vs genotyping
- **DOI**: 10.1002/alz.14610 (Alzheimers Dement. 2025;21(2):e14610) (ref [49])
- **Type**: imports
- **Delta**:
  - What changed: Evaluated plasma-based proteotyping assays against APOE-ε4 genotyping in a memory clinic (high agreement).
  - Why: Justifies using blood-based APOE-ε4 proteotyping (as done here) as a genotype surrogate.
- **Claims affected**: C04
- **Adopted elements**: Validity of plasma APOE-ε4 proteotyping.

## RW10: Janelidze, Barthélemy, He et al., 2023 — p-tau/total-tau ratios mitigate kidney effects
- **DOI**: 10.1001/jamaneurol.2023.0199 (JAMA Neurol. 2023;80(5):516–22) (ref [53])
- **Type**: bounds
- **Delta**:
  - What changed: Showed p-tau217/total-tau ratios (MS-based) mitigate the effect of kidney dysfunction on plasma p-tau217.
  - Why: Explains why such normalized ratios (unavailable for Elecsys/Lumipulse immunoassays) were not used; frames the renal-function null (C09).
- **Claims affected**: C09
- **Adopted elements**: Kidney-effect mitigation concept.

## RW11: CLSI EP15-A3, 2017 — precision verification guideline
- **DOI**: CLSI document EP15-A3 (ref [36] in text; listed as ref 35 in References)
- **Type**: imports
- **Delta**:
  - What changed: Standard protocol for user verification of precision and estimation of bias.
  - Why: Defines the analytical-precision experiment (C10 / E06).
- **Claims affected**: C10
- **Adopted elements**: Precision-verification protocol.

## RW12: Leitão, Silva-Spínola, Santana et al., 2019 — Lumipulse CSF assay validation
- **DOI**: Alzheimers Res Ther. 2019;11(1):91 (ref [37] in text mapping; ref 36 in References list — see note)
- **Type**: imports
- **Delta**:
  - What changed: Clinical validation of Lumipulse G CSF assays and reference cut-offs.
  - Why: Source of the CSF reference-standard cut-offs used to classify AD vs non-AD.
- **Claims affected**: reference standard (study_design.md)
- **Adopted elements**: CSF cut-off values.

## RW13: Pilotto, Quaresima, Trasciatti et al., 2025 — Lumipulse vs ALZpath SIMOA head-to-head
- **DOI**: 10.1093/brain/awae368 (Brain. 2025;148(2):408–15) (ref [37])
- **Type**: baseline
- **Delta**:
  - What changed: Lumipulse and ALZpath SIMOA p-tau217 head-to-head; precision comparisons.
  - Why: Supports comparability of imprecision estimates across platforms (C10 discussion).
- **Claims affected**: C10, C07
- **Adopted elements**: Cross-platform precision/agreement context.

## Additional citations (footprint, no distinct technical delta to this study)

| Ref | Work | Role |
|-----|------|------|
| [1] | Hansson et al., Nat Aging 2023 | Background — blood biomarkers in practice/trials |
| [2] | Hampel et al., Neuron 2023 | Background — future use of BBMs |
| [3] | Hansson et al., Alz & Dementia 2022 | Background — AA appropriate-use recommendations |
| [4] | Blennow et al., Alzheimers Dement 2023 | Background — clinical value of plasma biomarkers |
| [5] | Alcolea et al., Neurology 2023 | Background — blood biomarkers for neurologists |
| [6] | Karikari et al., Lancet Neurol 2020 | Background — p-tau181 diagnostic/prediction |
| [7] | Ashton et al., JAMA Neurol 2024 | Background — plasma p-tau217 immunoassay accuracy |
| [8] | Palmqvist et al., JAMA 2020 | Background — p-tau217 discriminative accuracy |
| [9] | Benedet et al., JAMA Neurol 2021 | Background — plasma vs CSF GFAP |
| [10] | Palmqvist et al., Nat Med 2021 | Background — prediction of future AD dementia |
| [11] | Nakamura et al., Nature 2018 | Background — plasma amyloid-β biomarkers |
| [12] | Cogswell et al., Alzheimers Dement 2024 | Background — temporal evolution of plasma p-tau |
| [13] | Therriault et al., Alzheimers Dement 2023 | Background — plasma p-tau217 ≈ CSF |
| [16] | Palmqvist et al., Alzheimers Dement 2023 | Background — automated plasma panel |
| [17] | Schindler et al., Alzheimers Dement 2024 | Background — head-to-head leading blood tests |
| [18] | Kirste et al., Neurology 2025 | Background — IVD p-tau181/ApoE4 rule-out |
| [19] | Anastasi et al., Alzheimers Dement 2025 | Background — memory-clinic biomarker comparison |
| [21] | Cooper et al., Alzheimers Dement 2024 | Background — APOE ε4 modifies p-tau181 |
| [22] | Contreras et al., Alzheimers Res Ther 2025 | Background — APOE4 effect on plasma biomarkers (HABS-HD) |
| [23] | Cody et al., Alzheimers Dement 2025 | Background — plasma biomarker accuracy pre-dementia |
| [26] | Hazan et al., Int J Geriatr Psychiatry 2025 | Background — p-tau181, age, kidney function |
| [27] | Mielke et al., Alzheimers Dement 2022 | Background — CSF p-tau181 vs 217 cognitive decline; precision context |
| [28] | Janelidze et al., Nat Med 2020 | Background — plasma p-tau181 differential diagnosis |
| [29] | Bornhorst et al., Neurology 2025 | Background — CKD effect on plasma p-tau217 |
| [30] | Twait et al., J Am Heart Assoc 2024 | Background — plasma markers vs MRI vascular load |
| [31] | Kang et al., JAMA Netw Open 2025 | Background — CAA and AD plasma biomarkers |
| [32] | Mattsson-Carlgren et al., JAMA Neurol 2023 | Background — plasma biomarkers predict decline |
| [33] | Ossenkoppele et al., Nat Aging 2025 | Background — p-tau217/tau-PET predict decline |
| [34] | Du et al., Alzheimers Dement 2024 | Background — longitudinal p-tau217 |
| [35] | CLSI EP15-A3, 2017 | Method — precision guideline (see RW11); also cited for CSF cut-offs |
| [39] | Wojdała et al., Alzheimers Res Ther 2024 | Discussion — Simoa/Lumipulse assay performance; standardization |
| [40] | Arslan et al., Clin Chem Lab Med 2025 | Discussion — p-tau217 standardization/harmonization |
| [41] | Ashton et al., Alzheimers Dement 2025 | Discussion — GBSC plasma phospho-tau Round Robin |
| [42] | Chen et al., J Neurochem 2025 | Discussion — plasma vs serum equivalence |
| [43] | Benedet et al., Clin Chem 2025 | Discussion — serum p-tau217 diagnostic value |
| [45] | Elecsys Phospho-Tau (181P) Plasma leaflet | Discussion — FDA-cleared p-tau181 use |
| [46] | Ashton et al., JAMA Neurol 2024 | Discussion — p-tau217 immunoassay accuracy (duplicate of [7]) |
| [47] | Groot et al., Alzheimers Res Ther 2022 | Discussion — novel p-tau217 assay correlation/agreement |
| [48] | Therriault et al., EBioMedicine 2024 | Discussion — two p-tau217 assays comparison |
| [51] | Hu et al., Med 2024 | Discussion — fluid biomarkers with amyloid-targeting DMTs |
| [52] | Milà-Alomà et al., Nat Med 2022 | Discussion — p-tau231/217 as amyloid state markers (discordant CSF) |

Note: reference numbering in the running text vs the References list has a minor offset for the
CLSI/Leitão citations (text cites CLSI EP15-A3 as [36] while it is item 35 in the list, and Leitão
2019 is item 36); reproduced as printed without silent correction.
