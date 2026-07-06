# Related Work

Typed dependency graph over the paper's References list (PDF p.29–39, refs 1–67). Works with a specific technical delta relative to this paper get full `RW` blocks; other cited works are captured more briefly to preserve the paper's full citation footprint.

## RW01: Jack et al., 2024 — NIA-AA revised criteria for diagnosis and staging of AD
- **DOI**: 10.1002/alz.13859
- **Type**: imports
- **Delta**:
  - What changed: Introduces the Core 1 (amyloid-associated) / Core 2 (aggregated-tau/neurodegeneration-associated) biomarker staging framework used to position VeraBIND Tau.
  - Why: This paper explicitly frames VeraBIND Tau as a candidate Core 2 biomarker within this NIA-AA schema (Discussion, PDF p.23, 27).
- **Claims affected**: C01–C12 (framing), concept "Core 1/Core 2 Biomarker Framework"
- **Adopted elements**: A/T biomarker positivity nomenclature; Core 1/Core 2 staging concept.

## RW02: Ossenkoppele et al., 2022 (Nat Med) — A+T+ CU risk of cognitive decline
- **DOI**: 10.1038/s41591-022-02049-x
- **Type**: imports
- **Delta**:
  - What changed: Establishes the 53–57% 3–5-year cognitive-decline risk figure for A+T+ CU individuals that motivates this paper's focus on tau-PET-positive screening (O1 in `problem.md`).
  - Why: Provides the epidemiological rationale for why detecting A+T+ status specifically (not just A+) matters clinically.
- **Claims affected**: motivates G1/O1 (problem framing); not directly a claim in claims.md
- **Adopted elements**: Risk stratification figures cited in Introduction.

## RW03: Moscoso et al., 2025 (JAMA) — Frequency and clinical outcomes of tau-PET positivity
- **DOI**: 10.1001/jama.2025.7817
- **Type**: imports
- **Delta**:
  - What changed: Supplies the population prevalence estimates (10% tau-PET+ in CU, 60% in CI) used as external priors to compute PPV/NPV in this study, rather than using this cohort's own enriched-sample prevalence.
  - Why: Ensures reported PPV/NPV reflect real-world (population-level) screening performance rather than this study's convenience-sample composition.
- **Claims affected**: C03 (PPV comparison depends on these priors)
- **Adopted elements**: 10%/60% prevalence figures (Table 3 footnote, PDF p.42).

## RW04: Bayart et al. (in revision) — Robustness of plasma pTau217 diagnostic thresholds
- **DOI**: Not specified in paper (listed as "Revis." / in revision, ref 19)
- **Type**: baseline
- **Delta**:
  - What changed: Establishes the three pTau217 thresholds (0.142/0.193/0.256 pg/mL) used throughout this paper as the amyloid-optimized comparator cutoffs for pTau217.
  - Why: These thresholds, derived in an independent 411-person multicentric cohort partially overlapping with this dataset, are re-purposed here as the benchmark against which VeraBIND Tau's tau-PET diagnostic performance is compared (Table 3).
- **Claims affected**: C03, C04, C05
- **Adopted elements**: The three numeric thresholds and their original calibration targets (95% sensitivity / balanced / 95% specificity for amyloid-PET).

## RW05: Therriault et al., 2025 (Lancet Neurol) — Meta-analysis of blood pTau diagnostic accuracy
- **DOI**: 10.1016/S1474-4422(25)00227-3
- **Type**: bounds
- **Delta**:
  - What changed: Documents that pTau217's accuracy for AD diagnosis, while excellent in CI, is systematically lower in CU individuals — the specific gap (G1) this paper's assay targets.
  - Why: Frames the unmet need (low CU accuracy of the leading plasma biomarker) that motivates evaluating a functional seeding assay.
- **Claims affected**: motivates G1; contextualizes C03
- **Adopted elements**: The CU-vs-CI accuracy gap framing.

