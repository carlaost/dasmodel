# Claims

All claims are about the **composition and trajectory of the AD drug development pipeline** on the
Index Date of 1 January 2026, as counted from ClinicalTrials.gov. They are not claims about the
efficacy of any single drug. `**Sources**` cite the paper (`paper.pdf`) by section/table/figure with
the verbatim matched line; every value is a survey `[result]` (a count the review produced from the
registry).

## C01: Pipeline size on the Index Date
- **Statement**: On the Index Date of 1 January 2026, the active AD pipeline comprised 158 drugs
  being assessed in 192 clinical trials.
- **Status**: supported
- **Falsification criteria**: An enumeration of active AD trials on ClinicalTrials.gov as of
  1 January 2026, applying the paper's inclusion rules, that yields materially different counts of
  drugs or trials.
- **Proof**: [E01]
- **Evidence basis**: Tables 1–3 enumerate all agents by phase; §3.1 states the totals.
- **Interpretation**: The registry census is comprehensive but not exhaustive (non-US-only trials
  and irregular registrations may be under-captured — see constraints.md), so 158/192 is a lower
  bound on true global activity.
- **Dependencies**: none
- **Tags**: pipeline-size, census, index-date
- **Sources**:
  - 158 drugs ← paper.pdf §3.1 Overview «On the Index Date of January 1, 2026, we identified 192 clinical trials for AD assessing 158 drugs.» [result]
  - 192 trials ← paper.pdf §3.1 Overview «we identified 192 clinical trials for AD assessing 158 drugs» [result]

## C02: Composition by therapeutic purpose
- **Statement**: Of the agents in trials, 39% are small-molecule disease-targeting therapies (DTTs),
  34% are biologic DTTs, 18% are cognition-enhancing symptom-targeted therapies (STTs), and 10% are
  STTs developed to treat neuropsychiatric symptoms (NPS); DTTs account for 73% of drugs in
  development (116 DTTs).
- **Status**: supported
- **Falsification criteria**: A re-classification of the same agent set by therapeutic purpose that
  shifts these proportions substantially, or shows DTTs are not the majority class.
- **Proof**: [E02]
- **Evidence basis**: Abstract; §3.1; Figures 2 and 4 show phase-specific therapeutic-purpose splits.
- **Interpretation**: The pipeline is dominated by disease-modification intent; the DTT/STT split is
  a classification of *declared* therapeutic intent and can be ambiguous for multi-mechanism agents.
- **Dependencies**: C01
- **Tags**: DTT, STT, therapeutic-purpose, composition
- **Sources**:
  - 39% small-molecule DTTs, 34% biologic DTTs, 18% cognition-enhancing STTs, 10% NPS STTs ← paper.pdf Abstract «39% are small molecule disease targeting therapies (DTTs); 34% are biologic DTTs; 18% are cognition enhancing symptom targeted therapies (STTs); and 10% are STTs being developed to treat neuropsychiatric symptoms of AD.» [result]
  - 116 DTTs = 73% ← paper.pdf §3.1 Overview «There are 116 DTTs representing 73% of drugs in development; DTTs account for 134 (70%) of current clinical trials.» [result]

## C03: Distribution across trial phases
- **Statement**: The active pipeline is distributed across phases as 36 drugs in 54 Phase 3 trials,
  84 drugs in 89 Phase 2 trials, and 45 drugs in 49 Phase 1 trials.
- **Status**: supported
- **Falsification criteria**: A phase-by-phase count from the registry (higher phase used for
  trials spanning two phases; Phase 0/4 excluded) that disagrees with these figures.
- **Proof**: [E01]
- **Evidence basis**: §3.1; Table 1 (Phase 3), Table 2 (Phase 2), Table 3 (Phase 1).
- **Interpretation**: The bulge of drugs (84) and trials (89) in Phase 2 identifies Phase 2 as the
  "innovation engine" of the pipeline (per §4).
- **Dependencies**: C01
- **Tags**: phase-distribution, phase-1, phase-2, phase-3
- **Sources**:
  - 36 drugs / 54 Phase 3 trials, 84 / 89 Phase 2, 45 / 49 Phase 1 ← paper.pdf §3.1 Overview «This included 54 trials assessing 36 drugs in Phase 3; 89 trials assessing 84 drugs in Phase 2; and 49 trials assessing 45 drugs in Phase 1 (Figure 1).» [result]

## C04: Participant demand
- **Statement**: Currently active trials require 54,728 participants, of which 38,417 (70%) are
  needed for Phase 3, 13,961 (26%) for Phase 2, and 2,350 (4%) for Phase 1.
