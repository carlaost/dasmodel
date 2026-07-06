# Experiments (Analysis Plans)

This is a survey/registry-analysis paper: an "experiment" is a **counting or classification
analysis** run over the ClinicalTrials.gov census, not a wet-lab or model experiment. Plans are
directional only; exact counts live in `evidence/`.

## E01: Enumerate the active pipeline and count by phase
- **Verifies**: C01, C03
- **Setup**:
  - Data source: ClinicalTrials.gov registry, accessed via its application programming interface
    (API); raw JSON parsed for >30 key data fields; loaded into a PostgreSQL relational database
    (UNLV Clinical Trial Observatory / Cleveland Clinic Laboratory of Network Medicine).
  - System: rule-based programming plus manual expert curation.
  - Reference point: Index Date 1 January 2026.
- **Procedure**:
  1. Query using AD-related search terms ("Alzheimer's disease", dementia of the Alzheimer type,
     prodromal AD, preclinical AD, MCI), excluding non-AD or mixed-dementia trials and device/gene/
     stem-cell/biomarker-only/Phase 0/Phase 4 trials.
  2. Retain only trials active on the Index Date (recruiting, active-not-recruiting, enrolling by
     invitation, not-yet-recruiting).
  3. For trials spanning two phases, assign the higher phase; count each novel agent once.
  4. Count trials and unique drugs overall and within Phase 1, Phase 2, Phase 3.
- **Metrics**: number of active trials; number of unique drugs; per-phase counts.
- **Expected outcome**: A finite active pipeline with the largest number of drugs and trials
  concentrated in Phase 2; a smaller Phase 3 set.
- **Baselines**: Prior Index Dates (annual review series) for comparison.
- **Dependencies**: none

## E02: Classify agents by therapeutic purpose (DTT/STT) and modality
- **Verifies**: C02
- **Setup**: Curated agent list from E01; declared trial purpose + literature + sponsor information.
- **Procedure**:
  1. For each agent, determine whether the declared intent is disease modification (DTT) or symptom
     targeting (STT).
  2. Sub-classify DTTs as biologic vs small molecule (<500 Da, oral) and STTs as cognition-enhancing
     vs NPS-targeting (vs "other").
  3. Tabulate counts and proportions overall and by phase (Figures 2, 4).
- **Metrics**: fraction of agents per therapeutic-purpose class.
- **Expected outcome**: DTTs are the majority; small-molecule and biologic DTTs together dominate
  over cognition-enhancing and NPS STTs.
- **Baselines**: none
- **Dependencies**: E01

## E03: Map agents onto CADRO pathophysiology categories
- **Verifies**: C07
- **Setup**: Curated agent list; CADRO ontology; mechanism data from ClinicalTrials.gov, literature,
  and ALZFORUM.
- **Procedure**:
  1. Assign each agent's mechanism of action to one (or "multitarget") CADRO category.
  2. Count agents per category, overall and by phase (Figure 3).
  3. Rank categories by number of agents.
- **Metrics**: number of CADRO categories represented; agents per category.
- **Expected outcome**: Many CADRO categories are represented; neurotransmitter receptors,
  inflammation/immune, and amyloid are the leading targets.
- **Baselines**: none
- **Dependencies**: E01

## E04: Sum required participants across active trials
- **Verifies**: C04
- **Setup**: Target enrollment field for each active trial from the registry.
- **Procedure**:
  1. Extract planned enrollment for every active trial.
  2. Sum overall and by phase; also aggregate by therapeutic purpose.
- **Metrics**: total required participants; per-phase and per-purpose totals and shares.
- **Expected outcome**: Total recruitment demand is dominated by Phase 3 trials.
- **Baselines**: none
- **Dependencies**: E01

## E05: Classify lead sponsor as industry vs non-industry
- **Verifies**: C05
- **Setup**: Lead-sponsor field per active trial.
- **Procedure**:
  1. Label each trial's lead sponsor as biopharmaceutical industry or not (non-industry = NIH/other
     federal, non-US governmental, advocacy, philanthropy, academia, public-private).
  2. Tabulate the industry share overall and by phase (and by DTT/STT modality).
- **Metrics**: fraction of trials sponsored by industry, overall and per phase.
- **Expected outcome**: Industry sponsors a majority of trials, with the highest share in Phase 3.
- **Baselines**: none
- **Dependencies**: E01

## E06: Identify repurposed agents against DrugBank
- **Verifies**: C06
- **Setup**: Curated agent list; the available version of DrugBank.
- **Procedure**:
  1. Compare each agent to DrugBank to determine whether it is approved for a non-AD indication or
     repositioned during development.
  2. Count repurposed agents and their trials; break down by phase and DTT/STT modality and by
     sponsor type.
- **Metrics**: fraction of drugs (and trials) that are repurposed.
- **Expected outcome**: A substantial minority of the pipeline is repurposed, concentrated in
  Phase 2 and among non-industry sponsors.
- **Baselines**: none
- **Dependencies**: E01

## E07: Longitudinal comparison across annual pipeline reviews
- **Verifies**: C08, C10
- **Setup**: The annual pipeline census series (Index Dates from 2016/2017 through 2026), each built
  with the same methodology.
- **Procedure**:
  1. Compare the current pipeline's trial and agent counts to prior years (Figure 5A).
  2. Track the percentage of the pipeline devoted to key CADRO target classes (amyloid, tau,
     inflammation/immune) over the decade (Figure 5B).
- **Metrics**: year-over-year trial/agent counts; annual target-class shares.
- **Expected outcome**: Trials and agents grow over the decade; amyloid's share declines while
  tau and inflammation/immune shares rise and converge toward amyloid's.
- **Baselines**: Prior years (2017 baseline).
- **Dependencies**: E01, E03

## E08: Audit biomarker use in active trials
- **Verifies**: C09
- **Setup**: Biomarker fields (eligibility criteria and outcome measures) per active trial.
- **Procedure**:
  1. For each trial, record whether a biomarker is required for eligibility and/or used as a
     primary outcome, and the modality (amyloid PET, tau PET, MRI, CSF, blood, saliva).
  2. Tabulate fractions of trials with a biomarker for eligibility and for primary outcome, overall
     and by phase.
- **Metrics**: fraction of trials using a biomarker for eligibility; fraction using one as a
  primary outcome; modality distribution.
- **Expected outcome**: Roughly half of trials use a biomarker for eligibility; a smaller fraction
  use one as a primary outcome, with amyloid PET the most common modality.
- **Baselines**: none
- **Dependencies**: E01
