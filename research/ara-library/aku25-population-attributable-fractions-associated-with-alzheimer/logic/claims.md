# Claims

> All claims are transcribed from the conference abstract (Innovation in Aging 2025, Vol. 9,
> Suppl. 2, pp. 743–744). Because the source is an abstract, the reported values carry **no
> confidence intervals, no sample sizes, and no methodological qualifiers** — those are "Not
> specified in the published abstract". Each load-bearing number carries a `**Sources**` entry with
> the verbatim abstract quote it was read from; tagged `[result]` because these are values the
> study reports (an abstract has no separate input recipe to cite).

## C01: A nine-disease multivariable Cox model captures the primary determinants of AD/ADRD risk variation
- **Statement**: A multivariable Cox model with nine diseases — heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, traumatic brain injury, and diabetes mellitus — was identified as the set of primary determinants of variation in AD/ADRD risk.
- **Status**: supported
- **Falsification criteria**: Refuted if re-analysis of the Medicare 5% sample finds that a different or materially smaller/larger predictor set (e.g., excluding one of these nine or requiring additional diseases) is needed to capture the primary variation in AD/ADRD risk, or if these nine are not jointly significant.
- **Proof**: [E01, E02]
- **Evidence basis**: The abstract states this nine-disease set was "identified" as the model of "primary determinants of variation in AD/ADRD risk"; the selection was performed via univariable then multivariable Cox modeling.
- **Interpretation**: The compact predictor set implies these comorbidities are the dominant modeled drivers, but the abstract does not report each disease's hazard ratio or the selection threshold, so the ranking within the nine is only partially observable.
- **Dependencies**: none
- **Tags**: cox-model, predictor-selection, comorbidity, AD/ADRD
- **Sources**:
  - nine diseases (heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, traumatic brain injury, diabetes mellitus) ← Abstract, p. 744 «The identified model included nine diseases—heart failure, hypertension, arrhythmia, stroke, hypotension, renal disease, depression, traumatic brain injury, and diabetes mellitus—as primary determinants of variation in AD/ADRD risk.» [result]

## C02: The fraction of total PAF explained by the predictors increases with age
- **Statement**: The fraction of the total population attributable fraction (PAF) explained by the nine-disease predictor set increased with age.
- **Status**: supported
- **Falsification criteria**: Refuted if the explained fraction of total PAF is flat or decreasing across age strata in the same cohort.
- **Proof**: [E03]
- **Evidence basis**: Direct statement in the abstract; no numeric age-stratified PAF values are reported.
- **Interpretation**: Suggests the modeled comorbidities account for a progressively larger share of attributable AD/ADRD risk at older ages, but the magnitude and the age bins are unspecified.
- **Dependencies**: C01
- **Tags**: PAF, age-gradient, attributable-risk
- **Sources**:
  - explained fraction of total PAF increases with age ← Abstract, p. 744 «The fraction of the total PAF explained by the predictors increased with age.» [result]

## C03: Hypertension, stroke, and depression are the strongest disease-specific PAF contributors across all subpopulations
- **Statement**: In the decomposition of total PAF into disease-specific PAFs, hypertension, stroke, and depression provided the strongest contribution for all subpopulations.
- **Status**: supported
- **Falsification criteria**: Refuted if, in any studied subpopulation, a disease outside {hypertension, stroke, depression} outranks all three as a PAF contributor.
- **Proof**: [E03, E04]
- **Evidence basis**: The abstract states these three "provided the strongest contribution for all subpopulations."
- **Interpretation**: Positions these three (all modifiable) as the priority prevention targets population-wide, though which of the three leads depends on the subpopulation (see C04–C07).
- **Dependencies**: C01
- **Tags**: PAF-decomposition, hypertension, stroke, depression
- **Sources**:
  - hypertension, stroke, depression strongest for all subpopulations ← Abstract, p. 744 «hypertension, stroke, and depression provided the strongest contribution for all subpopulations» [result]

## C04: Hypertension reaches 45–50% of total PAF for Black, Asian, and Hispanic subpopulations
- **Statement**: Hypertension reached 45–50% of total PAF for the Black, Asian, and Hispanic subpopulations.
- **Status**: supported
- **Falsification criteria**: Refuted if the hypertension share of total PAF for any of these three subpopulations falls outside the 45–50% band on re-analysis.
- **Proof**: [E04]
- **Evidence basis**: Direct numeric statement in the abstract.
- **Interpretation**: Hypertension is the single dominant attributable contributor in these minority subpopulations, roughly half of the total attributable burden — a notably larger share than its population-average role.
- **Dependencies**: C03
- **Tags**: hypertension, health-disparities, race-stratified, PAF
- **Sources**:
  - hypertension 45-50% of total PAF for Black, Asian, Hispanic ← Abstract, p. 744 «Hypertension reached 45-50% of total PAF for Black, Asian, and Hispanic subpopulations.» [result]