- **Status**: supported
- **Falsification criteria**: Summing the target enrollments of all active trials yields a
  materially different total or phase split.
- **Proof**: [E04]
- **Evidence basis**: Abstract; §3.7 Trial participants.
- **Interpretation**: Recruitment demand is concentrated in late-stage (Phase 3) trials, a
  bottleneck for pipeline throughput.
- **Dependencies**: C01, C03
- **Tags**: participants, recruitment, enrollment
- **Sources**:
  - 54,728 total; 38,417 Phase 3; 13,961 Phase 2; 2,350 Phase 1 ← paper.pdf §3.7 «To fully populate currently active trials, 54,728 participants are required: 38,417 in Phase 3; 13,961 in Phase 2; and 2,350 in Phase 1.» [result]
  - 70% Phase 3, 26% Phase 2, 4% Phase 1 ← paper.pdf §3.7 «Of the total number of required participants, 70% are needed for Phase 3, 26% are required for Phase 2, and 4% for Phase 1 trials.» [result]

## C05: Industry sponsorship
- **Statement**: The biopharmaceutical industry sponsors 113 (59%) of all AD trials, including 39
  (72%) of Phase 3 trials, 43 (48%) of Phase 2 trials, and 31 (63%) of Phase 1 trials.
- **Status**: supported
- **Falsification criteria**: Classifying lead sponsors of the active trials as industry vs
  non-industry gives a different sponsorship share, especially in Phase 3.
- **Proof**: [E05]
- **Evidence basis**: Abstract; §3.1; §3.10 Trial funders.
- **Interpretation**: Industry concentrates in late-stage, capital-intensive development; non-industry
  sponsors (NIH, academia, philanthropy) carry a larger share of early and repurposed programs.
- **Dependencies**: C01
- **Tags**: sponsorship, industry, funding
- **Sources**:
  - 113 (59%) all; 39 (72%) Phase 3; 43 (48%) Phase 2; 31 (63%) Phase 1 ← paper.pdf §3.1 «The biopharmaceutical industry sponsors 113 (59%) of all clinical trials in the current AD pipeline, including 39 (72%) Phase 3 trials; 43 (48%) Phase 2 trials; and 31 (63%) Phase 1 trials.» [result]

## C06: Repurposed drugs
- **Statement**: Repurposed agents (drugs approved or repositioned from a non-AD indication)
  represent 35% of drugs in trials — 56 repurposed agents in 73 trials (38% of all trials).
- **Status**: supported
- **Falsification criteria**: Comparing pipeline agents against DrugBank yields a materially
  different count of repurposed drugs.
- **Proof**: [E06]
- **Evidence basis**: Abstract; §3.9 Repurposed agents.
- **Interpretation**: Repurposing is a substantial development strategy, concentrated in Phase 2 and
  among non-industry sponsors (57% of the non-industry pipeline vs 16% of the industry pipeline).
- **Dependencies**: C01
- **Tags**: repurposing, drug-repositioning, drugbank
- **Sources**:
  - 35% of drugs; 56 agents; 73 trials; 38% of trials ← paper.pdf §3.9 «The 56 repurposed agents and 73 trials of repurposed drugs in the 2026 AD drug development pipeline represent 35% of the total number of drugs in trials and 38% of all trials.» [result]
  - 57% of non-industry pipeline; 16% of industry pipeline (Interpretation) ← paper.pdf §4 Discussion «Repurposing represents 16% of the industry pipeline and 57% of the non-industry pipeline.» [result]

## C07: CADRO mechanistic diversity
- **Statement**: 17 CADRO categories of AD pathophysiology are targeted by at least one drug;
  the most common targets are neurotransmitter receptors (38 drugs, 24%), inflammation/immune
  processes (28 drugs, 18%), amyloid-beta (25 drugs, 16%), and tau (15 drugs, 9%).
- **Status**: supported
- **Falsification criteria**: Re-mapping each agent's mechanism onto CADRO categories yields a
  different number of targeted categories or a different ranking/proportions of the top targets.
- **Proof**: [E03]
- **Evidence basis**: §3.1; Figure 3 (CADRO by phase); Tables 1–3 (per-agent CADRO column).
- **Interpretation**: The pipeline addresses a diverse array of pathophysiological processes, well
  beyond amyloid; category assignment reflects declared/literature-derived mechanism and can be
  ambiguous for multi-target agents.
