# Experiments

These are declarative analysis plans reconstructed from the paper's Methods section. As a targeted literature review, its "experiments" are literature-synthesis analyses rather than lab experiments — no exact numerical results appear here (those live in `evidence/`).

## E01: Severity-stratified societal-cost extraction and cross-severity percentage-change calculation
- **Verifies**: C01, C03, C04
- **Setup**:
  - Corpus: 81 included studies (59 prospective/retrospective studies, 2 AD reports, 20 SLRs/meta-analyses) identified via the TLR search.
  - Data extraction form: study design, country, indication, price year, costing approach, definitions, economic components (predesigned form; single-reviewer extraction, independent-reviewer validation).
  - Severity harmonization: each study's reported severity categories mapped onto four common buckets (MCI/very mild, mild [incl. mild-to-moderate], moderate, severe [incl. moderately severe/severe, very severe]) regardless of underlying staging instrument (MMSE/CDR/FAST/GDS/DS).
- **Procedure**:
  1. For each study reporting cost broken down by severity, record the total societal cost at each available severity bucket, in the study's original currency and cost year.
  2. Where a cost is reported as a range within a severity bucket, take the median value.
  3. For studies with cost data at more than one severity level, compute the percentage change in cost when moving from one severity bucket to the next (MCI→mild, mild→moderate, moderate→severe).
  4. Group percentage-change results by region/country and by the severity-staging instrument used.
- **Metrics**: Percentage change in total societal cost between consecutive severity buckets (%); fold-change ratio between least and most severe buckets available per study.
- **Expected outcome**:
  - Societal costs increase, not decrease, when moving to a more severe bucket, in the large majority of studies.
  - The magnitude of increase is directionally larger in studies further along the severity spectrum and varies more by region (Europe) than by some other regions (Asia).
  - Studies using CDR-based staging show a directionally larger fold-change than MMSE-based studies.
- **Baselines**: None (descriptive synthesis across included studies; no comparator arm).
- **Dependencies**: none

## E02: Cost-component breakdown and proportional normalization by severity
- **Verifies**: C02, C09
- **Setup**:
  - Subset: studies reporting a granular breakdown of direct and indirect cost sub-components (informal caregiving, long-term care, medication, hospitalization, outpatient visits, transportation, etc.) regardless of care setting (n=6 studies per Fig. 5).
  - Data: per-component cost value per severity bucket per study.
- **Procedure**:
  1. For each study and severity bucket, divide each cost component's value by the total summed cost (all indirect + direct components) for that severity, producing a per-study proportion for each component.
  2. Normalize each component's reported proportion by dividing by the total sum of proportions reported across studies for that severity bucket.
  3. Aggregate normalized proportions into a stacked-bar representation per severity bucket (Fig. 5).
  4. Separately, for the subset of studies reporting both total direct costs and total societal costs (n=8, Fig. S2), compute the direct-cost share of societal cost per severity bucket.
- **Metrics**: Normalized proportion of each cost component within total societal cost, by severity bucket; direct-cost share (%) of total societal cost, by severity bucket.
- **Expected outcome**:
  - Informal caregiving occupies the largest normalized proportion of any single component at every severity bucket, with its share peaking around the moderate stage.
  - Direct costs occupy a smaller but still substantial (at least roughly a third) share of total societal cost at every severity bucket.
- **Baselines**: None (descriptive proportion synthesis).
- **Dependencies**: E01

## E03: Caregiver profile and weekly caregiving-hours synthesis
- **Verifies**: C07
- **Setup**:
  - Subset: studies reporting informal caregiver demographic/profile data (mean age, % spouse, % child, % female, % living with patient, % working for pay) and/or weekly informal caregiving hours, stratified by severity and care setting (community vs. mixed vs. institutional).
  - Aggregation rule: caregiver-profile metrics averaged across studies reporting each metric for each severity bucket; caregiving-hour ranges (min–max) captured per severity bucket via stacked bagplots, annotated with the number of contributing studies (n).
- **Procedure**:
  1. For each severity bucket and care-setting group, average the reported caregiver-profile metrics across all studies reporting that metric.
  2. For each severity bucket and care-setting group, record the lower and upper bound of reported weekly informal caregiving hours across contributing studies, and the count of contributing studies.
  3. Compare community-care vs. institutional-care caregiving-hour ranges across severity buckets.
- **Metrics**: Mean caregiver age, % spouse, % child, % female, % living with patient, % working for pay (per severity/care-setting group); range of weekly caregiving hours (h/week), with study count (per severity/care-setting group).
- **Expected outcome**:
  - Caregivers are predominantly older (near-retirement age), more often female, and frequently the patient's spouse or child, consistently across severity buckets.
  - Weekly caregiving-hour ranges shift upward (both lower and upper bound) as severity increases, in both community and institutional care settings.
