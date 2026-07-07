# Claims

All numbers are copied exactly from the reviewed article's text/tables (paper.pdf). This is a targeted literature review, not an original data-collection study: every quantitative value is itself a result reported by one of the 81 reviewed source studies, extracted and (in a few cases, e.g., PPPM→PPPY) unit-converted by the review authors. All `**Sources**` entries below are tagged `[result]` because every number is a synthesized/extracted finding of the review, never a value the review authors themselves set as an input parameter.

## C01: Societal costs rise substantially and consistently with disease severity
- **Statement**: Total societal costs of AD/dementia typically increase by at least 50% between consecutive severity levels (abstract), and by at least 1.5x with progression from mild to more severe disease stages (moderate or severe) in community care settings, irrespective of region.
- **Status**: supported
- **Falsification criteria**: Disproved if a majority of the 81 reviewed studies showed societal costs flat or decreasing with increasing severity, or if the reported minimum fold-change across severity transitions were below 1.5x community-care studies.
- **Proof**: [E01]
- **Evidence basis**: Abstract and Results "Societal Costs" section state the ≥50%/≥1.5x pattern directly; Table 3 and Fig. 4 tabulate the underlying per-study cost-by-severity values and percentage changes.
- **Interpretation**: The direction (costs rise with severity) is highly consistent across studies, but the exact multiple varies widely by region, staging instrument, and care setting (see C04).
- **Dependencies**: none
- **Tags**: societal-cost, severity, trend
- **Sources**:
  - "societal costs of AD or dementia typically increased by at least 50% between consecutive severity levels" ← paper.pdf Abstract/Results «Findings consistently demonstrated that societal costs of AD or dementia typically increased by at least 50% between consecutive severity levels, increasing with disease progression» [result]
  - "societal costs typically increased by at least 1.5 × with progression from mild AD or dementia to more severe stages of disease... in community care settings" ← paper.pdf Results, "Societal Costs" (p.1804–1805) «Irrespective of region, studies demonstrated that societal costs typically increased by at least 1.5 × with progression from mild AD or dementia to more severe stages of disease (e.g., moderate or severe) in community care settings» [result]

## C02: Informal (indirect) caregiving is the largest single component of societal cost, especially in moderate-stage disease
- **Statement**: Informal/indirect caregiving costs often comprise close to half of total societal costs; in the subset of studies reporting a granular cost breakdown (n=6), informal caregiving exceeded 50% of total costs specifically in the moderate disease stage.
- **Status**: supported
- **Falsification criteria**: Disproved if the granular-breakdown studies (Fig. 5, n=6) showed informal caregiving below 50% of total cost in the moderate stage, or if informal care was not the largest single cost component across severities.
- **Proof**: [E02]
- **Evidence basis**: Plain Language Summary and Results state the ≥50% figure; Fig. 5 shows the "Informal caregiving" proportion (light blue, top segment) as the largest single component at every severity level, exceeding 0.50 of the stacked bar at the "Moderate" severity.
- **Interpretation**: Because informal caregiving is unpaid, it is often excluded or undervalued in conventional healthcare-cost accounting, making it the largest yet least visible component of AD's societal burden.
- **Dependencies**: none
- **Tags**: informal-care, caregiver-burden, cost-breakdown
- **Sources**:
  - "indirect costs attributed to unpaid, informal caregiving represented a large proportion of total costs, often reaching close to 50% of the total societal burden" ← paper.pdf Plain Language Summary (p.1798) «this review showed that indirect costs attributed to unpaid, informal caregiving represented a large proportion of total costs, often reaching close to 50% of the total societal burden, depending on stage of disease and region» [result]
  - "the informal or indirect cost of care formed the largest proportion of the total societal economic burden, especially in the moderate stage of the disease where it comprised > 50% of total costs [Fig. 5 (n = 6 studies)...]" ← paper.pdf Results, "Societal Costs" (p.1807) «Bringing the components of societal costing together, the informal or indirect cost of care formed the largest proportion of the total societal economic burden, especially in the moderate stage of the disease where it comprised > 50% of total costs [Fig. 5 (n = 6 studies), Figure S1]» [result]

