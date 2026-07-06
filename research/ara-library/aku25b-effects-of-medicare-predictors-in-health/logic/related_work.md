# Related Work

Typed dependency graph. Full `RW` blocks are given for works with a specific technical delta (methods this paper extends, bounds against, or compares to); the remaining citation footprint is captured briefly below.

## RW01: Yun, 2004 & Powers/Yun, 2009 — Oaxaca–Blinder decomposition for hazard-rate models
- **DOI**: 10.1016/j.econlet.2003.09.017 (Yun 2004); 10.1111/j.1467-9531.2009.01209.x (Powers & Yun 2009)
- **Type**: bounds
- **Delta**:
  - What changed: This paper's PAF-based decomposition is an alternative to the Yun–Powers adaptation of Oaxaca–Blinder decomposition for time-to-event data. Yun–Powers relies on two approximations — evaluating the mean of the nonlinear hazard as a function of mean risk factors, and linearizing the hazard via a first-order Taylor expansion.
  - Why: The PAF approach avoids those Taylor/mean-of-nonlinear approximations and derives exact mathematical expressions for exposure and vulnerability from the estimated Cox parameters.
- **Claims affected**: C01
- **Adopted elements**: the exposure/vulnerability estimand goal (quantifying prevalence vs risk contributions).

## RW02: Akushevich, Kolpakov, Yashkin, Kravchenko, 2022 — Vulnerability to hypertension as a determinant of racial disparities in AD
- **DOI**: 10.1093/ajh/hpac042
- **Type**: extends
- **Delta**:
  - What changed: An earlier Blinder–Oaxaca-based analysis (modified for censored data) identified disease-specific factors for Black–White AD disparities; the present study reproduces and generalizes that finding (hypertension's dominant role via vulnerability) using the new PAF decomposition across six disparities and four age cohorts.
  - Why: To confirm the hypertension-vulnerability result with an independent methodology and extend it beyond Black–White.
- **Claims affected**: C03, C05
- **Adopted elements**: hypothesis that hypertension vulnerability drives racial AD disparities; qualitative agreement used as validation.

## RW03: Akushevich, Yashkin, Kovtun, Stallard, Yashin, Kravchenko, 2023 — Decomposition of disparities applied to administrative claims and registry data
- **DOI**: 10.1016/j.tpb.2023.07.001
- **Type**: extends
- **Delta**:
  - What changed: Provides the decomposition-of-disparities framework for administrative health claims/registry data that this paper builds on and specializes to the PAF-based exposure/vulnerability split.
  - Why: Methodological lineage for applying disparity decomposition to Medicare data.
- **Claims affected**: C01
- **Adopted elements**: decomposition methodology for administrative data.

## RW04: VanderWeele and colleagues, 2010–2015 — Causal mediation analysis
- **DOI**: 10.1037/a0031034 (Valeri & VanderWeele 2013); 10.1093/aje/kwq332 (VanderWeele & Vansteelandt 2010); 10.1097/EDE.0b013e3182109296 (VanderWeele 2011)
- **Type**: imports
- **Delta**:
  - What changed: The paper positions its method within the causal-mediation family — the exposure/vulnerability split parallels mediator-prevalence vs mediator-effect mechanisms — and notes that a causal reading requires VanderWeele-style assumptions (no mediator–outcome confounding, sequential ignorability, mediator ordering).
  - Why: To delimit when the statistical decomposition supports causal interpretation.
- **Claims affected**: C01 (interpretation), A5 in problem.md
- **Adopted elements**: causal-mediation assumption framework as a caveat.

## RW05: Sudharsanan & Bijlsma, 2021 — g-formula decomposition of population health differences
- **DOI**: 10.1093/ije/dyab090
- **Type**: baseline
- **Delta**:
  - What changed: A parametric g-formula (Monte-Carlo integration) approach to decomposing population health differences; the present method is an alternative parametric-inference algorithm for time-to-event data.
  - Why: Situates the method among parametric causal-inference decomposition algorithms.
- **Claims affected**: C01
- **Adopted elements**: parametric decomposition perspective.

## RW06: Akushevich, Yashkin, Ukraintseva, Yashin, Kravchenko, 2023 — Multidomain risk model of AD/ADRD
- **DOI**: 10.3233/JAD-221292
- **Type**: imports
- **Delta**:
  - What changed: Supplies the set of AD/ADRD-related risk diseases (the 10 candidate predictors, Table S1) screened in the first analysis stage.
  - Why: Predictor selection grounding.
- **Claims affected**: C02, C04
- **Adopted elements**: the risk-disease predictor list.

## RW07: Akushevich et al., 2012 — Age patterns of geriatric disease incidence (Medicare-based); disease ascertainment algorithms (ref 18)
- **DOI**: 10.1111/j.1532-5415.2012.03971.x (ref 27); ascertainment algorithm (ref 18)
- **Type**: imports
- **Delta**:
  - What changed: Provides the previously published Medicare claims disease-ascertainment algorithms used to define binary predictors and the AD-onset outcome.
  - Why: Outcome and predictor measurement.
- **Claims affected**: C02, C08
- **Adopted elements**: claims-based ascertainment algorithms.

## RW08: Rank-and-replace / conditional decomposition methods
- **Type**: baseline
- **Delta**:
  - What changed: The paper contrasts its approach with rank-and-replace disparity methods (Rao et al. 2004; Lê Cook et al. 2010, 2012), the Pollard decomposition (1982), and Gelbach's conditional decomposition (2016) — all order-dependent or restricted to the parameter (vulnerability) channel.
  - Why: To motivate an order-independent method capturing both exposure and vulnerability.
- **Claims affected**: C01
- **Adopted elements**: none (comparison/critique baselines).

## Brief citation footprint (background, infrastructure, and inline references)

- **Life-expectancy and health-disparity background** — Olshansky et al. 2012 (ref 1); Dickman et al. 2017 (ref 2); Gutin & Hummer 2021 (ref 3); Dwyer-Lindgren et al. 2024 (ref 4); Chetty et al. 2016 (ref 11, income–life-expectancy). Motivate O1/G1.
- **AD/ADRD disparity reviews** — Akushevich et al. 2023 recommendations (ref 5); Mayeda et al. 2016 (ref 6); Co et al. 2021, 2023 (refs 7, 8); Mehta & Yeo 2017 (ref 9); Maestre et al. 2024 (ref 10). Background for O1.
- **Stroke belt definition** — Howard & Howard 2020 (ref 12): defines the stroke-belt geography used for the SB disparity.
- **Dual eligibility as SES indicator** — Joynt et al. 2017 (ref 13); Taylor et al. 2022 (ref 14); Roberts et al. 2019 (ref 15); Alberti & Baker 2020 (ref 16). Justify low income = Medicare/Medicaid dual eligibility.
- **Data infrastructure** — Friede et al. 1993 (ref 19, CDC WONDER); Barbieri et al. 2015 (ref 20, Human Mortality Database) — external references used to describe baseline population survival curves.
- **Causal-mediation identification** — Imai, Keele & Tingley 2010 (ref 22); Jackson & VanderWeele 2019 (ref 27, intersectional decomposition); Imai, Keele & Yamamoto 2010 (ref 37). Support the mediation framing/caveats.
- **Depression underdiagnosis in Black Americans** — Riley & Hill-Daniel 2020 (ref 38); Walton & Payne 2016 (ref 39); Jones, Drake & Lewis 2022 (ref 40). Qualify the depression PAF interpretation (C04).
- **Medicare Advantage comparisons / limitations** — Chen et al. 2019 (ref 41); Haye et al. 2023 (ref 42); Zissimopoulos et al. 2023 (ref 43). Referenced re: fee-for-service-only sample limitation.
- **Disparity-trend and scope references** — Chen et al. 2022 (ref 44); Mukadam et al. 2023 (ref 45); Burke et al. 2024 (ref 46); Chen & Zissimopoulos 2018 (ref 47); Hill et al. 2015 (ref 48); O'Neal 2024 (ref 49); Wiese et al. 2023 (ref 50, rural disparities). Background for persistence/growth of disparities.
