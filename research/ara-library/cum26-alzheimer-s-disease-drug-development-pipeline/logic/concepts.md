# Concepts

Genuine technical terms used by the review (definitions from §2 Methods, §3, and the CADRO source).

## Disease-Targeting Therapy (DTT)
- **Notation**: DTT
- **Definition**: An agent whose declared therapeutic purpose is to impact a specific aspect of the
  pathophysiology of AD with the intention of delaying the onset of symptoms or slowing clinical
  decline (i.e., disease modification). DTTs are divided into **biologics** (monoclonal antibodies
  [MABs], vaccines, antisense oligonucleotides [ASOs], gene therapies, etc.) and **small molecules**
  (drugs typically taken orally and < 500 Daltons in molecular weight).
- **Boundary conditions**: Classification is based on declared purpose plus trial characteristics,
  literature, and sponsor information; it can be ambiguous for agents with multiple mechanisms, and
  a drug may have both DTT and STT properties. In 2026, 116 agents (73%) are DTTs.
- **Related concepts**: Symptom-Targeted Therapy (STT), CADRO, Mechanism of Action

## Symptom-Targeted Therapy (STT)
- **Notation**: STT
- **Definition**: An agent intended to improve symptoms present at baseline in the trial rather than
  to modify the underlying disease course. STTs are divided into those with putative
  **cognition-enhancing** properties and those intended to ameliorate **neuropsychiatric symptoms
  (NPS)** such as psychosis, agitation, or depression. A residual "other" STT category covers
  targets such as seizures.
- **Boundary conditions**: Same declared-intent ambiguity as DTT. In 2026, cognition-enhancing STTs
  are 18% of agents and NPS-targeting STTs are 10%.
- **Related concepts**: Disease-Targeting Therapy (DTT), Neuropsychiatric Symptoms (NPS)

## Common Alzheimer's Disease Research Ontology (CADRO)
- **Notation**: CADRO
- **Definition**: A standardized ontology (developed by NIA/Alzheimer's Association) of AD
  pathophysiological target processes used to classify each agent's mechanism. Its categories
  include: amyloid-beta protein (Aβ); tau; apolipoprotein E (APOE), lipids and lipoprotein
  receptors; transmitter receptors; neurogenesis; inflammation and immune dysfunction; oxidative
  stress; cell death; proteostasis/proteinopathies; metabolism and bioenergetics; vascular factors;
  growth factors and hormones; synaptic plasticity/neuroprotection; gut–brain axis; circadian
  rhythm; environmental factors; epigenetic regulators; multitarget; unknown target; and "other".
- **Boundary conditions**: Within each category an agent can have one or several specific mechanisms
  of action. 17 of the categories are represented in the 2026 pipeline. Assignments derive from
  ClinicalTrials.gov, the literature, and ALZFORUM.
- **Related concepts**: Mechanism of Action (MoA), DTT, STT

## Mechanism of Action (MoA)
- **Notation**: MoA
- **Definition**: The specific molecular/pharmacological action by which an agent is proposed to
  affect a CADRO target process (e.g., "anti-amyloid monoclonal antibody specific for the
  pyroglutamate form of Aβ", "phosphodiesterase 5 (PDE-5) inhibitor"). Multiple MoAs can fall under
  a single CADRO category.
- **Boundary conditions**: MoAs presented in Tables 1–3 are derived from ClinicalTrials.gov or from
  review of the literature and informational websites such as ALZFORUM.
- **Related concepts**: CADRO, DTT, STT

## Repurposed drug
- **Notation**: —
- **Definition**: A drug approved for a non-AD indication, or repositioned during development from
  another indication, that is being tested in AD. Repurposing status is determined by comparing
  pipeline agents against the available version of DrugBank.
- **Boundary conditions**: 56 agents (35% of pipeline drugs) are repurposed in 2026; the definition
  covers drugs "approved for another indication or repositioned during development".
- **Related concepts**: DrugBank, DTT, STT

## Index Date
- **Notation**: —
- **Definition**: The fixed reference date (1 January 2026 for this review) on which the pipeline is
  censused. Trials reaching their completion date before the Index Date, or initiated/registered
  after it, are excluded; only trials active on the Index Date are included in the summaries.
- **Boundary conditions**: Enables year-over-year comparison across the annual review series
  (previous Index Date: 1 January 2025).
- **Related concepts**: Active trial, Longitudinal pipeline review

## Active trial
- **Notation**: —
- **Definition**: A trial identified as active on the Index Date, including those labeled recruiting,
  active-not-recruiting, enrolling by invitation (e.g., open-label extensions limited to prior-trial
  participants), and not-yet-recruiting (registered but no participants enrolled yet).
- **Boundary conditions**: Trials that are suspended, terminated, completed, withdrawn, or of unknown
  status (defined as no status update within the past 2 years) are described in the report but are
  NOT included among the active trial summaries and calculations.
- **Related concepts**: Index Date, Long-term extension trial

## Biomarker context of use
- **Notation**: —
- **Definition**: The role a biomarker plays in a trial: (1) **eligibility** — used to confirm AD
  diagnosis/pathology for enrollment; or (2) **primary outcome** — used as a pharmacodynamic
  endpoint to verify the mechanism of action. Modalities include imaging (amyloid PET, tau PET, MRI)
  and fluid biomarkers (CSF analytes, blood-based, saliva).
- **Boundary conditions**: 50% of trials use a biomarker for eligibility; 27% use one as a primary
  outcome. Amyloid PET is the most common eligibility modality (N=49).
- **Related concepts**: Biomarker, Pharmacodynamic outcome

## AD pathophysiological continuum
- **Notation**: —
- **Definition**: The staged progression of AD from cognitively unimpaired but biomarker-positive
  (preclinical), through MCI/prodromal AD, to early (MCI or mild), mild, moderate, and severe AD
  dementia. Trial populations are mapped onto this continuum.
- **Boundary conditions**: Population categories overlap and are not mutually exclusive, so trial
  counts across stages can exceed the number of active trials.
- **Related concepts**: Preclinical AD, MCI due to AD, AD dementia
