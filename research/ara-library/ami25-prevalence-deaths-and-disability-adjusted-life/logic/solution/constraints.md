# Constraints — assumptions, boundary conditions, and limitations

## Boundary conditions
- **Region**: 21 MENA ("North Africa and Middle East") countries only; not generalisable to other
  GBD regions.
- **Cause**: "Alzheimer's disease and other dementias" as a single GBD cause; the study cannot
  separate dementia subtypes (see L4).
- **Time**: 1990–2021, with 2021 as the reference year for cross-sectional results.
- **Age**: modelled/plotted in five-year bands, focus on 40–44 through 95+.
- **Metrics**: prevalence, deaths, DALYs as counts and age-standardised rates per 100,000.

## Assumptions (see also logic/problem.md A1–A5)
- GBD 2021 estimates faithfully represent true burden within their published uncertainty.
- The GBD case definition (DSM/ICD, CDR severity reference) is applied consistently enough to permit
  cross-country and cross-time comparison.
- Age-standardisation removes age-structure confounding.
- Significance = 95% UI (2.5th–97.5th percentile of 1000 draws) excludes zero.
- SDI adequately summarises development level for the expected-value comparison (Fig 4).

## Known limitations (stated by the authors, Strengths & Limitations, pp.9–10)
- **L1 — Wide uncertainty intervals**: GBD 2021 data collection produced wide UIs, particularly for
  low- and middle-income MENA countries, reducing precision. (Visible in the very wide death/DALY
  whiskers in Figures 1–2 and the broad UIs in Table 1.)
- **L2 — Data paucity and non-standardised case definitions**: sparse primary data and inconsistent
  use of standardised case definitions across included studies, especially in LMICs; regional
  conflicts and poor health-data systems worsen this. Modelling imputes in the absence of data but
  cannot substitute for high-quality data.
- **L3 — Case-definition misclassification**: defining AD via DSM or ICD criteria may cause
  misclassification and discrepancies in reported data.
- **L4 — No subtype separation**: the GBD data did not allow separation of dementia into subtypes;
  although AD dominates, other subtypes could influence interpretation. The authors recommend future
  GBD cycles separate subtypes.
- **L5 — COVID-19 disruption**: the pandemic overlapped data collection, causing delays and
  disruptions that may have affected data gathering/reporting/submission. The pandemic decreased life
  expectancy in every GBD super-region 2019–2021, most in those aged ≥25 (which includes most AD
  patients) and more severely in the Middle East among other regions; this should be considered when
  interpreting the results.

## Additional epistemic caveats (compiler-noted, grounded in the text)
- **C-a — Reproduced source inconsistency**: the Results text labels BOTH the highest death-ASR group
  (Afghanistan 33.27, Libya 28.04, Qatar 26.54) and the lowest group (Sudan 23.36, Jordan 23.37,
  Syrian Arab Republic 23.83) as "the lowest." This is internally inconsistent; preserved verbatim in
  `evidence/tables/table1.md` (Rule 10, honesty over completeness) rather than silently corrected.
- **C-b — Precision inconsistency**: several country ASRs appear at two decimals in running text
  (e.g. Lebanon 828.25) but one decimal in Table 1 (828.3); the regional prevalence-change UI upper
  bound differs (text 6.3 vs Table 1 6.2). Both captured verbatim.
- **C-c — Interpretive vs evidential**: risk-factor attributions (smoking/CVD/alcohol decline, ApoE4,
  cognitive reserve) are drawn from the literature and offered as explanations; they are NOT tested by
  this study's data and are kept in claim `Interpretation` fields, not `Statement`s.
- **C-d — No causal inference**: all findings are descriptive/associational; the study estimates
  burden and trends, not causes of the observed decline.