- **Baselines**: None (descriptive cross-study synthesis).
- **Dependencies**: none

## E04: Care-setting comparison of cost structure (community vs. institutional)
- **Verifies**: C08
- **Setup**:
  - Subset: studies reporting costs specifically in institutional care settings (limited: only 1 of 81 studies was institutional-only) versus the larger set of community-care studies.
  - Comparison axis: relative magnitude of direct vs. indirect cost components within each care setting.
- **Procedure**:
  1. For institutional-care studies, tabulate total direct and total indirect (or total societal) costs by severity where available.
  2. Compare the relative share of direct vs. indirect costs within institutional care against the corresponding shares within community care (from E02).
  3. Cross-reference with an independent related systematic review's reported percentage increase in direct cost attributable to institutional/formal caregiving.
- **Metrics**: Direct-cost share vs. indirect-cost share of total cost, by care setting; percentage increase in direct cost attributable to formal/institutional caregiving (as reported by a related review).
- **Expected outcome**:
  - Institutional care shows a direct-cost-dominated structure (non-medical/social direct costs, in particular, exceeding medical costs), in contrast to the indirect/informal-cost-dominated structure of community care.
- **Baselines**: Community-care cost structure (from E02) serves as the implicit comparator.
- **Dependencies**: E02

## E05: Under-reported societal cost capture (financial delinquency, public fiscal loss, intangible QoL loss)
- **Verifies**: C05, C06, C10
- **Setup**:
  - Scope: cost categories explicitly targeted by this review's search strategy as typically absent from AD-specific cost-of-illness studies — financial delinquency (scams, missed payments, poor credit), other direct non-medical costs (police call-outs, additional heating bills, power of attorney, reduced-mobility costs), public fiscal loss (lost tax revenue, increased financial aid/support), and intangible quality-of-life loss.
  - Sources: primarily the UK Alzheimer's Society 2024 report [20], Martins et al. 2022 [68] (Germany fiscal microsimulation), Jia et al. 2018 [90] (China), and Monfared et al. 2024 [59] (US patient-caregiver dyad survey).
- **Procedure**:
  1. Extract each under-reported cost category's value (PPPY, PPPM, or lifetime, as reported) by severity bucket and region, where stratified.
  2. Compare each category's value across severity buckets to identify whether the category rises monotonically with severity or peaks/falls at a particular stage.
  3. Where two related fiscal-loss metrics exist from the same source study (e.g., lifetime tax loss vs. net incremental government/social-security loss), record both separately without conflating them.
- **Metrics**: Cost value per category, per severity bucket, per region, in the source's original currency/unit.
- **Expected outcome**:
  - Some under-reported non-medical costs (heating bills, police call-outs, reduced mobility, scams) peak in the mild-to-moderate stage and decline in the severe stage, rather than rising monotonically with severity.
  - Public fiscal losses (tax loss, financial aid) and intangible patient-side QoL costs are substantial and, where data exist, trend upward with severity; intangible caregiver-side QoL costs trend in the opposite direction (downward) with severity in the one study reporting this.
- **Baselines**: None (descriptive extraction of a specifically targeted, otherwise-underreported evidence base).
- **Dependencies**: none

## E06: Literature search and PRISMA screening validity/coverage check
- **Verifies**: C04
- **Setup**:
  - Search: MEDLINE + Embase, PRISMA-S guidelines, AD-specific search plus a secondary broader-dementia search; grey literature hand search (websites, organisations, citation searching) run in parallel.
  - Screening: title/abstract screening by a single reviewer against PICOS criteria (Table 1), full-text retrieval and eligibility assessment, second-reviewer selective QA check, third-reviewer adjudication on disagreement.
- **Procedure**:
  1. Deduplicate and screen all identified records (databases + grey literature) against PICOS inclusion/exclusion criteria.
  2. Retrieve and assess full texts of records passing title/abstract screening.
  3. Tabulate the count of records at each PRISMA stage (identified, duplicates removed, screened, excluded [with reason], sought for retrieval, assessed for eligibility, included) separately for the database and grey-literature streams, then combine into the final included-study count.
  4. Characterize the resulting included-study set by design type, care setting, and region (Fig. 3) to assess whether the final evidence base is skewed toward particular regions/settings.
- **Metrics**: Record counts at each PRISMA stage; count and proportion of included studies by region, care setting, and study design.
- **Expected outcome**:
  - The database search (AD-specific + broader-dementia) captures the large majority of eligible records, with grey literature contributing a small supplementary set.
  - The final included-study set is unevenly distributed across regions (more Europe-based studies than other regions) and care settings (predominantly community care), which should be considered when interpreting regional cost-variability findings (C04).
- **Baselines**: None (methodological/coverage check on the review's own evidence base).
- **Dependencies**: none