## C05: Stroke is the primary PAF contributor for males (>30%)
- **Statement**: Stroke was the primary contributor to total PAF for males, exceeding 30%.
- **Status**: supported
- **Falsification criteria**: Refuted if, for males, stroke is not the top-ranked disease-specific PAF contributor or its share is ≤30%.
- **Proof**: [E04]
- **Evidence basis**: Direct statement in the abstract.
- **Interpretation**: Sex-specific prioritization: cerebrovascular disease dominates attributable AD/ADRD burden in men.
- **Dependencies**: C03
- **Tags**: stroke, sex-stratified, males, PAF
- **Sources**:
  - stroke primary contributor for males (>30%) ← Abstract, p. 744 «Stroke was the primary contributor for males (>30%)» [result]

## C06: Depression is the highest PAF contributor among females and White individuals (~30%)
- **Statement**: Depression was the highest disease-specific PAF contributor among females and among White individuals, at approximately 30%.
- **Status**: supported
- **Falsification criteria**: Refuted if depression is not the top contributor for females or for White individuals, or if its share deviates materially from ~30%.
- **Proof**: [E04]
- **Evidence basis**: Direct statement in the abstract; value is approximate ("approximately 30%").
- **Interpretation**: Complements C05 — the leading attributable driver flips from stroke (males) to depression (females / White individuals), underscoring demographic heterogeneity.
- **Dependencies**: C03
- **Tags**: depression, sex-stratified, race-stratified, females, White, PAF
- **Sources**:
  - depression highest for females and White individuals (~30%) ← Abstract, p. 744 «depression was highest among females and White individuals (approximately 30%)» [result]

## C07: Hypertension and depression are the leading PAF contributors for Native Americans (both ~30%)
- **Statement**: For Native Americans, hypertension and depression were the leading disease-specific PAF contributors, both at approximately 30%.
- **Status**: supported
- **Falsification criteria**: Refuted if, for the Native American subpopulation, hypertension and depression are not co-leading or their shares deviate materially from ~30%.
- **Proof**: [E04]
- **Evidence basis**: Direct statement in the abstract; values approximate.
- **Interpretation**: A distinct two-way lead (hypertension + depression) characterizes the Native American subpopulation, differing from the single-disease dominance seen elsewhere.
- **Dependencies**: C03
- **Tags**: hypertension, depression, Native-American, health-disparities, PAF
- **Sources**:
  - hypertension and depression leading for Native Americans (both ~30%) ← Abstract, p. 744 «Hypertension and depression were the leading contributors for Native Americans (both approximately 30%).» [result]

## C08: Heart failure is the fourth strongest PAF contributor for all subpopulations, exceeding 5% for Native Americans
- **Statement**: Heart failure was the fourth strongest disease-specific PAF contributor for all subpopulations, with its contribution exceeding 5% for Native American individuals.
- **Status**: supported
- **Falsification criteria**: Refuted if heart failure does not rank fourth in any subpopulation, or if its contribution among Native Americans is ≤5%.
- **Proof**: [E04]
- **Evidence basis**: Direct statement in the abstract.
- **Interpretation**: After the top three (hypertension/stroke/depression), heart failure is the consistent next contributor, most pronounced in the Native American subpopulation.
- **Dependencies**: C03
- **Tags**: heart-failure, PAF-ranking, Native-American
- **Sources**:
  - heart failure fourth strongest for all subpopulations, >5% for Native Americans ← Abstract, p. 744 «Heart Failure was the fourth strongest contributor for all subpopulations, with the contribution exceeding 5% for Native American individuals.» [result]

## C09: Several secondary diseases contribute PAFs exceeding 3% in specific subpopulations
- **Statement**: Additional noteworthy contributors with PAFs exceeding 3% included hypotension (males), diabetes (Asian, Hispanic), arrhythmia (males), and TBI (Black, Asian).
- **Status**: supported
- **Falsification criteria**: Refuted if any listed disease–subpopulation pairing does not exceed a 3% PAF contribution on re-analysis.
- **Proof**: [E04]
- **Evidence basis**: Direct statement in the abstract.
- **Interpretation**: Beyond the top four, the attributable-burden tail is subpopulation-specific (e.g., diabetes matters for Asian/Hispanic groups; TBI for Black/Asian groups; hypotension and arrhythmia for males).
- **Dependencies**: C03, C08
- **Tags**: hypotension, diabetes, arrhythmia, TBI, subpopulation, PAF
- **Sources**:
  - PAFs >3%: hypotension (males), diabetes (Asian, Hispanic), arrhythmia (males), TBI (Black, Asian) ← Abstract, p. 744 «Additional noteworthy contributors with PAFs exceeding 3% included hypotension (males), diabetes (Asian, Hispanic), arrhythmia (males), and TBI (Black, Asian).» [result]