## C03: MCI-stage economic burden is appreciable relative to mild AD despite sparse evidence
- **Statement**: Although few studies report MCI-stage costs, the reported burden is appreciable compared to mild AD; the largest single reported increase from MCI to mild AD was 126%, observed in a Finnish study.
- **Status**: supported
- **Falsification criteria**: Disproved if no study in the review reported an MCI-to-mild cost increase, or if the largest reported MCI-to-mild percentage increase were not 126%.
- **Proof**: [E01]
- **Evidence basis**: Table 3 shows Jetsonen et al. 2021 (Finland) MCI/very-mild societal cost of €16,448 rising to €37,184 at "mild" (median of two mild definitions) — consistent with a large percentage jump; the narrative directly states the 126% figure.
- **Interpretation**: Despite thin evidence, the magnitude of the MCI→mild jump in the one detailed study suggests substantial economic burden even before a formal AD diagnosis is reached.
- **Dependencies**: none
- **Tags**: MCI, early-stage, severity-transition
- **Sources**:
  - "a Finnish study showing the highest increase of 126%" (MCI to mild AD) ← paper.pdf Results, "Societal Costs" (p.1806–1807) «Within early stages, costs also commonly increased with progression from MCI to mild AD, with a Finnish study showing the highest increase of 126% [30]» [result]

## C04: Cost increase across severity varies substantially by region and by the staging instrument used
- **Statement**: Cost increases with severity vary widely by region (e.g., a fourfold jump from mild to severe AD in an Iranian study, the largest of any study reviewed) and by which dementia staging scale is used, with CDR-based studies showing 2.1–3.3-fold cost increases from mild to moderately severe/severe versus 1.4–2.0-fold in MMSE-based studies.
- **Status**: supported
- **Falsification criteria**: Disproved if the Iranian study's relative cost increase were not the largest reported, or if CDR-based and MMSE-based studies showed the same fold-range of cost increase.
- **Proof**: [E01, E06]
- **Evidence basis**: Results, "Societal Costs" (regional variability, Aajami 2019 four-fold finding) and Discussion, "By Disease Severity" (instrument-specific fold-change ranges); Fig. 4 visualizes percentage change per study grouped by region.
- **Interpretation**: Regional and instrument-driven variability limits direct numeric comparison across studies and motivates the review's decision not to force all studies onto one common severity scale (see logic/solution/study_design.md).
- **Dependencies**: none
- **Tags**: region, staging-instrument, variability
- **Sources**:
  - "The study by Aajami 2019 et al. [43], in Iran, demonstrated the highest relative increase in costs, with a four-fold jump from mild AD to severe AD" ← paper.pdf Results, "Societal Costs" (p.1807) «The study by Aajami 2019 et al. [43], in Iran, demonstrated the highest relative increase in costs, with a four-fold jump from mild AD to severe AD» [result]
  - "from mild to moderately severe or severe stages of AD, societal costs increased by 1.4 to 2.0 fold in studies assessing disease severity using the MMSE... and from 2.1 to 3.3 fold in studies assessing disease severity using the CDR" ← paper.pdf Results, "Societal Costs" (p.1807) «from mild to moderately severe or severe stages of AD, societal costs increased by 1.4 to 2.0 fold in studies assessing disease severity using the MMSE [5, 34, 35, 45, 46], from 2.1 to 3.3 fold in studies assessing disease severity using the CDR [30, 32, 47]» [result]
  - "Europe was the most widely represented region (n = 37)" ← paper.pdf Results, "Study Selection and Characteristics" (p.1805) «Of all studies, Europe was the most widely represented region (n = 37), followed by studies with a global focus (n = 15...), North America (n = 15), and Asia (n = 14)» [result]

