# Related Work — Typed Dependency Graph

Works with a specific technical delta relative to this paper get full RW blocks. The paper's
remaining citation footprint is captured briefly at the end.

## RW01: Ashton et al., 2023 — Plasma and CSF biomarkers head-to-head
- **DOI**: (Alzheimers Dement 19, 1913–1924, 2023) — ref 46
- **Type**: imports
- **Delta**:
  - What changed: This paper adopts Ashton et al.'s indirect evidence that doubly phosphorylated tau
    (p-tau181 & p-tau231) exists in CSF, and builds a *direct* dual-site sandwich assay for it.
  - Why: To measure co-phosphorylation directly rather than infer it by immunoprecipitation + MS.
- **Claims affected**: C01, C06
- **Adopted elements**: Anti-p-tau231 capture antibody (ADx253, ADx NeuroSciences) also used in
  Ashton's p-tau231 work; conceptual basis for doubly phosphorylated species (ref 18).

## RW02: Ashton et al., 2021 — Plasma p-tau231 as incipient AD biomarker
- **DOI**: (Acta Neuropathologica 141, 709–724, 2021) — ref 18
- **Type**: imports / baseline
- **Delta**:
  - What changed: Provides the p-tau231 antibody and prior demonstration (via immunoprecipitation +
    targeted MS) that after CSF IP with anti-p-tau181 one can detect T231-phosphorylated peptides,
    confirming doubly phosphorylated species indirectly.
  - Why: Motivates and validates the sandwich-assay design targeting T231 + a second site.
- **Claims affected**: C01, C06
- **Adopted elements**: p-tau231 capture antibody; power-analysis estimates.

## RW03: Barthélemy et al., 2020 — Soluble phosphorylated tau staging signature
- **DOI**: (Alzheimers Dement 26, 398–407, 2020) — ref 29
- **Type**: bounds / extends
- **Delta**:
  - What changed: Proposed CSF tau staging with site-specific phosphorylation trajectories (p-tau217
    rises before p-tau181); this paper tests whether *co*-phosphorylation adds staging value.
  - Why: Frames the hypothesis that multi-site phosphorylation is an enhanced proxy for AD stage.
- **Claims affected**: C05, C07
- **Adopted elements**: Site-trajectory framing.

## RW04: Janelidze et al., 2020 — CSF p-tau217 outperforms p-tau181
- **DOI**: (Nat. Commun. 11, 1–12, 2020) — ref 10
- **Type**: baseline
- **Delta**:
  - What changed: Establishes single-site p-tau217 as a strong AD marker; this paper compares its
    doubly phosphorylated p-tau217&231 against single-site p-tau217/p-tau231.
  - Why: p-tau217/p-tau231 are the diagnostic benchmarks the new proteoform must beat.
- **Claims affected**: C03, C08
- **Adopted elements**: Single-site p-tau217 as comparator.

## RW05: Jack et al., 2018 — NIA-AA A/T/N research framework
- **DOI**: (Alzheimers Dement 14, 535–562, 2018) — ref 47
- **Type**: imports
- **Delta**:
  - What changed: Defines the A/T/N biomarker classification used as ground truth for the AD
    continuum (A+/T+ CSF profile).
  - Why: Provides the diagnostic reference standard against which assay accuracy is measured.
- **Claims affected**: C02, C08 (and cohort definition)
- **Adopted elements**: A/T/N classification and continuum definition.

## RW06: Rissin et al., 2010 / Teunissen et al., 2023 — Simoa platform & biomarker methods
- **DOI**: (Nat. Biotechnol. 28, 595–599, 2010, ref 43; Mol. Cell. Proteom. 22, 100629, 2023, ref 44)
- **Type**: imports
- **Delta**:
  - What changed: The single-molecule array (Simoa) platform and biofluid biomarker development
    methodology underpin the assay technology used here.
  - Why: Ultrasensitive detection at subfemtomolar concentrations enables measuring low-abundance
    doubly phosphorylated tau in plasma.
- **Claims affected**: C01
- **Adopted elements**: Simoa HD-X platform, assay-development/validation methodology.

## RW07: Bellomo et al., 2021 — CSF core-biomarker cut-offs
- **DOI**: (Front. Neurosci. 15, 1–9, 2021) — ref 48
- **Type**: imports
- **Delta**:
  - What changed: Source of the CSF cut-off values (Aβ42/Aβ40 = 0.072; p-tau181 = 50; t-tau = 393)
    used for A/T/N classification.
  - Why: Defines the thresholds for cohort assignment.
- **Claims affected**: C02, C08
- **Adopted elements**: Machine-learning-derived core biomarker cut-offs.

## RW08: Cohen, 1988 — Standardized effect size
- **DOI**: (Statistical Power Analysis for the Behavioral Sciences, Routledge, 1988) — ref 54
- **Type**: imports
- **Delta**:
  - What changed: Provides Cohen's d and its interpretive thresholds (large/medium/small/negligible).
  - Why: Used to quantify group-separation effect sizes.
- **Claims affected**: C03, C04, C05
- **Adopted elements**: Effect-size thresholds.

---

## Additional citation footprint (brief)

- **AD epidemiology / therapies**: refs 1–5 (Alzheimer's facts & figures; lecanemab and
  amyloid-targeting therapies — van Dyck 2023, Söderberg 2023, Jönsson 2023).
- **Fluid biomarker reviews / single-site p-tau performance**: refs 6–9, 11–17, 19–23, 31, 32
  (Blennow & Zetterberg 2018; Gobom 2022; Barthélemy 2023 p-tau217/205; Kac 2024 p-tau212;
  Thijssen 2020/2021; Milà-Alomà 2022; Janelidze 2020 p-tau181; Palmqvist 2020 p-tau217;
  Barthélemy 2020 blood isoforms; Wilson 2022 Lumipulse; Brickman 2021; Montoliu-Gaya 2023;
  Lantero Rodriguez 2020/2024; Gonzalez-Ortiz 2024; Yu 2023; Leuzy 2021).
- **Tau PTMs / phosphorylation biology & brain-tissue MS**: refs 24–28, 30, 33–38
  (Wegmann 2021; Kimura 2018; Wesseling 2020; Barthélemy 2020 MS rates; Drepper 2020;
  Wang 2015 axonal transport; Kyalu Ngoie Zola 2023; Lantero-Rodriguez 2024 brain; Cicognola
  2019; Sato 2018; Brinkmalm 2023; Horie 2020).
- **Kidney/comorbidity effects on plasma tau**: refs 40, 41 (Dugger 2016; Janelidze 2023).
- **Methods/tools/consensus**: refs 39 (Cicognola 2019 fragments), 42 (Karikari 2020),
  45 (Vanmechelen & Vanderstichele 2002), 49 (Rascovsky 2011 bvFTD criteria), 50 (Gorno-Tempini
  2011 PPA), 51 (Teunissen 2009 CSF consensus), 52 (Rózga 2019 preanalytical), 53 (R Core Team 2019).