- **Dependencies**: C01
- **Tags**: CADRO, mechanism-of-action, target-diversity
- **Sources**:
  - 17 categories targeted ← paper.pdf §3.1 «Seventeen of the CADRO categories of AD pathophysiology are targeted by at least one drug in current clinical trials.» [result]
  - 38 (24%) neurotransmitter receptors; 28 (18%) inflammation/immune; 25 (16%) Aβ; 15 (9%) tau ← paper.pdf §3.1 «Thirty-eight drugs (24%) in the pipeline target neurotransmitter receptors; 28 agents (18%) address inflammation/immune processes; 25 treatments (16%) target Aβ protein-related pathophysiology; 15 agents (9%) target tau-related processes» [result]

## C08: Pipeline growth
- **Statement**: The 2026 pipeline (192 trials / 158 drugs) expands on the 2025 pipeline (182 trials
  / 138 drugs); over the 2017–2026 decade the number of trials increased approximately 35% and the
  number of agents approximately 40%.
- **Status**: supported
- **Falsification criteria**: Year-over-year pipeline counts from the annual review series that
  contradict the 2025→2026 change or the decade-scale growth percentages.
- **Proof**: [E07]
- **Evidence basis**: §4 Discussion (2025 vs 2026); §3.5 and Figure 5A (2017–2026 trajectory).
- **Interpretation**: AD drug development is a growing enterprise despite the absence of new
  approvals since 2023 and high late-stage failure rates.
- **Dependencies**: C01
- **Tags**: longitudinal, growth, trajectory
- **Sources**:
  - 192 trials / 158 drugs (2026) vs 182 trials / 138 drugs (2025) ← paper.pdf §4 Discussion «The 192 clinical trials and 158 novel agents in the 2026 AD drug development pipeline expands on the 182 clinical trials assessing 138 drugs present in the 2025 pipeline.» [result]
  - ~35% more trials, ~40% more agents (2017–2026) ← paper.pdf §3.5 «The number of trials increased by approximately 35%, and the number of agents increased by approximately 40% during this interval (Figure 5A).» [result]

## C09: Biomarker integration
- **Statement**: 96 (50%) of the 192 active trials use a biomarker for eligibility, and 52 (27%)
  use a biomarker as a primary outcome measure.
- **Status**: supported
- **Falsification criteria**: Auditing biomarker use (eligibility vs outcome) across the active
  trials yields materially different fractions.
- **Proof**: [E08]
- **Evidence basis**: §3.6 Biomarkers in trials; §4 Discussion.
- **Interpretation**: Biomarkers have become central to AD trial design for both patient selection
  and pharmacodynamic readout; amyloid PET is the most common eligibility modality (N=49).
- **Dependencies**: C01
- **Tags**: biomarkers, eligibility, outcome, amyloid-PET
- **Sources**:
  - 96 (50%) inclusion biomarker for eligibility ← paper.pdf §3.6 «Among the 192 clinical trials, 96 (50%) have an inclusion biomarker for trial eligibility, with amyloid positron emission tomography (PET) identified as the most common biomarker modality (N = 49).» [result]
  - 52 (27%) biomarker as primary outcome ← paper.pdf §3.6 «Fifty-two (27%) active AD trials have a biomarker as a primary outcome measure (nine in Phase 3, 32 in Phase 2, and 11 in Phase 1)» [result]

## C10: Longitudinal shift in target-class share
- **Statement**: Over 2017–2026 the share of the pipeline accounted for by amyloid-targeting agents
  fell from ~33% to ~20%, while inflammation/immune-dysfunction agents rose from ~6% to ~20% and
  tau-targeting agents rose from ~6% to ~20%.
- **Status**: supported
- **Falsification criteria**: The annual CADRO-share series shows amyloid not declining or
  inflammation/tau not rising to converge near amyloid's share by 2026.
- **Proof**: [E07]
- **Evidence basis**: §3.5; Figure 5B (percent of pipeline by target class, 2017–2026).
- **Interpretation**: The pipeline has diversified away from amyloid-centric development toward tau
  and neuroinflammation; the inflammation and amyloid shares have been stable since 2022.
- **Dependencies**: C07, C08
- **Tags**: longitudinal, amyloid, tau, inflammation, target-shift
- **Sources**:
  - inflammation/immune 6%→~20%; tau 6%→~20%; amyloid 33%→~20% ← paper.pdf §3.5 «the percentage of the pipeline devoted to inflammation/immune dysfunction drugs has increased from 6% to approximately 20%, tau targeted agents have increased from 6% to approximately 20%, and amyloid targeted agents have decreased from 33% to approximately 20% of the pipeline (Figure 5B).» [result]
