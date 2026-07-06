# Problem Specification

## Observations

### O1: A large and growing population lies on the AD continuum
- **Statement**: The number of affected individuals in the United States is projected to grow from
  46.7 million (biomarker-positive, no symptoms), 2.43 million (MCI), and 3.65 million (AD dementia)
  in 2017 to 75.68 million (biomarker-positive without symptoms), 5.7 million (MCI), and 9.3 million
  (AD dementia) in 2060; approximately 90 million persons in the US will have AD-type brain changes.
- **Evidence**: §1 Background (citing Brookmeyer et al. 2018).
- **Implication**: There is a large and expanding unmet therapeutic need spanning the continuum from
  preclinical (biomarker-positive) through MCI to AD dementia.

### O2: Approved therapy coverage is narrow
- **Statement**: Four mechanisms of action have been verified by therapeutic benefit in AD:
  cholinergic agents, an N-methyl-D-aspartate (NMDA) agent, anti-amyloid monoclonal antibodies, and
  a multi-transmitter antipsychotic for agitation. There are no disease-targeting therapies (DTTs)
  approved for preclinical AD or for moderate-to-severe AD dementia; no new classes of cognition-
  enhancing agents have been approved since 2004; and there are no treatments for non-agitation
  neuropsychiatric symptoms (psychosis, depression, apathy). There have been no new drug approvals
  for AD since 2023.
- **Evidence**: §1 Background; §4 Discussion.
- **Implication**: Large mechanistic and continuum-stage gaps remain despite recent DTT/STT progress.

### O3: ClinicalTrials.gov captures the active pipeline
- **Statement**: On the Index Date of 1 January 2026, 158 drugs were being assessed in 192 active AD
  clinical trials registered on ClinicalTrials.gov.
- **Evidence**: §3.1 Overview; Abstract; Tables 1–3.
- **Implication**: The public registry is a comprehensive (though not exhaustive) resource for
  characterizing the state of AD drug development.

### O4: The pipeline is expanding
- **Statement**: The 2026 pipeline (192 trials / 158 drugs) expands on the 2025 pipeline (182 trials
  / 138 drugs). The number of trials has increased ~35% and the number of agents ~40% over 2017–2026.
- **Evidence**: §3.5 Longitudinal observations; §4 Discussion; Figure 5A.
- **Implication**: AD drug development is a robust and growing enterprise despite high late-stage
  failure rates.

## Gaps

### G1: No standardized, mechanistically-organized census of the active pipeline
- **Statement**: Stakeholders planning, conducting, and analyzing AD trials lack a single up-to-date,
  mechanistically-classified view of every active agent, its target process, phase, sponsor,
  biomarker use, geography, and participant demand.
- **Caused by**: O3 (raw registry data are unstructured), O4 (a fast-moving target).
- **Existing attempts**: Prior annual pipeline reviews by the same group (2024, 2025) established the
  methodology; ALZFORUM and DrugBank provide supporting mechanistic/repurposing information.
- **Why they fail**: Registry entries are heterogeneous and irregular; without curation and a
  common ontology they cannot answer composition/trajectory questions.

### G2: Unmet need across mechanisms and continuum stages is not quantified
- **Statement**: It is unclear how development effort is distributed across pathophysiological
  targets, disease stages, therapeutic purposes, and sponsors — information needed to judge whether
  the pipeline addresses the diversity of AD pathophysiology and the full continuum.
- **Caused by**: O1, O2.
- **Existing attempts**: Individual trial registrations and company disclosures.
- **Why they fail**: They give no aggregate, comparable, longitudinal picture.

## Key Insight
- **Insight**: A curated annual census of ClinicalTrials.gov, in which every active AD agent is
  classified by therapeutic purpose (DTT vs STT) and by Common Alzheimer's Disease Research Ontology
  (CADRO) mechanistic category on a fixed Index Date, converts the unstructured registry into a
  quantitative, longitudinally comparable map of the entire pipeline.
- **Derived from**: O3, O4, G1, G2.
- **Enables**: Reporting the pipeline's composition (counts/percentages by phase, mechanism, sponsor,
  geography, biomarker use, repurposing) and its 10-year trajectory to inform trial planning.

## Assumptions
- A1: ClinicalTrials.gov registration is a valid, reasonably comprehensive proxy for the active AD
  pipeline (US trials are mandated to register; non-US-only trials may be under-captured).
- A2: The declared therapeutic intent, sponsor, and mechanism on the registry (supplemented by
  literature and ALZFORUM) correctly reflect each agent's DTT/STT class and CADRO target.
- A3: An agent assessed in more than one phase is counted once (in totals of novel agents) using the
  higher phase; Phase 0 and Phase 4 trials are excluded.
- A4: "Active" status on the Index Date (recruiting, active-not-recruiting, enrolling by invitation,
  not-yet-recruiting) defines inclusion; suspended/terminated/completed/withdrawn/unknown trials are
  described but not counted among active summaries.
