# Related Work — typed dependency graph

Type legend: `imports` (uses directly), `extends` (builds on/updates), `bounds` (defines
methodological limits), `baseline` (comparator/data source), `refutes`. The paper cites 43
references. Unlike a typical GBD-descendant burden paper (e.g., which would cite a prior
GBD-cycle dementia study by name for direct trend comparison — see the `ami25-*` ARA in this
library for a contrasting example), **this paper cites no prior GBD-based AD/dementia burden or
projection study anywhere in its 43 references**. Instead, its reference list shows a recurring
pattern in which citations attached to specific methodological claims (ASR formula, EAPC formula,
GAM, Mann-Whitney U, "371 diseases... age-standardization") resolve to GBD sub-studies of
*unrelated* diseases (respiratory infection, meningitis, hepatitis B, cancer, alcohol, diabetes,
headache, intentional injuries, neonatal mortality) rather than to a dementia-specific source or a
generic statistics/methods reference. Full `RW` blocks below are given for these methodology
citations (the paper's only real reference-level "dependencies") plus the GBD 2021 data source
itself; brief grouped entries preserve the remaining 34 references that carry no distinct
methodological delta. This is reported as a factual, source-grounded observation about the
citation footprint (Rule 10), not corrected or hidden.

## RW01: Global Burden of Disease (GBD) Study 2021, via the GHDx platform (data source; not a numbered in-text reference)
- **DOI**: Not stated in paper.pdf (accessed via https://ghdx.healthdata.org)
- **Type**: baseline / imports
- **Delta**:
  - What changed: Supplies every base estimate this paper analyzes — age-standardized incidence,
    death, and DALY rates for Alzheimer's disease, 1990–2021, globally and by sex/SDI/region/
    country. GBD 2021 newly incorporated AD incidence data (81 data points, 60 locations) and
    excluded USA claims data from dementia modeling.
  - Why: This paper performs no primary data collection; GBD 2021/GHDx is the sole empirical
    input to every claim (C01–C08).
- **Claims affected**: C01, C02, C03, C04, C05, C06, C07, C08
- **Adopted elements**: ASIR, ASDR, and age-standardized DALY-rate estimates (1990–2021) with 95%
  uncertainty intervals, at every stratification level (global, sex, SDI tier, GBD region,
  country); ICD-9/ICD-10 AD case definition (see RW06).

## RW02: Refs (15) and (16) — cited for the ASR / age-standardization formula (Methods §2.2)
- **DOI**: Ref 15 doi not verified in paper.pdf reference list beyond title; ref 16 likewise.
- **Type**: imports (nominally — see mismatch note)
- **Delta**:
  - What changed: In-text, these citations are presented as supplying the ASR weighted-average
    formula (ASR = Σᵢwᵢrᵢ) and the standard-population-weight formula (wᵢ = Pᵢ/ΣPᵢ) this paper uses
    throughout.
  - Why (as framed): To ground the age-standardization method in prior GBD methodology.
  - **Mismatch**: Ref 15 in the reference list is "GBD 2019 Mental Disorders Collaborators...
    Global, regional, and national burden of hepatitis B, 1990-2019" (a hepatitis B burden paper,
    whose own collaborator-group label ["Mental Disorders"] does not even match its own title
    ["hepatitis B"] — a second, nested inconsistency). Ref 16 is "GBD 2019 Adolescent Young Adult
    Cancer Collaborators... global burden of adolescent and young adult cancer." Neither concerns
    Alzheimer's disease, dementia, or age-standardization methodology specifically. See
    `logic/solution/constraints.md` C-d.
- **Claims affected**: C01–C08 (the ASR formula underlies every reported rate)
- **Adopted elements**: ASR formula and standard-population-weight formula, as reproduced in
  `logic/solution/study_design.md` §3 — the formulas themselves are standard GBD methodology
  regardless of the citation mismatch.

## RW03: Ref (17) — cited for the GAM model form (Methods §2.2)
- **DOI**: Not verified in paper.pdf reference list beyond title.
- **Type**: imports (nominally — see mismatch note)
- **Delta**:
  - What changed (as framed): Presented as the source for the GAM specification
    y = β₀ + s(x₁) + s(x₂) + … + s(xₙ) + ε used to forecast 2022–2030 ASRs.
  - **Mismatch**: Ref 17 in the reference list is "GBD 2020 Alcohol Collaborators... Population-
    level risks of alcohol consumption" — an alcohol-burden paper, not a GAM-methodology or
    dementia-forecasting source. See `logic/solution/constraints.md` C-d.
- **Claims affected**: C01 (the projection method underlying every 2022–2030 EAPC/ASR in C01–C08)
- **Adopted elements**: The GAM functional form, as reproduced in `logic/solution/study_design.md`
  §4.

## RW04: Ref (18) — cited for the EAPC formula (Methods §2.2)
- **DOI**: Not verified in paper.pdf reference list beyond title.
- **Type**: imports (nominally — see mismatch note)
- **Delta**:
  - What changed (as framed): Presented as the source for EAPC = 100×[(ASR_end/ASR_start)^(1/t)−1].
  - **Mismatch**: Ref 18 is "GBD 2019 LRI Collaborators... Age-sex differences in the global burden
    of lower respiratory infections" — unrelated to AD/dementia or specifically to the EAPC
    formula's derivation. See `logic/solution/constraints.md` C-d.
- **Claims affected**: C01–C08 (EAPC is the paper's primary summary statistic throughout)
- **Adopted elements**: EAPC formula, as reproduced in `logic/solution/study_design.md` §5.

## RW05: Refs (19) and (20) — cited for the Mann-Whitney U test description/formula (Methods §2.2)
- **DOI**: Ref 19 not verified beyond title; ref 20 is a journal erratum notice (no DOI given in
  paper.pdf beyond its title).
- **Type**: imports (nominally — see mismatch note)
- **Delta**:
  - What changed (as framed): Presented as the source for the Mann-Whitney U formula
    U = n₁n₂ + n₁(n₁+1)/2 − R₁, used for the SDI-threshold group comparisons in §3.5.
  - **Mismatch**: Ref 19 is "GBD 2019 Diabetes and Air Pollution Collaborators... global burden of
    type 2 diabetes attributable to PM(2.5) air pollution." Ref 20 is not a research paper at all —
    it is "Frontiers Production Office. Erratum: Burden of tracheal, bronchus, and lung cancer in
    North Africa and Middle East countries, 1990 to 2019," i.e., an erratum notice for an unrelated
    cancer-burden paper. See `logic/solution/constraints.md` C-d.
- **Claims affected**: C07 (the only claim whose statistical test is the Mann-Whitney U)
- **Adopted elements**: Mann-Whitney U formula, as reproduced in `logic/solution/study_design.md`
  §6.

## RW06: Refs (10), (11), (12) — cited for GBD's general scope/scale and modeling tools (Methods §2.1)
- **DOI**: Not verified in paper.pdf reference list beyond title.
- **Type**: imports (nominally — see mismatch note)
- **Delta**:
  - What changed (as framed): Refs 10/11 are cited for the "371 diseases and injuries...
    age-standardization" general GBD-scope description; ref 12 is cited for "advanced modeling
    tools, such as CODEm and DisMod-MR 2.1."
  - **Mismatch**: Ref 10 is "GBD 2015 Eastern Mediterranean Region Lower Respiratory Infections
    Collaborators"; ref 11 is "GBD 2015 Eastern Mediterranean Region Adolescent Health
    Collaborators"; ref 12 is "GBD 2016 Meningitis Collaborators" — none is a GBD 2021 general
    methods/overview paper or a CODEm/DisMod-MR 2.1 methods paper specifically. See
    `logic/solution/constraints.md` C-d.
- **Claims affected**: C01–C08 (general GBD pipeline description underlying all data)
- **Adopted elements**: The GBD-scope description ("371 diseases/injuries and 87 risk factors
  across 204 countries/territories") and the CODEm/DisMod-MR 2.1 upstream-tool references, as used
  in `logic/problem.md` O3 and `logic/solution/study_design.md` §2 and `logic/concepts.md`.

## RW07: Refs (13) and (14) — cited for the ICD diagnostic-code framework (Methods §2.1)
- **DOI**: Not verified in paper.pdf reference list beyond title.
- **Type**: bounds
- **Delta**:
  - What changed: Ref 13 (Jellinger, "Alzheimer's disease: a challenge for modern
    neuropathobiology") is plausibly relevant and AD-specific, supporting the ICD-9 290.0–290.9 /
    ICD-10 G30.0–G30.9 case-definition framework used throughout. Ref 14 (Lavano, "Neurosurgical
    treatment of Alzheimer's disease: where do we stand?") is an AD-relevant clinical paper but is
    not about ICD coding specifically.
  - Why: Bounds the case definition (and therefore ascertainment) underlying every GBD-derived
    estimate this paper reports.
- **Claims affected**: C01–C08 (case-definition scope underlies all AD-attributed estimates)
- **Adopted elements**: ICD-9 290.0/290.1/290.9 and ICD-10 G30.0/G30.1/G30.8/G30.9 as the reference
  case definition, per `logic/concepts.md` "ICD case-definition codes for Alzheimer's disease."

## Brief citation footprint (no distinct technical delta beyond the above)

**AD epidemiology and risk-factor background** (refs 1–9): Mantzavinos & Alexiou (AD biomarkers;
source of the "50 million individuals, projected to triple by 2050" figure); Libow (AD overview;
source of the "$1 trillion annually" economic-cost figure); McDaniel et al. (incorrect clinical
diagnosis; psychological/social burden framing); Liu et al. (neurovascular unit damage; "rising
prevalence" framing); Henderson (AD epidemiology; "complex interaction of genetic, environmental,
lifestyle factors"); Honig & Chin (AD; APOE ε4 mention); Kamal & Greig (AD molecular mechanisms;
lifestyle risk-factor framing); Klimova et al. (non-pharmacological AD prevention/treatment, rising
costs; chronic-condition risk-factor framing); Kwentus et al. (AD; "need for up-to-date,
comprehensive global data"). Support `logic/problem.md` O1, O2.

**Discussion-support references — AD clinical/biological narrative** (refs 21–37, 40): Alzheimer's
Association 2016 facts and figures; Harvard Women's Health Watch (AD aging); Lancet (three stages
of AD); Lancet Neurol (AD prevention, reality check); Abbott (conquering AD, Nature); Asaad & Lee
(fMRI in AD animal models); Beata et al. (AD biochemical/psychological background); Bayat & Roe
(driving assessment in preclinical AD); Bennett & Knopman (AD patient management); Bianchetti &
Trabucch (clinical aspects of AD); Blades (diet and AD); Bondi et al. (AD past/present/future);
Blass & Gibson (oxidative abnormalities in AD pathophysiology); Briggs et al. (drug treatments in
AD); Breteler (vascular risk factors for AD, epidemiologic perspective); Cammisuli et al.
(technological solutions for AD diagnosis/management); Brinton (women's health, AD, cognitive-
health strategies); Caraci et al. (depression and AD, neurobiological links). Cited throughout the
Discussion (§4, pp.6–9) to narratively interpret the projected trends — general AD clinical-care,
pathology, and policy reviews, not epidemiological burden studies this paper's estimates are
benchmarked against, and not separately tested by this study's data (see `logic/solution/
constraints.md` C-h).

**Generic "comprehensiveness / global perspective" references** (refs 38, 39, 41–43): GBD 2016
Collaborators (global/regional/national under-5, adult, and age-specific mortality and life
expectancy, 1970–2016); GBD 2015 Eastern Mediterranean Region Intentional Injuries Collaborators;
GBD 2016 Headache Collaborators (migraine/tension-type headache burden); GBD 2016 Alcohol and Drug
Use Collaborators; GBD 2015 Eastern Mediterranean Region Neonatal, Infant, and under-5 Mortality
Collaborators. Cited in the Discussion's Strengths section (p.9) to support "comprehensive view,"
"global perspective," and "improved data collection" claims; none is about AD/dementia specifically.

## Datasets and Clinical Trials (typed data dependencies)
Per `sources.yaml` (verified; do not re-verify): **no released code**, **no released dataset**
beyond the publicly queryable GHDx/GBD 2021 tool, and **no registered clinical trial** are
associated with this paper. `code: []`, `data: []`, `clinical_trials: []`.
- **Data dependency (type: baseline, access: publicly queryable via GHDx)**: GBD 2021 (RW01) is
  the sole data dependency; see `data/dataset.md` for full provenance.
- **No PROSPERO ID, NCT ID, or software repository** appears anywhere in the paper's full text.
