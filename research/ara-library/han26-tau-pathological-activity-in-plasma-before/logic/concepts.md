# Concepts

## Pathologically Active Hyperphosphorylated Tau (PA pTau) / Tau Seeding Activity
- **Notation**: PA pTau (abbreviation used throughout the paper)
- **Definition**: The subset of hyperphosphorylated tau (pTau) that retains the biological ability to bind to and template ("seed") normal tau, driving its misfolding and prion-like, propagating aggregation — as distinct from pTau that is merely phosphorylated at a given residue without this templating capacity.
- **Boundary conditions**: Defined functionally (by its seeding/binding behavior in the VeraBIND Tau assay), not by a specific phosphorylation site; the paper does not specify a minimum seeding threshold at the molecular level beyond the assay's semi-quantitative readout.
- **Related concepts**: VeraBIND Tau assay, Test result Score, tau-PET Braak-like stage.

## VeraBIND™ Technology / VeraBIND Tau Assay
- **Notation**: VeraBIND Tau (assay name); VeraBIND™ (Biomarker Isolation and eNrichment for Detection) (underlying technology name)
- **Definition**: A plasma-based functional immunoassay that (1) uses a pool of proprietary monoclonal antibody-coated capture beads to purify hyperphosphorylated tau (pTau) from plasma, removing the plasma matrix; (2) incubates the purified pTau with recombinant, tagged, full-length normal tau (Tau 1-441) under conditions mimicking the brain's pH/ionic/hydrophobic environment; and (3) detects, via an anti-tag alkaline-phosphatase-conjugated antibody and chemiluminescent substrate, the amount of recombinant normal tau bound — a relative luminescence signal (RLU) directly proportional to the amount of pathologically active pTau (PA pTau) in the sample. Described in the patent PCT/US24/50852 (Soldo, Iqbal, Bergmann & Ansari).
- **Boundary conditions**: Measures seeding/binding activity of purified plasma pTau, not its absolute concentration; requires the specific reagent set described in Methods (capture beads, recombinant Tau 1-441, AP-conjugated anti-tag antibody); performed at Veravas, Inc. and Access Genetics & OralDNA Labs.
- **Related concepts**: PA pTau, Test result Score.

## VeraBIND Tau Test Result Score
- **Notation**: Score = [Unknown signal response (RLU)] / [(Standard test result signal (RLU)) × (Correction Factor)]
- **Definition**: A semi-quantitative result computed by dividing a sample's raw luminescence signal (RLU) by an assay-run-specific Standard (a pool of EDTA plasma with known tau-PET-negative or young/healthy-donor status), corrected by a lot-specific correction factor. A Score <1.0 is a negative result (no detectable PA pTau); a Score ≥1.0 is a positive result. The assay's Negative Control (tau-PET-negative or young-donor plasma pool) has Score <0.93; its Positive Control (tau-PET-positive plasma pool) has Score >1.20.
- **Boundary conditions**: Applies only within a single assay run calibrated against its own Standard/Correction Factor; not an absolute concentration unit.
- **Related concepts**: VeraBIND Tau Assay, PA pTau.

## Braak-Like Tau-PET Staging
- **Notation**: Braak-like stage 0–6; T+ = stage>0; T- = stage 0
- **Definition**: A visual staging system, adapted from post-mortem Braak neurofibrillary staging, applied to [18F]MK6240 tau-PET images by two trained nuclear physicians, assigning each participant the furthest anatomical Braak-type region showing a significant tracer signal (excluding non-specific meningeal uptake); MRI segmentation assists reading for intricate scans.
- **Boundary conditions**: A visual (not fully automated/quantitative) read; explicitly noted in the Discussion to have "limited affinity for primary tauopathies" (ref 51) — i.e., [18F]MK6240 under-detects non-AD (e.g., 4R) tauopathies, which can create A-T- or A+T- discordant cases that are not true tau-negative individuals.
- **Related concepts**: SUVr, Entorhinal/inferior-temporal tau burden, A/T framework.