## C05: Financial delinquency costs (scams) rise from mild to moderate AD, then fall in severe AD
- **Statement**: The UK-reported cost of scams increased by £194 per person per year (PPPY) from the mild AD stage (£37) to the moderate AD stage (£231), then fell to £6 PPPY in the severe stage.
- **Status**: supported
- **Falsification criteria**: Disproved if Table 5's UK scam-cost values for mild/moderate/severe AD were not £37/£231/£6 PPPY respectively, or if the mild-to-moderate increase were not £194.
- **Proof**: [E05]
- **Evidence basis**: Table 5 (UK Alzheimer's Report [20]) lists Scams as PPPY: Mild £37, Moderate £231, Severe £6; the Plain Language Summary states the £194 increase directly.
- **Interpretation**: This non-monotonic (rise-then-fall) pattern recurs across several of the "unique" burden categories in Table 5 (heating bills, police call-outs, reduced mobility) and is attributed in the Discussion to increased informal supervision/structural adaptation as disease progresses, which suppresses these specific behavioral-impact costs in the most severe stage.
- **Dependencies**: none
- **Tags**: financial-delinquency, scams, under-reported-cost
- **Sources**:
  - "The cost of financial scams increased by ₤194 from the mild-to-moderate AD stage" ← paper.pdf Plain Language Summary (p.1798) «The cost of financial scams increased by ₤194 from the mild-to-moderate AD stage» [result]
  - Scams PPPY: Mild £37, Moderate £231, Severe £6 ← paper.pdf Table 5 (p.1812) «Scams | PPPY | NR | £37 | £231 | £6 | NR» [result]

## C06: Public fiscal losses from AD are large across multiple measurement approaches
- **Statement**: Lifetime direct-tax loss attributable to AD (patient plus caregiver) in Germany ranged from €7783 to €28,142, and a separate microsimulation of the same German AD-affected cohort estimated a net incremental fiscal loss of €74,288 to government and social security (from reduced tax revenue/consumption and increased financial aid).
- **Status**: supported
- **Falsification criteria**: Disproved if the Martins et al. 2022 study's reported lifetime direct-tax-loss range were not €7783–€28,142, or if the separately reported net incremental government/social-security loss were not €74,288.
- **Proof**: [E05]
- **Evidence basis**: Table 5 reports "Direct taxes loss, patient and caregiver | Lifetime | €7783 to €28,142"; the Discussion/Results narrative separately reports the €74,288 net incremental loss figure from the same underlying Martins et al. 2022 [68] simulation study.
- **Interpretation**: These are two distinct fiscal-loss metrics from the same source study (lifetime direct tax loss vs. a broader net simulation-based incremental loss including financial aid and consumption effects) and should not be treated as the same quantity.
- **Dependencies**: none
- **Tags**: public-fiscal-loss, taxes, under-reported-cost
- **Sources**:
  - "Direct taxes loss, patient and caregiver | Lifetime | € 7783 to € 28,142" ← paper.pdf Table 5 (p.1812) «Direct taxes loss, patient and caregiver | Lifetime | € 7783 to € 28,142» [result]
  - "a simulation study, based on AD affected cohorts in Germany, estimated a net incremental loss of €74,288 to the government and social security" ← paper.pdf Results, "Caregiver Burden and Indirect Costs" (p.1814–1815) «A simulation study, based on AD affected cohorts in Germany, estimated a net incremental loss of €74,288 to the government and social security, due to lost taxes... and increased financial aid spent [68]» [result]

## C07: Weekly informal caregiving hours rise substantially with disease severity in both care settings
- **Statement**: In community care, average weekly informal caregiving hours increased by at least 1.4x from mild to more severe disease stages, ranging from 1–83 h/week in mild disease (23 studies) to 21–120 h/week in severe disease (25 studies); in institutional care, caregiving hours rose from up to 69 h/week (moderate) to up to 97 h/week (severe).
- **Status**: supported
- **Falsification criteria**: Disproved if the reported community-care mild/severe hour ranges were not 1–83/21–120 h per week, or if the institutional-care moderate/severe ranges were not up to 69/97 h per week.
- **Proof**: [E03]
- **Evidence basis**: Fig. 7 and its surrounding narrative report these exact ranges with per-bucket study counts (n).
- **Interpretation**: Even under institutional/formal care, families continue to provide substantial supplementary informal care, and this burden grows rather than disappears as disease severity increases.
- **Dependencies**: none
- **Tags**: caregiver-hours, informal-care, severity
- **Sources**:
  - "caregiving hours were reported to increase by at least 1.4 × from mild to more severe stages in community care settings, varying from 1 to 83 h per week in mild disease (23 studies) and 21 to 120 h per week in severe stages (25 studies)" ← paper.pdf Results, "Caregiver Burden and Indirect Costs" (p.1812–1813) «On average, caregiving hours were reported to increase by at least 1.4 × from mild to more severe stages in community care settings, varying from 1 to 83 h per week in mild disease (23 studies) and 21 to 120 h per week in severe stages (25 studies)» [result]
  - "informal caregiving hours per week also increased from up to 69 h per week in moderate dementia stages to up to 97 h per week in severe dementia stages" ← paper.pdf Results, "Caregiver Burden and Indirect Costs" (p.1813–1814) «In institutional care settings, informal caregiving hours per week also increased from up to 69 h per week in moderate dementia stages to up to 97 h per week in severe dementia stages (Fig. 7; Table S7)» [result]

## C08: Institutional care is direct-cost-dominated, unlike community care
- **Statement**: In institutional care settings, total direct costs exceed indirect costs and social (non-medical) care costs exceed medical care costs; a related systematic review found formal institutional caregiving increases total direct cost by up to 67.3% of overall AD economic burden.
- **Status**: supported
- **Falsification criteria**: Disproved if institutional-care studies in the review reported indirect costs exceeding direct costs, or if the cited related review's maximum reported direct-cost increase from institutional caregiving were not 67.3%.
- **Proof**: [E04]
- **Evidence basis**: Discussion, "By Care Setting" states institutional care "incurred larger total direct costs across regions than indirect costs in this care setting, where the cost of social care... superseded medical care costs," and cites a corroborating review's 67.3% figure.
- **Interpretation**: This care-setting asymmetry (direct-cost-dominated institutional care vs. indirect/informal-cost-dominated community care) is a structural feature of how AD cost is realized depending on who provides care.
- **Dependencies**: none
- **Tags**: care-setting, institutional-care, direct-cost
- **Sources**:
  - "institutional care incurred larger total direct costs across regions than indirect costs in this care setting, where the cost of social care (i.e., direct non-medical care) superseded medical care costs" ← paper.pdf Discussion, "By Care Setting" (p.1818) «However, institutional care incurred larger total direct costs across regions than indirect costs in this care setting, where the cost of social care (i.e., direct non-medical care) superseded medical care costs [37, 45, 65, 76, 77]» [result]
  - "formal caregiving in an institutional care setting caused an increase in the total direct cost of up to 67.3% of the overall economic burden of the disease" ← paper.pdf Discussion, "By Care Setting" (p.1818) «This is corroborated by a recent review, where formal caregiving in an institutional care setting caused an increase in the total direct cost of up to 67.3% of the overall economic burden of the disease [5]» [result]

## C09: Direct costs comprise at least one-third of total societal costs across disease stages
- **Statement**: Across the 8 studies reporting both societal and total direct costs, direct costs typically comprised at least one-third of total societal costs within each disease state, with direct costs comprising 31% to 52% of societal costs specifically in the mild stage of dementia.
- **Status**: supported
- **Falsification criteria**: Disproved if the direct-cost share of societal cost in the mild stage fell outside the 31–52% range across the cited studies, or if fewer than one-third was the typical direct-cost share in any disease state.
- **Proof**: [E02]
- **Evidence basis**: Results, "Direct Costs" states the 31–52% range for mild-stage studies and the "at least one-third" general finding, citing Fig. S2 for the n=8 study set.
- **Interpretation**: Even though informal/indirect costs are the single largest component (C02), direct costs remain a substantial, non-trivial share of the total societal burden at every stage.
- **Dependencies**: C02
- **Tags**: direct-cost, cost-breakdown, societal-cost
- **Sources**:
  - "direct costs typically comprised at least one-third of total societal costs within each disease state. For example, in the mild stages of dementia, direct costs comprised 31% to 52% of the societal costs" ← paper.pdf Results, "Direct Costs" (p.1806–1807) «However, direct costs typically comprised at least one-third of total societal costs within each disease state. For example, in the mild stages of dementia, direct costs comprised 31% to 52% of the societal costs [30, 35, 36, 47, 51, 54, 55]» [result]

## C10: Intangible (quality-of-life) costs move in opposite directions for patients versus caregivers as severity increases
- **Statement**: In the one study reporting intangible (QoL-loss) costs by AD severity, patient intangible costs rose from $1496 USD/month (PPPM) in MCI to $3196 USD/month in severe AD, while caregiver intangible costs fell from $1187 USD/month in mild AD to $769 USD/month in severe AD.
- **Status**: supported
- **Falsification criteria**: Disproved if the Monfared et al. 2024 study's reported patient intangible-cost PPPM values across MCI/mild/moderate/severe were not $1496/$1958/$1572/$3196, or if caregiver intangible-cost PPPM across mild/moderate/severe were not $1187/$994/$769.
- **Proof**: [E05]
- **Evidence basis**: Table 5 lists both series in full (Monfared 2024 [59]); the Results and Discussion narrative restate the endpoint values ($1496→$3196 for patients; $1187→$769 for caregivers).
- **Interpretation**: The authors attribute the patient-side increase to worsening mental/emotional strain as cognition declines, and the caregiver-side decrease to caregivers' adaptation/adjustment over time as disease progresses, though this is based on a single study and should not be generalized without further replication.
- **Dependencies**: none
- **Tags**: intangible-cost, quality-of-life, patient-caregiver-dyad
- **Sources**:
  - "intangible costs (e.g., losses in mental and emotional wellbeing) to patients were found to be higher in the more severe disease states [e.g., $1496 USD per month in patients with MCI compared to $3196 USD in patients with severe AD (Table 5)]" ← paper.pdf Results, "Caregiver Burden and Indirect Costs" (p.1813) «intangible costs (e.g., losses in mental and emotional wellbeing) to patients were found to be higher in the more severe disease states [e.g., $1496 USD per month in patients with MCI compared to $3196 USD in patients with severe AD (Table 5)] [59]» [result]
  - "intangible costs to caregivers decreased with disease severity (i.e., $1187 USD per month in mild AD compared to $769 USD per month in severe AD)" ← paper.pdf Results, "Caregiver Burden and Indirect Costs" (p.1813) «However, intangible costs to caregivers decreased with disease severity (i.e., $1187 USD per month in mild AD compared to $769 USD per month in severe AD) [59]» [result]
