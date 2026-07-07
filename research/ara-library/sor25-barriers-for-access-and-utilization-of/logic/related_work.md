# Related Work — Typed Dependency Graph

Type legend: `imports` (uses directly), `extends` (builds on/updates), `bounds` (defines methodological limits), `baseline` (comparator/data source), `refutes`. Full `RW` blocks are given for works with a specific technical delta (methodology tools, prior reviews found via reference mining, and the primary-study evidence corpus); brief grouped entries below preserve the paper's full 125-reference footprint.

## RW01: Liberati A, Altman DG, Tetzlaff J, et al. — PRISMA Statement (ref 33)
- **DOI**: Not stated in paper.pdf (J Clin Epidemiol. 2009;62(10):e1–34)
- **Type**: imports
- **Delta**:
  - What changed: Provides the reporting/methodology backbone this review follows in full — the identification → screening → eligibility → inclusion flow (Fig. 1) and structured reporting of exclusion reasons at each stage.
  - Why: Ensures a transparent, reproducible, bias-minimizing systematic review process (explicitly cited as a review "strength").
- **Claims affected**: C01, C02
- **Adopted elements**: PRISMA flow-diagram structure; staged screening/exclusion reporting.

## RW02: Rayyan (ref 34) — Intelligent Systematic Review screening tool
- **DOI**: Not applicable (software; https://www.rayyan.ai)
- **Type**: imports
- **Delta**:
  - What changed: Used by the five reviewers to independently tag articles, apply inclusion/exclusion criteria, remove duplicates, and perform blind title/abstract screening — enabling systematic handling of the 1748+4 initially identified records down to 1202 unique records.
  - Why: Cited as adding "significant value to the review process," enabling efficient large-volume screening while minimizing errors/inconsistencies.
- **Claims affected**: C01
- **Adopted elements**: Duplicate removal; blind independent screening workflow.

## RW03: Hong QN, Fàbregues S, Bartlett G, et al. — Mixed Methods Appraisal Tool (MMAT), 2018 revised version (ref 35)
- **DOI**: Not stated in paper.pdf (Educ Inform. 2018;34(4):285–91)
- **Type**: imports
- **Delta**:
  - What changed: Supplies the quality-appraisal instrument applied to all 29 included studies, producing the 0–100% scores in Table 3 and the design-specific criteria sets (qualitative/quantitative/mixed-methods).
  - Why: Enables comparative, design-appropriate quality assessment across a heterogeneous corpus (qualitative, quantitative, and mixed-methods studies).
- **Claims affected**: C03
- **Adopted elements**: MMAT scoring rules, including the "weakest component" rule for mixed-methods studies.

## RW04: Reference-mined prior systematic/narrative reviews (refs 36–38)
- **DOI**: Not stated in paper.pdf for refs 36/37; ref 38 (Duran-Kiraç et al., Dementia. 2022;21(2):677–700)
- **Type**: baseline
- **Delta**:
  - What changed: Three prior reviews — Phenwan et al. (narrative review of advance care planning initiation in dementia, ref 36), Khanassov & Vedel (family physician–case manager collaboration systematic mixed-studies review, ref 37), and Duran-Kiraç et al. (scoping review of health-care accessibility for ethnic-minority persons with dementia in Europe, ref 38) — were mined for their reference lists, yielding 4 additional included studies beyond the primary database search.
  - Why: Reference mining supplements database search recall, particularly for narrower prior reviews whose included studies may not have surfaced via the PICO search string.
- **Claims affected**: C01
- **Adopted elements**: 4 additional included studies (contributing to the 1202-unique-record pool prior to title/abstract screening).

## RW05: The 29 included primary studies — the review's evidence corpus (refs 39–67)
- **DOI**: See individual study citations in `evidence/tables/table3.md`
- **Type**: baseline / imports
- **Delta**:
  - What changed: This review's entire empirical evidence base — every barrier finding, study characteristic, and quality score reported in claims C03–C10 — is drawn from these 29 primary studies (qualitative interviews/focus groups, quantitative surveys, and mixed-methods designs), spanning 2013–2022 and multiple European countries.
  - Why: These are the row-level data the narrative synthesis (E03, E04) aggregates; none is individually a methodological dependency of the review itself, but collectively they constitute its findings.
- **Claims affected**: C03, C04, C05, C06, C07, C08, C09, C10
- **Adopted elements**: Per-study barrier categorisation, sample characteristics, quality scores (all transcribed verbatim into `evidence/tables/table3.md`).

## Brief citation footprint (no distinct technical delta beyond the above)

**Dementia burden / epidemiology / economic-burden background** (refs 1–8): Li et al. (trace elements & AD bibliometric/meta-analysis); Khan (population ageing risks/dilemmas); WHO (Global status report on the public health response to dementia, 2021 — source of the "14 million EU," "392 billion EUR/year," "~27,815 EUR per person," and "double by 2050" figures used in `logic/problem.md` O1–O2); Fox & Petersen (G8 dementia research summit); Somme et al. (GP clinical practices/difficulties managing AD in France); Pini et al. (needs-led framework for caregiving impact); Meijer et al. (economic costs of dementia in 11 European countries); Jönsson (personal economic burden of dementia in Europe).

**Prior barriers-to-care / service-utilization literature motivating the review** (refs 9–20): Weber et al. (service use by community-dwelling dementia patients, systematic review); Georges et al. (Alzheimer's Disease International dementia carer's survey); Mansfield et al. (PCP-perceived barriers to optimal dementia care, systematic review); Aminzadeh et al. (barriers/enablers to diagnosis and management in primary care); Koch & Iliffe (rapid appraisal of barriers to diagnosis/management in primary care); Brodaty et al. (why caregivers don't use services); Laparidou et al. (caregivers' interactions with health care services); Peel & Harding ("huge maze" — dementia carers' constructions of navigating services); Lloyd & Stirling (ambiguous gain — uncertain benefits of service use); Potter (factors associated with caregivers' use/non-use of support services); Innes et al. (dementia care provision in rural Scotland); Devoy & Simpson (help-seeking intentions for early dementia diagnosis, Ireland).

**Dementia diagnosis/management guidance and primary-care context** (refs 21–25): Prince et al. (World Alzheimer Report 2016); Boustani (challenge of supporting dementia care in primary care); 2020 Alzheimer's Disease Facts and Figures; Bernstein et al. (US provider practices survey, dementia assessment/management in primary care); Bergman et al. (dementia and comorbidities in primary care, scoping review).

**COVID-19 impact on dementia care** (refs 26–32): Lai et al. (COVID-19 in long-term care facilities); Flint et al. (COVID-19 effect on mental health care of older people, Canada); Sundström et al. (loneliness increases risk of all-cause dementia/AD); Wang et al. (dementia care during COVID-19); Borges-Machado et al. (effects of COVID-19 home confinement on dementia care); Altieri & Santangelo (psychological impact of COVID-19/lockdown on dementia caregivers); Carpinelli Mazzi et al. (isolation time, education, gender effects during COVID-19 lockdown on caregivers).

**Care fragmentation and integrated-care literature (Discussion, "Organisational barriers")** (refs 68–80): Frandsen et al.; Qayed & Muftah; Kaltenborn et al.; Walunas et al.; Pinheiro et al.; Kern et al.; Enthoven; Rodríguez et al.; McKay et al.; Joo & Liu; Stange; Sweeney et al.; Kodner — a body of health-services-research literature on care fragmentation's costs/outcomes and integrated-care remedies, cited to contextualise (not to supply data for) the organisational-barriers finding (C04).

**Caregiver/HCW education and training literature (Discussion, "Information and educational barriers")** (refs 81–88): Gaugler et al.; Lu et al.; Callahan et al.; Austrom et al.; Opfer & Pedder; Griffiths et al. (DCM EPIC trial); Gulla et al. (COSMOS); Cooper et al. — evidence that education/support interventions improve caregiver outcomes, and that HCW professional-development time/resources are themselves constrained.

**Stigma, cultural attitudes, and minority/ethnicity literature (Discussion, "Cultural and stigma-related barriers")** (refs 89–107): Cahill et al.; Urbańska et al.; Low & Purwaningrum; Mahoney et al.; Cations et al.; Alladi & Hachinski; Zeng et al.; Warren et al.; Haralambous et al.; Nielsen et al. (ref 98); Giebel et al. (ref 99); Mukadam et al. (refs 100, 107); Parveen et al.; Sagbakken et al. (refs 102, 104); Casas et al.; Giebel et al. (ref 105); Cooper et al. (ref 106) — supports the minority/migrant-specific barrier findings (C10) and the general stigma/cultural-attitudes framing.

**Rural/logistical care-access and continuity-of-care literature (Discussion, "Logistical barriers")** (refs 108–119): Morgan et al.; Cations et al. (INSPIRED study); Bauer et al.; Innes et al.; Crabtree-Ide et al.; Samsi et al.; Tang et al.; Hobfoll et al.; Alazri et al.; Houghton et al.; Risco et al.; Emilsson — literature on rural-service gaps, continuity of care, and cross-national care-provision models cited to interpret the logistical-barriers finding (C04, C09).

**European policy context (Discussion, "Policies")** (refs 120–125): European Commission (EU dementia initiatives); Alzheimer Europe (National Dementia Strategies; Glasgow Declaration 2014; Strategic Plan 2021–2025; Helsinki Manifesto); European Working Group of People with Dementia (EWGPWD) — cited to situate the review's findings within ongoing EU-level policy efforts, not as evidence inputs to any claim.

## Datasets and Clinical Trials (typed data dependencies)
Per `sources.yaml` (verified; do not re-verify): **no released dataset**, **no code**, and **no registered clinical trial** are associated with this review. `code: []`, `data: []`, `clinical_trials: []`.
- **Data dependency (type: baseline/imports, access: published literature)**: The evidence base is the 29 primary studies (refs 39–67) plus their extracted characteristics (Table 3), assembled by the reviewers into an Excel sheet (`sources.yaml`-external; not released — "No datasets were generated or analysed during the current study").
- **No PROSPERO ID, NCT ID, or software repository** appears anywhere in the paper's full text.