## A/T Biomarker Framework
- **Notation**: A+/A- (amyloid positive/negative), T+/T- (tau positive/negative); four combined groups: A-T-, A+T-, A+T+, A-T+
- **Definition**: A classification scheme combining amyloid status (A+ = Centiloid≥20 by amyloid-PET, or CSF Aβ42≤544 pg/mL) and tau status (T+ = Braak-like tau-PET stage>0) into four biomarker profile groups, used to define concordant (A-T-, A+T+) vs. discordant (A+T-, A-T+) cases for evaluating VeraBIND Tau's specificity for tau vs. amyloid pathology.
- **Boundary conditions**: Requires both an amyloid measure (PET or CSF) and a tau-PET measure per participant; not defined for participants missing either modality.
- **Related concepts**: Braak-like staging, Centiloid scale, Core 1/Core 2 biomarkers.

## Centiloid Scale
- **Notation**: Centiloid units; A+ defined as Centiloid≥20
- **Definition**: A standardized, semi-quantitative scale for amyloid-PET signal (here derived via the PNEURO v4.1 pipeline following a previously validated Centiloid pipeline) enabling comparison of amyloid burden across tracers ([18F]Flutemetamol, [11C]PiB) and centers.
- **Boundary conditions**: Threshold of ≥20 used here specifically to define amyloid positivity in this cohort, citing Amadoru et al. 2020 (ref 36) and the authors' own prior Centiloid-threshold work (ref 35).
- **Related concepts**: A/T framework, amyloid-PET.

## Core 1 / Core 2 Biomarker Framework (NIA-AA)
- **Notation**: Core 1 (amyloid/early-stage AD-change) vs. Core 2 (later-stage/neurodegeneration-associated) biomarkers
- **Definition**: A classification introduced in the NIA-AA revised criteria for AD diagnosis and staging (Jack et al. 2024, ref 1), under which pTau205, MTBR-tau243, and (per this paper's Discussion) VeraBIND Tau are positioned as candidate Core 2 biomarkers reflecting aggregated tau pathology, complementary to Core 1 biomarkers (e.g., plasma pTau217) that primarily reflect amyloid pathology.
- **Boundary conditions**: A conceptual/regulatory framework, not itself a measurement; the paper explicitly proposes VeraBIND Tau as filling the Core 2 role rather than replacing Core 1 pTau217 testing.
- **Related concepts**: A/T framework, pTau217 diagnostic thresholds.

## pTau217 Diagnostic Thresholds (0.142 / 0.193 / 0.256 pg/mL)
- **Notation**: 0.142 pg/mL, 0.193 pg/mL, 0.256 pg/mL
- **Definition**: Three plasma pTau217 concentration cutoffs, derived in an independent, large multicentric cohort of 411 individuals (Bayart et al., ref 19; partially overlapping with the current dataset), calibrated respectively to provide 95% sensitivity, an optimal sensitivity/specificity balance (~92%/~92%), and 95% specificity for amyloid-PET status.
- **Boundary conditions**: Originally calibrated against amyloid-PET status, not tau-PET status; this paper repurposes them as comparator thresholds for tau-PET prediction, which is itself part of the motivation for the comparison (pTau217 thresholds are amyloid-optimized, potentially disadvantaging pTau217 in a tau-specific comparison).
- **Related concepts**: Core 1/Core 2 framework, PPV/NPV with population prevalence.

## PPV/NPV Adjusted for Population Prevalence
- **Notation**: PPV, NPV
- **Definition**: Positive and negative predictive values computed not from the observed (enriched, non-representative) sample prevalence of tau-PET positivity, but from an external, recently published meta-analytic prevalence estimate (10% in CU individuals, 60% in CI individuals; Moscoso et al. 2025, ref 6), to better reflect real-world screening performance.
- **Boundary conditions**: Depends entirely on the validity/generalizability of the external prevalence estimates used as priors; a different assumed prevalence would change PPV/NPV even with identical sensitivity/specificity.
- **Related concepts**: A/T framework, pTau217 diagnostic thresholds.