## RW06: Khalafi et al., 2025 (Alzheimers Dement) — Meta-analysis of pTau217 accuracy in CU vs. CI
- **DOI**: 10.1002/alz.14458
- **Type**: bounds
- **Delta**: Corroborates RW05's finding of lower pTau217 accuracy in CU individuals from an independent meta-analytic source.
- **Claims affected**: motivates G1
- **Adopted elements**: CU-accuracy-gap framing.

## RW07: Horie et al., 2025 (Nat Med) — Plasma MTBR-tau243 identifies tau tangle pathology
- **DOI**: 10.1038/s41591-025-03617-7
- **Type**: baseline
- **Delta**:
  - What changed: MTBR-tau243, an alternative emerging Core 2 plasma biomarker, shows the strongest correlation with tau-PET/cognition among tested species (vs. pTau205/pTau217) and outperforms them at intermediate/advanced Braak-like stages (≥3), but this paper's VeraBIND Tau instead shows its largest relative advantage at low Braak-like stages (1–3).
  - Why: Positions VeraBIND Tau's early-stage detection advantage (C04) as complementary to, and distinct from, MTBR-tau243's advanced-stage advantage — both are candidate Core 2 markers but with different stage-dependent strengths.
- **Claims affected**: C04, C05 (comparative framing in Discussion, PDF p.23–24)
- **Adopted elements**: None directly adopted; used as a comparative benchmark in Discussion.

## RW08: Montoliu-Gaya et al., 2024 (Acta Neuropathol) — Optimal blood tau species for AD neuropathology detection
- **DOI**: 10.1007/s00401-023-02660-3
- **Type**: bounds
- **Delta**: Mass-spectrometry/immunoprecipitation study surveying which blood tau species best track neuropathology; cited among evidence that pTau species generally track amyloid more than tau pathology.
- **Claims affected**: motivates G1/O3
- **Adopted elements**: None directly adopted.

## RW09: Lantero-Rodriguez et al., 2024 (Mol Neurodegener) — Plasma N-terminal tau fragments (NTA-tau)
- **DOI**: 10.1186/s13024-024-00707-x
- **Type**: baseline
- **Delta**: An alternative ultrasensitive plasma assay (targeting N-terminal tau fragments) also shown to have high performance for identifying advanced Braak stages, cited as further evidence that early-stage blood-based tau detection remains generally challenging across assay types.
- **Claims affected**: contextualizes C04 (Discussion, PDF p.24)
- **Adopted elements**: None directly adopted.

## RW10: Hu et al., 2016; Alonso et al., 1994; Alonso et al., 1996 — Prion-like tau seeding mechanism
- **DOI**: 10.1016/j.jalz.2016.01.014 (Hu 2016); 10.1073/pnas.91.12.5562 (Alonso 1994); 10.1038/nm0796-783 (Alonso 1996)
- **Type**: imports
- **Delta**:
  - What changed: Establishes the foundational biological mechanism — hyperphosphorylated tau binding to and sequestering/templating normal tau, disassembling microtubules and propagating pathology — that the VeraBIND Tau assay is designed to functionally measure.
  - Why: Directly motivates the Key Insight in `problem.md` (measuring seeding activity, not phosphorylation level).
- **Claims affected**: motivates Key Insight; concept "PA pTau / Tau Seeding Activity"
- **Adopted elements**: The seeding/templating mechanism itself as the assay's design rationale.

## RW11: Soldo, Iqbal, Bergmann & Ansari — VeraBIND assay patent (PCT/US24/50852, filed Oct. 10, 2024)
- **DOI**: Not applicable (patent application, not a journal DOI)
- **Type**: imports
- **Delta**:
  - What changed: Describes the underlying VeraBIND™ purification/detection method (capture beads, recombinant tau binding, AP-conjugate detection) that this paper clinically evaluates for the first time against tau-PET.
  - Why: This paper is the first diagnostic-performance validation of the assay described in the patent.
- **Claims affected**: C01–C12 (the assay itself); concept "VeraBIND™ Technology"
- **Adopted elements**: The full assay protocol (Methods, PDF p.9–11; mirrored in `logic/solution/method.md`).

## RW12: Gérard et al., 2025 (Eur J Neurol) — [18F]MK6240 limited affinity for primary tauopathies
- **DOI**: 10.1111/ene.70068
- **Type**: bounds
- **Delta**:
  - What changed: Establishes that [18F]MK6240, the tau-PET tracer used as this paper's reference standard, has limited affinity for primary (non-AD, e.g., 4R) tauopathies and high specificity for AD.
  - Why: Directly explains this paper's discordant cases (e.g., the A-T- corticobasal-degeneration case with a positive VeraBIND Tau result) as likely tracer insensitivity rather than assay false-positivity (C12).
- **Claims affected**: C12
- **Adopted elements**: The tracer-limitation caveat, carried into this paper's Discussion and Table 2 footnote.

## Other cited works (background, methods, or infrastructure references — no distinct technical delta claimed)
- **Plasma pTau species immunoassays** (refs 10–17: Milà-Alomà et al. 2022; Karikari et al. 2020; Ashton et al. 2021; Janelidze et al. 2020; Teunissen et al. 2024; Verberk et al. 2018; Kac et al. 2025 ×2) — background on the pTau181/205/212/217/231 biomarker landscape this paper compares against.
- **pTau217/plasma-vs-PET concordance studies** (refs 18, 20–23, 26–29, 62–63: Therriault et al. 2023; Mattsson-Carlgren et al. 2021, 2024; Ashton et al. 2024; Salvadó et al. 2023; Montoliu-Gaya et al. 2023; Woo et al. 2024; Shin et al. 2025; Feizpour et al. 2025; Salvadó et al. 2025) — supporting literature on pTau217's amyloid- vs. tau-tracking behavior and Braak-stage-dependent accuracy.
- **Head-to-head plasma biomarker comparisons** (refs 54–57: Anastasi et al. 2025; Kwon et al. 2025; Rissman et al. 2024; Mendes et al. 2024) — comparative context for pTau217 vs. pTau181/231 diagnostic performance.
- **CSF Core 2 biomarkers** (refs 58–60: Barthélemy et al. 2023; Lantero-Rodriguez et al. 2024; Horie et al. 2023) — CSF-based pTau205/MTBR-tau243 validation work preceding the plasma-based extensions discussed above.
- **Assay/technique infrastructure** (ref 34: Rissin et al. 2010, Simoa method; ref 67: Katzman et al. 2021, biotin-interference control) — underlying immunoassay platform methodology.
- **Amyloid/Centiloid and PET methodology** (refs 35–42: Hanseeuw et al. 2021; Amadoru et al. 2020; Bayart et al. 2019; Gérard et al. 2024; Zhang et al. 2011; Greve et al. 2014, 2016; Desikan et al. 2006) — imaging pipeline and atlas methods adopted directly in this paper's own PET processing (`src/environment.md`).
- **Cognitive assessment instruments** (refs 43–50, 66: Folstein et al. 1975 [MMSE]; Adam et al. 2004; de Partz et al. 2001; Reitan 1955; Bianconi et al. 2005; Rouleau et al. 1992; Morris et al. 1989 [CERAD]; Ivanoiu et al. 2015; Colmant et al. 2023) — neuropsychological battery adopted verbatim in Methods.
- **Genetic/epidemiological risk background** (refs 64–65: Roses 1996; Corder et al. 1993) — APOE ε4 risk-allele background motivating the CU-sample enrichment strategy.
- **Prior plasma Aβ42/Aβ40 work by the same group** (refs 7–9: Colmant et al. 2024; Vergallo et al. 2019; Boyer et al. 2024) — establishes the Aβ42/Aβ40 threshold/assay used as one comparator biomarker in this paper.
